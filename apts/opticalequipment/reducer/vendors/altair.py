from ...abstract import IntermediateOpticalEquipment
from ....constants import OpticalType
from ....units import get_unit_registry
from ....utils import Gender
from ..base import Reducer, Flattener, Corrector

class AltairReducer(Reducer):
    _DATABASE = {'Altair_0_8x_Reducer_M48': {'brand': 'Altair', 'name': '0.8x Reducer (M48)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Altair_Lightwave_0_8x_Reducer': {'brand': 'Altair', 'name': 'Lightwave 0.8x Reducer', 'type': 'type_reducer', 'optical_length': 0, 'mass': 220, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Altair_0_6x_Reducer_M48': {'brand': 'Altair', 'name': '0.6x Reducer (M48)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 280, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Altair_0_8x_Reducer_M48(cls):
        return cls.from_database(cls._DATABASE['Altair_0_8x_Reducer_M48'])

    @classmethod
    def Altair_Lightwave_0_8x_Reducer(cls):
        return cls.from_database(cls._DATABASE['Altair_Lightwave_0_8x_Reducer'])

    @classmethod
    def Altair_0_6x_Reducer_M48(cls):
        return cls.from_database(cls._DATABASE['Altair_0_6x_Reducer_M48'])

class AltairFlattener(Flattener):
    _DATABASE = {'Altair_Lightwave_Flattener_M48': {'brand': 'Altair', 'name': 'Lightwave Flattener (M48)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 230, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Altair_Lightwave_Flattener': {'brand': 'Altair', 'name': 'Lightwave Flattener', 'type': 'type_flattener', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Altair_Lightwave_Flattener_M48(cls):
        return cls.from_database(cls._DATABASE['Altair_Lightwave_Flattener_M48'])

    @classmethod
    def Altair_Lightwave_Flattener(cls):
        return cls.from_database(cls._DATABASE['Altair_Lightwave_Flattener'])