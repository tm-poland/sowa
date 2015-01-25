#-*- coding: utf-8 -*-

import sqlite3 
import threading

from module.sw_status import *
from module.sw_config import *
from module.sw_log import *


class DB_SQLite3 (threading.Thread):
  
  def __init__(self):
    threading.Thread.__init__(self)
    self.t_start = time.time()
    self.running = True
    self.db = None
    self.cur = None
    
  def run(self):
    
    Log(2, 'Wątek bazy danych SQLite3 został uruchomiony.')
    
    try:
      self.db = sqlite3.connect(config.sqlite3['db'])
      self.cur = self.db.cursor()
    except sqlite3.Error, e:
      Log(1, "Błąd połączenia z bazą: %s" % (e.args[0]))
      self.running = False

    try:
      self.cur.execute("CREATE TABLE IF NOT EXISTS historia ( \
        czas int(10) , \
        trwanie int(10) , \
        co_praca tinyint(1) , \
        co_rozpalanie tinyint(1) , \
        co_wygaszanie tinyint(1) , \
        co_temp_zasilania float(5,2), \
        co_temp_powrotu float(5,2), \
        cwu_praca tinyint(1) , \
        cwu_temp float(5,2), \
        ogrzewanie_podlogowe_praca tinyint(1) , \
        ogrzewanie_podlogowe_temp float(5,2), \
        cyrkulacja_praca tinyint(1) , \
        cyrkulacja_temp float(5,2), \
        grzalka_praca tinyint(1) , \
        temp float(5,2), \
        temp_wew float(5,2), \
        temp_zew float(5,2), \
        termopara_temp float(6,2), \
        PRIMARY KEY (czas) \
        )")

      self.db.commit()
      
    except sqlite3.Error as e:
      Log(1, "Błąd polecenia (1) tworzenia tabeli w bazie danych SQLite3: %s" % (e.args[0]))
      self.running = False
      
      try:
        self.db.rollback()
      except sqlite3.Error as e:
        Log(1, "Błąd polecenia (2) tworzenia tabeli w bazie danych SQLite3: %s" % (e.args[0]))


    while self.running:
      if time.time() - self.t_start >= config.sqlite3['freq_zapisu']:
        try:
          self.t_start = time.time()
          
          self.cur.execute("INSERT INTO historia VALUES ('%d', '%d', '%d', \
            '%d', '%d', '%.2f', '%.2f', '%d', '%.2f', '%d', '%.2f', '%d', \
            '%.2f', '%d', '%.2f', '%.2f', '%.2f', '%.2f')" \
            %(time.time(), int(config.sqlite3['freq_zapisu']), \
            int(status.co['praca']), int(status.co['rozpalanie']), \
            int(status.co['wygaszanie']), status.co['temp_zasilania'], \
            status.co['temp_powrotu'], int(status.cwu['praca']), \
            status.cwu['temp'], int(status.ogrzewanie_podlogowe['praca']), \
            status.ogrzewanie_podlogowe['temp'], \
            int(status.cyrkulacja['praca']), status.cyrkulacja['temp'], \
            int(status.grzalka['praca']), status.general['temp'], \
            status.general['temp_wew'], status.general['temp_zew'], \
            status.termopara['temp']))
            
          self.db.commit()
          
        except sqlite3.Error as e:
          Log(1, "Błąd polecenia (1) bazy danych SQLite3: %s" % (e.args[0]))
          try:
            self.db.rollback()
          except sqlite3.Error as e:
            Log(1, "Błąd polecenia (2) bazy danych SQLite3: %s" % (e.args[0]))
          
      time.sleep(1)
      
    self.db.close()
    Log(2, 'Wątek połączenia z bazą danych SQLite3 kończy działanie.')
    
