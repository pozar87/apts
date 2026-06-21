from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from ...observations import Observation

def plot_messier(
    observation: "Observation", dark_mode_override: Optional[bool] = None, **args
):
    from ..altitude import generate_plot_messier

    return generate_plot_messier(
        observation, dark_mode_override=dark_mode_override, **args
    )


def plot_ngc(
    observation: "Observation", dark_mode_override: Optional[bool] = None, **args
):
    from ..altitude import generate_plot_ngc

    return generate_plot_ngc(
        observation, dark_mode_override=dark_mode_override, **args
    )


def plot_planets(
    observation: "Observation", dark_mode_override: Optional[bool] = None, **args
):
    from ..altitude import generate_plot_planets

    return generate_plot_planets(
        observation, dark_mode_override=dark_mode_override, **args
    )

def plot_skymap(observation: "Observation", **args):
    from ..skymap import plot_skymap as base_plot_skymap

    return base_plot_skymap(observation, **args)


def plot_visible_planets(
    observation: "Observation", dark_mode_override: Optional[bool] = None, **args
):
    from ..planets import plot_visible_planets as base_plot_visible_planets

    return base_plot_visible_planets(
        observation, dark_mode_override=dark_mode_override, **args
    )


def plot_visible_planets_svg(
    observation: "Observation", dark_mode_override: Optional[bool] = None, **args
):
    from ..planets import plot_visible_planets_svg as base_plot_visible_planets_svg

    return base_plot_visible_planets_svg(
        observation, dark_mode_override=dark_mode_override, **args
    )


def plot_sun_and_moon_path(
    observation: "Observation", dark_mode_override: Optional[bool] = None, **args
):
    from ..path import plot_sun_and_moon_path as base_plot_sun_and_moon_path

    return base_plot_sun_and_moon_path(
        observation, dark_mode_override=dark_mode_override, **args
    )


def plot_jovian_moons(
    observation: "Observation", dark_mode_override: Optional[bool] = None, **args
):
    from ..jovian_moons import generate_plot_jovian_moons

    return generate_plot_jovian_moons(
        observation, dark_mode_override=dark_mode_override, **args
    )
