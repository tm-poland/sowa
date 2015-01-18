#!/usr/bin/python
#-*- coding: utf-8 -*-

import socket
import sys
import signal
import traceback

from module.sw_config import *
from module.sw_conn import *
from module.sw_status import *
from module.sw_log import *
from module.sw_funkcje import *


def sigterm_handler(_signo, _stack_frame):
  sys.exit(0)
signal.signal(signal.SIGTERM, sigterm_handler)

exc_type = exc_value = exc_traceback = None

try:
  config.read()
  Log(1, '########## SERWER SOWA1 START ##########')
  Log(3, 'Wczytano konfigurację serwera z pliku.')
  
  gpio.setmode(gpio.BCM)
  #gpio.setwarnings(False)
  GPIOset('led', config.general['dioda'])
  Log(2, 'Ustawiono wyjścia GPIO.')
  
  Power(True)
  
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
   
  try:
      s.bind((config.general['host'], config.general['port']))
      
  except socket.error as msg:
    Log(1, 'Nie można otworzyć portu serwera. Błąd: ' \
      + str(msg[0]) + ', ' + msg[1])
    sys.exit(1)
       
  s.listen(10)
  
  Log(1, 'Serwer uruchomiony na porcie ' + str(config.general['port']))
   
  ThreadsLoad()

       
  try:   
    while 1:
      conn, addr = s.accept()
      Log(3, 'Nawiązano polączenie z ' + addr[0] + ':' + str(addr[1]))
       
      th = Conn(1, conn, addr[0], addr[1])
      th.start()
      conn_threads.append(th)
      Log(3, 'Utworzono nowy wątek połączenia nr: ' + str(len(conn_threads)))
    
    for t in threads:
      t.running = False
      t.join()
      
    s.close() 
 
  except KeyboardInterrupt:
    Log(1, "Serwer otrzymał sygnał ^C.")

except Exception, e:
  exc_type, exc_value, exc_traceback = sys.exc_info()
  raise 
      
finally:  
  if exc_value != None:
    print >> sys.stderr, time.strftime("%d-%m-%Y %H:%M:%S ") + "Wystąpił błąd programu:"
    traceback.print_exception(exc_type, exc_value, exc_traceback, limit=2, file=sys.stderr)
  
  Log(1, "Serwer otrzymał sygnał SIGTERM. Kończy działanie.")
  
  for t in conn_threads:
    t.running = False
    
  ThreadsExit ()
  
  for t in conn_threads:
    t.join()
      
  s.close()
  Power(False)
  gpio.cleanup()
