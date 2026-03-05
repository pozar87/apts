from ..base import Eyepiece

class SiebertEyepiece(Eyepiece):
    _DATABASE = {       'Siebert_Stellar_10mm': {       'bf_role': '',
                                        'brand': 'Siebert',
                                        'cside_gender': '',
                                        'cside_thread': '',
                                        'field_of_view_deg': 50,
                                        'focal_length_mm': 10.0,
                                        'mass': 215,
                                        'name': 'Stellar 10mm',
                                        'optical_length': 0,
                                        'reversible': False,
                                        'tside_gender': 'Male',
                                        'tside_thread': '1.25"',
                                        'type': 'type_eyepiece'},
        'Siebert_Stellar_13mm': {       'bf_role': '',
                                        'brand': 'Siebert',
                                        'cside_gender': '',
                                        'cside_thread': '',
                                        'field_of_view_deg': 50,
                                        'focal_length_mm': 13.0,
                                        'mass': 240,
                                        'name': 'Stellar 13mm',
                                        'optical_length': 0,
                                        'reversible': False,
                                        'tside_gender': 'Male',
                                        'tside_thread': '1.25"',
                                        'type': 'type_eyepiece'},
        'Siebert_Stellar_18mm': {       'bf_role': '',
                                        'brand': 'Siebert',
                                        'cside_gender': '',
                                        'cside_thread': '',
                                        'field_of_view_deg': 50,
                                        'focal_length_mm': 18.0,
                                        'mass': 270,
                                        'name': 'Stellar 18mm',
                                        'optical_length': 0,
                                        'reversible': False,
                                        'tside_gender': 'Male',
                                        'tside_thread': '1.25"',
                                        'type': 'type_eyepiece'},
        'Siebert_Stellar_24mm': {       'bf_role': '',
                                        'brand': 'Siebert',
                                        'cside_gender': '',
                                        'cside_thread': '',
                                        'field_of_view_deg': 50,
                                        'focal_length_mm': 24.0,
                                        'mass': 320,
                                        'name': 'Stellar 24mm',
                                        'optical_length': 0,
                                        'reversible': False,
                                        'tside_gender': 'Male',
                                        'tside_thread': '2"',
                                        'type': 'type_eyepiece'},
        'Siebert_Stellar_36mm': {       'bf_role': '',
                                        'brand': 'Siebert',
                                        'cside_gender': '',
                                        'cside_thread': '',
                                        'field_of_view_deg': 50,
                                        'focal_length_mm': 36.0,
                                        'mass': 500,
                                        'name': 'Stellar 36mm',
                                        'optical_length': 0,
                                        'reversible': False,
                                        'tside_gender': 'Male',
                                        'tside_thread': '2"',
                                        'type': 'type_eyepiece'},
        'Siebert_Stellar_4mm': {       'bf_role': '',
                                       'brand': 'Siebert',
                                       'cside_gender': '',
                                       'cside_thread': '',
                                       'field_of_view_deg': 50,
                                       'focal_length_mm': 4.0,
                                       'mass': 180,
                                       'name': 'Stellar 4mm',
                                       'optical_length': 0,
                                       'reversible': False,
                                       'tside_gender': 'Male',
                                       'tside_thread': '1.25"',
                                       'type': 'type_eyepiece'},
        'Siebert_Stellar_6mm': {       'bf_role': '',
                                       'brand': 'Siebert',
                                       'cside_gender': '',
                                       'cside_thread': '',
                                       'field_of_view_deg': 50,
                                       'focal_length_mm': 6.0,
                                       'mass': 190,
                                       'name': 'Stellar 6mm',
                                       'optical_length': 0,
                                       'reversible': False,
                                       'tside_gender': 'Male',
                                       'tside_thread': '1.25"',
                                       'type': 'type_eyepiece'},
        'Siebert_Stellar_8mm': {       'bf_role': '',
                                       'brand': 'Siebert',
                                       'cside_gender': '',
                                       'cside_thread': '',
                                       'field_of_view_deg': 50,
                                       'focal_length_mm': 8.0,
                                       'mass': 200,
                                       'name': 'Stellar 8mm',
                                       'optical_length': 0,
                                       'reversible': False,
                                       'tside_gender': 'Male',
                                       'tside_thread': '1.25"',
                                       'type': 'type_eyepiece'}}

    @classmethod
    def Siebert_Stellar_4mm(cls):
        return cls.from_database(cls._DATABASE['Siebert_Stellar_4mm'])

    @classmethod
    def Siebert_Stellar_6mm(cls):
        return cls.from_database(cls._DATABASE['Siebert_Stellar_6mm'])

    @classmethod
    def Siebert_Stellar_8mm(cls):
        return cls.from_database(cls._DATABASE['Siebert_Stellar_8mm'])

    @classmethod
    def Siebert_Stellar_10mm(cls):
        return cls.from_database(cls._DATABASE['Siebert_Stellar_10mm'])

    @classmethod
    def Siebert_Stellar_13mm(cls):
        return cls.from_database(cls._DATABASE['Siebert_Stellar_13mm'])

    @classmethod
    def Siebert_Stellar_18mm(cls):
        return cls.from_database(cls._DATABASE['Siebert_Stellar_18mm'])

    @classmethod
    def Siebert_Stellar_24mm(cls):
        return cls.from_database(cls._DATABASE['Siebert_Stellar_24mm'])

    @classmethod
    def Siebert_Stellar_36mm(cls):
        return cls.from_database(cls._DATABASE['Siebert_Stellar_36mm'])