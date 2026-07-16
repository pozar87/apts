import functools
from .base import Objects
from ..catalogs import Catalogs
from ..constants import ObjectTableLabels


class Messier(Objects):
    is_star_catalog = True

    def __init__(self, place, catalogs: Catalogs, calculation_date=None):
        super(Messier, self).__init__(place, calculation_date=calculation_date)
        self.objects = catalogs.MESSIER.copy()  # type: ignore
        self.objects[ObjectTableLabels.TRANSIT] = None
        self.objects[ObjectTableLabels.RISING] = None
        self.objects[ObjectTableLabels.SETTING] = None
        self.objects[ObjectTableLabels.ALTITUDE] = None
        self.calculation_date = (
            calculation_date  # Store calculation_date for lazy computation
        )

    @functools.lru_cache(maxsize=128)
    def get_skyfield_object_cached(self, obj_id):
        """Cached version of skyfield object retrieval using object ID."""
        # Find object by ID and return its skyfield_object
        obj_row = self.objects.loc[obj_id]
        if "skyfield_object" in self.objects.columns:
            return obj_row["skyfield_object"]
        # Reconstruct from float coords if missing (e.g. after unpickling)
        return self.fixed_body(obj_row["ra_hours"], obj_row["dec_degrees"])

    def get_skyfield_object(self, obj):
        """Get skyfield object with caching when possible."""
        # Identify object ID from namedtuple (Index) or Series (name)
        obj_id = getattr(obj, "Index", getattr(obj, "name", None))

        if obj_id is not None and obj_id in self.objects.index:
            return self.get_skyfield_object_cached(obj_id)

        # Fallback: check for pre-calculated skyfield_object
        if hasattr(obj, "skyfield_object"):
            return getattr(obj, "skyfield_object")
        if isinstance(obj, dict) and "skyfield_object" in obj:
            return obj["skyfield_object"]

        # Reconstruct if possible (using attributes or dictionary keys)
        ra = getattr(obj, "ra_hours", obj.get("ra_hours") if isinstance(obj, dict) else None)
        dec = getattr(obj, "dec_degrees", obj.get("dec_degrees") if isinstance(obj, dict) else None)

        if ra is not None and dec is not None:
            return self.fixed_body(ra, dec)

        return None

    def find_by_name(self, name):
        """
        Finds a Messier object by its name (e.g., "M31").
        """
        result = self.objects[self.objects["Messier"] == name]
        if not result.empty:
            return self.get_skyfield_object(result.iloc[0])
        return None
