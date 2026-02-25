from ..base import Eyepiece

class Kokusai_kohkiEyepiece(Eyepiece):
    _DATABASE = {'Kokusai_Kohki_Ortho_5mm': {'brand': 'Kokusai Kohki', 'name': 'Ortho 5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 140, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Kokusai_Kohki_Ortho_8mm': {'brand': 'Kokusai Kohki', 'name': 'Ortho 8mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 155, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Kokusai_Kohki_Ortho_12mm': {'brand': 'Kokusai Kohki', 'name': 'Ortho 12mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 170, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Kokusai_Kohki_Ortho_18mm': {'brand': 'Kokusai Kohki', 'name': 'Ortho 18mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 200, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Kokusai_Kohki_Ortho_25mm': {'brand': 'Kokusai Kohki', 'name': 'Ortho 25mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 240, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}}

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