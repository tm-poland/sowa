#-*- coding: utf-8 -*-

import time
import threading

from module.sw_status import *
from module.sw_config import *
from module.sw_log import *
from module.sw_funkcje import *

class Cwu(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    self.running = True
    self.t_start = 0
    
  def run(self):
    
    Log(2, 'Wątek sterowania CWU został uruchomiony.')
    
    global config
    global status
    
    self.t_start = time.time() - config.cwu['t_petli']
    
    while self.running:
      if time.time() - self.t_start >= config.cwu['t_petli']:       
        self.t_start = time.time()
        
        if status.co['temp_zasilania'] >= \
          config.cwu['temp_alarm']:  
          Wlacz('cwu', '1')
          continue
        
        if (status.co['temp_zasilania'] <= 0) \
          or (status.cwu['temp'] <= 0):
          Log(2, 'Wątek CWU: czujnik temeratury zasilania CO lub CWU <= 0')
          Wylacz('cwu', '3')
          continue
          
        if status.co['temp_zasilania'] < config.cwu['temp_min_co']:
          Wylacz('cwu', '4')
          continue 
          
        if config.cwu['gdy_rozpalanie'] == False \
          and status.co['rozpalanie'] == True:
          Wylacz('cwu', '5')
          continue
        
        if status.co['temp_zasilania'] <= status.cwu['temp']:
          Wylacz('cwu', '6')
          continue
        
        if status.cwu['temp'] >= (config.cwu['temp_max'] + \
          config.cwu['histereza']/2):
          Wylacz('cwu', '7')
          continue   
      
        if (status.cwu['temp'] <= (config.cwu['temp_max'] \
          - config.cwu['histereza']/2)) \
          and (status.co['temp_zasilania'] >= (status.cwu['temp'] \
          + config.cwu['histereza']/2)):
          Wlacz('cwu', '8')
          continue
        
      else:
        time.sleep(1)
        
    Log(2, "Wątek sterowania CWU kończy działanie.")
