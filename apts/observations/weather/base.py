import logging
from datetime import datetime
from typing import TYPE_CHECKING, Optional, Union, cast, List, Dict, Any

import pandas as pd

if TYPE_CHECKING:
    from skyfield.api import Time
    from ...place import Place

from ...conditions import Conditions
from ...i18n import language_context
from ...utils.planetary import get_moon_illumination
from .constants import DEFAULT_WEATHER_VALUES
from .engine import analyze_weather_data

logger = logging.getLogger(__name__)


class WeatherAnalysisMixIn:
    if TYPE_CHECKING:
        start: Optional[datetime]
        stop: Optional[datetime]
        place: "Place"
        conditions: Conditions
        effective_date: Optional[Union[datetime, "Time"]]
        time_limit: Optional[datetime]
        _weather_analysis: Optional[List[Dict[str, Any]]]

    def _compute_weather_goodness(self, conditions: Optional[Conditions] = None):
        analysis = self.get_weather_analysis(conditions=conditions)
        if not analysis:
            return 0

        good_hours = sum(1 for hour in analysis if hour["is_good_hour"])
        all_hours = len(analysis)

        logger.debug("Good hours: {} and all hours: {}".format(good_hours, all_hours))
        if all_hours == 0:
            return 0

        return good_hours / all_hours * 100

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

    def is_weather_good(
        self,
        conditions: Optional[Conditions] = None,
        provider_name: Optional[str] = None,
        force: bool = False,
    ):
        effective_conditions = conditions or self.conditions
        if not force and not self._is_moon_condition_met(effective_conditions):
            return False

        if self.place.weather is None:
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

        return (
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
        if not force and conditions is None and self._weather_analysis is not None:
            return self._weather_analysis

        effective_conditions = conditions or self.conditions
        # Force a minimal check for is_moon_condition_met to allow it returning reasons later if needed,
        # but the current logic is to early-exit.

        if not force and not self._is_moon_condition_met(effective_conditions):
            logger.info("Skipping weather analysis due to moon condition.")
            return []

        if self.place.weather is None:
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
            if not force and not self._is_moon_condition_met(effective_conditions):
                logger.info("Skipping weather analysis due to moon condition.")
                return []

            if self.place.weather is None:
                logger.warning("Weather data unavailable after fetch attempt.")
                return []

        if self.start is None or self.stop is None:
            logger.warning("Observation window (start, stop) is not fully defined.")
            return []

        if self.place.weather is None:
            return []

        hourly_data = cast(
            pd.DataFrame, self.place.weather.get_critical_data(self.start, self.stop)
        )
        if hourly_data.empty:
            return []

        # Filter by time limit if defined
        # Ensure we use aware comparison
        if self.time_limit is not None:
            t_limit = pd.Timestamp(self.time_limit)
            if t_limit.tzinfo is None:
                t_limit = t_limit.tz_localize(self.place.local_timezone)

            hourly_data = cast(
                pd.DataFrame, hourly_data[hourly_data.time <= t_limit].copy()
            )
        else:
            hourly_data = cast(pd.DataFrame, hourly_data.copy())

        # Fill default values
        for col, val in DEFAULT_WEATHER_VALUES.items():
            if col not in hourly_data.columns:
                hourly_data[col] = val

        # Calculate moon altitudes exactly for each weather data point if not already cached
        if (
            "moon_altitude" in hourly_data.columns
            and not cast(pd.Series, hourly_data["moon_altitude"]).isna().all()
        ):
            hourly_data["Altitude"] = hourly_data["moon_altitude"]
        else:
            ts = self.place.ts
            times = ts.from_datetimes(hourly_data["time"].tolist())
            alt, _, _ = (
                self.place.observer.at(times)
                .observe(self.place.moon)
                .apparent()
                .altaz()
            )
            hourly_data["Altitude"] = alt.degrees

        for col in DEFAULT_WEATHER_VALUES.keys():
            if col in hourly_data.columns:
                hourly_data[col] = pd.to_numeric(hourly_data[col], errors="coerce")

        with language_context(language):
            from ...i18n import gettext_

            analysis_results = analyze_weather_data(
                hourly_data, effective_conditions, gettext_
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
