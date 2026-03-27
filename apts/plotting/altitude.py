import logging
from datetime import timedelta
from typing import TYPE_CHECKING, Any, Optional, cast

import pandas as pd
from matplotlib import lines, pyplot

from apts.config import get_dark_mode
from apts.constants.graphconstants import (
    OpticalType,
    get_messier_color,
    get_planet_color,
    get_plot_colors,
    get_plot_style,
)
from apts.i18n import gettext_
from apts.plotting.utils import mark_good_conditions, mark_observation
from apts.utils import planetary
from apts.utils.plot import Utils as PlotUtils
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
            PlotUtils.annotate_plot(
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

        # Vectorized property extraction to avoid slow iterrows()
        # Ensure numeric columns are floats to avoid Pint/Quantity overhead
        for col in [ObjectTableLabels.ALTITUDE, ObjectTableLabels.WIDTH, "Height"]:
            if col in messier_df.columns:
                messier_df[col] = [
                    getattr(x, "magnitude", x) for x in messier_df[col].values
                ]

        # Handle missing Height
        if "Height" not in messier_df.columns:
            messier_df["Height"] = messier_df[ObjectTableLabels.WIDTH]
        else:
            messier_df["Height"] = messier_df["Height"].fillna(
                messier_df[ObjectTableLabels.WIDTH]
            )

        # Vectorized marker size: marker area (s) as width * height
        messier_df["marker_size"] = (
            messier_df[ObjectTableLabels.WIDTH] * messier_df["Height"]
        )

        # Determine colors (Type is often already translated in get_visible_messier)
        types = (
            messier_df["Type"].fillna("Other")
            if "Type" in messier_df.columns
            else pd.Series("Other", index=messier_df.index)
        )
        messier_df["TranslatedType"] = [gettext_(t) for t in types]
        messier_df["color"] = [
            get_messier_color(t, effective_dark_mode)
            for t in messier_df["TranslatedType"]
        ]

        # Filter out objects without a valid transit time in the window
        plot_df = messier_df[messier_df[ObjectTableLabels.TRANSIT].notna()].copy()

        if not plot_df.empty:
            # Single vectorized scatter call for all objects
            ax.scatter(
                plot_df[ObjectTableLabels.TRANSIT],
                plot_df[ObjectTableLabels.ALTITUDE],
                s=plot_df["marker_size"],
                marker="o",
                c=plot_df["color"],
            )

            # Annotation loop optimized to avoid iterrows()
            for text, x, y in zip(
                plot_df[ObjectTableLabels.MESSIER],
                plot_df[ObjectTableLabels.TRANSIT],
                plot_df[ObjectTableLabels.ALTITUDE],
            ):
                ax.annotate(
                    text,
                    (x, y),
                    xytext=(5, 5),
                    textcoords="offset points",
                    color=style["TEXT_COLOR"],
                )

            # Collect unique types for legend
            # Using casting on the method itself to bypass Pyright's overload resolution issues with Pandas
            unique_rows = cast(Any, plot_df).drop_duplicates(subset=["TranslatedType"])
            plotted_types = dict(
                zip(unique_rows["TranslatedType"], unique_rows["color"])
            )
        else:
            plotted_types = {}

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
        PlotUtils.annotate_plot(
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
        ax.legend(handles=legend_handles, title=gettext_("Object Types"))
        PlotUtils.style_legend(ax, style)

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

    # Extended range for plotting context (+/- 30 mins)
    plot_start = (
        observation.start - timedelta(minutes=30) if observation.start else None
    )
    plot_end = observation.stop + timedelta(minutes=30) if observation.stop else None

    if len(planets_df) == 0:
        if plot_start is not None and observation.time_limit is not None:
            # Also extend empty plot
            plot_limit = observation.time_limit + timedelta(minutes=30)
            ax.set_xlim([plot_start, plot_limit])

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
        PlotUtils.annotate_plot(
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

        # Get curve for extended range
        curve_df = observation.place.get_altaz_curve(
            skyfield_object, plot_start, plot_end
        )

        specific_planet_color = get_planet_color(
            planetary.get_simple_name(str(planet["TechnicalName"])),
            effective_dark_mode,
            default_planet_color,  # type: ignore
        )

        # Use pre-computed UTC_datetime if available, fallback for mocks/overrides
        if "UTC_datetime" in curve_df.columns:
            time_series = curve_df["UTC_datetime"]
        else:
            time_series = curve_df["Time"].apply(
                lambda t: t.utc_datetime() if hasattr(t, "utc_datetime") else pd.NaT
            )
        valid_times = pd.notna(time_series)

        # Add Matplotlib-compatible time column for pandas plotting
        curve_df["Time_dt"] = time_series

        # Plot full range as dotted using pandas for x_compat
        curve_df[valid_times].plot(
            x="Time_dt",
            y="Altitude",
            ax=ax,
            x_compat=True,
            color=specific_planet_color,
            linestyle=":",
            alpha=0.6,
            label="_nolegend_",
            legend=False,
        )

        # Plot observation window as solid (only when above min altitude)
        if observation.start and observation.stop:
            visible_mask = observation.conditions.is_visible(
                curve_df["Azimuth"], curve_df["Altitude"]
            )
            in_window_mask = (
                (time_series >= observation.start)
                & (time_series <= observation.stop)
                & visible_mask
            )
            curve_df[valid_times & in_window_mask].plot(
                x="Time_dt",
                y="Altitude",
                ax=ax,
                x_compat=True,
                color=specific_planet_color,
                linestyle="-",
                label=name,
            )
        else:
            # Fallback if no start/stop defined (unlikely for valid observation)
            # Still apply altitude check if possible
            visible_mask = observation.conditions.is_visible(
                curve_df["Azimuth"], curve_df["Altitude"]
            )
            curve_df[valid_times & visible_mask].plot(
                x="Time_dt",
                y="Altitude",
                ax=ax,
                x_compat=True,
                color=specific_planet_color,
                linestyle="-",
                label=name,
            )

        rising_time = planet[ObjectTableLabels.RISING]
        if pd.notna(rising_time):  # type: ignore
            ax.scatter(rising_time, 0, marker="^", color=specific_planet_color, s=100)
        setting_time = planet[ObjectTableLabels.SETTING]
        if pd.notna(setting_time):  # type: ignore
            ax.scatter(setting_time, 0, marker="v", color=specific_planet_color, s=100)

        if not curve_df.empty:
            try:
                # Find peak within the curve (now extended range)
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

    if plot_start is not None and plot_end is not None:
        ax.set_xlim([plot_start, plot_end])

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
    PlotUtils.annotate_plot(
        ax,
        gettext_("Altitude [°]"),
        effective_dark_mode,
        observation.place.local_timezone,
    )
    ax.set_title(gettext_("Solar Objects Altitude"), color=style["TEXT_COLOR"])
    ax.legend()
    PlotUtils.style_legend(ax, style)

    return fig
