from ..base import Eyepiece

class LuntEyepiece(Eyepiece):
    _DATABASE = {       'Lunt_H_alpha_12mm': {       'bf_role': '',
                                     'brand': 'Lunt',
                                     'cside_gender': '',
                                     'cside_thread': '',
                                     'field_of_view_deg': 50,
                                     'focal_length_mm': 12.0,
                                     'mass': 160,
                                     'name': 'H-alpha 12mm',
                                     'optical_length': 0,
                                     'reversible': False,
                                     'tside_gender': 'Male',
                                     'tside_thread': '1.25"',
                                     'type': 'type_eyepiece'},
        'Lunt_H_alpha_16mm': {       'bf_role': '',
                                     'brand': 'Lunt',
                                     'cside_gender': '',
                                     'cside_thread': '',
                                     'field_of_view_deg': 50,
                                     'focal_length_mm': 16.0,
                                     'mass': 170,
                                     'name': 'H-alpha 16mm',
                                     'optical_length': 0,
                                     'reversible': False,
                                     'tside_gender': 'Male',
                                     'tside_thread': '1.25"',
                                     'type': 'type_eyepiece'},
        'Lunt_H_alpha_19mm': {       'bf_role': '',
                                     'brand': 'Lunt',
                                     'cside_gender': '',
                                     'cside_thread': '',
                                     'field_of_view_deg': 50,
                                     'focal_length_mm': 19.0,
                                     'mass': 190,
                                     'name': 'H-alpha 19mm',
                                     'optical_length': 0,
                                     'reversible': False,
                                     'tside_gender': 'Male',
                                     'tside_thread': '1.25"',
                                     'type': 'type_eyepiece'},
        'Lunt_H_alpha_27mm': {       'bf_role': '',
                                     'brand': 'Lunt',
                                     'cside_gender': '',
                                     'cside_thread': '',
                                     'field_of_view_deg': 50,
                                     'focal_length_mm': 27.0,
                                     'mass': 250,
                                     'name': 'H-alpha 27mm',
                                     'optical_length': 0,
                                     'reversible': False,
                                     'tside_gender': 'Male',
                                     'tside_thread': '1.25"',
                                     'type': 'type_eyepiece'},
        'Lunt_H_alpha_7_5mm': {       'bf_role': '',
                                      'brand': 'Lunt',
                                      'cside_gender': '',
                                      'cside_thread': '',
                                      'field_of_view_deg': 50,
                                      'focal_length_mm': 7.5,
                                      'mass': 150,
                                      'name': 'H-alpha 7.5mm',
                                      'optical_length': 0,
                                      'reversible': False,
                                      'tside_gender': 'Male',
                                      'tside_thread': '1.25"',
                                      'type': 'type_eyepiece'}}

    @classmethod
    def Lunt_H_alpha_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Lunt_H_alpha_7_5mm'])

    @classmethod
    def Lunt_H_alpha_12mm(cls):
        return cls.from_database(cls._DATABASE['Lunt_H_alpha_12mm'])

    @classmethod
    def Lunt_H_alpha_16mm(cls):
        return cls.from_database(cls._DATABASE['Lunt_H_alpha_16mm'])

    @classmethod
    def Lunt_H_alpha_19mm(cls):
        return cls.from_database(cls._DATABASE['Lunt_H_alpha_19mm'])

    @classmethod
    def Lunt_H_alpha_27mm(cls):
        return cls.from_database(cls._DATABASE['Lunt_H_alpha_27mm'])