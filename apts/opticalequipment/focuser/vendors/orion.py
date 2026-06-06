from ..base import Focuser


class OrionFocuser(Focuser):
    _DATABASE = {'Orion_2_Crayford_Focuser': {'brand': 'Orion', 'name':
        '2" Crayford Focuser', 'type': 'type_focuser', 'optical_length': 0,
        'mass': 550, 'tside_thread': '', 'tside_gender': 'Male',
        'cside_thread': '', 'cside_gender': 'Female', 'reversible': False,
        'bf_role': ''}}

    @classmethod
    def Orion_2_Crayford_Focuser(cls):
        return cls.from_database(cls._DATABASE['Orion_2_Crayford_Focuser'])
