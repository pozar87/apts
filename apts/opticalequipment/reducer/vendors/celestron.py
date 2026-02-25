from ..base import Reducer

class CelestronReducer(Reducer):
    _DATABASE = {'Celestron_f_6_3_Reducer_Corrector': {'brand': 'Celestron', 'name': 'f/6.3 Reducer/Corrector', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Celestron_0_7x_EdgeHD_Reducer_C6_C8_C9_25': {'brand': 'Celestron', 'name': '0.7x EdgeHD Reducer (C6/C8/C9.25)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 300, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Celestron_0_7x_EdgeHD_Reducer_C11_C14': {'brand': 'Celestron', 'name': '0.7x EdgeHD Reducer (C11/C14)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 400, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Celestron_f_7_Reducer_NexStar': {'brand': 'Celestron', 'name': 'f/7 Reducer (NexStar)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 150, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Celestron_0_63x_Reducer_Meade_compat': {'brand': 'Celestron', 'name': '0.63x Reducer (Meade compat.)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Celestron_EdgeHD_0_7x_Reducer_C8': {'brand': 'Celestron', 'name': 'EdgeHD 0.7x Reducer (C8)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 300, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Celestron_f_6_3_Reducer_Corrector(cls):
        return cls.from_database(cls._DATABASE['Celestron_f_6_3_Reducer_Corrector'])

    @classmethod
    def Celestron_0_7x_EdgeHD_Reducer_C6_C8_C9_25(cls):
        return cls.from_database(cls._DATABASE['Celestron_0_7x_EdgeHD_Reducer_C6_C8_C9_25'])

    @classmethod
    def Celestron_0_7x_EdgeHD_Reducer_C11_C14(cls):
        return cls.from_database(cls._DATABASE['Celestron_0_7x_EdgeHD_Reducer_C11_C14'])

    @classmethod
    def Celestron_f_7_Reducer_NexStar(cls):
        return cls.from_database(cls._DATABASE['Celestron_f_7_Reducer_NexStar'])

    @classmethod
    def Celestron_0_63x_Reducer_Meade_compat(cls):
        return cls.from_database(cls._DATABASE['Celestron_0_63x_Reducer_Meade_compat'])

    @classmethod
    def Celestron_EdgeHD_0_7x_Reducer_C8(cls):
        return cls.from_database(cls._DATABASE['Celestron_EdgeHD_0_7x_Reducer_C8'])