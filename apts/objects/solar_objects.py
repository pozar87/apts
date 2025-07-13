from datetime import timedelta

import ephem
import numpy
import pandas
import pint

from .objects import Objects
from ..constants import ObjectTableLabels
from ..utils import ureg
from apts.place import Place


class SolarObjects(Objects):
    def __init__(self, place):
        super(SolarObjects, self).__init__(place)
        # Init object list with all planets
        self.objects = pandas.DataFrame(
            [
                ephem.Mercury(),
                ephem.Venus(),
                ephem.Mars(),
                ephem.Jupiter(),
                ephem.Saturn(),
                ephem.Uranus(),
                ephem.Neptune(),
                ephem.Moon(),
                ephem.Sun(),
            ],
            columns=[ObjectTableLabels.EPHEM],
        )
        # Add name
        self.objects[ObjectTableLabels.NAME] = self.objects[
            [ObjectTableLabels.EPHEM]
        ].apply(lambda body: body.Ephem.name, axis=1)
        # Set proper dtype for string columns
        self.objects[ObjectTableLabels.NAME] = self.objects[
            ObjectTableLabels.NAME
        ].astype("string")
        # Compute positions
        self.compute()

    def compute(self, calculation_date=None):
        if calculation_date:
            # Instantiate as Place object
            temp_observer = Place(lat=self.place.lat_decimal,
                                  lon=self.place.lon_decimal,
                                  elevation=self.place.elevation,
                                  name=self.place.name + "_temp") # Add name to avoid issues if Place requires it

            # Copy relevant attributes
            # lat, lon, elevation are set by Place constructor
            # local_timezone is determined by Place constructor based on lon/lat
            temp_observer.pressure = self.place.pressure
            temp_observer.temp = self.place.temp
            temp_observer.horizon = self.place.horizon

            # Set the date
            temp_observer.date = ephem.Date(calculation_date)

            # Recompute sun and moon for the new date
            temp_observer.sun = ephem.Sun()
            temp_observer.sun.compute(temp_observer)
            temp_observer.moon = ephem.Moon()
            temp_observer.moon.compute(temp_observer)

            observer_to_use = temp_observer
        else:
            observer_to_use = self.place

        # Compute transit of planets at given place
        self.objects[ObjectTableLabels.TRANSIT] = self.objects[
            [ObjectTableLabels.EPHEM]
        ].apply(lambda body: self._compute_tranzit(body.Ephem, observer_to_use), axis=1)
        # Compute rising of planets at given place
        self.objects[ObjectTableLabels.RISING] = self.objects[
            [ObjectTableLabels.EPHEM]
        ].apply(lambda body: self._compute_rising(body.Ephem, observer_to_use), axis=1)
        # Compute transit of planets at given place
        self.objects[ObjectTableLabels.SETTING] = self.objects[
            [ObjectTableLabels.EPHEM]
        ].apply(lambda body: self._compute_setting(body.Ephem, observer_to_use), axis=1)
        # Compute altitude of planets at transit (at given place)
        self.objects[ObjectTableLabels.ALTITUDE] = self.objects[
            [ObjectTableLabels.EPHEM, ObjectTableLabels.TRANSIT]
        ].apply(
            lambda body: self._altitude_at_transit(body.Ephem, body.Transit, observer_to_use), axis=1
        )
        # Calculate planets magnitude
        self.objects[ObjectTableLabels.MAGNITUDE] = self.objects[
            [ObjectTableLabels.EPHEM]
        ].apply(lambda body: body.Ephem.mag * ureg.mag, axis=1)
        # Calculate planets RA
        self.objects[ObjectTableLabels.RA] = self.objects[
            [ObjectTableLabels.EPHEM]
        ].apply(
            lambda body: numpy.degrees(body.Ephem.ra) * 24 / 360 * ureg.hour, axis=1
        )
        # Calculate planets Dec
        self.objects[ObjectTableLabels.DEC] = self.objects[
            [ObjectTableLabels.EPHEM]
        ].apply(lambda body: numpy.degrees(body.Ephem.dec) * ureg.degree, axis=1)
        # Calculate planets distance from Earth
        self.objects[ObjectTableLabels.DISTANCE] = self.objects[
            [ObjectTableLabels.EPHEM]
        ].apply(lambda body: body.Ephem.earth_distance * ureg.AU, axis=1)
        # Calculate planets size
        self.objects[ObjectTableLabels.SIZE] = self.objects[
            [ObjectTableLabels.EPHEM]
        ].apply(lambda body: body.Ephem.size * ureg.arcsecond, axis=1)
        # Calculate planets elongation
        self.objects[ObjectTableLabels.ELONGATION] = self.objects[
            [ObjectTableLabels.EPHEM]
        ].apply(lambda body: numpy.degrees(body.Ephem.elong) * ureg.degree, axis=1)
        # Calculate planets phase
        self.objects[ObjectTableLabels.PHASE] = self.objects[
            [ObjectTableLabels.EPHEM]
        ].apply(lambda body: body.Ephem.phase * ureg.dimensionless, axis=1)

    def get_visible(
        self, conditions, start, stop, hours_margin=0, sort_by=ObjectTableLabels.TRANSIT
    ):
        visible = self.objects
        # Add ID collumn
        visible["ID"] = visible.index
        visible = visible[
            # Filter objects by they rising and setting within the time window, handling wrap-around
            (\
                ((visible.Rising <= visible.Setting) & (visible.Rising <= stop) & (visible.Setting >= start))\
                | ((visible.Setting < visible.Rising) & ~((visible.Setting < start) & (stop < visible.Rising)))\
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
