import pandas as pd
from .objects import Objects
from ..catalogs import Catalogs
from ..constants import ObjectTableLabels
from apts.place import Place


class NGC(Objects):
    def __init__(self, place, catalogs: Catalogs, calculation_date=None):
        super(NGC, self).__init__(place, calculation_date=calculation_date)
        self.objects = catalogs.NGC.copy() # type: ignore
        self.objects[ObjectTableLabels.TRANSIT] = None
        self.objects[ObjectTableLabels.ALTITUDE] = pd.NA
        self.calculation_date = calculation_date # Store calculation_date for lazy computation

    def compute(self, calculation_date=None, df_to_compute=None):
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

        # If no specific DataFrame is provided, use the class's default.
        if df_to_compute is None:
            df_to_compute = self.objects

        # Work on a copy to avoid modifying the original DataFrame slice
        computed_df = df_to_compute.copy()

        # Compute transit of ngc objects at given place
        computed_df[ObjectTableLabels.TRANSIT] = computed_df.apply(
            lambda body: self._compute_tranzit(self.get_skyfield_object(body), observer_to_use),
            axis=1
        )
        # Compute altitude of ngc objects at transit (at given place)
        computed_df[ObjectTableLabels.ALTITUDE] = computed_df.apply(
            lambda row: self._altitude_at_transit(
                self.get_skyfield_object(row), row.Transit, observer_to_use
            ),
            axis=1,
        )
        self.objects.update(computed_df)
        return computed_df

    def get_skyfield_object(self, obj):
        return obj.skyfield_object

    def find_by_name(self, name):
        """
        Finds a NGC object by its name (e.g., "NGC 224").
        """
        result = self.objects[
            (self.objects["NGC"] == name) | (self.objects["Name"] == name)
        ]
        if not result.empty:
            return self.get_skyfield_object(result.iloc[0])
        return None
