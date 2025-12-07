import datetime
import logging
from importlib import resources
from math import copysign as copysign
from math import radians as rad
from typing import Optional

import matplotlib.font_manager as font_manager
import pandas as pd
import numpy as np
import pytz
from dateutil import tz
from skyfield import almanac
from skyfield.api import Topos, load
from timezonefinder import TimezoneFinder

from apts.config import get_dark_mode
from apts.constants.graphconstants import get_plot_style
from apts.constants.twilight import Twilight
from apts.i18n import gettext_
from apts.light_pollution import LightPollution
from apts.utils.plot import Utils

from .utils.planetary import get_moon_illumination
from .weather import Weather

logger = logging.getLogger(__name__)


class Place:
    MOON_FONT = font_manager.FontProperties(
        fname=str(resources.files("apts").joinpath("data/moon_phases.ttf")), size=50
    )
    TF = TimezoneFinder()

    def __init__(
        self,
        lat,
        lon,
        name="",
        elevation=300,
        date=datetime.datetime.now(datetime.UTC),
    ):
        self.ts = load.timescale()
        self.eph = load("de421.bsp")
        if isinstance(date, type(self.ts.now())):
            self.date = date
        else:
            self.date = self.ts.utc(date)
        self.lat = rad(lat)
        self.lon = rad(lon)
        self.lat_decimal = lat
        self.lon_decimal = lon
        self.name = name
        self.elevation = elevation
        self.location = Topos(
            latitude_degrees=lat, longitude_degrees=lon, elevation_m=elevation
        )
        self.observer = self.eph["earth"] + self.location
        # Sun
        self.sun = self.eph["sun"]
        # Moon
        self.moon = self.eph["moon"]
        self.local_timezone = tz.gettz(
            Place.TF.timezone_at(lat=self.lat_decimal, lng=self.lon_decimal)
        )
        self.weather = None
        self.light_pollution = None
        logger.debug(f"Place {self.name} initialized, timezone: {self.local_timezone}")

    def get_light_pollution(self):
        self.light_pollution = LightPollution(
            self.lat_decimal,
            self.lon_decimal,
        )
        return self.light_pollution.get_light_pollution()

    def get_weather(self, provider_name: Optional[str] = None):
        self.weather = Weather(
            self.lat_decimal,
            self.lon_decimal,
            self.local_timezone,
            provider_name=provider_name,
        )

    def _next_setting_time(self, obj, start):
        t0 = self.ts.utc(start)
        t1 = self.ts.utc(start + datetime.timedelta(days=2))
        f = almanac.risings_and_settings(self.eph, obj, self.location)
        t, y = almanac.find_discrete(t0, t1, f)

        for ti, yi in zip(t, y):
            if yi == 0:  # Setting
                return (
                    ti.utc_datetime()
                    .replace(tzinfo=pytz.UTC)
                    .astimezone(self.local_timezone)
                )
        return None

    def _next_rising_time(self, obj, start):
        t0 = self.ts.utc(start)
        t1 = self.ts.utc(start + datetime.timedelta(days=2))
        f = almanac.risings_and_settings(self.eph, obj, self.location)
        t, y = almanac.find_discrete(t0, t1, f)

        for ti, yi in zip(t, y):
            if yi == 1:  # Rising
                return (
                    ti.utc_datetime()
                    .replace(tzinfo=pytz.UTC)
                    .astimezone(self.local_timezone)
                )
        return None

    def _get_start_date(self, target_date, start_search_from):
        if start_search_from:
            return start_search_from
        elif target_date:
            local_start_of_day = datetime.datetime.combine(
                target_date, datetime.time.min
            ).replace(tzinfo=self.local_timezone)
            return local_start_of_day.astimezone(datetime.timezone.utc)
        else:
            return self.date.utc_datetime()

    def _get_twilight_time(self, start_date, twilight: Twilight, event: str):
        t0 = self.ts.utc(start_date)
        t1 = self.ts.utc(start_date + datetime.timedelta(days=2))

        f = almanac.dark_twilight_day(self.eph, self.location)
        times, events = almanac.find_discrete(t0, t1, f)

        # Define transitions for evening (set) and morning (rise)
        if event == "set":  # Evening: getting darker
            transitions = {
                Twilight.CIVIL: (4, 3),  # Day -> Civil
                Twilight.NAUTICAL: (3, 2),  # Civil -> Nautical
                Twilight.ASTRONOMICAL: (2, 1),  # Nautical -> Astronomical
            }
        else:  # Morning: getting lighter
            transitions = {
                Twilight.ASTRONOMICAL: (0, 1),  # Night -> Astronomical
                Twilight.NAUTICAL: (1, 2),  # Astronomical -> Nautical
                Twilight.CIVIL: (2, 3),  # Nautical -> Civil
            }

        prev_event, next_event = transitions.get(twilight)

        # The first event is the state at t0
        previous_y = f(t0)
        for t, y in zip(times, events):
            if previous_y == prev_event and y == next_event:
                return (
                    t.utc_datetime()
                    .replace(tzinfo=pytz.UTC)
                    .astimezone(self.local_timezone)
                )
            previous_y = y

        return None

    def sunset_time(
        self,
        target_date=None,
        start_search_from: Optional[datetime.datetime] = None,
        twilight: Optional[Twilight] = None,
    ):
        start_date = self._get_start_date(target_date, start_search_from)
        if twilight:
            return self._get_twilight_time(start_date, twilight, "set")
        return self._next_setting_time(self.sun, start=start_date)

    def sunrise_time(
        self,
        target_date=None,
        start_search_from: Optional[datetime.datetime] = None,
        twilight: Optional[Twilight] = None,
    ):
        start_date = self._get_start_date(target_date, start_search_from)
        if twilight:
            return self._get_twilight_time(start_date, twilight, "rise")
        return self._next_rising_time(self.sun, start=start_date)

    def moonset_time(self):
        return self._next_setting_time(self.moon, start=self.date.utc_datetime())

    def moonrise_time(self):
        return self._next_rising_time(self.moon, start=self.date.utc_datetime())

    def _moon_phase_letter(self):
        moon_phase_angle = almanac.moon_phase(self.eph, self.date).degrees
        lunation = moon_phase_angle / 360.0
        letter = chr(ord("A") + int(round(lunation * 26)))
        return letter

    def moon_illumination(self):
        return get_moon_illumination(self.date)

    def get_altaz_curve(self, skyfield_object, start_time, end_time, num_points=100):
        t0 = self.ts.utc(start_time)
        t1 = self.ts.utc(end_time)
        times = self.ts.linspace(t0, t1, num_points)

        alt, az, _ = self.observer.at(times).observe(skyfield_object).apparent().altaz()

        time_list = [t for t in times]

        df = pd.DataFrame(
            {"Time": time_list, "Altitude": alt.degrees, "Azimuth": az.degrees}
        )

        # For Southern Hemisphere, the transit is North (0/360 degrees).
        # If the path crosses this point, matplotlib will draw a line across the plot.
        # To prevent this, we find the wrap-around point and insert a NaN row.
        if self.lat_decimal < 0:
            diffs = df["Azimuth"].diff()
            # A wrap-around is a large jump, positive or negative
            wrap_around_indices = diffs[diffs.abs() > 180].index
            if not wrap_around_indices.empty:
                # Create a new row with NaN values to break the line plot
                nan_row = pd.DataFrame(
                    {
                        "Time": [pd.NaT],
                        "Altitude": [np.nan],
                        "Azimuth": [np.nan],
                    },
                    index=[wrap_around_indices[0] - 0.5],
                )
                df = pd.concat([df, nan_row]).sort_index().reset_index(drop=True)

        df["Local_time"] = [
            t.utc_datetime().astimezone(self.local_timezone).strftime("%H:%M")
            if hasattr(t, "utc_datetime")
            else ""
            for t in df["Time"]
        ]
        return df

    def moon_path(self):
        start_time = self.date.utc_datetime().replace(
            hour=0, minute=0, second=0, microsecond=0
        )
        end_time = start_time + datetime.timedelta(days=1)
        df = self.get_altaz_curve(self.moon, start_time, end_time, num_points=26 * 4)
        df = df.rename(columns={"Altitude": "Moon altitude"})

        phases = []
        lunations = []
        for t in df["Time"]:
            if hasattr(t, "utc_datetime"):
                moon_phase_angle = almanac.moon_phase(self.eph, t)
                phases.append((moon_phase_angle.degrees / 360.0) * 100)
                lunations.append(moon_phase_angle.degrees / 360.0)
            else:
                phases.append(pd.NA)
                lunations.append(pd.NA)

        df["Phase"] = phases
        df["Lunation"] = lunations
        df["Time"] = [
            x.utc_datetime().time() if hasattr(x, "utc_datetime") else pd.NaT
            for x in df["Time"]
        ]
        return df

    def sun_path(self):
        start_time = self.date.utc_datetime().replace(
            hour=0, minute=0, second=0, microsecond=0
        )
        end_time = start_time + datetime.timedelta(days=1)
        df = self.get_altaz_curve(self.sun, start_time, end_time, num_points=26 * 4)
        df = df.rename(columns={"Altitude": "Sun altitude"})
        df["Time"] = [
            x.utc_datetime().time() if hasattr(x, "utc_datetime") else pd.NaT
            for x in df["Time"]
        ]
        return df

    def plot_sun_path(self, dark_mode_override: Optional[bool] = None, **args):
        if dark_mode_override is not None:
            effective_dark_mode = dark_mode_override
        else:
            effective_dark_mode = get_dark_mode()

        style = get_plot_style(effective_dark_mode)

        def add_marker(
            ax, label, position, text_color, grid_color
        ):  # Pass ax and colors
            ax.axvline(position, color=grid_color, linestyle="--", linewidth=1)
            ax.text(
                position,
                1,
                label,
                weight="bold",
                horizontalalignment="center",
                color=text_color,
            )

        data = self.sun_path()
        if self.lat_decimal < 0:
            data["Azimuth"] = (data["Azimuth"] + 180) % 360 - 180

        passed_ax = args.pop("ax", None)  # Renamed to avoid confusion

        plot_kwargs = {
            "x": "Azimuth",
            "y": "Sun altitude",
            "title": "Sun altitude",  # This title is styled later by direct ax.set_title
            "style": ".-",
            **args,  # Pass through any other user-supplied keyword arguments
        }

        if passed_ax is not None:
            plot_kwargs["ax"] = passed_ax  # Add 'ax' to kwargs only if it was provided
            data.plot(**plot_kwargs)  # Plot on the provided ax
            ax = passed_ax  # Use the axes that was passed in
            fig = ax.figure  # Get figure from provided ax
        else:
            ax = data.plot(**plot_kwargs)  # Let pandas create a new ax and figure
            fig = ax.figure  # Get figure from newly created ax

        fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
        ax.set_facecolor(style["AXES_FACE_COLOR"])

        if ax.lines:  # Style the main moon path line
            ax.lines[0].set_color(style["TEXT_COLOR"])

        ax.set_title(
            gettext_("Sun Path on {date}").format(
                date=self.date.utc_datetime().strftime("%Y-%m-%d")
            ),
            color=style["TEXT_COLOR"],
        )

        # Add cardinal direction and set x-axis limits based on hemisphere
        if self.lat_decimal < 0:  # Southern Hemisphere
            add_marker(ax, "W", -90, style["TEXT_COLOR"], style["GRID_COLOR"])
            add_marker(ax, "N", 0, style["TEXT_COLOR"], style["GRID_COLOR"])
            add_marker(ax, "E", 90, style["TEXT_COLOR"], style["GRID_COLOR"])
            ax.set_xlim(135, -135)  # Inverted for South-up view, SE to SW
        else:  # Northern Hemisphere
            add_marker(ax, "E", 90, style["TEXT_COLOR"], style["GRID_COLOR"])
            add_marker(ax, "S", 180, style["TEXT_COLOR"], style["GRID_COLOR"])
            add_marker(ax, "W", 270, style["TEXT_COLOR"], style["GRID_COLOR"])
            ax.set_xlim(45, 315)

        Utils.annotate_plot(
            ax,
            gettext_("Altitude [°]"),
            effective_dark_mode,
            self.local_timezone,
            x_label=gettext_("Azimuth [°]"),
        )

        # Plot horizon
        ax.axhspan(0, -50, color=style["GRID_COLOR"], alpha=0.3)
        ax.locator_params(nbins=20)
        ax.set_ylim(bottom=-10, top=90)

        # Plot time for altitudes
        for _, obj_row in data.dropna().iloc[::6, :].iterrows():
            altitude = obj_row["Sun altitude"]
            azimuth = obj_row["Azimuth"]
            local_time = obj_row["Local_time"]
            if altitude > 0:
                ax.annotate(
                    local_time,
                    (azimuth + copysign(10, azimuth - 180) + 10, altitude + 1),
                    color=style["TEXT_COLOR"],
                )
        return ax

    def __getstate__(self):
        state = self.__dict__.copy()
        # Remove the unpicklable entries.
        del state["ts"]
        del state["eph"]
        del state["location"]
        del state["observer"]
        del state["sun"]
        del state["moon"]
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        # Re-create the unpicklable entries.
        self.ts = load.timescale()
        self.eph = load("de421.bsp")
        self.location = Topos(
            latitude_degrees=self.lat_decimal,
            longitude_degrees=self.lon_decimal,
            elevation_m=self.elevation,
        )
        self.observer = self.eph["earth"] + self.location
        self.sun = self.eph["sun"]
        self.moon = self.eph["moon"]

    def plot_moon_path(self, dark_mode_override: Optional[bool] = None, **args):
        if dark_mode_override is not None:
            effective_dark_mode = dark_mode_override
        else:
            effective_dark_mode = get_dark_mode()

        style = get_plot_style(effective_dark_mode)

        def add_marker(
            ax, label, position, text_color, grid_color
        ):  # Pass ax and colors
            ax.axvline(position, color=grid_color, linestyle="--", linewidth=1)
            ax.text(
                position,
                1,
                label,
                weight="bold",
                horizontalalignment="center",
                color=text_color,
            )

        data = self.moon_path()
        if self.lat_decimal < 0:
            data["Azimuth"] = (data["Azimuth"] + 180) % 360 - 180

        passed_ax = args.pop("ax", None)  # Renamed to avoid confusion

        plot_kwargs = {
            "x": "Azimuth",
            "y": "Moon altitude",
            "title": "Moon altitude",  # This title is styled later by direct ax.set_title
            "style": ".-",
            **args,  # Pass through any other user-supplied keyword arguments
        }

        if passed_ax is not None:
            plot_kwargs["ax"] = passed_ax  # Add 'ax' to kwargs only if it was provided
            data.plot(**plot_kwargs)  # Plot on the provided ax
            ax = passed_ax  # Use the axes that was passed in
            fig = ax.figure  # Get figure from provided ax
        else:
            ax = data.plot(**plot_kwargs)  # Let pandas create a new ax and figure
            fig = ax.figure  # Get figure from newly created ax

        fig.patch.set_facecolor(style["FIGURE_FACE_COLOR"])
        ax.set_facecolor(style["AXES_FACE_COLOR"])

        if ax.lines:  # Style the main moon path line
            ax.lines[0].set_color(style["TEXT_COLOR"])

        # Add cardinal direction and set x-axis limits based on hemisphere
        if self.lat_decimal < 0:  # Southern Hemisphere
            add_marker(ax, "W", -90, style["TEXT_COLOR"], style["GRID_COLOR"])
            add_marker(ax, "N", 0, style["TEXT_COLOR"], style["GRID_COLOR"])
            add_marker(ax, "E", 90, style["TEXT_COLOR"], style["GRID_COLOR"])
            ax.set_xlim(135, -135)  # Inverted for South-up view
        else:  # Northern Hemisphere
            add_marker(ax, "E", 90, style["TEXT_COLOR"], style["GRID_COLOR"])
            add_marker(ax, "S", 180, style["TEXT_COLOR"], style["GRID_COLOR"])
            add_marker(ax, "W", 270, style["TEXT_COLOR"], style["GRID_COLOR"])
            ax.set_xlim(45, 315)
        Utils.annotate_plot(
            ax,
            gettext_("Altitude [°]"),
            effective_dark_mode,
            self.local_timezone,
            x_label=gettext_("Azimuth [°]"),
        )

        # Plot horizon
        ax.axhspan(0, -50, color=style["GRID_COLOR"], alpha=0.3)
        ax.locator_params(nbins=20)
        ax.set_ylim(bottom=-10, top=90)

        # --- Plot Moon Phase Icon and Illumination Text ---
        # Position icon differently based on hemisphere to avoid overlap with path
        if self.lat_decimal < 0:  # Southern Hemisphere, transit is North
            icon_x_position = 0
            icon_y_position = 20
            text_y_position = icon_y_position - 13
        else:  # Northern Hemisphere, transit is South
            icon_x_position = 180
            icon_y_position = 10
            text_y_position = -3

        if effective_dark_mode:
            # In dark mode, draw a solid circle first, then the shadow on top.
            ax.plot(
                icon_x_position,
                icon_y_position,
                marker="o",
                markersize=45,
                color=style["TEXT_COLOR"],
                linestyle="None",
            )
            ax.text(
                icon_x_position,
                icon_y_position,
                self._moon_phase_letter(),
                fontproperties=Place.MOON_FONT,
                horizontalalignment="center",
                verticalalignment="center",
                color=style["AXES_FACE_COLOR"],
            )
        else:
            # In light mode, just draw the phase character.
            ax.text(
                icon_x_position,
                icon_y_position,
                self._moon_phase_letter(),
                fontproperties=Place.MOON_FONT,
                horizontalalignment="center",
                verticalalignment="center",
                color=style["TEXT_COLOR"],
            )
        ax.text(
            icon_x_position,
            text_y_position,
            f"{self.moon_illumination():.0f}%",
            color=style["TEXT_COLOR"],
            alpha=0.7,
            horizontalalignment="center",
        )

        # Plot time for altitudes, adjusting for hemisphere
        for _, obj_row in data.dropna().iloc[::6, :].iterrows():
            altitude = obj_row["Moon altitude"]
            azimuth = obj_row["Azimuth"]
            local_time = obj_row["Local_time"]

            if altitude > 0:
                if self.lat_decimal < 0:  # Southern Hemisphere
                    # Adjust offset direction to avoid text crossing the plot edges
                    offset_direction = azimuth
                    x_offset = copysign(10, offset_direction) + 10
                else:  # Northern Hemisphere
                    x_offset = copysign(10, azimuth - 180) - 8

                ax.annotate(
                    local_time,
                    (azimuth + x_offset, altitude + 1),
                    color=style["TEXT_COLOR"],
                )
        ax.set_title(
            gettext_("Moon Path")
            + f" on {self.date.utc_datetime().strftime('%Y-%m-%d')}",
            color=style["TEXT_COLOR"],
        )
        return ax
