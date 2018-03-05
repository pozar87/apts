import pandas
import numpy
import base64
import pkg_resources
import matplotlib.dates as mdates

from datetime import datetime, timedelta
from matplotlib import pyplot
from string import Template

from .utils import ureg, Utils
from .messier import Messier
from .planets import Planets
from .conditions import Conditions

class Observation:

  NOTIFICATION = pkg_resources.resource_filename('apts', 'templates/notification.html.template')

  def __init__(self, place, equipment, conditions=Conditions()):
    self.place = place
    self.equipment = equipment
    self.conditions = conditions
    self.start, self.stop = self._normalize_dates(
        place.sunset_time(), place.sunrise_time())
    self.local_messier = Messier(self.place)
    self.local_planets = Planets(self.place)
    # Compute time limit
    max_return_time = [int(value)
                       for value in self.conditions.MAX_RETURN.split(":")]
    time_limit = self.start.replace(
        hour=max_return_time[0], minute=max_return_time[1], second=max_return_time[2])
    self.time_limit = time_limit if time_limit > self.start else time_limit + \
        timedelta(days=1)
  
  def get_visible_messier(self):
    return self.local_messier.get_visible(self.conditions, self.start, self.time_limit)

  def get_visible_planets(self):
    return self.local_planets.get_visible(self.conditions, self.start, self.time_limit)

  def _generate_plot_messier(self):
    messier = self.get_visible_messier(
    )[['Messier', 'Transit', 'Altitude', 'Width']]
    plot = messier.plot(
        x='Transit',
        y='Altitude',
        marker='o',
        #markersize = messier['Width'],
        linestyle='none',
        xlim=[self.start - timedelta(minutes=15),
              self.time_limit + timedelta(minutes=15)],
        ylim=(0, 90),
        figsize=(17, 5))

    last_position = [0, 0]
    offset_index = 0
    offsets = [(-25, -12), (5, 5), (-25, 5), (5, -12)]
    for obj in messier.values:
      distance = (((mdates.date2num(
          obj[1]) - last_position[0]) * 100)**2 + (obj[2] - last_position[1])**2)**0.5
      offset_index = offset_index + (1 if distance < 5 else 0)
      plot.annotate(obj[0],
                    (mdates.date2num(obj[1]), obj[2]),
                    xytext=offsets[offset_index % len(offsets)],
                    textcoords='offset points')
      last_position = [mdates.date2num(obj[1]), obj[2]]
    self._mark_observation(plot)
    self._mark_good_conditions(
        plot, self.conditions.MIN_OBJECT_ALTITUDE, 90)
    return plot.get_figure()    

  def _normalize_dates(self, start, stop):
    now = datetime.utcnow().astimezone(self.place.local_timezone)
    new_start = start if start < stop else now
    new_stop = stop
    return (new_start, new_stop)

  def plot_weather(self):
    plot = self._generate_plot_weather()
    
  def plot_messier(self):
    plot = self._generate_plot_messier()  

  def _compute_weather_goodnse(self):
    # Get critical weather data
    data = self.place.weather.get_critical_data(self.start, self.stop)
    # Get only data defore time limit
    data = data[data.time <= self.time_limit]
    all_hours = len(data)
    # Get hours with good conditions
    result = data[
        (data.cloudCover < self.conditions.MAX_CLOUDS) &
        (data.precipProbability < self.conditions.MAX_PRECIPATION_PROBABILITY) &
        (data.windSpeed < self.conditions.MAX_WIND) &
        (data.temperature > self.conditions.MIN_TEMPERATURE) &
        (data.temperature < self.conditions.MAX_TEMPERATURE)]
    good_hours = len(result)
    # Return relative number of good hours
    return good_hours / all_hours

  def weather_is_good(self):
    return self._compute_weather_goodnse() > self.conditions.MIN_WEATHER_GOODNESS

  def to_html(self):
    with open(Observation.NOTIFICATION) as template_file:
      template = Template(template_file.read())
      data = {
          "title" : "APTS",
          "start" : Utils.format_date(self.start),
          "stop" : Utils.format_date(self.stop),
          "planets_count" : len(self.get_visible_planets()),
          "messier_count" : len(self.get_visible_messier()),
          "planets_table" : self.get_visible_planets().to_html(),
          "messier_table" : self.get_visible_messier().to_html(),
          "equipment_table" : self.equipment.data().to_html(),
          "place_name" : self.place.name,
          "lat" : numpy.rad2deg(self.place.lat),
          "lon" : numpy.rad2deg(self.place.lon)
      }
      return str(template.substitute(data))
    return ""

  def _mark_observation(self, plot):
    # Add marker for night
    plot.axvspan(self.start, self.stop, color='gray', alpha=0.2)
    # Add marker for moon
    moon_start, moon_stop = self._normalize_dates(
        self.place.moonrise_time(), self.place.moonset_time())
    plot.axvspan(moon_start, moon_stop, color='yellow', alpha=0.1)
    # Add marker for time limit
    plot.axvline(self.start, color='orange', linestyle='--')
    plot.axvline(self.time_limit, color='orange', linestyle='--')

  def _mark_good_conditions(self, plot, minimal, maximal):
    plot.axhspan(minimal, maximal, color='green', alpha=0.1)

  def _generate_plot_weather(self):
    fig, axes = pyplot.subplots(nrows=4, ncols=2, figsize=(13, 18))
    # Clouds
    plt = self.place.weather.plot_clouds(ax=axes[0, 0])
    self._mark_observation(plt)
    self._mark_good_conditions(plt, 0, self.conditions.MAX_CLOUDS)
    # Cloud summary
    plt = self.place.weather.plot_clouds_summary(ax=axes[0, 1])
    # Precipation
    plt = self.place.weather.plot_precipitation(ax=axes[1, 0])
    self._mark_observation(plt)
    self._mark_good_conditions(
        plt, 0, self.conditions.MAX_PRECIPATION_PROBABILITY)
    # precipitation type summary
    plt = self.place.weather.plot_precipitation_type_summary(ax=axes[1, 1])
    # Temperature
    plt = self.place.weather.plot_temperature(ax=axes[2, 0])
    self._mark_observation(plt)
    self._mark_good_conditions(
        plt, self.conditions.MIN_TEMPERATURE, self.conditions.MAX_TEMPERATURE)
    # Wind
    plt = self.place.weather.plot_wind(ax=axes[2, 1])
    self._mark_observation(plt)
    self._mark_good_conditions(plt, 0, self.conditions.MAX_WIND)
    # Pressure
    plt = self.place.weather.plot_pressure_and_ozone(ax=axes[3, 0])
    self._mark_observation(plt)
    # Visibility
    plt = self.place.weather.plot_visibility(ax=axes[3, 1])
    self._mark_observation(plt)
    fig.tight_layout()
    return fig
