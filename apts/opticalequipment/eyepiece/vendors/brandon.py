from ..base import Eyepiece

class BrandonEyepiece(Eyepiece):
    _DATABASE = {       'Brandon_12mm': {       'bf_role': '',
                                'brand': 'Brandon',
                                'cside_gender': '',
                                'cside_thread': '',
                                'field_of_view_deg': 50,
                                'focal_length_mm': 12.0,
                                'mass': 140,
                                'name': '12mm',
                                'optical_length': 0,
                                'reversible': False,
                                'tside_gender': 'Male',
                                'tside_thread': '1.25"',
                                'type': 'type_eyepiece'},
        'Brandon_16mm': {       'bf_role': '',
                                'brand': 'Brandon',
                                'cside_gender': '',
                                'cside_thread': '',
                                'field_of_view_deg': 50,
                                'focal_length_mm': 16.0,
                                'mass': 150,
                                'name': '16mm',
                                'optical_length': 0,
                                'reversible': False,
                                'tside_gender': 'Male',
                                'tside_thread': '1.25"',
                                'type': 'type_eyepiece'},
        'Brandon_24mm': {       'bf_role': '',
                                'brand': 'Brandon',
                                'cside_gender': '',
                                'cside_thread': '',
                                'field_of_view_deg': 50,
                                'focal_length_mm': 24.0,
                                'mass': 170,
                                'name': '24mm',
                                'optical_length': 0,
                                'reversible': False,
                                'tside_gender': 'Male',
                                'tside_thread': '1.25"',
                                'type': 'type_eyepiece'},
        'Brandon_32mm': {       'bf_role': '',
                                'brand': 'Brandon',
                                'cside_gender': '',
                                'cside_thread': '',
                                'field_of_view_deg': 50,
                                'focal_length_mm': 32.0,
                                'mass': 200,
                                'name': '32mm',
                                'optical_length': 0,
                                'reversible': False,
                                'tside_gender': 'Male',
                                'tside_thread': '1.25"',
                                'type': 'type_eyepiece'},
        'Brandon_8mm': {       'bf_role': '',
                               'brand': 'Brandon',
                               'cside_gender': '',
                               'cside_thread': '',
                               'field_of_view_deg': 50,
                               'focal_length_mm': 8.0,
                               'mass': 130,
                               'name': '8mm',
                               'optical_length': 0,
                               'reversible': False,
                               'tside_gender': 'Male',
                               'tside_thread': '1.25"',
                               'type': 'type_eyepiece'}}

    @classmethod
    def Brandon_8mm(cls):
        return cls.from_database(cls._DATABASE['Brandon_8mm'])

    @classmethod
    def Brandon_12mm(cls):
        return cls.from_database(cls._DATABASE['Brandon_12mm'])

    @classmethod
    def Brandon_16mm(cls):
        return cls.from_database(cls._DATABASE['Brandon_16mm'])

    @classmethod
    def Brandon_24mm(cls):
        return cls.from_database(cls._DATABASE['Brandon_24mm'])

    @classmethod
    def Brandon_32mm(cls):
        return cls.from_database(cls._DATABASE['Brandon_32mm'])