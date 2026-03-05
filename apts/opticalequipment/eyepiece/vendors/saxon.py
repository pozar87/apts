from ..base import Eyepiece

class SaxonEyepiece(Eyepiece):
    _DATABASE = {       'Saxon_Plossl_12_5mm': {       'bf_role': '',
                                       'brand': 'Saxon',
                                       'cside_gender': '',
                                       'cside_thread': '',
                                       'field_of_view_deg': 50,
                                       'focal_length_mm': 12.5,
                                       'mass': 120,
                                       'name': 'Plossl 12.5mm',
                                       'optical_length': 0,
                                       'reversible': False,
                                       'tside_gender': 'Male',
                                       'tside_thread': '1.25"',
                                       'type': 'type_eyepiece'},
        'Saxon_Plossl_16mm': {       'bf_role': '',
                                     'brand': 'Saxon',
                                     'cside_gender': '',
                                     'cside_thread': '',
                                     'field_of_view_deg': 50,
                                     'focal_length_mm': 16.0,
                                     'mass': 130,
                                     'name': 'Plossl 16mm',
                                     'optical_length': 0,
                                     'reversible': False,
                                     'tside_gender': 'Male',
                                     'tside_thread': '1.25"',
                                     'type': 'type_eyepiece'},
        'Saxon_Plossl_20mm': {       'bf_role': '',
                                     'brand': 'Saxon',
                                     'cside_gender': '',
                                     'cside_thread': '',
                                     'field_of_view_deg': 50,
                                     'focal_length_mm': 20.0,
                                     'mass': 140,
                                     'name': 'Plossl 20mm',
                                     'optical_length': 0,
                                     'reversible': False,
                                     'tside_gender': 'Male',
                                     'tside_thread': '1.25"',
                                     'type': 'type_eyepiece'},
        'Saxon_Plossl_25mm': {       'bf_role': '',
                                     'brand': 'Saxon',
                                     'cside_gender': '',
                                     'cside_thread': '',
                                     'field_of_view_deg': 50,
                                     'focal_length_mm': 25.0,
                                     'mass': 160,
                                     'name': 'Plossl 25mm',
                                     'optical_length': 0,
                                     'reversible': False,
                                     'tside_gender': 'Male',
                                     'tside_thread': '1.25"',
                                     'type': 'type_eyepiece'},
        'Saxon_Plossl_4mm': {       'bf_role': '',
                                    'brand': 'Saxon',
                                    'cside_gender': '',
                                    'cside_thread': '',
                                    'field_of_view_deg': 50,
                                    'focal_length_mm': 4.0,
                                    'mass': 100,
                                    'name': 'Plossl 4mm',
                                    'optical_length': 0,
                                    'reversible': False,
                                    'tside_gender': 'Male',
                                    'tside_thread': '1.25"',
                                    'type': 'type_eyepiece'},
        'Saxon_Plossl_6mm': {       'bf_role': '',
                                    'brand': 'Saxon',
                                    'cside_gender': '',
                                    'cside_thread': '',
                                    'field_of_view_deg': 50,
                                    'focal_length_mm': 6.0,
                                    'mass': 105,
                                    'name': 'Plossl 6mm',
                                    'optical_length': 0,
                                    'reversible': False,
                                    'tside_gender': 'Male',
                                    'tside_thread': '1.25"',
                                    'type': 'type_eyepiece'},
        'Saxon_Plossl_9mm': {       'bf_role': '',
                                    'brand': 'Saxon',
                                    'cside_gender': '',
                                    'cside_thread': '',
                                    'field_of_view_deg': 50,
                                    'focal_length_mm': 9.0,
                                    'mass': 110,
                                    'name': 'Plossl 9mm',
                                    'optical_length': 0,
                                    'reversible': False,
                                    'tside_gender': 'Male',
                                    'tside_thread': '1.25"',
                                    'type': 'type_eyepiece'}}

    @classmethod
    def Saxon_Plossl_4mm(cls):
        return cls.from_database(cls._DATABASE['Saxon_Plossl_4mm'])

    @classmethod
    def Saxon_Plossl_6mm(cls):
        return cls.from_database(cls._DATABASE['Saxon_Plossl_6mm'])

    @classmethod
    def Saxon_Plossl_9mm(cls):
        return cls.from_database(cls._DATABASE['Saxon_Plossl_9mm'])

    @classmethod
    def Saxon_Plossl_12_5mm(cls):
        return cls.from_database(cls._DATABASE['Saxon_Plossl_12_5mm'])

    @classmethod
    def Saxon_Plossl_16mm(cls):
        return cls.from_database(cls._DATABASE['Saxon_Plossl_16mm'])

    @classmethod
    def Saxon_Plossl_20mm(cls):
        return cls.from_database(cls._DATABASE['Saxon_Plossl_20mm'])

    @classmethod
    def Saxon_Plossl_25mm(cls):
        return cls.from_database(cls._DATABASE['Saxon_Plossl_25mm'])