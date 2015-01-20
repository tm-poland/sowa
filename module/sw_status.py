
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
    self.general['temp'] = 0.0
    self.general['temp_wew'] = 0.0
    self.general['temp_zew'] = 0.0
     
    self.grzalka['praca'] = False
    
    self.cwu['praca'] = False
    self.cwu['temp'] = 0.0
    
    self.cyrkulacja['praca'] = False
    self.cyrkulacja['temp'] = False
    
    self.co['rozpalanie'] = False
    self.co['wygaszanie'] = False
    self.co['praca'] = False
    self.co['temp_zasilania'] = 0.0
    self.co['temp_powrotu'] = 0.0

    self.ogrzewanie_podlogowe['praca'] = False
    self.ogrzewanie_podlogowe['temp'] = 0.0
    
    self.termopara['temp'] = 0.0
    
    
  def get(self, config):

    sz = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n" \
      + "<sowa1>\n" \
      + "\t<general_praca>" + str(int(self.general['praca'])) + "</general_praca>\n" \
      + "\t<general_temp>" + str(float(self.general['temp'])) + "</general_temp>\n" \
      + "\t<general_temp_wew>" + str(float(self.general['temp_wew'])) + "</general_temp_wew>\n" \
      + "\t<general_temp_zew>" + str(float(self.general['temp_zew'])) + "</general_temp_zew>\n" \
      + "\t<co_on>" + str(int(config.co['wlaczone'])) + "</co_on>\n" \
      + "\t<co_praca>" + str(int(self.co['praca'])) + "</co_praca>\n" \
      + "\t<co_rozpalanie>" + str(int(self.co['rozpalanie'])) + "</co_rozpalanie>\n" \
      + "\t<co_wygaszanie>" + str(int(self.co['wygaszanie'])) + "</co_wygaszanie>\n" \
      + "\t<co_temp_zasilania>" + str(float(self.co['temp_zasilania'])) + "</co_temp_zasilania>\n" \
      + "\t<co_temp_powrotu>" + str(float(self.co['temp_powrotu'])) + "</co_temp_powrotu>\n" \
      + "\t<cwu_on>" + str(int(config.cwu['wlaczone'])) + "</cwu_on>\n" \
      + "\t<cwu_praca>" + str(int(self.cwu['praca'])) + "</cwu_praca>\n" \
      + "\t<cwu_temp>" + str(float(self.cwu['temp'])) + "</cwu_temp>\n" \
      + "\t<cyrkulacja_on>" + str(int(config.cyrkulacja['wlaczone'])) + "</cyrkulacja_on>\n" \
      + "\t<cyrkulacja_praca>" + str(int(self.cyrkulacja['praca'])) + "</cyrkulacja_praca>\n" \
      + "\t<cyrkulacja_temp>" + str(float(self.cyrkulacja['temp'])) + "</cyrkulacja_temp>\n" \
      + "\t<ogrzewanie_podlogowe_on>" + str(int(config.ogrzewanie_podlogowe['wlaczone'])) + "</ogrzewanie_podlogowe_on>\n" \
      + "\t<ogrzewanie_podlogowe_praca>" + str(int(self.ogrzewanie_podlogowe['praca'])) + "</ogrzewanie_podlogowe_praca>\n" \
      + "\t<ogrzewanie_podlogowe_temp>" + str(float(self.ogrzewanie_podlogowe['temp'])) + "</ogrzewanie_podlogowe_temp>\n" \
      + "\t<grzalka_on>" + str(int(config.grzalka['wlaczone'])) + "</grzalka_on>\n" \
      + "\t<grzalka_praca>" + str(int(self.grzalka['praca'])) + "</grzalka_praca>\n" \
      + "\t<termopara_on>" + str(int(config.termopara['wlaczone'])) + "</termopara_on>\n" \
      + "\t<termopara_temp>" + str(float(self.termopara['temp'])) + "</termopara_temp>\n" \
      + "</sowa1>\n"
          
    return sz    
