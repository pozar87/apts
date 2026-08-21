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
from .calculations import (
    calculate_moon_altitudes,
    check_moon_condition,
    compute_weather_goodness_ratio,
    prepare_weather_dataframe,
)
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
        Delegates calculations to compute_weather_goodness_ratio.
        """
        effective_conditions = conditions or self.conditions
        if conditions is None and self._weather_analysis is not None:
            return compute_weather_goodness_ratio(
                pd.DataFrame(),
                effective_conditions,
                cached_analysis=self._weather_analysis,
            )

        hourly_data = self._get_prepared_weather_df()
        return compute_weather_goodness_ratio(hourly_data, effective_conditions)

    def _is_moon_condition_met(self, conditions: Conditions) -> bool:
        """Delegates moon condition evaluation to check_moon_condition."""
        return check_moon_condition(
            self.start,
            self.stop,
            self.place,
            conditions,
            effective_date=self.effective_date,
            get_moon_illumination_fn=get_moon_illumination,
        )

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

        alts = calculate_moon_altitudes(self.place, hourly_data["time"].tolist())
        alts.index = hourly_data.index
        return alts

    def _get_prepared_weather_df(self) -> pd.DataFrame:
        """Retrieves and prepares the weather DataFrame for analysis using prepare_weather_dataframe."""
        return prepare_weather_dataframe(
            self.place, self.start, self.stop, time_limit=self.time_limit
        )

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
