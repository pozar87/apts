import logging
from datetime import datetime, timedelta, timezone
from string import Template

import matplotlib.dates as mdates
import numpy
from importlib import resources
import svgwrite as svg
from matplotlib import pyplot

from .conditions import Conditions
from .objects.messier import Messier
from .objects.planets import Planets
from .utils import Utils
from .constants import ObjectTableLabels

logger = logging.getLogger(__name__)


class Observation:
  NOTIFICATION_TEMPLATE = str(resources.files('apts').joinpath('templates/notification.html.template'))

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
                       for value in self.conditions.max_return.split(":")]
    time_limit = self.start.replace(
      hour=max_return_time[0], minute=max_return_time[1], second=max_return_time[2])
    self.time_limit = time_limit if time_limit > self.start else time_limit + \
                                                                 timedelta(days=1)

  def get_visible_messier(self, **args):
    self.local_messier.compute()
    return self.local_messier.get_visible(self.conditions, self.start, self.time_limit, **args)

  def get_visible_planets(self, **args):
    return self.local_planets.get_visible(self.conditions, self.start, self.time_limit, **args)

  def plot_visible_planets_svg(self, **args):
    visible_planets = self.get_visible_planets(**args)
    dwg = svg.Drawing()
    # Set y offset to biggest planet
    y = int(visible_planets[['Size']].max() + 12)
    # Set x offset to constant value
    x = 20
    # Set delta to constant value
    minimal_delta = 52
    last_radius = None
    for planet in visible_planets[['Name', 'Size', 'Phase']].values:
      name, radius, phase = planet[0], planet[1], str(round(planet[2], 2))
      if last_radius is None:
        y += radius
        x += radius
      else:
        x += max(radius + last_radius + 10, minimal_delta)
      last_radius = radius
      dwg.add(svg.shapes.Circle(center=(x, y), r=radius, stroke="black", stroke_width="1", fill="#e4e4e4"))
      dwg.add(svg.text.Text(name, insert=(x, y + radius + 15), text_anchor='middle'))
      dwg.add(svg.text.Text(phase + '%', insert=(x, y - radius - 4), text_anchor='middle'))
    return dwg.tostring()

  def plot_visible_planets(self):
    try:
      from IPython.display import SVG
    except:
      logger.warning("You can plot images only in Ipython notebook!")
      return
    return SVG(self.plot_visible_planets_svg())

  def _generate_plot_messier(self, **args):
    messier = self.get_visible_messier(
    )[[ObjectTableLabels.MESSIER,
       ObjectTableLabels.TRANSIT,
       ObjectTableLabels.ALTITUDE,
       ObjectTableLabels.WIDTH]]
    plot = messier.plot(
      x=ObjectTableLabels.TRANSIT,
      y=ObjectTableLabels.ALTITUDE,
      marker='o',
      # markersize = messier['Width'],
      linestyle='none',
      xlim=[self.start - timedelta(minutes=15),
            self.time_limit + timedelta(minutes=15)],
      ylim=(0, 90), **args)

    last_position = [0, 0]
    offset_index = 0
    offsets = [(-25, -12), (5, 5), (-25, 5), (5, -12)]
    for obj in messier.values:
      distance = (((mdates.date2num(
        obj[1]) - last_position[0]) * 100) ** 2 + (obj[2] - last_position[1]) ** 2) ** 0.5
      offset_index = offset_index + (1 if distance < 5 else 0)
      plot.annotate(obj[0],
                    (mdates.date2num(obj[1]), obj[2]),
                    xytext=offsets[offset_index % len(offsets)],
                    textcoords='offset points')
      last_position = [mdates.date2num(obj[1]), obj[2]]
    self._mark_observation(plot)
    self._mark_good_conditions(
      plot, self.conditions.min_object_altitude, 90)
    Utils.annotate_plot(plot, 'Altitude [°]')
    return plot.get_figure()

  def _normalize_dates(self, start, stop):
    now = datetime.now(timezone.utc).astimezone(self.place.local_timezone)
    new_start = start if start < stop else now
    new_stop = stop
    return (new_start, new_stop)

  def plot_weather(self, **args):
    if self.place.weather is None:
      self.place.get_weather()
    return self._generate_plot_weather(**args)

  def plot_messier(self, **args):
    return self._generate_plot_messier(**args)

  def _compute_weather_goodnse(self):
    # Get critical weather data
    data = self.place.weather.get_critical_data(self.start, self.stop)
    # Get only data defore time limit
    data = data[data.time <= self.time_limit]
    all_hours = len(data)
    # Get hours with good conditions
    result = data[
      (data.cloudCover < self.conditions.max_clouds) &
      (data.precipProbability < self.conditions.max_precipitation_probability) &
      (data.windSpeed < self.conditions.max_wind) &
      (data.temperature > self.conditions.min_temperature) &
      (data.temperature < self.conditions.max_temperature)]
    good_hours = len(result)
    logger.debug("Good hours: {} and all hours: {}".format(good_hours, all_hours))
    # Return relative % of good hours
    return good_hours / all_hours * 100

  def is_weather_good(self):
    if self.place.weather is None:
      self.place.get_weather()
    return self._compute_weather_goodnse() > self.conditions.min_weather_goodness

  def to_html(self):
    with open(Observation.NOTIFICATION_TEMPLATE) as template_file:
      template = Template(template_file.read())
      data = {
        "title": "APTS",
        "start": Utils.format_date(self.start),
        "stop": Utils.format_date(self.stop),
        "planets_count": len(self.get_visible_planets()),
        "messier_count": len(self.get_visible_messier()),
        "planets_table": self.get_visible_planets().to_html(),
        "messier_table": self.get_visible_messier().to_html(),
        "equipment_table": self.equipment.data().to_html(),
        "place_name": self.place.name,
        "lat": numpy.rad2deg(self.place.lat),
        "lon": numpy.rad2deg(self.place.lon)
      }
      return str(template.substitute(data))

  def _mark_observation(self, plot):
    # Check if there is a plot
    if plot is None:
      return
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
    # Check if there is a plot
    if plot is None:
      return
    plot.axhspan(minimal, maximal, color='green', alpha=0.1)

  def _generate_plot_weather(self, **args):
    fig, axes = pyplot.subplots(nrows=4, ncols=2, figsize=(13, 18))
    # Clouds
    plt = self.place.weather.plot_clouds(ax=axes[0, 0])
    self._mark_observation(plt)
    self._mark_good_conditions(plt, 0, self.conditions.max_clouds)
    # Cloud summary
    plt = self.place.weather.plot_clouds_summary(ax=axes[0, 1])
    # Precipation
    plt = self.place.weather.plot_precipitation(ax=axes[1, 0])
    self._mark_observation(plt)
    self._mark_good_conditions(
      plt, 0, self.conditions.max_precipitation_probability)
    # precipitation type summary
    plt = self.place.weather.plot_precipitation_type_summary(ax=axes[1, 1])
    # Temperature
    plt = self.place.weather.plot_temperature(ax=axes[2, 0])
    self._mark_observation(plt)
    self._mark_good_conditions(
      plt, self.conditions.min_temperature, self.conditions.max_temperature)
    # Wind
    plt = self.place.weather.plot_wind(ax=axes[2, 1])
    self._mark_observation(plt)
    self._mark_good_conditions(plt, 0, self.conditions.max_wind)
    # Pressure
    plt = self.place.weather.plot_pressure_and_ozone(ax=axes[3, 0])
    self._mark_observation(plt)
    # Visibility
    plt = self.place.weather.plot_visibility(ax=axes[3, 1])
    self._mark_observation(plt)
    fig.tight_layout()
    return fig
