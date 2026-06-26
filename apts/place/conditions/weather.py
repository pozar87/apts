import datetime
from typing import TYPE_CHECKING, Any, Optional, Tuple, cast

import numpy as np

if TYPE_CHECKING:
    from ..weather import Weather

from ...weather import Weather
from ...cache import get_timescale


class WeatherMixIn:
    if TYPE_CHECKING:
        lat_decimal: float
        lon_decimal: float
        local_timezone: Any
        weather: Optional[Weather]
        observer: Any
        sun: Any
        moon: Any

        def _calculate_bulk_sqm(
            self, sun_alts: np.ndarray, moon_alts: np.ndarray, moon_mags: np.ndarray
        ) -> np.ndarray: ...
        def _calculate_bulk_seeing(self) -> np.ndarray: ...

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
        from ...place import get_planet_magnitude as _get_planet_magnitude

        moon_mags = cast(
            np.ndarray, _get_planet_magnitude("moon", times, astrometric=moon_obs)
        )

        # Delegate specialized calculations to other mixins
        sqms = self._calculate_bulk_sqm(sun_alts, moon_alts, moon_mags)
        seeings = self._calculate_bulk_seeing()

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
