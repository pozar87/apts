import ephem
import pytz
import pkg_resources

import pandas as pd

from timezonefinder import TimezoneFinder
from dateutil import tz
from datetime import date 
from math import radians as rad,degrees as deg  

from .weather import Weather


import matplotlib.font_manager as font_manager


class Place(ephem.Observer):

  MOON_FONT = font_manager.FontProperties(fname=pkg_resources.resource_filename('apts', 'data/moon_phases.ttf'), size=50)
  TF = TimezoneFinder()

  def __init__(self, lat, lon, name="", elevation=300, *args):
    ephem.Observer.__init__(self, *args)
    self.lat = rad(lat)
    self.lon = rad(lon)
    self.lat_decimal = lat
    self.lon_decimal = lon
    self.name = name
    self.elevation = elevation
    # Sun
    self.sun = ephem.Sun()
    self.sun.compute(self)
    # Moon
    self.moon = ephem.Moon()
    self.moon.compute(self)
    self.local_timezone = tz.gettz(Place.TF.timezone_at(lat=self.lat_decimal,lng=self.lon_decimal))

  def get_weather(self):
    self.weather = Weather(self.lat_decimal, self.lon_decimal, self.local_timezone)

  def _next_setting_time(self, obj):
    #self.date = date.today()
    return self.next_setting(obj).datetime().replace(tzinfo=pytz.UTC).astimezone(self.local_timezone)

  def _next_rising_time(self, obj):
    #self.date = date.today()
    return self.next_rising(obj).datetime().replace(tzinfo=pytz.UTC).astimezone(self.local_timezone)

  def sunset_time(self):
    return self._next_setting_time(self.sun)

  def sunrise_time(self):
    return self._next_rising_time(self.sun)

  def moonset_time(self):
    return self._next_setting_time(self.moon)

  def moonrise_time(self):
    return self._next_rising_time(self.moon)
  
  def moon_phase_letter(self):
    lunation = self.moon_phase()
    letter = chr(ord('A')+int(round(lunation*26))) 
    return letter
  
  def moon_phase(self):
    lunation = self.moon_path()['Lunation'][48]
    return int(lunation+0.5)*100
  
  def moon_path(self):
    self.date = date.today()
    result = []
    for i in range(24*4): # compute position for every 15 minutes  
      self.moon.compute(self)  
      next_new_moon = ephem.next_new_moon(self.date)  
      previous_new_moon = ephem.previous_new_moon(self.date)  
      lunation = (self.date-previous_new_moon)/(next_new_moon-previous_new_moon)
      row = [ephem.localtime(self.date).time(), 
             deg(self.moon.alt),
             deg(self.moon.az),  
             self.date.datetime().replace(tzinfo=pytz.UTC).astimezone(self.local_timezone).strftime("%H:%M"),  
             self.moon.phase,
             lunation]
      result.append(row)
      self.date += ephem.minute*15  
    return pd.DataFrame(result, columns = ['Time','Moon altitude','Azimuth','Local_time','Phase','Lunation'])
  
  def plot_moon_path(self, **args):
    def add_marker(label, position):
      plt.axvline(position, color = 'green', linestyle='--', linewidth=1)
      plt.text(position, 1, label, weight='bold', horizontalalignment='center')

    data = self.moon_path() 
    plt = data.plot(x='Azimuth', y='Moon altitude', title='Moon altitude', style='.-', **args) 
    # Add cardinal direction
    if self.lat > 0:
      add_marker('E', 90)
      add_marker('S', 180)
      add_marker('W', 270)
      plt.set_xlim(45,315)
    else:  
      add_marker('E', 90)
      add_marker('S', 180)
      add_marker('W', 270)
      plt.set_xlim(0,360)
    
    # Plot horizon
    plt.axhspan(0, -50, color='gray', alpha=0.2)
    plt.locator_params(nbins=20)
    lim = plt.set_ylim(bottom=-10)
    
    # Plot Moon marker
    plt.text(180, 10, self.moon_phase_letter(), fontproperties=Place.MOON_FONT, horizontalalignment='center')
    plt.text(180, 15, str(100-self.moon_phase()) + '%', color='gray', horizontalalignment='center')
    
    # Plot time for altitudes 
    for obj in data.iloc[::5, :].values:
      plt.annotate(obj[3],(obj[2] - 10, obj[1]))
    
    return plt


