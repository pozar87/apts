import numpy as np
import pandas as pd
import logging
import datetime
from skyfield.api import Time
from .constants import FilterStrategy, ObjectTableLabels
from .cache import get_cached_score, set_cached_score

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

    def score_altitude(self, altitude):
        """
        S_alt: Altitude score (Max 30 pts)
        ≥65°: 30pts; ≥50°: 25pts; ≥35°: 18pts; ≥20°: 10pts
        """
        if altitude >= 65:
            return 30
        elif altitude >= 50:
            return 25
        elif altitude >= 35:
            return 18
        elif altitude >= 20:
            return 10
        else:
            return 0

    def score_imaging_window(self, window_minutes):
        """
        S_win: Imaging Window score (Max 20 pts)
        Time >30° alt. ≥5h: 20pts; ≥3h: 16pts; ≥2h: 12pts; ≥1h: 8pts
        """
        hours = window_minutes / 60.0
        if hours >= 5:
            return 20
        elif hours >= 3:
            return 16
        elif hours >= 2:
            return 12
        elif hours >= 1:
            return 8
        else:
            return 0

    def score_fov_fit(self, fov_ratio):
        """
        S_fov: FOV Fit score (Max 30 pts)
        30%-110%: 30pts; 10%-200%: 18pts
        """
        if 30 <= fov_ratio <= 110:
            return 30
        elif 10 <= fov_ratio <= 200:
            return 18
        else:
            return 0

    def score_moon_penalty(self, moon_separation):
        """
        S_moon: Moon Penalty score (Max 20 pts)
        NB Mode: 20pts (Static)
        BB Mode: max(0, 20 - (Dist_moon * 0.22))
        """
        if self.filter_strategy == FilterStrategy.NARROWBAND:
            return 20
        else:
            return max(0, 20 - (moon_separation * 0.22))

    def score_brightness(self, magnitude):
        """
        S_bright: Brightness score (Max 10 pts)
        Mag < 5: 10pts; 5.0-7.9: 7pts; 8.0-10.9: 4pts; ≥11: 1pt
        """
        if magnitude < 5:
            return 10
        elif magnitude < 8:
            return 7
        elif magnitude < 11:
            return 4
        else:
            return 1

    def calculate_total_score(self, target_row, time=None):
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
        scorer_id = hash((self.place.lat_decimal, self.place.lon_decimal, self.equipment_path.label(), self.filter_strategy))
        object_id = target_row.get("Name") or target_row.get("Messier") or target_row.get("NGC")
        timestamp = time.tt

        cached_result = get_cached_score(scorer_id, object_id, timestamp)
        if cached_result is not None:
            return cached_result

        # Get values from target_row
        try:
            # 1. Altitude
            skyfield_obj = target_row.get("skyfield_object")
            if pd.isna(skyfield_obj) or skyfield_obj is None:
                # Try to reconstruct if missing
                from .objects.objects import Objects
                if pd.isna(target_row["ra_hours"]) or pd.isna(target_row["dec_degrees"]):
                    return None
                skyfield_obj = Objects.fixed_body(target_row["ra_hours"], target_row["dec_degrees"])

            altitude = self.place.get_altitude(skyfield_obj, time)
            s_alt = self.score_altitude(altitude)

            # 2. Imaging Window
            window_info = self.place.get_imaging_window(skyfield_obj, target_date=time)
            s_win = self.score_imaging_window(window_info["total_minutes"])

            # 3. FOV Fit
            from .optics.utils import OpticsUtils
            object_size = (target_row[ObjectTableLabels.SIZE_MAJOR], target_row[ObjectTableLabels.SIZE_MINOR])
            # Handle NaNs in object size
            if pd.isna(object_size[0]):
                s_fov = 0
            else:
                sensor_size = (
                    self.equipment_path.output.sensor_width.to("mm").magnitude,
                    self.equipment_path.output.sensor_height.to("mm").magnitude
                )
                focal_length = (self.equipment_path.telescope.focal_length * self.equipment_path.effective_barlow()).to("mm").magnitude
                fov_ratio = OpticsUtils.calculate_fov_ratio(object_size, sensor_size, focal_length)
                s_fov = self.score_fov_fit(fov_ratio)

            # 4. Moon Penalty
            from .utils.planetary import get_moon_separation
            moon_sep = get_moon_separation(skyfield_obj, self.place.observer, time)
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
                "window_minutes": window_info["total_minutes"],
                "moon_separation": moon_sep
            }
            set_cached_score(scorer_id, object_id, timestamp, result)
            return result
        except Exception as e:
            logger.error(f"Error calculating score for target {object_id}: {e}")
            return None
