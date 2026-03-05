from ..base import Eyepiece

class Kokusai_kohkiEyepiece(Eyepiece):
    _DATABASE = {       'Kokusai_Kohki_Ortho_12mm': {       'bf_role': '',
                                            'brand': 'Kokusai Kohki',
                                            'cside_gender': '',
                                            'cside_thread': '',
                                            'field_of_view_deg': 50,
                                            'focal_length_mm': 12.0,
                                            'mass': 170,
                                            'name': 'Ortho 12mm',
                                            'optical_length': 0,
                                            'reversible': False,
                                            'tside_gender': 'Male',
                                            'tside_thread': '1.25"',
                                            'type': 'type_eyepiece'},
        'Kokusai_Kohki_Ortho_18mm': {       'bf_role': '',
                                            'brand': 'Kokusai Kohki',
                                            'cside_gender': '',
                                            'cside_thread': '',
                                            'field_of_view_deg': 50,
                                            'focal_length_mm': 18.0,
                                            'mass': 200,
                                            'name': 'Ortho 18mm',
                                            'optical_length': 0,
                                            'reversible': False,
                                            'tside_gender': 'Male',
                                            'tside_thread': '1.25"',
                                            'type': 'type_eyepiece'},
        'Kokusai_Kohki_Ortho_25mm': {       'bf_role': '',
                                            'brand': 'Kokusai Kohki',
                                            'cside_gender': '',
                                            'cside_thread': '',
                                            'field_of_view_deg': 50,
                                            'focal_length_mm': 25.0,
                                            'mass': 240,
                                            'name': 'Ortho 25mm',
                                            'optical_length': 0,
                                            'reversible': False,
                                            'tside_gender': 'Male',
                                            'tside_thread': '1.25"',
                                            'type': 'type_eyepiece'},
        'Kokusai_Kohki_Ortho_5mm': {       'bf_role': '',
                                           'brand': 'Kokusai Kohki',
                                           'cside_gender': '',
                                           'cside_thread': '',
                                           'field_of_view_deg': 50,
                                           'focal_length_mm': 5.0,
                                           'mass': 140,
                                           'name': 'Ortho 5mm',
                                           'optical_length': 0,
                                           'reversible': False,
                                           'tside_gender': 'Male',
                                           'tside_thread': '1.25"',
                                           'type': 'type_eyepiece'},
        'Kokusai_Kohki_Ortho_8mm': {       'bf_role': '',
                                           'brand': 'Kokusai Kohki',
                                           'cside_gender': '',
                                           'cside_thread': '',
                                           'field_of_view_deg': 50,
                                           'focal_length_mm': 8.0,
                                           'mass': 155,
                                           'name': 'Ortho 8mm',
                                           'optical_length': 0,
                                           'reversible': False,
                                           'tside_gender': 'Male',
                                           'tside_thread': '1.25"',
                                           'type': 'type_eyepiece'}}

    @classmethod
    def Kokusai_Kohki_Ortho_5mm(cls):
        return cls.from_database(cls._DATABASE['Kokusai_Kohki_Ortho_5mm'])

    @classmethod
    def Kokusai_Kohki_Ortho_8mm(cls):
        return cls.from_database(cls._DATABASE['Kokusai_Kohki_Ortho_8mm'])

    @classmethod
    def Kokusai_Kohki_Ortho_12mm(cls):
        return cls.from_database(cls._DATABASE['Kokusai_Kohki_Ortho_12mm'])

    @classmethod
    def Kokusai_Kohki_Ortho_18mm(cls):
        return cls.from_database(cls._DATABASE['Kokusai_Kohki_Ortho_18mm'])

    @classmethod
    def Kokusai_Kohki_Ortho_25mm(cls):
        return cls.from_database(cls._DATABASE['Kokusai_Kohki_Ortho_25mm'])