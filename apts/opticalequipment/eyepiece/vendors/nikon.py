from ..base import Eyepiece

class NikonEyepiece(Eyepiece):
    _DATABASE = {'Nikon_NAV_SW_10mm': {'brand': 'Nikon', 'name': 'NAV-SW 10mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 600, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Nikon_NAV_SW_12_5mm': {'brand': 'Nikon', 'name': 'NAV-SW 12.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 620, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Nikon_NAV_SW_17mm': {'brand': 'Nikon', 'name': 'NAV-SW 17mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 640, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Nikon_NAV_HW_12_5mm': {'brand': 'Nikon', 'name': 'NAV-HW 12.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 650, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Nikon_Fieldscope_Zoom_13_40mm': {'brand': 'Nikon', 'name': 'Fieldscope Zoom 13-40mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 350, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Nikon_NAV_HW_7mm': {'brand': 'Nikon', 'name': 'NAV-HW 7mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 550, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Nikon_NAV_HW_14mm': {'brand': 'Nikon', 'name': 'NAV-HW 14mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 630, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}}

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