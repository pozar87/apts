from typing import Optional
from apts.constants.twilight import Twilight


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
    # Maximal fog
    MAX_FOG = 5  # [%], range [0,100]
    # Minimal sky brightness
    MIN_SQM = 19.0  # [mag/arcsec²], range [10,22]
    # Maximal astronomical seeing
    MAX_SEEING = 2.5  # [arcsec], range [0.5,5]
    # Max acceptable hour of return
    MAX_RETURN = "02:00:00"
    # Start time for observation
    START_TIME: Optional[str] = None
    # Minimal object (i.e. Messier) altitude (https://en.wikipedia.org/wiki/Horizontal_coordinate_system)
    MIN_OBJECT_ALTITUDE = 15  # [°], range [0,90]
    # Minimal and maximal object azimuth
    MIN_OBJECT_AZIMUTH = 0  # [°], range [0,360]
    MAX_OBJECT_AZIMUTH = 360  # [°], range [0,360]
    # Maximal object brightness (https://en.wikipedia.org/wiki/Apparent_magnitude)
    MAX_OBJECT_MAGNITUDE = 9  # [m], range [∞,-∞]
    # Maximal moon illumination
    MAX_MOON_ILLUMINATION = 50  # [%], range [0,100]
    # Twilight setting for observation start
    TWILIGHT = Twilight.NAUTICAL
    # Minimal aurora
    MIN_AURORA = 0  # [%], range [0,100]
    # Path to horizon file (.hrz)
    HORIZON_FILE: Optional[str] = None
    # Content of horizon file
    HORIZON_CONTENT: Optional[str] = None
