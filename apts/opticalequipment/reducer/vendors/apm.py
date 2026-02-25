from ..base import Reducer, Corrector

class ApmReducer(Reducer):
    _DATABASE = {'APM_Riccardi_Design_0_75x': {'brand': 'APM', 'name': 'Riccardi-Design 0.75x', 'type': 'type_reducer', 'optical_length': 0, 'mass': 450, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def APM_Riccardi_Design_0_75x(cls):
        return cls.from_database(cls._DATABASE['APM_Riccardi_Design_0_75x'])

class ApmCorrector(Corrector):
    _DATABASE = {'APM_Comacorr_1x_M48': {'brand': 'APM', 'name': 'Comacorr 1x (M48)', 'type': 'type_corrector', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def APM_Comacorr_1x_M48(cls):
        return cls.from_database(cls._DATABASE['APM_Comacorr_1x_M48'])