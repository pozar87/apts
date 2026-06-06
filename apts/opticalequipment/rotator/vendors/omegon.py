from ..base import Rotator


class OmegonRotator(Rotator):
    _DATABASE = {'Omegon_Field_Rotator_M42': {'brand': 'Omegon', 'name':
        'Field Rotator (M42)', 'type': 'type_rotator', 'optical_length': 10,
        'mass': 230, 'tside_thread': 'M42', 'tside_gender': 'Female',
        'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False,
        'bf_role': ''}, 'Omegon_Field_Rotator_M48': {'brand': 'Omegon',
        'name': 'Field Rotator (M48)', 'type': 'type_rotator',
        'optical_length': 11, 'mass': 270, 'tside_thread': 'M48',
        'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Omegon_Field_Rotator_M42(cls):
        return cls.from_database(cls._DATABASE['Omegon_Field_Rotator_M42'])

    @classmethod
    def Omegon_Field_Rotator_M48(cls):
        return cls.from_database(cls._DATABASE['Omegon_Field_Rotator_M48'])
