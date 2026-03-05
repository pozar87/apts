from ..base import Telescope

class MeadeTelescope(Telescope):
    _DATABASE = {
        'Meade_LX85_ACF_6': {'brand': 'Meade', 'name': 'LX85 ACF 6"', 'type': 'catadioptric', 'optical_length': 0, 'mass': 4200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 152, 'focal_length_mm': 1524, 'central_obstruction_mm': 56},
        'Meade_LX85_ACF_8': {'brand': 'Meade', 'name': 'LX85 ACF 8"', 'type': 'catadioptric', 'optical_length': 0, 'mass': 5700, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 203, 'focal_length_mm': 2032, 'central_obstruction_mm': 76},
        'Meade_LX200_ACF_8': {'brand': 'Meade', 'name': 'LX200 ACF 8"', 'type': 'catadioptric', 'optical_length': 0, 'mass': 6400, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 203, 'focal_length_mm': 2000, 'central_obstruction_mm': 76},
        'Meade_LX200_ACF_10': {'brand': 'Meade', 'name': 'LX200 ACF 10"', 'type': 'catadioptric', 'optical_length': 0, 'mass': 11800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 254, 'focal_length_mm': 2500, 'central_obstruction_mm': 94},
        'Meade_LX200_ACF_12': {'brand': 'Meade', 'name': 'LX200 ACF 12"', 'type': 'catadioptric', 'optical_length': 0, 'mass': 16300, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 305, 'focal_length_mm': 3000, 'central_obstruction_mm': 102},
        'Meade_LX200_ACF_14': {'brand': 'Meade', 'name': 'LX200 ACF 14"', 'type': 'catadioptric', 'optical_length': 0, 'mass': 22700, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 355, 'focal_length_mm': 3556, 'central_obstruction_mm': 117},
        'Meade_LX200_ACF_16': {'brand': 'Meade', 'name': 'LX200 ACF 16"', 'type': 'catadioptric', 'optical_length': 0, 'mass': 30400, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 406, 'focal_length_mm': 4064, 'central_obstruction_mm': 127},
        'Meade_LX600_ACF_10': {'brand': 'Meade', 'name': 'LX600 ACF 10"', 'type': 'catadioptric', 'optical_length': 0, 'mass': 12000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 254, 'focal_length_mm': 2032, 'central_obstruction_mm': 94},
        'Meade_LX600_ACF_12': {'brand': 'Meade', 'name': 'LX600 ACF 12"', 'type': 'catadioptric', 'optical_length': 0, 'mass': 16500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 305, 'focal_length_mm': 2438, 'central_obstruction_mm': 102},
        'Meade_LX600_ACF_14': {'brand': 'Meade', 'name': 'LX600 ACF 14"', 'type': 'catadioptric', 'optical_length': 0, 'mass': 23000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 355, 'focal_length_mm': 2845, 'central_obstruction_mm': 117},
    }

    @classmethod
    def Meade_LX85_ACF_6(cls):
        return cls.from_database(cls._DATABASE['Meade_LX85_ACF_6'])

    @classmethod
    def Meade_LX85_ACF_8(cls):
        return cls.from_database(cls._DATABASE['Meade_LX85_ACF_8'])

    @classmethod
    def Meade_LX200_ACF_8(cls):
        return cls.from_database(cls._DATABASE['Meade_LX200_ACF_8'])

    @classmethod
    def Meade_LX200_ACF_10(cls):
        return cls.from_database(cls._DATABASE['Meade_LX200_ACF_10'])

    @classmethod
    def Meade_LX200_ACF_12(cls):
        return cls.from_database(cls._DATABASE['Meade_LX200_ACF_12'])

    @classmethod
    def Meade_LX200_ACF_14(cls):
        return cls.from_database(cls._DATABASE['Meade_LX200_ACF_14'])

    @classmethod
    def Meade_LX200_ACF_16(cls):
        return cls.from_database(cls._DATABASE['Meade_LX200_ACF_16'])

    @classmethod
    def Meade_LX600_ACF_10(cls):
        return cls.from_database(cls._DATABASE['Meade_LX600_ACF_10'])

    @classmethod
    def Meade_LX600_ACF_12(cls):
        return cls.from_database(cls._DATABASE['Meade_LX600_ACF_12'])

    @classmethod
    def Meade_LX600_ACF_14(cls):
        return cls.from_database(cls._DATABASE['Meade_LX600_ACF_14'])
