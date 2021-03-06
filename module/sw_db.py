#-*- coding: utf-8 -*-

import MySQLdb 
import threading

from module.sw_status import *
from module.sw_config import *
from module.sw_log import *


class BazaDanych (threading.Thread):
  
  def __init__(self):
    threading.Thread.__init__(self)
    self.t_start = time.time()
    self.running = True
    self.db = None
    self.cur = None
    
  def run(self):
    
    Log(2, 'Wątek bazy danych MySQL został uruchomiony.')
    
    try:
      self.db = MySQLdb.connect(host=config.mysql['host'], user=config.mysql['user'], \
        passwd=config.mysql['pass'], db=config.mysql['db'])
      self.cur = self.db.cursor()
    except MySQLdb.Error, e:
      Log(0, "Błąd połączenia z bazą MySQL %d: %s" % (e.args[0], e.args[1]))
      self.running = False

    try:
      # ukrycie ostrzeżenia o istniejącej tabeli 
      self.cur.execute("SET sql_notes = 0;")
      
      self.cur.execute("CREATE TABLE IF NOT EXISTS historia ( \
        czas int(10) unsigned NOT NULL, \
        trwanie int(10) unsigned NOT NULL, \
        co_praca tinyint(1) unsigned NOT NULL, \
        co_rozpalanie tinyint(1) unsigned NOT NULL, \
        co_wygaszanie tinyint(1) unsigned NOT NULL, \
        co_temp_zasilania float(5,2) DEFAULT NULL, \
        co_temp_powrotu float(5,2) DEFAULT NULL, \
        cwu_praca tinyint(1) unsigned NOT NULL, \
        cwu_temp float(5,2) DEFAULT NULL, \
        ogrzewanie_podlogowe_praca tinyint(1) unsigned NOT NULL, \
        ogrzewanie_podlogowe_temp float(5,2) DEFAULT NULL, \
        cyrkulacja_praca tinyint(1) unsigned NOT NULL, \
        cyrkulacja_temp float(5,2) DEFAULT NULL, \
        grzalka_praca tinyint(1) unsigned NOT NULL, \
        temp float(5,2) DEFAULT NULL, \
        temp_wew float(5,2) DEFAULT NULL, \
        temp_zew float(5,2) DEFAULT NULL, \
        termopara_temp float(6,2) DEFAULT NULL, \
        PRIMARY KEY (czas) \
        ) ENGINE=InnoDB")
      
      self.db.commit()
      
    except MySQLdb.Error as e:
      Log(0, "Błąd tworzenia tabeli (1) bazy danych MySQL %d: %s" % (e.args[0], e.args[1]))
      try:
        self.db.rollback()
      except MySQLdb.Error as e:
        Log(0, "Błąd tworzenia tabeli (2) bazy danych MySQL %d: %s" % (e.args[0], e.args[1]))


    while self.running:
      if time.time() - self.t_start >= config.mysql['freq_zapisu']:
        self.t_start = time.time()
        
        try:
#           self.cur.execute("INSERT INTO historia VALUES ('%d', '%d', '%d', \
#             '%d', '%d', '%.2f', '%.2f', '%d', '%.2f', '%d', '%.2f', '%d', \
#             '%.2f', '%d', '%.2f', '%.2f', '%.2f', '%.2f')" \
#             %(time.time(), int(config.mysql['freq_zapisu']), \
#             int(status.co['praca']), int(status.co['rozpalanie']), \
#             int(status.co['wygaszanie']), status.co['temp_zasilania'], \
#             status.co['temp_powrotu'], int(status.cwu['praca']), \
#             status.cwu['temp'], int(status.ogrzewanie_podlogowe['praca']), \
#             status.ogrzewanie_podlogowe['temp'], \
#             int(status.cyrkulacja['praca']), status.cyrkulacja['temp'], \
#             int(status.grzalka['praca']), status.general['temp'], \
#             status.general['temp_wew'], status.general['temp_zew'], \
#             status.termopara['temp']))
            
          self.cur.execute("INSERT INTO historia VALUES (" \
            + ("'%d', " % (time.time())) \
            + ("'%d', " % (int(config.mysql['freq_zapisu']))) \
            + ("'%d', " % (int(status.co['praca']))) \
            + ("'%d', " % (int(status.co['rozpalanie']))) \
            + ("'%d', " % (int(status.co['wygaszanie']))) \
            + ("'%.2f', " % (status.co['temp_zasilania']) if status.co['temp_zasilania'] != None else "NULL") \
            + ("'%.2f', " % (status.co['temp_powrotu']) if status.co['temp_powrotu'] != None else "NULL") \
            + ("'%d', " % (int(status.cwu['praca']))) \
            + ("'%.2f', " % (status.cwu['temp']) if status.cwu['temp'] != None else "NULL") \
            + ("'%d', " % (int(status.ogrzewanie_podlogowe['praca']))) \
            + ("'%.2f', " % (status.ogrzewanie_podlogowe['temp']) if status.ogrzewanie_podlogowe['temp'] != None else "NULL") \
            + ("'%d', " % (int(status.cyrkulacja['praca']))) \
            + ("'%.2f', " % (status.cyrkulacja['temp']) if status.cyrkulacja['temp'] != None else "NULL") \
            + ("'%d', " % (int(status.grzalka['praca']))) \
            + ("'%.2f', " % (status.general['temp']) if status.general['temp'] != None else "NULL") \
            + ("'%.2f', " % (status.general['temp_wew']) if status.general['temp_wew'] != None else "NULL") \
            + ("'%.2f', " % (status.general['temp_zew']) if status.general['temp_zew'] != None else "NULL") \
            + ("'%.2f'" % (status.termopara['temp']) if status.termopara['temp'] != None else "NULL") \
            + ")")
          
          self.db.commit()
          
        except MySQLdb.Error as e:
          Log(0, "Błąd polecenia (1) bazy danych MySQL %d: %s" % (e.args[0], e.args[1]))
          try:
            self.db.rollback()
          except MySQLdb.Error as e:
            Log(0, "Błąd polecenia (2) bazy danych MySQL %d: %s" % (e.args[0], e.args[1]))
          
      time.sleep(1)
      
    self.cur.close()
    self.db.close()
    Log(2, 'Wątek połączenia z bazą danych MySQL kończy działanie.')
    
