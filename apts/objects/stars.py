from .base import Objects
from ..catalogs import Catalogs
from ..constants import ObjectTableLabels


class Stars(Objects):
    is_star_catalog = True

    def __init__(self, place, catalogs: Catalogs, calculation_date=None):
        super(Stars, self).__init__(place, calculation_date=calculation_date)
        self.objects = catalogs.BRIGHT_STARS.copy()  # type: ignore
        self.objects[ObjectTableLabels.TRANSIT] = None
        self.objects[ObjectTableLabels.ALTITUDE] = None
        self.calculation_date = (
            calculation_date  # Store calculation_date for lazy computation
        )

    def get_skyfield_object(self, obj):
        if hasattr(obj, "skyfield_object"):
            return getattr(obj, "skyfield_object")
        if isinstance(obj, dict) and "skyfield_object" in obj:
            return obj["skyfield_object"]

        # Reconstruct if possible
        ra = getattr(obj, "ra_hours", obj.get("ra_hours") if isinstance(obj, dict) else None)
        dec = getattr(obj, "dec_degrees", obj.get("dec_degrees") if isinstance(obj, dict) else None)

        if ra is not None and dec is not None:
            return self.fixed_body(ra, dec)

        return None

    def find_by_name(self, name):
        """
        Finds a star by its name (e.g., "Sirius").
        """
        result = self.objects[self.objects["Name"] == name]
        if not result.empty:
            return self.get_skyfield_object(result.iloc[0])
        return None
