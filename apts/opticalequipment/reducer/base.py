from ..abstract import IntermediateOpticalEquipment
from ...constants import OpticalType
from ...units import get_unit_registry
from ...utils import Gender

class Reducer(IntermediateOpticalEquipment):

    @classmethod
    def from_database(cls, entry):
        from ...utils import Utils, Gender
        brand = entry['brand']
        name = entry['name']
        vendor = f'{brand} {name}'
        ol = entry.get('optical_length', 0)
        mass = entry.get('mass', 0)
        tt = Utils.map_conn(entry.get('tside_thread'))
        tg = Utils.map_gender(entry.get('tside_gender'))
        ct = Utils.map_conn(entry.get('cside_thread'))
        cg = Utils.map_gender(entry.get('cside_gender'))
        mag = Utils.extract_number(name, suffix='x') or 0.8
        return cls(vendor, magnification=mag, optical_length=ol, mass=mass, required_backfocus=55, in_connection_type=tt, out_connection_type=ct, in_gender=tg or Gender.MALE, out_gender=cg or Gender.FEMALE)

    def __init__(self, vendor, magnification=0.8, optical_length=0, mass=0, required_backfocus=None, in_connection_type=None, out_connection_type=None, in_gender=Gender.MALE, out_gender=Gender.FEMALE):
        super(Reducer, self).__init__(vendor, optical_length=optical_length, mass=mass, in_connection_type=in_connection_type, out_connection_type=out_connection_type, in_gender=in_gender, out_gender=out_gender)
        self._type = OpticalType.REDUCER
        self.magnification = magnification
        self.required_backfocus = required_backfocus * get_unit_registry().mm if required_backfocus is not None else None

class Flattener(IntermediateOpticalEquipment):

    @classmethod
    def from_database(cls, entry):
        from ...utils import Utils, Gender
        brand = entry['brand']
        name = entry['name']
        vendor = f'{brand} {name}'
        ol = entry.get('optical_length', 0)
        mass = entry.get('mass', 0)
        tt = Utils.map_conn(entry.get('tside_thread'))
        tg = Utils.map_gender(entry.get('tside_gender'))
        ct = Utils.map_conn(entry.get('cside_thread'))
        cg = Utils.map_gender(entry.get('cside_gender'))
        mag = 1.0
        return cls(vendor, magnification=mag, optical_length=ol, mass=mass, required_backfocus=55, in_connection_type=tt, out_connection_type=ct, in_gender=tg or Gender.MALE, out_gender=cg or Gender.FEMALE)

    def __init__(self, vendor, magnification=1.0, optical_length=0, mass=0, required_backfocus=None, in_connection_type=None, out_connection_type=None, in_gender=Gender.MALE, out_gender=Gender.FEMALE):
        super(Flattener, self).__init__(vendor, optical_length=optical_length, mass=mass, in_connection_type=in_connection_type, out_connection_type=out_connection_type, in_gender=in_gender, out_gender=out_gender)
        self._type = OpticalType.FLATTENER
        self.magnification = magnification
        self.required_backfocus = required_backfocus * get_unit_registry().mm if required_backfocus is not None else None

class Corrector(IntermediateOpticalEquipment):

    @classmethod
    def from_database(cls, entry):
        from ...utils import Utils, Gender
        brand = entry['brand']
        name = entry['name']
        vendor = f'{brand} {name}'
        ol = entry.get('optical_length', 0)
        mass = entry.get('mass', 0)
        tt = Utils.map_conn(entry.get('tside_thread'))
        tg = Utils.map_gender(entry.get('tside_gender'))
        ct = Utils.map_conn(entry.get('cside_thread'))
        cg = Utils.map_gender(entry.get('cside_gender'))
        mag = 1.0
        return cls(vendor, magnification=mag, optical_length=ol, mass=mass, required_backfocus=55, in_connection_type=tt, out_connection_type=ct, in_gender=tg or Gender.MALE, out_gender=cg or Gender.FEMALE)

    def __init__(self, vendor, magnification=1.0, optical_length=0, mass=0, required_backfocus=None, in_connection_type=None, out_connection_type=None, in_gender=Gender.MALE, out_gender=Gender.FEMALE):
        super(Corrector, self).__init__(vendor, optical_length=optical_length, mass=mass, in_connection_type=in_connection_type, out_connection_type=out_connection_type, in_gender=in_gender, out_gender=out_gender)
        self._type = OpticalType.CORRECTOR
        self.magnification = magnification
        self.required_backfocus = required_backfocus * get_unit_registry().mm if required_backfocus is not None else None