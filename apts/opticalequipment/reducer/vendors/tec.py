from ...abstract import IntermediateOpticalEquipment
from ....constants import OpticalType
from ....units import get_unit_registry
from ....utils import Gender
from ..base import Reducer, Flattener, Corrector

class TecReducer(Reducer):
    _DATABASE = {'TEC_TEC_140_Reducer_0_72x': {'brand': 'TEC', 'name': 'TEC-140 Reducer 0.72x', 'type': 'type_reducer', 'optical_length': 0, 'mass': 350, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'TEC_TEC_180_Reducer_0_72x': {'brand': 'TEC', 'name': 'TEC-180 Reducer 0.72x', 'type': 'type_reducer', 'optical_length': 0, 'mass': 450, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def TEC_TEC_140_Reducer_0_72x(cls):
        return cls.from_database(cls._DATABASE['TEC_TEC_140_Reducer_0_72x'])

    @classmethod
    def TEC_TEC_180_Reducer_0_72x(cls):
        return cls.from_database(cls._DATABASE['TEC_TEC_180_Reducer_0_72x'])

class TecFlattener(Flattener):
    _DATABASE = {'TEC_TEC_110_Flattener': {'brand': 'TEC', 'name': 'TEC-110 Flattener', 'type': 'type_flattener', 'optical_length': 0, 'mass': 280, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'TEC_TEC_160_Flattener': {'brand': 'TEC', 'name': 'TEC-160 Flattener', 'type': 'type_flattener', 'optical_length': 0, 'mass': 400, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def TEC_TEC_110_Flattener(cls):
        return cls.from_database(cls._DATABASE['TEC_TEC_110_Flattener'])

    @classmethod
    def TEC_TEC_160_Flattener(cls):
        return cls.from_database(cls._DATABASE['TEC_TEC_160_Flattener'])