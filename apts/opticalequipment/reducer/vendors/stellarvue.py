from ...abstract import IntermediateOpticalEquipment
from ....constants import OpticalType
from ....units import get_unit_registry
from ....utils import Gender
from ..base import Reducer, Flattener, Corrector

class StellarvueReducer(Reducer):
    _DATABASE = {'Stellarvue_SFFR_72_130_Reducer': {'brand': 'Stellarvue', 'name': 'SFFR.72-130 Reducer', 'type': 'type_reducer', 'optical_length': 0, 'mass': 350, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Stellarvue_SVR102_Reducer_0_72x': {'brand': 'Stellarvue', 'name': 'SVR102 Reducer 0.72x', 'type': 'type_reducer', 'optical_length': 0, 'mass': 280, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Stellarvue_SVR80_102_Reducer': {'brand': 'Stellarvue', 'name': 'SVR80-102 Reducer', 'type': 'type_reducer', 'optical_length': 0, 'mass': 260, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Stellarvue_SVR80_Reducer_0_8x': {'brand': 'Stellarvue', 'name': 'SVR80 Reducer 0.8x', 'type': 'type_reducer', 'optical_length': 0, 'mass': 260, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Stellarvue_SFFR_72_80_Reducer': {'brand': 'Stellarvue', 'name': 'SFFR.72-80 Reducer', 'type': 'type_reducer', 'optical_length': 0, 'mass': 280, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Stellarvue_SFFR_72_102_Reducer': {'brand': 'Stellarvue', 'name': 'SFFR.72-102 Reducer', 'type': 'type_reducer', 'optical_length': 0, 'mass': 300, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Stellarvue_SFFR_72_130_Reducer(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_SFFR_72_130_Reducer'])

    @classmethod
    def Stellarvue_SVR102_Reducer_0_72x(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_SVR102_Reducer_0_72x'])

    @classmethod
    def Stellarvue_SVR80_102_Reducer(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_SVR80_102_Reducer'])

    @classmethod
    def Stellarvue_SVR80_Reducer_0_8x(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_SVR80_Reducer_0_8x'])

    @classmethod
    def Stellarvue_SFFR_72_80_Reducer(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_SFFR_72_80_Reducer'])

    @classmethod
    def Stellarvue_SFFR_72_102_Reducer(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_SFFR_72_102_Reducer'])

class StellarvueFlattener(Flattener):
    _DATABASE = {'Stellarvue_SVF25_Flattener': {'brand': 'Stellarvue', 'name': 'SVF25 Flattener', 'type': 'type_flattener', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Stellarvue_SVF25_78_Flattener': {'brand': 'Stellarvue', 'name': 'SVF25-78 Flattener', 'type': 'type_flattener', 'optical_length': 0, 'mass': 230, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Stellarvue_SVF50_Flattener': {'brand': 'Stellarvue', 'name': 'SVF50 Flattener', 'type': 'type_flattener', 'optical_length': 0, 'mass': 220, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Stellarvue_SFF_Flattener_M68': {'brand': 'Stellarvue', 'name': 'SFF Flattener (M68)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 280, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Stellarvue_SVF25_Flattener(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_SVF25_Flattener'])

    @classmethod
    def Stellarvue_SVF25_78_Flattener(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_SVF25_78_Flattener'])

    @classmethod
    def Stellarvue_SVF50_Flattener(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_SVF50_Flattener'])

    @classmethod
    def Stellarvue_SFF_Flattener_M68(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_SFF_Flattener_M68'])