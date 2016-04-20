#-*- coding: utf-8 -*-

import time
import threading

from module.sw_status import *
from module.sw_config import *
from module.sw_log import *
from module.sw_funkcje import *

class OgrzewaniePodlogowe(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    self.running = True
    self.t_start = 0
    
  def run(self):
    
    Log(2, 'Wątek sterowania ogrzewaniem podłogowym został uruchomiony.')
    
    global config
    global status
    
    self.t_start = time.time() - config.ogrzewanie_podlogowe['t_petli']
    
    while self.running:
      if time.time() - self.t_start >= config.ogrzewanie_podlogowe['t_petli']:

        self.t_start = time.time()
        
        if status.co['temp_zasilania'] >= \
          config.ogrzewanie_podlogowe['temp_alarm']:  
          Wlacz('ogrzewanie_podlogowe', '1')
          continue
        
        if (status.co['temp_zasilania'] == None) \
          or (status.ogrzewanie_podlogowe['temp'] == None):
          Log(2, 'Wątek ogrzewania podłogowego: brak odczytu z czujnika temeratury zasilania CO lub ogrzewania podłogowego')
          Wylacz('ogrzewanie_podlogowe', '7')
          continue 
        
          
        if config.cwu['wlaczone'] == True and config.cwu['priorytet'] == True \
          and config.ogrzewanie_podlogowe['gdy_priorytet_cwu'] == False \
          and status.cwu['praca'] == True:
          Wylacz('ogrzewanie_podlogowe', '3')
          continue
          
        if config.co['wlaczone'] == True \
          and config.ogrzewanie_podlogowe['gdy_rozpalanie'] == False \
          and status.co['rozpalanie'] == True:
          Wylacz('ogrzewanie_podlogowe', '4')
          continue
        
        if status.co['temp_zasilania'] < \
          (config.ogrzewanie_podlogowe['temp_min_co'] - \
          config.ogrzewanie_podlogowe['histereza']/2):
          Wylacz('ogrzewanie_podlogowe', '5')
          continue   
      
        if status.co['temp_zasilania'] >= \
          (config.ogrzewanie_podlogowe['temp_min_co'] \
          + config.ogrzewanie_podlogowe['histereza']/2):
          Wlacz('ogrzewanie_podlogowe', '6')
          continue
        
      else:
        time.sleep(1)
    
    Log(2, "Wątek sterowania ogrzewaniem podłogowym kończy działanie.")
