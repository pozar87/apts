import logging
from datetime import datetime, timedelta, timezone
from string import Template
from typing import Optional # Added Optional

import matplotlib.dates as mdates
import numpy # Retained for potential use by other functions if Observation.to_html is modified
from importlib import resources
import svgwrite as svg
from matplotlib import pyplot, lines

from .conditions import Conditions
from .objects.messier import Messier
from .objects.planets import Planets
from .utils import Utils
from .constants import ObjectTableLabels
from apts.config import get_dark_mode
from apts.constants.graphconstants import get_plot_style, get_plot_colors, OpticalType, get_planet_color # Added get_planet_color

logger = logging.getLogger(__name__)


class Observation:
    NOTIFICATION_TEMPLATE = str(
        resources.files("apts").joinpath("templates/notification.html.template")
    )

    def __init__(self, place, equipment, conditions=Conditions(), target_date=None, offset_to_sunset_minutes=0):
        self.place = place
        self.equipment = equipment
        self.conditions = conditions

        # Initialize core attributes that depend on date calculations
        self.effective_ephem_date = None
        self.start_time_for_observation_window = None
        self.stop_time_for_observation_window = None
        self.observation_local_time = None
        self.start = None
        self.stop = None
        self.time_limit = None

        if target_date:
            # New behavior: use target_date and offset
            local_dt_obs_time, ephem_dt_obs_time = self.place.get_time_relative_to_sunset(
                target_date, offset_to_sunset_minutes
            )

            if ephem_dt_obs_time is None:
                logger.warning(
                    f"Could not determine observation time for {self.place.name} "
                    f"on {target_date} with offset {offset_to_sunset_minutes} mins. "
                    "Sun may be always up or down, or another issue occurred."
                )
                # Attributes remain None, subsequent operations should handle this
            else:
                self.effective_ephem_date = ephem_dt_obs_time
                self.observation_local_time = local_dt_obs_time
                self.start_time_for_observation_window = self.place.sunset_time(target_date=target_date)
                self.stop_time_for_observation_window = self.place.sunrise_time(target_date=target_date)
        else:
            # Legacy behavior: use place.date
            self.effective_ephem_date = self.place.date
            self.start_time_for_observation_window = self.place.sunset_time()
            self.stop_time_for_observation_window = self.place.sunrise_time()
            # self.observation_local_time remains None for legacy mode

        # Normalize start and stop dates for the observation window
        if self.start_time_for_observation_window is not None and \
           self.stop_time_for_observation_window is not None:
            self.start, self.stop = self._normalize_dates(
                self.start_time_for_observation_window, self.stop_time_for_observation_window
            )
        # If not, self.start and self.stop remain None

        # Instantiate Messier and Planets objects
        self.local_messier = Messier(self.place)
        self.local_planets = Planets(self.place)

        # Compute Messier and Planets data if an effective date was determined
        if self.effective_ephem_date is not None:
            self.local_messier.compute(calculation_date=self.effective_ephem_date)
            self.local_planets.compute(calculation_date=self.effective_ephem_date)
        # Else: Objects are instantiated but not computed with a specific date.
        # Their get_visible methods should handle self.start being None.

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
                time_limit_dt if time_limit_dt > self.start else time_limit_dt + timedelta(days=1)
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

    def plot_visible_planets_svg(self, dark_mode_override: Optional[bool] = None, **args):
        if dark_mode_override is not None:
            effective_dark_mode = dark_mode_override
        else:
            effective_dark_mode = get_dark_mode()

        style = get_plot_style(effective_dark_mode)
        # colors = get_plot_colors(effective_dark_mode) # Not strictly needed as style dict has most
        default_fill_color = style['AXES_FACE_COLOR']

        visible_planets = self.get_visible_planets(**args)
        dwg = svg.Drawing(style={'background-color': style['BACKGROUND_COLOR']})
        # Set y offset to biggest planet - extract magnitude from pint.Quantity
        max_size = visible_planets[["Size"]].max().iloc[0]
        max_size_val = max_size.magnitude if hasattr(max_size, 'magnitude') else max_size
        y = int(max_size_val + 12)
        # Set x offset to constant value
        x = 20
        # Set delta to constant value
        minimal_delta = 52
        last_radius = None
        for planet in visible_planets[["Name", "Size", "Phase"]].values:
            name = planet[0]
            # Handle radius as pint.Quantity
            radius_with_units = planet[1]
            radius = radius_with_units.magnitude if hasattr(radius_with_units, 'magnitude') else radius_with_units
            # Handle phase as pint.Quantity
            phase_with_units = planet[2]
            phase = phase_with_units.magnitude if hasattr(phase_with_units, 'magnitude') else phase_with_units
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
                    stroke=style['AXIS_COLOR'],
                    stroke_width="1",
                    fill=get_planet_color(name, effective_dark_mode, default_fill_color),
                )
            )
            dwg.add(dwg.text(name, insert=(x, y + radius + 15), text_anchor="middle", fill=style['TEXT_COLOR']))
            dwg.add(
                dwg.text(phase_str + "%", insert=(x, y - radius - 4), text_anchor="middle", fill=style['TEXT_COLOR'])
            )
        return dwg.tostring()

    def plot_visible_planets(self):
        try:
            from IPython.display import SVG
        except ImportError:
            logger.warning("You can plot images only in Ipython notebook!")
            return
        return SVG(self.plot_visible_planets_svg())

    def _generate_plot_messier(self, dark_mode_override: Optional[bool] = None, **args): # Added dark_mode_override from previous step
        if dark_mode_override is not None:
            effective_dark_mode = dark_mode_override
        else:
            effective_dark_mode = get_dark_mode()

        style = get_plot_style(effective_dark_mode)
        # plot_colors = get_plot_colors(effective_dark_mode) # Messier uses specific type colors

        ax = args.pop('ax', None)
        fig = None
        if ax:
            fig = ax.figure
        else:
            fig, ax = pyplot.subplots(figsize=(18, 12), **args)

        fig.patch.set_facecolor(style['FIGURE_FACE_COLOR'])
        ax.set_facecolor(style['AXES_FACE_COLOR'])

        try:
            messier_df = self.get_visible_messier().copy()

            if len(messier_df) == 0:
                ax.set_xlim([
                    self.start - timedelta(minutes=15),
                    self.time_limit + timedelta(minutes=15),
                ])
                ax.set_ylim(0, 90)
                self._mark_observation(ax, effective_dark_mode, style)
                self._mark_good_conditions(ax, self.conditions.min_object_altitude, 90, effective_dark_mode, style)
                Utils.annotate_plot(ax, "Altitude [°]", effective_dark_mode)
                ax.set_title("Messier Objects Altitude", color=style['TEXT_COLOR'])
                logger.info("Generated empty Messier plot as no objects are visible.")
                return fig

            messier_type_colors = {
                "Galaxy": "blue", "Globular Cluster": "red", "Open Cluster": "green",
                "Nebula": "purple", "Planetary Nebula": "orange",
                "Supernova Remnant": "brown", "Other": "grey",
            }
            DARK_MESSIER_TYPE_COLORS = {
                "Galaxy": '#5A1A75',        # Bright Purple
                "Globular Cluster": '#CCCCCC', # Light Gray
                "Open Cluster": '#FFFFFF',      # White
                "Nebula": '#5A1A75',        # Bright Purple (or a different shade)
                "Planetary Nebula": '#007447',# Vibrant Green
                "Supernova Remnant": '#BBBBBB', # Muted Light Gray
                "Other": '#999999',          # Another Muted Gray
            }

            if effective_dark_mode:
                current_messier_colors = DARK_MESSIER_TYPE_COLORS
            else:
                current_messier_colors = messier_type_colors

            plotted_types = {}

            for col in [ObjectTableLabels.ALTITUDE, ObjectTableLabels.WIDTH, 'Height']:
                if col in messier_df.columns and hasattr(messier_df[col].iloc[0], 'magnitude'):
                    messier_df[col] = messier_df[col].apply(
                        lambda x: x.magnitude if hasattr(x, 'magnitude') else x
                    )

            for _, obj in messier_df.iterrows():
                transit = obj[ObjectTableLabels.TRANSIT]
                altitude = obj[ObjectTableLabels.ALTITUDE]
                obj_type = obj['Type']
                width = obj[ObjectTableLabels.WIDTH]
                height = obj['Height'] if 'Height' in obj else width
                messier_id = obj[ObjectTableLabels.MESSIER]
                marker_size = (width * height) ** 0.5
                color = current_messier_colors.get(obj_type, current_messier_colors["Other"])
                plotted_types[obj_type] = color
                ax.scatter(transit, altitude, s=marker_size**2, marker='o', c=color)
                ax.annotate(messier_id, (transit, altitude), xytext=(5, 5), textcoords="offset points", color=style['TEXT_COLOR'])

            ax.set_xlim([self.start - timedelta(minutes=15), self.time_limit + timedelta(minutes=15)])
            ax.set_ylim(0, 90)
            date_format = mdates.DateFormatter('%H:%M:%S %Z', tz=self.place.local_timezone)
            ax.xaxis.set_major_formatter(date_format)
            self._mark_observation(ax, effective_dark_mode, style)
            self._mark_good_conditions(ax, self.conditions.min_object_altitude, 90, effective_dark_mode, style)
            Utils.annotate_plot(ax, "Altitude [°]", effective_dark_mode)

            legend_handles = [
                lines.Line2D([0], [0], marker='o', color='w', label=obj_type, # 'w' background for marker for visibility
                             markerfacecolor=color, markersize=10)
                for obj_type, color in plotted_types.items()
            ]
            legend = ax.legend(handles=legend_handles, title="Object Types")
            legend.get_frame().set_facecolor(style['AXES_FACE_COLOR'])
            legend.get_frame().set_edgecolor(style['AXIS_COLOR'])
            legend.get_title().set_color(style['TEXT_COLOR'])
            for text in legend.get_texts():
                text.set_color(style['TEXT_COLOR'])

            ax.set_title("Messier Objects Altitude", color=style['TEXT_COLOR'])
            logger.info("Successfully generated Messier plot.")
            return fig

        except Exception as e:
            logger.error(f"Error generating Messier plot: {e}", exc_info=True)
            ax.clear() # Clear existing axes
            fig.patch.set_facecolor(style['FIGURE_FACE_COLOR']) # Ensure figure bg is set
            ax.set_facecolor(style['AXES_FACE_COLOR']) # Ensure axes bg is set

            error_text_color = '#FF6B6B' if effective_dark_mode else 'red'
            ax.text(0.5, 0.5, 'Error generating Messier plot.\nSee logs for details.',
                    horizontalalignment='center', verticalalignment='center',
                    fontsize=12, color=error_text_color, wrap=True, transform=ax.transAxes)
            ax.set_xticks([])
            ax.set_yticks([])
            ax.set_title("Messier Plot Error", color=style['TEXT_COLOR'])
            return fig

    def _normalize_dates(self, start, stop):
        now = datetime.now(timezone.utc).astimezone(self.place.local_timezone)
        new_start = start if start < stop else now
        new_stop = stop
        return (new_start, new_stop)

    def plot_weather(self, dark_mode_override: Optional[bool] = None, **args): # Added dark_mode_override
        logger.info(f"plot_weather called for place: {self.place.name}. Current self.place.weather is: {type(self.place.weather)}")
        if self.place.weather is None:
            logger.info("self.place.weather is None, calling self.place.get_weather()...")
            try:
                self.place.get_weather()
                logger.info(f"self.place.get_weather() called. self.place.weather is now: {type(self.place.weather)}")
                if self.place.weather is not None:
                    # Add a log for a key attribute if it exists, e.g., hourly data
                    if hasattr(self.place.weather, 'hourly') and self.place.weather.hourly is not None:
                        logger.info(f"Weather hourly data length: {len(self.place.weather.hourly.time) if hasattr(self.place.weather.hourly, 'time') else 'N/A'}")
                    else:
                        logger.info("Weather hourly data is None or not present after get_weather.")
            except Exception as e:
                logger.error(f"Error calling self.place.get_weather(): {e}", exc_info=True)
        else:
            logger.info("self.place.weather already exists, not calling get_weather().")
        return self._generate_plot_weather(dark_mode_override=dark_mode_override, **args)

    def plot_messier(self, dark_mode_override: Optional[bool] = None, **args):
        return self._generate_plot_messier(dark_mode_override=dark_mode_override, **args)

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

        ax = args.pop('ax', None)
        fig = None
        if ax:
            fig = ax.figure
        else:
            fig, ax = pyplot.subplots(figsize=(18, 12), **args)

        fig.patch.set_facecolor(style['FIGURE_FACE_COLOR'])
        ax.set_facecolor(style['AXES_FACE_COLOR'])

        planets_df = self.get_visible_planets().copy()
        if len(planets_df) == 0:
            ax.set_xlim([self.start - timedelta(minutes=15), self.time_limit + timedelta(minutes=15)])
            ax.set_ylim(0, 90)
            self._mark_observation(ax, effective_dark_mode, style)
            self._mark_good_conditions(ax, self.conditions.min_object_altitude, 90, effective_dark_mode, style)
            Utils.annotate_plot(ax, "Altitude [°]", effective_dark_mode)
            ax.set_title("Planets Altitude", color=style['TEXT_COLOR'])
            return fig

        for col in [ObjectTableLabels.ALTITUDE, ObjectTableLabels.SIZE]:
            if hasattr(planets_df[col].iloc[0], 'magnitude'):
                planets_df[col] = planets_df[col].apply(
                    lambda x: x.magnitude if hasattr(x, 'magnitude') else x
                )

        default_planet_color = plot_colors.get(OpticalType.GENERIC, '#888888')

        for _, planet in planets_df.iterrows():
            transit = planet[ObjectTableLabels.TRANSIT]
            altitude = planet[ObjectTableLabels.ALTITUDE]
            size = planet[ObjectTableLabels.SIZE]
            name = planet[ObjectTableLabels.NAME]
            marker_size = size * 0.5 + 8

            specific_planet_color = get_planet_color(name, effective_dark_mode, default_planet_color)

            logger.debug(f"Plotting planet {name} at transit {transit} with altitude {altitude} and size {size}")
            ax.scatter(transit, altitude, s=marker_size**2, marker='o', color=specific_planet_color) # Apply specific color
            ax.annotate(name, (transit, altitude), xytext=(5, 5), textcoords="offset points", color=style['TEXT_COLOR'])

        # Ensure xlim and ylim are set after plotting data if not already fixed
        # ax.set_xlim([self.start - timedelta(minutes=15), self.time_limit + timedelta(minutes=15)]) # This might be too restrictive if planets are outside this
        # ax.set_ylim(0, 90) # Altitude is usually 0-90

        self._mark_observation(ax, effective_dark_mode, style)
        self._mark_good_conditions(ax, self.conditions.min_object_altitude, 90, effective_dark_mode, style)
        Utils.annotate_plot(ax, "Altitude [°]", effective_dark_mode)
        ax.set_title("Planets Altitude", color=style['TEXT_COLOR'])

        # Simple legend if needed (e.g. if colors vary by planet type, which they don't here)
        # handles = [lines.Line2D([0], [0], marker='o', color='w', label='Planet', markerfacecolor=planet_scatter_color or 'blue', markersize=10)]
        # legend = ax.legend(handles=handles, title="Celestial Objects")
        # legend.get_frame().set_facecolor(style['AXES_FACE_COLOR'])
        # legend.get_frame().set_edgecolor(style['AXIS_COLOR'])
        # legend.get_title().set_color(style['TEXT_COLOR'])
        # for text in legend.get_texts():
        # text.set_color(style['TEXT_COLOR'])
        return fig

    def plot_planets(self, dark_mode_override: Optional[bool] = None, **args):
        return self._generate_plot_planets(dark_mode_override=dark_mode_override, **args)

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
            logger.info("is_weather_good: self.place.weather is None, calling get_weather.")
            self.place.get_weather()
        else:
            logger.info("is_weather_good: self.place.weather already exists.")
        return self._compute_weather_goodnse() > self.conditions.min_weather_goodness

    # plot_weather is a public method, add dark_mode_override
    def plot_weather(self, dark_mode_override: Optional[bool] = None, **args):
        logger.info(f"plot_weather called for place: {self.place.name}. Current self.place.weather is: {type(self.place.weather)}")
        if self.place.weather is None:
            logger.info("self.place.weather is None, calling self.place.get_weather()...")
            try:
                self.place.get_weather()
                logger.info(f"self.place.get_weather() called. self.place.weather is now: {type(self.place.weather)}")
                if self.place.weather is not None:
                    # Add a log for a key attribute if it exists, e.g., hourly data
                    if hasattr(self.place.weather, 'hourly') and self.place.weather.hourly is not None:
                        logger.info(f"Weather hourly data length: {len(self.place.weather.hourly.time) if hasattr(self.place.weather.hourly, 'time') else 'N/A'}")
                    else:
                        logger.info("Weather hourly data is None or not present after get_weather.")
            except Exception as e:
                logger.error(f"Error calling self.place.get_weather(): {e}", exc_info=True)
        else:
            logger.info("self.place.weather already exists, not calling get_weather().")
        return self._generate_plot_weather(dark_mode_override=dark_mode_override, **args)


    def to_html(self, custom_template=None, css=None):
        template_path = custom_template if custom_template else Observation.NOTIFICATION_TEMPLATE
        with open(template_path) as template_file:
            template_content = template_file.read()
            if css:
                style_end_pos = template_content.find("</style>")
                if style_end_pos != -1:
                    template_content = template_content[:style_end_pos] + css + template_content[style_end_pos:]
            template = Template(template_content)
            data = {
                "title": "APTS",
                "start": Utils.format_date(self.start),
                "stop": Utils.format_date(self.stop),
                "planets_count": len(self.get_visible_planets()),
                "messier_count": len(self.get_visible_messier()),
                "planets_table": self.get_visible_planets().to_html(),
                "messier_table": self.get_visible_messier().to_html(),
                "equipment_table": self.equipment.data().to_html(),
                "place_name": self.place.name,
                "lat": numpy.rad2deg(self.place.lat),
                "lon": numpy.rad2deg(self.place.lon),
            }
            return str(template.substitute(data))

    def _mark_observation(self, plot, dark_mode_enabled: bool, style: dict):
        if plot is None: return
        # Use dedicated span colors from the style dictionary
        plot.axvspan(self.start, self.stop, color=style.get('SPAN_BACKGROUND_COLOR', '#DDDDDD' if not dark_mode_enabled else '#FFFFFF'),
                     alpha=0.07 if dark_mode_enabled else 0.2) # Default light mode color if key missing
        moon_start, moon_stop = self._normalize_dates(self.place.moonrise_time(), self.place.moonset_time())
        plot.axvspan(moon_start, moon_stop, color=style.get('MOON_SPAN_COLOR', '#FFFFE0' if not dark_mode_enabled else '#5A1A75'),
                     alpha=0.07 if dark_mode_enabled else 0.1) # Default light mode color if key missing

        plot.axvline(self.start, color=style['GRID_COLOR'], linestyle="--")
        plot.axvline(self.time_limit, color=style['GRID_COLOR'], linestyle="--")

    def _mark_good_conditions(self, plot, minimal, maximal, dark_mode_enabled: bool, style: dict):
        if plot is None: return
        # Use dedicated good condition highlight color
        plot.axhspan(minimal, maximal, color=style.get('GOOD_CONDITION_HL_COLOR', '#90EE90' if not dark_mode_enabled else '#007447'),
                     alpha=0.1) # Default light mode color if key missing. Alpha is same for both.

    def _generate_plot_weather(self, dark_mode_override: Optional[bool] = None, **args):
        if dark_mode_override is not None:
            effective_dark_mode = dark_mode_override
        else:
            effective_dark_mode = get_dark_mode()

        style = get_plot_style(effective_dark_mode)

        logger.info(f"_generate_plot_weather called. self.place.weather type: {type(self.place.weather)}")
        if self.place.weather is None:
            logger.warning("_generate_plot_weather: self.place.weather is None. Cannot generate plots. Returning error plot.")
            fig_err, ax_err = pyplot.subplots(figsize=(10, 6))
            fig_err.patch.set_facecolor(style['FIGURE_FACE_COLOR'])
            ax_err.set_facecolor(style['AXES_FACE_COLOR'])
            warning_color = '#FFCC00' if effective_dark_mode else 'orange' # Light orange for dark mode
            ax_err.text(0.5, 0.5, 'Weather data not available for plotting.\n(self.place.weather was None)',
                        horizontalalignment='center', verticalalignment='center',
                        fontsize=12, color=warning_color, wrap=True, transform=ax_err.transAxes)
            ax_err.set_xticks([])
            ax_err.set_yticks([])
            ax_err.set_title("Weather Plot Information", color=style['TEXT_COLOR'])
            return fig_err
        try:
            axes_arg = args.pop('ax', None)
            fig = None
            axes = None

            if axes_arg is not None and isinstance(axes_arg, numpy.ndarray) and axes_arg.shape == (4, 2): # Assuming numpy is available
                axes = axes_arg
                fig = axes[0, 0].figure
                logger.debug("Using provided axes for weather plot.")
            else:
                fig, axes = pyplot.subplots(nrows=4, ncols=2, figsize=(13, 18), **args)
                logger.debug("Created new figure and axes for weather plot.")

            fig.patch.set_facecolor(style['FIGURE_FACE_COLOR'])
            # Individual subplots face colors will be handled by their respective plot_... methods in weather.py (next subtask)
            # For now, we set the overall figure background. Titles and labels within this function are not present.
            # The _mark_observation and _mark_good_conditions calls below are on plots returned by weather.py methods.
            # Those methods in weather.py will need to be dark-mode aware to correctly style their axes.

            logger.debug("Plotting clouds...")
            # The plot_clouds method itself will need to be dark_mode aware.
            # The plot_clouds method itself (and others from weather.py) will use their own dark_mode_override logic.
            # The effective_dark_mode is passed to them to ensure consistency.
            plt_clouds_ax = self.place.weather.plot_clouds(ax=axes[0, 0], dark_mode_override=effective_dark_mode)
            if plt_clouds_ax: self._mark_observation(plt_clouds_ax, effective_dark_mode, style)
            if plt_clouds_ax: self._mark_good_conditions(plt_clouds_ax, 0, self.conditions.max_clouds, effective_dark_mode, style)

            logger.debug("Plotting clouds summary...")
            self.place.weather.plot_clouds_summary(ax=axes[0, 1], dark_mode_override=effective_dark_mode)

            logger.debug("Plotting precipitation...")
            plt_precip_ax = self.place.weather.plot_precipitation(ax=axes[1, 0], dark_mode_override=effective_dark_mode)
            if plt_precip_ax: self._mark_observation(plt_precip_ax, effective_dark_mode, style)
            if plt_precip_ax: self._mark_good_conditions(plt_precip_ax, 0, self.conditions.max_precipitation_probability, effective_dark_mode, style)

            logger.debug("Plotting precipitation type summary...")
            self.place.weather.plot_precipitation_type_summary(ax=axes[1, 1], dark_mode_override=effective_dark_mode)

            logger.debug("Plotting temperature...")
            plt_temp_ax = self.place.weather.plot_temperature(ax=axes[2, 0], dark_mode_override=effective_dark_mode)
            if plt_temp_ax: self._mark_observation(plt_temp_ax, effective_dark_mode, style)
            if plt_temp_ax: self._mark_good_conditions(plt_temp_ax, self.conditions.min_temperature, self.conditions.max_temperature, effective_dark_mode, style)

            logger.debug("Plotting wind...")
            plt_wind_ax = self.place.weather.plot_wind(ax=axes[2, 1], dark_mode_override=effective_dark_mode)
            if plt_wind_ax: self._mark_observation(plt_wind_ax, effective_dark_mode, style)
            if plt_wind_ax: self._mark_good_conditions(plt_wind_ax, 0, self.conditions.max_wind, effective_dark_mode, style)

            logger.debug("Plotting pressure and ozone...")
            plt_pressure_ax = self.place.weather.plot_pressure_and_ozone(ax=axes[3, 0], dark_mode_override=effective_dark_mode)
            if plt_pressure_ax: self._mark_observation(plt_pressure_ax, effective_dark_mode, style)

            logger.debug("Plotting visibility...")
            plt_visibility_ax = self.place.weather.plot_visibility(ax=axes[3, 1], dark_mode_override=effective_dark_mode)
            if plt_visibility_ax: self._mark_observation(plt_visibility_ax, effective_dark_mode, style)

            fig.tight_layout()
            logger.info("Successfully generated Weather plot (figure setup). Sub-plot styling uses dark_mode_override.")
            return fig

        except Exception as e:
            logger.error(f"Error generating Weather plot details: {e}", exc_info=True)
            # Ensure fig is defined for closing
            current_fig = locals().get('fig', None)
            if current_fig is not None:
                try:
                    pyplot.close(current_fig)
                except Exception as close_exc:
                    logger.error(f"Error closing figure during weather plot error handling: {close_exc}")

            fig_err, ax_err = pyplot.subplots(figsize=(10, 6))
            fig_err.patch.set_facecolor(style['FIGURE_FACE_COLOR'])
            ax_err.set_facecolor(style['AXES_FACE_COLOR'])
            error_color = '#FF6B6B' if effective_dark_mode else 'red' # Light red for dark mode
            ax_err.text(0.5, 0.5, 'Error generating Weather plot details.\nSee logs for specifics.',
                        horizontalalignment='center', verticalalignment='center',
                        fontsize=12, color=error_color, wrap=True, transform=ax_err.transAxes)
            ax_err.set_xticks([])
            ax_err.set_yticks([])
            ax_err.set_title("Weather Plot Error", color=style['TEXT_COLOR'])
            return fig_err

    def __str__(self) -> str:
        return (
            f"Observation at {self.place.name} from {self.start} to {self.time_limit}"
        )
