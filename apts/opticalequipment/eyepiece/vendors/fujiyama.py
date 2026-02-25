from ..base import Eyepiece

class FujiyamaEyepiece(Eyepiece):
    _DATABASE = {'Fujiyama_HD_Ortho_4mm': {'brand': 'Fujiyama', 'name': 'HD Ortho 4mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 110, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Fujiyama_HD_Ortho_5mm': {'brand': 'Fujiyama', 'name': 'HD Ortho 5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 115, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Fujiyama_HD_Ortho_6mm': {'brand': 'Fujiyama', 'name': 'HD Ortho 6mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 120, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Fujiyama_HD_Ortho_7mm': {'brand': 'Fujiyama', 'name': 'HD Ortho 7mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 125, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Fujiyama_HD_Ortho_9mm': {'brand': 'Fujiyama', 'name': 'HD Ortho 9mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 130, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Fujiyama_HD_Ortho_12_5mm': {'brand': 'Fujiyama', 'name': 'HD Ortho 12.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 140, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Fujiyama_HD_Ortho_18mm': {'brand': 'Fujiyama', 'name': 'HD Ortho 18mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 160, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Fujiyama_HD_Ortho_25mm': {'brand': 'Fujiyama', 'name': 'HD Ortho 25mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 180, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}}

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