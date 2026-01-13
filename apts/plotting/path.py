from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from ..observations import Observation


def plot_sun_and_moon_path(
    observation: "Observation", dark_mode_override: Optional[bool] = None, **args
):
    if observation.sun_observation:
        return observation.place.plot_sun_path(dark_mode_override, **args)
    else:
        return observation.place.plot_moon_path(dark_mode_override, **args)
