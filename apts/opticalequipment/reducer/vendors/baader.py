from ..base import Reducer, Corrector

class BaaderReducer(Reducer):
    _DATABASE = {'Baader_Alan_Gee_II_Telecompressor': {'brand': 'Baader', 'name': 'Alan Gee II Telecompressor', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Baader_Alan_Gee_II_Telecompressor(cls):
        return cls.from_database(cls._DATABASE['Baader_Alan_Gee_II_Telecompressor'])

class BaaderCorrector(Corrector):
    _DATABASE = {'Baader_MPCC_Mark_III': {'brand': 'Baader', 'name': 'MPCC Mark III', 'type': 'type_corrector', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Baader_RCC_I_Coma_Corrector': {'brand': 'Baader', 'name': 'RCC I (Coma Corrector)', 'type': 'type_corrector', 'optical_length': 0, 'mass': 300, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Baader_3_RCC_for_RC_telescopes': {'brand': 'Baader', 'name': '3" RCC (for RC telescopes)', 'type': 'type_corrector', 'optical_length': 0, 'mass': 500, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Baader_MPCC_III_1_1': {'brand': 'Baader', 'name': 'MPCC III (1:1)', 'type': 'type_corrector', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Baader_MPCC_Mark_III(cls):
        return cls.from_database(cls._DATABASE['Baader_MPCC_Mark_III'])

    @classmethod
    def Baader_RCC_I_Coma_Corrector(cls):
        return cls.from_database(cls._DATABASE['Baader_RCC_I_Coma_Corrector'])

    @classmethod
    def Baader_3_RCC_for_RC_telescopes(cls):
        return cls.from_database(cls._DATABASE['Baader_3_RCC_for_RC_telescopes'])

    @classmethod
    def Baader_MPCC_III_1_1(cls):
        return cls.from_database(cls._DATABASE['Baader_MPCC_III_1_1'])