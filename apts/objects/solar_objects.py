from types import SimpleNamespace
import functools
import numpy
import pandas as pd
import ephem

from .objects import Objects
from ..constants import ObjectTableLabels
from ..utils import planetary
from apts.place import Place


from ..cache import get_ephemeris, get_mpcorb_data, get_timescale


class SolarObjects(Objects):
    def __init__(self, place, calculation_date=None):
        super(SolarObjects, self).__init__(place)
        # Initialize minor planets data for lazy loading
        self._minor_planets = None
        self.minor_planet_names = {
            "ceres": "(1) Ceres",
            "haumea": "(136108) Haumea",
            "makemake": "(136472) Makemake",
            "eris": "(136199) Eris",
        }
        # Init object list with all planets
        self.objects = pd.DataFrame(
            planetary.TECHNICAL_NAMES,
            columns=[ObjectTableLabels.NAME],
        )  # pyright: ignore

        # Set proper dtype for string columns
        self.objects[ObjectTableLabels.NAME] = self.objects[
            ObjectTableLabels.NAME
        ].astype("string")
        # Compute positions
        self.compute(calculation_date)

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
        return self._get_skyfield_object_cached(name_to_use)

    def compute(self, calculation_date=None):
        if calculation_date is not None:
            # Instantiate as Place object
            temp_observer = Place(
                lat=self.place.lat_decimal,
                lon=self.place.lon_decimal,
                elevation=self.place.elevation,
                name=self.place.name + "_temp",
                date=calculation_date,
            )  # Add name to avoid issues if Place requires it

            observer_to_use = temp_observer
        else:
            observer_to_use = self.place

        # Compute transit of planets at given place
        self.objects[ObjectTableLabels.TRANSIT] = self.objects.apply(
            lambda body: self._compute_tranzit(
                self.get_skyfield_object(body), observer_to_use
            ),
            axis=1,
        )
        # Compute rising and setting of planets at given place
        self.objects[[ObjectTableLabels.RISING, ObjectTableLabels.SETTING]] = (
            self.objects.apply(
                lambda body: self._compute_rising_and_setting(
                    self.get_skyfield_object(body), observer_to_use
                ),
                axis=1,
            ).apply(pd.Series)
        )
        # Compute altitude of planets at transit (at given place)
        self.objects[ObjectTableLabels.ALTITUDE] = self.objects[
            [ObjectTableLabels.TRANSIT]
        ].apply(
            lambda row: self._altitude_at_transit(
                self.get_skyfield_object(self.objects.loc[row.name]),
                row.Transit,
                observer_to_use,
            ),
            axis=1,
        )

        t = observer_to_use.date
        # Calculate planets magnitude
        # Define a mapping from Skyfield object names to Pyephem object constructors
        # This map is local to the compute method as it's only used here.
        ephem_object_map = {
            "mercury": ephem.Mercury,  # pyright: ignore
            "venus": ephem.Venus,  # pyright: ignore
            "mars barycenter": ephem.Mars,  # pyright: ignore
            "jupiter barycenter": ephem.Jupiter,  # pyright: ignore
            "saturn barycenter": ephem.Saturn,  # pyright: ignore
            "uranus barycenter": ephem.Uranus,  # pyright: ignore
            "neptune barycenter": ephem.Neptune,  # pyright: ignore
            "moon": ephem.Moon,  # pyright: ignore
            "sun": ephem.Sun,  # pyright: ignore
        }

        # Create an ephem observer for the current place and time, once for efficiency
        ephem_observer = ephem.Observer()
        # pyephem expects latitude/longitude as strings or floats in degrees
        ephem_observer.lat = str(observer_to_use.lat_decimal)
        ephem_observer.lon = str(observer_to_use.lon_decimal)
        # pyephem expects elevation in meters
        ephem_observer.elevation = observer_to_use.elevation
        # pyephem expects a datetime object or ephem.Date
        ephem_observer.date = t.utc_datetime()

        # Helper function to calculate magnitude
        def get_ephem_properties(row):
            object_name = row[ObjectTableLabels.NAME]
            if object_name in self.minor_planet_names:
                # For minor planets, we'll use a placeholder for magnitude, size, and phase for now
                return pd.Series([pd.NA, pd.NA, pd.NA])
            else:
                ephem_obj_constructor = ephem_object_map.get(object_name)
                if ephem_obj_constructor:
                    ephem_obj = ephem_obj_constructor()
                    ephem_obj.compute(ephem_observer)
                    return pd.Series([ephem_obj.mag, ephem_obj.size, ephem_obj.phase])
            return pd.Series([numpy.nan, numpy.nan, numpy.nan])

        self.objects[
            [
                ObjectTableLabels.MAGNITUDE,
                ObjectTableLabels.SIZE,
                ObjectTableLabels.PHASE,
            ]
        ] = self.objects.apply(get_ephem_properties, axis=1)

        # Calculate planets RA, Dec, Distance, and Elongation
        # Batch compute positions for better performance
        def compute_position(row):
            pos = observer_to_use.observer.at(t).observe(self.get_skyfield_object(row))
            return pd.Series(
                {
                    ObjectTableLabels.RA: pos.radec()[0].hours,
                    ObjectTableLabels.DEC: pos.radec()[1].degrees,
                    ObjectTableLabels.DISTANCE: pos.distance().au,
                    ObjectTableLabels.ELONGATION: pos.separation_from(
                        observer_to_use.sun.at(t)
                    ).degrees,
                }
            )

        self.objects[
            [
                ObjectTableLabels.RA,
                ObjectTableLabels.DEC,
                ObjectTableLabels.DISTANCE,
                ObjectTableLabels.ELONGATION,
            ]
        ] = self.objects.apply(compute_position, axis=1)

    def get_visible(
        self, conditions, start, stop, hours_margin=0, sort_by=ObjectTableLabels.TRANSIT
    ):
        visible = self.objects.copy()
        # Add ID collumn
        visible["ID"] = visible.index
        visible = visible[
            # Filter objects by they rising and setting within the time window, handling wrap-around
            (
                (
                    (visible.Rising <= visible.Setting)
                    & (visible.Rising <= stop)
                    & (visible.Setting >= start)
                )
                | (
                    (visible.Setting < visible.Rising)
                    & ~((visible.Setting < start) & (stop < visible.Rising))
                )
            )
            &
            # Filter object by they magnitude
            # Handle pint.Quantity objects for magnitude
            # Allow objects with NA magnitude (dwarf planets) to pass through,
            # or filter by magnitude for others.
            (
                pd.isna(visible.Magnitude)
                | (
                    pd.to_numeric(
                        visible.Magnitude.apply(
                            lambda x: x.magnitude if hasattr(x, "magnitude") else x
                        ),
                        errors="coerce",
                    )
                    < conditions.max_object_magnitude
                )
            )
        ]

        if conditions.min_object_azimuth == 0 and conditions.max_object_azimuth == 360:
            # Sort objects by given order
            visible = visible.sort_values(by=sort_by, ascending=True)  # pyright: ignore
            if not visible.empty:
                visible["TechnicalName"] = visible["Name"]
                visible["Name"] = (
                    visible["TechnicalName"]
                    .apply(planetary.get_simple_name)
                    .astype("string")
                )
            return visible

        visible_objects_indices = []
        for index, row in visible.iterrows():
            skyfield_object = self.get_skyfield_object(row)
            altaz_df = self.place.get_altaz_curve(skyfield_object, start, stop)

            # Filter for times when altitude is sufficient
            above_horizon_df = altaz_df[
                altaz_df["Altitude"] > conditions.min_object_altitude
            ]

            if not above_horizon_df.empty:
                # Check if azimuth is within range for any of these times
                az_conditions_met = self._is_azimuth_in_range(
                    above_horizon_df["Azimuth"], conditions
                )
                if az_conditions_met.any():
                    visible_objects_indices.append(index)

        visible = self.objects.loc[visible_objects_indices]

        # Sort objects by given order
        visible = visible.sort_values(by=sort_by, ascending=True)

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
