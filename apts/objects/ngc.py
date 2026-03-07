from types import SimpleNamespace

import pandas as pd

from .objects import Objects
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

    def get_visible(self, conditions, start, stop, **kwargs):
        # Override get_visible to lazily restore skyfield objects BEFORE
        # calculation and units AFTER calculation.
        # This is a major performance win for NGC as it avoids creating
        # 14k Pint/Skyfield objects during catalog load.

        from skyfield.api import Star

        # 1. Determine magnitude threshold (handling Pint Quantities)
        limiting_magnitude = kwargs.get("limiting_magnitude")
        star_magnitude_limit = kwargs.get("star_magnitude_limit")
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
        if missing_sky_mask.any():
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
        visible = super().get_visible(conditions, start, stop, **kwargs)

        # 4. Restore Pint units for visible objects only and update master catalog
        if not visible.empty:
            from ..units import get_unit_registry

            ureg = get_unit_registry()

            # Identify which visible objects still need Quantity restoration in master catalog
            # We use Magnitude_float comparison as Magnitude column might contain floats
            restoration_mask = visible["Magnitude"].apply(
                lambda x: not hasattr(x, "magnitude")
            )
            if restoration_mask.any():
                indices_to_restore = visible.index[restoration_mask]

                # Magnitude restoration
                mags_q = list(
                    self.objects.loc[indices_to_restore, "Magnitude_float"].values
                    * ureg.mag
                )
                self.objects.loc[indices_to_restore, "Magnitude"] = mags_q

                # Size restoration
                sizes_q = [
                    x * ureg.arcminute if pd.notna(x) else None
                    for x in self.objects.loc[indices_to_restore, "Size"]
                ]
                self.objects.loc[indices_to_restore, "Size"] = sizes_q

                # Refresh the 'visible' slice with restored objects
                visible.loc[indices_to_restore, "Magnitude"] = mags_q
                visible.loc[indices_to_restore, "Size"] = sizes_q

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
        transits, alts, rises, sets = self._fast_compute_stars(
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

        # Case 2: Individual object (Series or dict)
        if "skyfield_object" in obj and pd.notna(obj["skyfield_object"]):
            return obj["skyfield_object"]

        # Reconstruct if missing (lazy loading or unpickled)
        if "ra_hours" in obj and "dec_degrees" in obj:
            sky_obj = self.fixed_body(obj["ra_hours"], obj["dec_degrees"])
            # If obj is a Series from self.objects, we might want to cache it back
            # However, we're in a read-only context here (obj might be a copy)
            return sky_obj

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
