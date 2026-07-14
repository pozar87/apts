import functools
from typing import cast

import numpy as np
import pandas as pd

from ...cache import get_mpcorb_data
from ...constants import DSOType, ObjectTableLabels
from ...utils import MINOR_PLANET_NAMES, planetary
from ..base import Objects
from .calculations import compute_ephem_and_skyfield_data


class SolarObjects(Objects):
    def __init__(self, place, calculation_date=None, lazy=False):
        super(SolarObjects, self).__init__(place)
        # Eagerly load minor planets data on initialization
        self._minor_planets = get_mpcorb_data()
        # Init object list with all planets and dwarf planets
        dwarf_planet_technical_names = list(MINOR_PLANET_NAMES.keys())
        major_planets_technical_names = [
            name
            for name in planetary.TECHNICAL_NAMES
            if name not in dwarf_planet_technical_names and name != "earth"
        ]
        all_solar_system_bodies = major_planets_technical_names + list(
            MINOR_PLANET_NAMES.values()
        )
        self.objects = pd.DataFrame(
            all_solar_system_bodies,
            columns=[ObjectTableLabels.NAME],  # pyright: ignore
        )

        # Set proper dtype for string columns
        self.objects[ObjectTableLabels.NAME] = self.objects[
            ObjectTableLabels.NAME
        ].astype("string")
        self.calculation_date = calculation_date
        # Compute positions and magnitudes. Skip slow transits if lazy.
        self.compute(calculation_date, skip_transits=lazy)

    @property
    def minor_planets(self):
        """Lazy loading of minor planets data."""
        if self._minor_planets is None:
            self._minor_planets = get_mpcorb_data()
        return self._minor_planets

    @functools.lru_cache(maxsize=32)
    def _get_skyfield_object_cached(self, obj_name):
        """Internal cached version of skyfield object retrieval."""
        return planetary.get_skyfield_obj(obj_name)

    def get_skyfield_object(self, obj):
        """Get skyfield object with caching when possible."""
        # Optimization: Prioritize direct attribute access for skyfield_object.
        # This bypasses more expensive name-based lookups when possible.
        sky_obj = getattr(obj, "skyfield_object", None)
        if sky_obj is not None and pd.notna(sky_obj):
            return sky_obj

        # Identification from TechnicalName or Name (NamedTuples, Series, or dicts)
        name_to_use = getattr(obj, "TechnicalName", None)
        if name_to_use is None:
            name_to_use = getattr(obj, ObjectTableLabels.NAME, None)

        if name_to_use is None and isinstance(obj, dict):
            name_to_use = obj.get("TechnicalName") or obj.get(ObjectTableLabels.NAME)
            if sky_obj is None:
                sky_obj = obj.get("skyfield_object")

        if name_to_use is not None:
            try:
                return self._get_skyfield_object_cached(name_to_use)
            except (ValueError, KeyError):
                pass

        return sky_obj if sky_obj is not None and pd.notna(sky_obj) else None

    def compute(self, calculation_date=None, df_to_compute=None, skip_transits=False):
        observer_to_use, t = self._prepare_observer(calculation_date)
        target_df = df_to_compute if df_to_compute is not None else self.objects
        computed_df = target_df.copy()

        compute_ephem_and_skyfield_data(
            computed_df,
            observer_to_use,
            t,
            self.minor_planets,
            self.get_skyfield_object,
        )
        computed_df.loc[:, ObjectTableLabels.DSO_TYPE] = DSOType.OTHER.value

        if not skip_transits:
            # Call the base class compute for transit, altitude, rise/set.
            # We pass computed_df which now has ra_hours/dec_degrees and skyfield_objects.
            computed_df = super().compute(calculation_date, computed_df)

        # Ensure all columns exist in self.objects
        for col in computed_df.columns:
            if col not in self.objects.columns:
                self.objects[col] = None

        self.objects.update(computed_df)
        return computed_df

    def get_visible(
        self,
        conditions,
        start,
        stop,
        hours_margin=0,
        sort_by=ObjectTableLabels.TRANSIT,
        star_magnitude_limit=None,
        limiting_magnitude=None,
    ):
        # Always ensure some basic computation is done if needed for magnitude filtering
        # Actually self.objects starts with only names. Magnitude is needed for filtering.
        # Since transits are now fast and vectorized, we compute them for all objects at once.
        if ObjectTableLabels.MAGNITUDE not in self.objects.columns or bool(
            self.objects[ObjectTableLabels.MAGNITUDE].isnull().all()
        ):
            self.compute(self.calculation_date, skip_transits=False)

        # First, call the parent's get_visible method
        visible = super().get_visible(
            conditions,
            start,
            stop,
            hours_margin,
            sort_by,
            star_magnitude_limit,
            limiting_magnitude,
        )

        if not visible.empty:
            # Optimization: use unique value mapping for get_simple_name
            # instead of row-wise .apply().
            visible["TechnicalName"] = visible["Name"]
            unique_tech_names = visible["TechnicalName"].unique()
            name_map = {tn: planetary.get_simple_name(tn) for tn in unique_tech_names}
            visible["Name"] = cast(
                pd.Series,
                visible["TechnicalName"].map(name_map),  # pyright: ignore[reportArgumentType]
            ).astype("string")

        return visible

    def find_by_name(self, name):
        """
        Finds a planet by its name (e.g., "Mars").
        """
        try:
            return planetary.get_skyfield_obj(name)
        except (ValueError, KeyError):
            return None
