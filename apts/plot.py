import logging
from datetime import timedelta, datetime
from typing import Optional, TYPE_CHECKING

import matplotlib.dates as mdates
import numpy
import pandas as pd
import svgwrite as svg
from matplotlib import pyplot, lines
from matplotlib.patches import Ellipse
from skyfield.api import Star as SkyfieldStar

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
    default_fill_color = style["AXES_FACE_COLOR"]

    visible_planets = observation.get_visible_planets(**args)
    dwg = svg.Drawing(style={"background-color": style["BACKGROUND_COLOR"]})
    if not visible_planets.empty:
        max_size = visible_planets[["Size"]].max().iloc[0]
        max_size_val = (
            max_size.magnitude if hasattr(max_size, "magnitude") else max_size
        )
    else:
        max_size_val = 0
    y = int(max_size_val + 12)
    x = 20
    minimal_delta = 52
    last_radius = None
    for planet in visible_planets[["Name", "Size", "Phase", "TechnicalName"]].values:
        name = planet[0]
        radius_with_units = planet[1]
        radius = (
            radius_with_units.magnitude
            if hasattr(radius_with_units, "magnitude")
            else radius_with_units
        )
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
                fill=get_planet_color(name, effective_dark_mode, default_fill_color),
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


def plot_visible_planets(
    observation: "Observation", dark_mode_override: Optional[bool] = None, **args
):
    try:
        from IPython.display import SVG  # pyright: ignore
    except ImportError:
        logger.warning("You can plot images only in Ipython notebook!")
        return
    return SVG(plot_visible_planets_svg(observation, dark_mode_override, **args))


def _generate_plot_messier(
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
            "Galaxy": "#8CA2AD",
            "Globular Cluster": "#A38F9B",
            "Open Cluster": "#8EA397",
            "Nebula": "#9B8FA3",
            "Planetary Nebula": "#A39B8F",
            "Supernova Remnant": "#AD9F9A",
            "Other": "#A0A0A0",
        }
        DARK_MESSIER_TYPE_COLORS = {
            "Galaxy": "#5A1A75",
            "Globular Cluster": "#CCCCCC",
            "Open Cluster": "#FFFFFF",
            "Nebula": "#5A1A75",
            "Planetary Nebula": "#007447",
            "Supernova Remnant": "#BBBBBB",
            "Other": "#999999",
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
        ax.clear()
        fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
        ax.set_facecolor(style["AXES_FACE_COLOR"])

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


def plot_messier(
    observation: "Observation", dark_mode_override: Optional[bool] = None, **args
):
    return _generate_plot_messier(
        observation, dark_mode_override=dark_mode_override, **args
    )


def _generate_plot_planets(
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
        )

        ax.plot(
            curve_df["Time"].apply(lambda t: t.utc_datetime()),
            curve_df["Altitude"],
            color=specific_planet_color,
            label=name,
        )

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

        peak_idx = curve_df["Altitude"].idxmax()
        peak_time = curve_df["Time"].iloc[peak_idx].utc_datetime()
        peak_alt = curve_df["Altitude"].iloc[peak_idx]
        ax.annotate(
            name,
            (peak_time, peak_alt),
            xytext=(5, 5),
            textcoords="offset points",
            color=style["TEXT_COLOR"],
        )

    if observation.start is not None and observation.stop is not None:
        ax.set_xlim([observation.start, observation.stop])
    ax.set_ylim(0, 90)
    date_format = mdates.DateFormatter("%H:%M", tz=observation.place.local_timezone)
    ax.xaxis.set_major_formatter(date_format)

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
    ax.set_title("Solar Objects Altitude", color=style["TEXT_COLOR"])
    ax.legend()

    return fig


def plot_planets(
    observation: "Observation", dark_mode_override: Optional[bool] = None, **args
):
    return _generate_plot_planets(
        observation, dark_mode_override=dark_mode_override, **args
    )


def plot_weather(
    observation: "Observation", dark_mode_override: Optional[bool] = None, **args
):
    if observation.place.weather is None:
        observation.place.get_weather()
    return _generate_plot_weather(
        observation, dark_mode_override=dark_mode_override, **args
    )


def _generate_plot_weather(
    observation: "Observation", dark_mode_override: Optional[bool] = None, **args
):
    if dark_mode_override is not None:
        effective_dark_mode = dark_mode_override
    else:
        effective_dark_mode = get_dark_mode()

    style = get_plot_style(effective_dark_mode)

    if observation.place.weather is None:
        fig_err, ax_err = pyplot.subplots(figsize=(10, 6))
        fig_err.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
        ax_err.set_facecolor(style["AXES_FACE_COLOR"])
        warning_color = "#FFCC00" if effective_dark_mode else "orange"
        ax_err.text(
            0.5,
            0.5,
            "Weather data not available for plotting.",
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
        ):
            axes = axes_arg
            fig = axes[0, 0].figure
        else:
            fig, axes = pyplot.subplots(nrows=5, ncols=2, figsize=(13, 22), **args)

        fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])

        axes[4, 1].axis("off")

        plt_clouds_ax = observation.place.weather.plot_clouds(
            ax=axes[0, 0], dark_mode_override=effective_dark_mode
        )
        if plt_clouds_ax:
            _mark_observation(observation, plt_clouds_ax, effective_dark_mode, style)
            _mark_good_conditions(
                observation,
                plt_clouds_ax,
                0,
                observation.conditions.max_clouds,
                effective_dark_mode,
                style,
            )

        observation.place.weather.plot_clouds_summary(
            ax=axes[0, 1], dark_mode_override=effective_dark_mode
        )

        plt_precip_ax = observation.place.weather.plot_precipitation(
            ax=axes[1, 0], dark_mode_override=effective_dark_mode
        )
        if plt_precip_ax:
            _mark_observation(observation, plt_precip_ax, effective_dark_mode, style)
            _mark_good_conditions(
                observation,
                plt_precip_ax,
                0,
                observation.conditions.max_precipitation_probability,
                effective_dark_mode,
                style,
            )

        observation.place.weather.plot_precipitation_type_summary(
            ax=axes[1, 1], dark_mode_override=effective_dark_mode
        )

        plt_temp_ax = observation.place.weather.plot_temperature(
            ax=axes[2, 0], dark_mode_override=effective_dark_mode
        )
        if plt_temp_ax:
            _mark_observation(observation, plt_temp_ax, effective_dark_mode, style)
            _mark_good_conditions(
                observation,
                plt_temp_ax,
                observation.conditions.min_temperature,
                observation.conditions.max_temperature,
                effective_dark_mode,
                style,
            )

        plt_wind_ax = observation.place.weather.plot_wind(
            ax=axes[2, 1], dark_mode_override=effective_dark_mode
        )
        if plt_wind_ax:
            _mark_observation(observation, plt_wind_ax, effective_dark_mode, style)
            _mark_good_conditions(
                observation,
                plt_wind_ax,
                0,
                observation.conditions.max_wind,
                effective_dark_mode,
                style,
            )

        plt_pressure_ax = observation.place.weather.plot_pressure_and_ozone(
            ax=axes[3, 0], dark_mode_override=effective_dark_mode
        )
        if plt_pressure_ax:
            _mark_observation(observation, plt_pressure_ax, effective_dark_mode, style)

        plt_visibility_ax = observation.place.weather.plot_visibility(
            ax=axes[3, 1], dark_mode_override=effective_dark_mode
        )
        if plt_visibility_ax:
            _mark_observation(
                observation, plt_visibility_ax, effective_dark_mode, style
            )

        plt_moon_phase_ax = observation.place.weather.plot_moon_phase(
            ax=axes[4, 0], dark_mode_override=effective_dark_mode
        )
        if plt_moon_phase_ax:
            _mark_observation(
                observation, plt_moon_phase_ax, effective_dark_mode, style
            )

        fig.tight_layout()
        return fig

    except Exception as e:
        logger.error(f"Error generating Weather plot details: {e}", exc_info=True)
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
        error_color = "#FF6B6B" if effective_dark_mode else "red"
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


def plot_sun_and_moon_path(
    observation: "Observation", dark_mode_override: Optional[bool] = None, **args
):
    if observation.sun_observation:
        return observation.place.plot_sun_path(dark_mode_override, **args)
    else:
        return observation.place.plot_moon_path(dark_mode_override, **args)


def _plot_bright_stars_on_skymap(
    observation: "Observation",
    ax,
    observer,
    is_polar,
    style: dict,
    zoom_deg: Optional[float] = None,
):
    bright_stars_df = observation.local_stars.objects.copy()
    if bright_stars_df.empty:
        return

    if hasattr(bright_stars_df["RA"].iloc[0], "magnitude"):
        bright_stars_df["RA"] = bright_stars_df["RA"].apply(lambda x: x.magnitude)
    if hasattr(bright_stars_df["Dec"].iloc[0], "magnitude"):
        bright_stars_df["Dec"] = bright_stars_df["Dec"].apply(lambda x: x.magnitude)
    if hasattr(bright_stars_df["Magnitude"].iloc[0], "magnitude"):
        bright_stars_df["Magnitude"] = bright_stars_df["Magnitude"].apply(
            lambda x: x.magnitude
        )

    bright_stars_df["epoch_year"] = 2000.0
    bright_stars_df.rename(
        columns={"RA": "ra_hours", "Dec": "dec_degrees"}, inplace=True
    )

    star_positions = observer.observe(SkyfieldStar.from_dataframe(bright_stars_df))
    alt, az, _ = star_positions.apparent().altaz()

    visible_mask = alt.degrees > 0

    df_visible = bright_stars_df[visible_mask]
    alt_visible_deg = alt.degrees[visible_mask]
    az_visible_deg = az.degrees[visible_mask]
    az_visible_rad = az.radians[visible_mask]

    if df_visible.empty:
        return

    star_color = style.get("EMPHASIS_COLOR", "yellow")

    if not is_polar and zoom_deg is not None:
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()

        zoom_mask = (
            (az_visible_deg >= xlim[0])
            & (az_visible_deg <= xlim[1])
            & (alt_visible_deg >= ylim[0])
            & (alt_visible_deg <= ylim[1])
        )

        df_zoomed = df_visible[zoom_mask]
        alt_zoomed_deg = alt_visible_deg[zoom_mask]
        az_zoomed_deg = az_visible_deg[zoom_mask]

        if df_zoomed.empty:
            return

        ax.scatter(az_zoomed_deg, alt_zoomed_deg, s=40, color=star_color, marker="*")

        for i in range(len(df_zoomed)):
            star = df_zoomed.iloc[i]
            ax.annotate(
                star["Name"],
                (az_zoomed_deg[i], alt_zoomed_deg[i]),
                textcoords="offset points",
                xytext=(5, 5),
                color=star_color,
                fontsize=8,
            )
    else:
        if is_polar:
            ax.scatter(
                az_visible_rad,
                90 - alt_visible_deg,
                s=40,
                color=star_color,
                marker="*",
            )
            for i in range(len(df_visible)):
                star = df_visible.iloc[i]
                ax.annotate(
                    star["Name"],
                    (az_visible_rad[i], 90 - alt_visible_deg[i]),
                    textcoords="offset points",
                    xytext=(5, 5),
                    color=star_color,
                    fontsize=8,
                )
        else:
            ax.scatter(
                az_visible_deg,
                alt_visible_deg,
                s=40,
                color=star_color,
                marker="*",
            )
            for i in range(len(df_visible)):
                star = df_visible.iloc[i]
                ax.annotate(
                    star["Name"],
                    (az_visible_deg[i], alt_visible_deg[i]),
                    textcoords="offset points",
                    xytext=(5, 5),
                    color=star_color,
                    fontsize=8,
                )


def _plot_stars_on_skymap(
    observation: "Observation",
    ax,
    observer,
    mag_limit,
    is_polar,
    style: dict,
    zoom_deg: Optional[float] = None,
    target_object=None,
):
    stars = get_hipparcos_data()

    if zoom_deg is not None and target_object is not None:
        # Optimization: pre-filter stars to a bounding box before expensive separation calculation
        if hasattr(target_object, 'ra'):
            ra_center_hours = target_object.ra.hours
            dec_center_degrees = target_object.dec.degrees
        else:
            # It's a planet or other solar system body
            ra, dec, _ = observer.observe(target_object).radec()
            ra_center_hours = ra.hours
            dec_center_degrees = dec.degrees

        # Create a generous bounding box around the target
        # The conversion from degrees to RA hours depends on declination,
        # but for a rough filter, a fixed factor is acceptable.
        deg_margin = zoom_deg * 2  # A larger margin to be safe
        ra_margin_hours = deg_margin / 15.0

        ra_min = ra_center_hours - ra_margin_hours
        ra_max = ra_center_hours + ra_margin_hours
        dec_min = dec_center_degrees - deg_margin
        dec_max = dec_center_degrees + deg_margin

        # Simple bounding box filter
        stars_in_box = stars[
            (stars["ra_hours"] >= ra_min)
            & (stars["ra_hours"] <= ra_max)
            & (stars["dec_degrees"] >= dec_min)
            & (stars["dec_degrees"] <= dec_max)
        ]

        # Now perform the precise separation calculation on the much smaller subset
        if not stars_in_box.empty:
                if hasattr(target_object, 'ra'):
                    center = SkyfieldStar(ra=target_object.ra, dec=target_object.dec)
                else:
                    ra, dec, _ = observer.observe(target_object).radec()
                    center = SkyfieldStar(ra_hours=ra.hours, dec_degrees=dec.degrees)
                observed_center = observer.observe(center)

                all_stars_vectors = SkyfieldStar.from_dataframe(stars_in_box)
                observed_all_stars = observer.observe(all_stars_vectors)

                dist_center = observed_center.position.au
                dist_all_stars = observed_all_stars.position.au

                vec_center_np = dist_center
                vec_all_stars_np = dist_all_stars

                dot_product = numpy.dot(vec_center_np, vec_all_stars_np)

                len_center = numpy.linalg.norm(vec_center_np, axis=0)
                len_all_stars = numpy.linalg.norm(vec_all_stars_np, axis=0)

                cosine_angle = dot_product / (len_center * len_all_stars)
                cosine_angle = numpy.clip(cosine_angle, -1.0, 1.0)

                separation_radians = numpy.arccos(cosine_angle)
                separation = numpy.degrees(separation_radians)
                nearby_mask = separation < zoom_deg
                stars = stars_in_box[nearby_mask]
        else:
            stars = stars_in_box  # empty dataframe

    if mag_limit is not None:
        limit = mag_limit
    elif is_polar:
        limit = 4.5
    elif zoom_deg is not None:
        limit = 7.5
    else:
        limit = 6.0

    bright_stars = stars[stars["magnitude"] <= limit]

    if bright_stars.empty:
        return

    star_positions = observer.observe(SkyfieldStar.from_dataframe(bright_stars))
    alt, az, _ = star_positions.apparent().altaz()

    visible = alt.degrees > 0

    if not any(visible):
        return

    if not is_polar and zoom_deg is not None:
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()

        visible_mask = alt.degrees > 0

        az_visible = az.degrees[visible_mask]
        alt_visible = alt.degrees[visible_mask]

        zoom_mask = (
            (az_visible >= xlim[0])
            & (az_visible <= xlim[1])
            & (alt_visible >= ylim[0])
            & (alt_visible <= ylim[1])
        )

        az_plot = az_visible[zoom_mask]
        alt_plot = alt_visible[zoom_mask]

        mag_plot = bright_stars[visible_mask][zoom_mask]["magnitude"]

        sizes = (limit + 1 - numpy.array(mag_plot)) * 3
        ax.scatter(
            az_plot,
            alt_plot,
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


def _plot_messier_on_skymap(
    observation: "Observation",
    ax,
    observer,
    is_polar,
    flipped_horizontally: bool = False,
    flipped_vertically: bool = False,
):
    visible_messier = observation.get_visible_messier()
    if not visible_messier.empty:
        for _, m_obj in visible_messier.iterrows():
            messier_name = m_obj[ObjectTableLabels.MESSIER]
            messier_object = observation.local_messier.find_by_name(messier_name)
            if messier_object:
                alt, az, _ = observer.observe(messier_object).apparent().altaz()
                if alt.degrees > 0:
                    width_arcmin = m_obj[ObjectTableLabels.WIDTH]
                    if hasattr(width_arcmin, "magnitude"):
                        width_arcmin = width_arcmin.magnitude
                    width_deg = width_arcmin / 60.0

                    height_arcmin = m_obj.get("Height", width_arcmin)
                    if hasattr(height_arcmin, "magnitude"):
                        height_arcmin = height_arcmin.magnitude
                    height_deg = height_arcmin / 60.0

                    angle = m_obj.get("Angle", 0)
                    if flipped_horizontally:
                        angle = -angle
                    if flipped_vertically:
                        angle = 180 - angle

                    if is_polar:
                        size = (width_deg + height_deg) / 2 * 100
                        ax.scatter(
                            az.radians,
                            90 - alt.degrees,
                            s=size,
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
                        ellipse = Ellipse(
                            xy=(az.degrees, alt.degrees),
                            width=width_deg,
                            height=height_deg,
                            angle=angle,
                            edgecolor="red",
                            facecolor="none",
                            alpha=0.6,
                        )
                        ax.add_patch(ellipse)
                        ax.annotate(
                            messier_name,
                            (az.degrees, alt.degrees),
                            textcoords="offset points",
                            xytext=(5, 5),
                            color="red",
                        )


def _parse_ra(ra_str):
    if isinstance(ra_str, str) and ra_str.count(":") == 2:
        parts = ra_str.split(":")
        return float(parts[0]) + float(parts[1]) / 60 + float(parts[2]) / 3600
    return None


def _parse_dec(dec_str):
    if isinstance(dec_str, str) and dec_str.count(":") == 2:
        sign = -1 if dec_str.startswith("-") else 1
        parts = dec_str.lstrip("+-").split(":")
        return sign * (float(parts[0]) + float(parts[1]) / 60 + float(parts[2]) / 3600)
    return None


def _plot_ngc_on_skymap(
    observation: "Observation",
    ax,
    observer,
    is_polar,
    star_magnitude_limit: Optional[float] = None,
    zoom_deg: Optional[float] = None,
    target_object=None,
    flipped_horizontally: bool = False,
    flipped_vertically: bool = False,
):
    if zoom_deg is not None and target_object is not None:
        visible_ngc = observation.local_ngc.objects.copy()
    else:
        visible_ngc = observation.get_visible_ngc(
            star_magnitude_limit=star_magnitude_limit
        )

    if not visible_ngc.empty:
        if zoom_deg is not None and target_object is not None:
            ra_center_hours = target_object.ra.hours
            dec_center_degrees = target_object.dec.degrees
            deg_margin = zoom_deg * 2
            ra_margin_hours = deg_margin / 15.0
            ra_min = ra_center_hours - ra_margin_hours
            ra_max = ra_center_hours + ra_margin_hours
            dec_min = dec_center_degrees - deg_margin
            dec_max = dec_center_degrees + deg_margin

            visible_ngc["RA_parsed"] = visible_ngc["RA"].apply(_parse_ra)
            visible_ngc["Dec_parsed"] = visible_ngc["Dec"].apply(_parse_dec)

            ngc_in_box = visible_ngc[
                (visible_ngc["RA_parsed"] >= ra_min)
                & (visible_ngc["RA_parsed"] <= ra_max)
                & (visible_ngc["Dec_parsed"] >= dec_min)
                & (visible_ngc["Dec_parsed"] <= dec_max)
            ]

            if not ngc_in_box.empty:
                center = SkyfieldStar(ra=target_object.ra, dec=target_object.dec)
                observed_center = observer.observe(center)

                all_ngc_vectors = observation.local_ngc.get_skyfield_object(ngc_in_box)
                observed_all_ngc = all_ngc_vectors.apply(observer.observe)

                dist_center = observed_center.position.au
                vec_all_ngc = observed_all_ngc.apply(lambda x: x.xyz.au)

                vec_center_np = dist_center
                vec_all_ngc_np = numpy.array(vec_all_ngc.tolist()).T

                dot_product = numpy.dot(vec_center_np, vec_all_ngc_np)

                len_center = numpy.linalg.norm(vec_center_np)
                len_all_ngc = numpy.linalg.norm(vec_all_ngc_np, axis=0)

                cosine_angle = dot_product / (len_center * len_all_ngc)
                cosine_angle = numpy.clip(cosine_angle, -1.0, 1.0)

                separation_radians = numpy.arccos(cosine_angle)
                separation = numpy.degrees(separation_radians)
                nearby_mask = separation < zoom_deg
                visible_ngc = ngc_in_box[nearby_mask]
            else:
                visible_ngc = ngc_in_box

    if not visible_ngc.empty:
        for _, n_obj in visible_ngc.iterrows():
            ngc_name = n_obj[ObjectTableLabels.NGC]
            if pd.isna(ngc_name):
                ngc_name = n_obj[ObjectTableLabels.NAME]
            ngc_object = observation.local_ngc.get_skyfield_object(n_obj)
            if ngc_object:
                alt, az, _ = observer.observe(ngc_object).apparent().altaz()
                if alt.degrees > 0:
                    width_arcmin = n_obj.get("Size", 0)
                    if hasattr(width_arcmin, "magnitude"):
                        width_arcmin = width_arcmin.magnitude
                    width_deg = width_arcmin / 60.0

                    height_arcmin = n_obj.get(
                        "MinAx", width_arcmin if width_arcmin else 0
                    )
                    if hasattr(height_arcmin, "magnitude"):
                        height_arcmin = height_arcmin.magnitude
                    height_deg = height_arcmin / 60.0

                    angle = n_obj.get("PosAng", 0)
                    if flipped_horizontally:
                        angle = -angle
                    if flipped_vertically:
                        angle = 180 - angle
                    if is_polar:
                        size = (width_deg + height_deg) / 2 * 100
                        ax.scatter(
                            az.radians,
                            90 - alt.degrees,
                            s=size,
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
                        ellipse = Ellipse(
                            xy=(az.degrees, alt.degrees),
                            width=width_deg,
                            height=height_deg,
                            angle=angle,
                            edgecolor="green",
                            facecolor="none",
                            alpha=0.6,
                        )
                        ax.add_patch(ellipse)
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
                    size_arcsec = p_obj.get(ObjectTableLabels.SIZE, 0)
                    if hasattr(size_arcsec, "magnitude"):
                        size_arcsec = size_arcsec.magnitude
                    size_deg = size_arcsec / 3600.0

                    if is_polar:
                        size = size_deg * 200
                        ax.scatter(
                            az.radians,
                            90 - alt.degrees,
                            s=size,
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
                        ellipse = Ellipse(
                            xy=(az.degrees, alt.degrees),
                            width=size_deg,
                            height=size_deg,
                            angle=0,
                            edgecolor=planet_color,
                            facecolor=planet_color,
                            alpha=0.6,
                        )
                        ax.add_patch(ellipse)
                        ax.annotate(
                            planet_name,
                            (az.degrees, alt.degrees),
                            textcoords="offset points",
                            xytext=(5, 5),
                            color=planet_color,
                        )


def _plot_sun_on_skymap(observation: "Observation", ax, observer, is_polar, style):
    sun = observation.place.sun
    alt, az, _ = observer.observe(sun).apparent().altaz()
    if alt.degrees > 0:
        # Approximate angular size of the sun
        size_deg = 0.5
        if is_polar:
            size = size_deg * 200
            ax.scatter(
                az.radians, 90 - alt.degrees, s=size, color="yellow", marker="*"
            )
            ax.annotate(
                "Sun",
                (az.radians, 90 - alt.degrees),
                textcoords="offset points",
                xytext=(5, 5),
                color="yellow",
            )
        else:
            ellipse = Ellipse(
                xy=(az.degrees, alt.degrees),
                width=size_deg,
                height=size_deg,
                angle=0,
                edgecolor="yellow",
                facecolor="yellow",
                alpha=0.6,
            )
            ax.add_patch(ellipse)
            ax.annotate(
                "Sun",
                (az.degrees, alt.degrees),
                textcoords="offset points",
                xytext=(5, 5),
                color="yellow",
            )


def _plot_moon_on_skymap(observation: "Observation", ax, observer, is_polar, style):
    moon = observation.place.moon
    alt, az, _ = observer.observe(moon).apparent().altaz()
    if alt.degrees > 0:
        # Approximate angular size of the moon
        size_deg = 0.5
        if is_polar:
            size = size_deg * 200
            ax.scatter(
                az.radians, 90 - alt.degrees, s=size, color="gray", marker="o"
            )
            ax.annotate(
                "Moon",
                (az.radians, 90 - alt.degrees),
                textcoords="offset points",
                xytext=(5, 5),
                color="gray",
            )
        else:
            ellipse = Ellipse(
                xy=(az.degrees, alt.degrees),
                width=size_deg,
                height=size_deg,
                angle=0,
                edgecolor="gray",
                facecolor="gray",
                alpha=0.6,
            )
            ax.add_patch(ellipse)
            ax.annotate(
                "Moon",
                (az.degrees, alt.degrees),
                textcoords="offset points",
                xytext=(5, 5),
                color="gray",
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
    plot_sun: bool = False,
    plot_moon: bool = False,
    plot_date: Optional[datetime] = None,
    flipped_horizontally: bool = False,
    flipped_vertically: bool = False,
    **kwargs,
):
    """
    Generates a skymap for a given time and location, highlighting a target object.
    Can generate a full polar skymap or a zoomed-in Cartesian skymap.
    """
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
    elif observation.effective_date:
        # Fallback to effective_date if start/stop are not available
        t = observation.effective_date
    else:
        # Final fallback to the current time
        t = observation.place.ts.now()

    observer = observation.place.observer.at(t)

    generation_time_str = t.astimezone(observation.place.local_timezone).strftime(
        "%Y-%m-%d %H:%M %Z"
    )

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
            )
            _plot_bright_stars_on_skymap(
                observation,
                ax,
                observer,
                is_polar=False,
                style=style,
                zoom_deg=zoom_deg,
            )
        if plot_messier:
            _plot_messier_on_skymap(
                observation,
                ax,
                observer,
                is_polar=False,
                flipped_horizontally=flipped_horizontally,
                flipped_vertically=flipped_vertically,
            )
        if plot_ngc:
            _plot_ngc_on_skymap(
                observation,
                ax,
                observer,
                is_polar=False,
                star_magnitude_limit=star_magnitude_limit,
                zoom_deg=zoom_deg,
                target_object=target_object,
                flipped_horizontally=flipped_horizontally,
                flipped_vertically=flipped_vertically,
            )
        if plot_planets:
            _plot_planets_on_skymap(
                observation,
                ax,
                observer,
                is_polar=False,
                effective_dark_mode=effective_dark_mode,
                style=style,
            )
        if plot_sun:
            _plot_sun_on_skymap(observation, ax, observer, is_polar=False, style=style)
        if plot_moon:
            _plot_moon_on_skymap(observation, ax, observer, is_polar=False, style=style)

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
        if flipped_horizontally:
            ax.invert_xaxis()
        if flipped_vertically:
            ax.invert_yaxis()
        if flipped_horizontally or flipped_vertically:
            flip_str = "Flipped "
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

        return fig
    else:
        fig, ax = pyplot.subplots(figsize=(10, 10), subplot_kw={"projection": "polar"})
        fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
        ax.set_facecolor(style["AXES_FACE_COLOR"])
        ax.set_rlim(0, 90)
        ax.set_theta_zero_location("N")
        ax.set_theta_direction(-1)
        ax.grid(True, color=style["GRID_COLOR"], linestyle="--", linewidth=0.5)

        ax.set_yticks([0, 30, 60, 90])
        ax.set_yticklabels(["90°", "60°", "30°", "0°"], color=style["TEXT_COLOR"])
        ax.set_rlabel_position(22.5)

        cardinal_directions = {
            "N": 0,
            "E": numpy.pi / 2,
            "S": numpy.pi,
            "W": 3 * numpy.pi / 2,
        }
        for direction, angle in cardinal_directions.items():
            ax.text(
                angle,
                95,
                direction,
                ha="center",
                va="center",
                color=style["TEXT_COLOR"],
                fontsize=12,
            )

        good_condition_color = style.get(
            "GOOD_CONDITION_HL_COLOR",
            "#90EE90" if not effective_dark_mode else "#007447",
        )

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

        if plot_stars:
            _plot_stars_on_skymap(
                observation,
                ax,
                observer,
                star_magnitude_limit,
                is_polar=True,
                style=style,
                zoom_deg=zoom_deg,
                target_object=target_object,
            )
            _plot_bright_stars_on_skymap(
                observation, ax, observer, is_polar=True, style=style, zoom_deg=zoom_deg
            )
        if plot_messier:
            _plot_messier_on_skymap(
                observation,
                ax,
                observer,
                is_polar=True,
                flipped_horizontally=flipped_horizontally,
                flipped_vertically=flipped_vertically,
            )
        if plot_ngc:
            _plot_ngc_on_skymap(
                observation,
                ax,
                observer,
                is_polar=True,
                star_magnitude_limit=star_magnitude_limit,
                zoom_deg=zoom_deg,
                target_object=target_object,
                flipped_horizontally=flipped_horizontally,
                flipped_vertically=flipped_vertically,
            )
        if plot_planets:
            _plot_planets_on_skymap(
                observation,
                ax,
                observer,
                is_polar=True,
                effective_dark_mode=effective_dark_mode,
                style=style,
            )
        if plot_sun:
            _plot_sun_on_skymap(observation, ax, observer, is_polar=True, style=style)
        if plot_moon:
            _plot_moon_on_skymap(observation, ax, observer, is_polar=True, style=style)

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
    plot_sun: bool = False,
    plot_moon: bool = False,
    plot_date: Optional[datetime] = None,
    equipment_id: Optional[int] = None,
    flip_horizontally: Optional[bool] = None,
    flip_vertically: Optional[bool] = None,
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
        **kwargs,
    )


def _mark_observation(
    observation: "Observation", plot, dark_mode_enabled: bool, style: dict
):
    if plot is None:
        return
    plot.axvspan(
        observation.start,
        observation.stop,
        color=style.get(
            "SPAN_BACKGROUND_COLOR",
            "#DDDDDD" if not dark_mode_enabled else "#FFFFFF",
        ),
        alpha=0.07 if dark_mode_enabled else 0.2,
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
        alpha=0.07 if dark_mode_enabled else 0.1,
    )

    plot.axvline(observation.start, color=style["GRID_COLOR"], linestyle="--")
    plot.axvline(observation.time_limit, color=style["GRID_COLOR"], linestyle="--")


def _mark_good_conditions(
    observation: "Observation",
    plot,
    minimal,
    maximal,
    dark_mode_enabled: bool,
    style: dict,
):
    if plot is None:
        return
    plot.axhspan(
        minimal,
        maximal,
        color=style.get(
            "GOOD_CONDITION_HL_COLOR",
            "#90EE90" if not dark_mode_enabled else "#007447",
        ),
        alpha=0.1,
    )
