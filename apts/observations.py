import ephem
import pytz
import datetime

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
    self.moon = ephem.Moon()
    self.moon.compute(self)
    self.weather = Weather(lat,lon)
    self.local_timezone = tz.gettz(self.weather.local_timezone)
  
  def _next_setting_time(self, obj):
    return self.next_setting(obj).datetime().replace(tzinfo=pytz.UTC).astimezone(self.local_timezone)
  
  def _next_rising_time(self, obj):
    return self.next_rising(obj).datetime().replace(tzinfo=pytz.UTC).astimezone(self.local_timezone)
    
  def sunset(self):
    return self._next_setting_time(self.sun)
  
  def sunrise(self):
    return self._next_rising_time(self.sun)
    
  def moonset(self):
    return self._next_setting_time(self.moon)
  
  def moonrise(self):
    return self._next_rising_time(self.moon)
   
   
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
    now = datetime.datetime.utcnow().astimezone(self.place.local_timezone)
    plot.axvspan(min(now,self.observation_start), self.observation_stop, color='gray', alpha=0.2)
    plot.axvspan(min(now,self.place.moonrise()), self.place.moonset(), color='yellow', alpha=0.2)
  
  def plot_weather(self):
    import matplotlib.pyplot as plt #TODO: move it form here
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(13, 9))
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
   
