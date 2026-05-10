from typing import TYPE_CHECKING, Optional
from . import sun
from . import moon
from .sun import generate_plot_sun_path
from .moon import generate_plot_moon_path
from .utils import MOON_FONT

if TYPE_CHECKING:
    from ...observations import Observation

def plot_sun_and_moon_path(
    observation: "Observation", dark_mode_override: Optional[bool] = None, **args
):
    if observation.sun_observation:
        return sun.generate_plot_sun_path(observation.place, dark_mode_override, **args)
    else:
        return moon.generate_plot_moon_path(observation.place, dark_mode_override, **args)

__all__ = [
    "plot_sun_and_moon_path",
    "generate_plot_sun_path",
    "generate_plot_moon_path",
    "MOON_FONT",
]
