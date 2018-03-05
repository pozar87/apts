class Conditions:
  """
  Class containing acceptable thresholds for observation quality.
  """
  # Fraction of cloud cover
  MAX_CLOUDS = 0.2  # unitless, range [0,1]
  # Acceptable chance and intensity of atmospheric precipitation
  MAX_PRECIPATION_PROBABILITY = 0.05  # unitless, range [0,1]
  MAX_PRECIPATION_INTENSITY = 0.05  # [mm], range [0,∞)
  # Acceptable wind speed
  MAX_WIND = 10  # [km/h], range [0,∞)
  # Acceptable temperature range
  MIN_TEMPERATURE = 0  # [C°]
  MAX_TEMPERATURE = 20  # [C°]
  # Threshold for abstract measurement of weather goodness. 0 - crappy weather, 1 - best weather
  MIN_WEATHER_GOODNESS = 0.8  # unitless, range [0,1]
  # Max acceptable hour of return
  MAX_RETURN = "01:00:00"
  # Minimal object (i.e. Messier) altitude (https://en.wikipedia.org/wiki/Horizontal_coordinate_system)
  MIN_OBJECT_ALTITUDE = 15  # [°], range [0,90]
  # Maximal object brightness (https://en.wikipedia.org/wiki/Apparent_magnitude)
  MAX_OBJECT_MAGNITUDE = 9  # [m], range [∞,-∞]
