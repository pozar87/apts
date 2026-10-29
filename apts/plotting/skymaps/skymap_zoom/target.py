from typing import TYPE_CHECKING, Any

import numpy
from matplotlib import axes
from matplotlib.patches import Ellipse

import apts.plotting.skymaps.skymap_zoom as skymap_zoom
from apts.constants.plot import CoordinateSystem
from apts.plotting.skymap_objects import (
    _plot_solar_system_object_on_skymap,
)

from ..utils import (
    calculate_target_ellipse_angle,
    get_target_plot_coordinates,
    parse_target_geometry,
)

if TYPE_CHECKING:
    from ....observations import Observation


def _plot_horizon(
    ax: axes.Axes,
    observation: "Observation",
    target_alt: Any,
    target_az: Any,
    zoom_deg: float,
    style: dict,
):
    # Plot horizon line if available
    if observation.conditions.horizon_file or observation.conditions.horizon_content:
        half_zoom = zoom_deg / 2
        az_view = numpy.linspace(
            target_az.degrees - half_zoom, target_az.degrees + half_zoom, 100
        )
        horizon_alt = observation.conditions.horizon.get_altitude(az_view)
        ax.plot(
            az_view,
            horizon_alt,
            color=style["GRID_COLOR"],
            linestyle="--",
            linewidth=1,
        )
        # Shade the area below horizon
        ax.fill_between(
            az_view,
            target_alt.degrees - half_zoom,
            horizon_alt,
            color="black",
            alpha=0.3,
        )


def _draw_catalog_target_ellipse(
    ax: axes.Axes,
    x_coord: float,
    y_coord: float,
    width_deg: float,
    height_deg: float,
    target_dec: Any,
    angle: float,
    magnitude: float | None,
    coordinate_system: CoordinateSystem,
):
    """Draws a detailed ellipse patch representing a catalog deep-sky target."""
    face_color = (
        "none" if magnitude is None else skymap_zoom.get_brightness_color(magnitude)
    )

    ellipse_width = (
        width_deg
        if coordinate_system == CoordinateSystem.HORIZONTAL
        else width_deg / (15 * numpy.cos(numpy.deg2rad(target_dec.degrees)))
    )

    ellipse = Ellipse(
        xy=(x_coord, y_coord),
        width=ellipse_width,
        height=height_deg,
        angle=angle,
        edgecolor="yellow",
        facecolor=face_color,
        linewidth=2,
        linestyle="--",
        alpha=0.6,
    )
    ax.add_patch(ellipse)


def _draw_target(
    observation: "Observation",
    ax: axes.Axes,
    observer: Any,
    style: dict,
    target_name: str,
    target_object: Any,
    target_object_data: Any,
    target_alt: Any,
    target_az: Any,
    target_ra: Any,
    target_dec: Any,
    coordinate_system: CoordinateSystem,
    flipped_horizontally: bool,
    flipped_vertically: bool,
):
    if target_object_data is not None:
        width_deg, height_deg, pos_angle, dec, magnitude = parse_target_geometry(
            target_object, target_object_data, observer
        )

        angle = calculate_target_ellipse_angle(
            pos_angle,
            dec,
            target_az,
            observation.place.lat,
            coordinate_system,
            flipped_horizontally,
            flipped_vertically,
            calculate_parallactic_angle_func=skymap_zoom.calculate_parallactic_angle,
            calculate_ellipse_angle_func=skymap_zoom.calculate_ellipse_angle,
        )

        x_coord, y_coord = get_target_plot_coordinates(
            target_alt, target_az, target_ra, target_dec, coordinate_system
        )

        _draw_catalog_target_ellipse(
            ax,
            x_coord,
            y_coord,
            width_deg,
            height_deg,
            target_dec,
            angle,
            magnitude,
            coordinate_system,
        )
    elif observation.local_planets.find_by_name(target_name) is not None:
        _plot_solar_system_object_on_skymap(
            observation,
            ax,
            observer,
            is_polar=False,
            style=style,
            object_name=target_name,
            is_target=True,
            coordinate_system=coordinate_system,
        )
    else:
        x_coord, y_coord = get_target_plot_coordinates(
            target_alt, target_az, target_ra, target_dec, coordinate_system
        )
        ax.scatter(
            x_coord,
            y_coord,
            s=200,
            facecolors="none",
            edgecolors="yellow",
            marker="o",
            linewidths=2,
        )
