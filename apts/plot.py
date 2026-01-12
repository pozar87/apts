from typing import TYPE_CHECKING, Optional

from apts.plotting.altitude import generate_plot_messier, generate_plot_planets
from apts.plotting.planets import plot_visible_planets, plot_visible_planets_svg
from apts.plotting.skymap import plot_skymap, plot_sun_and_moon_path
from apts.plotting.weather import generate_plot_weather

if TYPE_CHECKING:
    from .observations import Observation


def plot_messier(
    observation: "Observation", dark_mode_override: Optional[bool] = None, **args
):
    return generate_plot_messier(
        observation, dark_mode_override=dark_mode_override, **args
    )


def plot_planets(
    observation: "Observation", dark_mode_override: Optional[bool] = None, **args
):
    return generate_plot_planets(
        observation, dark_mode_override=dark_mode_override, **args
    )


def plot_weather(
    observation: "Observation", dark_mode_override: Optional[bool] = None, **args
):
    if observation.place.weather is None:
        observation.place.get_weather()
    return generate_plot_weather(
        observation, dark_mode_override=dark_mode_override, **args
    )




__all__ = [
    "plot_messier",
    "plot_planets",
    "plot_weather",
    "plot_skymap",
    "plot_visible_planets",
    "plot_visible_planets_svg",
    "plot_sun_and_moon_path",
]
