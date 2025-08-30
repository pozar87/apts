from .objects import Objects
from ..catalogs import Catalogs
from ..constants import ObjectTableLabels
from apts.place import Place
import numpy
from skyfield.api import Star


class Messier(Objects):
    def __init__(self, place, calculation_date=None):
        super(Messier, self).__init__(place)
        self.objects = Catalogs().MESSIER.copy()
        self.compute(calculation_date)

    def compute(self, calculation_date=None):
        if calculation_date is not None:
            # It's a Skyfield Time object. If it's an array, use the first element.
            if hasattr(calculation_date, "shape") and calculation_date.shape:
                calculation_date = calculation_date[0]

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

        

        # Compute transit of messier objects at given place
        self.objects[ObjectTableLabels.TRANSIT] = self.objects.apply(
            lambda body: self._compute_tranzit(self.get_skyfield_object(body), observer_to_use),
            axis=1
        )
        # Compute altitude of messier objects at transit (at given place)
        self.objects[ObjectTableLabels.ALTITUDE] = self.objects[
            [ObjectTableLabels.TRANSIT]
        ].apply(
            lambda row: self._altitude_at_transit(
                self.get_skyfield_object(self.objects.loc[row.name]), row.Transit, observer_to_use
            ),
            axis=1,
        )

    def get_skyfield_object(self, messier_object):
        return Star(ra_hours=messier_object.RA, dec_degrees=messier_object.Dec)

    def find_by_name(self, name):
        """
        Finds a Messier object by its name (e.g., "M31").
        """
        result = self.objects[self.objects["Messier"] == name]
        if not result.empty:
            return self.get_skyfield_object(result.iloc[0])
        return None
