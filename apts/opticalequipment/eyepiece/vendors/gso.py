from ..base import Eyepiece

class GsoEyepiece(Eyepiece):
    _DATABASE = {'GSO_Plossl_6mm': {'brand': 'GSO', 'name': 'Plossl 6mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 90, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'GSO_Plossl_8mm': {'brand': 'GSO', 'name': 'Plossl 8mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 95, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'GSO_Plossl_10mm': {'brand': 'GSO', 'name': 'Plossl 10mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 100, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'GSO_Plossl_12_5mm': {'brand': 'GSO', 'name': 'Plossl 12.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 110, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'GSO_Plossl_15mm': {'brand': 'GSO', 'name': 'Plossl 15mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 120, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'GSO_Plossl_20mm': {'brand': 'GSO', 'name': 'Plossl 20mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 130, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'GSO_Plossl_25mm': {'brand': 'GSO', 'name': 'Plossl 25mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 145, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'GSO_Plossl_32mm': {'brand': 'GSO', 'name': 'Plossl 32mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 160, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'GSO_Plossl_40mm': {'brand': 'GSO', 'name': 'Plossl 40mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 200, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'GSO_SuperView_7mm': {'brand': 'GSO', 'name': 'SuperView 7mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 200, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'GSO_SuperView_9mm': {'brand': 'GSO', 'name': 'SuperView 9mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 210, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'GSO_SuperView_12mm': {'brand': 'GSO', 'name': 'SuperView 12mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 225, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'GSO_SuperView_15mm': {'brand': 'GSO', 'name': 'SuperView 15mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 240, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'GSO_SuperView_20mm': {'brand': 'GSO', 'name': 'SuperView 20mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 260, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'GSO_SuperView_30mm': {'brand': 'GSO', 'name': 'SuperView 30mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 500, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'GSO_Wide_Field_4mm_70': {'brand': 'GSO', 'name': 'Wide Field 4mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 85, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'GSO_Wide_Field_6mm_70': {'brand': 'GSO', 'name': 'Wide Field 6mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 90, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'GSO_Wide_Field_10mm_70': {'brand': 'GSO', 'name': 'Wide Field 10mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 100, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'GSO_Wide_Field_15mm_70': {'brand': 'GSO', 'name': 'Wide Field 15mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 110, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'GSO_Wide_Field_20mm_70': {'brand': 'GSO', 'name': 'Wide Field 20mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 120, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'GSO_Wide_Field_25mm_70': {'brand': 'GSO', 'name': 'Wide Field 25mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 135, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'GSO_Wide_Field_8mm_70': {'brand': 'GSO', 'name': 'Wide Field 8mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 120, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'GSO_Wide_Field_30mm_70': {'brand': 'GSO', 'name': 'Wide Field 30mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 220, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'GSO_Wide_Field_42mm_70': {'brand': 'GSO', 'name': 'Wide Field 42mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 350, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'GSO_SuperPlossl_4mm': {'brand': 'GSO', 'name': 'SuperPlossl 4mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 82, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'GSO_SuperPlossl_5mm': {'brand': 'GSO', 'name': 'SuperPlossl 5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 85, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'GSO_SuperPlossl_7_5mm': {'brand': 'GSO', 'name': 'SuperPlossl 7.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 92, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'GSO_SuperPlossl_9_7mm': {'brand': 'GSO', 'name': 'SuperPlossl 9.7mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 98, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'GSO_SuperPlossl_12_5mm': {'brand': 'GSO', 'name': 'SuperPlossl 12.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 108, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'GSO_SuperPlossl_15mm': {'brand': 'GSO', 'name': 'SuperPlossl 15mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 118, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'GSO_SuperPlossl_17mm': {'brand': 'GSO', 'name': 'SuperPlossl 17mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 128, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'GSO_SuperPlossl_20mm': {'brand': 'GSO', 'name': 'SuperPlossl 20mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 138, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'GSO_SuperPlossl_25mm': {'brand': 'GSO', 'name': 'SuperPlossl 25mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 155, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'GSO_SuperPlossl_30mm': {'brand': 'GSO', 'name': 'SuperPlossl 30mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 180, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'GSO_SuperPlossl_40mm': {'brand': 'GSO', 'name': 'SuperPlossl 40mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 215, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def GSO_Plossl_6mm(cls):
        return cls.from_database(cls._DATABASE['GSO_Plossl_6mm'])

    @classmethod
    def GSO_Plossl_8mm(cls):
        return cls.from_database(cls._DATABASE['GSO_Plossl_8mm'])

    @classmethod
    def GSO_Plossl_10mm(cls):
        return cls.from_database(cls._DATABASE['GSO_Plossl_10mm'])

    @classmethod
    def GSO_Plossl_12_5mm(cls):
        return cls.from_database(cls._DATABASE['GSO_Plossl_12_5mm'])

    @classmethod
    def GSO_Plossl_15mm(cls):
        return cls.from_database(cls._DATABASE['GSO_Plossl_15mm'])

    @classmethod
    def GSO_Plossl_20mm(cls):
        return cls.from_database(cls._DATABASE['GSO_Plossl_20mm'])

    @classmethod
    def GSO_Plossl_25mm(cls):
        return cls.from_database(cls._DATABASE['GSO_Plossl_25mm'])

    @classmethod
    def GSO_Plossl_32mm(cls):
        return cls.from_database(cls._DATABASE['GSO_Plossl_32mm'])

    @classmethod
    def GSO_Plossl_40mm(cls):
        return cls.from_database(cls._DATABASE['GSO_Plossl_40mm'])

    @classmethod
    def GSO_SuperView_7mm(cls):
        return cls.from_database(cls._DATABASE['GSO_SuperView_7mm'])

    @classmethod
    def GSO_SuperView_9mm(cls):
        return cls.from_database(cls._DATABASE['GSO_SuperView_9mm'])

    @classmethod
    def GSO_SuperView_12mm(cls):
        return cls.from_database(cls._DATABASE['GSO_SuperView_12mm'])

    @classmethod
    def GSO_SuperView_15mm(cls):
        return cls.from_database(cls._DATABASE['GSO_SuperView_15mm'])

    @classmethod
    def GSO_SuperView_20mm(cls):
        return cls.from_database(cls._DATABASE['GSO_SuperView_20mm'])

    @classmethod
    def GSO_SuperView_30mm(cls):
        return cls.from_database(cls._DATABASE['GSO_SuperView_30mm'])

    @classmethod
    def GSO_Wide_Field_4mm_70(cls):
        return cls.from_database(cls._DATABASE['GSO_Wide_Field_4mm_70'])

    @classmethod
    def GSO_Wide_Field_6mm_70(cls):
        return cls.from_database(cls._DATABASE['GSO_Wide_Field_6mm_70'])

    @classmethod
    def GSO_Wide_Field_10mm_70(cls):
        return cls.from_database(cls._DATABASE['GSO_Wide_Field_10mm_70'])

    @classmethod
    def GSO_Wide_Field_15mm_70(cls):
        return cls.from_database(cls._DATABASE['GSO_Wide_Field_15mm_70'])

    @classmethod
    def GSO_Wide_Field_20mm_70(cls):
        return cls.from_database(cls._DATABASE['GSO_Wide_Field_20mm_70'])

    @classmethod
    def GSO_Wide_Field_25mm_70(cls):
        return cls.from_database(cls._DATABASE['GSO_Wide_Field_25mm_70'])

    @classmethod
    def GSO_Wide_Field_8mm_70(cls):
        return cls.from_database(cls._DATABASE['GSO_Wide_Field_8mm_70'])

    @classmethod
    def GSO_Wide_Field_30mm_70(cls):
        return cls.from_database(cls._DATABASE['GSO_Wide_Field_30mm_70'])

    @classmethod
    def GSO_Wide_Field_42mm_70(cls):
        return cls.from_database(cls._DATABASE['GSO_Wide_Field_42mm_70'])

    @classmethod
    def GSO_SuperPlossl_4mm(cls):
        return cls.from_database(cls._DATABASE['GSO_SuperPlossl_4mm'])

    @classmethod
    def GSO_SuperPlossl_5mm(cls):
        return cls.from_database(cls._DATABASE['GSO_SuperPlossl_5mm'])

    @classmethod
    def GSO_SuperPlossl_7_5mm(cls):
        return cls.from_database(cls._DATABASE['GSO_SuperPlossl_7_5mm'])

    @classmethod
    def GSO_SuperPlossl_9_7mm(cls):
        return cls.from_database(cls._DATABASE['GSO_SuperPlossl_9_7mm'])

    @classmethod
    def GSO_SuperPlossl_12_5mm(cls):
        return cls.from_database(cls._DATABASE['GSO_SuperPlossl_12_5mm'])

    @classmethod
    def GSO_SuperPlossl_15mm(cls):
        return cls.from_database(cls._DATABASE['GSO_SuperPlossl_15mm'])

    @classmethod
    def GSO_SuperPlossl_17mm(cls):
        return cls.from_database(cls._DATABASE['GSO_SuperPlossl_17mm'])

    @classmethod
    def GSO_SuperPlossl_20mm(cls):
        return cls.from_database(cls._DATABASE['GSO_SuperPlossl_20mm'])

    @classmethod
    def GSO_SuperPlossl_25mm(cls):
        return cls.from_database(cls._DATABASE['GSO_SuperPlossl_25mm'])

    @classmethod
    def GSO_SuperPlossl_30mm(cls):
        return cls.from_database(cls._DATABASE['GSO_SuperPlossl_30mm'])

    @classmethod
    def GSO_SuperPlossl_40mm(cls):
        return cls.from_database(cls._DATABASE['GSO_SuperPlossl_40mm'])