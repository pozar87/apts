from ..base import Eyepiece

class MasuyamaEyepiece(Eyepiece):
    _DATABASE = {       'Masuyama_10mm_85': {       'bf_role': '',
                                    'brand': 'Masuyama',
                                    'cside_gender': '',
                                    'cside_thread': '',
                                    'field_of_view_deg': 85.0,
                                    'focal_length_mm': 10.0,
                                    'mass': 170,
                                    'name': '10mm 85°',
                                    'optical_length': 0,
                                    'reversible': False,
                                    'tside_gender': 'Male',
                                    'tside_thread': '1.25"',
                                    'type': 'type_eyepiece'},
        'Masuyama_12_5mm_85': {       'bf_role': '',
                                      'brand': 'Masuyama',
                                      'cside_gender': '',
                                      'cside_thread': '',
                                      'field_of_view_deg': 85.0,
                                      'focal_length_mm': 12.5,
                                      'mass': 180,
                                      'name': '12.5mm 85°',
                                      'optical_length': 0,
                                      'reversible': False,
                                      'tside_gender': 'Male',
                                      'tside_thread': '1.25"',
                                      'type': 'type_eyepiece'},
        'Masuyama_15mm_85': {       'bf_role': '',
                                    'brand': 'Masuyama',
                                    'cside_gender': '',
                                    'cside_thread': '',
                                    'field_of_view_deg': 85.0,
                                    'focal_length_mm': 15.0,
                                    'mass': 180,
                                    'name': '15mm 85°',
                                    'optical_length': 0,
                                    'reversible': False,
                                    'tside_gender': 'Male',
                                    'tside_thread': '1.25"',
                                    'type': 'type_eyepiece'},
        'Masuyama_20mm_85': {       'bf_role': '',
                                    'brand': 'Masuyama',
                                    'cside_gender': '',
                                    'cside_thread': '',
                                    'field_of_view_deg': 85.0,
                                    'focal_length_mm': 20.0,
                                    'mass': 200,
                                    'name': '20mm 85°',
                                    'optical_length': 0,
                                    'reversible': False,
                                    'tside_gender': 'Male',
                                    'tside_thread': '1.25"',
                                    'type': 'type_eyepiece'},
        'Masuyama_25mm_85': {       'bf_role': '',
                                    'brand': 'Masuyama',
                                    'cside_gender': '',
                                    'cside_thread': '',
                                    'field_of_view_deg': 85.0,
                                    'focal_length_mm': 25.0,
                                    'mass': 220,
                                    'name': '25mm 85°',
                                    'optical_length': 0,
                                    'reversible': False,
                                    'tside_gender': 'Male',
                                    'tside_thread': '1.25"',
                                    'type': 'type_eyepiece'},
        'Masuyama_32mm_85': {       'bf_role': '',
                                    'brand': 'Masuyama',
                                    'cside_gender': '',
                                    'cside_thread': '',
                                    'field_of_view_deg': 85.0,
                                    'focal_length_mm': 32.0,
                                    'mass': 280,
                                    'name': '32mm 85°',
                                    'optical_length': 0,
                                    'reversible': False,
                                    'tside_gender': 'Male',
                                    'tside_thread': '1.25"',
                                    'type': 'type_eyepiece'},
        'Masuyama_5mm_85': {       'bf_role': '',
                                   'brand': 'Masuyama',
                                   'cside_gender': '',
                                   'cside_thread': '',
                                   'field_of_view_deg': 85.0,
                                   'focal_length_mm': 5.0,
                                   'mass': 160,
                                   'name': '5mm 85°',
                                   'optical_length': 0,
                                   'reversible': False,
                                   'tside_gender': 'Male',
                                   'tside_thread': '1.25"',
                                   'type': 'type_eyepiece'},
        'Masuyama_8mm_85': {       'bf_role': '',
                                   'brand': 'Masuyama',
                                   'cside_gender': '',
                                   'cside_thread': '',
                                   'field_of_view_deg': 85.0,
                                   'focal_length_mm': 8.0,
                                   'mass': 165,
                                   'name': '8mm 85°',
                                   'optical_length': 0,
                                   'reversible': False,
                                   'tside_gender': 'Male',
                                   'tside_thread': '1.25"',
                                   'type': 'type_eyepiece'}}

    @classmethod
    def Masuyama_5mm_85(cls):
        return cls.from_database(cls._DATABASE['Masuyama_5mm_85'])

    @classmethod
    def Masuyama_8mm_85(cls):
        return cls.from_database(cls._DATABASE['Masuyama_8mm_85'])

    @classmethod
    def Masuyama_10mm_85(cls):
        return cls.from_database(cls._DATABASE['Masuyama_10mm_85'])

    @classmethod
    def Masuyama_15mm_85(cls):
        return cls.from_database(cls._DATABASE['Masuyama_15mm_85'])

    @classmethod
    def Masuyama_20mm_85(cls):
        return cls.from_database(cls._DATABASE['Masuyama_20mm_85'])

    @classmethod
    def Masuyama_25mm_85(cls):
        return cls.from_database(cls._DATABASE['Masuyama_25mm_85'])

    @classmethod
    def Masuyama_32mm_85(cls):
        return cls.from_database(cls._DATABASE['Masuyama_32mm_85'])

    @classmethod
    def Masuyama_12_5mm_85(cls):
        return cls.from_database(cls._DATABASE['Masuyama_12_5mm_85'])