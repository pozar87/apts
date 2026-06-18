from .base import BasePlottingMixIn
from .celestial import CelestialPlottingMixIn
from .weather import WeatherPlottingMixIn


class PlottingMixIn(
    BasePlottingMixIn,
    WeatherPlottingMixIn,
    CelestialPlottingMixIn,
):
    """
    Combined plotting mixin for observations.
    Decomposed into specialized mixins for better maintainability.
    """

    pass


__all__ = ["PlottingMixIn", "BasePlottingMixIn", "WeatherPlottingMixIn", "CelestialPlottingMixIn"]
