from ..base import Rotator


class AltairRotator(Rotator):
    _DATABASE = {'Altair_Field_Rotator_M42': {'brand': 'Altair', 'name':
        'Field Rotator (M42)', 'type': 'type_rotator', 'optical_length': 10,
        'mass': 240, 'tside_thread': 'M42', 'tside_gender': 'Female',
        'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False,
        'bf_role': ''}, 'Altair_Field_Rotator_M48': {'brand': 'Altair',
        'name': 'Field Rotator (M48)', 'type': 'type_rotator',
        'optical_length': 11, 'mass': 280, 'tside_thread': 'M48',
        'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Altair_Field_Rotator_M42(cls):
        return cls.from_database(cls._DATABASE['Altair_Field_Rotator_M42'])

    @classmethod
    def Altair_Field_Rotator_M48(cls):
        return cls.from_database(cls._DATABASE['Altair_Field_Rotator_M48'])
