#-*- coding: utf-8 -*-

import time
import threading

from module.sw_status import *
from module.sw_config import *
from module.sw_log import *
from module.sw_funkcje import *

class Cyrkulacja(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    self.running = True
    self.t_start = 0
    
  def run(self):
    
    Log(2, 'Wątek sterowania cyrkulacją został uruchomiony.')
    
    global config
    global status
    
    self.t_start = time.time() - config.cyrkulacja['t_petli']
    
    while self.running:
      if time.time() - self.t_start >= config.cyrkulacja['t_petli']:

        self.t_start = time.time()
        
        if status.co['temp_zasilania'] >= config.cyrkulacja['temp_alarm']:  
          Wlacz('cyrkulacja', '1')
          continue
        
        if (status.cwu['temp'] <= 0) \
          or (status.cyrkulacja['temp'] <= 0):
          Log(2, 'Wątek cyrkulacji: czujnik temeratury CWU lub cyrkulacji <= 0')
          Wylacz('cyrkulacja', '7')
          continue 
        
        if status.cyrkulacja['temp'] >= \
          (config.cyrkulacja['temp_max'] + config.cyrkulacja['histereza']/2):
          Wylacz('cyrkulacja', '3')
          continue   
        
        if status.cyrkulacja['temp'] >= status.cwu['temp']:
          Wylacz('cyrkulacja', '4')
          continue
        
        if config.cyrkulacja['manual'] \
          and (status.cyrkulacja['temp'] <= \
          (config.cyrkulacja['temp_max'] - config.cyrkulacja['histereza']/2)) \
          and ((status.cyrkulacja['temp'] + config.cyrkulacja['histereza']/2) \
          <= status.cwu['temp']):
          Wlacz('cyrkulacja', '6')
          continue  
      
        # test czy cyrkulacja zostala w tym przejsciu petli wlaczona
        # jezeli to znaczy ze powinna zostac wylaczona
        test = False
        
        if config.cyrkulacja["harmonogram_wlaczony"] \
          and ((status.cyrkulacja['temp'] + config.cyrkulacja['histereza']/2) \
          <= status.cwu['temp']):
        
          for harm in config.cyrkulacja["harmonogram"]:
        
              localtime = time.localtime(time.time())
              
              if localtime >= harm['data_start'] and localtime <= harm['data_end']:
                if str(localtime.tm_wday + 1) in harm['dni']:
                                   
                  czas_start = time.strptime("%d-%d-%d " % \
                    (localtime.tm_mday, localtime.tm_mon, localtime.tm_year) + \
                    time.strftime("%H:%M", harm['data_start']), "%d-%m-%Y %H:%M")
                    
                  czas_end = time.strptime("%d-%d-%d " % \
                    (localtime.tm_mday, localtime.tm_mon, localtime.tm_year) + \
                    time.strftime("%H:%M", harm['data_end']), "%d-%m-%Y %H:%M")
                   
                  if localtime >= czas_start and localtime <= czas_end:
                  
                    test = True
                    if status.cyrkulacja['temp'] <= \
                      (config.cyrkulacja['temp_max'] - config.cyrkulacja['histereza']/2):
                      Wlacz('cyrkulacja', '5')
                    break
          
        if not test:
          Wylacz('cyrkulacja', '6')
          continue
        
      else:
        time.sleep(1)

    Log(2, "Wątek sterowania cyrkulacją kończy działanie.")
