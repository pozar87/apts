from ..base import Rotator


class MoonliteRotator(Rotator):
    _DATABASE = {'Moonlite_Rotator_M42': {'brand': 'Moonlite', 'name':
        'Rotator (M42)', 'type': 'type_rotator', 'optical_length': 11,
        'mass': 220, 'tside_thread': 'M42', 'tside_gender': 'Female',
        'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False,
        'bf_role': ''}, 'Moonlite_Rotator_M48': {'brand': 'Moonlite',
        'name': 'Rotator (M48)', 'type': 'type_rotator', 'optical_length': 
        11, 'mass': 270, 'tside_thread': 'M48', 'tside_gender': 'Female',
        'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False,
        'bf_role': ''}}

    @classmethod
    def Moonlite_Rotator_M42(cls):
        return cls.from_database(cls._DATABASE['Moonlite_Rotator_M42'])

    @classmethod
    def Moonlite_Rotator_M48(cls):
        return cls.from_database(cls._DATABASE['Moonlite_Rotator_M48'])
