from typing import TYPE_CHECKING, Any, Optional

from matplotlib import axes, figure, pyplot

from apts.constants.plot import CoordinateSystem
from apts.i18n import gettext_

from ..utils import plot_skymap_catalogs, setup_zoom_ax
from .target import _draw_target, _plot_horizon

if TYPE_CHECKING:
    from apts.observations import Observation


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

    plot_skymap_catalogs(
        observation,
        ax,
        observer,
        style,
        target_name,
        target_object,
        is_polar=False,
        coordinate_system=coordinate_system,
        zoom_deg=zoom_deg,
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
