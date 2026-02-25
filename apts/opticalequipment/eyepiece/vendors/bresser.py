from ...abstract import OutputOpticalEqipment
from ....constants import GraphConstants, OpticalType
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ..base import Eyepiece

class BresserEyepiece(Eyepiece):
    _DATABASE = {'Bresser_LER_5mm_70': {'brand': 'Bresser', 'name': 'LER 5mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 100, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Bresser_LER_9mm_70': {'brand': 'Bresser', 'name': 'LER 9mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 110, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Bresser_LER_12mm_70': {'brand': 'Bresser', 'name': 'LER 12mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 120, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Bresser_LER_15mm_70': {'brand': 'Bresser', 'name': 'LER 15mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 130, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Bresser_LER_20mm_70': {'brand': 'Bresser', 'name': 'LER 20mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 150, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Bresser_LER_25mm_70': {'brand': 'Bresser', 'name': 'LER 25mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 170, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Bresser_LER_32mm_70': {'brand': 'Bresser', 'name': 'LER 32mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 200, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Bresser_Plossl_2_5mm': {'brand': 'Bresser', 'name': 'Plossl 2.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 100, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Bresser_Plossl_4mm': {'brand': 'Bresser', 'name': 'Plossl 4mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 105, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Bresser_Plossl_6mm': {'brand': 'Bresser', 'name': 'Plossl 6mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 110, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Bresser_Plossl_8mm': {'brand': 'Bresser', 'name': 'Plossl 8mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 115, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Bresser_Plossl_12_5mm': {'brand': 'Bresser', 'name': 'Plossl 12.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 125, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Bresser_Plossl_20mm': {'brand': 'Bresser', 'name': 'Plossl 20mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 140, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Bresser_Plossl_25mm': {'brand': 'Bresser', 'name': 'Plossl 25mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 155, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Bresser_Plossl_32mm': {'brand': 'Bresser', 'name': 'Plossl 32mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 175, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Bresser_Plossl_6_5mm': {'brand': 'Bresser', 'name': 'Plossl 6.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 80, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Bresser_Plossl_10mm': {'brand': 'Bresser', 'name': 'Plossl 10mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 90, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Bresser_Plossl_15mm': {'brand': 'Bresser', 'name': 'Plossl 15mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 105, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Bresser_Plossl_40mm': {'brand': 'Bresser', 'name': 'Plossl 40mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 180, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Bresser_Wide_Angle_5mm_70': {'brand': 'Bresser', 'name': 'Wide Angle 5mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 110, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Bresser_Wide_Angle_8mm_70': {'brand': 'Bresser', 'name': 'Wide Angle 8mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 120, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Bresser_Wide_Angle_12mm_70': {'brand': 'Bresser', 'name': 'Wide Angle 12mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 135, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Bresser_Wide_Angle_15mm_70': {'brand': 'Bresser', 'name': 'Wide Angle 15mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 150, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Bresser_Wide_Angle_20mm_70': {'brand': 'Bresser', 'name': 'Wide Angle 20mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 175, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Bresser_Wide_Angle_25mm_70': {'brand': 'Bresser', 'name': 'Wide Angle 25mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 200, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Bresser_Wide_Field_4mm': {'brand': 'Bresser', 'name': 'Wide Field 4mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 100, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Bresser_Wide_Field_6mm': {'brand': 'Bresser', 'name': 'Wide Field 6mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 108, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Bresser_Wide_Field_8mm': {'brand': 'Bresser', 'name': 'Wide Field 8mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 115, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Bresser_Wide_Field_11mm': {'brand': 'Bresser', 'name': 'Wide Field 11mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 128, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Bresser_Wide_Field_14mm': {'brand': 'Bresser', 'name': 'Wide Field 14mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 140, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Bresser_Wide_Field_18mm': {'brand': 'Bresser', 'name': 'Wide Field 18mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 160, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Bresser_Wide_Field_23mm': {'brand': 'Bresser', 'name': 'Wide Field 23mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 200, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Bresser_Wide_Field_28mm': {'brand': 'Bresser', 'name': 'Wide Field 28mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 280, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Bresser_LER_5mm_70(cls):
        return cls.from_database(cls._DATABASE['Bresser_LER_5mm_70'])

    @classmethod
    def Bresser_LER_9mm_70(cls):
        return cls.from_database(cls._DATABASE['Bresser_LER_9mm_70'])

    @classmethod
    def Bresser_LER_12mm_70(cls):
        return cls.from_database(cls._DATABASE['Bresser_LER_12mm_70'])

    @classmethod
    def Bresser_LER_15mm_70(cls):
        return cls.from_database(cls._DATABASE['Bresser_LER_15mm_70'])

    @classmethod
    def Bresser_LER_20mm_70(cls):
        return cls.from_database(cls._DATABASE['Bresser_LER_20mm_70'])

    @classmethod
    def Bresser_LER_25mm_70(cls):
        return cls.from_database(cls._DATABASE['Bresser_LER_25mm_70'])

    @classmethod
    def Bresser_LER_32mm_70(cls):
        return cls.from_database(cls._DATABASE['Bresser_LER_32mm_70'])

    @classmethod
    def Bresser_Plossl_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_Plossl_2_5mm'])

    @classmethod
    def Bresser_Plossl_4mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_Plossl_4mm'])

    @classmethod
    def Bresser_Plossl_6mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_Plossl_6mm'])

    @classmethod
    def Bresser_Plossl_8mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_Plossl_8mm'])

    @classmethod
    def Bresser_Plossl_12_5mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_Plossl_12_5mm'])

    @classmethod
    def Bresser_Plossl_20mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_Plossl_20mm'])

    @classmethod
    def Bresser_Plossl_25mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_Plossl_25mm'])

    @classmethod
    def Bresser_Plossl_32mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_Plossl_32mm'])

    @classmethod
    def Bresser_Plossl_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_Plossl_6_5mm'])

    @classmethod
    def Bresser_Plossl_10mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_Plossl_10mm'])

    @classmethod
    def Bresser_Plossl_15mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_Plossl_15mm'])

    @classmethod
    def Bresser_Plossl_40mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_Plossl_40mm'])

    @classmethod
    def Bresser_Wide_Angle_5mm_70(cls):
        return cls.from_database(cls._DATABASE['Bresser_Wide_Angle_5mm_70'])

    @classmethod
    def Bresser_Wide_Angle_8mm_70(cls):
        return cls.from_database(cls._DATABASE['Bresser_Wide_Angle_8mm_70'])

    @classmethod
    def Bresser_Wide_Angle_12mm_70(cls):
        return cls.from_database(cls._DATABASE['Bresser_Wide_Angle_12mm_70'])

    @classmethod
    def Bresser_Wide_Angle_15mm_70(cls):
        return cls.from_database(cls._DATABASE['Bresser_Wide_Angle_15mm_70'])

    @classmethod
    def Bresser_Wide_Angle_20mm_70(cls):
        return cls.from_database(cls._DATABASE['Bresser_Wide_Angle_20mm_70'])

    @classmethod
    def Bresser_Wide_Angle_25mm_70(cls):
        return cls.from_database(cls._DATABASE['Bresser_Wide_Angle_25mm_70'])

    @classmethod
    def Bresser_Wide_Field_4mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_Wide_Field_4mm'])

    @classmethod
    def Bresser_Wide_Field_6mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_Wide_Field_6mm'])

    @classmethod
    def Bresser_Wide_Field_8mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_Wide_Field_8mm'])

    @classmethod
    def Bresser_Wide_Field_11mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_Wide_Field_11mm'])

    @classmethod
    def Bresser_Wide_Field_14mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_Wide_Field_14mm'])

    @classmethod
    def Bresser_Wide_Field_18mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_Wide_Field_18mm'])

    @classmethod
    def Bresser_Wide_Field_23mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_Wide_Field_23mm'])

    @classmethod
    def Bresser_Wide_Field_28mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_Wide_Field_28mm'])