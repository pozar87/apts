from datetime import timedelta

import numpy
import pandas
import pint

from .objects import Objects
from ..constants import ObjectTableLabels
from ..utils import ureg
from apts.place import Place
from skyfield.api import load
from skyfield import almanac


class SolarObjects(Objects):
    def __init__(self, place):
        super(SolarObjects, self).__init__(place)
        self.eph = load("de421.bsp")
        # Init object list with all planets
        self.objects = pandas.DataFrame(
            [
                "MERCURY",
                "VENUS",
                "MARS",
                "JUPITER BARYCENTER",
                "SATURN BARYCENTER",
                "URANUS BARYCENTER",
                "NEPTUNE BARYCENTER",
                "MOON",
                "SUN",
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
        self.compute()

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
        # Compute rising of planets at given place
        self.objects[ObjectTableLabels.RISING] = self.objects[
            [ObjectTableLabels.OBJECT]
        ].apply(lambda body: self._compute_rising(body.Object, observer_to_use), axis=1)
        # Compute transit of planets at given place
        self.objects[ObjectTableLabels.SETTING] = self.objects[
            [ObjectTableLabels.OBJECT]
        ].apply(
            lambda body: self._compute_setting(body.Object, observer_to_use), axis=1
        )
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
        self.objects[ObjectTableLabels.MAGNITUDE] = self.objects[
            [ObjectTableLabels.OBJECT]
        ].apply(
            lambda body: almanac.oppositions_conjunctions(self.eph, body.Object)(t)
            if body.name != "Sun" and body.name != "Moon"
            else 0,
            axis=1,
        )
        # Calculate planets RA
        self.objects[ObjectTableLabels.RA] = self.objects[
            [ObjectTableLabels.OBJECT]
        ].apply(
            lambda body: body.Object.at(t)
            .observe(self.place.observer)
            .radec()[0]
            .hours,
            axis=1,
        )
        # Calculate planets Dec
        self.objects[ObjectTableLabels.DEC] = self.objects[
            [ObjectTableLabels.OBJECT]
        ].apply(
            lambda body: body.Object.at(t)
            .observe(self.place.observer)
            .radec()[1]
            .degrees,
            axis=1,
        )
        # Calculate planets distance from Earth
        self.objects[ObjectTableLabels.DISTANCE] = self.objects[
            [ObjectTableLabels.OBJECT]
        ].apply(
            lambda body: body.Object.at(t).observe(self.place.observer).distance().au,
            axis=1,
        )
        # Calculate planets size
        self.objects[ObjectTableLabels.SIZE] = self.objects[
            [ObjectTableLabels.OBJECT]
        ].apply(
            lambda body: body.Object.radius.km if hasattr(body.Object, "radius") else 0,
            axis=1,
        )
        # Calculate planets elongation
        self.objects[ObjectTableLabels.ELONGATION] = self.objects[
            [ObjectTableLabels.OBJECT]
        ].apply(
            lambda body: body.Object.at(t)
            .observe(self.place.observer)
            .separation_from(self.place.sun.at(t))
            .degrees,
            axis=1,
        )
        # Calculate planets phase
        self.objects[ObjectTableLabels.PHASE] = self.objects[
            [ObjectTableLabels.OBJECT]
        ].apply(
            lambda body: body.Object.at(t)
            .observe(self.place.observer)
            .phase_angle(self.place.sun)
            .degrees,
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
