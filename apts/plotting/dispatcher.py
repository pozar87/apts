import logging
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from ..observations import Observation
    from ..conditions import Conditions

from .wrappers.objects import (
    plot_messier,
    plot_ngc,
    plot_planets,
    plot_skymap,
    plot_visible_planets,
    plot_visible_planets_svg,
    plot_sun_and_moon_path,
    plot_jovian_moons,
)
from .wrappers.weather import (
    plot_weather,
    plot_clouds,
    plot_clouds_summary,
    plot_precipitation,
    plot_precipitation_type_summary,
    plot_temperature,
    plot_wind,
    plot_pressure_and_ozone,
    plot_visibility,
    plot_moon_illumination,
    plot_fog,
    plot_aurora,
    plot_seeing,
    plot_sqm,
    plot_weather_summary,
)

logger = logging.getLogger(__name__)


class NullPlotter:
    """
    A null object for the plotter.
    Silently accepts any method call (e.g. plot.weather(), plot.messier())
    and returns None, preventing AttributeErrors when plotting is unavailable.
    """

    def __getattr__(self, name):
        return lambda *args, **kwargs: None


class Plotter:
    """
    Real plotter that delegates to the plotting modules.
    """

    def __init__(self, observation: "Observation"):
        self.observation = observation
        # Trigger ImportError if matplotlib is missing
        import matplotlib.pyplot  # noqa: F401

        from .utils import setup_plotting_style

        setup_plotting_style()

    def messier(self, **args):
        return plot_messier(self.observation, **args)

    def ngc(self, **args):
        return plot_ngc(self.observation, **args)

    def planets(self, **args):
        return plot_planets(self.observation, **args)

    def weather(self, conditions: Optional["Conditions"] = None, **args):
        return plot_weather(self.observation, conditions=conditions, **args)

    def clouds(self, conditions: Optional["Conditions"] = None, **args):
        return plot_clouds(self.observation, conditions=conditions, **args)

    def clouds_summary(self, **args):
        return plot_clouds_summary(self.observation, **args)

    def precipitation(self, conditions: Optional["Conditions"] = None, **args):
        return plot_precipitation(self.observation, conditions=conditions, **args)

    def precipitation_type_summary(self, **args):
        return plot_precipitation_type_summary(self.observation, **args)

    def temperature(self, conditions: Optional["Conditions"] = None, **args):
        return plot_temperature(self.observation, conditions=conditions, **args)

    def wind(self, conditions: Optional["Conditions"] = None, **args):
        return plot_wind(self.observation, conditions=conditions, **args)

    def pressure_and_ozone(self, **args):
        return plot_pressure_and_ozone(self.observation, **args)

    def visibility(self, conditions: Optional["Conditions"] = None, **args):
        return plot_visibility(self.observation, conditions=conditions, **args)

    def moon_illumination(self, conditions: Optional["Conditions"] = None, **args):
        return plot_moon_illumination(self.observation, conditions=conditions, **args)

    def fog(self, conditions: Optional["Conditions"] = None, **args):
        return plot_fog(self.observation, conditions=conditions, **args)

    def aurora(self, conditions: Optional["Conditions"] = None, **args):
        return plot_aurora(self.observation, conditions=conditions, **args)

    def seeing(self, conditions: Optional["Conditions"] = None, **args):
        return plot_seeing(self.observation, conditions=conditions, **args)

    def sqm(self, conditions: Optional["Conditions"] = None, **args):
        return plot_sqm(self.observation, conditions=conditions, **args)

    def weather_summary(self, conditions: Optional["Conditions"] = None, **args):
        return plot_weather_summary(self.observation, conditions=conditions, **args)

    def skymap(self, **args):
        return plot_skymap(self.observation, **args)

    def skymap_texture(self, **args):
        return plot_skymap(self.observation, texture_mode=True, **args)

    def visible_planets(self, **args):
        return plot_visible_planets(self.observation, **args)

    def visible_planets_svg(self, **args):
        return plot_visible_planets_svg(self.observation, **args)

    def sun_and_moon_path(self, **args):
        return plot_sun_and_moon_path(self.observation, **args)

    def jovian_moons(self, **args):
        return plot_jovian_moons(self.observation, **args)


__all__ = [
    "Plotter",
    "NullPlotter",
    "plot_messier",
    "plot_ngc",
    "plot_planets",
    "plot_weather",
    "plot_clouds",
    "plot_clouds_summary",
    "plot_precipitation",
    "plot_precipitation_type_summary",
    "plot_temperature",
    "plot_wind",
    "plot_pressure_and_ozone",
    "plot_visibility",
    "plot_moon_illumination",
    "plot_fog",
    "plot_aurora",
    "plot_seeing",
    "plot_sqm",
    "plot_weather_summary",
    "plot_skymap",
    "plot_visible_planets",
    "plot_visible_planets_svg",
    "plot_sun_and_moon_path",
    "plot_jovian_moons",
]
