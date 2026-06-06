from ..base import AntiTilt


class SharpstarAntiTilt(AntiTilt):
    _DATABASE = {'Sharpstar_Tilt_Adjuster_M48': {'brand': 'Sharpstar',
        'name': 'Tilt Adjuster (M48)', 'type': 'type_anti_tilt',
        'optical_length': 6, 'mass': 45, 'tside_thread': 'M48',
        'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''},
        'Sharpstar_Tilt_Adjuster_M54': {'brand': 'Sharpstar', 'name':
        'Tilt Adjuster (M54)', 'type': 'type_anti_tilt', 'optical_length': 
        8, 'mass': 55, 'tside_thread': 'M54', 'tside_gender': 'Female',
        'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False,
        'bf_role': ''}}

    @classmethod
    def Sharpstar_Tilt_Adjuster_M48(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_Tilt_Adjuster_M48'])

    @classmethod
    def Sharpstar_Tilt_Adjuster_M54(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_Tilt_Adjuster_M54'])
