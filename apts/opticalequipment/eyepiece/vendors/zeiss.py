from ..base import Eyepiece

class ZeissEyepiece(Eyepiece):
    _DATABASE = {       'Zeiss_Abbe_Ortho_10mm': {       'bf_role': '',
                                         'brand': 'Zeiss',
                                         'cside_gender': '',
                                         'cside_thread': '',
                                         'field_of_view_deg': 50,
                                         'focal_length_mm': 10.0,
                                         'mass': 280,
                                         'name': 'Abbe Ortho 10mm',
                                         'optical_length': 0,
                                         'reversible': False,
                                         'tside_gender': 'Male',
                                         'tside_thread': '1.25"',
                                         'type': 'type_eyepiece'},
        'Zeiss_Abbe_Ortho_16mm': {       'bf_role': '',
                                         'brand': 'Zeiss',
                                         'cside_gender': '',
                                         'cside_thread': '',
                                         'field_of_view_deg': 50,
                                         'focal_length_mm': 16.0,
                                         'mass': 320,
                                         'name': 'Abbe Ortho 16mm',
                                         'optical_length': 0,
                                         'reversible': False,
                                         'tside_gender': 'Male',
                                         'tside_thread': '1.25"',
                                         'type': 'type_eyepiece'},
        'Zeiss_Abbe_Ortho_25mm': {       'bf_role': '',
                                         'brand': 'Zeiss',
                                         'cside_gender': '',
                                         'cside_thread': '',
                                         'field_of_view_deg': 50,
                                         'focal_length_mm': 25.0,
                                         'mass': 380,
                                         'name': 'Abbe Ortho 25mm',
                                         'optical_length': 0,
                                         'reversible': False,
                                         'tside_gender': 'Male',
                                         'tside_thread': '1.25"',
                                         'type': 'type_eyepiece'},
        'Zeiss_Abbe_Ortho_4mm': {       'bf_role': '',
                                        'brand': 'Zeiss',
                                        'cside_gender': '',
                                        'cside_thread': '',
                                        'field_of_view_deg': 50,
                                        'focal_length_mm': 4.0,
                                        'mass': 250,
                                        'name': 'Abbe Ortho 4mm',
                                        'optical_length': 0,
                                        'reversible': False,
                                        'tside_gender': 'Male',
                                        'tside_thread': '1.25"',
                                        'type': 'type_eyepiece'},
        'Zeiss_Abbe_Ortho_6mm': {       'bf_role': '',
                                        'brand': 'Zeiss',
                                        'cside_gender': '',
                                        'cside_thread': '',
                                        'field_of_view_deg': 50,
                                        'focal_length_mm': 6.0,
                                        'mass': 260,
                                        'name': 'Abbe Ortho 6mm',
                                        'optical_length': 0,
                                        'reversible': False,
                                        'tside_gender': 'Male',
                                        'tside_thread': '1.25"',
                                        'type': 'type_eyepiece'}}

    @classmethod
    def Zeiss_Abbe_Ortho_4mm(cls):
        return cls.from_database(cls._DATABASE['Zeiss_Abbe_Ortho_4mm'])

    @classmethod
    def Zeiss_Abbe_Ortho_6mm(cls):
        return cls.from_database(cls._DATABASE['Zeiss_Abbe_Ortho_6mm'])

    @classmethod
    def Zeiss_Abbe_Ortho_10mm(cls):
        return cls.from_database(cls._DATABASE['Zeiss_Abbe_Ortho_10mm'])

    @classmethod
    def Zeiss_Abbe_Ortho_16mm(cls):
        return cls.from_database(cls._DATABASE['Zeiss_Abbe_Ortho_16mm'])

    @classmethod
    def Zeiss_Abbe_Ortho_25mm(cls):
        return cls.from_database(cls._DATABASE['Zeiss_Abbe_Ortho_25mm'])