import ephem
import pytz
from dateutil import tz


from .utils import ureg
from .weather import Weather 

class Place(ephem.Observer):
  def __init__(self, lat, lon, elevation = 300, *args):
    ephem.Observer.__init__(self, *args)
    self.lat = str(lat)
    self.lon = str(lon)
    self.elevation = 300
    self.sun = ephem.Sun()
    self.sun.compute(self)
    self.weather = Weather(lat,lon)
    self.local_timezone = tz.gettz(self.weather.local_timezone)
 
  def sunset(self):
    return self.next_setting(self.sun).datetime().replace(tzinfo=pytz.UTC).astimezone(self.local_timezone)
  
  def sunrise(self):
    return self.next_rising(self.sun).datetime().replace(tzinfo=pytz.UTC).astimezone(self.local_timezone)
    
  def sun_observation(self): 
    prevrise = self.next_rising(self.sun)
    transit = self.next_transit(self.sun)
    nextset = self.next_setting(self.sun) 
    return (str(prevrise), str(transit), str(nextset))
   
class Observation:

  MAX_CLOUDS_TRESHOLD = 0.2
  MAX_WIND_TRESHOLD = 5
  MIN_TEMP_TRESHOLD = 5
  

  def __init__(self, place, equipment):
    self.place = place
    self.equipment = equipment
    self.observation_start = self.place.sunset()
    self.observation_stop = self.place.sunrise()
  
  def _mark_observation(self,plot):
    plot.axvspan(self.observation_start, self.observation_stop, color='gray', alpha=0.2)
  
  def plot_weather(self):
    import matplotlib.pyplot as plt #TODO: move it form here
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 10))
    # Clouds
    plt = self.place.weather.plot_clouds(ax=axes[0,0])
    plt.axhspan(0, Observation.MAX_CLOUDS_TRESHOLD, color='green', alpha=0.2)
    self._mark_observation(plt) 
    # Temperature
    plt = self.place.weather.plot_temperature(ax=axes[0,1])
    plt.axhspan(Observation.MIN_TEMP_TRESHOLD, 12.5, color='green', alpha=0.2) 
    self._mark_observation(plt)
    # Wind
    plt = self.place.weather.plot_wind(ax=axes[1,0])
    plt.axhspan(0, Observation.MAX_WIND_TRESHOLD, color='green', alpha=0.2)
    self._mark_observation(plt)
    # Pressure
    plt = self.place.weather.plot_pressure_and_ozone(ax=axes[1,1])
    self._mark_observation(plt)
    fig.tight_layout()
 
    
    
