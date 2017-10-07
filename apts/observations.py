import ephem
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
 
  def sunset(self):
    return self.next_setting(self.sun)
  
  def sunrise(self):
    return self.next_rising(self.sun)
    
  def sun_observation(self): 
    prevrise = self.next_rising(self.sun)
    transit = self.next_transit(self.sun)
    nextset = self.next_setting(self.sun) 
    return (str(prevrise), str(transit), str(nextset))
   
class Observation:
  def __init__(self, place, equipment):
    self.place = place
    self.equipment = equipment
    self.observation_start = 24*(self.place.sunset() - ephem.now())
    self.observation_stop = 24*(self.place.sunrise() - ephem.now())
  
  def plot_weather(self):
    import matplotlib.pyplot as plt
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 10))
    # Clouds
    plt = self.place.weather.plot_clouds(ax=axes[0,0])
    axes[0,0].set_title('Clouds');
    plt.axvspan(self.observation_start, self.observation_stop, color='green', alpha=0.2)
    plt.axhspan(0, 0.2, color='green', alpha=0.2) 
    # Temperature
    plt = self.place.weather.plot_temperature(ax=axes[0,1])
    axes[0,1].set_title('Temperature');
    # Wind
    plt = self.place.weather.plot_wind(ax=axes[1,0])
    axes[1,0].set_title('Wind');
    # Pressure
    plt = self.place.weather.plot_pressure(ax=axes[1,1])
    axes[1,1].set_title('Pressure');
    
 
    
    
