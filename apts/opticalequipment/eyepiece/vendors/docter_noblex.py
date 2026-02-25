from ..base import Eyepiece

class Docter_noblexEyepiece(Eyepiece):
    _DATABASE = {'Docter_Noblex_UWF_10mm': {'brand': 'Docter/Noblex', 'name': 'UWF 10mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 200, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Docter_Noblex_UWF_12_5mm': {'brand': 'Docter/Noblex', 'name': 'UWF 12.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 220, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Docter_Noblex_UWF_17mm': {'brand': 'Docter/Noblex', 'name': 'UWF 17mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 270, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Docter_Noblex_UWF_10mm(cls):
        return cls.from_database(cls._DATABASE['Docter_Noblex_UWF_10mm'])

    @classmethod
    def Docter_Noblex_UWF_12_5mm(cls):
        return cls.from_database(cls._DATABASE['Docter_Noblex_UWF_12_5mm'])

    @classmethod
    def Docter_Noblex_UWF_17mm(cls):
        return cls.from_database(cls._DATABASE['Docter_Noblex_UWF_17mm'])