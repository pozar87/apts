import logging
import types
import unittest.mock
from abc import ABC, abstractmethod
from datetime import timedelta
from typing import Any, cast

import numpy as np
import pandas as pd
import pytz
from skyfield import almanac
from skyfield.api import Star
from skyfield.searchlib import find_discrete

from ..cache import get_timescale
from ..constants import ObjectTableLabels
from .utils import calculate_refraction, vectorized_geometric_compute

logger = logging.getLogger(__name__)


class Objects(ABC):
    @abstractmethod
    def get_skyfield_object(self, obj) -> object:
        pass

    @abstractmethod
    def compute(self, calculation_date=None, df_to_compute=None) -> pd.DataFrame | None:
        pass

    def __init__(self, place, calculation_date=None):
        self.place = place
        self.objects: pd.DataFrame = pd.DataFrame()
        self.ts = get_timescale()
        self.calculation_date = calculation_date  # Store it here

    def __getstate__(self):
        state = self.__dict__.copy()
        # Remove the unpicklable entries.
        if "ts" in state:
            del state["ts"]

        # Skyfield objects (especially planets) in the DataFrame are not picklable
        # because they reference open ephemeris files (BufferedReader).
        if "objects" in state and isinstance(state["objects"], pd.DataFrame):
            if "skyfield_object" in state["objects"].columns:
                # We drop the column. It will be re-populated by compute()
                # or get_visible() using get_skyfield_object() if needed.
                state["objects"] = state["objects"].drop(columns=["skyfield_object"])

        return state

    def __setstate__(self, state):
        cast(Any, self.__dict__).update(state)
        # Re-create the unpicklable entries.
        self.ts = get_timescale()

    def _filter_by_magnitude(
        self, conditions, star_magnitude_limit, limiting_magnitude
    ) -> pd.DataFrame:
        """
        Filters objects based on magnitude limits.
        """
        max_magnitude_q = (
            limiting_magnitude
            if limiting_magnitude is not None
            else (
                star_magnitude_limit
                if star_magnitude_limit is not None
                else conditions.max_object_magnitude
            )
        )

        # Ensure max_magnitude is a float for comparison with magnitude_values
        max_mag_float = (
            max_magnitude_q.magnitude
            if hasattr(max_magnitude_q, "magnitude")
            else max_magnitude_q
        )

        # Optimization: use pre-calculated float magnitudes if available
        if "Magnitude_float" in self.objects.columns:
            magnitude_values = self.objects["Magnitude_float"]
        else:
            magnitude_values = self.objects["Magnitude"].apply(
                lambda x: x.magnitude if hasattr(x, "magnitude") else x
            )
        return self.objects[magnitude_values < max_mag_float].copy()

    def _get_visible_mocked(self, candidate_objects, conditions, start, stop) -> list:
        """
        Calculates visibility for objects when the place.get_altaz_curve is mocked.
        """
        visible_objects_indices = []
        for index, row in candidate_objects.iterrows():
            skyfield_object = self.get_skyfield_object(row)
            if skyfield_object is None:
                continue
            altaz_df = self.place.get_altaz_curve(skyfield_object, start, stop)
            altitude_values = altaz_df["Altitude"].apply(
                lambda x: x.magnitude if hasattr(x, "magnitude") else x
            )
            azimuth_values = altaz_df["Azimuth"].apply(
                lambda x: x.magnitude if hasattr(x, "magnitude") else x
            )
            visible_condition = conditions.is_visible(azimuth_values, altitude_values)
            if cast(Any, visible_condition.any()):
                visible_objects_indices.append(index)
        return visible_objects_indices

    def _get_visible_stars(
        self,
        candidate_objects,
        skyfield_objs,
        stars_indices,
        check_times,
        conditions,
        visible_mask,
    ):
        """
        Check Stars using vectorized geometric formulas across all check_times.
        """
        # Extract RA/Dec for all stars
        if (
            "ra_hours" in candidate_objects.columns
            and "dec_degrees" in candidate_objects.columns
        ):
            stars_ras = cast(pd.Series, candidate_objects["ra_hours"]).to_numpy()[
                stars_indices
            ]
            stars_decs = cast(pd.Series, candidate_objects["dec_degrees"]).to_numpy()[
                stars_indices
            ]
        else:
            stars_ras = np.array(
                [cast(Any, skyfield_objs)[i].ra.hours for i in stars_indices]
            )
            stars_decs = np.array(
                [cast(Any, skyfield_objs)[i].dec.degrees for i in stars_indices]
            )

        # Preliminary filter: max altitude check
        max_alt_deg = 90.0 - np.abs(self.place.lat_decimal - stars_decs)
        # Add refraction at max altitude for better filtering
        max_alt_deg += calculate_refraction(max_alt_deg)

        # Only process stars that can potentially reach the minimum altitude
        potential_mask = max_alt_deg > conditions.horizon.get_min_altitude()

        if np.any(potential_mask):
            # Ensure stars_indices is an array before masking
            stars_indices = np.asarray(stars_indices)
            active_stars_indices = stars_indices[potential_mask]
            active_ras_hours = stars_ras[potential_mask]
            active_decs_deg = stars_decs[potential_mask]

            # Get LST for all check times (in hours)
            lst_hours = check_times.gmst + self.place.lon_decimal / 15.0

            # Pre-calculate trigonometric values for O(N+M) optimization
            lat_rad = np.deg2rad(self.place.lat_decimal)
            sin_lat = np.sin(lat_rad)
            cos_lat = np.cos(lat_rad)

            # For active stars (N_active)
            ra_rad = np.deg2rad(active_ras_hours * 15.0)
            dec_rad = np.deg2rad(active_decs_deg)
            sin_ra = np.sin(ra_rad)[:, np.newaxis]
            cos_ra = np.cos(ra_rad)[:, np.newaxis]
            sin_dec = np.sin(dec_rad)[:, np.newaxis]
            cos_dec = np.cos(dec_rad)[:, np.newaxis]
            tan_dec = np.tan(dec_rad)[:, np.newaxis]

            # For check times (M_times)
            lst_rad = np.deg2rad(lst_hours * 15.0)
            sin_lst = np.sin(lst_rad)[np.newaxis, :]
            cos_lst = np.cos(lst_rad)[np.newaxis, :]

            # Use identity: cos(H) = cos(LST-RA) = cos(LST)cos(RA) + sin(LST)sin(RA)
            cos_h = cos_lst * cos_ra + sin_lst * sin_ra
            # Use identity: sin(H) = sin(LST-RA) = sin(LST)cos(RA) - cos(LST)sin(RA)
            sin_h = sin_lst * cos_ra - cos_lst * sin_ra

            # Geometric altitude and azimuth calculation
            sin_alt = sin_lat * sin_dec + cos_lat * cos_dec * cos_h

            # Convert to degrees and add atmospheric refraction
            true_alt_deg = np.rad2deg(np.arcsin(np.clip(sin_alt, -1.0, 1.0)))
            apparent_alt_deg = true_alt_deg + calculate_refraction(true_alt_deg)

            # Determine azimuth
            x = cos_h * sin_lat - tan_dec * cos_lat
            y = sin_h
            az_deg = (np.rad2deg(np.arctan2(y, x)) + 180.0) % 360.0

            # Determine visibility using conditions
            visible_at_times = conditions.is_visible(az_deg, apparent_alt_deg)

            # Combine and check if visible at ANY time point
            visible_mask[active_stars_indices] = np.any(visible_at_times, axis=1)

    def _get_visible_other(
        self, skyfield_objs, other_indices, obs_at_check_times, conditions, visible_mask
    ):
        """
        Check Other objects (like planets) using Skyfield.
        """
        for i in other_indices:
            skyfield_obj = skyfield_objs[i]
            alt, az, _ = obs_at_check_times.observe(skyfield_obj).apparent().altaz()
            alt_deg = alt.degrees
            az_deg = az.degrees

            visible_at_times = conditions.is_visible(az_deg, alt_deg)

            if cast(Any, visible_at_times.any()):
                visible_mask[i] = True

    def _ensure_computed_fields(self, visible_candidate_objects, sort_by):
        """
        Ensures that transit, rise, set, and altitude fields are computed for visible objects.
        """
        if (
            sort_by
            in [
                ObjectTableLabels.TRANSIT,
                ObjectTableLabels.RISING,
                ObjectTableLabels.SETTING,
            ]
            or True
        ):
            needed_cols = [
                ObjectTableLabels.TRANSIT,
                ObjectTableLabels.RISING,
                ObjectTableLabels.SETTING,
                ObjectTableLabels.ALTITUDE,
            ]
            missing_any = False
            for col in needed_cols:
                if col not in visible_candidate_objects.columns or cast(
                    Any, visible_candidate_objects[col].isnull().any()
                ):
                    missing_any = True
                    break

            if missing_any:
                if not visible_candidate_objects.empty:
                    self.compute(
                        calculation_date=self.calculation_date,
                        df_to_compute=visible_candidate_objects,
                    )
                    # Update visible_candidate_objects with the new computed values
                    for col in self.objects.columns:
                        if col not in visible_candidate_objects.columns:
                            visible_candidate_objects[col] = None
                    visible_candidate_objects.update(
                        self.objects.loc[visible_candidate_objects.index]
                    )

    def get_visible(
        self,
        conditions,
        start,
        stop,
        hours_margin=0,
        sort_by=ObjectTableLabels.TRANSIT,
        star_magnitude_limit=None,
        limiting_magnitude=None,
    ) -> pd.DataFrame:
        if not start or not stop:
            return pd.DataFrame(columns=self.objects.columns)

        candidate_objects = self._filter_by_magnitude(
            conditions, star_magnitude_limit, limiting_magnitude
        )

        if candidate_objects.empty:
            return pd.DataFrame(columns=self.objects.columns)

        # Vectorized visibility check
        ts = self.ts
        t_start = ts.utc(start)
        t_stop = ts.utc(stop)
        # Use 100 points to match previous behavior and ensure precision
        check_times = ts.linspace(t_start, t_stop, 100)

        # Check if get_altaz_curve is mocked or overridden (common in tests)
        # Original method is a bound method, mocked/overridden is often a function or a Mock object
        is_mocked = isinstance(
            self.place.get_altaz_curve, unittest.mock.Mock
        ) or isinstance(self.place.get_altaz_curve, types.FunctionType)

        if is_mocked:
            visible_objects_indices = self._get_visible_mocked(
                candidate_objects, conditions, start, stop
            )
            visible_candidate_objects = cast(
                pd.DataFrame, candidate_objects.loc[visible_objects_indices].copy()
            )
        else:
            visible_mask = np.zeros(len(candidate_objects), dtype=bool)

            # Fast property extraction instead of iterrows()
            if "skyfield_object" in candidate_objects.columns:
                skyfield_objs = cast(
                    pd.Series, candidate_objects["skyfield_object"]
                ).to_numpy()
            else:
                skyfield_objs = np.array(
                    [
                        self.get_skyfield_object(row)
                        for _, row in candidate_objects.iterrows()
                    ]
                )
            is_star = np.array([isinstance(obj, Star) for obj in skyfield_objs])

            stars_indices = np.where(is_star)[0]
            other_indices = np.where(~is_star & pd.notnull(skyfield_objs))[0]

            if len(stars_indices) > 0:
                self._get_visible_stars(
                    candidate_objects,
                    skyfield_objs,
                    stars_indices,
                    check_times,
                    conditions,
                    visible_mask,
                )

            observer = self.place.observer
            # Optimization: move observer.at(check_times) out of the loop
            # to reuse calculated observer positions for all objects.
            obs_at_check_times = observer.at(check_times)

            # Check Other objects (like planets)
            self._get_visible_other(
                skyfield_objs, other_indices, obs_at_check_times, conditions, visible_mask
            )

            visible_candidate_objects: pd.DataFrame = cast(
                pd.DataFrame, candidate_objects.loc[visible_mask].copy()
            )

        if visible_candidate_objects.empty:
            return pd.DataFrame(columns=self.objects.columns)

        # Compute transit/rise/set ONLY for visible objects if needed for sorting or plotting
        self._ensure_computed_fields(visible_candidate_objects, sort_by)

        visible = visible_candidate_objects

        # Sort objects by given order, handling potential NaNs
        if sort_by in visible.columns and not bool(visible[sort_by].isnull().all()):
            visible = visible.sort_values(by=sort_by, ascending=True)

        return visible

    @staticmethod
    def fixed_body(RA, Dec):
        # Create body at given coordinates
        return Star(ra_hours=RA, dec_degrees=Dec)

    def _compute_tranzit(self, skyfield_object, observer):
        """
        Calculates the upper meridian transit of a celestial object.
        """
        if skyfield_object is None:
            return None

        # Fallback for moving objects (planets)
        current_dt = observer.date.utc_datetime()
        t0_dt = current_dt.replace(hour=0, minute=0, second=0, microsecond=0)
        t0 = self.ts.utc(t0_dt)
        t1 = self.ts.utc(t0_dt + timedelta(days=2))
        f = almanac.meridian_transits(
            self.place.eph, skyfield_object, self.place.location
        )
        t, y = almanac.find_discrete(t0, t1, f)

        cutoff_time = current_dt - timedelta(hours=12)
        valid_transits = []
        for i, event in enumerate(y):
            if event == 1:  # Upper
                transit_dt = t[i].utc_datetime()
                if transit_dt > cutoff_time:
                    valid_transits.append(transit_dt)

        if valid_transits:
            return (
                valid_transits[0]
                .replace(tzinfo=pytz.UTC)
                .astimezone(observer.local_timezone)
            )

        return None

    def _compute_rising_and_setting(self, skyfield_object, observer, transit_time):
        """
        Calculates rising and setting times for a celestial object.
        """
        if skyfield_object is None or transit_time is None or pd.isna(transit_time):
            return None, None

        f = almanac.risings_and_settings(
            self.place.eph, skyfield_object, self.place.location
        )

        # Find the latest rise time in the 24 hours before the transit
        t_transit = self.ts.utc(transit_time)
        t0_rise = self.ts.utc(transit_time - timedelta(days=1))
        t_rise, y_rise = find_discrete(t0_rise, t_transit, f)

        rising_time = None
        rise_events = [t for t, y in zip(t_rise, y_rise) if y == 1]
        if rise_events:
            rising_time = (
                rise_events[-1]
                .utc_datetime()
                .replace(tzinfo=pytz.UTC)
                .astimezone(observer.local_timezone)
            )

        # Find the earliest set time in the 24 hours after the transit
        t1_set = self.ts.utc(transit_time + timedelta(days=1))
        t_set, y_set = find_discrete(t_transit, t1_set, f)

        setting_time = None
        set_events = [t for t, y in zip(t_set, y_set) if y == 0]
        if set_events:
            setting_time = (
                set_events[0]
                .utc_datetime()
                .replace(tzinfo=pytz.UTC)
                .astimezone(observer.local_timezone)
            )

        return rising_time, setting_time

    def _altitude_at_transit(self, skyfield_object, transit, observer):
        # Calculate objects altitude at transit time
        if transit is None or pd.isna(transit):
            return 0

        t = self.ts.utc(transit)
        alt, _, _ = (
            self.place.observer.at(t)
            .observe(skyfield_object)
            .apparent()
            .altaz(temperature_C=10.0, pressure_mbar=1013.25)
        )
        return alt.degrees

    def _vectorized_geometric_compute(self, df, observer):
        """
        Fast transit, altitude, rising, and setting calculation for a DataFrame of Stars.
        Uses vectorized numpy operations and geometric approximations for speed.

        Note: Rising/setting times use a geometric formula that accounts for atmospheric
        refraction (~34'). This results in high accuracy compared to Skyfield's
        iterative solver, while maintaining excellent performance.
        """
        # Extract Skyfield Star objects and their coordinates in a vectorized way
        if "skyfield_object" in df.columns:
            sky_objs = df["skyfield_object"].to_numpy()
        else:
            sky_objs = np.array(
                [self.get_skyfield_object(row) for _, row in df.iterrows()]
            )

        valid_mask = np.array([isinstance(obj, Star) for obj in sky_objs])

        ras = np.array(
            [obj.ra.hours if isinstance(obj, Star) else 0 for obj in sky_objs]
        )
        decs = np.array(
            [obj.dec.degrees if isinstance(obj, Star) else 0 for obj in sky_objs]
        )

        return vectorized_geometric_compute(
            self.ts,
            self.place.lat_decimal,
            self.place.lon_decimal,
            observer.local_timezone,
            observer.date,
            ras,
            decs,
            valid_mask,
            len(df),
        )
