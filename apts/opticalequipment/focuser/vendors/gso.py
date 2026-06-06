from ..base import Focuser


class GSOFocuser(Focuser):
    _DATABASE = {'GSO_2_Crayford_Focuser': {'brand': 'GSO', 'name':
        '2" Crayford Focuser', 'type': 'type_focuser', 'optical_length': 0,
        'mass': 600, 'tside_thread': '', 'tside_gender': 'Male',
        'cside_thread': '', 'cside_gender': 'Female', 'reversible': False,
        'bf_role': ''}, 'GSO_2_Dual_Speed_Focuser': {'brand': 'GSO', 'name':
        '2" Dual-Speed Focuser', 'type': 'type_focuser', 'optical_length': 
        0, 'mass': 650, 'tside_thread': '', 'tside_gender': 'Male',
        'cside_thread': '', 'cside_gender': 'Female', 'reversible': False,
        'bf_role': ''}}

    @classmethod
    def GSO_2_Crayford_Focuser(cls):
        return cls.from_database(cls._DATABASE['GSO_2_Crayford_Focuser'])

    @classmethod
    def GSO_2_Dual_Speed_Focuser(cls):
        return cls.from_database(cls._DATABASE['GSO_2_Dual_Speed_Focuser'])
