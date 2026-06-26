from typing import TYPE_CHECKING, Any, Optional, cast

import numpy as np

if TYPE_CHECKING:
    from skyfield.api import Time
    from ..weather import Weather

from ..utils import get_scalar_datetime


class SeeingMixIn:
    if TYPE_CHECKING:
        date: "Time"
        weather: Optional["Weather"]

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

    def _calculate_bulk_seeing(self) -> np.ndarray:
        """
        Internal vectorized seeing calculation.
        """
        if self.weather is None or self.weather.data is None:
            return np.array([])

        cloud_cover = cast(
            np.ndarray, self.weather.data["cloudCover"].astype(float).values
        )
        wind_speed = cast(
            np.ndarray, self.weather.data["windSpeed"].astype(float).values
        )
        humidity = cast(np.ndarray, self.weather.data["humidity"].astype(float).values)

        seeings = cast(np.ndarray, np.full(len(self.weather.data), 1.5))
        seeings += np.maximum(0, (wind_speed - 15) / 50.0)
        seeings += np.where(humidity > 80, (humidity - 80) / 40.0, 0)
        seeings += np.where(cloud_cover > 50, 0.3, 0)
        return np.clip(seeings, 0.5, 5.0)
