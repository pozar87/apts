import logging
from datetime import datetime
from typing import TYPE_CHECKING, Optional, Union, cast

import pandas as pd

if TYPE_CHECKING:
    from skyfield.api import Time

    from ...conditions import Conditions
    from ...place import Place

from ...conditions import Conditions
from ...utils.planetary import get_moon_illumination
from .constants import DEFAULT_WEATHER_VALUES
from .engine import compute_condition_masks, generate_analysis_records

logger = logging.getLogger(__name__)


class WeatherAnalysisMixIn:
    if TYPE_CHECKING:
        start: Optional[datetime]
        stop: Optional[datetime]
        place: Place
        conditions: Conditions
        effective_date: Optional[Union[datetime, "Time"]]
        time_limit: Optional[datetime]
        _weather_analysis: Optional[list[dict]]

    def _compute_weather_goodness(self, conditions: Optional[Conditions] = None):
        """
        Calculates the percentage of good observation hours within the window.
        Uses a fast-path if detailed analysis isn't already cached.
        """
        # 1. If we already have a cached analysis, use it.
        if conditions is None and self._weather_analysis is not None:
            analysis = self._weather_analysis
            if not analysis:
                return 0
            good_hours = sum(1 for hour in analysis if hour["is_good_hour"])
            all_hours = len(analysis)
            return (good_hours / all_hours * 100) if all_hours > 0 else 0

        # 2. Fast-path: calculate goodness ratio without generating detailed records.
        effective_conditions = conditions or self.conditions
        hourly_data = self._get_prepared_weather_df()

        if hourly_data.empty:
            return 0

        from .engine import get_good_hour_mask

        is_good_mask = get_good_hour_mask(hourly_data, effective_conditions)
        good_hours = is_good_mask.sum()
        all_hours = len(is_good_mask)

        logger.debug("Good hours: {} and all hours: {}".format(good_hours, all_hours))

        return (good_hours / all_hours * 100) if all_hours > 0 else 0

    def _is_moon_condition_met(self, conditions: Conditions) -> bool:
        if not self.start or not self.stop:
            return True

        # Use effective_date for moon illumination if available, otherwise fallback to place.date.
        # We avoid using 'or' here because Skyfield Time objects can raise TypeError when evaluated in boolean context.
        date_for_illumination = (
            self.effective_date if self.effective_date is not None else self.place.date
        )
        moon_illumination = get_moon_illumination(date_for_illumination)
        if moon_illumination <= conditions.max_moon_illumination:
            return True

        # Illumination is too high, check if moon is up during observation window
        ts = self.place.ts
        t0 = ts.from_datetime(self.start)
        t1 = ts.from_datetime(self.stop)
        # Check at 10 points during the observation
        times = ts.linspace(t0, t1, 10)
        alt, _, _ = (
            self.place.observer.at(times).observe(self.place.moon).apparent().altaz()
        )

        # Calculate how much of the time the moon is up
        moon_up_ratio = sum(1 for a in alt.degrees if a > 0) / 10.0
        # If moon is up for more than (100 - min_weather_goodness)% of the time, it's bad
        allowed_bad_ratio = (100 - conditions.min_weather_goodness) / 100.0

        if moon_up_ratio > allowed_bad_ratio:
            logger.info(
                f"Moon condition not met: illumination {moon_illumination:.1f}% "
                f"exceeds {conditions.max_moon_illumination}% and moon is up for "
                f"{moon_up_ratio * 100:.1f}% of the observation window."
            )
            return False

        return True

    def _ensure_weather_data_available(
        self,
        conditions: Conditions,
        provider_name: Optional[str] = None,
        force: bool = False,
    ) -> bool:
        """
        Ensures that weather data is fetched and moon conditions are met.
        Returns True if analysis can proceed, False otherwise.
        """
        if not force and not self._is_moon_condition_met(conditions):
            logger.info("Skipping weather analysis due to moon condition.")
            return False

        if self.place.weather is None:
            obs_window = (
                (self.start, self.stop)
                if self.start is not None and self.stop is not None
                else None
            )
            self.place.get_weather(
                provider_name=provider_name,
                conditions=conditions,
                observation_window=obs_window,
                force=force,
            )
            # Re-check moon condition after potential weather update/fetch
            if not force and not self._is_moon_condition_met(conditions):
                logger.info("Skipping weather analysis due to moon condition.")
                return False

        if self.place.weather is None:
            logger.warning("Weather data unavailable after fetch attempt.")
            return False

        if self.start is None or self.stop is None:
            logger.warning("Observation window (start, stop) is not fully defined.")
            return False

        return True

    def _calculate_moon_altitudes(self, hourly_data: pd.DataFrame) -> pd.Series:
        """Calculates or retrieves moon altitudes for weather data points."""
        if (
            "moon_altitude" in hourly_data.columns
            and not cast(pd.Series, hourly_data["moon_altitude"]).isna().all()
        ):
            return cast(pd.Series, hourly_data["moon_altitude"])

        ts = self.place.ts
        times = ts.from_datetimes(hourly_data["time"].tolist())
        alt, _, _ = (
            self.place.observer.at(times).observe(self.place.moon).apparent().altaz()
        )
        return pd.Series(alt.degrees, index=hourly_data.index)

    def _get_prepared_weather_df(self) -> pd.DataFrame:
        """Retrieves and prepares the weather DataFrame for analysis."""
        if self.place.weather is None or self.start is None or self.stop is None:
            return pd.DataFrame()

        hourly_data = cast(
            pd.DataFrame, self.place.weather.get_critical_data(self.start, self.stop)
        )
        if hourly_data.empty:
            return hourly_data

        # Filter by time limit if defined
        if self.time_limit is not None:
            t_limit = pd.Timestamp(self.time_limit)
            if t_limit.tzinfo is None:
                t_limit = t_limit.tz_localize(self.place.local_timezone)
            hourly_data = cast(
                pd.DataFrame, hourly_data[hourly_data.time <= t_limit].copy()
            )
        else:
            hourly_data = cast(pd.DataFrame, hourly_data.copy())

        # Populate missing columns with default values
        for col, default_val in DEFAULT_WEATHER_VALUES.items():
            if col not in hourly_data.columns:
                hourly_data[col] = default_val

        # Calculate moon altitudes
        hourly_data["Altitude"] = self._calculate_moon_altitudes(hourly_data)

        # Coerce to numeric
        for col in DEFAULT_WEATHER_VALUES.keys():
            hourly_data[col] = pd.to_numeric(hourly_data[col], errors="coerce")

        return hourly_data

    def is_weather_good(
        self,
        conditions: Optional[Conditions] = None,
        provider_name: Optional[str] = None,
        force: bool = False,
    ):
        effective_conditions = conditions or self.conditions
        if not force and not self._is_moon_condition_met(effective_conditions):
            return False

        if force or self.place.weather is None:
            logger.info(
                "is_weather_good: self.place.weather is None, calling get_weather."
            )
            obs_window = (
                (self.start, self.stop)
                if self.start is not None and self.stop is not None
                else None
            )
            self.place.get_weather(
                provider_name=provider_name,
                conditions=effective_conditions,
                observation_window=obs_window,
                force=force,
            )
        else:
            logger.info("is_weather_good: self.place.weather already exists.")

        if force:
            analysis = self.get_weather_analysis(
                conditions=conditions, provider_name=provider_name, force=force
            )
            if not analysis:
                return False
            good_hours = sum(1 for hour in analysis if hour["is_good_hour"])
            return bool(
                (good_hours / len(analysis) * 100)
                >= effective_conditions.min_weather_goodness
            )

        return bool(
            self._compute_weather_goodness(conditions=conditions)
            >= effective_conditions.min_weather_goodness
        )

    def get_weather_analysis(
        self,
        language: Optional[str] = None,
        conditions: Optional[Conditions] = None,
        provider_name: Optional[str] = None,
        force: bool = False,
    ):
        """
        Orchestrates weather analysis for the observation window.
        Decomposed into helper methods for readability and maintainability.
        """
        if not force and conditions is None and self._weather_analysis is not None:
            return self._weather_analysis

        effective_conditions = conditions or self.conditions

        if not self._ensure_weather_data_available(
            effective_conditions, provider_name, force
        ):
            return []

        hourly_data = self._get_prepared_weather_df()
        if hourly_data.empty:
            return []

        masks = compute_condition_masks(hourly_data, effective_conditions)
        analysis_results = generate_analysis_records(
            hourly_data, masks, effective_conditions, language
        )

        if conditions is None:
            self._weather_analysis = analysis_results

        return analysis_results

    def get_hourly_weather_analysis(
        self,
        language: Optional[str] = None,
        conditions: Optional[Conditions] = None,
        provider_name: Optional[str] = None,
        force: bool = False,
    ):
        return self.get_weather_analysis(
            language=language,
            conditions=conditions,
            provider_name=provider_name,
            force=force,
        )
