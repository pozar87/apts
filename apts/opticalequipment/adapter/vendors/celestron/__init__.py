from ...base import Adapter, Spacer
from .adapters import DATABASE as a_db
from .spacers import DATABASE as s_db

class CelestronAdapter(Adapter):
    _DATABASE = a_db
    @classmethod
    def _add_factory_methods(cls):
        def create_factory(key):
            return classmethod(lambda c: c.from_database(c._DATABASE[key]))
        for key in cls._DATABASE:
            setattr(cls, key, create_factory(key))
CelestronAdapter._add_factory_methods()

class CelestronSpacer(Spacer):
    _DATABASE = s_db
    @classmethod
    def _add_factory_methods(cls):
        def create_factory(key):
            return classmethod(lambda c: c.from_database(c._DATABASE[key]))
        for key in cls._DATABASE:
            setattr(cls, key, create_factory(key))
CelestronSpacer._add_factory_methods()
