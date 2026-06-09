import datetime
import logging
from typing import Optional, Any

import numpy as np
import pandas as pd

from ..cache import get_cached_score, set_cached_score
from ..constants import FilterStrategy, ObjectTableLabels
from .rules import ALTITUDE_RULE, WINDOW_RULE, FOV_RULE, BRIGHTNESS_RULE, MOON_RULE

logger = logging.getLogger(__name__)


class SuitabilityScorer:
    """
    Multi-Factor Scoring Engine for astrophotography targets.
    Aggregates five distinct metrics into a normalized score (0…110 points).
    """

    def __init__(self, place, equipment_path, filter_strategy=FilterStrategy.BROADBAND):
        self.place = place
        self.equipment_path = equipment_path
        self.filter_strategy = filter_strategy

    def score_altitude(self, altitude: float) -> int:
        """S_alt: Altitude score (Max 30 pts)"""
        return ALTITUDE_RULE.score(altitude)

    def score_imaging_window(self, window_minutes: float) -> int:
        """S_win: Imaging Window score (Max 20 pts)"""
        return WINDOW_RULE.score(window_minutes / 60.0)

    def score_fov_fit(self, fov_ratio: float) -> int:
        """S_fov: FOV Fit score (Max 30 pts)"""
        return FOV_RULE.score(fov_ratio)

    def score_moon_penalty(self, moon_separation: float) -> float:
        """S_moon: Moon Penalty score (Max 20 pts)"""
        return MOON_RULE.score(
            moon_separation, self.filter_strategy == FilterStrategy.NARROWBAND
        )

    def score_brightness(self, magnitude: float) -> int:
        """S_bright: Brightness score (Max 10 pts)"""
        return BRIGHTNESS_RULE.score(magnitude)

    def calculate_scores_bulk(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Vectorized calculation of scores for a DataFrame of targets.
        """
        alt = df[ObjectTableLabels.ALTITUDE].to_numpy()
        s_alt = ALTITUDE_RULE.score_bulk(alt)

        hours = df["window_minutes"].to_numpy() / 60.0
        s_win = WINDOW_RULE.score_bulk(hours)

        fov = df["fov_ratio"].to_numpy()
        s_fov = FOV_RULE.score_bulk(fov)

        moon_sep = df["moon_separation"].to_numpy()
        s_moon = MOON_RULE.score_bulk(
            moon_sep, self.filter_strategy == FilterStrategy.NARROWBAND
        )

        mag = df["Magnitude_float"].to_numpy()
        s_bright = BRIGHTNESS_RULE.score_bulk(mag)

        total_score = s_alt + s_win + s_fov + s_moon + s_bright

        return pd.DataFrame(
            {
                "total_score": total_score,
                "s_alt": s_alt,
                "s_win": s_win,
                "s_fov": s_fov,
                "s_moon": s_moon,
                "s_bright": s_bright,
                "altitude": alt,
                "window_minutes": df["window_minutes"].to_numpy(),
                "moon_separation": moon_sep,
            },
            index=df.index,
        )

    def _get_skyfield_obj(self, target_row: Any):
        """Helper to get or reconstruct Skyfield object from target row."""
        skyfield_obj = target_row.get("skyfield_object")
        if pd.notna(skyfield_obj) and skyfield_obj is not None:
            return skyfield_obj

        from ..objects import Objects

        if pd.isna(target_row["ra_hours"]) or pd.isna(target_row["dec_degrees"]):
            return None

        return Objects.fixed_body(target_row["ra_hours"], target_row["dec_degrees"])

    def _get_altitude_for_scoring(
        self, target_row: Any, skyfield_obj: Any, time: Any
    ) -> Optional[float]:
        """Helper to retrieve altitude for scoring."""
        if ObjectTableLabels.ALTITUDE in target_row and pd.notna(
            target_row[ObjectTableLabels.ALTITUDE]
        ):
            return float(target_row[ObjectTableLabels.ALTITUDE])

        if skyfield_obj is None:
            return None

        return self.place.get_altitude(skyfield_obj, time)

    def _get_window_for_scoring(
        self, target_row: Any, skyfield_obj: Any, time: Any, twilight_times: Any
    ) -> Optional[float]:
        """Helper to retrieve imaging window for scoring."""
        if "window_minutes" in target_row and pd.notna(target_row["window_minutes"]):
            return float(target_row["window_minutes"])

        if skyfield_obj is None:
            return None

        twilight_start = twilight_times[0] if twilight_times else None
        twilight_end = twilight_times[1] if twilight_times else None

        window_info = self.place.get_imaging_window(
            skyfield_obj,
            target_date=time,
            astro_twilight_start=twilight_start,
            astro_twilight_end=twilight_end,
        )
        return window_info["total_minutes"]

    def _get_fov_ratio_for_scoring(self, target_row: Any) -> Optional[float]:
        """Helper to calculate FOV ratio for scoring."""
        object_size = (
            target_row[ObjectTableLabels.SIZE_MAJOR],
            target_row[ObjectTableLabels.SIZE_MINOR],
        )
        # Handle NaNs in object size
        if pd.isna(object_size[0]):
            return None

        from ..optics.utils import OpticsUtils

        sensor_size = (
            self.equipment_path.output.sensor_width.to("mm").magnitude,
            self.equipment_path.output.sensor_height.to("mm").magnitude,
        )
        focal_length = (
            (
                self.equipment_path.telescope.focal_length
                * self.equipment_path.effective_barlow()
            )
            .to("mm")
            .magnitude
        )
        return OpticsUtils.calculate_fov_ratio(object_size, sensor_size, focal_length)

    def _get_moon_sep_for_scoring(
        self, target_row: Any, skyfield_obj: Any, time: Any
    ) -> Optional[float]:
        """Helper to retrieve moon separation for scoring."""
        if "moon_separation" in target_row and pd.notna(target_row["moon_separation"]):
            return float(target_row["moon_separation"])

        if skyfield_obj is None:
            return None

        from ..utils.planetary import get_moon_separation

        return get_moon_separation(skyfield_obj, self.place.observer, time)

    def calculate_total_score(
        self, target_row: Any, time: Any = None, twilight_times: Any = None
    ):
        """
        Calculate total score for a target given its data row and observation time.
        """
        if time is None:
            time = self.place.date

        # Ensure time is a scalar Skyfield Time object for scoring
        ts = self.place.ts
        if hasattr(time, "shape") and time.shape:
            # If it's an array Time, take the first element
            time = time[0]
        elif isinstance(time, (datetime.datetime, datetime.date)):
            time = ts.utc(time)

        # Attempt to get from cache first
        scorer_id = hash(
            (
                self.place.lat_decimal,
                self.place.lon_decimal,
                self.equipment_path.label(),
                self.filter_strategy,
            )
        )
        object_id = (
            target_row.get("Name") or target_row.get("Messier") or target_row.get("NGC")
        )
        timestamp = time.tt

        cached_result = get_cached_score(scorer_id, object_id, timestamp)
        if cached_result is not None:
            return cached_result

        # Resolve Skyfield object once to be used by multiple helpers
        skyfield_obj = self._get_skyfield_obj(target_row)

        # Get values from target_row
        try:
            # 1. Altitude
            altitude = self._get_altitude_for_scoring(target_row, skyfield_obj, time)
            if altitude is None:
                return None
            s_alt = self.score_altitude(altitude)

            # 2. Imaging Window
            total_minutes = self._get_window_for_scoring(
                target_row, skyfield_obj, time, twilight_times
            )
            if total_minutes is None:
                return None
            s_win = self.score_imaging_window(total_minutes)

            # 3. FOV Fit
            fov_ratio = self._get_fov_ratio_for_scoring(target_row)
            s_fov = self.score_fov_fit(fov_ratio) if fov_ratio is not None else 0

            # 4. Moon Penalty
            moon_sep = self._get_moon_sep_for_scoring(target_row, skyfield_obj, time)
            if moon_sep is None:
                return None
            s_moon = self.score_moon_penalty(moon_sep)

            # 5. Brightness
            magnitude = target_row["Magnitude_float"]
            s_bright = self.score_brightness(magnitude)

            total_score = s_alt + s_win + s_fov + s_moon + s_bright

            result = {
                "total_score": total_score,
                "s_alt": s_alt,
                "s_win": s_win,
                "s_fov": s_fov,
                "s_moon": s_moon,
                "s_bright": s_bright,
                "altitude": altitude,
                "window_minutes": total_minutes,
                "moon_separation": moon_sep,
            }
            set_cached_score(scorer_id, object_id, timestamp, result)
            return result
        except Exception as e:
            logger.error(f"Error calculating score for target {object_id}: {e}")
            return None
