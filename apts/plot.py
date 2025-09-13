import logging
from datetime import timedelta
from typing import Optional, List, TYPE_CHECKING

import matplotlib.dates as mdates
import numpy
import pandas as pd
import svgwrite as svg
from matplotlib import pyplot, lines
from skyfield.api import Star, load

from .utils import Utils
from .constants import ObjectTableLabels
from apts.config import get_dark_mode
from apts.constants.graphconstants import (
    get_plot_style,
    get_plot_colors,
    OpticalType,
    get_planet_color,
)
from .cache import get_hipparcos_data

if TYPE_CHECKING:
    from .observations import Observation

logger = logging.getLogger(__name__)


def _normalize_dates(start, stop):
    # If the stop time is earlier than the start time, it means the observation
    # spans across midnight, so we add one day to the stop time.
    if stop < start:
        stop += timedelta(days=1)
    return (start, stop)


def plot_visible_planets_svg(
    observation: "Observation", dark_mode_override: Optional[bool] = None, **args
):
    if dark_mode_override is not None:
        effective_dark_mode = dark_mode_override
    else:
        effective_dark_mode = get_dark_mode()

    style = get_plot_style(effective_dark_mode)
    # colors = get_plot_colors(effective_dark_mode) # Not strictly needed as style dict has most
    default_fill_color = style["AXES_FACE_COLOR"]

    visible_planets = observation.get_visible_planets(**args)
    dwg = svg.Drawing(style={"background-color": style["BACKGROUND_COLOR"]})
    # Set y offset to biggest planet - extract magnitude from pint.Quantity
    if not visible_planets.empty:
        max_size = visible_planets[["Size"]].max().iloc[0]
        max_size_val = (
            max_size.magnitude if hasattr(max_size, "magnitude") else max_size
        )
    else:
        max_size_val = 0
    y = int(max_size_val + 12)
    # Set x offset to constant value
    x = 20
    # Set delta to constant value
    minimal_delta = 52
    last_radius = None
    for planet in visible_planets[
        ["Name", "Size", "Phase", "TechnicalName"]
    ].values:
        name = planet[0]
        # Handle radius as pint.Quantity
        radius_with_units = planet[1]
        radius = (
            radius_with_units.magnitude
            if hasattr(radius_with_units, "magnitude")
            else radius_with_units
        )
        # Handle phase as pint.Quantity
        phase_with_units = planet[2]
        phase = (
            phase_with_units.magnitude
            if hasattr(phase_with_units, "magnitude")
            else phase_with_units
        )
        phase_str = str(round(phase, 2))

        if last_radius is None:
            y += radius
            x += radius
        else:
            x += max(radius + last_radius + 10, minimal_delta)
        last_radius = radius
        dwg.add(
            dwg.circle(
                center=(x, y),
                r=radius,
                stroke=style["AXIS_COLOR"],
                stroke_width="1",
                fill=get_planet_color(
                    name, effective_dark_mode, default_fill_color
                ),
            )
        )
        dwg.add(
            dwg.text(
                name, 
                insert=(x, y + radius + 15),
                text_anchor="middle",
                fill=style["TEXT_COLOR"],
            )
        )
        dwg.add(
            dwg.text(
                phase_str + "%",
                insert=(x, y - radius - 4),
                text_anchor="middle",
                fill=style["TEXT_COLOR"],
            )
        )
    return dwg.tostring()


def plot_visible_planets(observation: "Observation", dark_mode_override: Optional[bool] = None, **args):
    try:
        from IPython.display import SVG  # pyright: ignore
    except ImportError:
        logger.warning("You can plot images only in Ipython notebook!")
        return
    return SVG(plot_visible_planets_svg(observation, dark_mode_override, **args))


def _generate_plot_messier(
    observation: "Observation", dark_mode_override: Optional[bool] = None, **args
):  # Added dark_mode_override from previous step
    if dark_mode_override is not None:
        effective_dark_mode = dark_mode_override
    else:
        effective_dark_mode = get_dark_mode()

    style = get_plot_style(effective_dark_mode)
    # plot_colors = get_plot_colors(effective_dark_mode) # Messier uses specific type colors

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
            _mark_observation(observation, ax, effective_dark_mode, style)
            _mark_good_conditions(
                observation,
                ax,
                observation.conditions.min_object_altitude,
                90,
                effective_dark_mode,
                style,
            )
            Utils.annotate_plot(ax, "Altitude [°]", effective_dark_mode)
            ax.set_title("Messier Objects Altitude", color=style["TEXT_COLOR"])
            logger.info("Generated empty Messier plot as no objects are visible.")
            return fig

        LIGHT_MESSIER_TYPE_COLORS = {
            "Galaxy": "#8CA2AD",  # Muted Blue-Grey
            "Globular Cluster": "#A38F9B",  # Muted Rose/Brown
            "Open Cluster": "#8EA397",  # Muted Green
            "Nebula": "#9B8FA3",  # Muted Purple
            "Planetary Nebula": "#A39B8F",  # Muted Orange/Brown
            "Supernova Remnant": "#AD9F9A",  # Muted Brown-Grey
            "Other": "#A0A0A0",  # Mid-Gray
        }
        DARK_MESSIER_TYPE_COLORS = {
            "Galaxy": "#5A1A75",  # Bright Purple
            "Globular Cluster": "#CCCCCC",  # Light Gray
            "Open Cluster": "#FFFFFF",  # White
            "Nebula": "#5A1A75",  # Bright Purple (or a different shade)
            "Planetary Nebula": "#007447",  # Vibrant Green
            "Supernova Remnant": "#BBBBBB",  # Muted Light Gray
            "Other": "#999999",  # Another Muted Gray
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
            altitude = obj[ObjectTableLabels.ALTITUDE]
            obj_type = obj["Type"]
            width = obj[ObjectTableLabels.WIDTH]
            height = obj["Height"] if "Height" in obj else width
            messier_id = obj[ObjectTableLabels.MESSIER]
            marker_size = (width * height) ** 0.5
            color = current_messier_colors.get(
                obj_type, current_messier_colors["Other"] 
            )  # pyright: ignore
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
        _mark_observation(observation, ax, effective_dark_mode, style)
        _mark_good_conditions(
            observation, ax, observation.conditions.min_object_altitude, 90, effective_dark_mode, style
        )
        Utils.annotate_plot(ax, "Altitude [°]", effective_dark_mode)

        legend_handles = [
            lines.Line2D(
                [0],
                [0],
                marker="o",
                color="w",
                label=obj_type,  # 'w' background for marker for visibility
                markerfacecolor=color,
                markersize=10,
            )
            for obj_type, color in plotted_types.items()
        ]
        legend = ax.legend(handles=legend_handles, title="Object Types")
        legend.get_frame().set_facecolor(style["AXES_FACE_COLOR"])
        legend.get_frame().set_edgecolor(style["AXIS_COLOR"])
        legend.get_title().set_color(style["TEXT_COLOR"])
        for text in legend.get_texts():
            text.set_color(style["TEXT_COLOR"])

        ax.set_title("Messier Objects Altitude", color=style["TEXT_COLOR"])
        logger.info("Successfully generated Messier plot.")
        return fig

    except Exception as e:
        logger.error(f"Error generating Messier plot: {e}", exc_info=True)
        ax.clear()  # Clear existing axes
        fig.patch.set_facecolor(
            style["FIGURE_FACE_COLOR"]
        )  # Ensure figure bg is set
        ax.set_facecolor(style["AXES_FACE_COLOR"])  # Ensure axes bg is set

        error_text_color = "#FF6B6B" if effective_dark_mode else "red"
        ax.text(
            0.5,
            0.5,
            "Error generating Messier plot.\nSee logs for details.",
            horizontalalignment="center",
            verticalalignment="center",
            fontsize=12,
            color=error_text_color,
            wrap=True,
            transform=ax.transAxes,
        )
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_title("Messier Plot Error", color=style["TEXT_COLOR"])
        return fig


def plot_messier(observation: "Observation", dark_mode_override: Optional[bool] = None, **args):
    return _generate_plot_messier(
        observation, dark_mode_override=dark_mode_override, **args
    )


def _generate_plot_planets(observation: "Observation", dark_mode_override: Optional[bool] = None, **args):
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
        _mark_observation(observation, ax, effective_dark_mode, style)
        _mark_good_conditions(
            observation, ax, observation.conditions.min_object_altitude, 90, effective_dark_mode, style
        )
        Utils.annotate_plot(ax, "Altitude [°]", effective_dark_mode)
        ax.set_title("Solar Objects Altitude", color=style["TEXT_COLOR"])
        return fig

    default_planet_color = plot_colors.get(OpticalType.GENERIC, "#888888")

    for _, planet in planets_df.iterrows():
        name = planet[ObjectTableLabels.NAME]
        skyfield_object = observation.local_planets.get_skyfield_object(planet)

        curve_df = observation.place.get_altaz_curve(
            skyfield_object, observation.start, observation.stop
        )

        specific_planet_color = get_planet_color(
            name, effective_dark_mode, default_planet_color
        )  # pyright: ignore

        # Plot altitude curve
        ax.plot(
            curve_df["Time"].apply(lambda t: t.utc_datetime()),
            curve_df["Altitude"],
            color=specific_planet_color,
            label=name,
        )

        # Mark rise and set times
        if planet[ObjectTableLabels.RISING] is not None:
            ax.scatter(
                planet[ObjectTableLabels.RISING],
                0,
                marker="^",
                color=specific_planet_color,
                s=100,
            )
        if planet[ObjectTableLabels.SETTING] is not None:
            ax.scatter(
                planet[ObjectTableLabels.SETTING],
                0,
                marker="v",
                color=specific_planet_color,
                s=100,
            )

        # Annotate planet name
        # Find a good position for the annotation, e.g., at the peak of the curve
        peak_idx = curve_df["Altitude"].idxmax()
        peak_time = curve_df["Time"].iloc[peak_idx].utc_datetime()
        peak_alt = curve_df["Altitude"].iloc[peak_idx]
        ax.annotate(
            name,
            (peak_time, peak_alt),
            xytext=(5, 5),
            textcoords="offset points",
            color=style["TEXT_COLOR"],
        )  # pyright: ignore

    if observation.start is not None and observation.stop is not None:
        ax.set_xlim([observation.start, observation.stop])
    ax.set_ylim(0, 90)
    date_format = mdates.DateFormatter("%H:%M", tz=observation.place.local_timezone)
    ax.xaxis.set_major_formatter(date_format)

    _mark_observation(observation, ax, effective_dark_mode, style)
    _mark_good_conditions(
        observation, ax, observation.conditions.min_object_altitude, 90, effective_dark_mode, style
    )
    Utils.annotate_plot(ax, "Altitude [°]", effective_dark_mode)
    ax.set_title("Solar Objects Altitude", color=style["TEXT_COLOR"])
    ax.legend()

    return fig


def plot_planets(observation: "Observation", dark_mode_override: Optional[bool] = None, **args):
    return _generate_plot_planets(
        observation, dark_mode_override=dark_mode_override, **args
    )


def plot_weather(observation: "Observation", dark_mode_override: Optional[bool] = None, **args):
    logger.info(
        f"plot_weather called for place: {observation.place.name}. Current observation.place.weather is: {type(observation.place.weather)}"
    )
    if observation.place.weather is None:
        logger.info(
            "observation.place.weather is None, calling observation.place.get_weather()..."
        )
        try:
            observation.place.get_weather()
            logger.info(
                f"observation.place.get_weather() called. observation.place.weather is now: {type(observation.place.weather)}"
            )
            if observation.place.weather is not None:
                # Add a log for a key attribute if it exists, e.g., hourly data
                if (
                    hasattr(observation.place.weather, "hourly")
                    and observation.place.weather.hourly is not None
                ):
                    logger.info(
                        f"Weather hourly data length: {len(observation.place.weather.hourly.time) if hasattr(observation.place.weather.hourly, 'time') else 'N/A'}"
                    )
                else:
                    logger.info(
                        "Weather hourly data is None or not present after get_weather."
                    )
        except Exception as e:
            logger.error(
                f"Error calling observation.place.get_weather(): {e}", exc_info=True
            )
    else:
        logger.info("observation.place.weather already exists, not calling get_weather().")
    return _generate_plot_weather(
        observation, dark_mode_override=dark_mode_override, **args
    )


def _generate_plot_weather(observation: "Observation", dark_mode_override: Optional[bool] = None, **args):
    if dark_mode_override is not None:
        effective_dark_mode = dark_mode_override
    else:
        effective_dark_mode = get_dark_mode()

    style = get_plot_style(effective_dark_mode)

    logger.info(
        f"_generate_plot_weather called. observation.place.weather type: {type(observation.place.weather)}"
    )
    if observation.place.weather is None:
        logger.warning(
            "_generate_plot_weather: observation.place.weather is None. Cannot generate plots. Returning error plot."
        )
        fig_err, ax_err = pyplot.subplots(figsize=(10, 6))
        fig_err.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
        ax_err.set_facecolor(style["AXES_FACE_COLOR"])
        warning_color = (
            "#FFCC00" if effective_dark_mode else "orange" 
        )  # Light orange for dark mode
        ax_err.text(
            0.5,
            0.5,
            "Weather data not available for plotting.\n(observation.place.weather was None)",
            horizontalalignment="center",
            verticalalignment="center",
            fontsize=12,
            color=warning_color,
            wrap=True,
            transform=ax_err.transAxes,
        )
        ax_err.set_xticks([])
        ax_err.set_yticks([])
        ax_err.set_title("Weather Plot Information", color=style["TEXT_COLOR"])
        return fig_err
    try:
        axes_arg = args.pop("ax", None)
        fig = None
        axes = None

        if (
            axes_arg is not None
            and isinstance(axes_arg, numpy.ndarray)
            and axes_arg.shape == (5, 2) 
        ):  # Assuming numpy is available
            axes = axes_arg
            fig = axes[0, 0].figure
            logger.debug("Using provided axes for weather plot.")
        else:
            fig, axes = pyplot.subplots(nrows=5, ncols=2, figsize=(13, 22), **args)
            logger.debug("Created new figure and axes for weather plot.")

        fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
        # Individual subplots face colors will be handled by their respective plot_... methods in weather.py (next subtask)
        # For now, we set the overall figure background. Titles and labels within this function are not present.
        # The _mark_observation and _mark_good_conditions calls below are on plots returned by weather.py methods.
        # Those methods in weather.py will need to be dark-mode aware to correctly style their axes.

        logger.debug("Plotting clouds...")
        # The plot_clouds method itself will need to be dark_mode aware.
        # The plot_clouds method itself (and others from weather.py) will use their own dark_mode_override logic.
        # The effective_dark_mode is passed to them to ensure consistency.
        plt_clouds_ax = observation.place.weather.plot_clouds(
            ax=axes[0, 0], dark_mode_override=effective_dark_mode
        )
        if plt_clouds_ax:
            _mark_observation(observation, plt_clouds_ax, effective_dark_mode, style)
        if plt_clouds_ax:
            _mark_good_conditions(
                observation,
                plt_clouds_ax,
                0,
                observation.conditions.max_clouds,
                effective_dark_mode,
                style,
            )

        logger.debug("Plotting clouds summary...")
        observation.place.weather.plot_clouds_summary(
            ax=axes[0, 1], dark_mode_override=effective_dark_mode
        )

        logger.debug("Plotting precipitation...")
        plt_precip_ax = observation.place.weather.plot_precipitation(
            ax=axes[1, 0], dark_mode_override=effective_dark_mode
        )
        if plt_precip_ax:
            _mark_observation(observation, plt_precip_ax, effective_dark_mode, style)
        if plt_precip_ax:
            _mark_good_conditions(
                observation,
                plt_precip_ax,
                0,
                observation.conditions.max_precipitation_probability,
                effective_dark_mode,
                style,
            )

        logger.debug("Plotting precipitation type summary...")
        observation.place.weather.plot_precipitation_type_summary(
            ax=axes[1, 1], dark_mode_override=effective_dark_mode
        )

        logger.debug("Plotting temperature...")
        plt_temp_ax = observation.place.weather.plot_temperature(
            ax=axes[2, 0], dark_mode_override=effective_dark_mode
        )
        if plt_temp_ax:
            _mark_observation(observation, plt_temp_ax, effective_dark_mode, style)
        if plt_temp_ax:
            _mark_good_conditions(
                observation,
                plt_temp_ax,
                observation.conditions.min_temperature,
                observation.conditions.max_temperature,
                effective_dark_mode,
                style,
            )

        logger.debug("Plotting wind...")
        plt_wind_ax = observation.place.weather.plot_wind(
            ax=axes[2, 1], dark_mode_override=effective_dark_mode
        )
        if plt_wind_ax:
            _mark_observation(observation, plt_wind_ax, effective_dark_mode, style)
        if plt_wind_ax:
            _mark_good_conditions(
                observation, plt_wind_ax, 0, observation.conditions.max_wind, effective_dark_mode, style
            )

        logger.debug("Plotting pressure and ozone...")
        plt_pressure_ax = observation.place.weather.plot_pressure_and_ozone(
            ax=axes[3, 0], dark_mode_override=effective_dark_mode
        )
        if plt_pressure_ax:
            _mark_observation(observation, plt_pressure_ax, effective_dark_mode, style)

        logger.debug("Plotting visibility...")
        plt_visibility_ax = observation.place.weather.plot_visibility(
            ax=axes[3, 1], dark_mode_override=effective_dark_mode
        )
        if plt_visibility_ax:
            _mark_observation(observation, plt_visibility_ax, effective_dark_mode, style)

        logger.debug("Plotting moon phase...")
        plt_moon_phase_ax = observation.place.weather.plot_moon_phase(
            ax=axes[4, 0], dark_mode_override=effective_dark_mode
        )
        if plt_moon_phase_ax:
            _mark_observation(observation, plt_moon_phase_ax, effective_dark_mode, style)

        fig.tight_layout()
        logger.info(
            "Successfully generated Weather plot (figure setup). Sub-plot styling uses dark_mode_override."
        )
        return fig

    except Exception as e:
        logger.error(f"Error generating Weather plot details: {e}", exc_info=True)
        # Ensure fig is defined for closing
        current_fig = locals().get("fig", None)
        if current_fig is not None:
            try:
                pyplot.close(current_fig)
            except Exception as close_exc:
                logger.error(
                    f"Error closing figure during weather plot error handling: {close_exc}"
                )

        fig_err, ax_err = pyplot.subplots(figsize=(10, 6))
        fig_err.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
        ax_err.set_facecolor(style["AXES_FACE_COLOR"])
        error_color = (
            "#FF6B6B" if effective_dark_mode else "red" 
        )  # Light red for dark mode
        ax_err.text(
            0.5,
            0.5,
            "Error generating Weather plot details.\nSee logs for specifics.",
            horizontalalignment="center",
            verticalalignment="center",
            fontsize=12,
            color=error_color,
            wrap=True,
            transform=ax_err.transAxes,
        )
        ax_err.set_xticks([])
        ax_err.set_yticks([])
        ax_err.set_title("Weather Plot Error", color=style["TEXT_COLOR"])
        return fig_err


def plot_sun_and_moon_path(observation: "Observation", dark_mode_override: Optional[bool] = None, **args):
    if observation.sun_observation:
        return observation.place.plot_sun_path(dark_mode_override, **args)
    else:
        return observation.place.plot_moon_path(dark_mode_override, **args)


def _plot_stars_on_skymap(observation: "Observation", ax, observer, mag_limit, is_polar, style: dict, zoom_deg: Optional[float] = None):
    stars = get_hipparcos_data()

    if mag_limit is not None:
        limit = mag_limit
    elif is_polar:
        limit = 4.5
    elif zoom_deg is not None:
        limit = 7.5
    else:
        limit = 6.0

    bright_stars = stars[stars["magnitude"] <= limit]
    star_positions = observer.observe(Star.from_dataframe(bright_stars))
    alt, az, _ = star_positions.apparent().altaz()

    visible = alt.degrees > 0

    if not is_polar and zoom_deg is not None:
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()
        az_degrees = az.degrees[visible]
        alt_degrees = alt.degrees[visible]
        zoom_mask = (az_degrees > xlim[0]) & (az_degrees < xlim[1]) & (alt_degrees > ylim[0]) & (alt_degrees < ylim[1])
        
        visible_indices = numpy.where(visible)[0][zoom_mask]
        alt_plot = alt[visible_indices]
        az_plot = az[visible_indices]
        mag_plot = bright_stars["magnitude"].iloc[visible_indices]

        sizes = (limit + 1 - numpy.array(mag_plot)) * 3
        ax.scatter(
            az_plot.degrees,
            alt_plot.degrees,
            s=sizes,
            color=style["TEXT_COLOR"],
            marker=".",
        )
    else:
        sizes = (limit + 1 - numpy.array(bright_stars["magnitude"][visible])) * (
            5 if is_polar else 3
        )
        if is_polar:
            ax.scatter(
                az.radians[visible],
                90 - alt.degrees[visible],
                s=sizes,
                color=ax.get_facecolor(),
                marker=".",
                edgecolors=style["TEXT_COLOR"],
            )
        else:
            ax.scatter(
                az.degrees[visible],
                alt.degrees[visible],
                s=sizes,
                color=style["TEXT_COLOR"],
                marker=".",
            )


def _plot_messier_on_skymap(observation: "Observation", ax, observer, is_polar):
    visible_messier = observation.get_visible_messier()
    if not visible_messier.empty:
        for _, m_obj in visible_messier.iterrows():
            messier_name = m_obj[ObjectTableLabels.MESSIER]
            messier_object = observation.local_messier.find_by_name(messier_name)
            if messier_object:
                alt, az, _ = observer.observe(messier_object).apparent().altaz()
                if alt.degrees > 0:
                    if is_polar:
                        ax.scatter(
                            az.radians,
                            90 - alt.degrees,
                            s=50,
                            color="red",
                            marker="+",
                        )
                        ax.annotate(
                            messier_name,
                            (az.radians, 90 - alt.degrees),
                            textcoords="offset points",
                            xytext=(5, 5),
                            color="red",
                        )
                    else:
                        ax.scatter(
                            az.degrees, alt.degrees, s=50, color="red", marker="+"
                        )
                        ax.annotate(
                            messier_name,
                            (az.degrees, alt.degrees),
                            textcoords="offset points",
                            xytext=(5, 5),
                            color="red",
                        )


def _plot_ngc_on_skymap(observation: "Observation", ax, observer, is_polar):
    visible_ngc = observation.get_visible_ngc()
    if not visible_ngc.empty:
        for _, n_obj in visible_ngc.iterrows():
            ngc_name = n_obj[ObjectTableLabels.NGC]
            ngc_object = observation.local_ngc.find_by_name(ngc_name)
            if ngc_object:
                alt, az, _ = observer.observe(ngc_object).apparent().altaz()
                if alt.degrees > 0:
                    if is_polar:
                        ax.scatter(
                            az.radians,
                            90 - alt.degrees,
                            s=50,
                            color="green",
                            marker="x",
                        )
                        ax.annotate(
                            ngc_name,
                            (az.radians, 90 - alt.degrees),
                            textcoords="offset points",
                            xytext=(5, 5),
                            color="green",
                        )
                    else:
                        ax.scatter(
                            az.degrees, alt.degrees, s=50, color="green", marker="x"
                        )
                        ax.annotate(
                            ngc_name,
                            (az.degrees, alt.degrees),
                            textcoords="offset points",
                            xytext=(5, 5),
                            color="green",
                        )


def _plot_planets_on_skymap(
    observation: "Observation", ax, observer, is_polar, effective_dark_mode, style
):
    visible_planets = observation.get_visible_planets()
    if not visible_planets.empty:
        for _, p_obj in visible_planets.iterrows():
            planet_name = p_obj[ObjectTableLabels.NAME]
            planet_object = observation.local_planets.find_by_name(planet_name)
            if planet_object:
                alt, az, _ = observer.observe(planet_object).apparent().altaz()
                if alt.degrees > 0:
                    planet_color = get_planet_color(
                        planet_name, effective_dark_mode, style["TEXT_COLOR"]
                    )
                    if is_polar:
                        ax.scatter(
                            az.radians,
                            90 - alt.degrees,
                            s=100,
                            color=planet_color,
                            marker="o",
                        )
                        ax.annotate(
                            planet_name,
                            (az.radians, 90 - alt.degrees),
                            textcoords="offset points",
                            xytext=(5, 5),
                            color=planet_color,
                        )
                    else:
                        ax.scatter(
                            az.degrees,
                            alt.degrees,
                            s=100,
                            color=planet_color,
                            marker="o",
                        )
                        ax.annotate(
                            planet_name,
                            (az.degrees, alt.degrees),
                            textcoords="offset points",
                            xytext=(5, 5),
                            color=planet_color,
                        )


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
    **kwargs,
):
    """
    Generates a skymap for the current time and location, highlighting a target object.
    Can generate a full polar skymap or a zoomed-in Cartesian skymap.
    """
    if dark_mode_override is not None:
        effective_dark_mode = dark_mode_override
    else:
        effective_dark_mode = get_dark_mode()

    style = get_plot_style(effective_dark_mode)

    # Time for observation
    t = observation.place.ts.now()
    if observation.effective_date is not None:
        t = observation.effective_date
    observer = observation.place.observer.at(t)

    # Format the generation time
    generation_time_str = t.astimezone(observation.place.local_timezone).strftime(
        "%Y-%m-%d %H:%M %Z"
    )

    # Find target object first, as we need its coordinates for zoom
    target_object = observation.local_messier.find_by_name(target_name)
    if target_object is None:
        target_object = observation.local_planets.find_by_name(target_name)
    if target_object is None:
        target_object = observation.local_ngc.find_by_name(target_name)
    if target_object is None:
        target_object = observation.local_stars.find_by_name(target_name)

    if not target_object:
        fig, ax = pyplot.subplots(figsize=(10, 10))
        fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
        ax.set_facecolor(style["AXES_FACE_COLOR"])
        ax.text(
            0.5,
            0.5,
            f"Object '{target_name}' not found.",
            horizontalalignment="center",
            verticalalignment="center",
            transform=ax.transAxes,
            color=style["TEXT_COLOR"],
        )
        ax.set_title(
            f"Skymap (Generated: {generation_time_str})",
            color=style["TEXT_COLOR"],
        )
        return fig

    target_alt, target_az, _ = observer.observe(target_object).apparent().altaz()

    # If zoomed view is requested
    if zoom_deg is not None:
        if target_alt.degrees < 0:
            fig, ax = pyplot.subplots(figsize=(10, 10))
            fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
            ax.set_facecolor(style["AXES_FACE_COLOR"])
            ax.text(
                0.5,
                0.5,
                f"Target '{target_name}' is below the horizon.",
                horizontalalignment="center",
                verticalalignment="center",
                transform=ax.transAxes,
                color=style["TEXT_COLOR"],
            )
            ax.set_title(
                f"Skymap for {target_name} (Generated: {generation_time_str})",
                color=style["TEXT_COLOR"],
            )
            return fig

        fig, ax = pyplot.subplots(figsize=(10, 10))
        fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
        ax.set_facecolor(style["AXES_FACE_COLOR"])

        ax.set_xlabel("Azimuth (°)", color=style["TEXT_COLOR"])
        ax.set_ylabel("Altitude (°)", color=style["TEXT_COLOR"])
        ax.tick_params(axis="x", colors=style["TEXT_COLOR"])
        ax.tick_params(axis="y", colors=style["TEXT_COLOR"])
        ax.spines["left"].set_color(style["AXIS_COLOR"])
        ax.spines["bottom"].set_color(style["AXIS_COLOR"])
        ax.spines["top"].set_color(style["AXIS_COLOR"])
        ax.spines["right"].set_color(style["AXIS_COLOR"])

        half_zoom = zoom_deg / 2
        ax.set_xlim(target_az.degrees - half_zoom, target_az.degrees + half_zoom)
        ax.set_ylim(target_alt.degrees - half_zoom, target_alt.degrees + half_zoom)
        ax.set_aspect("equal", adjustable="box")
        ax.grid(True, color=style["GRID_COLOR"], linestyle="--", linewidth=0.5)

        # Plot celestial objects
        if plot_stars:
            _plot_stars_on_skymap(
                observation, ax, observer, star_magnitude_limit, is_polar=False, style=style, zoom_deg=zoom_deg
            )
        if plot_messier:
            _plot_messier_on_skymap(observation, ax, observer, is_polar=False)
        if plot_ngc:
            _plot_ngc_on_skymap(observation, ax, observer, is_polar=False)
        if plot_planets:
            _plot_planets_on_skymap(
                observation,
                ax,
                observer,
                is_polar=False,
                effective_dark_mode=effective_dark_mode,
                style=style,
            )

        # 4. Highlight target object
        ax.scatter(
            target_az.degrees,
            target_alt.degrees,
            s=200,
            facecolors="none",
            edgecolors="yellow",
            marker="o",
            linewidths=2,
        )
        ax.annotate(
            target_name,
            (target_az.degrees, target_alt.degrees),
            textcoords="offset points",
            xytext=(0, 15),
            color="yellow",
            ha="center",
            fontsize=12,
        )

        # 4. Highlight target object
        ax.scatter(
            target_az.degrees,
            target_alt.degrees,
            s=200,
            facecolors="none",
            edgecolors="yellow",
            marker="o",
            linewidths=2,
        )
        ax.annotate(
            target_name,
            (target_az.degrees, target_alt.degrees),
            textcoords="offset points",
            xytext=(0, 15),
            color="yellow",
            ha="center",
            fontsize=12,
        )
        ax.set_title(
            f"Skymap for {target_name} ({zoom_deg}° view, Generated: {generation_time_str})",
            color=style["TEXT_COLOR"],
        )
        return fig
    else:
        # --- Full sky (polar) plot logic (existing code) ---
        fig, ax = pyplot.subplots(
            figsize=(10, 10), subplot_kw={"projection": "polar"}
        )
        fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
        ax.set_facecolor(style["AXES_FACE_COLOR"])
        ax.set_rlim(0, 90)  # Zenith angle from 0 (zenith) to 90 (horizon)
        ax.set_theta_zero_location("N")
        ax.set_theta_direction(-1)
        ax.grid(True, color=style["GRID_COLOR"], linestyle="--", linewidth=0.5)

        # Custom radial labels for altitude
        ax.set_yticks([0, 30, 60, 90])  # Zenith angles
        ax.set_yticklabels(["90°", "60°", "30°", "0°"], color=style["TEXT_COLOR"])
        ax.set_rlabel_position(22.5)  # Move labels away from the line

        # Add cardinal direction labels
        cardinal_directions = {
            "N": 0,
            "E": numpy.pi / 2,
            "S": numpy.pi,
            "W": 3 * numpy.pi / 2,
        }
        for direction, angle in cardinal_directions.items():
            ax.text(
                angle,
                95,  # Place it just outside the 90-degree limit
                direction,
                ha="center",
                va="center",
                color=style["TEXT_COLOR"],
                fontsize=12,
            )

        # Define good condition highlight color
        good_condition_color = style.get(
            "GOOD_CONDITION_HL_COLOR",
            "#90EE90" if not effective_dark_mode else "#007447",
        )

        # Calculate altitude boundaries
        r_inner_good = 0
        r_outer_good = 90 - observation.conditions.min_object_altitude

        # Calculate azimuth boundaries
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

        # Plot celestial objects
        if plot_stars:
            _plot_stars_on_skymap(
                observation, ax, observer, star_magnitude_limit, is_polar=True, style=style, zoom_deg=zoom_deg
            )
        if plot_messier:
            _plot_messier_on_skymap(observation, ax, observer, is_polar=True)
        if plot_ngc:
            _plot_ngc_on_skymap(observation, ax, observer, is_polar=True)
        if plot_planets:
            _plot_planets_on_skymap(
                observation,
                ax,
                observer,
                is_polar=True,
                effective_dark_mode=effective_dark_mode,
                style=style,
            )

        # 4. Highlight target object
        if target_alt.degrees > 0:
            ax.scatter(
                target_az.radians,
                90 - target_alt.degrees,
                s=200,
                facecolors="none",
                edgecolors="yellow",
                marker="o",
                linewidths=2,
            )
            ax.annotate(
                target_name,
                (target_az.radians, 90 - target_alt.degrees),
                textcoords="offset points",
                xytext=(0, 15),
                color="yellow",
                ha="center",
                fontsize=12,
            )

        # 4. Highlight target object
        if target_alt.degrees > 0:
            ax.scatter(
                target_az.radians,
                90 - target_alt.degrees,
                s=200,
                facecolors="none",
                edgecolors="yellow",
                marker="o",
                linewidths=2,
            )
            ax.annotate(
                target_name,
                (target_az.radians, 90 - target_alt.degrees),
                textcoords="offset points",
                xytext=(0, 15),
                color="yellow",
                ha="center",
                fontsize=12,
            )
        ax.set_title(
            f"Skymap for {target_name} (Generated: {generation_time_str})",
            color=style["TEXT_COLOR"],
        )

        return fig


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
    **kwargs,
):
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
        **kwargs,
    )


def _mark_observation(observation: "Observation", plot, dark_mode_enabled: bool, style: dict):
    if plot is None:
        return
    # Use dedicated span colors from the style dictionary
    plot.axvspan(
        observation.start,
        observation.stop,
        color=style.get(
            "SPAN_BACKGROUND_COLOR",
            "#DDDDDD" if not dark_mode_enabled else "#FFFFFF",
        ),
        alpha=0.07 if dark_mode_enabled else 0.2,  # Default light mode color if key missing
    )
    moon_start, moon_stop = _normalize_dates(
        observation.place.moonrise_time(), observation.place.moonset_time()
    )
    plot.axvspan(
        moon_start,
        moon_stop,
        color=style.get(
            "MOON_SPAN_COLOR", "#FFFFE0" if not dark_mode_enabled else "#5A1A75"
        ),
        alpha=0.07 if dark_mode_enabled else 0.1,  # Default light mode color if key missing
    )

    plot.axvline(observation.start, color=style["GRID_COLOR"], linestyle="--")
    plot.axvline(observation.time_limit, color=style["GRID_COLOR"], linestyle="--")


def _mark_good_conditions(
    observation: "Observation", plot, minimal, maximal, dark_mode_enabled: bool, style: dict
):
    if plot is None:
        return
    # Use dedicated good condition highlight color
    plot.axhspan(
        minimal,
        maximal,
        color=style.get(
            "GOOD_CONDITION_HL_COLOR",
            "#90EE90" if not dark_mode_enabled else "#007447",
        ),
        alpha=0.1,  # Default light mode color if key missing. Alpha is same for both.
    )
