from ..base import Reducer, Corrector

class CffReducer(Reducer):
    _DATABASE = {'CFF_0_65x_Reducer_M117': {'brand': 'CFF', 'name': '0.65x Reducer (M117)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 500, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def CFF_0_65x_Reducer_M117(cls):
        return cls.from_database(cls._DATABASE['CFF_0_65x_Reducer_M117'])

class CffCorrector(Corrector):
    _DATABASE = {'CFF_RC_Corrector_1x_M117': {'brand': 'CFF', 'name': 'RC Corrector 1x (M117)', 'type': 'type_corrector', 'optical_length': 0, 'mass': 600, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def CFF_RC_Corrector_1x_M117(cls):
        return cls.from_database(cls._DATABASE['CFF_RC_Corrector_1x_M117'])