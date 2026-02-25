from ...abstract import IntermediateOpticalEquipment
from ....constants import OpticalType
from ....units import get_unit_registry
from ....utils import Gender
from ..base import Reducer, Flattener, Corrector

class SvbonyReducer(Reducer):
    _DATABASE = {'SVBony_SV196_0_8x_Reducer': {'brand': 'SVBony', 'name': 'SV196 0.8x Reducer', 'type': 'type_reducer', 'optical_length': 0, 'mass': 220, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'SVBony_0_8x_Reducer_M42': {'brand': 'SVBony', 'name': '0.8x Reducer (M42)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def SVBony_SV196_0_8x_Reducer(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV196_0_8x_Reducer'])

    @classmethod
    def SVBony_0_8x_Reducer_M42(cls):
        return cls.from_database(cls._DATABASE['SVBony_0_8x_Reducer_M42'])

class SvbonyFlattener(Flattener):
    _DATABASE = {'SVBony_SV193_Field_Flattener': {'brand': 'SVBony', 'name': 'SV193 Field Flattener', 'type': 'type_flattener', 'optical_length': 0, 'mass': 180, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def SVBony_SV193_Field_Flattener(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV193_Field_Flattener'])

class SvbonyCorrector(Corrector):
    _DATABASE = {'SVBony_SV193_Coma_Corrector': {'brand': 'SVBony', 'name': 'SV193 Coma Corrector', 'type': 'type_corrector', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'SVBony_SV116_Coma_Corrector': {'brand': 'SVBony', 'name': 'SV116 Coma Corrector', 'type': 'type_corrector', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def SVBony_SV193_Coma_Corrector(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV193_Coma_Corrector'])

    @classmethod
    def SVBony_SV116_Coma_Corrector(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV116_Coma_Corrector'])