from ..base import Telescope

class TelevueTelescope(Telescope):
    _DATABASE = {
        'TeleVue_NP101is': {
            'aperture_mm': 101,
            'bf_role': '',
            'brand': 'TeleVue',
            'central_obstruction_mm': 0,
            'cside_gender': 'Male',
            'cside_thread': 'M48',
            'focal_length_mm': 540,
            'mass': 4850,
            'name': 'NP101is',
            'optical_length': 0,
            'reversible': False,
            'tside_gender': '',
            'tside_thread': '',
            'type': 'type_refractor'
        }, # Verified via specs (10.7 lbs OTA)
        'TeleVue_NP127fli': {
            'aperture_mm': 127,
            'bf_role': '',
            'brand': 'TeleVue',
            'central_obstruction_mm': 0,
            'cside_gender': 'Male',
            'cside_thread': 'M68',
            'focal_length_mm': 660,
            'mass': 6500,
            'name': 'NP127fli',
            'optical_length': 0,
            'reversible': False,
            'tside_gender': '',
            'tside_thread': '',
            'type': 'type_refractor'
        },
        'TeleVue_TV_102': {
            'aperture_mm': 102,
            'bf_role': '',
            'brand': 'TeleVue',
            'central_obstruction_mm': 0,
            'cside_gender': 'Male',
            'cside_thread': 'M48',
            'focal_length_mm': 880,
            'mass': 4000,
            'name': 'TV-102',
            'optical_length': 0,
            'reversible': False,
            'tside_gender': '',
            'tside_thread': '',
            'type': 'type_refractor'
        }, # Verified via operating guide
        'TeleVue_TV_60': {
            'aperture_mm': 60,
            'bf_role': '',
            'brand': 'TeleVue',
            'central_obstruction_mm': 0,
            'cside_gender': 'Male',
            'cside_thread': 'M48',
            'focal_length_mm': 360,
            'mass': 1360,
            'name': 'TV-60',
            'optical_length': 0,
            'reversible': False,
            'tside_gender': '',
            'tside_thread': '',
            'type': 'type_refractor'
        }, # Verified via specs (3 lbs)
        'TeleVue_TV_76': {
            'aperture_mm': 76,
            'bf_role': '',
            'brand': 'TeleVue',
            'central_obstruction_mm': 0,
            'cside_gender': 'Male',
            'cside_thread': 'M48',
            'focal_length_mm': 480,
            'mass': 2310,
            'name': 'TV-76',
            'optical_length': 0,
            'reversible': False,
            'tside_gender': '',
            'tside_thread': '',
            'type': 'type_refractor'
        }, # Verified via specs (5.1 lbs)
        'TeleVue_TV_85': {
            'aperture_mm': 85,
            'bf_role': '',
            'brand': 'TeleVue',
            'central_obstruction_mm': 0,
            'cside_gender': 'Male',
            'cside_thread': 'M48',
            'focal_length_mm': 600,
            'mass': 2770,
            'name': 'TV-85',
            'optical_length': 0,
            'reversible': False,
            'tside_gender': '',
            'tside_thread': '',
            'type': 'type_refractor'
        }, # Verified via specs (6.1 lbs)
        'TeleVue_TV_NP101': {
            'aperture_mm': 101,
            'bf_role': '',
            'brand': 'TeleVue',
            'central_obstruction_mm': 0,
            'cside_gender': 'Male',
            'cside_thread': 'M48',
            'focal_length_mm': 540,
            'mass': 4220,
            'name': 'TV-NP101',
            'optical_length': 0,
            'reversible': False,
            'tside_gender': '',
            'tside_thread': '',
            'type': 'type_refractor'
        }, # Verified via specs (9.3 lbs)
        'TeleVue_TV_NP127is': {
            'aperture_mm': 127,
            'bf_role': '',
            'brand': 'TeleVue',
            'central_obstruction_mm': 0,
            'cside_gender': 'Male',
            'cside_thread': 'M68',
            'focal_length_mm': 660,
            'mass': 6580,
            'name': 'TV-NP127is',
            'optical_length': 0,
            'reversible': False,
            'tside_gender': '',
            'tside_thread': '',
            'type': 'type_refractor'
        }, # Verified via specs (14.5 lbs)
    }

    @classmethod
    def TeleVue_NP101is(cls):
        return cls.from_database(cls._DATABASE['TeleVue_NP101is'])

    @classmethod
    def TeleVue_NP127fli(cls):
        return cls.from_database(cls._DATABASE['TeleVue_NP127fli'])

    @classmethod
    def TeleVue_TV_60(cls):
        return cls.from_database(cls._DATABASE['TeleVue_TV_60'])

    @classmethod
    def TeleVue_TV_76(cls):
        return cls.from_database(cls._DATABASE['TeleVue_TV_76'])

    @classmethod
    def TeleVue_TV_85(cls):
        return cls.from_database(cls._DATABASE['TeleVue_TV_85'])

    @classmethod
    def TeleVue_TV_102(cls):
        return cls.from_database(cls._DATABASE['TeleVue_TV_102'])

    @classmethod
    def TeleVue_TV_NP127is(cls):
        return cls.from_database(cls._DATABASE['TeleVue_TV_NP127is'])

    @classmethod
    def TeleVue_TV_NP101(cls):
        return cls.from_database(cls._DATABASE['TeleVue_TV_NP101'])
