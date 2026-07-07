
from skyfield.api import Star
from ....catalogs import Catalogs
from ....utils import planetary

class BodyResolver:
    """
    Utility to resolve celestial bodies from catalogs or planetary data.
    """
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
        if body_type == "planet":
            return self._planets.get(name)

        if body_type == "star":
            # Handle multiple names or single name
            names = [name] if isinstance(name, str) else name
            for n in names:
                row = self.catalogs.BRIGHT_STARS[self.catalogs.BRIGHT_STARS['Name'] == n]
                if not row.empty:
                    return (n, Star(ra_hours=row['ra_hours'].values[0], dec_degrees=row['dec_degrees'].values[0]))

        if body_type == "messier":
            row = self.catalogs.MESSIER[self.catalogs.MESSIER['Messier'] == name]
            if not row.empty:
                return (name, Star(ra_hours=row['ra_hours'].values[0], dec_degrees=row['dec_degrees'].values[0]))

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
