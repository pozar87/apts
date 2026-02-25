from ..base import Eyepiece

class PentaxEyepiece(Eyepiece):
    _DATABASE = {'Pentax_XW_3_5mm': {'brand': 'Pentax', 'name': 'XW 3.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 260, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Pentax_XW_5mm': {'brand': 'Pentax', 'name': 'XW 5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 265, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Pentax_XW_7mm': {'brand': 'Pentax', 'name': 'XW 7mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 270, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Pentax_XW_10mm': {'brand': 'Pentax', 'name': 'XW 10mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 280, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Pentax_XW_14mm': {'brand': 'Pentax', 'name': 'XW 14mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 290, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Pentax_XW_20mm': {'brand': 'Pentax', 'name': 'XW 20mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 310, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Pentax_XW_30mm': {'brand': 'Pentax', 'name': 'XW 30mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 530, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Pentax_XW_40mm': {'brand': 'Pentax', 'name': 'XW 40mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 680, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Pentax_XF_6_5mm': {'brand': 'Pentax', 'name': 'XF 6.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 230, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Pentax_XF_8_5mm': {'brand': 'Pentax', 'name': 'XF 8.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 240, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Pentax_XF_12mm': {'brand': 'Pentax', 'name': 'XF 12mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 260, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Pentax_XF_6_5_19_5mm_Zoom': {'brand': 'Pentax', 'name': 'XF 6.5-19.5mm Zoom', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 390, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Pentax_XL_2_5mm': {'brand': 'Pentax', 'name': 'XL 2.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 200, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Pentax_XL_5_2mm': {'brand': 'Pentax', 'name': 'XL 5.2mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 210, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Pentax_XL_7mm': {'brand': 'Pentax', 'name': 'XL 7mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 220, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Pentax_XL_10_5mm': {'brand': 'Pentax', 'name': 'XL 10.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 240, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Pentax_XL_14mm': {'brand': 'Pentax', 'name': 'XL 14mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 260, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Pentax_XL_21mm': {'brand': 'Pentax', 'name': 'XL 21mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 300, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Pentax_XL_28mm': {'brand': 'Pentax', 'name': 'XL 28mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 420, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Pentax_XL_40mm': {'brand': 'Pentax', 'name': 'XL 40mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 550, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Pentax_XO_2_5mm': {'brand': 'Pentax', 'name': 'XO 2.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 250, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Pentax_XO_5mm': {'brand': 'Pentax', 'name': 'XO 5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 260, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Pentax_XO_10mm': {'brand': 'Pentax', 'name': 'XO 10mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 280, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Pentax_XW_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Pentax_XW_3_5mm'])

    @classmethod
    def Pentax_XW_5mm(cls):
        return cls.from_database(cls._DATABASE['Pentax_XW_5mm'])

    @classmethod
    def Pentax_XW_7mm(cls):
        return cls.from_database(cls._DATABASE['Pentax_XW_7mm'])

    @classmethod
    def Pentax_XW_10mm(cls):
        return cls.from_database(cls._DATABASE['Pentax_XW_10mm'])

    @classmethod
    def Pentax_XW_14mm(cls):
        return cls.from_database(cls._DATABASE['Pentax_XW_14mm'])

    @classmethod
    def Pentax_XW_20mm(cls):
        return cls.from_database(cls._DATABASE['Pentax_XW_20mm'])

    @classmethod
    def Pentax_XW_30mm(cls):
        return cls.from_database(cls._DATABASE['Pentax_XW_30mm'])

    @classmethod
    def Pentax_XW_40mm(cls):
        return cls.from_database(cls._DATABASE['Pentax_XW_40mm'])

    @classmethod
    def Pentax_XF_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Pentax_XF_6_5mm'])

    @classmethod
    def Pentax_XF_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Pentax_XF_8_5mm'])

    @classmethod
    def Pentax_XF_12mm(cls):
        return cls.from_database(cls._DATABASE['Pentax_XF_12mm'])

    @classmethod
    def Pentax_XF_6_5_19_5mm_Zoom(cls):
        return cls.from_database(cls._DATABASE['Pentax_XF_6_5_19_5mm_Zoom'])

    @classmethod
    def Pentax_XL_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Pentax_XL_2_5mm'])

    @classmethod
    def Pentax_XL_5_2mm(cls):
        return cls.from_database(cls._DATABASE['Pentax_XL_5_2mm'])

    @classmethod
    def Pentax_XL_7mm(cls):
        return cls.from_database(cls._DATABASE['Pentax_XL_7mm'])

    @classmethod
    def Pentax_XL_10_5mm(cls):
        return cls.from_database(cls._DATABASE['Pentax_XL_10_5mm'])

    @classmethod
    def Pentax_XL_14mm(cls):
        return cls.from_database(cls._DATABASE['Pentax_XL_14mm'])

    @classmethod
    def Pentax_XL_21mm(cls):
        return cls.from_database(cls._DATABASE['Pentax_XL_21mm'])

    @classmethod
    def Pentax_XL_28mm(cls):
        return cls.from_database(cls._DATABASE['Pentax_XL_28mm'])

    @classmethod
    def Pentax_XL_40mm(cls):
        return cls.from_database(cls._DATABASE['Pentax_XL_40mm'])

    @classmethod
    def Pentax_XO_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Pentax_XO_2_5mm'])

    @classmethod
    def Pentax_XO_5mm(cls):
        return cls.from_database(cls._DATABASE['Pentax_XO_5mm'])

    @classmethod
    def Pentax_XO_10mm(cls):
        return cls.from_database(cls._DATABASE['Pentax_XO_10mm'])