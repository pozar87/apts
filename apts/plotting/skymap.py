import logging
from datetime import datetime
from typing import TYPE_CHECKING, Optional, cast

import pandas as pd
from matplotlib import figure, pyplot

from apts.config import get_dark_mode
from apts.constants.graphconstants import get_plot_style
from apts.constants.plot import CoordinateSystem
from apts.i18n import _thread_local, gettext_
from apts.plotting.skymaps.resolver import resolve_target
from apts.plotting.skymaps.skymap_polar import _generate_polar_skymap
from apts.plotting.skymaps.skymap_texture import _generate_texture_skymap
from apts.plotting.skymaps.skymap_zoom import _generate_zoom_skymap
from apts.utils.planetary import get_reverse_translated_planet_names

from ..place.utils import get_scalar_datetime

if TYPE_CHECKING:
    from ..observations import Observation

logger = logging.getLogger(__name__)


def _generate_plot_skymap(
    observation: "Observation",
    target_name: Optional[str] = None,
    dark_mode_override: Optional[bool] = None,
    zoom_deg: Optional[float] = None,
    star_magnitude_limit: Optional[float] = None,
    plot_stars: bool = True,
    plot_messier: bool = False,
    plot_ngc: bool = False,
    plot_planets: bool = False,
    plot_sun: bool = False,
    plot_moon: bool = False,
    plot_date: Optional[datetime] = None,
    flipped_horizontally: bool = False,
    flipped_vertically: bool = False,
    coordinate_system: CoordinateSystem = cast(
        CoordinateSystem, CoordinateSystem.HORIZONTAL
    ),
    texture_mode: bool = False,
    plot_labels: Optional[bool] = None,
    **kwargs,
) -> figure.Figure:
    """
    Generates a skymap for a given time and location, highlighting a target object.
    Can generate a full polar skymap or a zoomed-in Cartesian skymap.
    """
    current_language = getattr(_thread_local, "language", "en")
    if current_language != "en":
        reverse_map = get_reverse_translated_planet_names(current_language)
        target_name = reverse_map.get(target_name, target_name)

    if dark_mode_override is not None:
        effective_dark_mode = dark_mode_override
    else:
        effective_dark_mode = get_dark_mode()

    style = get_plot_style(effective_dark_mode)

    if plot_date:
        # Use the specified plot_date
        t = observation.place.ts.utc(plot_date)
    elif observation.start and observation.stop:
        # Default to the middle of the observation window
        start_ts = observation.place.ts.utc(observation.start)
        stop_ts = observation.place.ts.utc(observation.stop)
        middle_julian_date = (start_ts.tt + stop_ts.tt) / 2
        t = observation.place.ts.tt_jd(middle_julian_date)
    elif observation.effective_date is not None:
        # Fallback to effective_date if start/stop are not available
        t = observation.effective_date
    else:
        # Final fallback to the current time
        t = observation.place.ts.now()

    observer = observation.place.observer.at(t)

    # Ensure t is treated as a single datetime for formatting.
    t_dt = get_scalar_datetime(t).astimezone(observation.place.local_timezone)
    generation_time_str = t_dt.strftime("%Y-%m-%d %H:%M %Z")

    if texture_mode:
        figsize = kwargs.get("figsize", (20, 10))
        _, ax = pyplot.subplots(figsize=figsize)
        return cast(
            figure.Figure,
            _generate_texture_skymap(
                observation,
                ax,
                style,
                observer,
                effective_dark_mode,
                star_magnitude_limit,
                plot_stars,
                plot_messier,
                plot_ngc,
                plot_planets,
                plot_sun,
                plot_moon,
                coordinate_system,
                plot_labels=plot_labels if plot_labels is not None else False,
            ),
        )

    if not target_name:
        # If not texture mode, target_name is required.
        fig, ax = pyplot.subplots(figsize=(10, 10))
        ax.text(
            0.5,
            0.5,
            gettext_("Target name is required for polar/zoom skymaps."),
            horizontalalignment="center",
            verticalalignment="center",
            transform=ax.transAxes,
        )
        return cast(figure.Figure, fig)

    target_object, target_object_data = resolve_target(observation, target_name)

    if not target_object:
        fig, ax = pyplot.subplots(figsize=(10, 10))
        fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
        ax.set_facecolor(style["AXES_FACE_COLOR"])
        ax.text(
            0.5,
            0.5,
            gettext_("Object '{target_name}' not found.").format(
                target_name=target_name
            ),
            horizontalalignment="center",
            verticalalignment="center",
            transform=ax.transAxes,
            color=style["TEXT_COLOR"],
        )
        ax.set_title(
            gettext_("Skymap (Generated: {generation_time_str})").format(
                generation_time_str=generation_time_str
            ),
            color=style["TEXT_COLOR"],
        )
        return cast(figure.Figure, fig)

    if zoom_deg is not None:
        _, ax = pyplot.subplots(figsize=(10, 10))
        return cast(
            figure.Figure,
            _generate_zoom_skymap(
                observation,
                ax,
                style,
                target_name,
                target_object,
                target_object_data,
                observer,
                generation_time_str,
                effective_dark_mode,
                zoom_deg,
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
            ),
        )
    else:
        _, ax = pyplot.subplots(figsize=(10, 10), subplot_kw={"projection": "polar"})
        return cast(
            figure.Figure,
            _generate_polar_skymap(
                observation,
                ax,
                style,
                target_name,
                target_object,
                target_object_data,
                observer,
                generation_time_str,
                effective_dark_mode,
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
            ),
        )


def plot_skymap(
    observation: "Observation",
    target_name: Optional[str] = None,
    dark_mode_override: Optional[bool] = None,
    zoom_deg: Optional[float] = None,
    star_magnitude_limit: Optional[float] = None,
    plot_stars: bool = True,
    plot_messier: bool = False,
    plot_ngc: bool = False,
    plot_planets: bool = False,
    plot_sun: bool = False,
    plot_moon: bool = False,
    plot_date: Optional[datetime] = None,
    equipment_id: Optional[int] = None,
    flip_horizontally: Optional[bool] = None,
    flip_vertically: Optional[bool] = None,
    coordinate_system: CoordinateSystem = cast(
        CoordinateSystem, CoordinateSystem.HORIZONTAL
    ),
    texture_mode: bool = False,
    plot_labels: Optional[bool] = None,
    **kwargs,
) -> figure.Figure:
    flipped_horizontally = False
    flipped_vertically = False
    if flip_horizontally is not None:
        flipped_horizontally = flip_horizontally
    if flip_vertically is not None:
        flipped_vertically = flip_vertically
    elif equipment_id is not None and zoom_deg is not None:
        # Check if equipment has data method, otherwise assume it's already a DataFrame
        equipment_data = cast(
            pd.DataFrame,
            observation.equipment.data()
            if hasattr(observation.equipment, "data")
            else observation.equipment,
        )
        if (
            equipment_data is not None
            and not equipment_data.empty
            and "ID" in equipment_data.columns
            and equipment_id in equipment_data["ID"].values
        ):
            row = equipment_data.loc[equipment_data["ID"] == equipment_id]
            if "Flipped Horizontally" in row.columns:
                flipped_horizontally = row["Flipped Horizontally"].iloc[0]
            if "Flipped Vertically" in row.columns:
                flipped_vertically = row["Flipped Vertically"].iloc[0]

    return _generate_plot_skymap(
        observation,
        target_name=target_name,
        dark_mode_override=dark_mode_override,
        zoom_deg=zoom_deg,
        star_magnitude_limit=star_magnitude_limit,
        plot_stars=plot_stars,
        plot_messier=plot_messier,
        plot_ngc=plot_ngc,
        plot_planets=plot_planets,
        plot_sun=plot_sun,
        plot_moon=plot_moon,
        plot_date=plot_date,
        flipped_horizontally=flipped_horizontally,
        flipped_vertically=flipped_vertically,
        coordinate_system=coordinate_system,
        texture_mode=texture_mode,
        plot_labels=plot_labels,
        **kwargs,
    )
