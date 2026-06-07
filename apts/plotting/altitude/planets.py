import logging
from datetime import timedelta
from typing import TYPE_CHECKING, Optional

import pandas as pd
from matplotlib import pyplot

from apts.config import get_dark_mode
from apts.constants.graphconstants import (
    OpticalType,
    get_planet_color,
    get_plot_colors,
    get_plot_style,
)
from apts.i18n import gettext_
from apts.plotting.utils import mark_good_conditions, mark_observation
from apts.utils import planetary
from apts.utils.plot import PlotUtils
from ...constants import ObjectTableLabels

if TYPE_CHECKING:
    from apts.observations import Observation

logger = logging.getLogger(__name__)


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
        return _generate_empty_planets_plot(
            observation, ax, effective_dark_mode, style, plot_start
        )

    default_planet_color = plot_colors.get(OpticalType.GENERIC, "#888888")

    # Optimization: Pre-calculate observer_at_times once for all planets
    observer_at_times = None
    if plot_start is not None and plot_end is not None:
        t0 = observation.place.ts.utc(plot_start)
        t1 = observation.place.ts.utc(plot_end)
        times = observation.place.ts.linspace(t0, t1, 100)
        observer_at_times = observation.place.observer.at(times)

    # Optimization: use itertuples() for faster row access
    for planet in planets_df.itertuples():
        _plot_single_planet_curve(
            observation,
            ax,
            planet,
            plot_start,
            plot_end,
            effective_dark_mode,
            default_planet_color,
            style,
            observer_at_times=observer_at_times,
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


def _generate_empty_planets_plot(
    observation, ax, effective_dark_mode, style, plot_start
):
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
    return ax.figure


def _plot_single_planet_curve(
    observation,
    ax,
    planet,
    plot_start,
    plot_end,
    effective_dark_mode,
    default_planet_color,
    style,
    observer_at_times=None,
):
    # planet is a NamedTuple from itertuples()
    name = getattr(planet, ObjectTableLabels.NAME)
    # Convert NamedTuple to dict for get_skyfield_object which expects Series/dict
    planet_dict = planet._asdict()
    skyfield_object = observation.local_planets.get_skyfield_object(planet_dict)

    # Get curve for extended range, using pre-calculated observer position and fast mode
    curve_df = observation.place.get_altaz_curve(
        skyfield_object,
        plot_start,
        plot_end,
        observer_at_times=observer_at_times,
        fast=True,
    )

    specific_planet_color = get_planet_color(
        planetary.get_simple_name(str(getattr(planet, "TechnicalName"))),
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
    _plot_observation_window_curve(
        observation, ax, curve_df, time_series, valid_times, specific_planet_color, name
    )

    rising_time = getattr(planet, ObjectTableLabels.RISING)
    if pd.notna(rising_time):  # type: ignore
        ax.scatter(rising_time, 0, marker="^", color=specific_planet_color, s=100)
    setting_time = getattr(planet, ObjectTableLabels.SETTING)
    if pd.notna(setting_time):  # type: ignore
        ax.scatter(setting_time, 0, marker="v", color=specific_planet_color, s=100)

    _annotate_planet_peak(ax, curve_df, name, style)


def _plot_observation_window_curve(
    observation, ax, curve_df, time_series, valid_times, specific_planet_color, name
):
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


def _annotate_planet_peak(ax, curve_df, name, style):
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
            logger.debug(f"Could not find peak for {name} as all altitudes are NaN.")
