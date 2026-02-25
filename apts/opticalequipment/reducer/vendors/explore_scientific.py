from ..base import Reducer, Flattener, Corrector

class Explore_scientificReducer(Reducer):
    _DATABASE = {'Explore_Scientific_0_7x_Reducer': {'brand': 'Explore Scientific', 'name': '0.7x Reducer', 'type': 'type_reducer', 'optical_length': 0, 'mass': 280, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Explore_Scientific_0_7x_Reducer_2': {'brand': 'Explore Scientific', 'name': '0.7x Reducer (2")', 'type': 'type_reducer', 'optical_length': 0, 'mass': 300, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Explore_Scientific_0_7x_Reducer(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_0_7x_Reducer'])

    @classmethod
    def Explore_Scientific_0_7x_Reducer_2(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_0_7x_Reducer_2'])

class Explore_scientificFlattener(Flattener):
    _DATABASE = {'Explore_Scientific_ED_Field_Flattener': {'brand': 'Explore Scientific', 'name': 'ED Field Flattener', 'type': 'type_flattener', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Explore_Scientific_ED_Field_Flattener(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_ED_Field_Flattener'])

class Explore_scientificCorrector(Corrector):
    _DATABASE = {'Explore_Scientific_HR_Coma_Corrector': {'brand': 'Explore Scientific', 'name': 'HR Coma Corrector', 'type': 'type_corrector', 'optical_length': 0, 'mass': 350, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Explore_Scientific_HR_Coma_Corrector(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_HR_Coma_Corrector'])