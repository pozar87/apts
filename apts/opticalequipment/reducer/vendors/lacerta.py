from ...abstract import IntermediateOpticalEquipment
from ....constants import OpticalType
from ....units import get_unit_registry
from ....utils import Gender
from ..base import Reducer, Flattener, Corrector

class LacertaReducer(Reducer):
    _DATABASE = {'Lacerta_0_8x_Reducer_M48': {'brand': 'Lacerta', 'name': '0.8x Reducer (M48)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 220, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Lacerta_0_72x_Reducer_M48': {'brand': 'Lacerta', 'name': '0.72x Reducer (M48)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Lacerta_0_8x_Reducer_M48(cls):
        return cls.from_database(cls._DATABASE['Lacerta_0_8x_Reducer_M48'])

    @classmethod
    def Lacerta_0_72x_Reducer_M48(cls):
        return cls.from_database(cls._DATABASE['Lacerta_0_72x_Reducer_M48'])

class LacertaFlattener(Flattener):
    _DATABASE = {'Lacerta_2_Flattener_M48': {'brand': 'Lacerta', 'name': '2" Flattener (M48)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Lacerta_2_Flattener_M48(cls):
        return cls.from_database(cls._DATABASE['Lacerta_2_Flattener_M48'])

class LacertaCorrector(Corrector):
    _DATABASE = {'Lacerta_GPU_3_CC_1x': {'brand': 'Lacerta', 'name': 'GPU-3 CC 1x', 'type': 'type_corrector', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Lacerta_Wynne_Corrector_3_M68': {'brand': 'Lacerta', 'name': 'Wynne Corrector 3" (M68)', 'type': 'type_corrector', 'optical_length': 0, 'mass': 480, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Lacerta_GPU_3_CC_1x(cls):
        return cls.from_database(cls._DATABASE['Lacerta_GPU_3_CC_1x'])

    @classmethod
    def Lacerta_Wynne_Corrector_3_M68(cls):
        return cls.from_database(cls._DATABASE['Lacerta_Wynne_Corrector_3_M68'])