import datetime
import math
from typing import Any, Iterable, Optional, Tuple, cast, TYPE_CHECKING, Callable

import numpy as np
import pandas as pd
from skyfield import almanac
from skyfield.api import Time

if TYPE_CHECKING:
    from skyfield.api import Timescale
    from .base import Place

from apts.cache import get_timescale
from apts.constants.twilight import Twilight
from apts.light_pollution import LightPollution

from .utils import (
    get_scalar_datetime,
    get_twilight_time_utc,
    next_rising_time_utc,
    next_setting_time_utc,
    previous_rising_time_utc,
    previous_setting_time_utc,
)
from ..weather import Weather


class PlaceConditionsMixIn:
    if TYPE_CHECKING:
        light_pollution: Optional[LightPollution]
        lat_decimal: float
        lon_decimal: float
        date: Time
        observer: Any
        sun: Any
        moon: Any
        local_timezone: Any
        weather: Optional[Weather]

    def get_light_pollution(self):
        if self.light_pollution is None:
            self.light_pollution = LightPollution(
                self.lat_decimal,
                self.lon_decimal,
            )
        return self.light_pollution.get_light_pollution()

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
            # Import within the method to ensure patch targets on apts.place work.
            from ..place import get_planet_magnitude as _get_planet_magnitude
            mag_m = _get_planet_magnitude("moon", target_time)
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
            dt = get_scalar_datetime(target_time)

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
            dt = get_scalar_datetime(target_time)
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
            dt = get_scalar_datetime(target_time)
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
            dt = get_scalar_datetime(target_time)
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
        # Optimization: Reuse the Moon observation for both altitude and magnitude
        # to avoid redundant high-precision coordinate transformations.
        moon_obs = self.observer.at(times).observe(self.moon).apparent()
        moon_alts = cast(
            np.ndarray,
            moon_obs.altaz()[0].degrees,
        )
        # Vectorized magnitude calculation - reusing topocentric observation for better accuracy and performance
        # Import within the method to ensure patch targets on apts.place work.
        from ..place import get_planet_magnitude as _get_planet_magnitude
        moon_mags = cast(np.ndarray, _get_planet_magnitude("moon", times, astrometric=moon_obs))

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
            # Dark site: clouds block starlight
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


class PlaceTimesMixIn:
    if TYPE_CHECKING:
        lat_decimal: float
        lon_decimal: float
        elevation: float
        local_timezone: Any

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
        if start_search_from is not None:
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


class PlacePathsMixIn:
    if TYPE_CHECKING:
        ts: Timescale
        observer: Any
        lat_decimal: float
        local_timezone: Any
        moon: Any
        eph: Any
        sun: Any

    def get_altaz_curve(self, skyfield_object, start_time, end_time, num_points=100):
        t0 = start_time if isinstance(start_time, Time) else self.ts.utc(start_time)
        t1 = end_time if isinstance(end_time, Time) else self.ts.utc(end_time)
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
        from ..plotting.path import generate_plot_sun_path

        return generate_plot_sun_path(self, dark_mode_override, **args)

    def plot_moon_path(self, dark_mode_override: Optional[bool] = None, **args):
        from ..plotting.path import generate_plot_moon_path

        return generate_plot_moon_path(self, dark_mode_override, **args)


class PlaceImagingMixIn:
    if TYPE_CHECKING:
        date: Time
        local_timezone: Any
        sunset_time: Callable[..., Any]
        sunrise_time: Callable[..., Any]
        get_altaz_curve: Callable[..., Any]

    def get_imaging_window(
        self, skyfield_object, min_altitude=30, target_date=None
    ) -> dict:
        """
        Calculate total continuous minutes an object remains above the threshold during "darkness"
        (Astronomical Twilight to Astronomical Twilight).
        Provides start_time and end_time for this window.
        """
        # 1. Determine the night window (astronomical twilight)
        # We look for the night following the given target_date or self.date
        t_start = (
            target_date
            if target_date is not None
            else self.date.utc_datetime().replace(tzinfo=datetime.timezone.utc)
        )
        # Ensure it's a datetime
        if isinstance(t_start, datetime.date) and not isinstance(
            t_start, datetime.datetime
        ):
            t_start = datetime.datetime.combine(t_start, datetime.time.min).replace(
                tzinfo=self.local_timezone
            )

        # Get sunset and sunrise (astronomical twilight)
        astro_twilight_start = self.sunset_time(
            start_search_from=t_start, twilight=Twilight.ASTRONOMICAL
        )
        if astro_twilight_start is None:
            return {
                "total_minutes": 0,
                "start_time": None,
                "end_time": None,
            }

        astro_twilight_end = self.sunrise_time(
            start_search_from=astro_twilight_start, twilight=Twilight.ASTRONOMICAL
        )
        if astro_twilight_end is None:
            return {
                "total_minutes": 0,
                "start_time": None,
                "end_time": None,
            }

        # 2. Check object altitude during this window
        num_points = 60 * 12  # Every 2 minutes for 24h
        df = self.get_altaz_curve(
            skyfield_object, astro_twilight_start, astro_twilight_end, num_points
        )

        above_threshold = df[df["Altitude"] >= min_altitude]
        if above_threshold.empty:
            return {
                "total_minutes": 0,
                "start_time": None,
                "end_time": None,
            }

        # Find the longest continuous block
        above_threshold = above_threshold.copy()
        above_threshold["group"] = (above_threshold.index.to_series().diff() > 1).cumsum()
        longest_group = above_threshold.groupby("group").size().idxmax()
        window_df = above_threshold[above_threshold["group"] == longest_group]

        start_time = window_df["UTC_datetime"].iloc[0].to_pydatetime()
        end_time = window_df["UTC_datetime"].iloc[-1].to_pydatetime()
        total_minutes = (end_time - start_time).total_seconds() / 60.0

        return {
            "total_minutes": total_minutes,
            "start_time": start_time,
            "end_time": end_time,
        }
