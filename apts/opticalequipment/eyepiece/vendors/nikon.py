from ..base import Eyepiece

class NikonEyepiece(Eyepiece):
    _DATABASE = {       'Nikon_Fieldscope_Zoom_13_40mm': {       'bf_role': '',
                                                 'brand': 'Nikon',
                                                 'cside_gender': '',
                                                 'cside_thread': '',
                                                 'field_of_view_deg': 50,
                                                 'focal_length_mm': 40.0,
                                                 'mass': 350,
                                                 'name': 'Fieldscope Zoom 13-40mm',
                                                 'optical_length': 0,
                                                 'reversible': False,
                                                 'tside_gender': 'Male',
                                                 'tside_thread': '1.25"',
                                                 'type': 'type_eyepiece'},
        'Nikon_NAV_HW_12_5mm': {       'bf_role': '',
                                       'brand': 'Nikon',
                                       'cside_gender': '',
                                       'cside_thread': '',
                                       'field_of_view_deg': 102,
                                       'focal_length_mm': 12.5,
                                       'mass': 650,
                                       'name': 'NAV-HW 12.5mm',
                                       'optical_length': 0,
                                       'reversible': False,
                                       'tside_gender': 'Male',
                                       'tside_thread': '2"',
                                       'type': 'type_eyepiece'},
        'Nikon_NAV_HW_14mm': {       'bf_role': '',
                                     'brand': 'Nikon',
                                     'cside_gender': '',
                                     'cside_thread': '',
                                     'field_of_view_deg': 102,
                                     'focal_length_mm': 14.0,
                                     'mass': 630,
                                     'name': 'NAV-HW 14mm',
                                     'optical_length': 0,
                                     'reversible': False,
                                     'tside_gender': 'Male',
                                     'tside_thread': '2"',
                                     'type': 'type_eyepiece'},
        'Nikon_NAV_HW_7mm': {       'bf_role': '',
                                    'brand': 'Nikon',
                                    'cside_gender': '',
                                    'cside_thread': '',
                                    'field_of_view_deg': 102,
                                    'focal_length_mm': 7.0,
                                    'mass': 550,
                                    'name': 'NAV-HW 7mm',
                                    'optical_length': 0,
                                    'reversible': False,
                                    'tside_gender': 'Male',
                                    'tside_thread': '2"',
                                    'type': 'type_eyepiece'},
        'Nikon_NAV_SW_10mm': {       'bf_role': '',
                                     'brand': 'Nikon',
                                     'cside_gender': '',
                                     'cside_thread': '',
                                     'field_of_view_deg': 72,
                                     'focal_length_mm': 10.0,
                                     'mass': 600,
                                     'name': 'NAV-SW 10mm',
                                     'optical_length': 0,
                                     'reversible': False,
                                     'tside_gender': 'Male',
                                     'tside_thread': '1.25"',
                                     'type': 'type_eyepiece'},
        'Nikon_NAV_SW_12_5mm': {       'bf_role': '',
                                       'brand': 'Nikon',
                                       'cside_gender': '',
                                       'cside_thread': '',
                                       'field_of_view_deg': 72,
                                       'focal_length_mm': 12.5,
                                       'mass': 620,
                                       'name': 'NAV-SW 12.5mm',
                                       'optical_length': 0,
                                       'reversible': False,
                                       'tside_gender': 'Male',
                                       'tside_thread': '1.25"',
                                       'type': 'type_eyepiece'},
        'Nikon_NAV_SW_17mm': {       'bf_role': '',
                                     'brand': 'Nikon',
                                     'cside_gender': '',
                                     'cside_thread': '',
                                     'field_of_view_deg': 72,
                                     'focal_length_mm': 17.0,
                                     'mass': 640,
                                     'name': 'NAV-SW 17mm',
                                     'optical_length': 0,
                                     'reversible': False,
                                     'tside_gender': 'Male',
                                     'tside_thread': '1.25"',
                                     'type': 'type_eyepiece'}}

    @classmethod
    def Nikon_NAV_SW_10mm(cls):
        return cls.from_database(cls._DATABASE['Nikon_NAV_SW_10mm'])

    @classmethod
    def Nikon_NAV_SW_12_5mm(cls):
        return cls.from_database(cls._DATABASE['Nikon_NAV_SW_12_5mm'])

    @classmethod
    def Nikon_NAV_SW_17mm(cls):
        return cls.from_database(cls._DATABASE['Nikon_NAV_SW_17mm'])

    @classmethod
    def Nikon_NAV_HW_12_5mm(cls):
        return cls.from_database(cls._DATABASE['Nikon_NAV_HW_12_5mm'])

    @classmethod
    def Nikon_Fieldscope_Zoom_13_40mm(cls):
        return cls.from_database(cls._DATABASE['Nikon_Fieldscope_Zoom_13_40mm'])

    @classmethod
    def Nikon_NAV_HW_7mm(cls):
        return cls.from_database(cls._DATABASE['Nikon_NAV_HW_7mm'])

    @classmethod
    def Nikon_NAV_HW_14mm(cls):
        return cls.from_database(cls._DATABASE['Nikon_NAV_HW_14mm'])