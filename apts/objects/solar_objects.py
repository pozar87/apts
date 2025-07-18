from datetime import timedelta

from skyfield.api import load, Topos
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
        self.ts = load.timescale()
        self.eph = load('de421.bsp')
        self.earth = self.eph['earth']
        self.sun = self.eph['sun']
        self.moon = self.eph['moon']
        self.mercury = self.eph['mercury']
        self.venus = self.eph['venus']
        self.mars = self.eph['mars']
        self.jupiter = self.eph['jupiter barycenter']
        self.saturn = self.eph['saturn barycenter']
        self.uranus = self.eph['uranus barycenter']
        self.neptune = self.eph['neptune barycenter']

        self.planets = [
            self.mercury,
            self.venus,
            self.mars,
            self.jupiter,
            self.saturn,
            self.uranus,
            self.neptune,
            self.moon,
            self.sun,
        ]

        self.planet_names = [
            'Mercury',
            'Venus',
            'Mars',
            'Jupiter',
            'Saturn',
            'Uranus',
            'Neptune',
            'Moon',
            'Sun',
        ]

        self.objects = pandas.DataFrame(
            {
                ObjectTableLabels.NAME: self.planet_names,
                ObjectTableLabels.EPHEM: self.planets,
            }
        )
        self.compute()

    def compute(self, calculation_date=None):
        if calculation_date:
            t = self.ts.utc(calculation_date)
        else:
            t = self.ts.now()

        observer = self.earth + Topos(latitude_degrees=self.place.lat_decimal,
                                     longitude_degrees=self.place.lon_decimal,
                                     elevation_m=self.place.elevation)

        def compute_properties(planet):
            astrometric = observer.at(t).observe(planet)
            ra, dec, distance = astrometric.radec()
            alt, az, _ = astrometric.altaz()

            # Placeholder for magnitude, size, elongation, phase
            # Skyfield does not directly provide these for all bodies in the same way as ephem.
            # This would require more complex calculations or external data.
            magnitude = 0
            size = 0
            elongation = 0
            phase = 0

            return pandas.Series({
                ObjectTableLabels.RA: ra.hours * ureg.hour,
                ObjectTableLabels.DEC: dec.degrees * ureg.degree,
                ObjectTableLabels.DISTANCE: distance.au * ureg.AU,
                ObjectTableLabels.ALTITUDE: alt.degrees * ureg.degree,
                ObjectTableLabels.MAGNITUDE: magnitude * ureg.mag,
                ObjectTableLabels.SIZE: size * ureg.arcsecond,
                ObjectTableLabels.ELONGATION: elongation * ureg.degree,
                ObjectTableLabels.PHASE: phase * ureg.dimensionless,
                # Rising, setting, and transit times require a search over time,
                # which is more involved than this compute function.
                # These are placeholders.
                ObjectTableLabels.RISING: t.utc_datetime(),
                ObjectTableLabels.SETTING: t.utc_datetime(),
                ObjectTableLabels.TRANSIT: t.utc_datetime(),
            })

        props = self.objects[ObjectTableLabels.EPHEM].apply(compute_properties)
        self.objects = self.objects.join(props)


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
