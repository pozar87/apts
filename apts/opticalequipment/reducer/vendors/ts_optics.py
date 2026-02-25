from ...abstract import IntermediateOpticalEquipment
from ....constants import OpticalType
from ....units import get_unit_registry
from ....utils import Gender
from ..base import Reducer, Flattener, Corrector

class Ts_opticsReducer(Reducer):
    _DATABASE = {'TS_Optics_TSRED3_0_79x_Reducer': {'brand': 'TS-Optics', 'name': 'TSRED3 0.79x Reducer', 'type': 'type_reducer', 'optical_length': 0, 'mass': 300, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'TS_Optics_0_8x_Reducer_M48': {'brand': 'TS-Optics', 'name': '0.8x Reducer (M48)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'TS_Optics_TSRED2_0_6x_Reducer': {'brand': 'TS-Optics', 'name': 'TSRED2 0.6x Reducer', 'type': 'type_reducer', 'optical_length': 0, 'mass': 280, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'TS_Optics_TSRED4_0_67x_Reducer': {'brand': 'TS-Optics', 'name': 'TSRED4 0.67x Reducer', 'type': 'type_reducer', 'optical_length': 0, 'mass': 300, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def TS_Optics_TSRED3_0_79x_Reducer(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_TSRED3_0_79x_Reducer'])

    @classmethod
    def TS_Optics_0_8x_Reducer_M48(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_0_8x_Reducer_M48'])

    @classmethod
    def TS_Optics_TSRED2_0_6x_Reducer(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_TSRED2_0_6x_Reducer'])

    @classmethod
    def TS_Optics_TSRED4_0_67x_Reducer(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_TSRED4_0_67x_Reducer'])

class Ts_opticsFlattener(Flattener):
    _DATABASE = {'TS_Optics_Flattener_2_M48': {'brand': 'TS-Optics', 'name': 'Flattener 2" (M48)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 280, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'TS_Optics_TSFlat2_M48': {'brand': 'TS-Optics', 'name': 'TSFlat2 (M48)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'TS_Optics_RC_Flattener_M68': {'brand': 'TS-Optics', 'name': 'RC Flattener (M68)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 350, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'TS_Optics_TSFlat3_M54': {'brand': 'TS-Optics', 'name': 'TSFlat3 (M54)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'TS_Optics_TSFlat4_M68': {'brand': 'TS-Optics', 'name': 'TSFlat4 (M68)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 350, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def TS_Optics_Flattener_2_M48(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Flattener_2_M48'])

    @classmethod
    def TS_Optics_TSFlat2_M48(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_TSFlat2_M48'])

    @classmethod
    def TS_Optics_RC_Flattener_M68(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_RC_Flattener_M68'])

    @classmethod
    def TS_Optics_TSFlat3_M54(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_TSFlat3_M54'])

    @classmethod
    def TS_Optics_TSFlat4_M68(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_TSFlat4_M68'])

class Ts_opticsCorrector(Corrector):
    _DATABASE = {'TS_Optics_GPU_3_Coma_Corrector': {'brand': 'TS-Optics', 'name': 'GPU-3 Coma Corrector', 'type': 'type_corrector', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'TS_Optics_Wynne_Corrector_3': {'brand': 'TS-Optics', 'name': 'Wynne Corrector 3"', 'type': 'type_corrector', 'optical_length': 0, 'mass': 500, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'TS_Optics_Riccardi_Design_1x_M54': {'brand': 'TS-Optics', 'name': 'Riccardi-Design 1x (M54)', 'type': 'type_corrector', 'optical_length': 0, 'mass': 300, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def TS_Optics_GPU_3_Coma_Corrector(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_GPU_3_Coma_Corrector'])

    @classmethod
    def TS_Optics_Wynne_Corrector_3(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Wynne_Corrector_3'])

    @classmethod
    def TS_Optics_Riccardi_Design_1x_M54(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Riccardi_Design_1x_M54'])