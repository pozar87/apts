from ..base import Camera

class FujiCamera(Camera):
    _DATABASE = {'Fuji_X_T4': {'brand': 'Fuji', 'name': 'X-T4', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 607, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Fuji_X_T5': {'brand': 'Fuji', 'name': 'X-T5', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 557, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Fuji_X_T3': {'brand': 'Fuji', 'name': 'X-T3', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 539, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Fuji_X_T2': {'brand': 'Fuji', 'name': 'X-T2', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 507, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Fuji_X_T30_II': {'brand': 'Fuji', 'name': 'X-T30 II', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 378, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Fuji_X_H2': {'brand': 'Fuji', 'name': 'X-H2', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 660, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Fuji_X_H2S': {'brand': 'Fuji', 'name': 'X-H2S', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 660, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Fuji_X_S20': {'brand': 'Fuji', 'name': 'X-S20', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 491, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Fuji_X_S10': {'brand': 'Fuji', 'name': 'X-S10', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 465, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Fuji_X_E4': {'brand': 'Fuji', 'name': 'X-E4', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 364, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Fuji_X_T50': {'brand': 'Fuji', 'name': 'X-T50', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 438, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Fuji_X_T1': {'brand': 'Fuji', 'name': 'X-T1', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 440, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Fuji_X_T20': {'brand': 'Fuji', 'name': 'X-T20', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 383, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Fuji_X_A7': {'brand': 'Fuji', 'name': 'X-A7', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 320, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Fuji_X_Pro3': {'brand': 'Fuji', 'name': 'X-Pro3', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 497, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Fuji_X_Pro2': {'brand': 'Fuji', 'name': 'X-Pro2', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 495, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Fuji_X_E3': {'brand': 'Fuji', 'name': 'X-E3', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 337, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Fuji_X_E2': {'brand': 'Fuji', 'name': 'X-E2', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 350, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Fuji_X100V': {'brand': 'Fuji', 'name': 'X100V', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 478, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Fuji_X_A5': {'brand': 'Fuji', 'name': 'X-A5', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 311, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Fuji_X_A3': {'brand': 'Fuji', 'name': 'X-A3', 'type': 'type_dslr', 'optical_length': 17.7, 'mass': 339, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}}

    @classmethod
    def Fuji_X_T4(cls):
        return cls.from_database(cls._DATABASE['Fuji_X_T4'])

    @classmethod
    def Fuji_X_T5(cls):
        return cls.from_database(cls._DATABASE['Fuji_X_T5'])

    @classmethod
    def Fuji_X_T3(cls):
        return cls.from_database(cls._DATABASE['Fuji_X_T3'])

    @classmethod
    def Fuji_X_T2(cls):
        return cls.from_database(cls._DATABASE['Fuji_X_T2'])

    @classmethod
    def Fuji_X_T30_II(cls):
        return cls.from_database(cls._DATABASE['Fuji_X_T30_II'])

    @classmethod
    def Fuji_X_H2(cls):
        return cls.from_database(cls._DATABASE['Fuji_X_H2'])

    @classmethod
    def Fuji_X_H2S(cls):
        return cls.from_database(cls._DATABASE['Fuji_X_H2S'])

    @classmethod
    def Fuji_X_S20(cls):
        return cls.from_database(cls._DATABASE['Fuji_X_S20'])

    @classmethod
    def Fuji_X_S10(cls):
        return cls.from_database(cls._DATABASE['Fuji_X_S10'])

    @classmethod
    def Fuji_X_E4(cls):
        return cls.from_database(cls._DATABASE['Fuji_X_E4'])

    @classmethod
    def Fuji_X_T50(cls):
        return cls.from_database(cls._DATABASE['Fuji_X_T50'])

    @classmethod
    def Fuji_X_T1(cls):
        return cls.from_database(cls._DATABASE['Fuji_X_T1'])

    @classmethod
    def Fuji_X_T20(cls):
        return cls.from_database(cls._DATABASE['Fuji_X_T20'])

    @classmethod
    def Fuji_X_A7(cls):
        return cls.from_database(cls._DATABASE['Fuji_X_A7'])

    @classmethod
    def Fuji_X_Pro3(cls):
        return cls.from_database(cls._DATABASE['Fuji_X_Pro3'])

    @classmethod
    def Fuji_X_Pro2(cls):
        return cls.from_database(cls._DATABASE['Fuji_X_Pro2'])

    @classmethod
    def Fuji_X_E3(cls):
        return cls.from_database(cls._DATABASE['Fuji_X_E3'])

    @classmethod
    def Fuji_X_E2(cls):
        return cls.from_database(cls._DATABASE['Fuji_X_E2'])

    @classmethod
    def Fuji_X100V(cls):
        return cls.from_database(cls._DATABASE['Fuji_X100V'])

    @classmethod
    def Fuji_X_A5(cls):
        return cls.from_database(cls._DATABASE['Fuji_X_A5'])

    @classmethod
    def Fuji_X_A3(cls):
        return cls.from_database(cls._DATABASE['Fuji_X_A3'])