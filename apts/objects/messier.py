import functools
from .objects import Objects
from ..catalogs import Catalogs
from ..constants import ObjectTableLabels
from apts.place import Place


class Messier(Objects):
    def __init__(self, place, catalogs: Catalogs, calculation_date=None):
        super(Messier, self).__init__(place, calculation_date=calculation_date)
        self.objects = catalogs.MESSIER.copy()
        self.calculation_date = (
            calculation_date  # Store calculation_date for lazy computation
        )

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
            lambda body: self._compute_tranzit(
                self.get_skyfield_object(body), observer_to_use
            ),
            axis=1,
        )
        # Compute altitude of messier objects at transit (at given place)
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

    @functools.lru_cache(maxsize=128)
    def get_skyfield_object_cached(self, obj_id):
        """Cached version of skyfield object retrieval using object ID."""
        # Find object by ID and return its skyfield_object
        obj_row = self.objects.loc[obj_id]
        return obj_row.skyfield_object

    def get_skyfield_object(self, obj):
        """Get skyfield object with caching when possible."""
        if hasattr(obj, "name") and obj.name in self.objects.index:
            return self.get_skyfield_object_cached(obj.name)
        return obj.skyfield_object

    def find_by_name(self, name):
        """
        Finds a Messier object by its name (e.g., "M31").
        """
        result = self.objects[self.objects["Messier"] == name]
        if not result.empty:
            return self.get_skyfield_object(result.iloc[0])
        return None
