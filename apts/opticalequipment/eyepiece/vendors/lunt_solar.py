from ...abstract import OutputOpticalEqipment
from ....constants import GraphConstants, OpticalType
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ..base import Eyepiece

class Lunt_solarEyepiece(Eyepiece):
    _DATABASE = {'Lunt_Solar_EWA_6mm_82': {'brand': 'Lunt Solar', 'name': 'EWA 6mm 82°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 140, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Lunt_Solar_EWA_8mm_82': {'brand': 'Lunt Solar', 'name': 'EWA 8mm 82°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 150, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Lunt_Solar_EWA_10mm_82': {'brand': 'Lunt Solar', 'name': 'EWA 10mm 82°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 160, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Lunt_Solar_EWA_13mm_82': {'brand': 'Lunt Solar', 'name': 'EWA 13mm 82°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 175, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Lunt_Solar_EWA_16mm_82': {'brand': 'Lunt Solar', 'name': 'EWA 16mm 82°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 190, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Lunt_Solar_EWA_19mm_82': {'brand': 'Lunt Solar', 'name': 'EWA 19mm 82°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 210, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Lunt_Solar_EWA_22mm_82': {'brand': 'Lunt Solar', 'name': 'EWA 22mm 82°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 235, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Lunt_Solar_EWA_26mm_82': {'brand': 'Lunt Solar', 'name': 'EWA 26mm 82°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 270, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Lunt_Solar_EWA_32mm_82': {'brand': 'Lunt Solar', 'name': 'EWA 32mm 82°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 400, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Lunt_Solar_Solar_7_5mm': {'brand': 'Lunt Solar', 'name': 'Solar 7.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 170, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Lunt_Solar_Solar_10mm': {'brand': 'Lunt Solar', 'name': 'Solar 10mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 180, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Lunt_Solar_Solar_12mm': {'brand': 'Lunt Solar', 'name': 'Solar 12mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 190, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Lunt_Solar_Solar_16mm': {'brand': 'Lunt Solar', 'name': 'Solar 16mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 210, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Lunt_Solar_Solar_19mm': {'brand': 'Lunt Solar', 'name': 'Solar 19mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 230, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Lunt_Solar_Solar_25mm': {'brand': 'Lunt Solar', 'name': 'Solar 25mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 260, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Lunt_Solar_Solar_32mm': {'brand': 'Lunt Solar', 'name': 'Solar 32mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 350, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Lunt_Solar_EWA_6mm_82(cls):
        return cls.from_database(cls._DATABASE['Lunt_Solar_EWA_6mm_82'])

    @classmethod
    def Lunt_Solar_EWA_8mm_82(cls):
        return cls.from_database(cls._DATABASE['Lunt_Solar_EWA_8mm_82'])

    @classmethod
    def Lunt_Solar_EWA_10mm_82(cls):
        return cls.from_database(cls._DATABASE['Lunt_Solar_EWA_10mm_82'])

    @classmethod
    def Lunt_Solar_EWA_13mm_82(cls):
        return cls.from_database(cls._DATABASE['Lunt_Solar_EWA_13mm_82'])

    @classmethod
    def Lunt_Solar_EWA_16mm_82(cls):
        return cls.from_database(cls._DATABASE['Lunt_Solar_EWA_16mm_82'])

    @classmethod
    def Lunt_Solar_EWA_19mm_82(cls):
        return cls.from_database(cls._DATABASE['Lunt_Solar_EWA_19mm_82'])

    @classmethod
    def Lunt_Solar_EWA_22mm_82(cls):
        return cls.from_database(cls._DATABASE['Lunt_Solar_EWA_22mm_82'])

    @classmethod
    def Lunt_Solar_EWA_26mm_82(cls):
        return cls.from_database(cls._DATABASE['Lunt_Solar_EWA_26mm_82'])

    @classmethod
    def Lunt_Solar_EWA_32mm_82(cls):
        return cls.from_database(cls._DATABASE['Lunt_Solar_EWA_32mm_82'])

    @classmethod
    def Lunt_Solar_Solar_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Lunt_Solar_Solar_7_5mm'])

    @classmethod
    def Lunt_Solar_Solar_10mm(cls):
        return cls.from_database(cls._DATABASE['Lunt_Solar_Solar_10mm'])

    @classmethod
    def Lunt_Solar_Solar_12mm(cls):
        return cls.from_database(cls._DATABASE['Lunt_Solar_Solar_12mm'])

    @classmethod
    def Lunt_Solar_Solar_16mm(cls):
        return cls.from_database(cls._DATABASE['Lunt_Solar_Solar_16mm'])

    @classmethod
    def Lunt_Solar_Solar_19mm(cls):
        return cls.from_database(cls._DATABASE['Lunt_Solar_Solar_19mm'])

    @classmethod
    def Lunt_Solar_Solar_25mm(cls):
        return cls.from_database(cls._DATABASE['Lunt_Solar_Solar_25mm'])

    @classmethod
    def Lunt_Solar_Solar_32mm(cls):
        return cls.from_database(cls._DATABASE['Lunt_Solar_Solar_32mm'])