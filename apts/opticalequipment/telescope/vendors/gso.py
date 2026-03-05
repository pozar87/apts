from ..base import Telescope

class GsoTelescope(Telescope):
    _DATABASE = {
        'GSO_RC_6': {'brand': 'GSO', 'name': 'RC 6"', 'type': 'catadioptric', 'optical_length': 0, 'mass': 5400, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M90', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 152, 'focal_length_mm': 1370, 'central_obstruction_mm': 61}, # Verified via specs
        'GSO_RC_8': {'brand': 'GSO', 'name': 'RC 8"', 'type': 'catadioptric', 'optical_length': 0, 'mass': 7500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M90', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 203, 'focal_length_mm': 1624, 'central_obstruction_mm': 85}, # Verified via specs
        'GSO_RC_10': {'brand': 'GSO', 'name': 'RC 10"', 'type': 'catadioptric', 'optical_length': 0, 'mass': 15000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 254, 'focal_length_mm': 2000, 'central_obstruction_mm': 110}, # Verified via specs
        'GSO_RC_12': {'brand': 'GSO', 'name': 'RC 12"', 'type': 'catadioptric', 'optical_length': 0, 'mass': 21000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 304, 'focal_length_mm': 2432, 'central_obstruction_mm': 130}, # Verified via specs
        'GSO_Newton_6_f_5': {'brand': 'GSO', 'name': 'Newton 6" f/5', 'type': 'newtonian_reflector', 'optical_length': 0, 'mass': 5300, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 150, 'focal_length_mm': 750},
        'GSO_Newton_8_f_4': {'brand': 'GSO', 'name': 'Newton 8" f/4', 'type': 'newtonian_reflector', 'optical_length': 0, 'mass': 8000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 200, 'focal_length_mm': 800},
        'GSO_Newton_8_f_5': {'brand': 'GSO', 'name': 'Newton 8" f/5', 'type': 'newtonian_reflector', 'optical_length': 0, 'mass': 9000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 200, 'focal_length_mm': 1000},
        'GSO_Dobson_6': {'brand': 'GSO', 'name': 'Dobson 6"', 'type': 'newtonian_reflector', 'optical_length': 0, 'mass': 8300, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 152, 'focal_length_mm': 1200},
        'GSO_Dobson_8': {'brand': 'GSO', 'name': 'Dobson 8"', 'type': 'newtonian_reflector', 'optical_length': 0, 'mass': 11100, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 203, 'focal_length_mm': 1200},
        'GSO_Dobson_10': {'brand': 'GSO', 'name': 'Dobson 10"', 'type': 'newtonian_reflector', 'optical_length': 0, 'mass': 15800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 254, 'focal_length_mm': 1250},
        'GSO_Dobson_12': {'brand': 'GSO', 'name': 'Dobson 12"', 'type': 'newtonian_reflector', 'optical_length': 0, 'mass': 21700, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 305, 'focal_length_mm': 1520},
    }

    @classmethod
    def GSO_RC_6(cls):
        return cls.from_database(cls._DATABASE['GSO_RC_6'])

    @classmethod
    def GSO_RC_8(cls):
        return cls.from_database(cls._DATABASE['GSO_RC_8'])

    @classmethod
    def GSO_RC_10(cls):
        return cls.from_database(cls._DATABASE['GSO_RC_10'])

    @classmethod
    def GSO_RC_12(cls):
        return cls.from_database(cls._DATABASE['GSO_RC_12'])

    @classmethod
    def GSO_Newton_6_f_5(cls):
        return cls.from_database(cls._DATABASE['GSO_Newton_6_f_5'])

    @classmethod
    def GSO_Newton_8_f_4(cls):
        return cls.from_database(cls._DATABASE['GSO_Newton_8_f_4'])

    @classmethod
    def GSO_Newton_8_f_5(cls):
        return cls.from_database(cls._DATABASE['GSO_Newton_8_f_5'])

    @classmethod
    def GSO_Dobson_6(cls):
        return cls.from_database(cls._DATABASE['GSO_Dobson_6'])

    @classmethod
    def GSO_Dobson_8(cls):
        return cls.from_database(cls._DATABASE['GSO_Dobson_8'])

    @classmethod
    def GSO_Dobson_10(cls):
        return cls.from_database(cls._DATABASE['GSO_Dobson_10'])

    @classmethod
    def GSO_Dobson_12(cls):
        return cls.from_database(cls._DATABASE['GSO_Dobson_12'])
