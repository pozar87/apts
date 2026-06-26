import math
from typing import TYPE_CHECKING, Any, Optional, cast

import numpy as np

if TYPE_CHECKING:
    from skyfield.api import Time
    from ..weather import Weather
    from apts.light_pollution import LightPollution

from ..utils import get_scalar_datetime


class SqmMixIn:
    if TYPE_CHECKING:
        light_pollution: Optional["LightPollution"]
        date: "Time"
        observer: Any
        sun: Any
        moon: Any
        weather: Optional["Weather"]

        def get_light_pollution(self) -> float: ...
        def _ensure_light_pollution(self) -> None: ...

    def get_sqm(self, time: Optional[Any] = None) -> float:
        """
        Returns the approximate SQM value for the place based on its base light pollution,
        accounting for Sun, Moon, and cloud cover if weather data is available.
        """
        target_time = time if time is not None else self.date

        bortle = self.get_light_pollution()
        if bortle <= 0:
            return 0.0

        self._ensure_light_pollution()
        from apts.light_pollution import LightPollution

        sqm_base = cast(LightPollution, self.light_pollution).get_base_sqm(
            forced_bortle=bortle
        )

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
            from ...place import get_planet_magnitude as _get_planet_magnitude

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

        bortle = self.get_light_pollution()
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

    def _calculate_bulk_sqm(
        self,
        sun_alts: np.ndarray,
        moon_alts: np.ndarray,
        moon_mags: np.ndarray,
    ) -> np.ndarray:
        """
        Internal vectorized SQM calculation.
        """
        if self.weather is None or self.weather.data is None:
            return np.array([])

        bortle = self.get_light_pollution()
        self._ensure_light_pollution()
        from apts.light_pollution import LightPollution

        sqm_base = cast(LightPollution, self.light_pollution).get_base_sqm(
            forced_bortle=bortle
        )

        b_starlight = 10 ** (-0.4 * sqm_base)

        # Vectorized SQM Calculation
        b_total = cast(np.ndarray, np.full(len(sun_alts), b_starlight))

        # Sun contribution
        sun_mask = sun_alts > -18
        if np.any(sun_mask):
            b_sun = 10 ** (-0.4 * (21.8 - (18 + sun_alts[sun_mask]) * 0.65))
            b_total[sun_mask] += b_sun

        # Moon contribution
        moon_mask = moon_alts > 0
        if np.any(moon_mask):
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
        return np.clip(sqms, 10.0, 22.0)
