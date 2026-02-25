from ..base import Reducer, Flattener, Corrector

class OrionReducer(Reducer):
    _DATABASE = {'Orion_0_85x_Reducer': {'brand': 'Orion', 'name': '0.85x Reducer', 'type': 'type_reducer', 'optical_length': 0, 'mass': 220, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Orion_0_5x_Focal_Reducer': {'brand': 'Orion', 'name': '0.5x Focal Reducer', 'type': 'type_reducer', 'optical_length': 0, 'mass': 300, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Orion_0_85x_Reducer(cls):
        return cls.from_database(cls._DATABASE['Orion_0_85x_Reducer'])

    @classmethod
    def Orion_0_5x_Focal_Reducer(cls):
        return cls.from_database(cls._DATABASE['Orion_0_5x_Focal_Reducer'])

class OrionFlattener(Flattener):
    _DATABASE = {'Orion_Field_Flattener_M48': {'brand': 'Orion', 'name': 'Field Flattener (M48)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Orion_Field_Flattener_M48(cls):
        return cls.from_database(cls._DATABASE['Orion_Field_Flattener_M48'])

class OrionCorrector(Corrector):
    _DATABASE = {'Orion_Coma_Corrector_M48': {'brand': 'Orion', 'name': 'Coma Corrector (M48)', 'type': 'type_corrector', 'optical_length': 0, 'mass': 240, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Orion_SkyGlow_Broadband_Filter': {'brand': 'Orion', 'name': 'SkyGlow Broadband Filter', 'type': 'type_corrector', 'optical_length': 0, 'mass': 50, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Orion_Coma_Corrector_M48(cls):
        return cls.from_database(cls._DATABASE['Orion_Coma_Corrector_M48'])

    @classmethod
    def Orion_SkyGlow_Broadband_Filter(cls):
        return cls.from_database(cls._DATABASE['Orion_SkyGlow_Broadband_Filter'])