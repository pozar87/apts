from ..base import Eyepiece

class LeicaEyepiece(Eyepiece):
    _DATABASE = {       'Leica_ASPH_10mm': {       'bf_role': '',
                                   'brand': 'Leica',
                                   'cside_gender': '',
                                   'cside_thread': '',
                                   'field_of_view_deg': 50,
                                   'focal_length_mm': 10.0,
                                   'mass': 350,
                                   'name': 'ASPH 10mm',
                                   'optical_length': 0,
                                   'reversible': False,
                                   'tside_gender': 'Male',
                                   'tside_thread': '1.25"',
                                   'type': 'type_eyepiece'},
        'Leica_ASPH_12_5mm_v2': {       'bf_role': '',
                                        'brand': 'Leica',
                                        'cside_gender': '',
                                        'cside_thread': '',
                                        'field_of_view_deg': 50,
                                        'focal_length_mm': 12.5,
                                        'mass': 370,
                                        'name': 'ASPH 12.5mm (v2)',
                                        'optical_length': 0,
                                        'reversible': False,
                                        'tside_gender': 'Male',
                                        'tside_thread': '1.25"',
                                        'type': 'type_eyepiece'},
        'Leica_ASPH_17_5mm': {       'bf_role': '',
                                     'brand': 'Leica',
                                     'cside_gender': '',
                                     'cside_thread': '',
                                     'field_of_view_deg': 50,
                                     'focal_length_mm': 17.5,
                                     'mass': 380,
                                     'name': 'ASPH 17.5mm',
                                     'optical_length': 0,
                                     'reversible': False,
                                     'tside_gender': 'Male',
                                     'tside_thread': '1.25"',
                                     'type': 'type_eyepiece'},
        'Leica_ASPH_20mm_v2': {       'bf_role': '',
                                      'brand': 'Leica',
                                      'cside_gender': '',
                                      'cside_thread': '',
                                      'field_of_view_deg': 50,
                                      'focal_length_mm': 20.0,
                                      'mass': 400,
                                      'name': 'ASPH 20mm (v2)',
                                      'optical_length': 0,
                                      'reversible': False,
                                      'tside_gender': 'Male',
                                      'tside_thread': '1.25"',
                                      'type': 'type_eyepiece'},
        'Leica_ASPH_25mm': {       'bf_role': '',
                                   'brand': 'Leica',
                                   'cside_gender': '',
                                   'cside_thread': '',
                                   'field_of_view_deg': 50,
                                   'focal_length_mm': 25.0,
                                   'mass': 410,
                                   'name': 'ASPH 25mm',
                                   'optical_length': 0,
                                   'reversible': False,
                                   'tside_gender': 'Male',
                                   'tside_thread': '1.25"',
                                   'type': 'type_eyepiece'},
        'Leica_ASPH_30mm': {       'bf_role': '',
                                   'brand': 'Leica',
                                   'cside_gender': '',
                                   'cside_thread': '',
                                   'field_of_view_deg': 50,
                                   'focal_length_mm': 30.0,
                                   'mass': 450,
                                   'name': 'ASPH 30mm',
                                   'optical_length': 0,
                                   'reversible': False,
                                   'tside_gender': 'Male',
                                   'tside_thread': '1.25"',
                                   'type': 'type_eyepiece'},
        'Leica_ASPH_6_5mm_v2': {       'bf_role': '',
                                       'brand': 'Leica',
                                       'cside_gender': '',
                                       'cside_thread': '',
                                       'field_of_view_deg': 50,
                                       'focal_length_mm': 6.5,
                                       'mass': 320,
                                       'name': 'ASPH 6.5mm (v2)',
                                       'optical_length': 0,
                                       'reversible': False,
                                       'tside_gender': 'Male',
                                       'tside_thread': '1.25"',
                                       'type': 'type_eyepiece'}}

    @classmethod
    def Leica_ASPH_10mm(cls):
        return cls.from_database(cls._DATABASE['Leica_ASPH_10mm'])

    @classmethod
    def Leica_ASPH_17_5mm(cls):
        return cls.from_database(cls._DATABASE['Leica_ASPH_17_5mm'])

    @classmethod
    def Leica_ASPH_25mm(cls):
        return cls.from_database(cls._DATABASE['Leica_ASPH_25mm'])

    @classmethod
    def Leica_ASPH_30mm(cls):
        return cls.from_database(cls._DATABASE['Leica_ASPH_30mm'])

    @classmethod
    def Leica_ASPH_6_5mm_v2(cls):
        return cls.from_database(cls._DATABASE['Leica_ASPH_6_5mm_v2'])

    @classmethod
    def Leica_ASPH_12_5mm_v2(cls):
        return cls.from_database(cls._DATABASE['Leica_ASPH_12_5mm_v2'])

    @classmethod
    def Leica_ASPH_20mm_v2(cls):
        return cls.from_database(cls._DATABASE['Leica_ASPH_20mm_v2'])