import logging
from datetime import datetime
from typing import TYPE_CHECKING, Any, Optional, cast

import numpy
import pandas as pd
from matplotlib import pyplot
from matplotlib.patches import Ellipse
from skyfield.api import Star as SkyfieldStar
from skyfield.units import Angle

from apts.config import get_dark_mode
from apts.constants.graphconstants import get_planet_color, get_plot_style
from apts.constants.plot import CoordinateSystem
from apts.i18n import _thread_local, gettext_
from apts.plotting.skymap_objects import (
    _plot_bright_stars_on_skymap,
    _plot_messier_on_skymap,
    _plot_ngc_on_skymap,
    _plot_planets_on_skymap,
    _plot_solar_system_object_on_skymap,
    _plot_stars_on_skymap,
)
from apts.plotting.skymap_polar import _generate_polar_skymap
from apts.plotting.skymap_zoom import _generate_zoom_skymap
from apts.plotting.utils import (
    calculate_ellipse_angle,
    calculate_parallactic_angle,
    get_brightness_color,
)
from apts.utils.planetary import get_reverse_translated_planet_names
from ..constants import ObjectTableLabels

if TYPE_CHECKING:
    from ..observations import Observation

logger = logging.getLogger(__name__)




def _generate_plot_skymap(
    observation: "Observation",
    target_name: str,
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
    **kwargs,
):
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

    generation_time_str = t.astimezone(observation.place.local_timezone).strftime(
        "%Y-%m-%d %H:%M %Z"
    )

    target_object = None
    target_object_data = None

    # Search logic that mirrors find_by_name methods
    # Messier
    result_df = observation.local_messier.objects[
        observation.local_messier.objects["Messier"] == target_name
    ]
    if not result_df.empty:
        target_object_data = result_df.iloc[0]
        target_object = observation.local_messier.get_skyfield_object(
            target_object_data
        )
    else:
        # NGC
        result_df = observation.local_ngc.objects[
            (observation.local_ngc.objects["NGC"] == target_name)
            | (observation.local_ngc.objects["Name"] == target_name)
        ]
        if not result_df.empty:
            target_object_data = result_df.iloc[0]
            target_object = observation.local_ngc.get_skyfield_object(
                target_object_data
            )
        else:
            # Stars
            result_df = observation.local_stars.objects[
                observation.local_stars.objects["Name"] == target_name
            ]
            if not result_df.empty:
                target_object_data = result_df.iloc[0]
                target_object = observation.local_stars.get_skyfield_object(
                    target_object_data
                )
            else:
                # Planets
                target_object = observation.local_planets.find_by_name(target_name)

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
        return fig

    target_alt, target_az, _ = observer.observe(target_object).apparent().altaz()
    target_ra, target_dec, _ = observer.observe(target_object).apparent().radec()

    if zoom_deg is not None:
        fig, ax = pyplot.subplots(figsize=(10, 10))
        return _generate_zoom_skymap(
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
        )
    else:
        fig, ax = pyplot.subplots(figsize=(10, 10), subplot_kw={"projection": "polar"})
        return _generate_polar_skymap(
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
        )

def plot_skymap(
    observation: "Observation",
    target_name: str,
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
    coordinate_system: CoordinateSystem = cast(CoordinateSystem, CoordinateSystem.HORIZONTAL),
    **kwargs,
):
    flipped_horizontally = False
    flipped_vertically = False
    if flip_horizontally is not None:
        flipped_horizontally = flip_horizontally
    if flip_vertically is not None:
        flipped_vertically = flip_vertically
    elif equipment_id is not None and zoom_deg is not None:
        equipment_data = observation.equipment.data()
        if not equipment_data.empty and equipment_id in equipment_data["ID"].values:
            row = equipment_data.loc[equipment_data["ID"] == equipment_id]
            flipped_horizontally = row["Flipped Horizontally"].iloc[0]
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
        **kwargs,
    )
