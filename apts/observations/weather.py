import logging
from typing import Optional

import numpy as np
import pandas as pd

from ..conditions import Conditions
from ..i18n import language_context
from ..utils.planetary import get_moon_illumination

logger = logging.getLogger(__name__)


class WeatherAnalysisMixIn:
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
            self.place.get_weather(
                provider_name=provider_name,
                conditions=effective_conditions,
                observation_window=(self.start, self.stop),
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
        if conditions is None and self._weather_analysis is not None:
            return self._weather_analysis

        effective_conditions = conditions or self.conditions
        # Force a minimal check for is_moon_condition_met to allow it returning reasons later if needed,
        # but the current logic is to early-exit.

        if not force and not self._is_moon_condition_met(effective_conditions):
            logger.info("Skipping weather analysis due to moon condition.")
            return []

        if self.place.weather is None:
            self.place.get_weather(
                provider_name=provider_name,
                conditions=effective_conditions,
                observation_window=(self.start, self.stop),
                force=force,
            )
            if not force and not self._is_moon_condition_met(effective_conditions):
                logger.info("Skipping weather analysis due to moon condition.")
                return []

            if self.place.weather is None:
                logger.warning("Weather data unavailable after fetch attempt.")
                return []

        if not all([self.start, self.stop]):
            logger.warning("Observation window (start, stop) is not fully defined.")
            return []

        hourly_data = self.place.weather.get_critical_data(self.start, self.stop)
        if hourly_data.empty:
            return []

        # Filter by time limit if defined
        # Ensure we use aware comparison
        if self.time_limit is not None:
            t_limit = pd.Timestamp(self.time_limit)
            if t_limit.tzinfo is None:
                t_limit = t_limit.tz_localize(self.place.local_timezone)

            hourly_data = hourly_data[hourly_data.time <= t_limit].copy()
        else:
            hourly_data = hourly_data.copy()

        if "fog" not in hourly_data.columns:
            hourly_data["fog"] = 0
        if "aurora" not in hourly_data.columns:
            hourly_data["aurora"] = 0
        if "precipIntensity" not in hourly_data.columns:
            hourly_data["precipIntensity"] = 0
        if "precipProbability" not in hourly_data.columns:
            hourly_data["precipProbability"] = 0
        if "cloudCover" not in hourly_data.columns:
            hourly_data["cloudCover"] = 0
        if "windSpeed" not in hourly_data.columns:
            hourly_data["windSpeed"] = 0
        if "temperature" not in hourly_data.columns:
            hourly_data["temperature"] = 20
        if "visibility" not in hourly_data.columns:
            hourly_data["visibility"] = 20
        if "moonIllumination" not in hourly_data.columns:
            hourly_data["moonIllumination"] = 0
        if "seeing" not in hourly_data.columns:
            hourly_data["seeing"] = 1.5
        if "sqm" not in hourly_data.columns:
            hourly_data["sqm"] = 21.0

        # Calculate moon altitudes exactly for each weather data point if not already cached
        if (
            "moon_altitude" in hourly_data.columns
            and not hourly_data["moon_altitude"].isna().all()
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

        for col in [
            "cloudCover",
            "precipProbability",
            "precipIntensity",
            "windSpeed",
            "temperature",
            "visibility",
            "moonIllumination",
            "fog",
            "aurora",
            "seeing",
            "sqm",
        ]:
            if col in hourly_data.columns:
                hourly_data[col] = pd.to_numeric(hourly_data[col], errors="coerce")

        effective_conditions = conditions or self.conditions
        with language_context(language):
            from ..i18n import gettext_

            # Vectorized condition checks
            is_bad_clouds = hourly_data.cloudCover.isna() | (
                hourly_data.cloudCover > effective_conditions.max_clouds
            )
            is_bad_precip_prob = hourly_data.precipProbability.isna() | (
                hourly_data.precipProbability
                > effective_conditions.max_precipitation_probability
            )
            is_bad_precip_intens = hourly_data.precipIntensity.isna() | (
                hourly_data.precipIntensity
                > effective_conditions.max_precipitation_intensity
            )
            is_bad_wind = hourly_data.windSpeed.isna() | (
                hourly_data.windSpeed > effective_conditions.max_wind
            )
            is_bad_temp = hourly_data.temperature.isna() | (
                (effective_conditions.min_temperature > hourly_data.temperature)
                | (hourly_data.temperature > effective_conditions.max_temperature)
            )
            is_bad_vis = hourly_data.visibility.isna() | (
                hourly_data.visibility < effective_conditions.min_visibility
            )
            is_bad_fog = hourly_data.fog.isna() | (
                hourly_data.fog > effective_conditions.max_fog
            )
            is_bad_moon = (hourly_data["Altitude"] > 0) & (
                hourly_data.moonIllumination
                > effective_conditions.max_moon_illumination
            )
            is_bad_aurora = hourly_data.aurora.isna() | (
                hourly_data.aurora < effective_conditions.min_aurora
            )
            is_bad_seeing = hourly_data.seeing.isna() | (
                hourly_data.seeing > effective_conditions.max_seeing
            )
            is_bad_sqm = hourly_data.sqm.isna() | (
                hourly_data.sqm < effective_conditions.min_sqm
            )

            # Determine good hours
            is_good_hour_mask = ~(
                is_bad_clouds
                | is_bad_precip_prob
                | is_bad_precip_intens
                | is_bad_wind
                | is_bad_temp
                | is_bad_vis
                | is_bad_fog
                | is_bad_moon
                | is_bad_aurora
                | is_bad_seeing
                | is_bad_sqm
            )

            # Pre-populate analysis_results with vectorized data
            hourly_data["is_good_hour"] = is_good_hour_mask
            # Initialize reasons with empty lists
            # Note: We use a list of empty lists because objects in Series are slow to update individually
            reasons_col = [[] for _ in range(len(hourly_data))]

            # Only iterate over "bad" hours to generate reason strings (optimization)
            bad_indices = np.where(~is_good_hour_mask)[0]
            if len(bad_indices) > 0:
                # Convert only bad rows to dict for much faster access than iloc in loop
                bad_rows = hourly_data.iloc[bad_indices].to_dict("records")
                for i, row in enumerate(bad_rows):
                    idx = bad_indices[i]
                    reasons = []
                    if is_bad_clouds.iloc[idx]:
                        reasons.append(
                            gettext_(
                                "Cloud cover %(cloud_cover)s%% exceeds limit of %(max_clouds)s%%"
                            )
                            % {
                                "cloud_cover": f"{row['cloudCover']:.1f}",
                                "max_clouds": effective_conditions.max_clouds,
                            }
                        )
                    if is_bad_precip_prob.iloc[idx]:
                        reasons.append(
                            gettext_(
                                "Precipitation probability %(precip_prob)s%% exceeds limit of %(max_precip_prob)s%%"
                            )
                            % {
                                "precip_prob": f"{row['precipProbability']:.1f}",
                                "max_precip_prob": effective_conditions.max_precipitation_probability,
                            }
                        )
                    if is_bad_precip_intens.iloc[idx]:
                        reasons.append(
                            gettext_(
                                "Precipitation intensity %(precip_intens)s mm exceeds limit of %(max_precip_intens)s mm"
                            )
                            % {
                                "precip_intens": f"{row['precipIntensity']:.1f}",
                                "max_precip_intens": effective_conditions.max_precipitation_intensity,
                            }
                        )
                    if is_bad_wind.iloc[idx]:
                        reasons.append(
                            gettext_(
                                "Wind speed %(wind_speed)s km/h exceeds limit of %(max_wind)s km/h"
                            )
                            % {
                                "wind_speed": f"{row['windSpeed']:.1f}",
                                "max_wind": effective_conditions.max_wind,
                            }
                        )
                    if is_bad_temp.iloc[idx]:
                        reasons.append(
                            gettext_(
                                "Temperature %(temp)s°C out of range (%(min_temp)s - %(max_temp)s°C)"
                            )
                            % {
                                "temp": f"{row['temperature']:.1f}",
                                "min_temp": effective_conditions.min_temperature,
                                "max_temp": effective_conditions.max_temperature,
                            }
                        )
                    if is_bad_vis.iloc[idx]:
                        reasons.append(
                            gettext_(
                                "Visibility %(vis)s km below limit of %(min_vis)s km"
                            )
                            % {
                                "vis": f"{row['visibility']:.1f}",
                                "min_vis": effective_conditions.min_visibility,
                            }
                        )
                    if is_bad_fog.iloc[idx]:
                        reasons.append(
                            gettext_("Fog %(fog)s%% exceeds limit of %(max_fog)s%%")
                            % {
                                "fog": f"{row['fog']:.1f}",
                                "max_fog": effective_conditions.max_fog,
                            }
                        )
                    if is_bad_moon.iloc[idx]:
                        reasons.append(
                            gettext_(
                                "Moon illumination %(illum)s%% exceeds limit of %(max_illum)s%% while moon is up"
                            )
                            % {
                                "illum": f"{row['moonIllumination']:.1f}",
                                "max_illum": effective_conditions.max_moon_illumination,
                            }
                        )
                    if is_bad_aurora.iloc[idx]:
                        reasons.append(
                            gettext_(
                                "Aurora %(aurora)s%% below limit of %(min_aurora)s%%"
                            )
                            % {
                                "aurora": f"{row['aurora']:.1f}",
                                "min_aurora": effective_conditions.min_aurora,
                            }
                        )
                    if is_bad_seeing.iloc[idx]:
                        reasons.append(
                            gettext_(
                                "Seeing %(seeing)s arcsec exceeds limit of %(max_seeing)s arcsec"
                            )
                            % {
                                "seeing": f"{row['seeing']:.1f}",
                                "max_seeing": effective_conditions.max_seeing,
                            }
                        )
                    if is_bad_sqm.iloc[idx]:
                        reasons.append(
                            gettext_(
                                "Sky brightness %(sqm)s mag/arcsec² below limit of %(min_sqm)s mag/arcsec²"
                            )
                            % {
                                "sqm": f"{row['sqm']:.1f}",
                                "min_sqm": effective_conditions.min_sqm,
                            }
                        )
                    reasons_col[idx] = reasons

            hourly_data["reasons"] = reasons_col

            # Rename columns to match expected output dictionary keys
            rename_map = {
                "cloudCover": "clouds",
                "precipProbability": "precipitation",
                "precipIntensity": "precipitation_intensity",
                "windSpeed": "wind_speed",
                "moonIllumination": "moon_illumination",
            }
            # Select and rename columns for the final result
            final_cols = [
                "time",
                "is_good_hour",
                "reasons",
                "temperature",
                "cloudCover",
                "precipProbability",
                "precipIntensity",
                "windSpeed",
                "visibility",
                "moonIllumination",
                "fog",
                "aurora",
                "seeing",
                "sqm",
            ]
            result_df = hourly_data[final_cols].rename(columns=rename_map)
            analysis_results = result_df.to_dict("records")
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
