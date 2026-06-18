from .base import BasePlottingMixIn
from .weather import WeatherPlottingMixIn
from .celestial import CelestialPlottingMixIn


class PlottingMixIn(BasePlottingMixIn, WeatherPlottingMixIn, CelestialPlottingMixIn):
    pass
