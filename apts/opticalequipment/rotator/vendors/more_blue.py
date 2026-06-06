from ..base import Rotator


class MoreBlueRotator(Rotator):
    _DATABASE = {'More_Blue_Camera_Rotator_M56': {'brand': 'More Blue',
        'name': 'Camera Rotator (M56)', 'type': 'type_rotator',
        'optical_length': 10, 'mass': 180, 'tside_thread': 'M56',
        'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''},
        'More_Blue_Camera_Rotator_M72': {'brand': 'More Blue', 'name':
        'Camera Rotator (M72)', 'type': 'type_rotator', 'optical_length': 
        12, 'mass': 250, 'tside_thread': 'M72', 'tside_gender': 'Female',
        'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False,
        'bf_role': ''}}

    @classmethod
    def More_Blue_Camera_Rotator_M56(cls):
        return cls.from_database(cls._DATABASE['More_Blue_Camera_Rotator_M56'])

    @classmethod
    def More_Blue_Camera_Rotator_M72(cls):
        return cls.from_database(cls._DATABASE['More_Blue_Camera_Rotator_M72'])
