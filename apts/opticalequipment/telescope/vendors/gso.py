from ..base import Telescope

class GsoTelescope(Telescope):
    _DATABASE = {
        'GSO_RC_6': {
            'brand': 'GSO',
            'name': 'RC 6"',
            'type': 'catadioptric',
            'optical_length': 0,
            'mass': 5580,
            'tside_thread': '',
            'tside_gender': '',
            'cside_thread': 'M90',
            'cside_gender': 'Male',
            'reversible': False,
            'bf_role': '',
            'aperture_mm': 152,
            'focal_length_mm': 1370,
            'central_obstruction_mm': 71
        }, # Verified via Optical Universe (71mm CO, 5.58kg weight)
        'GSO_RC_8': {
            'brand': 'GSO',
            'name': 'RC 8"',
            'type': 'catadioptric',
            'optical_length': 0,
            'mass': 7500,
            'tside_thread': '',
            'tside_gender': '',
            'cside_thread': 'M90',
            'cside_gender': 'Male',
            'reversible': False,
            'bf_role': '',
            'aperture_mm': 203,
            'focal_length_mm': 1624,
            'central_obstruction_mm': 85
        }, # Verified via specs
        'GSO_RC_10': {
            'brand': 'GSO',
            'name': 'RC 10"',
            'type': 'catadioptric',
            'optical_length': 0,
            'mass': 15000,
            'tside_thread': '',
            'tside_gender': '',
            'cside_thread': 'M117',
            'cside_gender': 'Male',
            'reversible': False,
            'bf_role': '',
            'aperture_mm': 254,
            'focal_length_mm': 2000,
            'central_obstruction_mm': 110
        }, # Verified via specs
        'GSO_RC_12': {
            'brand': 'GSO',
            'name': 'RC 12"',
            'type': 'catadioptric',
            'optical_length': 0,
            'mass': 21000,
            'tside_thread': '',
            'tside_gender': '',
            'cside_thread': 'M117',
            'cside_gender': 'Male',
            'reversible': False,
            'bf_role': '',
            'aperture_mm': 304,
            'focal_length_mm': 2432,
            'central_obstruction_mm': 130
        }, # Verified via specs
        'GSO_Newton_6_f_5': {
            'brand': 'GSO',
            'name': 'Newton 6" f/5',
            'type': 'newtonian_reflector',
            'optical_length': 0,
            'mass': 5900,
            'tside_thread': '',
            'tside_gender': '',
            'cside_thread': '2"',
            'cside_gender': 'Female',
            'reversible': False,
            'bf_role': '',
            'aperture_mm': 150,
            'focal_length_mm': 750,
            'central_obstruction_mm': 50
        }, # Verified via Agena Astro and Optical Universe (50mm CO, 5.9kg OTA)
        'GSO_Newton_8_f_4': {
            'brand': 'GSO',
            'name': 'Newton 8" f/4',
            'type': 'newtonian_reflector',
            'optical_length': 0,
            'mass': 8900,
            'tside_thread': '',
            'tside_gender': '',
            'cside_thread': '2"',
            'cside_gender': 'Female',
            'reversible': False,
            'bf_role': '',
            'aperture_mm': 200,
            'focal_length_mm': 800,
            'central_obstruction_mm': 70
        }, # Verified via Agena Astro (70mm CO, 8.9kg OTA with accessories)
        'GSO_Newton_8_f_5': {
            'brand': 'GSO',
            'name': 'Newton 8" f/5',
            'type': 'newtonian_reflector',
            'optical_length': 0,
            'mass': 9000,
            'tside_thread': '',
            'tside_gender': '',
            'cside_thread': '2"',
            'cside_gender': 'Female',
            'reversible': False,
            'bf_role': '',
            'aperture_mm': 200,
            'focal_length_mm': 1000,
            'central_obstruction_mm': 63
        }, # Verified via Optical Universe (63mm CO, 9kg weight)
        'GSO_Dobson_6': {
            'brand': 'GSO',
            'name': 'Dobson 6"',
            'type': 'newtonian_reflector',
            'optical_length': 0,
            'mass': 8300,
            'tside_thread': '',
            'tside_gender': '',
            'cside_thread': '2"',
            'cside_gender': 'Female',
            'reversible': False,
            'bf_role': '',
            'aperture_mm': 152,
            'focal_length_mm': 1200,
            'central_obstruction_mm': 42
        }, # Verified via manufacturer specs
        'GSO_Dobson_8': {
            'brand': 'GSO',
            'name': 'Dobson 8"',
            'type': 'newtonian_reflector',
            'optical_length': 0,
            'mass': 11100,
            'tside_thread': '',
            'tside_gender': '',
            'cside_thread': '2"',
            'cside_gender': 'Female',
            'reversible': False,
            'bf_role': '',
            'aperture_mm': 203,
            'focal_length_mm': 1200,
            'central_obstruction_mm': 47
        }, # Verified via manufacturer specs
        'GSO_Dobson_10': {
            'brand': 'GSO',
            'name': 'Dobson 10"',
            'type': 'newtonian_reflector',
            'optical_length': 0,
            'mass': 18000,
            'tside_thread': '',
            'tside_gender': '',
            'cside_thread': '2"',
            'cside_gender': 'Female',
            'reversible': False,
            'bf_role': '',
            'aperture_mm': 254,
            'focal_length_mm': 1250,
            'central_obstruction_mm': 64
        }, # Verified via APM Telescopes and Optical Universe (64mm CO, 18kg OTA)
        'GSO_Dobson_12': {
            'brand': 'GSO',
            'name': 'Dobson 12"',
            'type': 'newtonian_reflector',
            'optical_length': 0,
            'mass': 21700,
            'tside_thread': '',
            'tside_gender': '',
            'cside_thread': '2"',
            'cside_gender': 'Female',
            'reversible': False,
            'bf_role': '',
            'aperture_mm': 305,
            'focal_length_mm': 1520,
            'central_obstruction_mm': 70
        }, # Verified via manufacturer specs
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
