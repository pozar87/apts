from datetime import timedelta

import numpy
import pandas
import ephem
import pint

from .objects import Objects
from ..constants import ObjectTableLabels
from ..utils import ureg
from apts.place import Place
from skyfield.api import load
from skyfield import almanac


class SolarObjects(Objects):
    def __init__(self, place, calculation_date=None):
        super(SolarObjects, self).__init__(place)
        self.eph = load("de421.bsp")
        # Init object list with all planets
        self.objects = pandas.DataFrame(
            [
                "Mercury",
                "Venus",
                "Mars",
                "Jupiter barycenter",
                "Saturn barycenter",
                "Uranus barycenter",
                "Neptune barycenter",
                "Moon",
                "Sun",
            ],
            columns=[ObjectTableLabels.NAME],
        )
        # Add name
        self.objects[ObjectTableLabels.OBJECT] = self.objects[
            [ObjectTableLabels.NAME]
        ].apply(lambda body: self.eph[body.Name], axis=1)
        # Set proper dtype for string columns
        self.objects[ObjectTableLabels.NAME] = self.objects[
            ObjectTableLabels.NAME
        ].astype("string")
        # Compute positions
        self.compute(calculation_date)

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
        self.objects[ObjectTableLabels.TRANSIT] = self.objects[
            [ObjectTableLabels.OBJECT]
        ].apply(
            lambda body: self._compute_tranzit(body.Object, observer_to_use), axis=1
        )
        # Compute rising and setting of planets at given place
        self.objects[[ObjectTableLabels.RISING, ObjectTableLabels.SETTING]] = self.objects[
            [ObjectTableLabels.OBJECT]
        ].apply(
            lambda body: self._compute_rising_and_setting(body.Object, observer_to_use),
            axis=1,
        ).apply(pandas.Series)
        # Compute altitude of planets at transit (at given place)
        self.objects[ObjectTableLabels.ALTITUDE] = self.objects[
            [ObjectTableLabels.OBJECT, ObjectTableLabels.TRANSIT]
        ].apply(
            lambda body: self._altitude_at_transit(
                body.Object, body.Transit, observer_to_use
            ),
            axis=1,
        )

        t = observer_to_use.date
        # Calculate planets magnitude
        # Define a mapping from Skyfield object names to Pyephem object constructors
        # This map is local to the compute method as it's only used here.
        ephem_object_map = {
            "Mercury": ephem.Mercury,
            "Venus": ephem.Venus,
            "Mars": ephem.Mars,
            "Jupiter barycenter": ephem.Jupiter,  # Pyephem's Jupiter refers to the planet itself
            "Saturn barycenter": ephem.Saturn,
            "Uranus barycenter": ephem.Uranus,
            "Neptune barycenter": ephem.Neptune,
            "Moon": ephem.Moon,
            "Sun": ephem.Sun,
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

        # Helper function to calculate magnitude using pyephem
        # This function is defined locally to enclose ephem_observer and ephem_object_map
        def get_ephem_properties(row):
            object_name = row[ObjectTableLabels.NAME]
            ephem_obj_constructor = ephem_object_map.get(object_name)
            if ephem_obj_constructor:
                ephem_obj = ephem_obj_constructor()
                ephem_obj.compute(ephem_observer)
                return pandas.Series([ephem_obj.mag, ephem_obj.size, ephem_obj.phase])
            # This case should ideally not be reached if the initial object list is complete
            # and mapped correctly. Returning numpy.nan for unhandled objects.
            return pandas.Series([numpy.nan, numpy.nan, numpy.nan])

        self.objects[
            [
                ObjectTableLabels.MAGNITUDE,
                ObjectTableLabels.SIZE,
                ObjectTableLabels.PHASE,
            ]
        ] = self.objects.apply(get_ephem_properties, axis=1)
        # Calculate planets RA, Dec, Distance, and Elongation
        positions = self.objects[ObjectTableLabels.OBJECT].apply(
            lambda obj: self.place.observer.at(t).observe(obj)
        )

        self.objects[ObjectTableLabels.RA] = positions.apply(
            lambda pos: pos.radec()[0].hours
        )
        self.objects[ObjectTableLabels.DEC] = positions.apply(
            lambda pos: pos.radec()[1].degrees
        )
        self.objects[ObjectTableLabels.DISTANCE] = positions.apply(
            lambda pos: pos.distance().au
        )
        self.objects[ObjectTableLabels.ELONGATION] = positions.apply(
            lambda pos: pos.separation_from(self.place.sun.at(t)).degrees
        )

    def get_visible(
        self, conditions, start, stop, hours_margin=0, sort_by=ObjectTableLabels.TRANSIT
    ):
        visible = self.objects
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
            (
                visible.Magnitude.apply(
                    lambda x: x.magnitude if hasattr(x, "magnitude") else x
                )
                < conditions.max_object_magnitude
            )
        ]
        # Sort objects by given order
        visible = visible.sort_values(by=sort_by, ascending=True)
        return visible