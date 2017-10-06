import ephem
from .weather import Weather 

class Place(ephem.Observer):
  def __init__(self, lat, lon, *args):
    ephem.Observer.__init__(self, *args)
    self.lat = str(lat)
    self.lon = str(lon)
    self.elevation = 300
    self.sun = ephem.Sun()
    self.sun.compute(self)
    self.weather = Weather(lat,lon)
    
  def sun_observation(self): 
    prevrise = self.next_rising(self.sun)
    transit = self.next_transit(self.sun)
    nextset = self.next_setting(self.sun) 
    return (str(prevrise), str(transit), str(nextset))
  
  
class Observation:
  def __init__(self, place, equipment):
    self.place = place
    self.equipment = equipment
    
  
  
  
    
