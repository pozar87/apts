from types import SimpleNamespace

import numpy as np
import pandas as pd

from ..catalogs import Catalogs
from ..catalogs.ngc import normalize_name as internal_normalize_name
from ..constants import ObjectTableLabels
from .base import Objects


class NGC(Objects):
    is_star_catalog = True

    def __init__(self, place, catalogs: Catalogs, calculation_date=None):
        super(NGC, self).__init__(place, calculation_date=calculation_date)
        self.objects = catalogs.NGC.copy()  # type: ignore
        self.objects[ObjectTableLabels.TRANSIT] = None
        self.objects[ObjectTableLabels.RISING] = None
        self.objects[ObjectTableLabels.SETTING] = None
        self.objects[ObjectTableLabels.ALTITUDE] = None
        self.calculation_date = (
            calculation_date  # Store calculation_date for lazy computation
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
        exclude_messier=True,
        **kwargs,
    ) -> pd.DataFrame:
        # Override get_visible to lazily restore skyfield objects and Pint units
        # ONLY for the final set of visible objects.
        # This is a major performance win for NGC as it avoids creating
        # thousands of Pint/Skyfield objects for candidates that are below the horizon.

        # 1. Ensure skyfield_object column exists in master catalog
        if "skyfield_object" not in self.objects.columns:
            self.objects["skyfield_object"] = None

        # 2. Call super().get_visible to perform vectorized visibility calculations
        # NGC uses is_star_catalog=True and ra_hours/dec_degrees columns,
        # so super().get_visible() does NOT need skyfield_objects yet.
        visible = super().get_visible(
            conditions,
            start,
            stop,
            hours_margin=hours_margin,
            sort_by=sort_by,
            star_magnitude_limit=star_magnitude_limit,
            limiting_magnitude=limiting_magnitude,
            **kwargs,
        )

        if visible.empty:
            return visible

        # 3. Apply exclude_messier filter to visible objects
        if exclude_messier and "M" in visible.columns:
            visible = visible[visible["M"].isna()]

        if visible.empty:
            return visible  # type: ignore[return-value]

        # 4. Defer restoration of skyfield_objects and Pint units to visible subset
        from skyfield.api import Star

        from ..units import get_unit_registry

        ureg = get_unit_registry()

        # Identify which visible objects still need restoration (missing Skyfield object
        # or Pint Quantity magnitude). We use the master catalog (self.objects) as the
        # source of truth for existing restorations.
        # Optimization: Use list comprehension over .values to minimize Pandas overhead.
        indices_needing_restoration = [
            idx
            for idx in visible.index
            if pd.isnull(self.objects.at[idx, "skyfield_object"])
            or not hasattr(self.objects.at[idx, "Magnitude"], "magnitude")
        ]

        if indices_needing_restoration:
            # Vectorized Skyfield Star restoration
            # Since NGC catalog has fixed RA/Dec, we can use them directly
            ras = self.objects.loc[indices_needing_restoration, "ra_hours"].values
            decs = self.objects.loc[indices_needing_restoration, "dec_degrees"].values
            sky_objs = [
                Star(ra_hours=r, dec_degrees=d) if pd.notna(r) and pd.notna(d) else None
                for r, d in zip(ras, decs)
            ]
            self.objects.loc[indices_needing_restoration, "skyfield_object"] = sky_objs

            # Vectorized Pint Magnitude restoration
            mags_q = list(
                self.objects.loc[indices_needing_restoration, "Magnitude_float"].values
                * ureg.mag
            )
            self.objects.loc[indices_needing_restoration, "Magnitude"] = mags_q

            # Vectorized Pint Size restoration
            # Extract plain floats first to handle both raw floats and already-restored Quantities
            sizes_major_raw = self.objects.loc[
                indices_needing_restoration, ObjectTableLabels.SIZE_MAJOR
            ].values
            if hasattr(sizes_major_raw, "dtype") and sizes_major_raw.dtype == object:
                # Object array likely contains Quantities; extract magnitudes
                sizes_major_floats = np.array(
                    [getattr(v, "magnitude", v) for v in sizes_major_raw], dtype=float
                )
            else:
                sizes_major_floats = np.atleast_1d(sizes_major_raw)
            sizes_major_q = list(sizes_major_floats * ureg.arcminute)

            sizes_minor_raw = self.objects.loc[
                indices_needing_restoration, ObjectTableLabels.SIZE_MINOR
            ].values
            if hasattr(sizes_minor_raw, "dtype") and sizes_minor_raw.dtype == object:
                sizes_minor_floats = np.array(
                    [getattr(v, "magnitude", v) for v in sizes_minor_raw], dtype=float
                )
            else:
                sizes_minor_floats = np.atleast_1d(sizes_minor_raw)
            sizes_minor_q = list(sizes_minor_floats * ureg.arcminute)
            self.objects.loc[
                indices_needing_restoration, ObjectTableLabels.SIZE_MAJOR
            ] = sizes_major_q
            self.objects.loc[
                indices_needing_restoration, ObjectTableLabels.SIZE_MINOR
            ] = sizes_minor_q

            # Refresh the 'visible' slice with restored objects for returning to the caller.
            # We must re-copy from the master catalog to ensure consistency.
            visible.update(self.objects.loc[indices_needing_restoration])

        return visible  # type: ignore[return-value]

    def compute(self, calculation_date=None, df_to_compute=None):
        if calculation_date is not None:
            # It's a Skyfield Time object. If it's an array, use the first element.
            if hasattr(calculation_date, "shape") and calculation_date.shape:
                t = calculation_date[0]
            elif isinstance(calculation_date, type(self.ts.now())):
                t = calculation_date
            else:
                t = self.ts.utc(calculation_date)

            # Avoid creating a whole new Place object, which is slow.
            observer_to_use = SimpleNamespace(
                date=t,
                local_timezone=self.place.local_timezone,
                lat_decimal=self.place.lat_decimal,
                lon_decimal=self.place.lon_decimal,
                elevation=self.place.elevation,
                observer=self.place.observer,
            )
        else:
            observer_to_use = self.place

        # If no specific DataFrame is provided, use the class's default.
        if df_to_compute is None:
            df_to_compute = self.objects

        # Work on a copy to avoid modifying the original DataFrame slice
        computed_df = df_to_compute.copy()

        # Fast transit and altitude calculation for stars
        transits, alts, rises, sets = self._vectorized_geometric_compute(
            computed_df, observer_to_use
        )
        computed_df[ObjectTableLabels.TRANSIT] = transits
        computed_df[ObjectTableLabels.ALTITUDE] = alts
        computed_df[ObjectTableLabels.RISING] = rises
        computed_df[ObjectTableLabels.SETTING] = sets
        self.objects.update(computed_df)
        return computed_df

    def get_skyfield_object(self, obj):
        # Handle lazy skyfield_object restoration
        # Case 1: DataFrame passed for vectorized Star creation
        if isinstance(obj, pd.DataFrame):
            from skyfield.api import Star

            return Star(
                ra_hours=obj["ra_hours"].to_numpy(),
                dec_degrees=obj["dec_degrees"].to_numpy(),
            )

        # Case 2: Individual object (Series, dict, or namedtuple)
        sky_obj = getattr(
            obj,
            "skyfield_object",
            obj.get("skyfield_object") if isinstance(obj, dict) else None,
        )
        if sky_obj is not None and pd.notna(sky_obj):
            return sky_obj

        # Reconstruct if missing (lazy loading or unpickled)
        ra = getattr(
            obj, "ra_hours", obj.get("ra_hours") if isinstance(obj, dict) else None
        )
        dec = getattr(
            obj,
            "dec_degrees",
            obj.get("dec_degrees") if isinstance(obj, dict) else None,
        )

        if ra is not None and dec is not None:
            return self.fixed_body(ra, dec)

        return None

    @staticmethod
    def normalize_name(n):
        """
        Normalize NGC/IC names to a standard format (e.g., 'NGC 224' -> 'NGC0224').
        """
        return internal_normalize_name(n)

    def find_by_name(self, name):
        """
        Finds a NGC object by its name (e.g., "NGC 224" or "IC 71").
        """
        norm_name = self.normalize_name(name)

        if self.objects.empty:
            return None

        mask = pd.Series(False, index=self.objects.index)

        # Optimization: use pre-calculated normalized columns if available
        if "NGC_norm" in self.objects.columns:
            mask |= self.objects["NGC_norm"] == norm_name
        elif ObjectTableLabels.NGC in self.objects.columns:
            mask |= (
                self.objects[ObjectTableLabels.NGC].apply(self.normalize_name)
                == norm_name
            )

        if "Name_norm" in self.objects.columns:
            mask |= self.objects["Name_norm"] == norm_name
        elif ObjectTableLabels.NAME in self.objects.columns:
            mask |= (
                self.objects[ObjectTableLabels.NAME].apply(self.normalize_name)
                == norm_name
            )

        if "IC_norm" in self.objects.columns:
            mask |= self.objects["IC_norm"] == norm_name
        elif ObjectTableLabels.IC in self.objects.columns:
            mask |= (
                self.objects[ObjectTableLabels.IC].apply(self.normalize_name)
                == norm_name
            )

        result = self.objects[mask]
        if not result.empty:
            return self.get_skyfield_object(result.iloc[0])
        return None
