import ephem
import pytz
import io
import pandas
import numpy
import matplotlib.dates as mdates


from dateutil import tz
from datetime import datetime, timedelta
from matplotlib import pyplot
from string import Template


from .utils import ureg
from .weather import Weather 
from .catalog import Catalog

class Place(ephem.Observer):
  def __init__(self, lat, lon, name = "", elevation = 300, *args):
    ephem.Observer.__init__(self, *args)
    self.lat = str(lat)
    self.lon = str(lon)
    self.name = name
    self.elevation = 300
    # Sun
    self.sun = ephem.Sun()
    self.sun.compute(self)
    # Moon
    self.moon = ephem.Moon()
    self.moon.compute(self)
   
    self.weather = Weather(lat,lon)
    self.local_timezone = tz.gettz(self.weather.local_timezone)
  
  def _next_setting_time(self, obj):
    return self.next_setting(obj).datetime().replace(tzinfo = pytz.UTC).astimezone(self.local_timezone)
  
  def _next_rising_time(self, obj):
    return self.next_rising(obj).datetime().replace(tzinfo = pytz.UTC).astimezone(self.local_timezone)
    
  def sunset(self):
    return self._next_setting_time(self.sun)
  
  def sunrise(self):
    return self._next_rising_time(self.sun)
    
  def moonset(self):
    return self._next_setting_time(self.moon)
  
  def moonrise(self):
    return self._next_rising_time(self.moon)

class Conditions:
  MAX_CLOUDS = 0.2
  MAX_PRECIP_PROBABILITY = 0.05 
  MAX_PRECIP_INTENSITY = 0.05
  MAX_WIND = 10
  MIN_TEMPERATURE = 0
  MAX_TEMPERATURE = 20
  MIN_WEATHER_GOODNES = 0.8
  MAX_RETURN = "01:00:00" 
  
  MIN_OBJECT_ALTITUDE = 15  
  MAX_OBJECT_MAGNITUDE = 9
   
class Observation:

  def __init__(self, place, equipment, conditions = Conditions()):
    self.place = place
    self.equipment = equipment
    self.conditions = conditions
    self.start, self.stop = self._normalize_dates(place.sunset(), place.sunrise())
    self.local_messier = Catalog.MESSIER.copy() 
    # Compute time limit    
    max_return_time = [int(value) for value in self.conditions.MAX_RETURN.split(":")]
    time_limit = self.start.replace(hour = max_return_time[0], minute = max_return_time[1], second = max_return_time[2]) 
    self.time_limit = time_limit if time_limit > self.start else time_limit + timedelta(days = 1)
    # Compute transit of messier objects 
    self.local_messier['Transit'] = self.local_messier[['RA','Dec']].apply(
      lambda body: Catalog.compute_tranzit(Catalog.fixed_body(body.RA,body.Dec), self.place) ,axis=1)
    # Compute altitude of messier objects at transit   
    self.local_messier['Altitude'] = self.local_messier[['RA','Dec','Transit']].apply(
      lambda body: Catalog.altitude_at_transit(Catalog.fixed_body(body.RA,body.Dec), self.place, body.Transit) ,axis=1)  
    
  def get_visible_messier(self, hours_margin = 0, sort_by = ['Transit']):
    visible_messier = self.local_messier
    visible_messier = visible_messier[
      # Filter objects by they transit
      (visible_messier.Transit > self.start - timedelta(hours = hours_margin)) & 
      (visible_messier.Transit < self.time_limit + timedelta(hours = hours_margin)) & 
      # Filter objects by they min altitude at transit
      (visible_messier.Altitude > self.conditions.MIN_OBJECT_ALTITUDE) &
      # Filter object by they magnitude
      (visible_messier.Magnitude < self.conditions.MAX_OBJECT_MAGNITUDE)].sort_values(sort_by, ascending=[1])
    return visible_messier

  def plot_visible_messier(self):
    messier = self.get_visible_messier()[['Messier', 'Transit', 'Altitude','Width']]
    plot = messier.plot(
      x = 'Transit', 
      y = 'Altitude',
      marker = 'o', 
      #markersize = messier['Width'],
      linestyle='none', 
      xlim=[self.start - timedelta(minutes = 15) ,self.time_limit + timedelta(minutes = 15)],
      ylim=(0,90),
      figsize = (17, 5))

    last_position = [0,0] 
    offset_index = 0
    offsets = [(-25,-12),(5,5),(-25,5),(5,-12)]
    for obj in messier.values:
      distance = (((mdates.date2num(obj[1]) - last_position[0])*100)**2 + (obj[2] - last_position[1])**2)**0.5
      offset_index = offset_index + (1 if distance < 5 else 0)
      plot.annotate(obj[0], 
        (mdates.date2num(obj[1]), obj[2]),
        xytext = offsets[offset_index % len(offsets)], 
        textcoords='offset points')
      last_position = [mdates.date2num(obj[1]), obj[2]]
    self._mark_observation(plot)  
    self._mark_good_conditions(plot, self.conditions.MIN_OBJECT_ALTITUDE, 90)  
            

  def _normalize_dates(self, start, stop):
    now = datetime.utcnow().astimezone(self.place.local_timezone)
    new_start = start if start < stop else now
    new_stop = stop
    return (new_start, new_stop)

  def _mark_observation(self, plot):
    # Add marker for night
    plot.axvspan(self.start, self.stop, color = 'gray', alpha = 0.2) 
    # Add marker for moon 
    moon_start, moon_stop = self._normalize_dates(self.place.moonrise(), self.place.moonset())
    plot.axvspan(moon_start, moon_stop, color = 'yellow', alpha = 0.1)
    # Add marker for time limit
    plot.axvline(self.start, color='orange', linestyle='--')  
    plot.axvline(self.time_limit, color='orange', linestyle='--')  

  def _mark_good_conditions(self, plot, minimal, maximal):
    plot.axhspan(minimal, maximal, color = 'green', alpha = 0.1)

  def plot_weather(self):
    plot = self._generate_plot_weather()

  def get_weather_plot_bytes(self):
    plot = self._generate_plot_weather()
    plot_bytes = io.BytesIO()
    plot.savefig(plot_bytes, format='png')
    # Prevent showing plot in ipython
    pyplot.close(plot)
    plot_bytes.seek(0)
    return plot_bytes

  def _computer_weather_goodnse(self):
    # Get critical weather data 
    data = self.place.weather.get_critical_data(self.start, self.stop)
    # Get only data defore time limit  
    data = data[data.time <= self.time_limit]
    all_hours = len(data)
    # Get hours with good conditions
    result = data[
      (data.cloudCover < self.conditions.MAX_CLOUDS) &
      (data.precipProbability < self.conditions.MAX_PRECIP_PROBABILITY) &
      (data.windSpeed < self.conditions.MAX_WIND) &
      (data.temperature > self.conditions.MIN_TEMPERATURE) &
      (data.temperature < self.conditions.MAX_TEMPERATURE)]
    good_hours = len(result)
    # Return relative number of good hours
    return good_hours/all_hours

  def weather_is_good(self):
    return self._computer_weather_goodnse() > self.conditions.MIN_WEATHER_GOODNES
    
  def to_html(self):
    with open("./apts/templates/message.html.template") as template_file:
      template = Template(template_file.read())
      data = {
        "title" : "Astro Pożar",
        #"weather_image_data" : self._encode_weather_plot(),
        "equipment_table" : self.equipment.data().to_html()
      }
      return template.substitute(data) 
    return ""
    
    
  def _generate_plot_weather(self):
    fig, axes = pyplot.subplots(nrows = 4, ncols = 2, figsize = (13, 18))
    # Clouds
    plt = self.place.weather.plot_clouds(ax=axes[0,0])
    self._mark_observation(plt)
    self._mark_good_conditions(plt, 0, self.conditions.MAX_CLOUDS)
    # Cloud summary
    plt = self.place.weather.plot_clouds_summary(ax = axes[0,1])
    # Precip
    plt = self.place.weather.plot_precip(ax = axes[1,0])
    self._mark_observation(plt) 
    self._mark_good_conditions(plt, 0, self.conditions.MAX_PRECIP_PROBABILITY)
    # Precip type summary
    plt = self.place.weather.plot_precip_type_summary(ax = axes[1,1])   
    # Temperature
    plt = self.place.weather.plot_temperature(ax = axes[2,0])
    self._mark_observation(plt)
    self._mark_good_conditions(plt, self.conditions.MIN_TEMPERATURE, self.conditions.MAX_TEMPERATURE)
    # Wind
    plt = self.place.weather.plot_wind(ax=axes[2,1])
    self._mark_observation(plt)
    self._mark_good_conditions(plt, 0, self.conditions.MAX_WIND)
    # Pressure
    plt = self.place.weather.plot_pressure_and_ozone(ax = axes[3,0])
    self._mark_observation(plt)
    # Visibility
    plt = self.place.weather.plot_visibility(ax = axes[3,1])
    self._mark_observation(plt)
    fig.tight_layout()
    return fig
   
