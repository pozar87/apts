from ..base import Eyepiece

class TecnoskyEyepiece(Eyepiece):
    _DATABASE = {'Tecnosky_SWA_5mm_70': {'brand': 'Tecnosky', 'name': 'SWA 5mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 140, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Tecnosky_SWA_7mm_70': {'brand': 'Tecnosky', 'name': 'SWA 7mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 150, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Tecnosky_SWA_10mm_70': {'brand': 'Tecnosky', 'name': 'SWA 10mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 165, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Tecnosky_SWA_14mm_70': {'brand': 'Tecnosky', 'name': 'SWA 14mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 185, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Tecnosky_SWA_20mm_70': {'brand': 'Tecnosky', 'name': 'SWA 20mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 210, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Tecnosky_SWA_25mm_70': {'brand': 'Tecnosky', 'name': 'SWA 25mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 240, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Tecnosky_SWA_30mm_70': {'brand': 'Tecnosky', 'name': 'SWA 30mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 400, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Tecnosky_Plossl_6mm': {'brand': 'Tecnosky', 'name': 'Plossl 6mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 95, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Tecnosky_Plossl_10mm': {'brand': 'Tecnosky', 'name': 'Plossl 10mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 105, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Tecnosky_Plossl_15mm': {'brand': 'Tecnosky', 'name': 'Plossl 15mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 120, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Tecnosky_Plossl_20mm': {'brand': 'Tecnosky', 'name': 'Plossl 20mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 135, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Tecnosky_Plossl_25mm': {'brand': 'Tecnosky', 'name': 'Plossl 25mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 155, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Tecnosky_Plossl_32mm': {'brand': 'Tecnosky', 'name': 'Plossl 32mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 180, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Tecnosky_SWA_5mm_70(cls):
        return cls.from_database(cls._DATABASE['Tecnosky_SWA_5mm_70'])

    @classmethod
    def Tecnosky_SWA_7mm_70(cls):
        return cls.from_database(cls._DATABASE['Tecnosky_SWA_7mm_70'])

    @classmethod
    def Tecnosky_SWA_10mm_70(cls):
        return cls.from_database(cls._DATABASE['Tecnosky_SWA_10mm_70'])

    @classmethod
    def Tecnosky_SWA_14mm_70(cls):
        return cls.from_database(cls._DATABASE['Tecnosky_SWA_14mm_70'])

    @classmethod
    def Tecnosky_SWA_20mm_70(cls):
        return cls.from_database(cls._DATABASE['Tecnosky_SWA_20mm_70'])

    @classmethod
    def Tecnosky_SWA_25mm_70(cls):
        return cls.from_database(cls._DATABASE['Tecnosky_SWA_25mm_70'])

    @classmethod
    def Tecnosky_SWA_30mm_70(cls):
        return cls.from_database(cls._DATABASE['Tecnosky_SWA_30mm_70'])

    @classmethod
    def Tecnosky_Plossl_6mm(cls):
        return cls.from_database(cls._DATABASE['Tecnosky_Plossl_6mm'])

    @classmethod
    def Tecnosky_Plossl_10mm(cls):
        return cls.from_database(cls._DATABASE['Tecnosky_Plossl_10mm'])

    @classmethod
    def Tecnosky_Plossl_15mm(cls):
        return cls.from_database(cls._DATABASE['Tecnosky_Plossl_15mm'])

    @classmethod
    def Tecnosky_Plossl_20mm(cls):
        return cls.from_database(cls._DATABASE['Tecnosky_Plossl_20mm'])

    @classmethod
    def Tecnosky_Plossl_25mm(cls):
        return cls.from_database(cls._DATABASE['Tecnosky_Plossl_25mm'])

    @classmethod
    def Tecnosky_Plossl_32mm(cls):
        return cls.from_database(cls._DATABASE['Tecnosky_Plossl_32mm'])