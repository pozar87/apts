from ..base import AntiTilt


class APMAntiTilt(AntiTilt):
    _DATABASE = {'APM_Tilt_Adjuster_M54': {'brand': 'APM', 'name':
        'Tilt Adjuster (M54)', 'type': 'type_anti_tilt', 'optical_length': 
        8, 'mass': 55, 'tside_thread': 'M54', 'tside_gender': 'Female',
        'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False,
        'bf_role': ''}}

    @classmethod
    def APM_Tilt_Adjuster_M54(cls):
        return cls.from_database(cls._DATABASE['APM_Tilt_Adjuster_M54'])
