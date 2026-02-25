from ..base import Reducer, Flattener, Corrector

class TecnoskyReducer(Reducer):
    _DATABASE = {'Tecnosky_0_8x_Reducer_M48': {'brand': 'Tecnosky', 'name': '0.8x Reducer (M48)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 220, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Tecnosky_0_8x_Reducer_M48(cls):
        return cls.from_database(cls._DATABASE['Tecnosky_0_8x_Reducer_M48'])

class TecnoskyFlattener(Flattener):
    _DATABASE = {'Tecnosky_Field_Flattener_M48': {'brand': 'Tecnosky', 'name': 'Field Flattener (M48)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Tecnosky_Field_Flattener_M48(cls):
        return cls.from_database(cls._DATABASE['Tecnosky_Field_Flattener_M48'])

class TecnoskyCorrector(Corrector):
    _DATABASE = {'Tecnosky_Wynne_Corrector_M68': {'brand': 'Tecnosky', 'name': 'Wynne Corrector (M68)', 'type': 'type_corrector', 'optical_length': 0, 'mass': 400, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Tecnosky_Wynne_Corrector_M68(cls):
        return cls.from_database(cls._DATABASE['Tecnosky_Wynne_Corrector_M68'])