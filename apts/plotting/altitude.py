import logging
from datetime import timedelta
from typing import TYPE_CHECKING, Optional

import matplotlib.dates as mdates
import pandas as pd
from matplotlib import lines, pyplot

from apts.config import get_dark_mode
from apts.constants.graphconstants import (
    OpticalType,
    get_planet_color,
    get_plot_colors,
    get_plot_style,
)
from apts.i18n import gettext_
from apts.plotting.utils import mark_good_conditions, mark_observation
from apts.utils.plot import Utils
from ..constants import ObjectTableLabels

if TYPE_CHECKING:
    from apts.observations import Observation

logger = logging.getLogger(__name__)


def generate_plot_messier(
    observation: "Observation", dark_mode_override: Optional[bool] = None, **args
):
    if dark_mode_override is not None:
        effective_dark_mode = dark_mode_override
    else:
        effective_dark_mode = get_dark_mode()

    style = get_plot_style(effective_dark_mode)

    ax = args.pop("ax", None)
    fig = None
    if ax:
        fig = ax.figure
    else:
        fig, ax = pyplot.subplots(figsize=(18, 12), **args)

    fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
    ax.set_facecolor(style["AXES_FACE_COLOR"])

    try:
        messier_df = observation.get_visible_messier().copy()

        if len(messier_df) == 0:
            if observation.start is not None and observation.time_limit is not None:
                ax.set_xlim(
                    [
                        observation.start - timedelta(minutes=15),
                        observation.time_limit + timedelta(minutes=15),
                    ]
                )
            ax.set_ylim(0, 90)
            mark_observation(observation, ax, effective_dark_mode, style)
            mark_good_conditions(
                observation,
                ax,
                observation.conditions.min_object_altitude,
                90,
                effective_dark_mode,
                style,
            )
            Utils.annotate_plot(
                ax,
                gettext_("Altitude [°]"),
                effective_dark_mode,
                observation.place.local_timezone,
            )
            ax.set_title(
                gettext_("Messier Objects Altitude"), color=style["TEXT_COLOR"]
            )
            logger.info(
                gettext_("Generated empty Messier plot as no objects are visible.")
            )
            return fig

        LIGHT_MESSIER_TYPE_COLORS = {
            gettext_("Galaxy"): "#8CA2AD",
            gettext_("Globular Cluster"): "#A38F9B",
            gettext_("Open Cluster"): "#8EA397",
            gettext_("Nebula"): "#9B8FA3",
            gettext_("Planetary Nebula"): "#A39B8F",
            gettext_("Supernova Remnant"): "#AD9F9A",
            gettext_("Other"): "#A0A0A0",
        }
        DARK_MESSIER_TYPE_COLORS = {
            gettext_("Galaxy"): "#5A1A75",
            gettext_("Globular Cluster"): "#CCCCCC",
            gettext_("Open Cluster"): "#FFFFFF",
            gettext_("Nebula"): "#5A1A75",
            gettext_("Planetary Nebula"): "#007447",
            gettext_("Supernova Remnant"): "#BBBBBB",
            gettext_("Other"): "#999999",
        }

        if effective_dark_mode:
            current_messier_colors = DARK_MESSIER_TYPE_COLORS
        else:
            current_messier_colors = LIGHT_MESSIER_TYPE_COLORS

        plotted_types = {}

        for col in [ObjectTableLabels.ALTITUDE, ObjectTableLabels.WIDTH, "Height"]:
            if col in messier_df.columns and hasattr(
                messier_df[col].iloc[0], "magnitude"
            ):
                messier_df[col] = messier_df[col].apply(
                    lambda x: x.magnitude if hasattr(x, "magnitude") else x
                )

        for _, obj in messier_df.iterrows():
            transit = obj[ObjectTableLabels.TRANSIT]
            if bool(pd.notna(transit)):
                altitude = obj[ObjectTableLabels.ALTITUDE]
                obj_type = gettext_(obj["Type"])
                width = obj[ObjectTableLabels.WIDTH]
                height = obj["Height"] if "Height" in obj else width
                messier_id = obj[ObjectTableLabels.MESSIER]
                marker_size = (width * height) ** 0.5
                color = current_messier_colors.get(
                    obj_type, current_messier_colors[gettext_("Other")]
                )
                plotted_types[obj_type] = color
                ax.scatter(transit, altitude, s=marker_size**2, marker="o", c=color)
                ax.annotate(
                    messier_id,
                    (transit, altitude),
                    xytext=(5, 5),
                    textcoords="offset points",
                    color=style["TEXT_COLOR"],
                )

        if observation.start is not None and observation.time_limit is not None:
            ax.set_xlim(
                [
                    observation.start - timedelta(minutes=15),
                    observation.time_limit + timedelta(minutes=15),
                ]
            )
        ax.set_ylim(0, 90)
        date_format = mdates.DateFormatter(
            "%H:%M:%S %Z", tz=observation.place.local_timezone
        )
        ax.xaxis.set_major_formatter(date_format)
        mark_observation(observation, ax, effective_dark_mode, style)
        mark_good_conditions(
            observation,
            ax,
            observation.conditions.min_object_altitude,
            90,
            effective_dark_mode,
            style,
        )
        Utils.annotate_plot(
            ax,
            gettext_("Altitude [°]"),
            effective_dark_mode,
            observation.place.local_timezone,
        )

        legend_handles = [
            lines.Line2D(
                [0],
                [0],
                marker="o",
                color="w",
                label=obj_type,
                markerfacecolor=color,
                markersize=10,
            )
            for obj_type, color in plotted_types.items()
        ]
        legend = ax.legend(handles=legend_handles, title=gettext_("Object Types"))
        legend.get_frame().set_facecolor(style["AXES_FACE_COLOR"])
        legend.get_frame().set_edgecolor(style["AXIS_COLOR"])
        legend.get_title().set_color(style["TEXT_COLOR"])
        for text in legend.get_texts():
            text.set_color(style["TEXT_COLOR"])

        ax.set_title(gettext_("Messier Objects Altitude"), color=style["TEXT_COLOR"])
        logger.info(gettext_("Successfully generated Messier plot."))
        return fig

    except Exception as e:
        logger.error(f"Error generating Messier plot: {e}", exc_info=True)
        ax.clear()
        fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
        ax.set_facecolor(style["AXES_FACE_COLOR"])

        error_text_color = "#FF6B6B" if effective_dark_mode else "red"
        ax.text(
            0.5,
            0.5,
            gettext_("Error generating Messier plot.\nSee logs for details."),
            horizontalalignment="center",
            verticalalignment="center",
            fontsize=12,
            color=error_text_color,
            wrap=True,
            transform=ax.transAxes,
        )
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title(gettext_("Messier Plot Error"), color=style["TEXT_COLOR"])
        return fig


def generate_plot_planets(
    observation: "Observation", dark_mode_override: Optional[bool] = None, **args
):
    if dark_mode_override is not None:
        effective_dark_mode = dark_mode_override
    else:
        effective_dark_mode = get_dark_mode()

    style = get_plot_style(effective_dark_mode)
    plot_colors = get_plot_colors(effective_dark_mode)

    ax = args.pop("ax", None)
    fig = None
    if ax:
        fig = ax.figure
    else:
        fig, ax = pyplot.subplots(figsize=(18, 12), **args)

    fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
    ax.set_facecolor(style["AXES_FACE_COLOR"])

    planets_df = observation.get_visible_planets().copy()
    if len(planets_df) == 0:
        if observation.start is not None and observation.time_limit is not None:
            ax.set_xlim(
                [
                    observation.start - timedelta(minutes=15),
                    observation.time_limit + timedelta(minutes=15),
                ]
            )
        ax.set_ylim(0, 90)
        mark_observation(observation, ax, effective_dark_mode, style)
        mark_good_conditions(
            observation,
            ax,
            observation.conditions.min_object_altitude,
            90,
            effective_dark_mode,
            style,
        )
        Utils.annotate_plot(
            ax,
            gettext_("Altitude [°]"),
            effective_dark_mode,
            observation.place.local_timezone,
        )
        ax.set_title(gettext_("Solar Objects Altitude"), color=style["TEXT_COLOR"])
        return fig

    default_planet_color = plot_colors.get(OpticalType.GENERIC, "#888888")

    for _, planet in planets_df.iterrows():
        name = planet[ObjectTableLabels.NAME]
        skyfield_object = observation.local_planets.get_skyfield_object(planet)

        curve_df = observation.place.get_altaz_curve(
            skyfield_object, observation.start, observation.stop
        )

        specific_planet_color = get_planet_color(
            name, effective_dark_mode, default_planet_color  # type: ignore
        )

        time_series = curve_df["Time"].apply(
            lambda t: t.utc_datetime() if hasattr(t, "utc_datetime") else pd.NaT
        )
        valid_times = pd.notna(time_series)
        ax.plot(
            time_series[valid_times],
            curve_df["Altitude"][valid_times],
            color=specific_planet_color,
            label=name,
        )

        rising_time = planet[ObjectTableLabels.RISING]
        if pd.notna(rising_time):  # type: ignore
            ax.scatter(
                rising_time, 0, marker="^", color=specific_planet_color, s=100
            )
        setting_time = planet[ObjectTableLabels.SETTING]
        if pd.notna(setting_time):  # type: ignore
            ax.scatter(
                setting_time, 0, marker="v", color=specific_planet_color, s=100
            )

        if not curve_df.empty:
            try:
                peak_idx = curve_df["Altitude"].idxmax()
                peak_time_obj = curve_df["Time"].iloc[peak_idx]
                if hasattr(peak_time_obj, "utc_datetime"):
                    peak_time = peak_time_obj.utc_datetime()
                    peak_alt = curve_df["Altitude"].iloc[peak_idx]
                    if pd.notna(peak_time) and pd.notna(peak_alt):
                        ax.annotate(
                            name,
                            (peak_time, peak_alt),
                            xytext=(5, 5),
                            textcoords="offset points",
                            color=style["TEXT_COLOR"],
                        )
            except ValueError:
                # This can happen if 'Altitude' column is all NaN
                logger.debug(
                    f"Could not find peak for {name} as all altitudes are NaN."
                )

    if observation.start is not None and observation.stop is not None:
        ax.set_xlim([observation.start, observation.stop])
    ax.set_ylim(0, 90)
    date_format = mdates.DateFormatter("%H:%M", tz=observation.place.local_timezone)
    ax.xaxis.set_major_formatter(date_format)

    mark_observation(observation, ax, effective_dark_mode, style)
    mark_good_conditions(
        observation,
        ax,
        observation.conditions.min_object_altitude,
        90,
        effective_dark_mode,
        style,
    )
    Utils.annotate_plot(
        ax,
        gettext_("Altitude [°]"),
        effective_dark_mode,
        observation.place.local_timezone,
    )
    ax.set_title(gettext_("Solar Objects Altitude"), color=style["TEXT_COLOR"])
    ax.legend()

    return fig
