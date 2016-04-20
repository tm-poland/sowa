#-*- coding: utf-8 -*-

import time
import threading

from module.sw_status import *
from module.sw_config import *
from module.sw_log import *
from module.sw_funkcje import *

class Grzalka(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    self.running = True
    self.t_start = 0
    self.name = "grzalka"
    
  def run(self):
    
    Log(2, 'Wątek sterowania grzałką został uruchomiony.')
    
    global config
    global status
    
    self.t_start = time.time() - config.grzalka['t_petli']
    
    while self.running:
      if time.time() - self.t_start >= config.grzalka['t_petli']:

        self.t_start = time.time()
          
        if (status.cwu['temp'] == None):
          Log(2, 'Wątek grzałki: brak odczytu z czujnika temeratury CWU')
          Wylacz('grzalka', '8')
          continue 
        
        if config.grzalka['gdy_co'] == False and \
          ((status.co['praca'] and not status.co['wygaszanie']) \
          or status.co['rozpalanie']):
          Wylacz('grzalka', '2')
          continue

        if config.grzalka['gdy_cwu'] == False and status.cwu['praca']:
          Wylacz('grzalka', '3')
          continue   
  
        if (status.cwu['temp'] >= (config.grzalka['temp_max'] \
          + config.grzalka['histereza']/2)):  
          Wylacz('grzalka', '4')
          continue

        if config.grzalka['manual'] \
          and (status.cwu['temp'] < (config.grzalka['temp_max'] \
          - config.grzalka['histereza']/2)):
          Wlacz('grzalka', '5')
          continue
          

        # test czy grzalka zostala w tym przejsciu petli wlaczona
        test = False
        
        if config.grzalka["harmonogram_wlaczony"] \
          and (status.cwu['temp'] < (config.grzalka['temp_max'] \
          - config.grzalka['histereza']/2)):
        
          for harm in config.grzalka["harmonogram"]:
        
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
                    Wlacz('grzalka', '6')
                    break
          
        if not test:
          Wylacz('grzalka', '7')
          continue
        
      else:
        time.sleep(1)
    
    Log(2, "Wątek sterowania grzałką kończy działanie.")
