from ..base import AntiTilt


class PlayerOneAntiTilt(AntiTilt):
    _DATABASE = {'Player_One_Tilt_Adjuster_M42': {'brand': 'Player One',
        'name': 'Tilt Adjuster (M42)', 'type': 'type_anti_tilt',
        'optical_length': 8, 'mass': 40, 'tside_thread': 'M42',
        'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''},
        'Player_One_Tilt_Adjuster_M54': {'brand': 'Player One', 'name':
        'Tilt Adjuster (M54)', 'type': 'type_anti_tilt', 'optical_length': 
        10, 'mass': 60, 'tside_thread': 'M54', 'tside_gender': 'Female',
        'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False,
        'bf_role': ''}}

    @classmethod
    def Player_One_Tilt_Adjuster_M42(cls):
        return cls.from_database(cls._DATABASE['Player_One_Tilt_Adjuster_M42'])

    @classmethod
    def Player_One_Tilt_Adjuster_M54(cls):
        return cls.from_database(cls._DATABASE['Player_One_Tilt_Adjuster_M54'])
