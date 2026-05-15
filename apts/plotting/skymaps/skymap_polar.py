from typing import TYPE_CHECKING, Any, Optional, cast

import numpy
from matplotlib import axes
from skyfield.api import Star as SkyfieldStar
from skyfield.units import Angle

from apts.constants.plot import CoordinateSystem
from apts.i18n import gettext_
from apts.plotting.skymap_objects import (
    _plot_bright_stars_on_skymap,
    _plot_messier_on_skymap,
    _plot_ngc_on_skymap,
    _plot_planets_on_skymap,
    _plot_solar_system_object_on_skymap,
    _plot_stars_on_skymap,
)
from .utils import setup_polar_ax

from ...constants import ObjectTableLabels

if TYPE_CHECKING:
    from ...observations import Observation


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


def _plot_polar_visibility_overlay(
    observation: "Observation",
    ax: axes.Axes,
    style: dict,
    coordinate_system: CoordinateSystem,
    observer: Any,
    is_sh: bool,
    good_condition_color: str,
):
    """Plots the visibility overlay (horizon or altitude/azimuth limits) on the skymap."""
    if coordinate_system == CoordinateSystem.HORIZONTAL:
        theta = numpy.linspace(0, 2 * numpy.pi, 200)
        az_deg = numpy.rad2deg(theta)

        # We need these later for plotting the min/max azimuth lines
        min_az_rad = numpy.deg2rad(float(observation.conditions.min_object_azimuth))
        max_az_rad = numpy.deg2rad(float(observation.conditions.max_object_azimuth))

        # Get the visibility mask for a range of altitudes at each azimuth
        if observation.conditions.horizon_file or observation.conditions.horizon_content:
            horizon_alt = observation.conditions.horizon.get_altitude(az_deg)
            r_outer_good = 90 - horizon_alt

            ax.fill_between(
                theta,
                0,
                r_outer_good,
                color=good_condition_color,
                alpha=0.1,
            )
            ax.plot(
                theta,
                r_outer_good,
                color=style["GRID_COLOR"],
                linestyle="--",
                linewidth=1,
            )
        else:
            r_inner_good = 0
            r_outer_good = 90 - observation.conditions.min_object_altitude

            if (r_outer_good > 0) or not (
                float(observation.conditions.min_object_azimuth) == 0.0
                and float(observation.conditions.max_object_azimuth) == 360.0
            ):
                if min_az_rad > max_az_rad:  # Crosses North
                    theta1 = numpy.linspace(min_az_rad, 2 * numpy.pi, 50)
                    ax.fill_between(
                        theta1,
                        r_inner_good,
                        r_outer_good,
                        color=good_condition_color,
                        alpha=0.1,
                    )
                    theta2 = numpy.linspace(0, max_az_rad, 50)
                    ax.fill_between(
                        theta2,
                        r_inner_good,
                        r_outer_good,
                        color=good_condition_color,
                        alpha=0.1,
                    )
                else:
                    theta_range = numpy.linspace(min_az_rad, max_az_rad, 100)
                    ax.fill_between(
                        theta_range,
                        r_inner_good,
                        r_outer_good,
                        color=good_condition_color,
                        alpha=0.1,
                    )

            if r_outer_good > 0:
                ax.plot(
                    numpy.linspace(0, 2 * numpy.pi, 100),
                    [90 - observation.conditions.min_object_altitude] * 100,
                    color=style["GRID_COLOR"],
                    linestyle="--",
                    linewidth=1,
                )
                ax.text(
                    numpy.deg2rad(90),
                    90 - observation.conditions.min_object_altitude,
                    f"{observation.conditions.min_object_altitude}°",
                    ha="center",
                    va="bottom",
                    color=style["TEXT_COLOR"],
                    fontsize=10,
                    bbox=dict(
                        facecolor=style["AXES_FACE_COLOR"],
                        edgecolor="none",
                        boxstyle="round,pad=0.2",
                    ),
                )

        if not (
            observation.conditions.horizon_file or observation.conditions.horizon_content
        ) and not (
            float(observation.conditions.min_object_azimuth) == 0.0
            and float(observation.conditions.max_object_azimuth) == 360.0
        ):
            ax.plot(
                [min_az_rad, min_az_rad],
                [0, 90],
                color=style["GRID_COLOR"],
                linestyle=":",
                linewidth=1,
            )
            ax.plot(
                [max_az_rad, max_az_rad],
                [0, 90],
                color=style["GRID_COLOR"],
                linestyle=":",
                linewidth=1,
            )
    else:  # Equatorial
        num_ra = 120
        num_dec = 30
        theta = numpy.linspace(0, 2 * numpy.pi, num_ra)
        r = numpy.linspace(0, 90, num_dec)
        theta_grid, r_grid = numpy.meshgrid(theta, r)

        ra_rad = theta_grid
        if is_sh:
            dec_deg = r_grid - 90
        else:
            dec_deg = 90 - r_grid
        ra_hours = ra_rad * 12 / numpy.pi

        grid_stars = SkyfieldStar(ra_hours=ra_hours.ravel(), dec_degrees=dec_deg.ravel())
        alt_flat, az_flat, _ = observer.observe(grid_stars).apparent().altaz()
        alt = Angle(degrees=alt_flat.degrees.reshape(ra_hours.shape))
        az = Angle(degrees=az_flat.degrees.reshape(ra_hours.shape))

        alt_deg_grid = cast(Any, alt.degrees).reshape(theta_grid.shape)
        az_deg_grid = cast(Any, az.degrees).reshape(theta_grid.shape)

        good_mask = observation.conditions.is_visible(az_deg_grid, alt_deg_grid)

        ax.contourf(
            theta_grid,
            r_grid,
            numpy.array(good_mask).astype(int),
            levels=[0.5, 1.5],
            colors=[good_condition_color],
            alpha=0.1,
        )


def _plot_polar_skymap_objects(
    observation: "Observation",
    ax: axes.Axes,
    observer: Any,
    style: dict,
    target_name: str,
    target_object: Any,
    star_magnitude_limit: Optional[float],
    plot_stars: bool,
    plot_messier: bool,
    plot_ngc: bool,
    plot_planets: bool,
    plot_sun: bool,
    plot_moon: bool,
    flipped_horizontally: bool,
    flipped_vertically: bool,
    coordinate_system: CoordinateSystem,
    effective_dark_mode: bool,
):
    """Plots various celestial objects (stars, Messier, NGC, planets, Sun, Moon) on the skymap."""
    if plot_stars:
        _plot_stars_on_skymap(
            observation,
            ax,
            observer,
            star_magnitude_limit,
            is_polar=True,
            style=style,
            zoom_deg=None,
            target_object=target_object,
            target_name=target_name,
            coordinate_system=coordinate_system,
        )
        _plot_bright_stars_on_skymap(
            observation,
            ax,
            observer,
            is_polar=True,
            style=style,
            zoom_deg=None,
            coordinate_system=coordinate_system,
            target_name=target_name,
        )
    if plot_messier:
        _plot_messier_on_skymap(
            observation,
            ax,
            observer,
            is_polar=True,
            target_name=target_name,
            flipped_horizontally=flipped_horizontally,
            flipped_vertically=flipped_vertically,
            coordinate_system=coordinate_system,
        )
    if plot_ngc:
        _plot_ngc_on_skymap(
            observation,
            ax,
            observer,
            is_polar=True,
            target_name=target_name,
            star_magnitude_limit=star_magnitude_limit,
            zoom_deg=None,
            target_object=target_object,
            flipped_horizontally=flipped_horizontally,
            flipped_vertically=flipped_vertically,
            coordinate_system=coordinate_system,
        )
    if plot_planets:
        _plot_planets_on_skymap(
            observation,
            ax,
            observer,
            is_polar=True,
            effective_dark_mode=effective_dark_mode,
            style=style,
            target_name=target_name,
            coordinate_system=coordinate_system,
        )
    if plot_sun and target_name != "Sun":
        _plot_solar_system_object_on_skymap(
            observation,
            ax,
            observer,
            is_polar=True,
            style=style,
            object_name="Sun",
            coordinate_system=coordinate_system,
        )
    if plot_moon and target_name != "Moon":
        _plot_solar_system_object_on_skymap(
            observation,
            ax,
            observer,
            is_polar=True,
            style=style,
            object_name="Moon",
            coordinate_system=coordinate_system,
        )
    if observation.local_planets.find_by_name(target_name) is not None:
        _plot_solar_system_object_on_skymap(
            observation,
            ax,
            observer,
            is_polar=True,
            style=style,
            object_name=target_name,
            is_target=True,
            coordinate_system=coordinate_system,
        )


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
            width_arcmin = target_object_data.get(ObjectTableLabels.SIZE_MAJOR, 0)
            width_arcmin = getattr(width_arcmin, "magnitude", width_arcmin)
            width_deg = width_arcmin / 60.0

            height_arcmin = target_object_data.get(
                ObjectTableLabels.SIZE_MINOR, width_arcmin
            )
            height_arcmin = getattr(height_arcmin, "magnitude", height_arcmin)
            height_deg = height_arcmin / 60.0

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
            width_arcmin = target_object_data.get(ObjectTableLabels.SIZE_MAJOR, 0)
            width_arcmin = getattr(width_arcmin, "magnitude", width_arcmin)
            width_deg = width_arcmin / 60.0

            height_arcmin = target_object_data.get(
                ObjectTableLabels.SIZE_MINOR, width_arcmin
            )
            height_arcmin = getattr(height_arcmin, "magnitude", height_arcmin)
            height_deg = height_arcmin / 60.0

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
    star_magnitude_limit: Optional[float],
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

    _plot_polar_skymap_objects(
        observation,
        ax,
        observer,
        style,
        target_name,
        target_object,
        star_magnitude_limit,
        plot_stars,
        plot_messier,
        plot_ngc,
        plot_planets,
        plot_sun,
        plot_moon,
        flipped_horizontally,
        flipped_vertically,
        coordinate_system,
        effective_dark_mode,
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
