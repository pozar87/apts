from types import SimpleNamespace

import pandas as pd

from .base import Objects
from ..catalogs import Catalogs
from ..constants import ObjectTableLabels


class NGC(Objects):
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
        **kwargs,
    ) -> pd.DataFrame:
        # Override get_visible to lazily restore skyfield objects BEFORE
        # calculation and units AFTER calculation.
        # This is a major performance win for NGC as it avoids creating
        # 14k Pint/Skyfield objects during catalog load.

        from skyfield.api import Star

        # 1. Determine magnitude threshold (handling Pint Quantities)
        max_magnitude_q = (
            limiting_magnitude
            if limiting_magnitude is not None
            else (
                star_magnitude_limit
                if star_magnitude_limit is not None
                else conditions.max_object_magnitude
            )
        )
        # Convert threshold to float for fast comparison with Magnitude_float
        max_mag = (
            max_magnitude_q.magnitude
            if hasattr(max_magnitude_q, "magnitude")
            else max_magnitude_q
        )

        candidate_mask = self.objects["Magnitude_float"] < max_mag

        # 2. Restore skyfield_objects for candidates only
        if "skyfield_object" not in self.objects.columns:
            self.objects["skyfield_object"] = None

        missing_sky_mask = candidate_mask & self.objects["skyfield_object"].isnull()
        if bool(missing_sky_mask.any()):
            missing_indices = self.objects.index[missing_sky_mask]
            self.objects.loc[missing_indices, "skyfield_object"] = [
                Star(ra_hours=ra, dec_degrees=dec)
                if pd.notna(ra) and pd.notna(dec)
                else None
                for ra, dec in zip(
                    self.objects.loc[missing_indices, "ra_hours"],
                    self.objects.loc[missing_indices, "dec_degrees"],
                )
            ]

        # 3. Call super().get_visible to perform visibility calculations
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

        # 4. Restore Pint units for visible objects only and update master catalog
        if not visible.empty:
            from ..units import get_unit_registry

            ureg = get_unit_registry()

            # Identify which visible objects still need Quantity restoration in master catalog
            # We use Magnitude_float comparison as Magnitude column might contain floats
            restoration_mask = visible["Magnitude"].apply(
                lambda x: not hasattr(x, "magnitude")
            )
            if bool(restoration_mask.any()):
                indices_to_restore = visible.index[restoration_mask]

                # Magnitude restoration
                mags_q = list(
                    self.objects.loc[indices_to_restore, "Magnitude_float"].values
                    * ureg.mag
                )
                self.objects.loc[indices_to_restore, "Magnitude"] = mags_q

                # Size restoration
                # Optimization: vectorized Quantity creation is ~7x faster for large lists
                sizes_major_q = list(
                    self.objects.loc[indices_to_restore, ObjectTableLabels.SIZE_MAJOR].values
                    * ureg.arcminute
                )
                sizes_minor_q = list(
                    self.objects.loc[indices_to_restore, ObjectTableLabels.SIZE_MINOR].values
                    * ureg.arcminute
                )
                self.objects.loc[indices_to_restore, ObjectTableLabels.SIZE_MAJOR] = sizes_major_q
                self.objects.loc[indices_to_restore, ObjectTableLabels.SIZE_MINOR] = sizes_minor_q

                # Refresh the 'visible' slice with restored objects
                visible.loc[indices_to_restore, "Magnitude"] = mags_q
                visible.loc[indices_to_restore, ObjectTableLabels.SIZE_MAJOR] = sizes_major_q
                visible.loc[indices_to_restore, ObjectTableLabels.SIZE_MINOR] = sizes_minor_q

        return visible

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
        sky_obj = getattr(obj, "skyfield_object", obj.get("skyfield_object") if isinstance(obj, dict) else None)
        if sky_obj is not None and pd.notna(sky_obj):
            return sky_obj

        # Reconstruct if missing (lazy loading or unpickled)
        ra = getattr(obj, "ra_hours", obj.get("ra_hours") if isinstance(obj, dict) else None)
        dec = getattr(obj, "dec_degrees", obj.get("dec_degrees") if isinstance(obj, dict) else None)

        if ra is not None and dec is not None:
            return self.fixed_body(ra, dec)

        return None

    def find_by_name(self, name):
        """
        Finds a NGC object by its name (e.g., "NGC 224").
        """
        result = self.objects[
            (self.objects["NGC"] == name) | (self.objects["Name"] == name)
        ]
        if not result.empty:
            return self.get_skyfield_object(result.iloc[0])
        return None
