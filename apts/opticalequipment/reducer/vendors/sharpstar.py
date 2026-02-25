from ..base import Reducer, Flattener, Corrector

class SharpstarReducer(Reducer):
    _DATABASE = {'Sharpstar_0_8x_Reducer_EDPH': {'brand': 'Sharpstar', 'name': '0.8x Reducer (EDPH)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Sharpstar_0_7x_Reducer_EDPH': {'brand': 'Sharpstar', 'name': '0.7x Reducer (EDPH)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 260, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Sharpstar_0_74x_Reducer_94EDPH': {'brand': 'Sharpstar', 'name': '0.74x Reducer (94EDPH)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 280, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Sharpstar_0_8x_Reducer_140PH': {'brand': 'Sharpstar', 'name': '0.8x Reducer (140PH)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 350, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Sharpstar_0_8x_Reducer_EDPH(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_0_8x_Reducer_EDPH'])

    @classmethod
    def Sharpstar_0_7x_Reducer_EDPH(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_0_7x_Reducer_EDPH'])

    @classmethod
    def Sharpstar_0_74x_Reducer_94EDPH(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_0_74x_Reducer_94EDPH'])

    @classmethod
    def Sharpstar_0_8x_Reducer_140PH(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_0_8x_Reducer_140PH'])

class SharpstarFlattener(Flattener):
    _DATABASE = {'Sharpstar_2_Field_Flattener': {'brand': 'Sharpstar', 'name': '2" Field Flattener', 'type': 'type_flattener', 'optical_length': 0, 'mass': 300, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Sharpstar_2_Field_Flattener(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_2_Field_Flattener'])

class SharpstarCorrector(Corrector):
    _DATABASE = {'Sharpstar_HNT_Corrector': {'brand': 'Sharpstar', 'name': 'HNT Corrector', 'type': 'type_corrector', 'optical_length': 0, 'mass': 350, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Sharpstar_HNT_Corrector(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_HNT_Corrector'])