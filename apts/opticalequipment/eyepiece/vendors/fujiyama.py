from ..base import Eyepiece

class FujiyamaEyepiece(Eyepiece):
    _DATABASE = {       'Fujiyama_HD_Ortho_12_5mm': {       'bf_role': '',
                                            'brand': 'Fujiyama',
                                            'cside_gender': '',
                                            'cside_thread': '',
                                            'field_of_view_deg': 50,
                                            'focal_length_mm': 12.5,
                                            'mass': 140,
                                            'name': 'HD Ortho 12.5mm',
                                            'optical_length': 0,
                                            'reversible': False,
                                            'tside_gender': 'Male',
                                            'tside_thread': '1.25"',
                                            'type': 'type_eyepiece'},
        'Fujiyama_HD_Ortho_18mm': {       'bf_role': '',
                                          'brand': 'Fujiyama',
                                          'cside_gender': '',
                                          'cside_thread': '',
                                          'field_of_view_deg': 50,
                                          'focal_length_mm': 18.0,
                                          'mass': 160,
                                          'name': 'HD Ortho 18mm',
                                          'optical_length': 0,
                                          'reversible': False,
                                          'tside_gender': 'Male',
                                          'tside_thread': '1.25"',
                                          'type': 'type_eyepiece'},
        'Fujiyama_HD_Ortho_25mm': {       'bf_role': '',
                                          'brand': 'Fujiyama',
                                          'cside_gender': '',
                                          'cside_thread': '',
                                          'field_of_view_deg': 50,
                                          'focal_length_mm': 25.0,
                                          'mass': 180,
                                          'name': 'HD Ortho 25mm',
                                          'optical_length': 0,
                                          'reversible': False,
                                          'tside_gender': 'Male',
                                          'tside_thread': '1.25"',
                                          'type': 'type_eyepiece'},
        'Fujiyama_HD_Ortho_4mm': {       'bf_role': '',
                                         'brand': 'Fujiyama',
                                         'cside_gender': '',
                                         'cside_thread': '',
                                         'field_of_view_deg': 50,
                                         'focal_length_mm': 4.0,
                                         'mass': 110,
                                         'name': 'HD Ortho 4mm',
                                         'optical_length': 0,
                                         'reversible': False,
                                         'tside_gender': 'Male',
                                         'tside_thread': '1.25"',
                                         'type': 'type_eyepiece'},
        'Fujiyama_HD_Ortho_5mm': {       'bf_role': '',
                                         'brand': 'Fujiyama',
                                         'cside_gender': '',
                                         'cside_thread': '',
                                         'field_of_view_deg': 50,
                                         'focal_length_mm': 5.0,
                                         'mass': 115,
                                         'name': 'HD Ortho 5mm',
                                         'optical_length': 0,
                                         'reversible': False,
                                         'tside_gender': 'Male',
                                         'tside_thread': '1.25"',
                                         'type': 'type_eyepiece'},
        'Fujiyama_HD_Ortho_6mm': {       'bf_role': '',
                                         'brand': 'Fujiyama',
                                         'cside_gender': '',
                                         'cside_thread': '',
                                         'field_of_view_deg': 50,
                                         'focal_length_mm': 6.0,
                                         'mass': 120,
                                         'name': 'HD Ortho 6mm',
                                         'optical_length': 0,
                                         'reversible': False,
                                         'tside_gender': 'Male',
                                         'tside_thread': '1.25"',
                                         'type': 'type_eyepiece'},
        'Fujiyama_HD_Ortho_7mm': {       'bf_role': '',
                                         'brand': 'Fujiyama',
                                         'cside_gender': '',
                                         'cside_thread': '',
                                         'field_of_view_deg': 50,
                                         'focal_length_mm': 7.0,
                                         'mass': 125,
                                         'name': 'HD Ortho 7mm',
                                         'optical_length': 0,
                                         'reversible': False,
                                         'tside_gender': 'Male',
                                         'tside_thread': '1.25"',
                                         'type': 'type_eyepiece'},
        'Fujiyama_HD_Ortho_9mm': {       'bf_role': '',
                                         'brand': 'Fujiyama',
                                         'cside_gender': '',
                                         'cside_thread': '',
                                         'field_of_view_deg': 50,
                                         'focal_length_mm': 9.0,
                                         'mass': 130,
                                         'name': 'HD Ortho 9mm',
                                         'optical_length': 0,
                                         'reversible': False,
                                         'tside_gender': 'Male',
                                         'tside_thread': '1.25"',
                                         'type': 'type_eyepiece'}}

    @classmethod
    def Fujiyama_HD_Ortho_4mm(cls):
        return cls.from_database(cls._DATABASE['Fujiyama_HD_Ortho_4mm'])

    @classmethod
    def Fujiyama_HD_Ortho_5mm(cls):
        return cls.from_database(cls._DATABASE['Fujiyama_HD_Ortho_5mm'])

    @classmethod
    def Fujiyama_HD_Ortho_6mm(cls):
        return cls.from_database(cls._DATABASE['Fujiyama_HD_Ortho_6mm'])

    @classmethod
    def Fujiyama_HD_Ortho_7mm(cls):
        return cls.from_database(cls._DATABASE['Fujiyama_HD_Ortho_7mm'])

    @classmethod
    def Fujiyama_HD_Ortho_9mm(cls):
        return cls.from_database(cls._DATABASE['Fujiyama_HD_Ortho_9mm'])

    @classmethod
    def Fujiyama_HD_Ortho_12_5mm(cls):
        return cls.from_database(cls._DATABASE['Fujiyama_HD_Ortho_12_5mm'])

    @classmethod
    def Fujiyama_HD_Ortho_18mm(cls):
        return cls.from_database(cls._DATABASE['Fujiyama_HD_Ortho_18mm'])

    @classmethod
    def Fujiyama_HD_Ortho_25mm(cls):
        return cls.from_database(cls._DATABASE['Fujiyama_HD_Ortho_25mm'])