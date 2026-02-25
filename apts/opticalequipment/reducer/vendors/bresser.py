from ...abstract import IntermediateOpticalEquipment
from ....constants import OpticalType
from ....units import get_unit_registry
from ....utils import Gender
from ..base import Reducer, Flattener, Corrector

class BresserReducer(Reducer):
    _DATABASE = {'Bresser_0_8x_Reducer_M48': {'brand': 'Bresser', 'name': '0.8x Reducer (M48)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Bresser_0_8x_Reducer_M48(cls):
        return cls.from_database(cls._DATABASE['Bresser_0_8x_Reducer_M48'])

class BresserFlattener(Flattener):
    _DATABASE = {'Bresser_Field_Flattener_M48': {'brand': 'Bresser', 'name': 'Field Flattener (M48)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Bresser_Field_Flattener_M48(cls):
        return cls.from_database(cls._DATABASE['Bresser_Field_Flattener_M48'])