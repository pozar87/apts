from .objects import Objects
from ..catalogs import Catalogs
from ..constants import ObjectTableLabels
from apts.place import Place
from skyfield.api import Star


class NGC(Objects):
    def __init__(self, place, calculation_date=None):
        super(NGC, self).__init__(place, calculation_date=calculation_date)
        self.objects = Catalogs().NGC.copy()
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
            )  # Add name to avoid issues if Place requires it
            observer_to_use = temp_observer
        else:
            observer_to_use = self.place



        # Compute transit of ngc objects at given place
        self.objects[ObjectTableLabels.TRANSIT] = self.objects.apply(
            lambda body: self._compute_tranzit(self.get_skyfield_object(body), observer_to_use),
            axis=1
        )
        # Compute altitude of ngc objects at transit (at given place)
        self.objects[ObjectTableLabels.ALTITUDE] = self.objects[
            [ObjectTableLabels.TRANSIT]
        ].apply(
            lambda row: self._altitude_at_transit(
                self.get_skyfield_object(self.objects.loc[row.name]), row.Transit, observer_to_use
            ),
            axis=1,
        )

    def _parse_ra(self, ra_str):
        if isinstance(ra_str, str) and ra_str.count(':') == 2:
            parts = ra_str.split(':')
            return float(parts[0]) + float(parts[1])/60 + float(parts[2])/3600
        return None

    def _parse_dec(self, dec_str):
        if isinstance(dec_str, str) and dec_str.count(':') == 2:
            sign = -1 if dec_str.startswith('-') else 1
            parts = dec_str.lstrip('+-').split(':')
            return sign * (float(parts[0]) + float(parts[1])/60 + float(parts[2])/3600)
        return None

    def get_skyfield_object(self, obj):
        ra = self._parse_ra(obj.RA)
        dec = self._parse_dec(obj.Dec)
        if ra is None or dec is None:
            return None
        return Star(ra_hours=ra, dec_degrees=dec)

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
