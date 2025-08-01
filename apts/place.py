import datetime
import logging
from math import radians as rad, copysign as copysign

import matplotlib.font_manager as font_manager
import pandas as pd
from importlib import resources
import pytz
from dateutil import tz
from timezonefinder import TimezoneFinder
from typing import Optional  # Added
from apts.config import get_dark_mode  # Added
from apts.constants.graphconstants import get_plot_style  # Added

from .weather import Weather
from skyfield.api import load, Topos, Star
from skyfield import almanac

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
        logger.debug(f"Place {self.name} initialized, timezone: {self.local_timezone}")

    def get_weather(self):
        self.weather = Weather(self.lat_decimal, self.lon_decimal, self.local_timezone)

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

    def sunset_time(
        self, target_date=None, start_search_from: Optional[datetime.datetime] = None
    ):
        if start_search_from:
            start_date = start_search_from
        elif target_date:
            start_date = datetime.datetime.combine(
                target_date, datetime.time(12, 0, 0, tzinfo=datetime.timezone.utc)
            )
        else:
            start_date = self.date.utc_datetime()
        return self._next_setting_time(self.sun, start=start_date)

    def sunrise_time(
        self, target_date=None, start_search_from: Optional[datetime.datetime] = None
    ):
        if start_search_from:
            start_date = start_search_from
        elif target_date:
            start_date = datetime.datetime.combine(
                target_date, datetime.time(12, 0, 0, tzinfo=datetime.timezone.utc)
            )
        else:
            start_date = self.date.utc_datetime()
        return self._next_rising_time(self.sun, start=start_date)

    def moonset_time(self):
        return self._next_setting_time(self.moon, start=self.date.utc_datetime())

    def moonrise_time(self):
        return self._next_rising_time(self.moon, start=self.date.utc_datetime())

    def get_time_relative_to_event(self, target_date, offset_minutes=0, event="sunset"):
        # Get sunset time for the target_date
        if event == "sunset":
            event_dt = self.sunset_time(target_date=target_date)
        else:
            event_dt = self.sunrise_time(target_date=target_date)

        # If sunset doesn't occur (e.g., polar day/night)
        if event_dt is None:
            return (None, None)

        # Apply the offset
        # sunset_dt is already a timezone-aware local datetime object
        local_datetime_obs_time = event_dt + datetime.timedelta(minutes=offset_minutes)

        # Convert local observation time to UTC datetime
        utc_datetime_obs_time = local_datetime_obs_time.astimezone(
            datetime.timezone.utc
        )

        return (local_datetime_obs_time, self.ts.utc(utc_datetime_obs_time))

    def _moon_phase_letter(self):
        lunation = self.moon_lunation() / 100
        letter = chr(ord("A") + int(round(lunation * 26)))
        return letter

    def moon_lunation(self):
        return int(self.moon_path()["Lunation"][48] * 100)

    def moon_phase(self):
        return int(self.moon_path()["Phase"][48])

    def moon_path(self):
        t0 = self.ts.utc(datetime.date.today())
        t1 = self.ts.utc(datetime.date.today() + datetime.timedelta(days=1))
        times = self.ts.linspace(t0, t1, 26 * 4)
        result = []
        for t in times:
            alt, az, _ = self.observer.at(t).observe(self.moon).apparent().altaz()
            moon_phase_angle = almanac.moon_phase(self.eph, t)
            phase = (moon_phase_angle.degrees / 360.0) * 100
            lunation = moon_phase_angle.degrees / 360.0
            row = [
                t.utc_datetime().time(),
                alt.degrees,
                az.degrees,
                t.astimezone(self.local_timezone).strftime("%H:%M"),
                phase,
                lunation,
            ]
            result.append(row)
        return pd.DataFrame(
            result,
            columns=[
                "Time",
                "Moon altitude",
                "Azimuth",
                "Local_time",
                "Phase",
                "Lunation",
            ],
        )

    def sun_path(self):
        t0 = self.ts.utc(datetime.date.today())
        t1 = self.ts.utc(datetime.date.today() + datetime.timedelta(days=1))
        times = self.ts.linspace(t0, t1, 26 * 4)
        result = []
        for t in times:
            alt, az, _ = self.observer.at(t).observe(self.sun).apparent().altaz()
            row = [
                t.utc_datetime().time(),
                alt.degrees,
                az.degrees,
                t.astimezone(self.local_timezone).strftime("%H:%M"),
            ]
            result.append(row)
        return pd.DataFrame(
            result,
            columns=[
                "Time",
                "Sun altitude",
                "Azimuth",
                "Local_time",
            ],
        )

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

        ax.set_xlabel("Azimuth [°]", color=style["TEXT_COLOR"])
        ax.set_ylabel("Altitude [°]", color=style["TEXT_COLOR"])
        ax.set_title("Sun altitude", color=style["TEXT_COLOR"])

        ax.tick_params(axis="x", colors=style["TICK_COLOR"])
        ax.tick_params(axis="y", colors=style["TICK_COLOR"])

        for spine_pos in ["top", "bottom", "left", "right"]:
            ax.spines[spine_pos].set_color(style["AXIS_COLOR"])

        # Add cardinal direction
        add_marker(ax, "E", 90, style["TEXT_COLOR"], style["GRID_COLOR"])
        add_marker(ax, "S", 180, style["TEXT_COLOR"], style["GRID_COLOR"])
        add_marker(ax, "W", 270, style["TEXT_COLOR"], style["GRID_COLOR"])
        ax.set_xlim(45, 315)

        # Plot horizon
        ax.axhspan(0, -50, color=style["GRID_COLOR"], alpha=0.3)
        ax.locator_params(nbins=20)
        ax.set_ylim(bottom=-10, top=90)

        # Plot time for altitudes
        for obj_row in data.iloc[
            ::6, :
        ].values:  # Renamed obj to obj_row to avoid conflict
            if obj_row[1] > 0:  # Altitude is at index 1
                ax.annotate(
                    obj_row[3],
                    (obj_row[2] + copysign(10, obj_row[2] - 180) - 8, obj_row[1] + 1),
                    color=style["TEXT_COLOR"],
                )

        return ax

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

        ax.set_xlabel("Azimuth [°]", color=style["TEXT_COLOR"])
        ax.set_ylabel("Altitude [°]", color=style["TEXT_COLOR"])
        ax.set_title("Moon altitude", color=style["TEXT_COLOR"])

        ax.tick_params(axis="x", colors=style["TICK_COLOR"])
        ax.tick_params(axis="y", colors=style["TICK_COLOR"])

        for spine_pos in ["top", "bottom", "left", "right"]:
            ax.spines[spine_pos].set_color(style["AXIS_COLOR"])

        # Add cardinal direction
        add_marker(ax, "E", 90, style["TEXT_COLOR"], style["GRID_COLOR"])
        add_marker(ax, "S", 180, style["TEXT_COLOR"], style["GRID_COLOR"])
        add_marker(ax, "W", 270, style["TEXT_COLOR"], style["GRID_COLOR"])
        ax.set_xlim(45, 315)

        # Plot horizon
        ax.axhspan(0, -50, color=style["GRID_COLOR"], alpha=0.3)
        ax.locator_params(nbins=20)
        ax.set_ylim(bottom=-10, top=90)

        # Plot Moon marker
        ax.text(
            180,
            10,
            self._moon_phase_letter(),
            fontproperties=Place.MOON_FONT,
            horizontalalignment="center",
            color=style["TEXT_COLOR"],
        )
        ax.text(
            180,
            5,
            str(self.moon_phase()) + "%",
            color=style[
                "TEXT_COLOR"
            ],  # Using main text color, adjust alpha for muted effect
            alpha=0.7,
            horizontalalignment="center",
        )

        # Plot time for altitudes
        for obj_row in data.iloc[
            ::6, :
        ].values:  # Renamed obj to obj_row to avoid conflict
            if obj_row[1] > 0:  # Altitude is at index 1
                ax.annotate(
                    obj_row[3],
                    (obj_row[2] + copysign(10, obj_row[2] - 180) - 8, obj_row[1] + 1),
                    color=style["TEXT_COLOR"],
                )

        return ax
