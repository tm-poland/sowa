import sys
import time

from module.sw_config import *

global config
def Log (poziom, text):
  if poziom <= config.general['loglevel']:
    text = time.strftime("%d-%m-%Y %H:%M:%S ") + str(text)
    
    fo = open(config.general['logfile'], "a")
    fo.write( text + "\n");
    fo.close()
    
    if config.general['debug']:
      print >> sys.stderr, text
