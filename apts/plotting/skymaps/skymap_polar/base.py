from typing import TYPE_CHECKING, Any, cast

import numpy
from matplotlib import axes

from apts.constants.plot import CoordinateSystem
from apts.i18n import gettext_

from ..utils import parse_target_geometry, plot_skymap_catalogs, setup_polar_ax
from .overlays import _plot_polar_visibility_overlay

if TYPE_CHECKING:
    from ....observations import Observation


def _setup_polar_skymap_axes(
    observation: "Observation",
    ax: axes.Axes,
    style: dict,
    coordinate_system: CoordinateSystem,
):
    """Sets up the background colors and basic axes configuration for a polar skymap."""
    fig = ax.get_figure()
    if fig:
        fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
    ax.set_facecolor(style["AXES_FACE_COLOR"])

    setup_polar_ax(observation, ax, style, coordinate_system)


def _plot_polar_skymap_target(
    ax: axes.Axes,
    observer: Any,
    target_name: str,
    target_object: Any,
    target_object_data: Any,
    is_sh: bool,
    coordinate_system: CoordinateSystem,
):
    """Plots the target object with highlighting and annotation."""
    target_alt, target_az, _ = observer.observe(target_object).apparent().altaz()
    target_ra, target_dec, _ = observer.observe(target_object).apparent().radec()
    polar_ax = cast(Any, ax)

    if coordinate_system == CoordinateSystem.HORIZONTAL and bool(
        numpy.any(target_alt.degrees > 0)
    ):
        if target_object_data is not None:
            width_deg, height_deg, _, _, _ = parse_target_geometry(
                target_object, target_object_data, observer
            )
            size = (width_deg + height_deg) / 2 * 100
            polar_ax.scatter(
                target_az.radians,
                90 - target_alt.degrees,
                s=size,
                color="yellow",
                marker="+",
            )
        else:
            polar_ax.scatter(
                target_az.radians,
                90 - target_alt.degrees,
                s=200,
                facecolors="none",
                edgecolors="yellow",
                marker="o",
                linewidths=2,
            )
        polar_ax.annotate(
            gettext_(target_name),
            (target_az.radians, 90 - target_alt.degrees),
            textcoords="offset points",
            xytext=(0, 15),
            color="yellow",
            ha="center",
            fontsize=12,
        )
    elif coordinate_system == CoordinateSystem.EQUATORIAL:
        target_radius = 90 + target_dec.degrees if is_sh else 90 - target_dec.degrees
        if target_object_data is not None:
            width_deg, height_deg, _, _, _ = parse_target_geometry(
                target_object, target_object_data, observer
            )
            size = (width_deg + height_deg) / 2 * 100
            polar_ax.scatter(
                target_ra.radians,
                target_radius,
                s=size,
                color="yellow",
                marker="+",
            )
        else:
            polar_ax.scatter(
                target_ra.radians,
                target_radius,
                s=200,
                facecolors="none",
                edgecolors="yellow",
                marker="o",
                linewidths=2,
            )
        polar_ax.annotate(
            gettext_(target_name),
            (target_ra.radians, target_radius),
            textcoords="offset points",
            xytext=(0, 15),
            color="yellow",
            ha="center",
            fontsize=12,
        )


def _generate_polar_skymap(
    observation: "Observation",
    ax: axes.Axes,
    style: dict,
    target_name: str,
    target_object: Any,
    target_object_data: Any,
    observer: Any,
    generation_time_str: str,
    effective_dark_mode: bool,
    star_magnitude_limit: float | None,
    plot_stars: bool,
    plot_messier: bool,
    plot_ngc: bool,
    plot_planets: bool,
    plot_sun: bool,
    plot_moon: bool,
    flipped_horizontally: bool,
    flipped_vertically: bool,
    coordinate_system: CoordinateSystem,
):
    """Generates a polar skymap for a given observation and target."""
    _setup_polar_skymap_axes(observation, ax, style, coordinate_system)

    is_sh = observation.place.lat_decimal < 0
    good_condition_color = style.get(
        "GOOD_CONDITION_HL_COLOR",
        "#90EE90" if not effective_dark_mode else "#007447",
    )

    _plot_polar_visibility_overlay(
        observation,
        ax,
        style,
        coordinate_system,
        observer,
        is_sh,
        good_condition_color,
    )

    plot_skymap_catalogs(
        observation,
        ax,
        observer,
        style,
        target_name,
        target_object,
        is_polar=True,
        coordinate_system=coordinate_system,
        zoom_deg=None,
        star_magnitude_limit=star_magnitude_limit,
        effective_dark_mode=effective_dark_mode,
        flipped_horizontally=flipped_horizontally,
        flipped_vertically=flipped_vertically,
        plot_stars=plot_stars,
        plot_messier=plot_messier,
        plot_ngc=plot_ngc,
        plot_planets=plot_planets,
        plot_sun=plot_sun,
        plot_moon=plot_moon,
    )

    _plot_polar_skymap_target(
        ax,
        observer,
        target_name,
        target_object,
        target_object_data,
        is_sh,
        coordinate_system,
    )

    ax.set_title(
        gettext_("Skymap for {target_name} (Generated: {generation_time_str})").format(
            target_name=gettext_(target_name), generation_time_str=generation_time_str
        ),
        color=style["TEXT_COLOR"],
    )

    return ax.get_figure()
