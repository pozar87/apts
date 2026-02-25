from ..base import Reducer, Flattener, Corrector

class OmegonReducer(Reducer):
    _DATABASE = {'Omegon_0_8x_Reducer_M48': {'brand': 'Omegon', 'name': '0.8x Reducer (M48)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 220, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Omegon_0_8x_Reducer_M48(cls):
        return cls.from_database(cls._DATABASE['Omegon_0_8x_Reducer_M48'])

class OmegonFlattener(Flattener):
    _DATABASE = {'Omegon_Field_Flattener_M48': {'brand': 'Omegon', 'name': 'Field Flattener (M48)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Omegon_Field_Flattener_M48(cls):
        return cls.from_database(cls._DATABASE['Omegon_Field_Flattener_M48'])

class OmegonCorrector(Corrector):
    _DATABASE = {'Omegon_Coma_Corrector_M48': {'brand': 'Omegon', 'name': 'Coma Corrector (M48)', 'type': 'type_corrector', 'optical_length': 0, 'mass': 220, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Omegon_Coma_Corrector_M48(cls):
        return cls.from_database(cls._DATABASE['Omegon_Coma_Corrector_M48'])