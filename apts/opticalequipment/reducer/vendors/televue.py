from ..base import Reducer, Flattener, Corrector

class TelevueReducer(Reducer):
    _DATABASE = {'TeleVue_0_8x_Reducer': {'brand': 'TeleVue', 'name': '0.8x Reducer', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'TeleVue_TRF_2008_0_8x': {'brand': 'TeleVue', 'name': 'TRF-2008 0.8x', 'type': 'type_reducer', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'TeleVue_TV_76_Reducer_0_8x': {'brand': 'TeleVue', 'name': 'TV-76 Reducer 0.8x', 'type': 'type_reducer', 'optical_length': 0, 'mass': 180, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'TeleVue_TV_85_Reducer_0_8x': {'brand': 'TeleVue', 'name': 'TV-85 Reducer 0.8x', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def TeleVue_0_8x_Reducer(cls):
        return cls.from_database(cls._DATABASE['TeleVue_0_8x_Reducer'])

    @classmethod
    def TeleVue_TRF_2008_0_8x(cls):
        return cls.from_database(cls._DATABASE['TeleVue_TRF_2008_0_8x'])

    @classmethod
    def TeleVue_TV_76_Reducer_0_8x(cls):
        return cls.from_database(cls._DATABASE['TeleVue_TV_76_Reducer_0_8x'])

    @classmethod
    def TeleVue_TV_85_Reducer_0_8x(cls):
        return cls.from_database(cls._DATABASE['TeleVue_TV_85_Reducer_0_8x'])

class TelevueFlattener(Flattener):
    _DATABASE = {'TeleVue_NP101_Flattener': {'brand': 'TeleVue', 'name': 'NP101 Flattener', 'type': 'type_flattener', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'TeleVue_NP127_Flattener': {'brand': 'TeleVue', 'name': 'NP127 Flattener', 'type': 'type_flattener', 'optical_length': 0, 'mass': 280, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def TeleVue_NP101_Flattener(cls):
        return cls.from_database(cls._DATABASE['TeleVue_NP101_Flattener'])

    @classmethod
    def TeleVue_NP127_Flattener(cls):
        return cls.from_database(cls._DATABASE['TeleVue_NP127_Flattener'])

class TelevueCorrector(Corrector):
    _DATABASE = {'TeleVue_Paracorr_Type_2': {'brand': 'TeleVue', 'name': 'Paracorr Type 2', 'type': 'type_corrector', 'optical_length': 0, 'mass': 400, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'TeleVue_Big_Paracorr_Type_2': {'brand': 'TeleVue', 'name': 'Big Paracorr Type 2', 'type': 'type_corrector', 'optical_length': 0, 'mass': 600, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def TeleVue_Paracorr_Type_2(cls):
        return cls.from_database(cls._DATABASE['TeleVue_Paracorr_Type_2'])

    @classmethod
    def TeleVue_Big_Paracorr_Type_2(cls):
        return cls.from_database(cls._DATABASE['TeleVue_Big_Paracorr_Type_2'])