from typing import TYPE_CHECKING, Any, Optional

import numpy
import pandas as pd
from matplotlib import axes, figure, pyplot
from matplotlib.patches import Ellipse

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
from apts.plotting.utils import (
    calculate_ellipse_angle,
    calculate_parallactic_angle,
    get_brightness_color,
)

from ...constants import ObjectTableLabels
from .utils import setup_zoom_ax

if TYPE_CHECKING:
    from ...observations import Observation


def _generate_zoom_skymap(
    observation: "Observation",
    ax: axes.Axes,
    style: dict,
    target_name: str,
    target_object: Any,
    target_object_data: Any,
    observer: Any,
    generation_time_str: str,
    effective_dark_mode: bool,
    zoom_deg: float,
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
    target_alt, target_az, _ = observer.observe(target_object).apparent().altaz()
    target_ra, target_dec, _ = observer.observe(target_object).apparent().radec()
    if (
        coordinate_system == CoordinateSystem.HORIZONTAL
        and not observation.conditions.is_visible(target_az.degrees, target_alt.degrees)
    ):
        return _handle_below_horizon(target_name, generation_time_str, style)

    fig = ax.get_figure()
    if fig:
        fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
    ax.set_facecolor(style["AXES_FACE_COLOR"])

    setup_zoom_ax(
        observation,
        ax,
        style,
        coordinate_system,
        zoom_deg,
        target_alt,
        target_az,
        target_ra,
        target_dec,
    )

    if coordinate_system == CoordinateSystem.HORIZONTAL:
        _plot_horizon(ax, observation, target_alt, target_az, zoom_deg, style)

    _plot_catalogs(
        observation,
        ax,
        observer,
        style,
        target_name,
        target_object,
        coordinate_system,
        zoom_deg,
        star_magnitude_limit,
        effective_dark_mode,
        flipped_horizontally,
        flipped_vertically,
        plot_stars,
        plot_messier,
        plot_ngc,
        plot_planets,
        plot_sun,
        plot_moon,
    )

    _draw_target(
        observation,
        ax,
        observer,
        style,
        target_name,
        target_object,
        target_object_data,
        target_alt,
        target_az,
        target_ra,
        target_dec,
        coordinate_system,
        flipped_horizontally,
        flipped_vertically,
    )

    _finalize_plot(
        ax,
        style,
        target_name,
        target_alt,
        target_az,
        target_ra,
        target_dec,
        zoom_deg,
        generation_time_str,
        coordinate_system,
        flipped_horizontally,
        flipped_vertically,
    )

    return fig


def _handle_below_horizon(
    target_name: str, generation_time_str: str, style: dict
) -> figure.Figure:
    fig, ax = pyplot.subplots(figsize=(10, 10))
    fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
    ax.set_facecolor(style["AXES_FACE_COLOR"])
    ax.text(
        0.5,
        0.5,
        gettext_("Target '{target_name}' is below the horizon.").format(
            target_name=gettext_(target_name)
        ),
        horizontalalignment="center",
        verticalalignment="center",
        transform=ax.transAxes,
        color=style["TEXT_COLOR"],
    )
    ax.set_title(
        gettext_("Skymap for {target_name} (Generated: {generation_time_str})").format(
            target_name=gettext_(target_name),
            generation_time_str=generation_time_str,
        ),
        color=style["TEXT_COLOR"],
    )
    return fig


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


def _plot_catalogs(
    observation: "Observation",
    ax: axes.Axes,
    observer: Any,
    style: dict,
    target_name: str,
    target_object: Any,
    coordinate_system: CoordinateSystem,
    zoom_deg: float,
    star_magnitude_limit: Optional[float],
    effective_dark_mode: bool,
    flipped_horizontally: bool,
    flipped_vertically: bool,
    plot_stars: bool,
    plot_messier: bool,
    plot_ngc: bool,
    plot_planets: bool,
    plot_sun: bool,
    plot_moon: bool,
):
    if plot_stars:
        _plot_stars_on_skymap(
            observation,
            ax,
            observer,
            star_magnitude_limit,
            is_polar=False,
            style=style,
            zoom_deg=zoom_deg,
            target_object=target_object,
            target_name=target_name,
            coordinate_system=coordinate_system,
        )
        _plot_bright_stars_on_skymap(
            observation,
            ax,
            observer,
            is_polar=False,
            style=style,
            zoom_deg=zoom_deg,
            coordinate_system=coordinate_system,
            target_name=target_name,
        )
    if plot_messier:
        _plot_messier_on_skymap(
            observation,
            ax,
            observer,
            is_polar=False,
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
            is_polar=False,
            target_name=target_name,
            star_magnitude_limit=star_magnitude_limit,
            zoom_deg=zoom_deg,
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
            is_polar=False,
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
            is_polar=False,
            style=style,
            object_name="Sun",
            coordinate_system=coordinate_system,
        )
    if plot_moon and target_name != "Moon":
        _plot_solar_system_object_on_skymap(
            observation,
            ax,
            observer,
            is_polar=False,
            style=style,
            object_name="Moon",
            coordinate_system=coordinate_system,
        )


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
        width_arcmin = target_object_data.get(ObjectTableLabels.SIZE_MAJOR, 0)
        width_arcmin = getattr(width_arcmin, "magnitude", width_arcmin)
        width_deg = width_arcmin / 60.0

        height_arcmin = target_object_data.get(
            ObjectTableLabels.SIZE_MINOR, width_arcmin
        )
        height_arcmin = getattr(height_arcmin, "magnitude", height_arcmin)
        height_deg = height_arcmin / 60.0

        pos_angle = target_object_data.get("PosAng", 0.0)
        if pd.isna(pos_angle):
            pos_angle = 0.0
        pos_angle = getattr(pos_angle, "magnitude", pos_angle)
        pos_angle = float(pos_angle)

        dec = None
        if hasattr(target_object, "dec"):
            dec = getattr(target_object, "dec", None)
        else:
            try:
                _, dec, _ = observer.observe(target_object).apparent().radec()
            except Exception:
                dec = None

        if dec is not None:
            parallactic_angle = calculate_parallactic_angle(
                observation.place.lat, dec, target_az
            )
            angle = calculate_ellipse_angle(
                pos_angle,
                parallactic_angle,
                coordinate_system,
                flipped_horizontally,
                flipped_vertically,
            )
        else:
            angle = pos_angle

        magnitude = target_object_data.get("Magnitude")
        if pd.isna(magnitude) or magnitude is None:
            magnitude = target_object_data.get("Mag")
        if pd.isna(magnitude) or magnitude is None:
            magnitude = target_object_data.get("magnitude")
        face_color = get_brightness_color(magnitude)

        x_coord, y_coord = (
            (target_az.degrees, target_alt.degrees)
            if coordinate_system == CoordinateSystem.HORIZONTAL
            else (target_ra.hours, target_dec.degrees)
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
        x_coord, y_coord = (
            (target_az.degrees, target_alt.degrees)
            if coordinate_system == CoordinateSystem.HORIZONTAL
            else (target_ra.hours, target_dec.degrees)
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


def _finalize_plot(
    ax: axes.Axes,
    style: dict,
    target_name: str,
    target_alt: Any,
    target_az: Any,
    target_ra: Any,
    target_dec: Any,
    zoom_deg: float,
    generation_time_str: str,
    coordinate_system: CoordinateSystem,
    flipped_horizontally: bool,
    flipped_vertically: bool,
):
    annotate_coords = (
        (target_az.degrees, target_alt.degrees)
        if coordinate_system == CoordinateSystem.HORIZONTAL
        else (target_ra.hours, target_dec.degrees)
    )
    ax.annotate(
        gettext_(target_name),
        annotate_coords,
        textcoords="offset points",
        xytext=(0, 15),
        color="yellow",
        ha="center",
        fontsize=12,
    )

    ax.set_title(
        gettext_(
            "Skymap for {target_name} ({zoom_deg}° view, Generated: {generation_time_str})"
        ).format(
            target_name=gettext_(target_name),
            zoom_deg=zoom_deg,
            generation_time_str=generation_time_str,
        ),
        color=style["TEXT_COLOR"],
    )
    if flipped_horizontally:
        ax.invert_xaxis()
    if flipped_vertically:
        ax.invert_yaxis()
    if flipped_horizontally or flipped_vertically:
        flip_str = gettext_("Flipped") + " "
        if flipped_horizontally:
            flip_str += "H"
        if flipped_vertically:
            flip_str += "V"
        ax.text(
            0.05,
            0.95,
            flip_str,
            transform=ax.transAxes,
            fontsize=12,
            verticalalignment="top",
            color=style["TEXT_COLOR"],
        )
