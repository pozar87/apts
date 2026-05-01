import datetime
import math
from typing import TYPE_CHECKING, Any, Callable, Optional, Tuple, cast

import numpy as np
from skyfield.api import Time

if TYPE_CHECKING:
    from skyfield.api import Timescale
    from apts.light_pollution import LightPollution
    from ..weather import Weather

from apts.cache import get_timescale
from apts.light_pollution import LightPollution
from ..weather import Weather
from .utils import get_scalar_datetime


class PlaceConditionsMixIn:
    if TYPE_CHECKING:
        light_pollution: Optional[LightPollution]

        @property
        def lat_decimal(self) -> float: ...
        @property
        def lon_decimal(self) -> float: ...

        date: Time
        observer: Any
        sun: Any
        moon: Any
        local_timezone: Any
        weather: Optional[Weather]
        ts: Timescale
        eph: Any
        elevation: float
        sunset_time: Callable[..., Any]
        sunrise_time: Callable[..., Any]
        get_altaz_curve: Callable[..., Any]

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
            self.observer.at(target_time)
            .observe(self.sun)
            .apparent()
            .altaz()[0]
            .degrees
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

        moon_mags = cast(
            np.ndarray, _get_planet_magnitude("moon", times, astrometric=moon_obs)
        )

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
        cloud_cover = cast(
            np.ndarray, self.weather.data["cloudCover"].astype(float).values
        )
        if bortle > 4:
            b_total *= 1 + 2 * (cloud_cover / 100.0)
        else:
            # Dark site: clouds block starlight
            b_total *= 1 - 0.5 * (cloud_cover / 100.0)

        sqms = cast(np.ndarray, -2.5 * np.log10(np.maximum(b_total, 1e-10)))
        sqms = np.clip(sqms, 10.0, 22.0)

        # Vectorized Seeing Calculation
        wind_speed = cast(
            np.ndarray, self.weather.data["windSpeed"].astype(float).values
        )
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
