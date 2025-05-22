import datetime
import logging
from math import radians as rad, degrees as deg, copysign as copysign

import ephem
import matplotlib.font_manager as font_manager
import pandas as pd
from importlib import resources
import pytz
from dateutil import tz
from timezonefinder import TimezoneFinder

from .weather import Weather

logger = logging.getLogger(__name__)


class Place(ephem.Observer):
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
        date=ephem.Date(datetime.datetime.now(datetime.UTC)),
        *args,
    ):
        ephem.Observer.__init__(self, *args)
        self.date = date
        self.lat = rad(lat)
        self.lon = rad(lon)
        self.lat_decimal = lat
        self.lon_decimal = lon
        self.name = name
        self.elevation = elevation
        # Sun
        self.sun = ephem.Sun()
        self.sun.compute(self)
        # Moon
        self.moon = ephem.Moon()
        self.moon.compute(self)
        self.local_timezone = tz.gettz(
            Place.TF.timezone_at(lat=self.lat_decimal, lng=self.lon_decimal)
        )
        self.weather = None
        logger.debug(f"Place {self.name} initialized, timezone: {self.local_timezone}")

    def get_weather(self):
        self.weather = Weather(self.lat_decimal, self.lon_decimal, self.local_timezone)

    def _next_setting_time(self, obj, start):
        try:
            return (
                self.next_setting(obj, start=start)
                .datetime()
                .replace(tzinfo=pytz.UTC)
                .astimezone(self.local_timezone)
            )
        except (ephem.AlwaysUpError, ephem.NeverUpError):
            return None

    def _next_rising_time(self, obj, start):
        try:
            return (
                self.next_rising(obj, start=start)
                .datetime()
                .replace(tzinfo=pytz.UTC)
                .astimezone(self.local_timezone)
            )
        except (ephem.AlwaysUpError, ephem.NeverUpError):
            return None

    def sunset_time(self, target_date=None):
        if target_date:
            dt_utc = datetime.datetime.combine(target_date, datetime.time(12, 0, 0, tzinfo=datetime.timezone.utc))
            start_date = ephem.Date(dt_utc)
        else:
            start_date = self.date
        return self._next_setting_time(self.sun, start=start_date)

    def sunrise_time(self, target_date=None):
        if target_date:
            dt_utc = datetime.datetime.combine(target_date, datetime.time(12, 0, 0, tzinfo=datetime.timezone.utc))
            start_date = ephem.Date(dt_utc)
        else:
            start_date = self.date
        return self._next_rising_time(self.sun, start=start_date)

    def moonset_time(self):
        return self._next_setting_time(self.moon, start=self.date)

    def moonrise_time(self):
        return self._next_rising_time(self.moon, start=self.date)

    def get_time_relative_to_sunset(self, target_date, offset_minutes=0):
        # Get sunset time for the target_date
        sunset_dt = self.sunset_time(target_date=target_date)

        # If sunset doesn't occur (e.g., polar day/night)
        if sunset_dt is None:
            return (None, None)

        # Apply the offset
        # sunset_dt is already a timezone-aware local datetime object
        local_datetime_obs_time = sunset_dt + datetime.timedelta(minutes=offset_minutes)

        # Convert local observation time to UTC datetime
        utc_datetime_obs_time = local_datetime_obs_time.astimezone(datetime.timezone.utc)

        # Convert UTC datetime to ephem.Date
        corresponding_ephem_date_obs_time = ephem.Date(utc_datetime_obs_time)

        return (local_datetime_obs_time, corresponding_ephem_date_obs_time)

    def _moon_phase_letter(self):
        lunation = self.moon_lunation() / 100
        letter = chr(ord("A") + int(round(lunation * 26)))
        return letter

    def moon_lunation(self):
        return int(self.moon_path()["Lunation"][48] * 100)

    def moon_phase(self):
        return int(self.moon_path()["Phase"][48])

    def moon_path(self):
        self.date = datetime.date.today()
        result = []
        for i in range(26 * 4):  # compute position for every 15 minutes
            self.moon.compute(self)
            next_new_moon = ephem.next_new_moon(self.date)
            previous_new_moon = ephem.previous_new_moon(self.date)
            lunation = (self.date - previous_new_moon) / (
                next_new_moon - previous_new_moon
            )
            row = [
                ephem.localtime(self.date).time(),
                deg(self.moon.alt),
                deg(self.moon.az),
                self.date.datetime()
                .replace(tzinfo=pytz.UTC)
                .astimezone(self.local_timezone)
                .strftime("%H:%M"),
                self.moon.phase,
                lunation,
            ]
            result.append(row)
            self.date += ephem.minute * 15
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

    def plot_moon_path(self, **args):
        def add_marker(label, position):
            plt.axvline(position, color="green", linestyle="--", linewidth=1)
            plt.text(position, 1, label, weight="bold", horizontalalignment="center")

        data = self.moon_path()

        plt = data.plot(
            x="Azimuth", y="Moon altitude", title="Moon altitude", style=".-", **args
        )

        plt.set_xlabel("Azimuth [°]")
        plt.set_ylabel("Altitude [°]")

        # Add cardinal direction
        add_marker("E", 90)
        add_marker("S", 180)
        add_marker("W", 270)
        plt.set_xlim(45, 315)

        # Plot horizon
        plt.axhspan(0, -50, color="gray", alpha=0.2)
        plt.locator_params(nbins=20)
        plt.set_ylim(bottom=-10, top=90)

        # Plot Moon marker
        plt.text(
            180,
            10,
            self._moon_phase_letter(),
            fontproperties=Place.MOON_FONT,
            horizontalalignment="center",
        )
        plt.text(
            180,
            5,
            str(self.moon_phase()) + "%",
            color="gray",
            horizontalalignment="center",
        )

        # Plot time for altitudes
        for obj in data.iloc[::6, :].values:
            if obj[1] > 0:
                plt.annotate(
                    obj[3], (obj[2] + copysign(10, obj[2] - 180) - 8, obj[1] + 1)
                )

        return plt
