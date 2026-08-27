import logging
from abc import ABC, abstractmethod
from types import SimpleNamespace
from typing import Any, cast

import numpy as np
import pandas as pd
from skyfield.api import Star

from ..cache import get_timescale
from ..constants import ObjectTableLabels
from .almanac import AlmanacMixIn
from .utils import vectorized_geometric_compute
from .visibility import VisibilityMixIn

logger = logging.getLogger(__name__)


class Objects(VisibilityMixIn, AlmanacMixIn, ABC):
    # Flag to indicate if this catalog consists primarily of fixed stars.
    # Enables massive performance optimizations in visibility gating by bypassing
    # individual Skyfield object instantiations.
    is_star_catalog = False

    @abstractmethod
    def get_skyfield_object(self, obj) -> object:
        pass

    def drop_technical_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Removes internal technical calculation and caching columns from a DataFrame
        before returning or presenting it to the user.
        """
        from .utils import filter_technical_columns

        return filter_technical_columns(df)

    def data(self, clean: bool = True) -> pd.DataFrame:
        """
        Returns the catalog DataFrame. If clean is True (default),
        internal technical calculation columns are omitted.
        """
        if clean:
            return self.drop_technical_columns(self.objects)
        return self.objects

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
        # Optimization: Explicitly wrapping the lists as pd.Series with dtype=object and the correct index.
        # This prevents Pandas from triggering expensive row-wise datetime parsing and timezone conversions.
        computed_df[ObjectTableLabels.TRANSIT] = pd.Series(
            transits, index=computed_df.index, dtype=object
        )
        computed_df[ObjectTableLabels.ALTITUDE] = alts
        computed_df[ObjectTableLabels.RISING] = pd.Series(
            rises, index=computed_df.index, dtype=object
        )
        computed_df[ObjectTableLabels.SETTING] = pd.Series(
            sets, index=computed_df.index, dtype=object
        )

        # Always update the master objects DataFrame to keep data in sync.
        # This handles both full catalog computations and subset-specific updates.
        computed_cols = [
            ObjectTableLabels.TRANSIT,
            ObjectTableLabels.ALTITUDE,
            ObjectTableLabels.RISING,
            ObjectTableLabels.SETTING,
        ]
        if df_to_compute is self.objects:
            # Optimization: Direct column assignment when computing on the full catalog.
            # This completely avoids the massive overhead of self.objects.update() which
            # triggers slow timezone-aware datetime inference and alignment across 14k rows.
            self.objects[ObjectTableLabels.TRANSIT] = computed_df[
                ObjectTableLabels.TRANSIT
            ]
            self.objects[ObjectTableLabels.ALTITUDE] = computed_df[
                ObjectTableLabels.ALTITUDE
            ]
            self.objects[ObjectTableLabels.RISING] = computed_df[
                ObjectTableLabels.RISING
            ]
            self.objects[ObjectTableLabels.SETTING] = computed_df[
                ObjectTableLabels.SETTING
            ]
        else:
            # Optimization: Direct .loc column assignment for computed fields only.
            # Bypasses self.objects.update() which triggers slow alignment and pandas
            # FutureWarning when updating string-dtype catalog columns (e.g., Constellation).
            for col in computed_cols:
                vals = computed_df[col]
                if col in self.objects.columns and pd.api.types.is_datetime64_any_dtype(
                    self.objects[col]
                ):
                    vals = pd.to_datetime(vals, utc=True)
                self.objects.loc[computed_df.index, col] = vals

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

    @staticmethod
    def fixed_body(RA, Dec):
        # Create body at given coordinates
        return Star(ra_hours=RA, dec_degrees=Dec)

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
                    cast(Any, getattr(obj, "ra", getattr(obj, "target_ra", None))).hours
                    if obj is not None and hasattr(obj, "ra")
                    else 0
                    for obj in sky_objs
                ]
            )
            decs = np.array(
                [
                    cast(
                        Any, getattr(obj, "dec", getattr(obj, "target_dec", None))
                    ).degrees
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
            cd_cr=df["cos_dec_cos_ra"].values
            if "cos_dec_cos_ra" in df.columns
            else None,
            cd_sr=df["cos_dec_sin_ra"].values
            if "cos_dec_sin_ra" in df.columns
            else None,
        )
