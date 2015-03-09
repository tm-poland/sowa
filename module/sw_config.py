#-*- coding: utf-8 -*-

import ConfigParser
import re
import time
import sys

from module.sw_status import *

class Config ():
  
  def __init__(self):
    self.general = {}
    self.mysql = {}
    self.cwu = {}
    self.cyrkulacja = {}
    self.grzalka = {} 
    self.co = {}
    self.ogrzewanie_podlogowe = {}
    self.termopara = {}
    
    self.hconfig = ConfigParser.ConfigParser()
  
  
  def parseHarm (self, data):
  
    szTempArray = data.split(";")
    data = []
    
    x = 0
    for harm in szTempArray:
      szData = re.findall('<\/*(.*?)>', harm)
       
      if len(szData) >= 2:
        dni = re.findall('(\d)\s*[,<]{1}', harm)
        
        if len(dni) > 0:
          data.append({})
          try:
            data[x]['data_start'] = time.strptime(szData[0], "%d-%m-%Y %H:%M")
            
            # poniżej dodaję 59 sekund do pełnej wartości minuty, inaczej ostatnie
            # 59 sekund byłoby poza harmonogramem np. do 23:59 <> do 23:59:59
            data[x]['data_end'] = time.strptime(szData[1]+':59', "%d-%m-%Y %H:%M:%S")
          except:
            print >> sys.stderr, time.strftime("%d-%m-%Y %H:%M:%S ") + \
              ("Podczas parsowania harmonogramu wystąpił błąd. Zakres %s zostanie pominięty. Należy sprawdzić poprawność dat, godzin, dni." \
              % harm)
            continue
              
          data[x]['dni'] = dni
          x += 1
    
    return data
    
  def parseHarmRev (self, data):
    
    sztemp = ""
    
    for harm in data:
      sztemp += "<" + time.strftime("%d-%m-%Y %H:%M", harm['data_start']) + ">"
      
      for dzien in harm['dni']:
        sztemp += str(dzien) + ","
      
      if len(harm['dni']) > 0: sztemp = sztemp[:-1]
      
      sztemp += "</" + time.strftime("%d-%m-%Y %H:%M", harm['data_end']) + ">;\n"
      
    if len(data) > 0: sztemp = sztemp[:-2]  
    
    return sztemp
  
  
  def ConfigSectionMap(self, section):
    
    dict1 = {}
    options = self.hconfig.options(section)
    
    for option in options:
      
      try:
        szTemp = self.hconfig.get(section, option)
        
        if option == 'gpio':
          arTemp = szTemp.split(',')
          dict1[option] = []
          if arTemp[0] != '':
            dict1[option] = []
            for v in arTemp:
              dict1[option].append(int(v.strip()))
        elif szTemp.lower() in ('yes', 'no', 'true', 'false'):
          dict1[option] = self.hconfig.getboolean(section, option)
        elif re.match(r'^\d+\.\d+$', szTemp):
          dict1[option] = self.hconfig.getfloat(section, option)
        elif re.match(r'^\d+$', szTemp) and option[:12] != 'czujnik_temp':
          dict1[option] = self.hconfig.getint(section, option)
        else:
          dict1[option] = self.hconfig.get(section, option)
        
        if dict1[option] == -1:
          print >> sys.stderr, time.strftime("%d-%m-%Y %H:%M:%S ") + \
            ("Brak wartości w pliku konfiguracyjnym dla opcji: %s" % option)
      except:
        print >> sys.stderr, time.strftime("%d-%m-%Y %H:%M:%S ") + \
          ("Podczas odczytu opcji %s w pliku konfiguracyjnym wystąpił wyjątek." \
          % option)
        dict1[option] = None
        
    return dict1
    
    
  def read(self):

    self.hconfig.read('./sowa.conf')
    
    self.cwu = self.ConfigSectionMap("cwu")
    self.grzalka = self.ConfigSectionMap("grzalka")
    self.cyrkulacja = self.ConfigSectionMap("cyrkulacja")
    self.general = self.ConfigSectionMap("general")
    self.mysql = self.ConfigSectionMap("mysql")
    self.sqlite3 = self.ConfigSectionMap("sqlite3")
    self.co = self.ConfigSectionMap("co")
    self.ogrzewanie_podlogowe = self.ConfigSectionMap("ogrzewanie_podlogowe")
    self.termopara = self.ConfigSectionMap("termopara")
    
    self.grzalka["harmonogram"] = self.parseHarm(self.grzalka["harmonogram"])
    self.cyrkulacja["harmonogram"] = self.parseHarm(self.cyrkulacja["harmonogram"])
    
   

status = Status()
config = Config()
conn_threads = []

thCzujniki = None
thTermopara = None
thCo = None
thCwu = None
thOgrzewaniePodlogowe = None
thCyrkulacja = None
thGrzalka = None
thDb = None
thDbSQLite3 = None

