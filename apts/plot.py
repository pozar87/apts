import logging
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .observations import Observation
    from .conditions import Conditions


logger = logging.getLogger(__name__)


class NullPlotter:
    """
    A null object for the plotter.
    Silently accepts any method call (e.g. plot.weather(), plot.messier())
    and returns None, preventing AttributeErrors when plotting is unavailable.
    """

    def __getattr__(self, name):
        # Optional: Log that a plot method was skipped
        # logger.debug(f"NullPlotter: Ignoring call to '{name}'")
        return lambda *args, **kwargs: None


class Plotter:
    """
    Real plotter that delegates to the plotting modules.
    """

    def __init__(self, observation: "Observation"):
        self.observation = observation
        # Trigger ImportError if matplotlib is missing
        import matplotlib.pyplot  # noqa: F401

    def messier(self, **args):
        return plot_messier(self.observation, **args)

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

    def skymap(self, **args):
        return plot_skymap(self.observation, **args)

    def visible_planets(self, **args):
        return plot_visible_planets(self.observation, **args)

    def visible_planets_svg(self, **args):
        return plot_visible_planets_svg(self.observation, **args)

    def sun_and_moon_path(self, **args):
        return plot_sun_and_moon_path(self.observation, **args)


def plot_messier(
    observation: "Observation", dark_mode_override: Optional[bool] = None, **args
):
    from .plotting.altitude import generate_plot_messier

    return generate_plot_messier(
        observation, dark_mode_override=dark_mode_override, **args
    )


def plot_planets(
    observation: "Observation", dark_mode_override: Optional[bool] = None, **args
):
    from .plotting.altitude import generate_plot_planets

    return generate_plot_planets(
        observation, dark_mode_override=dark_mode_override, **args
    )


def plot_weather(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    from .plotting.weather import generate_plot_weather

    if observation.place.weather is None:
        observation.place.get_weather()
    return generate_plot_weather(
        observation,
        dark_mode_override=dark_mode_override,
        conditions=conditions,
        **args,
    )


def plot_clouds(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    from .plotting.weather import generate_plot_clouds

    if observation.place.weather is None:
        observation.place.get_weather()
    return generate_plot_clouds(
        observation,
        dark_mode_override=dark_mode_override,
        conditions=conditions,
        **args,
    )


def plot_clouds_summary(
    observation: "Observation", dark_mode_override: Optional[bool] = None, **args
):
    from .plotting.weather import generate_plot_clouds_summary

    if observation.place.weather is None:
        observation.place.get_weather()
    return generate_plot_clouds_summary(
        observation, dark_mode_override=dark_mode_override, **args
    )


def plot_precipitation(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    from .plotting.weather import generate_plot_precipitation

    if observation.place.weather is None:
        observation.place.get_weather()
    return generate_plot_precipitation(
        observation,
        dark_mode_override=dark_mode_override,
        conditions=conditions,
        **args,
    )


def plot_precipitation_type_summary(
    observation: "Observation", dark_mode_override: Optional[bool] = None, **args
):
    from .plotting.weather import generate_plot_precipitation_type_summary

    if observation.place.weather is None:
        observation.place.get_weather()
    return generate_plot_precipitation_type_summary(
        observation, dark_mode_override=dark_mode_override, **args
    )


def plot_temperature(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    from .plotting.weather import generate_plot_temperature

    if observation.place.weather is None:
        observation.place.get_weather()
    return generate_plot_temperature(
        observation,
        dark_mode_override=dark_mode_override,
        conditions=conditions,
        **args,
    )


def plot_wind(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    from .plotting.weather import generate_plot_wind

    if observation.place.weather is None:
        observation.place.get_weather()
    return generate_plot_wind(
        observation,
        dark_mode_override=dark_mode_override,
        conditions=conditions,
        **args,
    )


def plot_pressure_and_ozone(
    observation: "Observation", dark_mode_override: Optional[bool] = None, **args
):
    from .plotting.weather import generate_plot_pressure_and_ozone

    if observation.place.weather is None:
        observation.place.get_weather()
    return generate_plot_pressure_and_ozone(
        observation, dark_mode_override=dark_mode_override, **args
    )


def plot_visibility(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    from .plotting.weather import generate_plot_visibility

    if observation.place.weather is None:
        observation.place.get_weather()
    return generate_plot_visibility(
        observation,
        dark_mode_override=dark_mode_override,
        conditions=conditions,
        **args,
    )


def plot_moon_illumination(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    from .plotting.weather import generate_plot_moon_illumination

    if observation.place.weather is None:
        observation.place.get_weather()
    return generate_plot_moon_illumination(
        observation,
        dark_mode_override=dark_mode_override,
        conditions=conditions,
        **args,
    )


def plot_fog(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    from .plotting.weather import generate_plot_fog

    if observation.place.weather is None:
        observation.place.get_weather()
    return generate_plot_fog(
        observation,
        dark_mode_override=dark_mode_override,
        conditions=conditions,
        **args,
    )


def plot_aurora(
    observation: "Observation",
    dark_mode_override: Optional[bool] = None,
    conditions: Optional["Conditions"] = None,
    **args,
):
    from .plotting.weather import generate_plot_aurora

    if observation.place.weather is None:
        observation.place.get_weather()
    return generate_plot_aurora(
        observation,
        dark_mode_override=dark_mode_override,
        conditions=conditions,
        **args,
    )


def plot_skymap(observation: "Observation", **args):
    from .plotting.skymap import plot_skymap

    return plot_skymap(observation, **args)


def plot_visible_planets(
    observation: "Observation", dark_mode_override: Optional[bool] = None, **args
):
    from .plotting.planets import plot_visible_planets

    return plot_visible_planets(
        observation, dark_mode_override=dark_mode_override, **args
    )


def plot_visible_planets_svg(
    observation: "Observation", dark_mode_override: Optional[bool] = None, **args
):
    from .plotting.planets import plot_visible_planets_svg

    return plot_visible_planets_svg(
        observation, dark_mode_override=dark_mode_override, **args
    )


def plot_sun_and_moon_path(
    observation: "Observation", dark_mode_override: Optional[bool] = None, **args
):
    from .plotting.path import plot_sun_and_moon_path

    return plot_sun_and_moon_path(
        observation, dark_mode_override=dark_mode_override, **args
    )


__all__ = [
    "Plotter",
    "NullPlotter",
    "plot_messier",
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
    "plot_skymap",
    "plot_visible_planets",
    "plot_visible_planets_svg",
    "plot_sun_and_moon_path",
]
