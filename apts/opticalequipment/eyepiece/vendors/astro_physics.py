from ..base import Eyepiece

class Astro_physicsEyepiece(Eyepiece):
    _DATABASE = {       'Astro_Physics_MaxView_10mm': {       'bf_role': '',
                                              'brand': 'Astro-Physics',
                                              'cside_gender': '',
                                              'cside_thread': '',
                                              'field_of_view_deg': 50,
                                              'focal_length_mm': 10.0,
                                              'mass': 200,
                                              'name': 'MaxView 10mm',
                                              'optical_length': 0,
                                              'reversible': False,
                                              'tside_gender': 'Male',
                                              'tside_thread': '1.25"',
                                              'type': 'type_eyepiece'},
        'Astro_Physics_MaxView_15mm': {       'bf_role': '',
                                              'brand': 'Astro-Physics',
                                              'cside_gender': '',
                                              'cside_thread': '',
                                              'field_of_view_deg': 50,
                                              'focal_length_mm': 15.0,
                                              'mass': 230,
                                              'name': 'MaxView 15mm',
                                              'optical_length': 0,
                                              'reversible': False,
                                              'tside_gender': 'Male',
                                              'tside_thread': '1.25"',
                                              'type': 'type_eyepiece'},
        'Astro_Physics_MaxView_20mm': {       'bf_role': '',
                                              'brand': 'Astro-Physics',
                                              'cside_gender': '',
                                              'cside_thread': '',
                                              'field_of_view_deg': 50,
                                              'focal_length_mm': 20.0,
                                              'mass': 250,
                                              'name': 'MaxView 20mm',
                                              'optical_length': 0,
                                              'reversible': False,
                                              'tside_gender': 'Male',
                                              'tside_thread': '1.25"',
                                              'type': 'type_eyepiece'},
        'Astro_Physics_MaxView_25mm': {       'bf_role': '',
                                              'brand': 'Astro-Physics',
                                              'cside_gender': '',
                                              'cside_thread': '',
                                              'field_of_view_deg': 50,
                                              'focal_length_mm': 25.0,
                                              'mass': 280,
                                              'name': 'MaxView 25mm',
                                              'optical_length': 0,
                                              'reversible': False,
                                              'tside_gender': 'Male',
                                              'tside_thread': '1.25"',
                                              'type': 'type_eyepiece'}}

    @classmethod
    def Astro_Physics_MaxView_10mm(cls):
        return cls.from_database(cls._DATABASE['Astro_Physics_MaxView_10mm'])

    @classmethod
    def Astro_Physics_MaxView_15mm(cls):
        return cls.from_database(cls._DATABASE['Astro_Physics_MaxView_15mm'])

    @classmethod
    def Astro_Physics_MaxView_20mm(cls):
        return cls.from_database(cls._DATABASE['Astro_Physics_MaxView_20mm'])

    @classmethod
    def Astro_Physics_MaxView_25mm(cls):
        return cls.from_database(cls._DATABASE['Astro_Physics_MaxView_25mm'])