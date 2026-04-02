import datetime
import logging
import math
from functools import lru_cache
from math import copysign as copysign
from math import radians as rad
from typing import Any, Iterable, Optional, Tuple, cast

import numpy as np
import pandas as pd
from dateutil import tz
from skyfield import almanac
from skyfield.api import Topos
from timezonefinder import TimezoneFinder

from apts.cache import get_ephemeris, get_timescale
from apts.constants.twilight import Twilight
from apts.light_pollution import LightPollution

from .skyfield_searches.visibility import (
    get_twilight_time_utc,
    next_rising_time_utc,
    next_setting_time_utc,
    previous_rising_time_utc,
    previous_setting_time_utc,
)
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


get_twilight_time_utc = lru_cache(maxsize=1024)(get_twilight_time_utc)
previous_setting_time_utc = lru_cache(maxsize=1024)(previous_setting_time_utc)
next_rising_time_utc = lru_cache(maxsize=1024)(next_rising_time_utc)
next_setting_time_utc = lru_cache(maxsize=1024)(next_setting_time_utc)
previous_rising_time_utc = lru_cache(maxsize=1024)(previous_rising_time_utc)


class TFProxy:
    def __init__(self):
        self._instance = None

    def __getattr__(self, name):
        if self._instance is None:
            self._instance = TimezoneFinder()
        return getattr(self._instance, name)


class Place:
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
        if self.light_pollution is None:
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
        sun_alts = cast(
            np.ndarray,
            self.observer.at(times).observe(self.sun).apparent().altaz()[0].degrees,
        )
        moon_alts = cast(
            np.ndarray,
            self.observer.at(times).observe(self.moon).apparent().altaz()[0].degrees,
        )
        # Vectorized magnitude calculation
        moon_mags = cast(np.ndarray, get_planet_magnitude("moon", times))

        # Bortle info
        bortle = self.get_light_pollution()
        sqm_base = LightPollution.bortle_to_sqm(bortle)
        b_starlight = 10 ** (-0.4 * sqm_base)

        # Vectorized SQM Calculation
        b_total = cast(np.ndarray, np.full(len(times), b_starlight))

        # Sun contribution
        sun_mask = sun_alts > -18
        if np.any(sun_mask):
            b_sun = 10 ** (-0.4 * (21.8 - (18 + sun_alts[sun_mask]) * 0.65))
            b_total[sun_mask] += b_sun

        # Moon contribution
        moon_mask = moon_alts > 0
        if np.any(moon_mask):
            # moon_mags is now an array
            b_moon = 10 ** (-0.4 * (moon_mags[moon_mask] + 31)) * np.sin(
                np.radians(moon_alts[moon_mask])
            )
            b_total[moon_mask] += b_moon

        # Cloud cover effect
        cloud_cover = cast(np.ndarray, self.weather.data["cloudCover"].astype(float).values)
        if bortle > 4:
            b_total *= 1 + 2 * (cloud_cover / 100.0)
        else:
            b_total *= 1 - 0.5 * (cloud_cover / 100.0)

        sqms = cast(np.ndarray, -2.5 * np.log10(np.maximum(b_total, 1e-10)))
        sqms = np.clip(sqms, 10.0, 22.0)

        # Vectorized Seeing Calculation
        wind_speed = cast(np.ndarray, self.weather.data["windSpeed"].astype(float).values)
        humidity = cast(np.ndarray, self.weather.data["humidity"].astype(float).values)

        seeings = cast(np.ndarray, np.full(len(times), 1.5))
        seeings += np.maximum(0, (wind_speed - 15) / 50.0)
        seeings += np.where(humidity > 80, (humidity - 80) / 40.0, 0)
        seeings += np.where(cloud_cover > 50, 0.3, 0)
        seeings = np.clip(seeings, 0.5, 5.0)

        self.weather.data["sqm"] = sqms
        self.weather.data["seeing"] = seeings
        self.weather.data["moon_altitude"] = moon_alts

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
        res = previous_setting_time_utc(
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
        res = next_setting_time_utc(
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
        res = previous_rising_time_utc(
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
        res = next_rising_time_utc(
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
        res = get_twilight_time_utc(
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
        from .plotting.path import generate_plot_sun_path

        return generate_plot_sun_path(self, dark_mode_override, **args)

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
        from .plotting.path import generate_plot_moon_path

        return generate_plot_moon_path(self, dark_mode_override, **args)
