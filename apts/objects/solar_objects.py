import functools
from decimal import Decimal

import ephem
import numpy
import pandas as pd

from apts.place import Place

from ..cache import get_mpcorb_data
from ..constants import ObjectTableLabels
from ..utils import MINOR_PLANET_NAMES, planetary
from .objects import Objects


def _to_float(value):
    """
    Safely converts a value to a float, handling Decimal, NA, and other types.
    """
    if pd.isna(value):
        return numpy.nan
    if isinstance(value, Decimal):
        return float(value)
    if hasattr(value, "magnitude"):  # Handle pint.Quantity objects
        return float(value.magnitude)
    return float(value)


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
            if name not in dwarf_planet_technical_names
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
        name_to_use = obj.get("TechnicalName", obj.Name)
        try:
            return self._get_skyfield_object_cached(name_to_use)
        except (ValueError, KeyError):
            return None

    def compute(self, calculation_date=None, df_to_compute=None, skip_transits=False):
        if calculation_date is not None:
            # Instantiate as Place object
            temp_observer = Place(
                lat=self.place.lat_decimal,
                lon=self.place.lon_decimal,
                elevation=self.place.elevation,
                name=self.place.name + "_temp",
                date=calculation_date,
            )
            observer_to_use = temp_observer
        else:
            observer_to_use = self.place

        # If no specific DataFrame is provided, use the class's default.
        target_df = df_to_compute if df_to_compute is not None else self.objects

        # Work on a copy to avoid SettingWithCopyWarning
        computed_df = target_df.copy()

        if not skip_transits:
            # Compute transit of planets
            computed_df[ObjectTableLabels.TRANSIT] = [
                self._compute_tranzit(self.get_skyfield_object(row), observer_to_use)
                for _, row in computed_df.iterrows()
            ]

            # Compute rising and setting
            rise_set = [
                self._compute_rising_and_setting(
                    self.get_skyfield_object(row),
                    observer_to_use,
                    row[ObjectTableLabels.TRANSIT],
                )
                for _, row in computed_df.iterrows()
            ]
            computed_df[[ObjectTableLabels.RISING, ObjectTableLabels.SETTING]] = pd.DataFrame(
                rise_set, index=computed_df.index
            )

            # Compute altitude at transit
            computed_df[ObjectTableLabels.ALTITUDE] = [
                self._altitude_at_transit(
                    self.get_skyfield_object(row),
                    row[ObjectTableLabels.TRANSIT],
                    observer_to_use,
                )
                for _, row in computed_df.iterrows()
            ]

        t = observer_to_use.date
        # Calculate planets magnitude
        ephem_object_map = {
            "mercury": ephem.Mercury,
            "venus": ephem.Venus,
            "mars barycenter": ephem.Mars,
            "jupiter barycenter": ephem.Jupiter,
            "saturn barycenter": ephem.Saturn,
            "uranus barycenter": ephem.Uranus,
            "neptune barycenter": ephem.Neptune,
            "moon": ephem.Moon,
            "sun": ephem.Sun,
        }

        ephem_observer = ephem.Observer()
        ephem_observer.lat = str(observer_to_use.lat_decimal)
        ephem_observer.lon = str(observer_to_use.lon_decimal)
        ephem_observer.elevation = observer_to_use.elevation
        ephem_observer.date = t.utc_datetime()

        mags, sizes, phases = [], [], []

        for _, row in computed_df.iterrows():
            object_name = row[ObjectTableLabels.NAME]
            if object_name in MINOR_PLANET_NAMES.values():
                try:
                    minor_planet_details = self.minor_planets.loc[object_name]
                    dp = ephem.EllipticalBody()
                    dp._inc = numpy.deg2rad(minor_planet_details["inclination_degrees"])
                    dp._Om = numpy.deg2rad(minor_planet_details["longitude_of_ascending_node_degrees"])
                    dp._om = numpy.deg2rad(minor_planet_details["argument_of_perihelion_degrees"])
                    dp._a = minor_planet_details["semimajor_axis_au"]
                    dp._e = minor_planet_details["eccentricity"]
                    dp._M = numpy.deg2rad(minor_planet_details["mean_anomaly_degrees"])
                    if pd.notna(minor_planet_details["magnitude_H"]):
                        dp._H = minor_planet_details["magnitude_H"]
                    if pd.notna(minor_planet_details["magnitude_G"]):
                        dp._G = minor_planet_details["magnitude_G"]

                    packed_epoch = minor_planet_details["epoch_packed"]
                    _MPC_CENTURY = {"I": 18, "J": 19, "K": 20}
                    _MPC_MONTH = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 11, "C": 12}
                    _MPC_DAY = {str(d): d for d in range(1, 10)}
                    _MPC_DAY.update({chr(ord("A") + i): i + 10 for i in range(22)})

                    year = _MPC_CENTURY[packed_epoch[0]] * 100 + int(packed_epoch[1:3])
                    month = _MPC_MONTH[packed_epoch[3]]
                    day = _MPC_DAY[packed_epoch[4]]
                    dp._epoch_M = ephem.Date(f"{year}/{month}/{day}")

                    dp.compute(ephem_observer)
                    mags.append(dp.mag)
                    sizes.append(pd.NA)
                    phases.append(pd.NA)
                except:
                    mags.append(pd.NA)
                    sizes.append(pd.NA)
                    phases.append(pd.NA)
            else:
                ephem_obj_constructor = ephem_object_map.get(object_name)
                if ephem_obj_constructor:
                    ephem_obj = ephem_obj_constructor()
                    ephem_obj.compute(ephem_observer)
                    mags.append(ephem_obj.mag)
                    sizes.append(ephem_obj.size)
                    phases.append(ephem_obj.phase)
                else:
                    mags.append(numpy.nan)
                    sizes.append(numpy.nan)
                    phases.append(numpy.nan)

        computed_df[ObjectTableLabels.MAGNITUDE] = mags
        computed_df[ObjectTableLabels.SIZE] = sizes
        computed_df[ObjectTableLabels.PHASE] = phases

        # Vectorized Skyfield positions
        obs_at_t = observer_to_use.observer.at(t)
        # For elongation, use apparent position of Sun for consistency with planets
        sun_pos = obs_at_t.observe(observer_to_use.sun).apparent()

        ras, decs, dists, elongs = [], [], [], []
        for _, row in computed_df.iterrows():
            sky_obj = self.get_skyfield_object(row)
            if sky_obj:
                pos = obs_at_t.observe(sky_obj).apparent()
                ra, dec, dist = pos.radec()
                ras.append(ra.hours)
                decs.append(dec.degrees)
                dists.append(dist.au)
                elongs.append(pos.separation_from(sun_pos).degrees)
            else:
                ras.append(numpy.nan)
                decs.append(numpy.nan)
                dists.append(numpy.nan)
                elongs.append(numpy.nan)

        computed_df[ObjectTableLabels.RA] = ras
        computed_df[ObjectTableLabels.DEC] = decs
        computed_df[ObjectTableLabels.DISTANCE] = dists
        computed_df[ObjectTableLabels.ELONGATION] = elongs

        # Ensure all columns exist in self.objects
        for col in computed_df.columns:
            if col not in self.objects.columns:
                self.objects[col] = pd.NA

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
        # We skip transits here because they are slow and not needed for visibility filtering.
        if ObjectTableLabels.MAGNITUDE not in self.objects.columns or self.objects[ObjectTableLabels.MAGNITUDE].isnull().all():
            self.compute(self.calculation_date, skip_transits=True)

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
            visible["TechnicalName"] = visible["Name"]
            visible["Name"] = (
                visible["TechnicalName"]
                .apply(planetary.get_simple_name)
                .astype("string")
            )

        return visible

    def find_by_name(self, name):
        """
        Finds a planet by its name (e.g., "Mars").
        """
        try:
            return planetary.get_skyfield_obj(name)
        except (ValueError, KeyError):
            return None
