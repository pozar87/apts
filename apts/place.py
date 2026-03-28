import datetime
import logging
import math
from functools import lru_cache
from importlib import resources
from math import copysign as copysign
from math import radians as rad
from typing import Any, Iterable, Optional, Tuple, cast

import matplotlib.font_manager as font_manager
import numpy as np
import pandas as pd
import pytz
from dateutil import tz
from skyfield import almanac
from skyfield.api import Topos
from timezonefinder import TimezoneFinder

from apts.cache import get_ephemeris, get_timescale
from apts.config import get_dark_mode
from apts.constants.graphconstants import get_plot_style
from apts.constants.twilight import Twilight
from apts.i18n import gettext_
from apts.light_pollution import LightPollution
from apts.utils.plot import Utils as PlotUtils

from .utils.planetary import (
    get_moon_age,
    get_moon_distance,
    get_moon_illumination,
    get_moon_phase_name,
    get_planet_magnitude,
    get_skyfield_obj,
)
from .weather import Weather

logger = logging.getLogger(__name__)


@lru_cache(maxsize=1024)
def _get_twilight_time_utc(lat, lon, elevation, start_date, twilight, event):
    ts = get_timescale()
    eph = get_ephemeris()
    location = Topos(latitude_degrees=lat, longitude_degrees=lon, elevation_m=float(elevation))
    t0 = ts.utc(start_date)
    t1 = ts.utc(start_date + datetime.timedelta(days=2))

    f = almanac.dark_twilight_day(eph, location)
    times, events = almanac.find_discrete(t0, t1, f)

    # Define transitions for evening (set) and morning (rise)
    if event == "set":  # Evening: getting darker
        transitions = {
            Twilight.CIVIL: (3, 2),  # Civil -> Nautical
            Twilight.NAUTICAL: (2, 1),  # Nautical -> Astronomical
            Twilight.ASTRONOMICAL: (1, 0),  # Astronomical -> Night
        }
    else:  # Morning: getting lighter
        transitions = {
            Twilight.ASTRONOMICAL: (0, 1),  # Night -> Astronomical
            Twilight.NAUTICAL: (1, 2),  # Astronomical -> Nautical
            Twilight.CIVIL: (2, 3),  # Nautical -> Civil
        }

    trans = transitions.get(twilight)
    if trans is None:
        return None
    prev_event, next_event = trans

    # The first event is the state at t0
    previous_y = f(t0)
    if times is not None and events is not None:
        for t, y in zip(times, events):
            if previous_y == prev_event and y == next_event:
                return t.utc_datetime().replace(tzinfo=pytz.UTC)
            previous_y = y

    return None


@lru_cache(maxsize=1024)
def _previous_setting_time_utc(lat, lon, elevation, obj_name, start, horizon_degrees=None):
    ts = get_timescale()
    eph = get_ephemeris()
    location = Topos(latitude_degrees=lat, longitude_degrees=lon, elevation_m=float(elevation))
    obj = eph[obj_name]
    t0 = ts.utc(start - datetime.timedelta(days=2))
    t1 = ts.utc(start)
    if horizon_degrees is not None:
        f = almanac.risings_and_settings(eph, obj, location, horizon_degrees=horizon_degrees)
    else:
        f = almanac.risings_and_settings(eph, obj, location)
    t, y = almanac.find_discrete(t0, t1, f)

    if t is None:
        return None

    settings = [ti for ti, yi in zip(t, y) if yi == 0]
    if settings:
        return settings[-1].utc_datetime().replace(tzinfo=pytz.UTC)
    return None


@lru_cache(maxsize=1024)
def _next_rising_time_utc(lat, lon, elevation, obj_name, start, horizon_degrees=None):
    ts = get_timescale()
    eph = get_ephemeris()
    location = Topos(latitude_degrees=lat, longitude_degrees=lon, elevation_m=float(elevation))
    obj = eph[obj_name]
    t0 = ts.utc(start)
    t1 = ts.utc(start + datetime.timedelta(days=2))
    if horizon_degrees is not None:
        f = almanac.risings_and_settings(eph, obj, location, horizon_degrees=horizon_degrees)
    else:
        f = almanac.risings_and_settings(eph, obj, location)
    t, y = almanac.find_discrete(t0, t1, f)

    if t is not None:
        for ti, yi in zip(t, y):
            if yi == 1:  # Rising
                return ti.utc_datetime().replace(tzinfo=pytz.UTC)
    return None


@lru_cache(maxsize=1024)
def _next_setting_time_utc(lat, lon, elevation, obj_name, start, horizon_degrees=None):
    ts = get_timescale()
    eph = get_ephemeris()
    location = Topos(latitude_degrees=lat, longitude_degrees=lon, elevation_m=float(elevation))
    obj = eph[obj_name]
    t0 = ts.utc(start)
    t1 = ts.utc(start + datetime.timedelta(days=2))
    if horizon_degrees is not None:
        f = almanac.risings_and_settings(eph, obj, location, horizon_degrees=horizon_degrees)
    else:
        f = almanac.risings_and_settings(eph, obj, location)
    t, y = almanac.find_discrete(t0, t1, f)

    if t is not None:
        for ti, yi in zip(t, y):
            if yi == 0:  # Setting
                return ti.utc_datetime().replace(tzinfo=pytz.UTC)
    return None


@lru_cache(maxsize=1024)
def _previous_rising_time_utc(lat, lon, elevation, obj_name, start, horizon_degrees=None):
    ts = get_timescale()
    eph = get_ephemeris()
    location = Topos(latitude_degrees=lat, longitude_degrees=lon, elevation_m=float(elevation))
    obj = eph[obj_name]
    t0 = ts.utc(start - datetime.timedelta(days=2))
    t1 = ts.utc(start)
    if horizon_degrees is not None:
        f = almanac.risings_and_settings(eph, obj, location, horizon_degrees=horizon_degrees)
    else:
        f = almanac.risings_and_settings(eph, obj, location)
    t, y = almanac.find_discrete(t0, t1, f)

    if t is None:
        return None

    risings = [ti for ti, yi in zip(t, y) if yi == 1]
    if risings:
        return risings[-1].utc_datetime().replace(tzinfo=pytz.UTC)
    return None


class TFProxy:
    def __init__(self):
        self._instance = None

    def __getattr__(self, name):
        if self._instance is None:
            self._instance = TimezoneFinder()
        return getattr(self._instance, name)


class Place:
    MOON_FONT = font_manager.FontProperties(
        fname=str(resources.files("apts").joinpath("data/moon_phases.ttf")), size=50
    )
    TF = TFProxy()

    def __init__(
        self,
        lat,
        lon,
        name="",
        elevation=300,
        date=datetime.datetime.now(datetime.UTC),
    ):
        self.ts = get_timescale()
        self.eph = get_ephemeris()
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
            latitude_degrees=lat, longitude_degrees=lon, elevation_m=float(elevation)
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

    def _get_scalar_datetime(self, target_time: Any) -> datetime.datetime:
        """
        Helper to convert a Skyfield Time object (scalar or vector) to a scalar
        timezone-aware UTC datetime.
        """
        dt_raw = target_time.utc_datetime()
        if isinstance(dt_raw, (list, np.ndarray)):
            dt = dt_raw[0]
        else:
            dt = dt_raw

        if dt.tzinfo is None:
            return dt.replace(tzinfo=datetime.timezone.utc)
        return dt

    def get_sqm(self, time: Optional[Any] = None) -> float:
        """
        Returns the approximate SQM value for the place based on its Bortle class,
        accounting for Sun, Moon, and cloud cover if weather data is available.
        """
        target_time = time if time is not None else self.date
        bortle = self.get_light_pollution()
        if bortle <= 0:
            return 0.0

        sqm_base = LightPollution.bortle_to_sqm(bortle)
        b_total = 10 ** (-0.4 * sqm_base)

        # Sun contribution
        sun_alt = (
            self.observer.at(target_time).observe(self.sun).apparent().altaz()[0].degrees
        )
        if sun_alt > -18:
            # Simplified twilight model: brightness increases as sun rises
            # At -18 deg, it's roughly base starlight. At -6, it's much brighter.
            # Using: SQM_sun = 21.8 - (18 + sun_alt) * 0.65
            b_sun = 10 ** (-0.4 * (21.8 - (18 + sun_alt) * 0.65))
            b_total += b_sun

        # Moon contribution
        moon_alt = (
            self.observer.at(target_time)
            .observe(self.moon)
            .apparent()
            .altaz()[0]
            .degrees
        )
        if moon_alt > 0:
            mag_m = get_planet_magnitude("moon", target_time)
            # Simplified moon model
            # Zenith brightness model for Moon: SQM_moon_zenith = mag_m + 31
            # Combined with sine altitude factor
            b_moon = 10 ** (-0.4 * (mag_m + 31)) * np.sin(np.radians(moon_alt))
            b_total += b_moon

        # Cloud cover effect
        cloud_cover = 0
        if (
            self.weather is not None
            and self.weather.data is not None
            and not self.weather.data.empty
        ):
            # Find nearest time in weather data
            # target_time is Skyfield Time, convert to scalar aware datetime
            dt = self._get_scalar_datetime(target_time)

            # Simple nearest neighbor
            idx = (self.weather.data["time"] - dt).abs().idxmin()
            cloud_cover = float(self.weather.data.loc[idx, "cloudCover"])

        if bortle > 4:
            # Urban: clouds reflect city lights
            b_total *= 1 + 2 * (cloud_cover / 100.0)
        else:
            # Dark site: clouds block starlight
            b_total *= 1 - 0.5 * (cloud_cover / 100.0)

        sqm = -2.5 * math.log10(max(b_total, 1e-10))
        sqm_val = min(max(sqm, 10.0), 22.0)

        # Update cache if time matches weather data
        if (
            self.weather is not None
            and self.weather.data is not None
            and not self.weather.data.empty
        ):
            dt = self._get_scalar_datetime(target_time)
            idx = (self.weather.data["time"] - dt).abs().idxmin()
            if (self.weather.data.loc[idx, "time"] - dt).total_seconds() == 0:
                self.weather.data.loc[idx, "sqm"] = sqm_val

        return sqm_val

    def get_seeing(self, time: Optional[Any] = None) -> float:
        """
        Estimates the astronomical seeing in arcseconds based on weather conditions.
        """
        target_time = time if time is not None else self.date
        s = 1.5  # Base seeing

        if (
            self.weather is not None
            and self.weather.data is not None
            and not self.weather.data.empty
        ):
            dt = self._get_scalar_datetime(target_time)
            idx = (self.weather.data["time"] - dt).abs().idxmin()

            wind_speed = float(self.weather.data.loc[idx, "windSpeed"])
            humidity = float(self.weather.data.loc[idx, "humidity"])
            cloud_cover = float(self.weather.data.loc[idx, "cloudCover"])

            # Wind penalty: turbulence increases with wind
            s += max(0, (wind_speed - 15) / 50.0)

            # Humidity penalty: haze and instability
            if humidity > 80:
                s += (humidity - 80) / 40.0

            # Cloud penalty: correlation with instability
            if cloud_cover > 50:
                s += 0.3

        seeing_val = min(max(s, 0.5), 5.0)

        # Update cache if time matches weather data
        if (
            self.weather is not None
            and self.weather.data is not None
            and not self.weather.data.empty
        ):
            dt = self._get_scalar_datetime(target_time)
            idx = (self.weather.data["time"] - dt).abs().idxmin()
            if (self.weather.data.loc[idx, "time"] - dt).total_seconds() == 0:
                self.weather.data.loc[idx, "seeing"] = seeing_val

        return seeing_val

    def _add_extra_weather_info(self):
        """
        Calculates seeing and SQM for all time points in weather data.
        """
        if self.weather is None or self.weather.data is None or self.weather.data.empty:
            return

        ts = get_timescale()
        times = ts.from_datetimes(self.weather.data["time"].tolist())

        # Vectorized Sun/Moon altitude calculation
        sun_alts = (
            self.observer.at(times).observe(self.sun).apparent().altaz()[0].degrees
        )
        moon_alts = (
            self.observer.at(times).observe(self.moon).apparent().altaz()[0].degrees
        )
        # Handle magnitude calculation for vectorized times
        moon_mags = [get_planet_magnitude("moon", t) for t in times]

        # Bortle info
        bortle = self.get_light_pollution()
        sqm_base = LightPollution.bortle_to_sqm(bortle)
        b_starlight = 10 ** (-0.4 * sqm_base)

        seeings = []
        sqms = []

        for i, row in self.weather.data.iterrows():
            # SQM Calculation
            b_total = b_starlight
            sun_alt = sun_alts[i]
            if sun_alt > -18:
                b_sun = 10 ** (-0.4 * (21.8 - (18 + sun_alt) * 0.65))
                b_total += b_sun

            moon_alt = moon_alts[i]
            if moon_alt > 0:
                mag_m = moon_mags[i]
                b_moon = 10 ** (-0.4 * (mag_m + 31)) * np.sin(np.radians(moon_alt))
                b_total += b_moon

            cloud_cover = float(row["cloudCover"])
            if bortle > 4:
                b_total *= 1 + 2 * (cloud_cover / 100.0)
            else:
                b_total *= 1 - 0.5 * (cloud_cover / 100.0)

            sqm = -2.5 * math.log10(max(b_total, 1e-10))
            sqms.append(min(max(sqm, 10.0), 22.0))

            # Seeing Calculation
            s = 1.5
            wind_speed = float(row["windSpeed"])
            humidity = float(row["humidity"])
            s += max(0, (wind_speed - 15) / 50.0)
            if humidity > 80:
                s += (humidity - 80) / 40.0
            if cloud_cover > 50:
                s += 0.3
            seeings.append(min(max(s, 0.5), 5.0))

        self.weather.data["sqm"] = sqms
        self.weather.data["seeing"] = seeings

    def get_altitude(self, object_or_name: Any, time: Optional[Any] = None) -> float:
        """
        Returns the topocentric apparent altitude of a celestial object in degrees.
        Supports both Skyfield objects and string names (e.g., 'Jupiter').
        Uses high-precision refraction settings (10°C, 1013.25 mbar).
        """
        target_time = time if time is not None else self.date
        obj = (
            get_skyfield_obj(object_or_name)
            if isinstance(object_or_name, str)
            else object_or_name
        )
        alt, _, _ = (
            self.observer.at(target_time)
            .observe(obj)
            .apparent()
            .altaz(temperature_C=10.0, pressure_mbar=1013.25)
        )
        return float(alt.degrees)

    def get_azimuth(self, object_or_name: Any, time: Optional[Any] = None) -> float:
        """
        Returns the topocentric apparent azimuth of a celestial object in degrees.
        Supports both Skyfield objects and string names (e.g., 'Jupiter').
        Uses high-precision refraction settings (10°C, 1013.25 mbar).
        """
        target_time = time if time is not None else self.date
        obj = (
            get_skyfield_obj(object_or_name)
            if isinstance(object_or_name, str)
            else object_or_name
        )
        _, az, _ = (
            self.observer.at(target_time)
            .observe(obj)
            .apparent()
            .altaz(temperature_C=10.0, pressure_mbar=1013.25)
        )
        return float(az.degrees)

    def get_weather(
        self,
        provider_name: Optional[str] = None,
        hours: int = 48,
        conditions: Optional[Any] = None,
        observation_window: Optional[
            Tuple[datetime.datetime, datetime.datetime]
        ] = None,
        force: bool = False,
    ):
        self.weather = Weather(
            self.lat_decimal,
            self.lon_decimal,
            self.local_timezone,
            provider_name=provider_name,
            hours=hours,
            conditions=conditions,
            observation_window=observation_window,
            force=force,
        )
        self._add_extra_weather_info()

    def _previous_setting_time(self, obj_name, start, horizon_degrees=None):
        res = _previous_setting_time_utc(
            self.lat_decimal,
            self.lon_decimal,
            self.elevation,
            obj_name,
            start,
            horizon_degrees=horizon_degrees,
        )
        if res:
            return res.astimezone(self.local_timezone)
        return None

    def _next_setting_time(self, obj_name, start, horizon_degrees=None):
        res = _next_setting_time_utc(
            self.lat_decimal,
            self.lon_decimal,
            self.elevation,
            obj_name,
            start,
            horizon_degrees=horizon_degrees,
        )
        if res:
            return res.astimezone(self.local_timezone)
        return None

    def _previous_rising_time(self, obj_name, start, horizon_degrees=None):
        res = _previous_rising_time_utc(
            self.lat_decimal,
            self.lon_decimal,
            self.elevation,
            obj_name,
            start,
            horizon_degrees=horizon_degrees,
        )
        if res:
            return res.astimezone(self.local_timezone)
        return None

    def _next_rising_time(self, obj_name, start, horizon_degrees=None):
        res = _next_rising_time_utc(
            self.lat_decimal,
            self.lon_decimal,
            self.elevation,
            obj_name,
            start,
            horizon_degrees=horizon_degrees,
        )
        if res:
            return res.astimezone(self.local_timezone)
        return None

    def _get_start_date(self, target_date, start_search_from):
        if start_search_from:
            return start_search_from
        elif target_date:
            if isinstance(target_date, datetime.datetime):
                # Ensure we handle both date and datetime
                target_date = target_date.date()
            local_start_of_day = datetime.datetime.combine(
                target_date, datetime.time.min
            ).replace(tzinfo=self.local_timezone)
            return local_start_of_day.astimezone(datetime.timezone.utc)
        else:
            return self.date.utc_datetime()  # type: ignore

    def _get_twilight_time(self, start_date, twilight: Twilight, event: str):
        res = _get_twilight_time_utc(
            self.lat_decimal,
            self.lon_decimal,
            self.elevation,
            start_date,
            twilight,
            event,
        )
        if res:
            return res.astimezone(self.local_timezone)
        return None

    def sunset_time(
        self,
        target_date=None,
        start_search_from: Optional[datetime.datetime] = None,
        twilight: Optional[Twilight] = None,
        horizon_degrees: float = -0.8333,
    ):
        start_date = self._get_start_date(target_date, start_search_from)
        if twilight:
            return self._get_twilight_time(start_date, twilight, "set")
        return self._next_setting_time("sun", start=start_date, horizon_degrees=horizon_degrees)

    def sunrise_time(
        self,
        target_date=None,
        start_search_from: Optional[datetime.datetime] = None,
        twilight: Optional[Twilight] = None,
        horizon_degrees: float = -0.8333,
    ):
        start_date = self._get_start_date(target_date, start_search_from)
        if twilight:
            return self._get_twilight_time(start_date, twilight, "rise")
        return self._next_rising_time("sun", start=start_date, horizon_degrees=horizon_degrees)

    def moonset_time(
        self,
        target_date=None,
        start_search_from: Optional[datetime.datetime] = None,
        horizon_degrees: float = -0.8333,
    ):
        start_date = self._get_start_date(target_date, start_search_from)
        return self._next_setting_time(
            "moon", start=start_date, horizon_degrees=horizon_degrees
        )

    def moonrise_time(
        self,
        target_date=None,
        start_search_from: Optional[datetime.datetime] = None,
        horizon_degrees: float = -0.8333,
    ):
        start_date = self._get_start_date(target_date, start_search_from)
        return self._next_rising_time(
            "moon", start=start_date, horizon_degrees=horizon_degrees
        )

    def _moon_phase_letter(self) -> str:
        phase_angle = almanac.moon_phase(self.eph, self.date)
        if hasattr(phase_angle, "degrees"):
            phase_angle_deg = phase_angle.degrees
        else:
            phase_angle_deg = float(phase_angle)  # type: ignore
        lunation = cast(float, phase_angle_deg) / 360.0
        letter = chr(ord("A") + int(round(lunation * 26)))
        return letter

    def moon_illumination(self):
        return get_moon_illumination(self.date)

    def moon_phase_name(self):
        """
        Returns the name of the moon phase.
        """
        return get_moon_phase_name(self.date)

    def moon_age(self):
        """
        Returns the Moon age in days.
        """
        return get_moon_age(self.date)

    def moon_distance(self):
        """
        Returns the Moon distance in km.
        """
        return get_moon_distance(self.date)

    def get_altaz_curve(self, skyfield_object, start_time, end_time, num_points=100):
        t0 = self.ts.utc(start_time)
        t1 = self.ts.utc(end_time)
        times = self.ts.linspace(t0, t1, num_points)

        alt, az, _ = self.observer.at(times).observe(skyfield_object).apparent().altaz()

        # Vectorized conversion to datetime
        utcs = times.utc_datetime()

        df = pd.DataFrame(
            {
                "Time": list(cast(Iterable[Any], times)),
                "UTC_datetime": utcs,
                "Altitude": alt.degrees,
                "Azimuth": az.degrees,
            }
        )

        # For Southern Hemisphere, the transit is North (0/360 degrees).
        # If the path crosses this point, matplotlib will draw a line across the plot.
        # To prevent this, we find the wrap-around point and insert a NaN row.
        if self.lat_decimal < 0:
            diffs = cast(pd.Series, df["Azimuth"].diff())
            wrap_around_indices = cast(pd.Series, diffs[diffs.abs() > 180]).index
            if len(wrap_around_indices) > 0:
                idx = cast(Any, wrap_around_indices[0])
                new_index = idx - 0.5
                nan_row = pd.DataFrame(
                    {
                        "Time": [pd.NaT],
                        "UTC_datetime": [pd.NaT],
                        "Altitude": [np.nan],
                        "Azimuth": [np.nan],
                    },
                    index=[new_index],  # type: ignore
                )
                df = pd.concat([df, nan_row]).sort_index().reset_index(drop=True)  # type: ignore

        # Ensure UTC_datetime is recognized as a datetime series
        df["UTC_datetime"] = pd.to_datetime(df["UTC_datetime"])
        local_datetimes = df["UTC_datetime"]
        if local_datetimes.dt.tz is None:
            local_datetimes = local_datetimes.dt.tz_localize("UTC")

        df["Local_time"] = local_datetimes.dt.tz_convert(
            self.local_timezone
        ).dt.strftime("%H:%M")
        return df

    def moon_path(self) -> pd.DataFrame:
        start_time = self.date.utc_datetime().replace(  # type: ignore
            hour=0, minute=0, second=0, microsecond=0
        )
        end_time = start_time + datetime.timedelta(days=1)
        df = self.get_altaz_curve(self.moon, start_time, end_time, num_points=26 * 8)
        df = df.rename(columns={"Altitude": "Moon altitude"})

        # Vectorized moon phase calculation
        if "UTC_datetime" in df.columns:
            valid_mask = df["UTC_datetime"].notna()
        else:
            # Fallback for mocks
            df["UTC_datetime"] = df["Time"].apply(
                lambda t: t.utc_datetime() if hasattr(t, "utc_datetime") else pd.NaT
            )
            df["UTC_datetime"] = pd.to_datetime(df["UTC_datetime"])
            valid_mask = df["UTC_datetime"].notna()

        if bool(valid_mask.any()):
            # Convert valid datetimes back to a Skyfield Time vector
            times_vec = self.ts.from_datetimes(
                df.loc[valid_mask, "UTC_datetime"].tolist()
            )
            moon_phase_angles = almanac.moon_phase(self.eph, times_vec).degrees
            df.loc[valid_mask, "Phase"] = (
                cast(np.ndarray[Any, Any], moon_phase_angles) / 360.0
            ) * 100
            df.loc[valid_mask, "Lunation"] = (
                cast(np.ndarray[Any, Any], moon_phase_angles) / 360.0
            )
        else:
            df["Phase"] = pd.NA
            df["Lunation"] = pd.NA

        df["Time"] = df["UTC_datetime"].dt.time
        return df

    def sun_path(self) -> pd.DataFrame:
        start_time = self.date.utc_datetime().replace(  # type: ignore
            hour=0, minute=0, second=0, microsecond=0
        )
        end_time = start_time + datetime.timedelta(days=1)
        df = self.get_altaz_curve(self.sun, start_time, end_time, num_points=26 * 4)
        df = df.rename(columns={"Altitude": "Sun altitude"})

        if "UTC_datetime" not in df.columns:
            # Fallback for mocks
            df["UTC_datetime"] = df["Time"].apply(
                lambda t: t.utc_datetime() if hasattr(t, "utc_datetime") else pd.NaT
            )
            df["UTC_datetime"] = pd.to_datetime(df["UTC_datetime"])

        df["Time"] = df["UTC_datetime"].dt.time
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
                date=self.date.utc_datetime().strftime("%Y-%m-%d")  # type: ignore
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

        PlotUtils.annotate_plot(
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
        PlotUtils.style_legend(ax, style)
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
        self.ts = get_timescale()
        self.eph = get_ephemeris()
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
        PlotUtils.annotate_plot(
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
            + f" on {self.date.utc_datetime().strftime('%Y-%m-%d')}",  # type: ignore
            color=style["TEXT_COLOR"],
        )
        PlotUtils.style_legend(ax, style)
        return ax
