#-*- coding: utf-8 -*-

import RPi.GPIO as gpio

from module.sw_config import *
from module.sw_status import *
from module.sw_log import *


def ThreadsExit ():

  global status
  
  global thDb
  if thDb != None:
    try:
      if thDb.running == True:
        thDb.running = False
        thDb.join()
    except NameError:
      Log(0, 'Błąd: wątek bazy danych został wcześniej nieoczekiwanie zamknięty.')
    thDb = None
    
  global thDbSQLite3
  if thDbSQLite3 != None:
    try:
      if thDbSQLite3.running == True:
        thDbSQLite3.running = False
        thDbSQLite3.join()
    except NameError:
      Log(0, 'Błąd: wątek bazy danych SQLite3 został wcześniej nieoczekiwanie zamknięty.')
    thDbSQLite3 = None
  
  global thCzujniki
  if thCzujniki != None:
    try:
      if thCzujniki.running == True:
        thCzujniki.running = False
        thCzujniki.join()
    except NameError:
      Log(0, 'Błąd: wątek odczytu czujników temperatury został wcześniej nieoczekiwanie zamknięty.')
    thCzujniki = None

  global thTermopara
  if thTermopara != None:
    try:
      if thTermopara.running == True:
        thTermopara.running = False
        thTermopara.join()
    except NameError:
      Log(0, 'Błąd: wątek termopary został wcześniej nieoczekiwanie zamknięty.')
    thTermopara = None
    status.termopara['temp'] = 0.0

  global thGrzalka
  if thGrzalka != None:
    try:
      if thGrzalka.running == True:
        thGrzalka.running = False    
        thGrzalka.join()
        Wylacz('grzalka')
    except NameError:
      Log(0, 'Błąd: wątek grzałki został wcześniej nieoczekiwanie zamknięty.')
    thGrzalka = None
      
  global thCyrkulacja
  if thCyrkulacja != None:
    try:
      if thCyrkulacja.running == True:
        thCyrkulacja.running = False
        thCyrkulacja.join()
        Wylacz('cyrkulacja')
    except NameError:
      Log(0, 'Błąd: wątek cyrkulacji CWU został wcześniej nieoczekiwanie zamknięty.')
    thCyrkulacja = None
  
  global thOgrzewaniePodlogowe
  if thOgrzewaniePodlogowe != None:
    try:
      if thOgrzewaniePodlogowe.running == True:
        thOgrzewaniePodlogowe.running = False
        thOgrzewaniePodlogowe.join()
        Wylacz('ogrzewanie_podlogowe')
    except NameError:
      Log(0, 'Błąd: wątek ogrzewania podłogowego został wcześniej nieoczekiwanie zamknięty.')
    thOgrzewaniePodlogowe = None
      
  global thCwu
  if thCwu != None:
    try:
      if thCwu.running == True:
        thCwu.running = False
        thCwu.join()
        Wylacz('cwu')
    except NameError:
      Log(0, 'Błąd: wątek obiegu CWU został wcześniej nieoczekiwanie zamknięty.')
    thCwu = None
      
  global thCo
  if thCo != None:
    try:
      if thCo.running == True:
        thCo.running = False
        thCo.join()
        Wylacz('co')
    except NameError:
      Log(0, 'Błąd: wątek obiegu CO został wcześniej nieoczekiwanie zamknięty.')
    thCo = None  
  

def ThreadsLoad ():
  
  global status
  
  global thCzujniki
  if thCzujniki == None:
    from module.sw_czujniki import Czujniki
    thCzujniki = Czujniki()
    thCzujniki.start()

  global thTermopara
  if thTermopara == None:
    if config.termopara['wlaczone'] == True:
      from module.sw_termopara import Termopara
      thTermopara = Termopara()
      thTermopara.start()
  else:
    if config.termopara['wlaczone'] == False:
      try: 
        if thTermopara.running == True:
          thTermopara.running = False
          thTermopara.join()
          status.termopara['temp'] = 0.0
      except NameError:
        Log(0, 'Błąd: wątek termopary został wcześniej nieoczekiwanie zamknięty.')  
      thTermopara = None
              
  global thCo
  if thCo == None:
    if config.co['wlaczone'] == True:
      GPIOset ('relay', config.co['gpio'])
      GPIOset ('led', (config.co['dioda'], config.co['rozpalanie_dioda'], \
        config.co['wygaszanie_dioda']))
      from module.sw_co import Co
      thCo = Co()
      thCo.start()
  else:
    if config.co['wlaczone'] == False:
      try: 
        if thCo.running == True:
          thCo.running = False
          thCo.join()
          Wylacz('co')
      except NameError:
        Log(0, 'Błąd: wątek obiegu CO został wcześniej nieoczekiwanie zamknięty.')  
      thCo = None
  
  global thCwu
  if thCwu == None:
    if config.cwu['wlaczone'] == True:
      GPIOset ('relay', config.cwu['gpio'])
      GPIOset ('led', config.cwu['dioda'])
      from module.sw_cwu import Cwu
      thCwu = Cwu()
      thCwu.start()
  else:
    if config.cwu['wlaczone'] == False:
      try: 
        if thCwu.running == True:
          thCwu.running = False
          thCwu.join()
          Wylacz('cwu')
      except NameError:
        Log(0, 'Błąd: wątek obiegu CWU został wcześniej nieoczekiwanie zamknięty.')  
      thCwu = None

  global thOgrzewaniePodlogowe
  if thOgrzewaniePodlogowe == None:
    if config.ogrzewanie_podlogowe['wlaczone'] == True:
      GPIOset ('relay', config.ogrzewanie_podlogowe['gpio'])
      GPIOset ('led', config.ogrzewanie_podlogowe['dioda'])
      from module.sw_ogrzewanie_podlogowe import OgrzewaniePodlogowe
      thOgrzewaniePodlogowe = OgrzewaniePodlogowe()
      thOgrzewaniePodlogowe.start()
  else:
    if config.ogrzewanie_podlogowe['wlaczone'] == False:
      try: 
        if thOgrzewaniePodlogowe.running == True:
          thOgrzewaniePodlogowe.running = False
          thOgrzewaniePodlogowe.join()
          Wylacz('ogrzewanie_podlogowe')
      except NameError:
        Log(0, 'Błąd: wątek ogrzewania podłogowego został wcześniej nieoczekiwanie zamknięty.')  
      thOgrzewaniePodlogowe = None

  global thCyrkulacja
  if thCyrkulacja == None:
    if config.cyrkulacja['wlaczone'] == True:
      GPIOset ('relay', config.cyrkulacja['gpio'])
      GPIOset ('led', config.cyrkulacja['dioda'])
      from module.sw_cyrkulacja import Cyrkulacja
      thCyrkulacja = Cyrkulacja()
      thCyrkulacja.start()
  else:
    if config.cyrkulacja['wlaczone'] == False:
      try: 
        if thCyrkulacja.running == True:
          thCyrkulacja.running = False
          thCyrkulacja.join()
          Wylacz('cyrkulacja')
      except NameError:
        Log(0, 'Błąd: wątek cyrkulacji CWU został wcześniej nieoczekiwanie zamknięty.')  
      thCyrkulacja = None
  
  global thGrzalka
  if thGrzalka == None:
    if config.grzalka['wlaczone'] == True:
      GPIOset ('relay', config.grzalka['gpio'])
      GPIOset ('led', config.grzalka['dioda'])
      from module.sw_grzalka import Grzalka
      thGrzalka = Grzalka()
      thGrzalka.start()
  else:
    if config.grzalka['wlaczone'] == False:
      try: 
        if thGrzalka.running == True:
          thGrzalka.running = False
          thGrzalka.join()
          Wylacz('grzalka')
      except NameError:
        Log(0, 'Błąd: wątek grzałki został wcześniej nieoczekiwanie zamknięty.')  
      thGrzalka = None

  global thDb
  if thDb == None:
    if config.mysql['wlaczone'] == True:
      from module.sw_db import BazaDanych
      thDb = BazaDanych()
      thDb.start()
  else:
    if config.mysql['wlaczone'] == False:
      try: 
        if thDb.running == True:
          thDb.running = False
          thDb.join()
      except NameError:
        Log(0, 'Błąd: wątek bazy danych został wcześniej nieoczekiwanie zamknięty.')  
      thDb = None

  global thDbSQLite3
  if thDbSQLite3 == None:
    if config.sqlite3['wlaczone'] == True:
      from module.sw_sqlite3 import DB_SQLite3
      thDbSQLite3 = DB_SQLite3()
      thDbSQLite3.start()
  else:
    if config.sqlite3['wlaczone'] == False:
      try: 
        if thDbSQLite3.running == True:
          thDbSQLite3.running = False
          thDbSQLite3.join()
      except NameError:
        Log(0, 'Błąd: wątek bazy danych SQLite3 został wcześniej nieoczekiwanie zamknięty.')  
      thDbSQLite3 = None
      
        
def GPIOset (typ, tablica):

  gpio_unique = []
  
  if isinstance(tablica, list) == False:
    tmp = tablica
    tablica = []
    tablica.append(tmp)
  
  for gpio_id in (tablica):
    
    if gpio_id > 0:
      
      if gpio_id not in gpio_unique:
        gpio_unique.append(gpio_id)
        gpio.setup(gpio_id, gpio.OUT)
        
        if typ == 'relay':
          gpio.output(gpio_id, config.general['relay_off'])
          Log(3, 'Ustawiono wyjścia GPIO dla przekaźnika.')
        else:
          gpio.output(gpio_id, 0)
          Log(3, 'Ustawiono wyjścia GPIO dla diody.')



def Wlacz (urzadzenie, txt=''):
  
  global status
  
  if urzadzenie == 'co':
    if not status.co['praca']:
      for v in config.co['gpio']: gpio.output(v, config.general['relay_on'])
      if config.co['dioda']: gpio.output(config.co['dioda'], True)
      if config.co['wygaszanie_dioda']: gpio.output(config.co['wygaszanie_dioda'], False)
      if config.co['rozpalanie_dioda']: gpio.output(config.co['rozpalanie_dioda'], False)
      status.co['praca'] = True
      status.co['rozpalanie'] = False
      Log(2, "Włączono urządzenie: " + urzadzenie + ' (' + txt + ')')
  
  elif urzadzenie == 'cwu':
    if not status.cwu['praca']:
      for v in config.cwu['gpio']: gpio.output(v, config.general['relay_on'])
      if config.cwu['dioda']: gpio.output(config.cwu['dioda'], True)
      status.cwu['praca'] = True
      Log(2, "Włączono urządzenie: " + urzadzenie + ' (' + txt + ')')
  
  elif urzadzenie == 'cyrkulacja':
    if not status.cyrkulacja['praca']:
      for v in config.cyrkulacja['gpio']: gpio.output(v, config.general['relay_on'])
      if config.cyrkulacja['dioda']:
        gpio.output(config.cyrkulacja['dioda'], True)
      status.cyrkulacja['praca'] = True
      Log(2, "Włączono urządzenie: " + urzadzenie + ' (' + txt + ')')
  
  elif urzadzenie == 'grzalka':
    if not status.grzalka['praca']:
      for v in config.grzalka['gpio']: gpio.output(v, config.general['relay_on'])
      if config.grzalka['dioda']: gpio.output(config.grzalka['dioda'], True)
      status.grzalka['praca'] = True
      Log(2, "Włączono urządzenie: " + urzadzenie + ' (' + txt + ')')
  
  elif urzadzenie == 'ogrzewanie_podlogowe':
    if not status.ogrzewanie_podlogowe['praca']:
      for v in config.ogrzewanie_podlogowe['gpio']: gpio.output(v, config.general['relay_on'])
      if config.ogrzewanie_podlogowe['dioda']:
        gpio.output(config.ogrzewanie_podlogowe['dioda'], True)
      status.ogrzewanie_podlogowe['praca'] = True
      Log(2, "Włączono urządzenie: " + urzadzenie + ' (' + txt + ')')
  
  else:
    Log(2, "Włącz urządzenie: brak urządzenia o takiej nazwie" + \
      ' (' + txt + ')')
    return False

    
def Wylacz (urzadzenie, txt=''):
  
  global status
  
  if urzadzenie == 'co':
    if status.co['praca']:
      for v in config.co['gpio']: gpio.output(v, config.general['relay_off'])
      if config.co['dioda']: gpio.output(config.co['dioda'], False)
      if config.co['wygaszanie_dioda']: gpio.output(config.co['wygaszanie_dioda'], False)
      if config.co['rozpalanie_dioda']: gpio.output(config.co['rozpalanie_dioda'], False)
      status.co['praca'] = False
      status.co['wygaszanie'] = False
      Log(2, "Wyłączono urządzenie: " + urzadzenie + ' (' + txt + ')')
  
  elif urzadzenie == 'cwu':
    if status.cwu['praca']:
      for v in config.cwu['gpio']: gpio.output(v, config.general['relay_off'])
      if config.cwu['dioda']: gpio.output(config.cwu['dioda'], False)
      status.cwu['praca'] = False
      Log(2, "Wyłączono urządzenie: " + urzadzenie + ' (' + txt + ')')
  
  elif urzadzenie == 'cyrkulacja':
    if status.cyrkulacja['praca']:
      for v in config.cyrkulacja['gpio']: gpio.output(v, config.general['relay_off'])
      if config.cyrkulacja['dioda']:
        gpio.output(config.cyrkulacja['dioda'], False)
      status.cyrkulacja['praca'] = False
      Log(2, "Wyłączono urządzenie: " + urzadzenie + ' (' + txt + ')')
  
  elif urzadzenie == 'grzalka':
    if status.grzalka['praca']:
      for v in config.grzalka['gpio']: gpio.output(v, config.general['relay_off'])
      if config.grzalka['dioda']: gpio.output(config.grzalka['dioda'], False)
      status.grzalka['praca'] = False
      Log(2, "Wyłączono urządzenie: " + urzadzenie + ' (' + txt + ')')
  
  elif urzadzenie == 'ogrzewanie_podlogowe':
    if status.ogrzewanie_podlogowe['praca']:
      for v in config.ogrzewanie_podlogowe['gpio']: gpio.output(v, config.general['relay_off'])
      if config.ogrzewanie_podlogowe['dioda']:
        gpio.output(config.ogrzewanie_podlogowe['dioda'], False)
      status.ogrzewanie_podlogowe['praca'] = False
      Log(2, "Wyłączono urządzenie: " + urzadzenie + ' (' + txt + ')')
  
  else:
    Log(0, "Wyłącz urządzenie: brak urządzenia o takiej nazwie" + \
      ' (' + txt + ')')
    return False
    
    
def Rozpalanie (txt=''):  
 
  global status
  
  if not status.co['rozpalanie']: 
    status.co['rozpalanie'] = True
    if config.co['rozpalanie_dioda']: \
      gpio.output(config.co['rozpalanie_dioda'], True)
    Log(2, 'Rozpoczęto proces rozpalania kotła co: ' + '(' + txt + ')')
 
    
def WylaczRozpalanie (txt=''):  
 
  global status
  
  if status.co['rozpalanie']: 
    status.co['rozpalanie'] = False
    if config.co['rozpalanie_dioda']: \
      gpio.output(config.co['rozpalanie_dioda'], False)
    Log(2, 'Przerwano proces rozpalania kotła co: ' + '(' + txt + ')')
 
    
def WylaczWygaszanie (txt=''):  
 
  global status
  
  if status.co['wygaszanie']: 
    status.co['wygaszanie'] = False
    if config.co['wygaszanie_dioda']: \
      gpio.output(config.co['wygaszanie_dioda'], False)
    Log(2, 'Przerwano proces wygaszania kotła co: ' + '(' + txt + ')')
  
  
def Wygaszanie (txt=''):
  
  global status
 
  if not status.co['wygaszanie']: 
    status.co['wygaszanie'] = True
    if config.co['wygaszanie_dioda']: \
      gpio.output(config.co['wygaszanie_dioda'], True)
    Log(2, 'Rozpoczęto proces wygaszania kotła co: ' + '(' + txt + ')')
    
    
def Power(switch):  
  
  if switch:
    status.general['praca'] = True
    if config.general['dioda']:
      gpio.output(config.general['dioda'], True)
  else:
    status.general['praca'] = False
    if config.general['dioda']:
      gpio.output(config.general['dioda'], False)
