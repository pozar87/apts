from ...abstract import IntermediateOpticalEquipment
from ....constants import OpticalType
from ....units import get_unit_registry
from ....utils import Gender
from ..base import Reducer, Flattener, Corrector

class William_opticsReducer(Reducer):
    _DATABASE = {'William_Optics_Reducer_Flat_0_8x': {'brand': 'William Optics', 'name': 'Reducer Flat 0.8x', 'type': 'type_reducer', 'optical_length': 0, 'mass': 300, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'William_Optics_AFR_IV_0_8x': {'brand': 'William Optics', 'name': 'AFR-IV 0.8x', 'type': 'type_reducer', 'optical_length': 0, 'mass': 320, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'William_Optics_Flat61R': {'brand': 'William Optics', 'name': 'Flat61R', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'William_Optics_RedCat_Reducer_0_8x': {'brand': 'William Optics', 'name': 'RedCat Reducer 0.8x', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def William_Optics_Reducer_Flat_0_8x(cls):
        return cls.from_database(cls._DATABASE['William_Optics_Reducer_Flat_0_8x'])

    @classmethod
    def William_Optics_AFR_IV_0_8x(cls):
        return cls.from_database(cls._DATABASE['William_Optics_AFR_IV_0_8x'])

    @classmethod
    def William_Optics_Flat61R(cls):
        return cls.from_database(cls._DATABASE['William_Optics_Flat61R'])

    @classmethod
    def William_Optics_RedCat_Reducer_0_8x(cls):
        return cls.from_database(cls._DATABASE['William_Optics_RedCat_Reducer_0_8x'])

class William_opticsFlattener(Flattener):
    _DATABASE = {'William_Optics_Flat68_III': {'brand': 'William Optics', 'name': 'Flat68 III', 'type': 'type_flattener', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'William_Optics_P_FLAT_68': {'brand': 'William Optics', 'name': 'P-FLAT 68', 'type': 'type_flattener', 'optical_length': 0, 'mass': 280, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'William_Optics_P_FLAT_73': {'brand': 'William Optics', 'name': 'P-FLAT 73', 'type': 'type_flattener', 'optical_length': 0, 'mass': 290, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def William_Optics_Flat68_III(cls):
        return cls.from_database(cls._DATABASE['William_Optics_Flat68_III'])

    @classmethod
    def William_Optics_P_FLAT_68(cls):
        return cls.from_database(cls._DATABASE['William_Optics_P_FLAT_68'])

    @classmethod
    def William_Optics_P_FLAT_73(cls):
        return cls.from_database(cls._DATABASE['William_Optics_P_FLAT_73'])