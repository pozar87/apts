from ..base import AntiTilt


class TS_OpticsAntiTilt(AntiTilt):
    _DATABASE = {'TS_Optics_Tilt_Adjuster_M48': {'brand': 'TS-Optics',
        'name': 'Tilt Adjuster (M48)', 'type': 'type_anti_tilt',
        'optical_length': 6, 'mass': 50, 'tside_thread': 'M48',
        'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''},
        'TS_Optics_Tilt_Adjuster_M54': {'brand': 'TS-Optics', 'name':
        'Tilt Adjuster (M54)', 'type': 'type_anti_tilt', 'optical_length': 
        6, 'mass': 60, 'tside_thread': 'M54', 'tside_gender': 'Female',
        'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False,
        'bf_role': ''}}

    @classmethod
    def TS_Optics_Tilt_Adjuster_M48(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Tilt_Adjuster_M48'])

    @classmethod
    def TS_Optics_Tilt_Adjuster_M54(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Tilt_Adjuster_M54'])
