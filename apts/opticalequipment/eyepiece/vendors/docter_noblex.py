from ..base import Eyepiece

class Docter_noblexEyepiece(Eyepiece):
    _DATABASE = {       'Docter_Noblex_UWF_10mm': {       'bf_role': '',
                                          'brand': 'Docter/Noblex',
                                          'cside_gender': '',
                                          'cside_thread': '',
                                          'field_of_view_deg': 50,
                                          'focal_length_mm': 10.0,
                                          'mass': 200,
                                          'name': 'UWF 10mm',
                                          'optical_length': 0,
                                          'reversible': False,
                                          'tside_gender': 'Male',
                                          'tside_thread': '1.25"',
                                          'type': 'type_eyepiece'},
        'Docter_Noblex_UWF_12_5mm': {       'bf_role': '',
                                            'brand': 'Docter/Noblex',
                                            'cside_gender': '',
                                            'cside_thread': '',
                                            'field_of_view_deg': 50,
                                            'focal_length_mm': 12.5,
                                            'mass': 220,
                                            'name': 'UWF 12.5mm',
                                            'optical_length': 0,
                                            'reversible': False,
                                            'tside_gender': 'Male',
                                            'tside_thread': '1.25"',
                                            'type': 'type_eyepiece'},
        'Docter_Noblex_UWF_17mm': {       'bf_role': '',
                                          'brand': 'Docter/Noblex',
                                          'cside_gender': '',
                                          'cside_thread': '',
                                          'field_of_view_deg': 50,
                                          'focal_length_mm': 17.0,
                                          'mass': 270,
                                          'name': 'UWF 17mm',
                                          'optical_length': 0,
                                          'reversible': False,
                                          'tside_gender': 'Male',
                                          'tside_thread': '1.25"',
                                          'type': 'type_eyepiece'}}

    @classmethod
    def Docter_Noblex_UWF_10mm(cls):
        return cls.from_database(cls._DATABASE['Docter_Noblex_UWF_10mm'])

    @classmethod
    def Docter_Noblex_UWF_12_5mm(cls):
        return cls.from_database(cls._DATABASE['Docter_Noblex_UWF_12_5mm'])

    @classmethod
    def Docter_Noblex_UWF_17mm(cls):
        return cls.from_database(cls._DATABASE['Docter_Noblex_UWF_17mm'])