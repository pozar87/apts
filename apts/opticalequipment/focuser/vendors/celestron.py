from ..base import Focuser


class CelestronFocuser(Focuser):
    _DATABASE = {'Celestron_2_Crayford_Focuser': {'brand': 'Celestron',
        'name': '2" Crayford Focuser', 'type': 'type_focuser',
        'optical_length': 0, 'mass': 500, 'tside_thread': '',
        'tside_gender': 'Male', 'cside_thread': '', 'cside_gender':
        'Female', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Celestron_2_Crayford_Focuser(cls):
        return cls.from_database(cls._DATABASE['Celestron_2_Crayford_Focuser'])
