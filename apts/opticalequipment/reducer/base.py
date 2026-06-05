from ..abstract import IntermediateOpticalEquipment
from ...constants import OpticalType
from ...units import get_unit_registry

class Reducer(IntermediateOpticalEquipment):
    path_layer = 2
    _DATABASE = {}

    @classmethod
    def from_database(cls, entry):
        from ...utils import map_conn, map_gender, extract_number
        brand = entry['brand']
        name = entry['name']
        vendor = f'{brand} {name}'
        ol = entry.get('optical_length', 0)
        mass = entry.get('mass', 0)
        tt = map_conn(entry.get('tside_thread'))
        tg = map_gender(entry.get('tside_gender'))
        ct = map_conn(entry.get('cside_thread'))
        cg = map_gender(entry.get('cside_gender'))
        mag = extract_number(name, suffix='x') or 0.8
        bf = entry.get('required_backfocus', 55)

        inputs = entry.get('inputs')
        if inputs is None:
            inputs = [(tt, tg)] if tt else []
        else:
            inputs = [(map_conn(c), map_gender(g)) if isinstance(c, str) else (c, g) for c, g in inputs]

        outputs = entry.get('outputs')
        if outputs is None:
            outputs = [(ct, cg)] if ct else []
        else:
            outputs = [(map_conn(c), map_gender(g)) if isinstance(c, str) else (c, g) for c, g in outputs]

        return cls(vendor, magnification=mag, optical_length=ol, mass=mass, required_backfocus=bf, inputs=inputs, outputs=outputs)

    def __init__(self, vendor, magnification=0.8, optical_length=0, mass=0, required_backfocus=None, inputs=None, outputs=None, in_connection=None, out_connection=None, in_connection_type=None, out_connection_type=None, in_gender=None, out_gender=None):
        super(Reducer, self).__init__(vendor, optical_length=optical_length, mass=mass, inputs=inputs, outputs=outputs, in_connection=in_connection, out_connection=out_connection, in_connection_type=in_connection_type, out_connection_type=out_connection_type, in_gender=in_gender, out_gender=out_gender)
        self._type = OpticalType.REDUCER
        self.magnification = magnification
        self.required_backfocus = required_backfocus * get_unit_registry().mm if required_backfocus is not None else None

class Flattener(IntermediateOpticalEquipment):
    path_layer = 2
    _DATABASE = {}

    @classmethod
    def from_database(cls, entry):
        from ...utils import map_conn, map_gender
        brand = entry['brand']
        name = entry['name']
        vendor = f'{brand} {name}'
        ol = entry.get('optical_length', 0)
        mass = entry.get('mass', 0)
        tt = map_conn(entry.get('tside_thread'))
        tg = map_gender(entry.get('tside_gender'))
        ct = map_conn(entry.get('cside_thread'))
        cg = map_gender(entry.get('cside_gender'))
        mag = 1.0
        bf = entry.get('required_backfocus', 55)

        inputs = entry.get('inputs')
        if inputs is None:
            inputs = [(tt, tg)] if tt else []
        else:
            inputs = [(map_conn(c), map_gender(g)) if isinstance(c, str) else (c, g) for c, g in inputs]

        outputs = entry.get('outputs')
        if outputs is None:
            outputs = [(ct, cg)] if ct else []
        else:
            outputs = [(map_conn(c), map_gender(g)) if isinstance(c, str) else (c, g) for c, g in outputs]

        return cls(vendor, magnification=mag, optical_length=ol, mass=mass, required_backfocus=bf, inputs=inputs, outputs=outputs)

    def __init__(self, vendor, magnification=1.0, optical_length=0, mass=0, required_backfocus=None, inputs=None, outputs=None, in_connection=None, out_connection=None, in_connection_type=None, out_connection_type=None, in_gender=None, out_gender=None):
        super(Flattener, self).__init__(vendor, optical_length=optical_length, mass=mass, inputs=inputs, outputs=outputs, in_connection=in_connection, out_connection=out_connection, in_connection_type=in_connection_type, out_connection_type=out_connection_type, in_gender=in_gender, out_gender=out_gender)
        self._type = OpticalType.FLATTENER
        self.magnification = magnification
        self.required_backfocus = required_backfocus * get_unit_registry().mm if required_backfocus is not None else None

class Corrector(IntermediateOpticalEquipment):
    path_layer = 2
    _DATABASE = {}

    @classmethod
    def from_database(cls, entry):
        from ...utils import map_conn, map_gender
        brand = entry['brand']
        name = entry['name']
        vendor = f'{brand} {name}'
        ol = entry.get('optical_length', 0)
        mass = entry.get('mass', 0)
        tt = map_conn(entry.get('tside_thread'))
        tg = map_gender(entry.get('tside_gender'))
        ct = map_conn(entry.get('cside_thread'))
        cg = map_gender(entry.get('cside_gender'))
        mag = 1.0
        bf = entry.get('required_backfocus', 55)

        inputs = entry.get('inputs')
        if inputs is None:
            inputs = [(tt, tg)] if tt else []
        else:
            inputs = [(map_conn(c), map_gender(g)) if isinstance(c, str) else (c, g) for c, g in inputs]

        outputs = entry.get('outputs')
        if outputs is None:
            outputs = [(ct, cg)] if ct else []
        else:
            outputs = [(map_conn(c), map_gender(g)) if isinstance(c, str) else (c, g) for c, g in outputs]

        return cls(vendor, magnification=mag, optical_length=ol, mass=mass, required_backfocus=bf, inputs=inputs, outputs=outputs)

    def __init__(self, vendor, magnification=1.0, optical_length=0, mass=0, required_backfocus=None, inputs=None, outputs=None, in_connection=None, out_connection=None, in_connection_type=None, out_connection_type=None, in_gender=None, out_gender=None):
        super(Corrector, self).__init__(vendor, optical_length=optical_length, mass=mass, inputs=inputs, outputs=outputs, in_connection=in_connection, out_connection=out_connection, in_connection_type=in_connection_type, out_connection_type=out_connection_type, in_gender=in_gender, out_gender=out_gender)
        self._type = OpticalType.CORRECTOR
        self.magnification = magnification
        self.required_backfocus = required_backfocus * get_unit_registry().mm if required_backfocus is not None else None