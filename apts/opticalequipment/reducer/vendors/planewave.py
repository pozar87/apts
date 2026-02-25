from ..base import Reducer, Corrector

class PlanewaveReducer(Reducer):
    _DATABASE = {'PlaneWave_0_66x_Reducer_CDK14': {'brand': 'PlaneWave', 'name': '0.66x Reducer (CDK14)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 900, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def PlaneWave_0_66x_Reducer_CDK14(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_0_66x_Reducer_CDK14'])

class PlanewaveCorrector(Corrector):
    _DATABASE = {'PlaneWave_CDK12_5_Corrector': {'brand': 'PlaneWave', 'name': 'CDK12.5 Corrector', 'type': 'type_corrector', 'optical_length': 0, 'mass': 600, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'PlaneWave_CDK14_Corrector': {'brand': 'PlaneWave', 'name': 'CDK14 Corrector', 'type': 'type_corrector', 'optical_length': 0, 'mass': 700, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'PlaneWave_CDK17_Corrector': {'brand': 'PlaneWave', 'name': 'CDK17 Corrector', 'type': 'type_corrector', 'optical_length': 0, 'mass': 800, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'PlaneWave_CDK20_Corrector': {'brand': 'PlaneWave', 'name': 'CDK20 Corrector', 'type': 'type_corrector', 'optical_length': 0, 'mass': 1000, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def PlaneWave_CDK12_5_Corrector(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_CDK12_5_Corrector'])

    @classmethod
    def PlaneWave_CDK14_Corrector(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_CDK14_Corrector'])

    @classmethod
    def PlaneWave_CDK17_Corrector(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_CDK17_Corrector'])

    @classmethod
    def PlaneWave_CDK20_Corrector(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_CDK20_Corrector'])