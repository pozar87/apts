from ..base import Camera

class LeicaCamera(Camera):
    _DATABASE = {'Leica_SL2': {'brand': 'Leica', 'name': 'SL2', 'type': 'type_dslr', 'optical_length': 20, 'mass': 835, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Leica_SL2_S': {'brand': 'Leica', 'name': 'SL2-S', 'type': 'type_dslr', 'optical_length': 20, 'mass': 850, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Leica_M11': {'brand': 'Leica', 'name': 'M11', 'type': 'type_dslr', 'optical_length': 20, 'mass': 530, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Leica_Q2': {'brand': 'Leica', 'name': 'Q2', 'type': 'type_dslr', 'optical_length': 20, 'mass': 718, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Leica_CL': {'brand': 'Leica', 'name': 'CL', 'type': 'type_dslr', 'optical_length': 20, 'mass': 390, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}}

    @classmethod
    def Leica_SL2(cls):
        return cls.from_database(cls._DATABASE['Leica_SL2'])

    @classmethod
    def Leica_SL2_S(cls):
        return cls.from_database(cls._DATABASE['Leica_SL2_S'])

    @classmethod
    def Leica_M11(cls):
        return cls.from_database(cls._DATABASE['Leica_M11'])

    @classmethod
    def Leica_Q2(cls):
        return cls.from_database(cls._DATABASE['Leica_Q2'])

    @classmethod
    def Leica_CL(cls):
        return cls.from_database(cls._DATABASE['Leica_CL'])