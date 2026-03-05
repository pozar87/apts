from ..base import Eyepiece

class IstarEyepiece(Eyepiece):
    _DATABASE = {       'Istar_UWA_10mm_100': {       'bf_role': '',
                                      'brand': 'Istar',
                                      'cside_gender': '',
                                      'cside_thread': '',
                                      'field_of_view_deg': 100.0,
                                      'focal_length_mm': 10.0,
                                      'mass': 290,
                                      'name': 'UWA 10mm 100°',
                                      'optical_length': 0,
                                      'reversible': False,
                                      'tside_gender': 'Male',
                                      'tside_thread': '1.25"',
                                      'type': 'type_eyepiece'},
        'Istar_UWA_14mm_100': {       'bf_role': '',
                                      'brand': 'Istar',
                                      'cside_gender': '',
                                      'cside_thread': '',
                                      'field_of_view_deg': 100.0,
                                      'focal_length_mm': 14.0,
                                      'mass': 320,
                                      'name': 'UWA 14mm 100°',
                                      'optical_length': 0,
                                      'reversible': False,
                                      'tside_gender': 'Male',
                                      'tside_thread': '1.25"',
                                      'type': 'type_eyepiece'},
        'Istar_UWA_18mm_100': {       'bf_role': '',
                                      'brand': 'Istar',
                                      'cside_gender': '',
                                      'cside_thread': '',
                                      'field_of_view_deg': 100.0,
                                      'focal_length_mm': 18.0,
                                      'mass': 350,
                                      'name': 'UWA 18mm 100°',
                                      'optical_length': 0,
                                      'reversible': False,
                                      'tside_gender': 'Male',
                                      'tside_thread': '1.25"',
                                      'type': 'type_eyepiece'},
        'Istar_UWA_22mm_100': {       'bf_role': '',
                                      'brand': 'Istar',
                                      'cside_gender': '',
                                      'cside_thread': '',
                                      'field_of_view_deg': 100.0,
                                      'focal_length_mm': 22.0,
                                      'mass': 400,
                                      'name': 'UWA 22mm 100°',
                                      'optical_length': 0,
                                      'reversible': False,
                                      'tside_gender': 'Male',
                                      'tside_thread': '2"',
                                      'type': 'type_eyepiece'},
        'Istar_UWA_30mm_100': {       'bf_role': '',
                                      'brand': 'Istar',
                                      'cside_gender': '',
                                      'cside_thread': '',
                                      'field_of_view_deg': 100.0,
                                      'focal_length_mm': 30.0,
                                      'mass': 600,
                                      'name': 'UWA 30mm 100°',
                                      'optical_length': 0,
                                      'reversible': False,
                                      'tside_gender': 'Male',
                                      'tside_thread': '2"',
                                      'type': 'type_eyepiece'},
        'Istar_UWA_3_5mm_100': {       'bf_role': '',
                                       'brand': 'Istar',
                                       'cside_gender': '',
                                       'cside_thread': '',
                                       'field_of_view_deg': 100.0,
                                       'focal_length_mm': 3.5,
                                       'mass': 250,
                                       'name': 'UWA 3.5mm 100°',
                                       'optical_length': 0,
                                       'reversible': False,
                                       'tside_gender': 'Male',
                                       'tside_thread': '1.25"',
                                       'type': 'type_eyepiece'},
        'Istar_UWA_5mm_100': {       'bf_role': '',
                                     'brand': 'Istar',
                                     'cside_gender': '',
                                     'cside_thread': '',
                                     'field_of_view_deg': 100.0,
                                     'focal_length_mm': 5.0,
                                     'mass': 260,
                                     'name': 'UWA 5mm 100°',
                                     'optical_length': 0,
                                     'reversible': False,
                                     'tside_gender': 'Male',
                                     'tside_thread': '1.25"',
                                     'type': 'type_eyepiece'},
        'Istar_UWA_7mm_100': {       'bf_role': '',
                                     'brand': 'Istar',
                                     'cside_gender': '',
                                     'cside_thread': '',
                                     'field_of_view_deg': 100.0,
                                     'focal_length_mm': 7.0,
                                     'mass': 270,
                                     'name': 'UWA 7mm 100°',
                                     'optical_length': 0,
                                     'reversible': False,
                                     'tside_gender': 'Male',
                                     'tside_thread': '1.25"',
                                     'type': 'type_eyepiece'}}

    @classmethod
    def Istar_UWA_3_5mm_100(cls):
        return cls.from_database(cls._DATABASE['Istar_UWA_3_5mm_100'])

    @classmethod
    def Istar_UWA_5mm_100(cls):
        return cls.from_database(cls._DATABASE['Istar_UWA_5mm_100'])

    @classmethod
    def Istar_UWA_7mm_100(cls):
        return cls.from_database(cls._DATABASE['Istar_UWA_7mm_100'])

    @classmethod
    def Istar_UWA_10mm_100(cls):
        return cls.from_database(cls._DATABASE['Istar_UWA_10mm_100'])

    @classmethod
    def Istar_UWA_14mm_100(cls):
        return cls.from_database(cls._DATABASE['Istar_UWA_14mm_100'])

    @classmethod
    def Istar_UWA_18mm_100(cls):
        return cls.from_database(cls._DATABASE['Istar_UWA_18mm_100'])

    @classmethod
    def Istar_UWA_22mm_100(cls):
        return cls.from_database(cls._DATABASE['Istar_UWA_22mm_100'])

    @classmethod
    def Istar_UWA_30mm_100(cls):
        return cls.from_database(cls._DATABASE['Istar_UWA_30mm_100'])