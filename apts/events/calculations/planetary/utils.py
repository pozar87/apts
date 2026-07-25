
from skyfield.api import Star
from ....catalogs import Catalogs
from ....utils import planetary

class BodyResolver:
    """
    Utility to resolve celestial bodies from catalogs or planetary data.
    """
    # Class-level cache to store resolved celestial bodies and avoid redundant filtering/instantiations
    _cache = {}

    def __init__(self):
        self._catalogs = None
        # Common planetary bodies
        self._planets = {
            "Mars": ("Mars", planetary.get_skyfield_obj("mars barycenter")),
            "Uranus": ("Uranus", planetary.get_skyfield_obj("uranus barycenter")),
            "Venus": ("Venus", planetary.get_skyfield_obj("venus")),
            "Moon": ("Moon", planetary.get_skyfield_obj("moon")),
        }

    @property
    def catalogs(self):
        if self._catalogs is None:
            self._catalogs = Catalogs()
        return self._catalogs

    def resolve(self, name, body_type="planet"):
        """
        Resolves a body by name and type.
        """
        # Ensure name is hashable for cache key safety (e.g. convert lists to tuples)
        cache_key = (tuple(name) if isinstance(name, list) else name, body_type)
        if cache_key in self._cache:
            return self._cache[cache_key]

        if body_type == "planet":
            result = self._planets.get(name)
            self._cache[cache_key] = result
            return result

        if body_type == "star":
            # Handle multiple names or single name
            names = [name] if isinstance(name, str) else name
            for n in names:
                row = self.catalogs.BRIGHT_STARS[self.catalogs.BRIGHT_STARS['Name'] == n]
                if not row.empty:
                    # Optimization: Reuse the pre-calculated skyfield_object column
                    # instead of re-instantiating the Star class.
                    sky_obj = row['skyfield_object'].values[0]
                    result = (n, sky_obj)
                    self._cache[cache_key] = result
                    return result

        if body_type == "messier":
            row = self.catalogs.MESSIER[self.catalogs.MESSIER['Messier'] == name]
            if not row.empty:
                # Optimization: Reuse the pre-calculated skyfield_object column
                # instead of re-instantiating the Star class.
                sky_obj = row['skyfield_object'].values[0]
                result = (name, sky_obj)
                self._cache[cache_key] = result
                return result

        self._cache[cache_key] = None
        return None

    def resolve_multi(self, body_definitions):
        """
        Resolves a list of bodies.
        Each definition is (name, type).
        """
        resolved = []
        for name, b_type in body_definitions:
            res = self.resolve(name, b_type)
            if res:
                resolved.append(res)
            else:
                # If any body cannot be resolved, we might want to flag it
                return None
        return resolved
