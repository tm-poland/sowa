#-*- coding: utf-8 -*-

from lib.w1thermsensor.w1thermsensor import W1ThermSensor, NoSensorFoundError, SensorNotReadyError, UnsupportedUnitError

import threading
import time

from module.sw_status import *
from module.sw_config import *
from module.sw_log import *

class Czujniki (threading.Thread):
  
  def __init__(self):
    threading.Thread.__init__(self)
    self.sensor = None
    self.running = True
    self.t = 0
    
  def run(self):
    
    Log(2, 'Wątek odczytu czujników temperatury został uruchomiony.')
    
    global status
    
    try:
      self.sensor = W1ThermSensor()
    except NoSensorFoundError:
      Log(0, "System nie wykrył jakiegokolwiek czujnika temperatury!")
      self.running = False
    
    while self.running:

      for sensor in W1ThermSensor.get_available_sensors():
        
        try:
          self.t = sensor.get_temperature()
        except SensorNotReadyError:
          Log(0, "Czujnik %s nie jest jeszcze gotowy do odczytu tempertury." % (sensor.id))  
        
        Log(3, "Sensor %s zanotował temperaturę %.1f" % (sensor.id, self.t))
        
        if config.co['czujnik_temp_zasilania'] == sensor.id:
          status.co['temp_zasilania'] = self.t
        elif config.general['czujnik_temp'] == sensor.id:
          status.general['temp'] = self.t       
        elif config.general['czujnik_temp_wew'] == sensor.id:
          status.general['temp_wew'] = self.t
        elif config.general['czujnik_temp_zew'] == sensor.id:
          status.general['temp_zew'] = self.t  
        elif config.co['czujnik_temp_powrotu'] == sensor.id:
          status.co['temp_powrotu'] = self.t
        elif config.cwu['czujnik_temp'] == sensor.id:
          status.cwu['temp'] = self.t
        elif config.ogrzewanie_podlogowe['czujnik_temp'] == sensor.id:
          status.ogrzewanie_podlogowe['temp'] = self.t
        elif config.cyrkulacja['czujnik_temp'] == sensor.id:
          status.cyrkulacja['temp'] = self.t
        else:
          Log(3, "Brak sensora %s zdefiniowanego w pliku konfiguracyjnym" % (sensor.id))
          
    Log(2, 'Wątek odczytu czujników temperatury kończy działanie.')
      
      
