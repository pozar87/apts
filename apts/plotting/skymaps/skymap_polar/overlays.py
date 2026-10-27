from typing import Any, cast

import numpy
from matplotlib import axes
from skyfield.api import Star as SkyfieldStar
from skyfield.units import Angle

from apts.constants.plot import CoordinateSystem


def _plot_polar_horizontal_overlay(
    observation: Any,
    ax: axes.Axes,
    style: dict,
    good_condition_color: str,
):
    """Plots the horizontal coordinates visibility overlay (horizon or altitude/azimuth limits)."""
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
                bbox={
                    "facecolor": style["AXES_FACE_COLOR"],
                    "edgecolor": "none",
                    "boxstyle": "round,pad=0.2",
                },
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


def _plot_polar_equatorial_overlay(
    observation: Any,
    ax: axes.Axes,
    good_condition_color: str,
    observer: Any,
    is_sh: bool,
):
    """Plots the equatorial coordinates visibility overlay on the polar skymap."""
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


def _plot_polar_visibility_overlay(
    observation: Any,
    ax: axes.Axes,
    style: dict,
    coordinate_system: CoordinateSystem,
    observer: Any,
    is_sh: bool,
    good_condition_color: str,
):
    """Plots the visibility overlay (horizon or altitude/azimuth limits) on the skymap."""
    if coordinate_system == CoordinateSystem.HORIZONTAL:
        _plot_polar_horizontal_overlay(observation, ax, style, good_condition_color)
    else:  # Equatorial
        _plot_polar_equatorial_overlay(
            observation, ax, good_condition_color, observer, is_sh
        )
