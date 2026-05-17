from ...base import Adapter, Spacer
from .m42 import ADAPTERS as m42_a, SPACERS as m42_s
from .m48 import ADAPTERS as m48_a, SPACERS as m48_s
from .m54 import ADAPTERS as m54_a, SPACERS as m54_s
from .m68 import ADAPTERS as m68_a, SPACERS as m68_s
from .large_metric import ADAPTERS as lm_a, SPACERS as lm_s
from .small_metric import ADAPTERS as sm_a, SPACERS as sm_s
from .sc import ADAPTERS as sc_a, SPACERS as sc_s
from .barrels import ADAPTERS as b_a, SPACERS as b_s
from .mounts import ADAPTERS as mount_a, SPACERS as mount_s
from .other import ADAPTERS as o_a, SPACERS as o_s

class GenericAdapter(Adapter):
    _DATABASE = {}
    _DATABASE.update(m42_a)
    _DATABASE.update(m48_a)
    _DATABASE.update(m54_a)
    _DATABASE.update(m68_a)
    _DATABASE.update(lm_a)
    _DATABASE.update(sm_a)
    _DATABASE.update(sc_a)
    _DATABASE.update(b_a)
    _DATABASE.update(mount_a)
    _DATABASE.update(o_a)

    @classmethod
    def _add_factory_methods(cls):
        def create_factory(key):
            @classmethod
            def factory(c):
                return c.from_database(c._DATABASE[key])
            return factory
        for key in cls._DATABASE:
            setattr(cls, key, create_factory(key))

GenericAdapter._add_factory_methods()

class GenericSpacer(Spacer):
    _DATABASE = {}
    _DATABASE.update(m42_s)
    _DATABASE.update(m48_s)
    _DATABASE.update(m54_s)
    _DATABASE.update(m68_s)
    _DATABASE.update(lm_s)
    _DATABASE.update(sm_s)
    _DATABASE.update(sc_s)
    _DATABASE.update(b_s)
    _DATABASE.update(mount_s)
    _DATABASE.update(o_s)

    @classmethod
    def _add_factory_methods(cls):
        def create_factory(key):
            @classmethod
            def factory(c):
                return c.from_database(c._DATABASE[key])
            return factory
        for key in cls._DATABASE:
            setattr(cls, key, create_factory(key))

GenericSpacer._add_factory_methods()
