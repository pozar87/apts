from ..base import Eyepiece

class LeicaEyepiece(Eyepiece):
    _DATABASE = {'Leica_ASPH_10mm': {'brand': 'Leica', 'name': 'ASPH 10mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 350, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Leica_ASPH_17_5mm': {'brand': 'Leica', 'name': 'ASPH 17.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 380, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Leica_ASPH_25mm': {'brand': 'Leica', 'name': 'ASPH 25mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 410, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Leica_ASPH_30mm': {'brand': 'Leica', 'name': 'ASPH 30mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 450, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Leica_ASPH_6_5mm_v2': {'brand': 'Leica', 'name': 'ASPH 6.5mm (v2)', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 320, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Leica_ASPH_12_5mm_v2': {'brand': 'Leica', 'name': 'ASPH 12.5mm (v2)', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 370, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Leica_ASPH_20mm_v2': {'brand': 'Leica', 'name': 'ASPH 20mm (v2)', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 400, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Leica_ASPH_10mm(cls):
        return cls.from_database(cls._DATABASE['Leica_ASPH_10mm'])

    @classmethod
    def Leica_ASPH_17_5mm(cls):
        return cls.from_database(cls._DATABASE['Leica_ASPH_17_5mm'])

    @classmethod
    def Leica_ASPH_25mm(cls):
        return cls.from_database(cls._DATABASE['Leica_ASPH_25mm'])

    @classmethod
    def Leica_ASPH_30mm(cls):
        return cls.from_database(cls._DATABASE['Leica_ASPH_30mm'])

    @classmethod
    def Leica_ASPH_6_5mm_v2(cls):
        return cls.from_database(cls._DATABASE['Leica_ASPH_6_5mm_v2'])

    @classmethod
    def Leica_ASPH_12_5mm_v2(cls):
        return cls.from_database(cls._DATABASE['Leica_ASPH_12_5mm_v2'])

    @classmethod
    def Leica_ASPH_20mm_v2(cls):
        return cls.from_database(cls._DATABASE['Leica_ASPH_20mm_v2'])