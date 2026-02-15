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

from ..constants import ObjectTableLabels

if TYPE_CHECKING:
    from ..observations import Observation


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
    fig = ax.get_figure()
    if fig:
        fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
    ax.set_facecolor(style["AXES_FACE_COLOR"])

    polar_ax = cast(Any, ax)
    is_sh = observation.place.lat_decimal < 0
    if coordinate_system == CoordinateSystem.HORIZONTAL:
        polar_ax.set_rlim(0, 90)
        polar_ax.set_theta_zero_location("S" if is_sh else "N")
        polar_ax.set_theta_direction(1)
        polar_ax.set_yticks([0, 30, 60, 90])
        polar_ax.set_yticklabels(["90°", "60°", "30°", "0°"], color=style["TEXT_COLOR"])
        polar_ax.set_rlabel_position(22.5)
        cardinal_directions = {
            "N": 0,
            "E": numpy.pi / 2,
            "S": numpy.pi,
            "W": 3 * numpy.pi / 2,
        }
        for direction, angle in cardinal_directions.items():
            polar_ax.text(
                angle,
                95,
                direction,
                ha="center",
                va="center",
                color=style["TEXT_COLOR"],
                fontsize=12,
            )
    else:  # Equatorial
        polar_ax.set_rlim(0, 90)
        polar_ax.set_theta_zero_location("S" if is_sh else "N")
        polar_ax.set_theta_direction(1)  # RA increases eastward
        polar_ax.set_yticks([0, 30, 60, 90])
        if is_sh:
            polar_ax.set_yticklabels(
                ["-90°", "-60°", "-30°", "0°"], color=style["TEXT_COLOR"]
            )
        else:
            polar_ax.set_yticklabels(
                ["90°", "60°", "30°", "0°"], color=style["TEXT_COLOR"]
            )
        polar_ax.set_rlabel_position(22.5)
        ra_labels = [f"{h}h" for h in range(0, 24, 3)]
        polar_ax.set_xticklabels(ra_labels, color=style["TEXT_COLOR"])

    ax.grid(True, color=style["GRID_COLOR"], linestyle="--", linewidth=0.5)

    good_condition_color = style.get(
        "GOOD_CONDITION_HL_COLOR",
        "#90EE90" if not effective_dark_mode else "#007447",
    )

    if coordinate_system == CoordinateSystem.HORIZONTAL:
        r_inner_good = 0
        r_outer_good = 90 - observation.conditions.min_object_altitude

        min_az_rad = numpy.deg2rad(float(observation.conditions.min_object_azimuth))
        max_az_rad = numpy.deg2rad(float(observation.conditions.max_object_azimuth))

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
                theta = numpy.linspace(min_az_rad, max_az_rad, 100)
                ax.fill_between(
                    theta,
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
        # Create a grid in polar coordinates (RA, Dec)
        num_ra = 120  # ~3 degree resolution
        num_dec = 30  # ~3 degree resolution
        theta = numpy.linspace(0, 2 * numpy.pi, num_ra)  # RA
        r = numpy.linspace(0, 90, num_dec)  # Radius (90-Dec)
        theta_grid, r_grid = numpy.meshgrid(theta, r)

        # Convert polar grid to RA/Dec
        ra_rad = theta_grid
        if is_sh:
            dec_deg = r_grid - 90
        else:
            dec_deg = 90 - r_grid
        ra_hours = ra_rad * 12 / numpy.pi

        # Create Skyfield Star objects for the entire grid
        grid_stars = SkyfieldStar(
            ra_hours=ra_hours.ravel(), dec_degrees=dec_deg.ravel()
        )
        alt_flat, az_flat, _ = observer.observe(grid_stars).apparent().altaz()
        alt = Angle(degrees=alt_flat.degrees.reshape(ra_hours.shape))
        az = Angle(degrees=az_flat.degrees.reshape(ra_hours.shape))

        # Reshape the results back to the grid shape
        alt_deg_grid = cast(Any, alt.degrees).reshape(theta_grid.shape)
        az_deg_grid = cast(Any, az.degrees).reshape(theta_grid.shape)

        # Check conditions
        min_alt = float(observation.conditions.min_object_altitude)
        min_az = float(observation.conditions.min_object_azimuth)
        max_az = float(observation.conditions.max_object_azimuth)

        # Create a mask for "good" conditions
        alt_mask = alt_deg_grid >= min_alt
        if min_az <= max_az:
            az_mask = (az_deg_grid >= min_az) & (az_deg_grid <= max_az)
        else:  # Azimuth range crosses 0/360
            az_mask = (az_deg_grid >= min_az) | (az_deg_grid <= max_az)
        good_mask = alt_mask & az_mask

        # Use contourf to shade the "good" area
        # We plot where the mask is True (1)
        ax.contourf(
            theta_grid,
            r_grid,
            good_mask.astype(int),
            levels=[0.5, 1.5],
            colors=[good_condition_color],
            alpha=0.1,
        )

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
    target_alt, target_az, _ = observer.observe(target_object).apparent().altaz()
    target_ra, target_dec, _ = observer.observe(target_object).apparent().radec()

    if coordinate_system == CoordinateSystem.HORIZONTAL and bool(
        numpy.any(target_alt.degrees > 0)
    ):
        if target_object_data is not None:
            width_arcmin = target_object_data.get(ObjectTableLabels.WIDTH, 0)
            width_arcmin = getattr(width_arcmin, "magnitude", width_arcmin)
            width_deg = width_arcmin / 60.0

            height_arcmin = target_object_data.get("Height", width_arcmin)
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
            width_arcmin = target_object_data.get(ObjectTableLabels.WIDTH, 0)
            width_arcmin = getattr(width_arcmin, "magnitude", width_arcmin)
            width_deg = width_arcmin / 60.0

            height_arcmin = target_object_data.get("Height", width_arcmin)
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

    ax.set_title(
        gettext_("Skymap for {target_name} (Generated: {generation_time_str})").format(
            target_name=gettext_(target_name), generation_time_str=generation_time_str
        ),
        color=style["TEXT_COLOR"],
    )

    return fig
