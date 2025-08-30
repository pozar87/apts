class DefaultConditions:
  """
  Class containing default thresholds for observation quality.
  """
  # Fraction of cloud cover
  MAX_CLOUDS = 20  # [%], range [0,100]
  # Acceptable chance and intensity of atmospheric precipitation
  MAX_PRECIPITATION_PROBABILITY = 5  # [%], range [0,100]
  MAX_PRECIPITATION_INTENSITY = 5  # [mm], range [0,∞)
  # Acceptable wind speed
  MAX_WIND = 10  # [km/h], range [0,∞)
  # Acceptable temperature range
  MIN_TEMPERATURE = 0  # [C°]
  MAX_TEMPERATURE = 20  # [C°]
  # Threshold for abstract measurement of weather goodness. 0 - crappy weather, 1 - best weather
  MIN_WEATHER_GOODNESS = 80  # [%], range [0,100]
  # Minimal visibility
  MIN_VISIBILITY = 10  # [km], range [0,∞)
  # Max acceptable hour of return
  MAX_RETURN = "02:00:00"
  # Minimal object (i.e. Messier) altitude (https://en.wikipedia.org/wiki/Horizontal_coordinate_system)
  MIN_OBJECT_ALTITUDE = 15  # [°], range [0,90]
  # Minimal and maximal object azimuth
  MIN_OBJECT_AZIMUTH = 0  # [°], range [0,360]
  MAX_OBJECT_AZIMUTH = 360  # [°], range [0,360]
  # Maximal object brightness (https://en.wikipedia.org/wiki/Apparent_magnitude)
  MAX_OBJECT_MAGNITUDE = 9  # [m], range [∞,-∞]


class Conditions:
  """
  Class containing acceptable thresholds for observation quality.
  """

  def __init__(self,
               max_clouds=DefaultConditions.MAX_CLOUDS,
               max_precipitation_probability=DefaultConditions.MAX_PRECIPITATION_PROBABILITY,
               max_precipitation_intensity=DefaultConditions.MAX_PRECIPITATION_INTENSITY,
               max_wind=DefaultConditions.MAX_WIND,
               min_temperature=DefaultConditions.MIN_TEMPERATURE,
               max_temperature=DefaultConditions.MAX_TEMPERATURE,
               min_weather_goodness=DefaultConditions.MIN_WEATHER_GOODNESS,
               min_visibility=DefaultConditions.MIN_VISIBILITY,
               max_return=DefaultConditions.MAX_RETURN,
               min_object_altitude=DefaultConditions.MIN_OBJECT_ALTITUDE,
               max_object_magnitude=DefaultConditions.MAX_OBJECT_MAGNITUDE,
               min_object_azimuth=DefaultConditions.MIN_OBJECT_AZIMUTH,
               max_object_azimuth=DefaultConditions.MAX_OBJECT_AZIMUTH
               ):
    self.max_clouds = max_clouds
    self.max_precipitation_probability = max_precipitation_probability
    self.max_precipitation_intensity = max_precipitation_intensity
    self.max_wind = max_wind
    self.min_temperature = min_temperature
    self.max_temperature = max_temperature
    self.min_weather_goodness = min_weather_goodness
    self.min_visibility = min_visibility
    self.max_return = max_return
    self.min_object_altitude = min_object_altitude
    self.max_object_magnitude = max_object_magnitude
    self.min_object_azimuth = min_object_azimuth
    self.max_object_azimuth = max_object_azimuth
