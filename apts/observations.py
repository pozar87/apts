import logging
from datetime import datetime, timedelta, timezone
from string import Template

import matplotlib.dates as mdates
import numpy
from importlib import resources
import svgwrite as svg
from matplotlib import pyplot, lines

from .conditions import Conditions
from .objects.messier import Messier
from .objects.planets import Planets
from .utils import Utils
from .constants import ObjectTableLabels

logger = logging.getLogger(__name__)


class Observation:
    NOTIFICATION_TEMPLATE = str(
        resources.files("apts").joinpath("templates/notification.html.template")
    )

    def __init__(self, place, equipment, conditions=Conditions()):
        self.place = place
        self.equipment = equipment
        self.conditions = conditions
        self.start, self.stop = self._normalize_dates(
            place.sunset_time(), place.sunrise_time()
        )
        self.local_messier = Messier(self.place)
        self.local_planets = Planets(self.place)
        # Compute time limit
        max_return_time = [
            int(value) for value in self.conditions.max_return.split(":")
        ]
        time_limit = self.start.replace(
            hour=max_return_time[0],
            minute=max_return_time[1],
            second=max_return_time[2],
        )
        self.time_limit = (
            time_limit if time_limit > self.start else time_limit + timedelta(days=1)
        )

    def get_visible_messier(self, **args):
        return self.local_messier.get_visible(
            self.conditions, self.start, self.time_limit, **args
        )

    def get_visible_planets(self, **args):
        return self.local_planets.get_visible(
            self.conditions, self.start, self.time_limit, **args
        )

    def plot_visible_planets_svg(self, **args):
        visible_planets = self.get_visible_planets(**args)
        dwg = svg.Drawing()
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
                    stroke="black",
                    stroke_width="1",
                    fill="#e4e4e4",
                )
            )
            dwg.add(dwg.text(name, insert=(x, y + radius + 15), text_anchor="middle"))
            dwg.add(
                dwg.text(phase_str + "%", insert=(x, y - radius - 4), text_anchor="middle")
            )
        return dwg.tostring()

    def plot_visible_planets(self):
        try:
            from IPython.display import SVG
        except ImportError:
            logger.warning("You can plot images only in Ipython notebook!")
            return
        return SVG(self.plot_visible_planets_svg())

    def _generate_plot_messier(self, **args):
        # Check if an axes object is provided
        ax = args.pop('ax', None)
        fig = None
        if ax:
            fig = ax.figure # Use the figure associated with the provided axes

        # Get visible Messier objects with necessary columns
        messier_df = self.get_visible_messier().copy()

        if len(messier_df) == 0:
            # Create an empty plot if no objects are visible
            if ax is None: # Only create if ax was not provided
                fig, ax = pyplot.subplots(**args) # Pass remaining args
            ax.set_xlim([
                self.start - timedelta(minutes=15),
                self.time_limit + timedelta(minutes=15),
            ])
            ax.set_ylim(0, 90)
            self._mark_observation(ax)
            self._mark_good_conditions(ax, self.conditions.min_object_altitude, 90)
            Utils.annotate_plot(ax, "Altitude [°]")
            return fig

        # Define colors for Messier object types
        messier_type_colors = {
            "Galaxy": "blue",
            "Globular Cluster": "red",
            "Open Cluster": "green",
            "Nebula": "purple",
            "Planetary Nebula": "orange",
            "Supernova Remnant": "brown",
            "Other": "grey",  # For types not explicitly listed
        }
        plotted_types = {} # To store handles for the legend

        # Convert Pint quantities to plain values for plotting
        for col in [ObjectTableLabels.ALTITUDE, ObjectTableLabels.WIDTH, 'Height']:
            if col in messier_df.columns and hasattr(messier_df[col].iloc[0], 'magnitude'):
                messier_df[col] = messier_df[col].apply(
                    lambda x: x.magnitude if hasattr(x, 'magnitude') else x
                )

        # Create a matplotlib figure directly with increased size
        fig, ax = pyplot.subplots(figsize=(18, 12), **args)

        # Plot each Messier object individually
        for _, obj in messier_df.iterrows():
            transit = obj[ObjectTableLabels.TRANSIT]
            altitude = obj[ObjectTableLabels.ALTITUDE]
            obj_type = obj['Type'] # Use string literal for column name
            width = obj[ObjectTableLabels.WIDTH]
            height = obj['Height'] if 'Height' in obj else width  # Use width if height is not available
            messier_id = obj[ObjectTableLabels.MESSIER]

            # Calculate marker size based on object dimensions
            # Use geometric mean of width and height for a balanced measure
            marker_size = (width * height) ** 0.5

            # Get color based on object type
            color = messier_type_colors.get(obj_type, messier_type_colors["Other"])
            plotted_types[obj_type] = color # Store for legend

            # Plot the point with color
            ax.scatter(transit, altitude, s=marker_size**2, marker='o', c=color)

            # Add annotation with the Messier ID
            ax.annotate(
                messier_id,
                (transit, altitude),
                xytext=(5, 5),
                textcoords="offset points",
            )

        # Configure axes
        ax.set_xlim([
            self.start - timedelta(minutes=15),
            self.time_limit + timedelta(minutes=15),
        ])
        ax.set_ylim(0, 90)

        # Add observation markers and styling
        self._mark_observation(ax)
        self._mark_good_conditions(ax, self.conditions.min_object_altitude, 90)
        Utils.annotate_plot(ax, "Altitude [°]")

        # Add legend
        legend_handles = [
            lines.Line2D([0], [0], marker='o', color='w', label=obj_type,
                         markerfacecolor=color, markersize=10)
            for obj_type, color in plotted_types.items()
        ]
        ax.legend(handles=legend_handles, title="Object Types")

        return fig # Return the figure object

    def _normalize_dates(self, start, stop):
        now = datetime.now(timezone.utc).astimezone(self.place.local_timezone)
        new_start = start if start < stop else now
        new_stop = stop
        return (new_start, new_stop)

    def plot_weather(self, **args):
        if self.place.weather is None:
            self.place.get_weather()
        return self._generate_plot_weather(**args)

    def plot_messier(self, **args):
        return self._generate_plot_messier(**args)

    def _generate_plot_planets(self, **args):
        # Get visible planets
        planets_df = self.get_visible_planets().copy()

        if len(planets_df) == 0:
            # Create an empty plot if no planets are visible
            fig, ax = pyplot.subplots()
            ax.set_xlim([
                self.start - timedelta(minutes=15),
                self.time_limit + timedelta(minutes=15),
            ])
            ax.set_ylim(0, 90)
            self._mark_observation(ax)
            self._mark_good_conditions(ax, self.conditions.min_object_altitude, 90)
            Utils.annotate_plot(ax, "Altitude [°]")
            return fig

        # Convert Pint quantities to plain values for plotting
        # We need to convert all quantity fields to plain values first
        for col in [ObjectTableLabels.ALTITUDE, ObjectTableLabels.SIZE]:
            if hasattr(planets_df[col].iloc[0], 'magnitude'):
                planets_df[col] = planets_df[col].apply(
                    lambda x: x.magnitude if hasattr(x, 'magnitude') else x
                )

        # Create a matplotlib figure directly with increased size
        fig, ax = pyplot.subplots(figsize=(18, 12), **args)

        # Plot each planet individually
        for _, planet in planets_df.iterrows():
            transit = planet[ObjectTableLabels.TRANSIT]
            altitude = planet[ObjectTableLabels.ALTITUDE]
            size = planet[ObjectTableLabels.SIZE]
            name = planet[ObjectTableLabels.NAME]

            # Scale marker size for better visualization
            marker_size = size * 0.5 + 8

            # Plot the point
            ax.scatter(transit, altitude, s=marker_size**2, marker='o')

            # Add annotation
            ax.annotate(
                name,
                (transit, altitude),
                xytext=(5, 5),
                textcoords="offset points",
            )

        # Configure axes
        ax.set_xlim([
            self.start - timedelta(minutes=15),
            self.time_limit + timedelta(minutes=15),
        ])
        ax.set_ylim(0, 90)

        # Add observation markers and styling
        self._mark_observation(ax)
        self._mark_good_conditions(ax, self.conditions.min_object_altitude, 90)
        Utils.annotate_plot(ax, "Altitude [°]")

        return fig # Return the figure object

    def plot_planets(self, **args):
        return self._generate_plot_planets(**args)

    def _compute_weather_goodnse(self):
        # Get critical weather data
        data = self.place.weather.get_critical_data(self.start, self.stop)
        # Get only data defore time limit
        data = data[data.time <= self.time_limit]
        all_hours = len(data)
        # Get hours with good conditions
        result = data[
            (data.cloudCover < self.conditions.max_clouds)
            & (data.precipProbability < self.conditions.max_precipitation_probability)
            & (data.windSpeed < self.conditions.max_wind)
            & (data.temperature > self.conditions.min_temperature)
            & (data.temperature < self.conditions.max_temperature)
        ]
        good_hours = len(result)
        logger.debug("Good hours: {} and all hours: {}".format(good_hours, all_hours))
        # Return relative % of good hours
        if all_hours == 0:
            return 0
        return good_hours / all_hours * 100

    def is_weather_good(self):
        if self.place.weather is None:
            self.place.get_weather()
        return self._compute_weather_goodnse() > self.conditions.min_weather_goodness

    def to_html(self):
        with open(Observation.NOTIFICATION_TEMPLATE) as template_file:
            template = Template(template_file.read())
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

    def _mark_observation(self, plot):
        # Check if there is a plot
        if plot is None:
            return
        # Add marker for night
        plot.axvspan(self.start, self.stop, color="gray", alpha=0.2)
        # Add marker for moon
        moon_start, moon_stop = self._normalize_dates(
            self.place.moonrise_time(), self.place.moonset_time()
        )
        plot.axvspan(moon_start, moon_stop, color="yellow", alpha=0.1)
        # Add marker for time limit
        plot.axvline(self.start, color="orange", linestyle="--")
        plot.axvline(self.time_limit, color="orange", linestyle="--")

    def _mark_good_conditions(self, plot, minimal, maximal):
        # Check if there is a plot
        if plot is None:
            return
        plot.axhspan(minimal, maximal, color="green", alpha=0.1)

    def _generate_plot_weather(self, **args):
        fig, axes = pyplot.subplots(nrows=4, ncols=2, figsize=(13, 18))
        # Clouds
        plt = self.place.weather.plot_clouds(ax=axes[0, 0])
        self._mark_observation(plt)
        self._mark_good_conditions(plt, 0, self.conditions.max_clouds)
        # Cloud summary
        plt = self.place.weather.plot_clouds_summary(ax=axes[0, 1])
        # Precipation
        plt = self.place.weather.plot_precipitation(ax=axes[1, 0])
        self._mark_observation(plt)
        self._mark_good_conditions(
            plt, 0, self.conditions.max_precipitation_probability
        )
        # precipitation type summary
        plt = self.place.weather.plot_precipitation_type_summary(ax=axes[1, 1])
        # Temperature
        plt = self.place.weather.plot_temperature(ax=axes[2, 0])
        self._mark_observation(plt)
        self._mark_good_conditions(
            plt, self.conditions.min_temperature, self.conditions.max_temperature
        )
        # Wind
        plt = self.place.weather.plot_wind(ax=axes[2, 1])
        self._mark_observation(plt)
        self._mark_good_conditions(plt, 0, self.conditions.max_wind)
        # Pressure
        plt = self.place.weather.plot_pressure_and_ozone(ax=axes[3, 0])
        self._mark_observation(plt)
        # Visibility
        plt = self.place.weather.plot_visibility(ax=axes[3, 1])
        self._mark_observation(plt)
        fig.tight_layout()
        return fig

    def __str__(self) -> str:
        return (
            f"Observation at {self.place.name} from {self.start} to {self.time_limit}"
        )
