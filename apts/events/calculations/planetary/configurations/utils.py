from skyfield.api import Star
from apts.catalogs import Catalogs
from apts.utils import planetary

class BodyResolver:
    def __init__(self):
        self._catalogs = None

    @property
    def catalogs(self):
        if self._catalogs is None:
            self._catalogs = Catalogs()
        return self._catalogs

    def get_star(self, name):
        row = self.catalogs.BRIGHT_STARS[self.catalogs.BRIGHT_STARS['Name'] == name]
        if not row.empty:
            return (name, Star(ra_hours=row['ra_hours'].values[0], dec_degrees=row['dec_degrees'].values[0]))
        return None

    def get_messier(self, name):
        row = self.catalogs.MESSIER[self.catalogs.MESSIER['Messier'] == name]
        if not row.empty:
            return (name, Star(ra_hours=row['ra_hours'].values[0], dec_degrees=row['dec_degrees'].values[0]))
        return None

    def get_planet(self, name, skyfield_name=None):
        skyfield_name = skyfield_name or name.lower()
        return (name, planetary.get_skyfield_obj(skyfield_name))

    def resolve_bodies(self, body_configs):
        """
        Resolves a list of body configurations into (name, skyfield_obj) tuples.
        """
        resolved = []
        for config in body_configs:
            if isinstance(config, tuple):
                # Already resolved or manually defined
                resolved.append(config)
                continue

            body_type = config.get("type")
            name = config.get("name")

            if body_type == "star":
                resolved.append(self.get_star(name))
            elif body_type == "messier":
                resolved.append(self.get_messier(name))
            elif body_type == "planet":
                resolved.append(self.get_planet(name, config.get("skyfield_name")))
            else:
                resolved.append(None)

        return resolved
