import logging
from datetime import datetime, timedelta, timezone
from string import Template
from typing import Optional, List  # Added Optional

import matplotlib.dates as mdates
import numpy  # Retained for potential use by other functions if Observation.to_html is modified
from importlib import resources
import svgwrite as svg
from matplotlib import pyplot, lines
from skyfield.api import utc, Star, load
from skyfield.data import hipparcos
from skyfield.projections import build_stereographic_projection

from .conditions import Conditions
from .objects.messier import Messier
from .cache import get_ephemeris
from .objects.solar_objects import SolarObjects
from .utils import Utils, planetary
from .constants import ObjectTableLabels
from apts.config import get_dark_mode
from apts.constants.graphconstants import (
    get_plot_style,
    get_plot_colors,
    OpticalType,
    get_planet_color,
)  # Added get_planet_color
from .events import AstronomicalEvents
from .constants.event_types import EventType

logger = logging.getLogger(__name__)


class Observation:
    NOTIFICATION_TEMPLATE = str(
        resources.files("apts").joinpath("templates/notification.html.template")
    )

    def __init__(
        self,
        place,
        equipment,
        conditions=Conditions(),
        target_date=None,
        offset_to_sunset_minutes=0,
        sun_observation=False,
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None,
    ):
        self.place = place
        self.equipment = equipment
        self.conditions = conditions
        self.sun_observation = sun_observation
        self.eph = get_ephemeris()

        # Initialize core attributes that depend on date calculations
        self.effective_date = None
        self.observation_local_time = None
        self.start = None
        self.stop = None
        self.time_limit = None

        if sun_observation and start_time and end_time:
            self.start = start_time
            self.stop = end_time
            self.effective_date = (
                start_time  # Use start_time as effective date for calculations
            )
            self.observation_local_time = (
                start_time  # Use start_time as local observation time
            )
        elif target_date:
            # New behavior: use target_date and offset
            event = "sunrise" if sun_observation else "sunset"
            local_dt_obs_time, dt_obs_time = self.place.get_time_relative_to_event(
                target_date, offset_to_sunset_minutes, event=event
            )

            if dt_obs_time is None:
                logger.warning(
                    f"Could not determine observation time for {self.place.name} "
                    f"on {target_date} with offset {offset_to_sunset_minutes} mins. "
                    "Sun may be always up or down, or another issue occurred."
                )
                # Attributes remain None, subsequent operations should handle this
            else:
                self.effective_date = dt_obs_time
                self.observation_local_time = local_dt_obs_time
                if sun_observation:
                    self.start = self.place.sunrise_time(target_date=target_date)
                    self.stop = self.place.sunset_time(target_date=target_date)
                else:
                    self.start = self.place.sunset_time(target_date=target_date)
                    # For night observations, the stop time is sunrise of the *next* day
                    self.stop = self.place.sunrise_time(start_search_from=self.start)
        else:
            # Legacy behavior: use place.date
            self.effective_date = self.place.date
            if sun_observation:
                self.start = self.place.sunrise_time()
                self.stop = self.place.sunset_time()
            else:
                self.start = self.place.sunset_time()
                self.stop = self.place.sunrise_time()
            # self.observation_local_time remains None for legacy mode

        # Normalize start and stop dates for the observation window
        if self.start is not None and self.stop is not None:
            self.start, self.stop = self._normalize_dates(
                self.start,
                self.stop,
            )
        # If not, self.start and self.stop remain None

        # Instantiate Messier and SolarObjects objects
        self.local_messier = Messier(self.place, calculation_date=self.effective_date)
        self.local_planets = SolarObjects(
            self.place, calculation_date=self.effective_date
        )

        # Compute time limit for observation
        if self.start is not None:
            max_return_values = [
                int(value) for value in self.conditions.max_return.split(":")
            ]
            time_limit_dt = self.start.replace(
                hour=max_return_values[0],
                minute=max_return_values[1],
                second=max_return_values[2],
            )
            # Ensure time_limit is after self.start, if it's on the same day but earlier, add a day
            self.time_limit = (
                time_limit_dt
                if time_limit_dt > self.start
                else time_limit_dt + timedelta(days=1)
            )
        # If self.start is None, self.time_limit remains None.

    def get_visible_messier(self, **args):
        return self.local_messier.get_visible(
            self.conditions, self.start, self.time_limit, **args
        )

    def get_visible_planets(self, **args):
        return self.local_planets.get_visible(
            self.conditions, self.start, self.time_limit, **args
        )

    def get_astronomical_events(
        self,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        events_to_calculate: Optional[List[EventType]] = None,
    ):
        if start_date is None:
            start_date = self.start
        if end_date is None:
            end_date = self.stop

        if start_date is None:
            start_date = datetime.now(utc)
        if end_date is None:
            end_date = start_date + timedelta(days=365)

        events = AstronomicalEvents(
            self.place, start_date, end_date, events_to_calculate=events_to_calculate
        )
        return events.get_events()

    def plot_visible_planets_svg(
        self, dark_mode_override: Optional[bool] = None, **args
    ):
        if dark_mode_override is not None:
            effective_dark_mode = dark_mode_override
        else:
            effective_dark_mode = get_dark_mode()

        style = get_plot_style(effective_dark_mode)
        # colors = get_plot_colors(effective_dark_mode) # Not strictly needed as style dict has most
        default_fill_color = style["AXES_FACE_COLOR"]

        visible_planets = self.get_visible_planets(**args)
        dwg = svg.Drawing(style={"background-color": style["BACKGROUND_COLOR"]})
        # Set y offset to biggest planet - extract magnitude from pint.Quantity
        max_size = (
            visible_planets[["Size"]].max().iloc[0]
            if not visible_planets.empty
            else 0
        )
        max_size_val = (
            max_size.magnitude if hasattr(max_size, "magnitude") else max_size
        )
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

    def plot_visible_planets(self):
        try:
            from IPython.display import SVG
        except ImportError:
            logger.warning("You can plot images only in Ipython notebook!")
            return
        return SVG(self.plot_visible_planets_svg())

    def _generate_plot_messier(
        self, dark_mode_override: Optional[bool] = None, **args
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
            messier_df = self.get_visible_messier().copy()

            if len(messier_df) == 0:
                ax.set_xlim(
                    [
                        self.start - timedelta(minutes=15),
                        self.time_limit + timedelta(minutes=15),
                    ]
                )
                ax.set_ylim(0, 90)
                self._mark_observation(ax, effective_dark_mode, style)
                self._mark_good_conditions(
                    ax,
                    self.conditions.min_object_altitude,
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

            ax.set_xlim(
                [
                    self.start - timedelta(minutes=15),
                    self.time_limit + timedelta(minutes=15),
                ]
            )
            ax.set_ylim(0, 90)
            date_format = mdates.DateFormatter(
                "%H:%M:%S %Z", tz=self.place.local_timezone
            )
            ax.xaxis.set_major_formatter(date_format)
            self._mark_observation(ax, effective_dark_mode, style)
            self._mark_good_conditions(
                ax, self.conditions.min_object_altitude, 90, effective_dark_mode, style
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

    def _normalize_dates(self, start, stop):
        # If the stop time is earlier than the start time, it means the observation
        # spans across midnight, so we add one day to the stop time.
        if stop < start:
            stop += timedelta(days=1)
        return (start, stop)

    def plot_weather(
        self, dark_mode_override: Optional[bool] = None, **args
    ):  # Added dark_mode_override
        logger.info(
            f"plot_weather called for place: {self.place.name}. Current self.place.weather is: {type(self.place.weather)}"
        )
        if self.place.weather is None:
            logger.info(
                "self.place.weather is None, calling self.place.get_weather()..."
            )
            try:
                self.place.get_weather()
                logger.info(
                    f"self.place.get_weather() called. self.place.weather is now: {type(self.place.weather)}"
                )
                if self.place.weather is not None:
                    # Add a log for a key attribute if it exists, e.g., hourly data
                    if (
                        hasattr(self.place.weather, "hourly")
                        and self.place.weather.hourly is not None
                    ):
                        logger.info(
                            f"Weather hourly data length: {len(self.place.weather.hourly.time) if hasattr(self.place.weather.hourly, 'time') else 'N/A'}"
                        )
                    else:
                        logger.info(
                            "Weather hourly data is None or not present after get_weather."
                        )
            except Exception as e:
                logger.error(
                    f"Error calling self.place.get_weather(): {e}", exc_info=True
                )
        else:
            logger.info("self.place.weather already exists, not calling get_weather().")
        return self._generate_plot_weather(
            dark_mode_override=dark_mode_override, **args
        )

    def plot_messier(self, dark_mode_override: Optional[bool] = None, **args):
        return self._generate_plot_messier(
            dark_mode_override=dark_mode_override, **args
        )

    # Note: _generate_plot_messier already updated in a previous step to have dark_mode_override
    # For this step, we just ensure its signature is correct if it wasn't.
    # The actual use of dark_mode_override is in the next step.
    # def _generate_plot_messier(self, dark_mode_override: Optional[bool] = None, **args):
    # existing body ...

    def _generate_plot_planets(self, dark_mode_override: Optional[bool] = None, **args):
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

        planets_df = self.get_visible_planets().copy()
        if len(planets_df) == 0:
            ax.set_xlim(
                [
                    self.start - timedelta(minutes=15),
                    self.time_limit + timedelta(minutes=15),
                ]
            )
            ax.set_ylim(0, 90)
            self._mark_observation(ax, effective_dark_mode, style)
            self._mark_good_conditions(
                ax, self.conditions.min_object_altitude, 90, effective_dark_mode, style
            )
            Utils.annotate_plot(ax, "Altitude [°]", effective_dark_mode)
            ax.set_title("Solar Objects Altitude", color=style["TEXT_COLOR"])
            return fig

        default_planet_color = plot_colors.get(OpticalType.GENERIC, "#888888")

        for _, planet in planets_df.iterrows():
            name = planet[ObjectTableLabels.NAME]
            skyfield_object = self.local_planets.get_skyfield_object(planet)

            curve_df = self.place.get_altitude_curve(skyfield_object, self.start, self.stop)

            specific_planet_color = get_planet_color(
                name, effective_dark_mode, default_planet_color
            )

            # Plot altitude curve
            ax.plot(
                curve_df["Time"].apply(lambda t: t.utc_datetime()),
                curve_df["Altitude"],
                color=specific_planet_color,
                label=name
            )

            # Mark rise and set times
            if planet[ObjectTableLabels.RISING] is not None:
                ax.scatter(planet[ObjectTableLabels.RISING], 0, marker='^', color=specific_planet_color, s=100)
            if planet[ObjectTableLabels.SETTING] is not None:
                ax.scatter(planet[ObjectTableLabels.SETTING], 0, marker='v', color=specific_planet_color, s=100)

            # Annotate planet name
            # Find a good position for the annotation, e.g., at the peak of the curve
            peak_idx = curve_df["Altitude"].idxmax()
            peak_time = curve_df["Time"][peak_idx].utc_datetime()
            peak_alt = curve_df["Altitude"][peak_idx]
            ax.annotate(
                name,
                (peak_time, peak_alt),
                xytext=(5, 5),
                textcoords="offset points",
                color=style["TEXT_COLOR"],
            )

        ax.set_xlim([self.start, self.stop])
        ax.set_ylim(0, 90)
        date_format = mdates.DateFormatter("%H:%M", tz=self.place.local_timezone)
        ax.xaxis.set_major_formatter(date_format)

        self._mark_observation(ax, effective_dark_mode, style)
        self._mark_good_conditions(
            ax, self.conditions.min_object_altitude, 90, effective_dark_mode, style
        )
        Utils.annotate_plot(ax, "Altitude [°]", effective_dark_mode)
        ax.set_title("Solar Objects Altitude", color=style["TEXT_COLOR"])
        ax.legend()

        return fig

    def plot_planets(self, dark_mode_override: Optional[bool] = None, **args):
        return self._generate_plot_planets(
            dark_mode_override=dark_mode_override, **args
        )

    def _compute_weather_goodnse(self):
        data = self.place.weather.get_critical_data(self.start, self.stop)
        data = data[data.time <= self.time_limit]
        all_hours = len(data)
        result = data[
            (data.cloudCover < self.conditions.max_clouds)
            & (data.precipProbability < self.conditions.max_precipitation_probability)
            & (data.windSpeed < self.conditions.max_wind)
            & (data.temperature > self.conditions.min_temperature)
            & (data.temperature < self.conditions.max_temperature)
        ]
        good_hours = len(result)
        logger.debug("Good hours: {} and all hours: {}".format(good_hours, all_hours))
        if all_hours == 0:
            return 0
        return good_hours / all_hours * 100

    def is_weather_good(self):
        if self.place.weather is None:
            logger.info(
                "is_weather_good: self.place.weather is None, calling get_weather."
            )
            self.place.get_weather()
        else:
            logger.info("is_weather_good: self.place.weather already exists.")
        return self._compute_weather_goodnse() > self.conditions.min_weather_goodness

    # plot_weather is a public method, add dark_mode_override
    def plot_weather(self, dark_mode_override: Optional[bool] = None, **args):
        logger.info(
            f"plot_weather called for place: {self.place.name}. Current self.place.weather is: {type(self.place.weather)}"
        )
        if self.place.weather is None:
            logger.info(
                "self.place.weather is None, calling self.place.get_weather()..."
            )
            try:
                self.place.get_weather()
                logger.info(
                    f"self.place.get_weather() called. self.place.weather is now: {type(self.place.weather)}"
                )
                if self.place.weather is not None:
                    # Add a log for a key attribute if it exists, e.g., hourly data
                    if (
                        hasattr(self.place.weather, "hourly")
                        and self.place.weather.hourly is not None
                    ):
                        logger.info(
                            f"Weather hourly data length: {len(self.place.weather.hourly.time) if hasattr(self.place.weather.hourly, 'time') else 'N/A'}"
                        )
                    else:
                        logger.info(
                            "Weather hourly data is None or not present after get_weather."
                        )
            except Exception as e:
                logger.error(
                    f"Error calling self.place.get_weather(): {e}", exc_info=True
                )
        else:
            logger.info("self.place.weather already exists, not calling get_weather().")
        return self._generate_plot_weather(
            dark_mode_override=dark_mode_override, **args
        )

    def to_html(self, custom_template=None, css=None):
        template_path = (
            custom_template if custom_template else Observation.NOTIFICATION_TEMPLATE
        )
        with open(template_path) as template_file:
            template_content = template_file.read()
            if css:
                style_end_pos = template_content.find("</style>")
                if style_end_pos != -1:
                    template_content = (
                        template_content[:style_end_pos]
                        + css
                        + template_content[style_end_pos:]
                    )
            template = Template(template_content)
            hourly_weather = self.get_hourly_weather_analysis()
            visible_planets_df = self.get_visible_planets()

            data = {
                "title": "APTS",
                "start": Utils.format_date(self.start),
                "stop": Utils.format_date(self.stop),
                "planets_count": len(visible_planets_df),
                "messier_count": len(self.get_visible_messier()),
                "planets_table": visible_planets_df.drop(columns=["TechnicalName"]).to_html() if "TechnicalName" in visible_planets_df.columns else visible_planets_df.to_html(),
                "messier_table": self.get_visible_messier().to_html(),
                "equipment_table": self.equipment.data().to_html(),
                "place_name": self.place.name,
                "lat": numpy.rad2deg(self.place.lat),
                "lon": numpy.rad2deg(self.place.lon),
                "hourly_weather": hourly_weather,
                "timezone": self.place.local_timezone,
            }
            return str(template.substitute(data))

    def _mark_observation(self, plot, dark_mode_enabled: bool, style: dict):
        if plot is None:
            return
        # Use dedicated span colors from the style dictionary
        plot.axvspan(
            self.start,
            self.stop,
            color=style.get(
                "SPAN_BACKGROUND_COLOR",
                "#DDDDDD" if not dark_mode_enabled else "#FFFFFF",
            ),
            alpha=0.07 if dark_mode_enabled else 0.2,
        )  # Default light mode color if key missing
        moon_start, moon_stop = self._normalize_dates(
            self.place.moonrise_time(), self.place.moonset_time()
        )
        plot.axvspan(
            moon_start,
            moon_stop,
            color=style.get(
                "MOON_SPAN_COLOR", "#FFFFE0" if not dark_mode_enabled else "#5A1A75"
            ),
            alpha=0.07 if dark_mode_enabled else 0.1,
        )  # Default light mode color if key missing

        plot.axvline(self.start, color=style["GRID_COLOR"], linestyle="--")
        plot.axvline(self.time_limit, color=style["GRID_COLOR"], linestyle="--")

    def _mark_good_conditions(
        self, plot, minimal, maximal, dark_mode_enabled: bool, style: dict
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
            alpha=0.1,
        )  # Default light mode color if key missing. Alpha is same for both.

    def _generate_plot_weather(self, dark_mode_override: Optional[bool] = None, **args):
        if dark_mode_override is not None:
            effective_dark_mode = dark_mode_override
        else:
            effective_dark_mode = get_dark_mode()

        style = get_plot_style(effective_dark_mode)

        logger.info(
            f"_generate_plot_weather called. self.place.weather type: {type(self.place.weather)}"
        )
        if self.place.weather is None:
            logger.warning(
                "_generate_plot_weather: self.place.weather is None. Cannot generate plots. Returning error plot."
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
                "Weather data not available for plotting.\n(self.place.weather was None)",
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
                and axes_arg.shape == (4, 2)
            ):  # Assuming numpy is available
                axes = axes_arg
                fig = axes[0, 0].figure
                logger.debug("Using provided axes for weather plot.")
            else:
                fig, axes = pyplot.subplots(nrows=4, ncols=2, figsize=(13, 18), **args)
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
            plt_clouds_ax = self.place.weather.plot_clouds(
                ax=axes[0, 0], dark_mode_override=effective_dark_mode
            )
            if plt_clouds_ax:
                self._mark_observation(plt_clouds_ax, effective_dark_mode, style)
            if plt_clouds_ax:
                self._mark_good_conditions(
                    plt_clouds_ax,
                    0,
                    self.conditions.max_clouds,
                    effective_dark_mode,
                    style,
                )

            logger.debug("Plotting clouds summary...")
            self.place.weather.plot_clouds_summary(
                ax=axes[0, 1], dark_mode_override=effective_dark_mode
            )

            logger.debug("Plotting precipitation...")
            plt_precip_ax = self.place.weather.plot_precipitation(
                ax=axes[1, 0], dark_mode_override=effective_dark_mode
            )
            if plt_precip_ax:
                self._mark_observation(plt_precip_ax, effective_dark_mode, style)
            if plt_precip_ax:
                self._mark_good_conditions(
                    plt_precip_ax,
                    0,
                    self.conditions.max_precipitation_probability,
                    effective_dark_mode,
                    style,
                )

            logger.debug("Plotting precipitation type summary...")
            self.place.weather.plot_precipitation_type_summary(
                ax=axes[1, 1], dark_mode_override=effective_dark_mode
            )

            logger.debug("Plotting temperature...")
            plt_temp_ax = self.place.weather.plot_temperature(
                ax=axes[2, 0], dark_mode_override=effective_dark_mode
            )
            if plt_temp_ax:
                self._mark_observation(plt_temp_ax, effective_dark_mode, style)
            if plt_temp_ax:
                self._mark_good_conditions(
                    plt_temp_ax,
                    self.conditions.min_temperature,
                    self.conditions.max_temperature,
                    effective_dark_mode,
                    style,
                )

            logger.debug("Plotting wind...")
            plt_wind_ax = self.place.weather.plot_wind(
                ax=axes[2, 1], dark_mode_override=effective_dark_mode
            )
            if plt_wind_ax:
                self._mark_observation(plt_wind_ax, effective_dark_mode, style)
            if plt_wind_ax:
                self._mark_good_conditions(
                    plt_wind_ax, 0, self.conditions.max_wind, effective_dark_mode, style
                )

            logger.debug("Plotting pressure and ozone...")
            plt_pressure_ax = self.place.weather.plot_pressure_and_ozone(
                ax=axes[3, 0], dark_mode_override=effective_dark_mode
            )
            if plt_pressure_ax:
                self._mark_observation(plt_pressure_ax, effective_dark_mode, style)

            logger.debug("Plotting visibility...")
            plt_visibility_ax = self.place.weather.plot_visibility(
                ax=axes[3, 1], dark_mode_override=effective_dark_mode
            )
            if plt_visibility_ax:
                self._mark_observation(plt_visibility_ax, effective_dark_mode, style)

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

    def plot_sun_and_moon_path(self, dark_mode_override: Optional[bool] = None, **args):
        if self.sun_observation:
            return self.place.plot_sun_path(dark_mode_override, **args)
        else:
            return self.place.plot_moon_path(dark_mode_override, **args)

    def plot_skymap(self, target_name: str, dark_mode_override: Optional[bool] = None, **args):
        return self._generate_plot_skymap(
            target_name=target_name, dark_mode_override=dark_mode_override, **args
        )

    def _generate_plot_skymap(self, target_name: str, dark_mode_override: Optional[bool] = None, **args):
        if dark_mode_override is not None:
            effective_dark_mode = dark_mode_override
        else:
            effective_dark_mode = get_dark_mode()

        style = get_plot_style(effective_dark_mode)
        # plot_colors = get_plot_colors(effective_dark_mode)

        ax = args.pop("ax", None)
        fig = None
        if ax:
            fig = ax.figure
        else:
            fig, ax = pyplot.subplots(figsize=(12, 12), **args)

        fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
        ax.set_facecolor(style["AXES_FACE_COLOR"])

        # Load star data
        with load.open(hipparcos.URL) as f:
            stars = hipparcos.load_dataframe(f)

        # Observer
        ts = load.timescale()
        observer = self.place.location.at(ts.from_datetime(self.effective_date.astimezone(utc)))

        # Center of projection
        target_object = None

        # Try to find in Messier catalog
        messier_obj = self.local_messier.get_by_name(target_name)
        if messier_obj is not None:
            target_object = Star(ra_hours=messier_obj['RA'], dec_degrees=messier_obj['Dec'])

        # Try to find in solar system objects
        if target_object is None:
            try:
                planet_obj = self.local_planets.get_skyfield_object_by_name(target_name)
                if planet_obj:
                    target_object = planet_obj
            except ValueError:
                pass # Object not found

        if target_object is None:
            logger.error(f"Could not find an object named '{target_name}'")
            ax.text(0.5, 0.5, f"Object '{target_name}' not found.",
                    horizontalalignment='center', verticalalignment='center',
                    transform=ax.transAxes, color=style.get("TEXT_COLOR", "red"))
            return fig

        center = observer.observe(target_object)
        projection = build_stereographic_projection(center)

        # Project stars
        star_positions = observer.observe(Star.from_dataframe(stars))
        stars['x'], stars['y'] = projection(star_positions)

        # Plotting
        chart_size = 10
        max_star_size = 100
        limiting_magnitude = 6.0  # Common limit for naked eye

        bright_stars = (stars.magnitude <= limiting_magnitude)
        magnitude = stars['magnitude'][bright_stars]

        marker_size = max_star_size * 10 ** (magnitude / -2.5)

        ax.scatter(stars['x'][bright_stars], stars['y'][bright_stars],
                   s=marker_size, color=style.get("TEXT_COLOR", "white"), marker='.', linewidths=0, zorder=2)

        # Plot target object
        target_x, target_y = projection(observer.observe(target_object))
        ax.scatter(target_x, target_y, s=200, color='red', marker='+', zorder=3)
        ax.annotate(target_name, (target_x, target_y), textcoords="offset points", xytext=(0,10), ha='center', color='red')

        # Set limits and hide axes
        limit = 1.0
        ax.set_xlim(-limit, limit)
        ax.set_ylim(-limit, limit)
        ax.axis('off')

        # Draw a circle for the horizon
        border = pyplot.Circle((0, 0), limit, color=style.get("GRID_COLOR", "grey"), fill=False)
        ax.add_patch(border)
        ax.set_aspect('equal', 'box')

        ax.set_title(f"Skymap centered on {target_name}", color=style["TEXT_COLOR"])
        return fig

    def __str__(self) -> str:
        return (
            f"Observation at {self.place.name} from {self.start} to {self.time_limit}"
        )

    def get_hourly_weather_analysis(self):
        if self.place.weather is None:
            logger.info(
                "get_hourly_weather_analysis: self.place.weather is None, calling get_weather."
            )
            self.place.get_weather()
            if self.place.weather is None:  # Still None after trying to fetch
                logger.warning(
                    "get_hourly_weather_analysis: Weather data unavailable after fetch attempt."
                )
                return []  # Return empty list

        # Ensure start, stop, and time_limit are valid
        if not all([self.start, self.stop, self.time_limit]):
            logger.warning(
                "get_hourly_weather_analysis: Observation window (start, stop, time_limit) is not fully defined."
            )
            return []

        hourly_data = self.place.weather.get_critical_data(self.start, self.stop)
        # Filter data further by self.time_limit
        # The time_limit is the exclusive end point for the observation window.
        hourly_data = hourly_data[hourly_data.time <= self.time_limit]
        logger.debug(
            f"[Observation.get_hourly_weather_analysis] Filtered hourly_data time range: {hourly_data.time.min()} to {hourly_data.time.max()}"
        )

        analysis_results = []

        for index, row in hourly_data.iterrows():
            current_time = row.time
            is_good_hour = True
            reasons = []

            # Check cloud cover
            if not (row.cloudCover < self.conditions.max_clouds):
                is_good_hour = False
                reasons.append(
                    f"Cloud cover {row.cloudCover:.1f}% exceeds limit {self.conditions.max_clouds:.1f}%"
                )

            # Check precipitation probability
            if not (
                row.precipProbability < self.conditions.max_precipitation_probability
            ):
                is_good_hour = False
                reasons.append(
                    f"Precipitation probability {row.precipProbability:.1f}% exceeds limit {self.conditions.max_precipitation_probability:.1f}%"
                )

            # Check wind speed
            if not (row.windSpeed < self.conditions.max_wind):
                is_good_hour = False
                reasons.append(
                    f"Wind speed {row.windSpeed:.1f} km/h exceeds limit {self.conditions.max_wind:.1f} km/h"
                )

            # Check temperature (min)
            if not (row.temperature > self.conditions.min_temperature):
                is_good_hour = False
                reasons.append(
                    f"Temperature {row.temperature:.1f}°C below limit {self.conditions.min_temperature:.1f}°C"
                )

            # Check temperature (max)
            if not (row.temperature < self.conditions.max_temperature):
                is_good_hour = False
                reasons.append(
                    f"Temperature {row.temperature:.1f}°C exceeds limit {self.conditions.max_temperature:.1f}°C"
                )

            analysis_results.append(
                {
                    "time": current_time,
                    "is_good_hour": is_good_hour,
                    "reasons": reasons,
                    "temperature": row.temperature,
                    "clouds": row.cloudCover,
                    "precipitation": row.precipProbability,
                    "wind_speed": row.windSpeed,
                }
            )

        return analysis_results
