from typing import TYPE_CHECKING, Any, Optional

from matplotlib import axes

from apts.constants.plot import CoordinateSystem
from apts.plotting.skymap_objects import (
    _plot_bright_stars_on_skymap,
    _plot_messier_on_skymap,
    _plot_ngc_on_skymap,
    _plot_planets_on_skymap,
    _plot_solar_system_object_on_skymap,
    _plot_stars_on_skymap,
)

if TYPE_CHECKING:
    from ...observations import Observation


def _generate_texture_skymap(
    observation: "Observation",
    ax: axes.Axes,
    style: dict,
    observer: Any,
    effective_dark_mode: bool,
    star_magnitude_limit: Optional[float],
    plot_stars: bool,
    plot_messier: bool,
    plot_ngc: bool,
    plot_planets: bool,
    plot_sun: bool,
    plot_moon: bool,
    coordinate_system: CoordinateSystem,
    plot_labels: bool = False,
):
    fig = ax.get_figure()
    if fig:
        fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
        # Remove all margins
        fig.subplots_adjust(left=0, right=1, bottom=0, top=1)

    ax.set_facecolor(style["AXES_FACE_COLOR"])
    # Hide all axis decorations
    ax.set_axis_off()

    if coordinate_system == CoordinateSystem.HORIZONTAL:
        ax.set_xlim(0, 360)
        ax.set_ylim(-90, 90)
        # Width 360, Height 180. aspect=1 gives 2:1 physical ratio.
        ax.set_aspect("equal", adjustable="box")
    else:  # EQUATORIAL
        ax.set_xlim(24, 0)  # RA usually increases to the left
        ax.set_ylim(-90, 90)
        # 1 hour (x) = 15 degrees. We want 1:1 degree ratio.
        ax.set_aspect(1.0 / 15.0, adjustable="box")

    # Plot everything with ignore_horizon=True and the specified plot_labels setting
    if plot_stars:
        _plot_stars_on_skymap(
            observation,
            ax,
            observer,
            star_magnitude_limit,
            is_polar=False,
            style=style,
            coordinate_system=coordinate_system,
            plot_labels=plot_labels,
            ignore_horizon=True,
        )
        _plot_bright_stars_on_skymap(
            observation,
            ax,
            observer,
            is_polar=False,
            style=style,
            coordinate_system=coordinate_system,
            plot_labels=plot_labels,
            ignore_horizon=True,
        )
    if plot_messier:
        _plot_messier_on_skymap(
            observation,
            ax,
            observer,
            is_polar=False,
            target_name="",  # No specific target
            coordinate_system=coordinate_system,
            plot_labels=plot_labels,
            ignore_horizon=True,
        )
    if plot_ngc:
        _plot_ngc_on_skymap(
            observation,
            ax,
            observer,
            is_polar=False,
            target_name="",
            star_magnitude_limit=star_magnitude_limit,
            coordinate_system=coordinate_system,
            plot_labels=plot_labels,
            ignore_horizon=True,
        )
    if plot_planets:
        _plot_planets_on_skymap(
            observation,
            ax,
            observer,
            is_polar=False,
            effective_dark_mode=effective_dark_mode,
            style=style,
            target_name="",
            coordinate_system=coordinate_system,
            plot_labels=plot_labels,
            ignore_horizon=True,
        )
    if plot_sun:
        _plot_solar_system_object_on_skymap(
            observation,
            ax,
            observer,
            is_polar=False,
            style=style,
            object_name="Sun",
            coordinate_system=coordinate_system,
            plot_labels=plot_labels,
            ignore_horizon=True,
        )
    if plot_moon:
        _plot_solar_system_object_on_skymap(
            observation,
            ax,
            observer,
            is_polar=False,
            style=style,
            object_name="Moon",
            coordinate_system=coordinate_system,
            plot_labels=plot_labels,
            ignore_horizon=True,
        )

    return fig
