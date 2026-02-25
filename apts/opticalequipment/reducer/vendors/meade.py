from ..base import Reducer, Flattener, Corrector

class MeadeReducer(Reducer):
    _DATABASE = {'Meade_f_6_3_Reducer_Corrector': {'brand': 'Meade', 'name': 'f/6.3 Reducer/Corrector', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Meade_f_3_3_Reducer': {'brand': 'Meade', 'name': 'f/3.3 Reducer', 'type': 'type_reducer', 'optical_length': 0, 'mass': 300, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Meade_Series_4000_0_33x_Reducer': {'brand': 'Meade', 'name': 'Series 4000 0.33x Reducer', 'type': 'type_reducer', 'optical_length': 0, 'mass': 150, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Meade_f_6_3_Reducer_Corrector(cls):
        return cls.from_database(cls._DATABASE['Meade_f_6_3_Reducer_Corrector'])

    @classmethod
    def Meade_f_3_3_Reducer(cls):
        return cls.from_database(cls._DATABASE['Meade_f_3_3_Reducer'])

    @classmethod
    def Meade_Series_4000_0_33x_Reducer(cls):
        return cls.from_database(cls._DATABASE['Meade_Series_4000_0_33x_Reducer'])

class MeadeFlattener(Flattener):
    _DATABASE = {'Meade_Series_6000_Field_Flattener': {'brand': 'Meade', 'name': 'Series 6000 Field Flattener', 'type': 'type_flattener', 'optical_length': 0, 'mass': 280, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Meade_Series_6000_Field_Flattener(cls):
        return cls.from_database(cls._DATABASE['Meade_Series_6000_Field_Flattener'])

class MeadeCorrector(Corrector):
    _DATABASE = {'Meade_Series_6000_Coma_Corrector': {'brand': 'Meade', 'name': 'Series 6000 Coma Corrector', 'type': 'type_corrector', 'optical_length': 0, 'mass': 300, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Meade_Series_6000_Coma_Corrector(cls):
        return cls.from_database(cls._DATABASE['Meade_Series_6000_Coma_Corrector'])