import json

class Status ():
  
  def __init__(self):

    self.general = {}
    self.cwu = {}
    self.grzalka = {}
    self.cyrkulacja = {} 
    self.co = {}
    self.ogrzewanie_podlogowe = {}
    self.termopara = {}
    
    self.general['praca'] = False
    self.general['temp'] = None
    self.general['temp_wew'] = None
    self.general['temp_zew'] = None
     
    self.grzalka['praca'] = False
    
    self.cwu['praca'] = False
    self.cwu['temp'] = None
    
    self.cyrkulacja['praca'] = False
    self.cyrkulacja['temp'] = False
    
    self.co['rozpalanie'] = False
    self.co['wygaszanie'] = False
    self.co['praca'] = False
    self.co['temp_zasilania'] = None
    self.co['temp_powrotu'] = None

    self.ogrzewanie_podlogowe['praca'] = False
    self.ogrzewanie_podlogowe['temp'] = None
    
    self.termopara['temp'] = None
    
    
  def get(self, config):

#     sz = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" \
#       + "<sowa1>\n" \
#       + "\t<general_praca>" + str(int(self.general['praca'])) + "</general_praca>\n" \
#       + "\t<general_temp>" + str(float(self.general['temp'])) + "</general_temp>\n" \
#       + "\t<general_temp_wew>" + str(float(self.general['temp_wew'])) + "</general_temp_wew>\n" \
#       + "\t<general_temp_zew>" + str(float(self.general['temp_zew'])) + "</general_temp_zew>\n" \
#       + "\t<co_on>" + str(int(config.co['wlaczone'])) + "</co_on>\n" \
#       + "\t<co_praca>" + str(int(self.co['praca'])) + "</co_praca>\n" \
#       + "\t<co_rozpalanie>" + str(int(self.co['rozpalanie'])) + "</co_rozpalanie>\n" \
#       + "\t<co_wygaszanie>" + str(int(self.co['wygaszanie'])) + "</co_wygaszanie>\n" \
#       + "\t<co_temp_zasilania>" + str(float(self.co['temp_zasilania'])) + "</co_temp_zasilania>\n" \
#       + "\t<co_temp_powrotu>" + str(float(self.co['temp_powrotu'])) + "</co_temp_powrotu>\n" \
#       + "\t<cwu_on>" + str(int(config.cwu['wlaczone'])) + "</cwu_on>\n" \
#       + "\t<cwu_praca>" + str(int(self.cwu['praca'])) + "</cwu_praca>\n" \
#       + "\t<cwu_temp>" + str(float(self.cwu['temp'])) + "</cwu_temp>\n" \
#       + "\t<cyrkulacja_on>" + str(int(config.cyrkulacja['wlaczone'])) + "</cyrkulacja_on>\n" \
#       + "\t<cyrkulacja_praca>" + str(int(self.cyrkulacja['praca'])) + "</cyrkulacja_praca>\n" \
#       + "\t<cyrkulacja_temp>" + str(float(self.cyrkulacja['temp'])) + "</cyrkulacja_temp>\n" \
#       + "\t<ogrzewanie_podlogowe_on>" + str(int(config.ogrzewanie_podlogowe['wlaczone'])) + "</ogrzewanie_podlogowe_on>\n" \
#       + "\t<ogrzewanie_podlogowe_praca>" + str(int(self.ogrzewanie_podlogowe['praca'])) + "</ogrzewanie_podlogowe_praca>\n" \
#       + "\t<ogrzewanie_podlogowe_temp>" + str(float(self.ogrzewanie_podlogowe['temp'])) + "</ogrzewanie_podlogowe_temp>\n" \
#       + "\t<grzalka_on>" + str(int(config.grzalka['wlaczone'])) + "</grzalka_on>\n" \
#       + "\t<grzalka_praca>" + str(int(self.grzalka['praca'])) + "</grzalka_praca>\n" \
#       + "\t<termopara_on>" + str(int(config.termopara['wlaczone'])) + "</termopara_on>\n" \
#       + "\t<termopara_temp>" + str(float(self.termopara['temp'])) + "</termopara_temp>\n" \
#       + "</sowa1>\n"
      
#     sz = {
#       'general_praca': str(int(self.general['praca'])),
#       'general_temp': str(float(self.general['temp'])),
#       'general_temp_wew': str(float(self.general['temp_wew'])),
#       'general_temp_zew': str(float(self.general['temp_zew'])),
#       'co_on': str(int(config.co['wlaczone'])),
#       'co_praca': str(int(self.co['praca'])),
#       'co_rozpalanie': str(int(self.co['rozpalanie'])),
#       'co_wygaszanie': str(int(self.co['wygaszanie'])),
#       'co_temp_zasilania': str(float(self.co['temp_zasilania'])),
#       'co_temp_powrotu': str(float(self.co['temp_powrotu'])),
#       'cwu_on': str(int(config.cwu['wlaczone'])),
#       'cwu_praca': str(int(self.cwu['praca'])),
#       'cwu_temp': str(float(self.cwu['temp'])),
#       'cyrkulacja_on': str(int(config.cyrkulacja['wlaczone'])),
#       'cyrkulacja_manual': str(int(config.cyrkulacja['manual'])),
#       'cyrkulacja_praca': str(int(self.cyrkulacja['praca'])),
#       'cyrkulacja_temp': str(float(self.cyrkulacja['temp'])),
#       'ogrzewanie_podlogowe_on': str(int(config.ogrzewanie_podlogowe['wlaczone'])),
#       'ogrzewanie_podlogowe_praca': str(int(self.ogrzewanie_podlogowe['praca'])),
#       'ogrzewanie_podlogowe_temp': str(float(self.ogrzewanie_podlogowe['temp'])),
#       'grzalka_on': str(int(config.grzalka['wlaczone'])),
#       'grzalka_manual': str(int(config.grzalka['manual'])),
#       'grzalka_praca': str(int(self.grzalka['praca'])),
#       'termopara_on': str(int(config.termopara['wlaczone'])),
#       'termopara_temp': str(float(self.termopara['temp']))
#       }

    sz = {
      'general_praca': int(self.general['praca']),
      'general_temp': self.general['temp'],
      'general_temp_wew': self.general['temp_wew'],
      'general_temp_zew': self.general['temp_zew'],
      'co_on': int(config.co['wlaczone']),
      'co_praca': int(self.co['praca']),
      'co_rozpalanie': int(self.co['rozpalanie']),
      'co_wygaszanie': int(self.co['wygaszanie']),
      'co_temp_zasilania': self.co['temp_zasilania'],
      'co_temp_powrotu': self.co['temp_powrotu'],
      'cwu_on': int(config.cwu['wlaczone']),
      'cwu_praca': int(self.cwu['praca']),
      'cwu_temp': self.cwu['temp'],
      'cyrkulacja_on': int(config.cyrkulacja['wlaczone']),
      'cyrkulacja_manual': int(config.cyrkulacja['manual']),
      'cyrkulacja_praca': int(self.cyrkulacja['praca']),
      'cyrkulacja_temp': self.cyrkulacja['temp'],
      'ogrzewanie_podlogowe_on': int(config.ogrzewanie_podlogowe['wlaczone']),
      'ogrzewanie_podlogowe_praca': int(self.ogrzewanie_podlogowe['praca']),
      'ogrzewanie_podlogowe_temp': self.ogrzewanie_podlogowe['temp'],
      'grzalka_on': int(config.grzalka['wlaczone']),
      'grzalka_manual': int(config.grzalka['manual']),
      'grzalka_praca': int(self.grzalka['praca']),
      'termopara_on': int(config.termopara['wlaczone']),
      'termopara_temp': self.termopara['temp']
    }
          
    return json.dumps(sz)
#    return sz    
