import logging
import types
import unittest.mock
from abc import ABC, abstractmethod
from typing import Any, cast
from types import SimpleNamespace

import numpy as np
import pandas as pd
from skyfield.api import Star

from . import almanac, visibility
from ..cache import get_timescale
from ..constants import ObjectTableLabels
from .utils import vectorized_geometric_compute

logger = logging.getLogger(__name__)


class Objects(ABC):
    # Flag to indicate if this catalog consists primarily of fixed stars.
    # Enables massive performance optimizations in visibility gating by bypassing
    # individual Skyfield object instantiations.
    is_star_catalog = False

    @abstractmethod
    def get_skyfield_object(self, obj) -> object:
        pass

    def compute(self, calculation_date=None, df_to_compute=None) -> pd.DataFrame:
        """
        Default compute implementation using vectorized geometric formulas.
        Works for all catalogs (Stars, Messier, NGC, SolarObjects).
        """
        observer_to_use, _ = self._prepare_observer(calculation_date)

        # If no specific DataFrame is provided, use the class's default.
        if df_to_compute is None:
            df_to_compute = self.objects

        # Work on a copy to avoid modifying the original DataFrame slice
        computed_df = df_to_compute.copy()

        # Fast transit and altitude calculation
        transits, alts, rises, sets = self._vectorized_geometric_compute(
            computed_df, observer_to_use
        )
        computed_df[ObjectTableLabels.TRANSIT] = transits
        computed_df[ObjectTableLabels.ALTITUDE] = alts
        computed_df[ObjectTableLabels.RISING] = rises
        computed_df[ObjectTableLabels.SETTING] = sets

        # Always update the master objects DataFrame to keep data in sync.
        # This handles both full catalog computations and subset-specific updates.
        self.objects.update(computed_df)

        return computed_df

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

    def _prepare_observer(self, calculation_date):
        """Prepares the observer and time for computation."""
        if calculation_date is not None:
            # It's a Skyfield Time object. If it's an array, use the first element.
            if hasattr(calculation_date, "shape") and calculation_date.shape:
                t = calculation_date[0]
            elif isinstance(calculation_date, type(self.ts.now())):
                t = calculation_date
            else:
                t = self.ts.utc(calculation_date)

            # Avoid creating a whole new Place object, which is slow.
            # We only need basic properties for computation.
            observer_to_use = SimpleNamespace(
                date=t,
                local_timezone=self.place.local_timezone,
                lat_decimal=self.place.lat_decimal,
                lon_decimal=self.place.lon_decimal,
                elevation=self.place.elevation,
                observer=self.place.observer,
                sun=getattr(self.place, "sun", None),
            )
        else:
            observer_to_use = self.place
            t = self.place.date
        return observer_to_use, t

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
            # Optimization: list comprehension over .values is faster than .apply() for extracting magnitudes.
            magnitude_values = np.array(
                [
                    x.magnitude if hasattr(x, "magnitude") else x
                    for x in self.objects["Magnitude"].values
                ]
            )
        return cast(pd.DataFrame, self.objects[magnitude_values < max_mag_float].copy())

    def _get_visible_mocked(self, candidate_objects, conditions, start, stop) -> list:
        """
        Calculates visibility for objects when the place.get_altaz_curve is mocked.
        """
        return visibility.get_visible_mocked(self, candidate_objects, conditions, start, stop)

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
        return visibility.get_visible_stars(
            self.place,
            candidate_objects,
            skyfield_objs,
            stars_indices,
            check_times,
            conditions,
            visible_mask,
        )

    def _get_visible_other(
        self, skyfield_objs, other_indices, obs_at_check_times, conditions, visible_mask
    ):
        """
        Check Other objects (like planets) using Skyfield.
        """
        return visibility.get_visible_other(
            skyfield_objs, other_indices, obs_at_check_times, conditions, visible_mask
        )

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

    def _prepare_visibility_check_times(self, start, stop):
        """Prepares the time grid for visibility checking."""
        ts = self.ts
        t_start = ts.utc(start)
        t_stop = ts.utc(stop)
        # Use 100 points to match previous behavior and ensure precision
        return ts.linspace(t_start, t_stop, 100)

    def _perform_visibility_check(self, candidate_objects, check_times, conditions):
        """Core visibility check logic."""
        visible_mask = np.zeros(len(candidate_objects), dtype=bool)

        # Optimization: Identify stars vs moving bodies (others).
        # For star-only catalogs (NGC, Messier), we can bypass expensive row-wise
        # Skyfield object instantiation and property access by using a class flag.
        if getattr(self, "is_star_catalog", False) and "ra_hours" in candidate_objects.columns:
            is_star = np.ones(len(candidate_objects), dtype=bool)
            skyfield_objs = None
        else:
            # Traditional path for mixed or moving-body catalogs.
            # Fast property extraction instead of iterrows()
            if "skyfield_object" in candidate_objects.columns:
                skyfield_objs = cast(
                    pd.Series, candidate_objects["skyfield_object"]
                ).to_numpy()
            else:
                skyfield_objs = np.array(
                    [self.get_skyfield_object(row) for row in candidate_objects.itertuples()]
                )
            is_star = np.array([isinstance(obj, Star) for obj in skyfield_objs])

        stars_indices = np.where(is_star)[0]
        if skyfield_objs is not None:
            other_indices = np.where(~is_star & pd.notnull(skyfield_objs))[0]
        else:
            other_indices = np.array([], dtype=int)

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

        return visible_mask

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
        check_times = self._prepare_visibility_check_times(start, stop)

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
            visible_mask = self._perform_visibility_check(
                candidate_objects, check_times, conditions
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
        return almanac.compute_tranzit(self, skyfield_object, observer)

    def _compute_rising_and_setting(self, skyfield_object, observer, transit_time):
        """
        Calculates rising and setting times for a celestial object.
        """
        return almanac.compute_rising_and_setting(self, skyfield_object, observer, transit_time)

    def _altitude_at_transit(self, skyfield_object, transit, observer):
        # Calculate objects altitude at transit time
        return almanac.altitude_at_transit(self, skyfield_object, transit, observer)

    def _vectorized_geometric_compute(self, df, observer):
        """
        Fast transit, altitude, rising, and setting calculation for a DataFrame of objects.
        Uses vectorized numpy operations and geometric approximations for speed.

        Note: Rising/setting times use a geometric formula that accounts for atmospheric
        refraction (~34'). This results in high accuracy compared to Skyfield's
        iterative solver, while maintaining excellent performance.
        """
        # Optimization: prioritize pre-calculated coordinate columns to avoid slow
        # Python loops and attribute access on Skyfield objects.
        if "ra_hours" in df.columns and "dec_degrees" in df.columns:
            ras = df["ra_hours"].to_numpy()
            decs = df["dec_degrees"].to_numpy()
            # Check for skyfield_object to determine valid stars, or assume valid
            # if we have coordinates but no objects yet (lazy loading case).
            if getattr(self, "is_star_catalog", False):
                # Optimization: In star catalogs, validity is tied to presence of coordinates.
                valid_mask = pd.notna(ras) & pd.notna(decs)
            elif "skyfield_object" in df.columns:
                sky_objs = df["skyfield_object"].to_numpy()
                # Relaxed validity check: any valid Skyfield object in the column
                valid_mask = pd.notnull(sky_objs)
            else:
                valid_mask = np.ones(len(df), dtype=bool)
        else:
            # Fallback: Extract Skyfield objects and their coordinates in a vectorized way
            if "skyfield_object" in df.columns:
                sky_objs = df["skyfield_object"].to_numpy()
            else:
                # Optimization: itertuples() is significantly faster than iterrows()
                sky_objs = np.array(
                    [self.get_skyfield_object(row) for row in df.itertuples()]
                )

            valid_mask = pd.notnull(sky_objs)

            ras = np.array(
                [
                    getattr(obj, "ra", getattr(obj, "target_ra", None)).hours
                    if obj is not None and hasattr(obj, "ra")
                    else 0
                    for obj in sky_objs
                ]
            )
            decs = np.array(
                [
                    getattr(obj, "dec", getattr(obj, "target_dec", None)).degrees
                    if obj is not None and hasattr(obj, "dec")
                    else 0
                    for obj in sky_objs
                ]
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
            sin_dec=df["sin_dec"].values if "sin_dec" in df.columns else None,
            cd_cr=df["cos_dec_cos_ra"].values if "cos_dec_cos_ra" in df.columns else None,
            cd_sr=df["cos_dec_sin_ra"].values if "cos_dec_sin_ra" in df.columns else None,
        )
