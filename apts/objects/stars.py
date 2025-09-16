from .objects import Objects
from ..catalogs import Catalogs
from ..constants import ObjectTableLabels
from apts.place import Place
from skyfield.api import Star


class Stars(Objects):
    def __init__(self, place, calculation_date=None):
        super(Stars, self).__init__(place, calculation_date=calculation_date)
        self.objects = Catalogs().BRIGHT_STARS.copy()
        self.calculation_date = calculation_date # Store calculation_date for lazy computation

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
            )
            observer_to_use = temp_observer
        else:
            observer_to_use = self.place

        # Compute transit of stars at given place
        self.objects[ObjectTableLabels.TRANSIT] = self.objects.apply(
            lambda body: self._compute_tranzit(self.get_skyfield_object(body), observer_to_use),
            axis=1
        )
        # Compute altitude of stars at transit (at given place)
        self.objects[ObjectTableLabels.ALTITUDE] = self.objects[
            [ObjectTableLabels.TRANSIT]
        ].apply(
            lambda row: self._altitude_at_transit(
                self.get_skyfield_object(self.objects.loc[row.name]), row.Transit, observer_to_use
            ),
            axis=1,
        )

    def get_skyfield_object(self, obj):
        return Star(ra_hours=obj.RA, dec_degrees=obj.Dec)

    def find_by_name(self, name):
        """
        Finds a star by its name (e.g., "Sirius").
        """
        result = self.objects[self.objects["Name"] == name]
        if not result.empty:
            return self.get_skyfield_object(result.iloc[0])
        return None
