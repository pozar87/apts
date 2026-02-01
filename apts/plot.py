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
    "plot_skymap",
    "plot_visible_planets",
    "plot_visible_planets_svg",
    "plot_sun_and_moon_path",
]
