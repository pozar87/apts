from datetime import timedelta

import numpy
import pandas
import ephem
import pint

from .objects import Objects
from ..constants import ObjectTableLabels
from ..units import ureg
from ..utils import planetary
from apts.place import Place
from skyfield.api import load
from skyfield import almanac


from ..cache import get_ephemeris


class SolarObjects(Objects):
    def __init__(self, place, calculation_date=None):
        super(SolarObjects, self).__init__(place)
        # Init object list with all planets
        self.objects = pandas.DataFrame(
            planetary.TECHNICAL_NAMES,
            columns=[ObjectTableLabels.NAME],
        )

        # Set proper dtype for string columns
        self.objects[ObjectTableLabels.NAME] = self.objects[
            ObjectTableLabels.NAME
        ].astype("string")
        # Compute positions
        self.compute(calculation_date)

    def get_skyfield_object(self, solar_object):
        eph = get_ephemeris()
        return eph[solar_object.Name]

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
            lambda body: self._compute_tranzit(self.get_skyfield_object(body), observer_to_use), axis=1
        )
        # Compute rising and setting of planets at given place
        self.objects[[ObjectTableLabels.RISING, ObjectTableLabels.SETTING]] = self.objects.apply(
            lambda body: self._compute_rising_and_setting(self.get_skyfield_object(body), observer_to_use),
            axis=1,
        ).apply(pandas.Series)
        # Compute altitude of planets at transit (at given place)
        self.objects[ObjectTableLabels.ALTITUDE] = self.objects[
            [ObjectTableLabels.TRANSIT]
        ].apply(
            lambda row: self._altitude_at_transit(
                self.get_skyfield_object(self.objects.loc[row.name]), row.Transit, observer_to_use
            ),
            axis=1,
        )

        t = observer_to_use.date
        # Calculate planets magnitude
        # Define a mapping from Skyfield object names to Pyephem object constructors
        # This map is local to the compute method as it's only used here.
        ephem_object_map = {
            "mercury": ephem.Mercury,
            "venus": ephem.Venus,
            "mars": ephem.Mars,
            "jupiter barycenter": ephem.Jupiter,
            "saturn barycenter": ephem.Saturn,
            "uranus barycenter": ephem.Uranus,
            "neptune barycenter": ephem.Neptune,
            "moon": ephem.Moon,
            "sun": ephem.Sun,
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
        self.objects[
            [
                ObjectTableLabels.RA,
                ObjectTableLabels.DEC,
                ObjectTableLabels.DISTANCE,
                ObjectTableLabels.ELONGATION,
            ]
        ] = self.objects.apply(
            lambda row: pandas.Series(
                (
                    pos := self.place.observer.at(t).observe(
                        self.get_skyfield_object(row)
                    )
                )
                and {
                    ObjectTableLabels.RA: pos.radec()[0].hours,
                    ObjectTableLabels.DEC: pos.radec()[1].degrees,
                    ObjectTableLabels.DISTANCE: pos.distance().au,
                    ObjectTableLabels.ELONGATION: pos.separation_from(
                        self.place.sun.at(t)
                    ).degrees,
                }
            ),
            axis=1,
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
            # Filter objects by they min altitude at transit
            (visible.Altitude > conditions.min_object_altitude)
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

    
        