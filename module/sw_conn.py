#-*- coding: utf-8 -*-

import threading
import RPi.GPIO as gpio

import time
import re
import hashlib
from types import BooleanType, IntType, LongType, FloatType

from module.sw_status import *
from module.sw_config import *
from module.sw_log import *
from module.sw_funkcje import ThreadsLoad


class BlinkLed(threading.Thread):
  def __init__(self):
      threading.Thread.__init__(self)
      self.running = True

  def run(self):  
    while self.running:
      gpio.output(config.general['dioda'], False)
      time.sleep(0.1)
      gpio.output(config.general['dioda'], True)
      time.sleep(0.1)
      

class Conn (threading.Thread): 
  def __init__(self, id, conn, ip, port):
    threading.Thread.__init__(self)
    self.conn = conn
    self.running = True
    self.id = id
    self.ip = ip
    self.port = port
    self.conntype = ""
    self.message = ""
    self.conn.settimeout(2.0)
    self.thBlink = BlinkLed()

  
  def val2str(self, v):
    if isinstance(v, (BooleanType)):
      if v == True:
        return 'True'
      else:
        return 'False'   
    elif isinstance(v, (IntType, LongType, FloatType)):
      return str(v)
    else:
      return v
    
  
  def ParseRev(self, data):  
    
    words = data.split(":")
    wartosc = ""
    
    if len(words) > 3:
      words.pop(0)
      words.pop(len(words) -1)
      
      try:    
        if words[0] == "general":
          wartosc = self.val2str(config.general[words[1]])
          
        elif words[0] == "co":
          wartosc = self.val2str(config.co[words[1]])
          
        elif words[0] == "cwu":
          wartosc = self.val2str(config.cwu[words[1]])
          
        elif words[0] == "ogrzewanie_podlogowe":
          wartosc = self.val2str(config.ogrzewanie_podlogowe[words[1]])
        
        elif words[0] == "cyrkulacja":
          if words[1] == "harmonogram":
            wartosc = config.parseHarmRev(config.cyrkulacja["harmonogram"])
          else:
            wartosc = self.val2str(config.cyrkulacja[words[1]])
            
        elif words[0] == "grzalka":
          if words[1] == "harmonogram":
            wartosc = config.parseHarmRev(config.grzalka["harmonogram"])
          else:
            wartosc = self.val2str(config.grzalka[words[1]])
        
        elif words[0] == "mysql":
          wartosc = self.val2str(config.mysql[words[1]])
          
        elif words[0] == "sqlite3":
          wartosc = self.val2str(config.sqlite3[words[1]])
        
        elif words[0] == "termopara":
          wartosc = self.val2str(config.termopara[words[1]])

        else:
          Log(1, 'Zdalna konfiguracja: zmienna config.' + \
            words[0] + '[' +words[1]+ '] nie istnieje (2)');
          return False 

      except NameError:
        Log(1, 'Zdalna konfiguracja: zmienna config.' + \
          words[0] + '[' +words[1]+ '] nie istnieje');
        return False
      
      return wartosc
      
    else:
      Log(3, 'Błąd zdalnego pobierania konfiguracji - niepełne dane '+data);
      return False

   
  def Parse(self, data):
    
    global config
    
    v = data.split("\n")
    if len(v) > 2:
      if len(v[1]) > 0:
        if v[1] == hashlib.md5(config.general['password']).hexdigest():
          Log(2, 'Zdalna konfiguracja: hasło poprawne.')
        else:
          Log(1, 'Błąd zdalnej konfiguracji: niepoprawne hasło: ' + v[1] \
            + ' != ' + hashlib.md5(config.general['password']).hexdigest())
          return 'BADPASSWORD'
      else:
          Log(1, 'Błąd zdalnej konfiguracji: puste hasło.')
          return 'BADPASSWORD'   
    else:
      Log(2, 'Błąd zdalnej konfiguracji: wiadomość niekompletna.')
      return False
    
    words = data.split("\n:")
    
    if len(words) > 2:
      words.pop(0)
      words.pop(len(words) -1)
      
      for word in words:
        record = word.split("=")
        if len(record) == 2:
          etykiety = record[0].split(".")
          if len(etykiety) == 2:
            try:
              
              record[0] = record[0].strip()
              record[1] = record[1].strip()
              
              if record[1].lower() in ('yes', 'true'):
                record[1] = True
              elif record[1].lower() in ('no', 'false'):  
                record[1] = False
              elif re.match(r'^\d+$', record[1]):
                record[1] = int(record[1])
              elif re.match(r'^\d+\.\d+$', record[1]):
                record[1] = float(record[1])
            
              if etykiety[0] == "general":
                config.general[etykiety[1]] = record[1]
              
              elif etykiety[0] == "co":
                config.co[etykiety[1]] = record[1]
              
              elif etykiety[0] == "cwu":
                config.cwu[etykiety[1]] = record[1]
              
              elif etykiety[0] == "ogrzewanie_podlogowe":
                config.ogrzewanie_podlogowe[etykiety[1]] = record[1]
              
              elif etykiety[0] == "grzalka":
                if etykiety[1] == "harmonogram":
                  config.grzalka[etykiety[1]] = config.parseHarm(record[1])
                else:
                  config.grzalka[etykiety[1]] = record[1]
              
              elif etykiety[0] == "cyrkulacja":
                if etykiety[1] == "harmonogram":
                  config.cyrkulacja[etykiety[1]] = config.parseHarm(record[1])
                else:
                  config.cyrkulacja[etykiety[1]] = record[1]
              
              elif etykiety[0] == "mysql":
                config.mysql[etykiety[1]] = record[1]
                
              elif etykiety[0] == "sqlite3":
                config.sqlite3[etykiety[1]] = record[1]
              
              elif etykiety[0] == "termopara":
                config.termopara[etykiety[1]] = record[1]
                
              else:
                Log(2, 'Błąd zdalnej konfiguracji - zmienna config.' + \
                  etykiety[0] + '[' +etykiety[1]+ '] nie isnieje (2)');
                return False 
              
              Log(1, 'Zdalna konfiguracja: ustawiono wartość config.' + \
                etykiety[0] + '[' +etykiety[1]+ '] = ' + str(record[1]));
                     
            except NameError:
              Log(2, 'Błąd zdalnej konfiguracji - zmienna config.' + \
                etykiety[0] + '[' +etykiety[1]+ '] = ' + str(record[1]) + \
                ' nie istnieje');
              return False
            
            if etykiety[1] == 'wlaczone':   
               Log(2, 'Zdalna konfiguracja: wątek ' + etykiety[0] + ' = ' + str(record[1]))
               ThreadsLoad()
          
          else:
            Log(2, 'Błąd zdalnej konfiguracji - brak wystarczającej ilości etykiet zmiennych');
            return False
        else:
          Log(2, 'Błąd zdalnej konfiguracji - brak zmiennych zdefiniowanych');
          return False
    
    else:
      Log(3, 'Błąd zdalnej konfiguracji - niepełne dane '+data);
      return False
  

  def run(self):
    
    global conn_threads
    self.thBlink.start()
    
    #Sending message to connected client
    #self.conn.send('SOWA1\r\n') #send only takes string
     
    #infinite loop so that function do not terminate and thread do not end.
    while self.running:
        
      #Receiving from client
      
      try:
        data = self.conn.recv(1024)
      except:
        Log(3, 'Czas oczekiwania na dane od ' + self.ip + ':' \
          + str(self.port)  + ' został przekroczony.')
        break
        
      if not data:
          break
      if data[:6] == "STATUS":
        reply = status.get(config)
        self.conn.sendall(reply)
        break
      elif data[:6] == "CONFIG" or self.conntype == "config":
        
        self.message += data
        
        if self.conntype != "config":
          self.conntype = "config"  
          Log(3, 'Klient rozpoczyna zdalną konfigurację.')

        if self.message[-4:] == "END.":
          
          v = self.Parse(self.message)
          
          if v == False:
            reply = "ERROR."
          elif v == 'BADPASSWORD':
            reply = "BADPASSWORD."
          else:
            reply = "OK."
            
          self.conn.sendall(reply)
          break
      
      elif data[:9] == "GETCONFIG" or self.conntype == "getconfig":
        
        self.message += data
        
        if self.conntype != "getconfig":
          self.conntype = "getconfig"  
          Log(3, 'Klient rozpoczyna zdalne pibieranie konfiguracji.' + self.message)

        if self.message[-4:] == "END.":
          rep = self.ParseRev(self.message)
          if rep != False:
            reply = rep
          else:
            reply = "ERROR."
          self.conn.sendall(reply)
          break
      elif data[:4] == "QUIT":
        reply = "END."
        self.conn.sendall(reply)
        break
      else:
        reply = "2 sekundy na cos konkretnego :)"
        self.conn.sendall(reply)
      #self.conn.close()
      #break
     
    #came out of loop
    Log(3, 'Polaczenie z ' + self.ip + ':' + str(self.port)  + ' zostalo zakonczone.')
    self.conn.close()
    self.thBlink.running = False
    self.thBlink.join()
    conn_threads.remove(self)
