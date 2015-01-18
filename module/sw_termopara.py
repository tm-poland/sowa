#-*- coding: utf-8 -*-

import time
import threading

from lib.max31855.max6675 import MAX6675, MAX6675Error
from module.sw_status import *
from module.sw_config import *
from module.sw_log import *


class Termopara(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    self.running = True
    self.t_start = 0
    
  def run(self):
    
    Log(2, 'Wątek termopary został uruchomiony.')

    global status
    
    thermocouple = MAX6675(config.termopara['gpio_cs'], \
      config.termopara['gpio_clock'], config.termopara['gpio_data'])
    
    self.t_start = time.time() - config.termopara['t_petli']
    
    while self.running:
      if time.time() - self.t_start >= config.termopara['t_petli']:
        self.t_start = time.time()
        
        if config.termopara['tylko_gdy_co'] == True \
          and config.co['wlaczone'] == False:
          Log(2, "Wątek termopary: warunek tylko_gdy_co działania nie został spełniony.")
          continue

        try:
          status.termopara['temp'] = thermocouple.get()
        except MAX6675Error as e:
          Log(1, "Wątek termopary: błąd odczytu temperatury, ") + e.value

      else:
        time.sleep(1)
    
    thermocouple.cleanup()    
    Log(2, "Wątek termopary kończy działanie.")
