from ..base import Telescope

class IoptronTelescope(Telescope):
    _DATABASE = {
        'iOptron_Photron_RC_6': {
            'brand': 'iOptron',
            'name': 'Photron 6" RC',
            'type': 'catadioptric',
            'optical_length': 0,
            'mass': 5443, # 12 lbs
            'tside_thread': '',
            'tside_gender': '',
            'cside_thread': 'M90',
            'cside_gender': 'Male',
            'reversible': False,
            'bf_role': '',
            'aperture_mm': 150,
            'focal_length_mm': 1370,
            'central_obstruction_mm': 67 # Verified via iOptron Website
        },
        'iOptron_Photron_RC_8': {
            'brand': 'iOptron',
            'name': 'Photron 8" RC',
            'type': 'catadioptric',
            'optical_length': 0,
            'mass': 8165, # 18 lbs
            'tside_thread': '',
            'tside_gender': '',
            'cside_thread': 'M90',
            'cside_gender': 'Male',
            'reversible': False,
            'bf_role': '',
            'aperture_mm': 200,
            'focal_length_mm': 1624,
            'central_obstruction_mm': 95 # Verified via iOptron Website
        },
        'iOptron_Photron_RC_10_Steel': {
            'brand': 'iOptron',
            'name': 'Photron 10" RC (Steel)',
            'type': 'catadioptric',
            'optical_length': 0,
            'mass': 15876, # 35 lbs
            'tside_thread': '',
            'tside_gender': '',
            'cside_thread': 'M117',
            'cside_gender': 'Male',
            'reversible': False,
            'bf_role': '',
            'aperture_mm': 250,
            'focal_length_mm': 2000,
            'central_obstruction_mm': 110 # Verified via iOptron Website
        },
        'iOptron_Photron_RC_10_Truss': {
            'brand': 'iOptron',
            'name': 'Photron 10" RC (Truss)',
            'type': 'catadioptric',
            'optical_length': 0,
            'mass': 15422, # 34 lbs
            'tside_thread': '',
            'tside_gender': '',
            'cside_thread': 'M117',
            'cside_gender': 'Male',
            'reversible': False,
            'bf_role': '',
            'aperture_mm': 254,
            'focal_length_mm': 2032,
            'central_obstruction_mm': 110 # Verified via iOptron Manual
        },
        'iOptron_Photron_RC_12_Truss': {
            'brand': 'iOptron',
            'name': 'Photron 12" RC (Truss)',
            'type': 'catadioptric',
            'optical_length': 0,
            'mass': 24040, # 53 lbs
            'tside_thread': '',
            'tside_gender': '',
            'cside_thread': 'M117',
            'cside_gender': 'Male',
            'reversible': False,
            'bf_role': '',
            'aperture_mm': 304,
            'focal_length_mm': 2432,
            'central_obstruction_mm': 150 # Verified via iOptron Manual
        },
        'iOptron_Photron_RC_16_Truss': {
            'brand': 'iOptron',
            'name': 'Photron 16" RC (Truss)',
            'type': 'catadioptric',
            'optical_length': 0,
            'mass': 42184, # 93 lbs
            'tside_thread': '',
            'tside_gender': '',
            'cside_thread': 'M117',
            'cside_gender': 'Male',
            'reversible': False,
            'bf_role': '',
            'aperture_mm': 406,
            'focal_length_mm': 3250,
            'central_obstruction_mm': 171 # Estimated based on 42% obstruction typical for these large RCs
        },
        'iOptron_80mm_APO': {
            'brand': 'iOptron',
            'name': 'iOptron 80mm APO',
            'type': 'type_refractor',
            'optical_length': 0,
            'mass': 3100,
            'tside_thread': '',
            'tside_gender': '',
            'cside_thread': 'M48',
            'cside_gender': 'Male',
            'reversible': False,
            'bf_role': '',
            'aperture_mm': 80,
            'focal_length_mm': 480,
            'central_obstruction_mm': 0
        },
        'iOptron_102mm_APO': {
            'brand': 'iOptron',
            'name': 'iOptron 102mm APO',
            'type': 'type_refractor',
            'optical_length': 0,
            'mass': 4500,
            'tside_thread': '',
            'tside_gender': '',
            'cside_thread': 'M48',
            'cside_gender': 'Male',
            'reversible': False,
            'bf_role': '',
            'aperture_mm': 102,
            'focal_length_mm': 714,
            'central_obstruction_mm': 0
        },
        'iOptron_R80': {
            'brand': 'iOptron',
            'name': 'iOptron R80',
            'type': 'type_refractor',
            'optical_length': 0,
            'mass': 998, # 2.2 lbs
            'tside_thread': '',
            'tside_gender': '',
            'cside_thread': '1.25"',
            'cside_gender': 'Female',
            'reversible': False,
            'bf_role': '',
            'aperture_mm': 80,
            'focal_length_mm': 400,
            'central_obstruction_mm': 0 # Verified via iOptron Manual
        },
    }

    @classmethod
    def iOptron_Photron_RC_6(cls):
        return cls.from_database(cls._DATABASE['iOptron_Photron_RC_6'])

    @classmethod
    def iOptron_iOptron_RC_6(cls):
        """Legacy method for backward compatibility."""
        return cls.iOptron_Photron_RC_6()

    @classmethod
    def iOptron_Photron_RC_8(cls):
        return cls.from_database(cls._DATABASE['iOptron_Photron_RC_8'])

    @classmethod
    def iOptron_iOptron_RC_8(cls):
        """Legacy method for backward compatibility."""
        return cls.iOptron_Photron_RC_8()

    @classmethod
    def iOptron_Photron_RC_10_Steel(cls):
        return cls.from_database(cls._DATABASE['iOptron_Photron_RC_10_Steel'])

    @classmethod
    def iOptron_Photron_RC_10_Truss(cls):
        return cls.from_database(cls._DATABASE['iOptron_Photron_RC_10_Truss'])

    @classmethod
    def iOptron_Photron_RC_12_Truss(cls):
        return cls.from_database(cls._DATABASE['iOptron_Photron_RC_12_Truss'])

    @classmethod
    def iOptron_Photron_RC_16_Truss(cls):
        return cls.from_database(cls._DATABASE['iOptron_Photron_RC_16_Truss'])

    @classmethod
    def iOptron_80mm_APO(cls):
        return cls.from_database(cls._DATABASE['iOptron_80mm_APO'])

    @classmethod
    def iOptron_iOptron_80mm_APO(cls):
        """Legacy method for backward compatibility."""
        return cls.iOptron_80mm_APO()

    @classmethod
    def iOptron_102mm_APO(cls):
        return cls.from_database(cls._DATABASE['iOptron_102mm_APO'])

    @classmethod
    def iOptron_iOptron_102mm_APO(cls):
        """Legacy method for backward compatibility."""
        return cls.iOptron_102mm_APO()

    @classmethod
    def iOptron_R80(cls):
        return cls.from_database(cls._DATABASE['iOptron_R80'])
