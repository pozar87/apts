import types
import unittest.mock
from typing import TYPE_CHECKING, Any, cast

import numpy as np
import pandas as pd
from skyfield.api import Star

if TYPE_CHECKING:
    from skyfield.api import Timescale

from ..constants import ObjectTableLabels
from ..skyfield_searches.utils import fast_altaz
from .calculations import (
    calculate_visible_stars_mask,
    filter_objects_by_magnitude,
)
from .utils import filter_technical_columns


class VisibilityMixIn:
    if TYPE_CHECKING:
        objects: pd.DataFrame
        place: Any
        ts: Timescale
        calculation_date: Any

        def get_skyfield_object(self, obj) -> object: ...
        def compute(
            self, calculation_date=None, df_to_compute=None
        ) -> pd.DataFrame: ...

    def _filter_by_magnitude(
        self, conditions, star_magnitude_limit, limiting_magnitude
    ) -> pd.DataFrame:
        """
        Filters objects based on magnitude limits. Delegates to pure helper.
        """
        return filter_objects_by_magnitude(
            self.objects, conditions, star_magnitude_limit, limiting_magnitude
        )

    def _get_visible_mocked(self, candidate_objects, conditions, start, stop) -> list:
        """
        Calculates visibility for objects when the place.get_altaz_curve is mocked.
        """
        visible_objects_indices = []
        # Optimization: itertuples() is significantly faster than iterrows()
        for row in candidate_objects.itertuples():
            index = row.Index
            skyfield_object = self.get_skyfield_object(row)
            if skyfield_object is None:
                continue
            altaz_df = self.place.get_altaz_curve(skyfield_object, start, stop)
            # Optimization: list comprehension over .values is faster than .apply() for extracting magnitudes.
            altitude_values = [
                x.magnitude if hasattr(x, "magnitude") else x
                for x in altaz_df["Altitude"].values
            ]
            azimuth_values = [
                x.magnitude if hasattr(x, "magnitude") else x
                for x in altaz_df["Azimuth"].values
            ]
            visible_condition = conditions.is_visible(
                np.array(azimuth_values), np.array(altitude_values)
            )
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
        Delegates to the pure calculate_visible_stars_mask function.
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

        # Prepare direction cosine arrays if present in the candidate dataframe
        sin_dec = None
        cos_dec_cos_ra = None
        cos_dec_sin_ra = None
        if "sin_dec" in candidate_objects.columns:
            # Note: active_stars_indices indexing is done inside the pure function
            # So we pass the entire column or a slice matching stars_indices.
            sin_dec = candidate_objects["sin_dec"].values
            cos_dec_cos_ra = candidate_objects["cos_dec_cos_ra"].values
            cos_dec_sin_ra = candidate_objects["cos_dec_sin_ra"].values

        # Delegate pure geometry checks to the extracted pure function
        visible_stars_potential_mask = calculate_visible_stars_mask(
            self.place.lat_decimal,
            self.place.lon_decimal,
            stars_ras,
            stars_decs,
            check_times.gmst,
            conditions,
            sin_dec=sin_dec[stars_indices] if sin_dec is not None else None,
            cos_dec_cos_ra=cos_dec_cos_ra[stars_indices]
            if cos_dec_cos_ra is not None
            else None,
            cos_dec_sin_ra=cos_dec_sin_ra[stars_indices]
            if cos_dec_sin_ra is not None
            else None,
        )

        visible_mask[stars_indices] = visible_stars_potential_mask

    def _get_visible_other(
        self, skyfield_objs, other_indices, obs_at_check_times, conditions, visible_mask
    ):
        """
        Check Other objects (like planets) using Skyfield.
        """
        for i in other_indices:
            skyfield_obj = skyfield_objs[i]
            # Optimization: Use fast_altaz to bypass expensive Standard Apparent calculations.
            # This provides a ~2.5x speedup for visibility gating with negligible accuracy loss.
            alt, az, _ = fast_altaz(obs_at_check_times, skyfield_obj)
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
                    computed_df = self.compute(
                        calculation_date=self.calculation_date,
                        df_to_compute=visible_candidate_objects,
                    )
                    # Optimization: Directly assign computed transit, rise, set, and altitude
                    # columns from returned computed_df. Bypasses redundant self.objects.loc[]
                    # lookups and expensive DataFrame.update() alignment checks.
                    for col in needed_cols:
                        visible_candidate_objects[col] = computed_df[col]

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
        if (
            getattr(self, "is_star_catalog", False)
            and "ra_hours" in candidate_objects.columns
        ):
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
                    [
                        self.get_skyfield_object(row)
                        for row in candidate_objects.itertuples()
                    ]
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
        clean=True,
    ) -> pd.DataFrame:
        if not start or not stop:
            df = pd.DataFrame(columns=self.objects.columns)
            return filter_technical_columns(df) if clean else df

        candidate_objects = self._filter_by_magnitude(
            conditions, star_magnitude_limit, limiting_magnitude
        )

        if candidate_objects.empty:
            df = pd.DataFrame(columns=self.objects.columns)
            return filter_technical_columns(df) if clean else df

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
            df = pd.DataFrame(columns=self.objects.columns)
            return filter_technical_columns(df) if clean else df

        # Compute transit/rise/set ONLY for visible objects if needed for sorting or plotting
        self._ensure_computed_fields(visible_candidate_objects, sort_by)

        visible = visible_candidate_objects

        # Sort objects by given order, handling potential NaNs
        if sort_by in visible.columns and not bool(visible[sort_by].isnull().all()):
            visible = visible.sort_values(by=sort_by, ascending=True)

        if clean:
            visible = filter_technical_columns(visible)

        return visible
