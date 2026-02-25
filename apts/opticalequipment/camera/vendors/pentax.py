from ..base import Camera

class PentaxCamera(Camera):
    _DATABASE = {'Pentax_K_1_II': {'brand': 'Pentax', 'name': 'K-1 II', 'type': 'type_dslr', 'optical_length': 45.5, 'mass': 1010, 'tside_thread': 'Pentax K', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Pentax_K_1': {'brand': 'Pentax', 'name': 'K-1', 'type': 'type_dslr', 'optical_length': 45.5, 'mass': 1010, 'tside_thread': 'Pentax K', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Pentax_K_3_III': {'brand': 'Pentax', 'name': 'K-3 III', 'type': 'type_dslr', 'optical_length': 45.5, 'mass': 820, 'tside_thread': 'Pentax K', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Pentax_KP': {'brand': 'Pentax', 'name': 'KP', 'type': 'type_dslr', 'optical_length': 45.5, 'mass': 703, 'tside_thread': 'Pentax K', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Pentax_K_70': {'brand': 'Pentax', 'name': 'K-70', 'type': 'type_dslr', 'optical_length': 45.5, 'mass': 688, 'tside_thread': 'Pentax K', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}}

    @classmethod
    def Pentax_K_1_II(cls):
        return cls.from_database(cls._DATABASE['Pentax_K_1_II'])

    @classmethod
    def Pentax_K_1(cls):
        return cls.from_database(cls._DATABASE['Pentax_K_1'])

    @classmethod
    def Pentax_K_3_III(cls):
        return cls.from_database(cls._DATABASE['Pentax_K_3_III'])

    @classmethod
    def Pentax_KP(cls):
        return cls.from_database(cls._DATABASE['Pentax_KP'])

    @classmethod
    def Pentax_K_70(cls):
        return cls.from_database(cls._DATABASE['Pentax_K_70'])