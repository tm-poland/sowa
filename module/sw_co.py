#-*- coding: utf-8 -*-

import time
import threading

from module.sw_status import *
from module.sw_config import *
from module.sw_log import *
from module.sw_funkcje import *

class Co(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    self.running = True
    self.t_start = 0
    self.t_start2 = 0
    self.temp_tab = []
    
  def run(self):
    
    Log(2, 'Wątek sterowania CO został uruchomiony.')
    
    global config
    global status
    
    self.t_start = time.time() - config.co['t_petli']
    self.t_start2 = time.time() - config.co['czas_probek_temp']
    
    while self.running:
      
      if time.time() - self.t_start2 >= config.co['czas_probek_temp'] \
        and status.co['temp_zasilania'] > 0:
        self.t_start2 = time.time()
        self.temp_tab.append(status.co['temp_zasilania'])
        Log(3, "Do tablicy temperatur CO dodano " + str(status.co['temp_zasilania']))
        if len(self.temp_tab) > 10:
          self.temp_tab.pop(0)  
      
      
      if time.time() - self.t_start >= config.co['t_petli']:
        #print str(time.time() - self.t_start)
        self.t_start = time.time()
        
        #print "dochodzę 10 co"
        
        if status.co['temp_zasilania'] >= \
          config.co['temp_alarm']:  
          Wlacz('co', '1')
          continue
          
        if (status.co['temp_zasilania'] <= 0):
          Log(2, 'Wątek CO: czujnik temeratury zasilania CO <= 0')
          Wylacz('co', '10')
          continue 
          
        #print "dochodzę 8 co"
        if config.cwu ['wlaczone'] and config.cwu['priorytet'] == True \
          and config.co['gdy_priorytet_cwu'] == False:
          Wylacz('co', '3')
          continue
        
        #print "dochodzę 7 co"  
        if config.co['wygaszanie'] == True \
          and status.co['rozpalanie'] == False \
          and (status.co['temp_zasilania'] < config.co['temp_min']) \
          and (status.co['praca'] or status.co['wygaszanie']):
          WylaczWygaszanie('4')
          Wylacz('co', '4')
          continue
          
        #print "dochodzę 6 co"  
        
        if status.co['wygaszanie'] == False \
          and config.co['wygaszanie'] == False \
          and (status.co['temp_zasilania'] < (config.co['temp_start']- \
          config.co['histereza']/2)):
          Wylacz('co', '5')
          continue
        #print "dochodzę 5 co"  
        
        if config.co['rozpalanie'] == True \
          and (status.co['temp_zasilania'] >= config.co['temp_rozpalanie']):
          WylaczRozpalanie('6')
          Wlacz('co', '6')
          continue
        
        #print "dochodzę 4 co"   
        if status.co['rozpalanie'] == False and (status.co['temp_zasilania'] \
          >= (config.co['temp_start'] + config.co['histereza']/2)):
          Wlacz('co', '7')
          continue
    
        ##
        if config.co['rozpalanie'] and (status.co['praca'] == False) and (len(self.temp_tab) > 1):
          if (self.temp_tab[len(self.temp_tab) - 1] - self.temp_tab[0]) >= config.co['rozpalanie_delta']:
            Rozpalanie('8')
            continue
          else:
            WylaczRozpalanie('8')
            continue
            
        #print "dochodzę 2 co"      
        if config.co['wygaszanie'] and status.co['praca'] == True \
          and (status.co['temp_zasilania'] <= config.co['temp_wygaszanie']) \
          and (len(self.temp_tab) > 1):
          if (self.temp_tab[0] - self.temp_tab[len(self.temp_tab) - 1]) >= config.co['wygaszanie_delta']:
            Wygaszanie('9')
            continue
        
        if status.co['wygaszanie'] == True \
          and (status.co['temp_zasilania'] > config.co['temp_wygaszanie']):
          WylaczWygaszanie('10')
          Wlacz('co', '10')
          continue 
        

      else:
        time.sleep(1)
        
    Log(2, "Wątek sterowania CO kończy działanie.")
