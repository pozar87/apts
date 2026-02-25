from ...abstract import OutputOpticalEqipment
from ....constants import GraphConstants, OpticalType
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ..base import Eyepiece

class StellarvueEyepiece(Eyepiece):
    _DATABASE = {'Stellarvue_Optimus_3_5mm_82': {'brand': 'Stellarvue', 'name': 'Optimus 3.5mm 82°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 200, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Stellarvue_Optimus_5mm_82': {'brand': 'Stellarvue', 'name': 'Optimus 5mm 82°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 210, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Stellarvue_Optimus_7mm_82': {'brand': 'Stellarvue', 'name': 'Optimus 7mm 82°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 220, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Stellarvue_Optimus_9mm_82': {'brand': 'Stellarvue', 'name': 'Optimus 9mm 82°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 230, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Stellarvue_Optimus_13mm_82': {'brand': 'Stellarvue', 'name': 'Optimus 13mm 82°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 250, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Stellarvue_Optimus_20mm_82': {'brand': 'Stellarvue', 'name': 'Optimus 20mm 82°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 280, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Stellarvue_Optimus_3_5mm': {'brand': 'Stellarvue', 'name': 'Optimus 3.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 190, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Stellarvue_Optimus_5mm': {'brand': 'Stellarvue', 'name': 'Optimus 5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 200, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Stellarvue_Optimus_7mm': {'brand': 'Stellarvue', 'name': 'Optimus 7mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 210, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Stellarvue_Optimus_10mm': {'brand': 'Stellarvue', 'name': 'Optimus 10mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 225, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Stellarvue_Optimus_14mm': {'brand': 'Stellarvue', 'name': 'Optimus 14mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 250, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Stellarvue_Optimus_19mm': {'brand': 'Stellarvue', 'name': 'Optimus 19mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 280, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Stellarvue_Optimus_28mm': {'brand': 'Stellarvue', 'name': 'Optimus 28mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 450, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Stellarvue_Optimus_Wide_5mm': {'brand': 'Stellarvue', 'name': 'Optimus Wide 5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 220, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Stellarvue_Optimus_Wide_8mm': {'brand': 'Stellarvue', 'name': 'Optimus Wide 8mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 240, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Stellarvue_Optimus_Wide_12mm': {'brand': 'Stellarvue', 'name': 'Optimus Wide 12mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 260, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Stellarvue_Optimus_Wide_16mm': {'brand': 'Stellarvue', 'name': 'Optimus Wide 16mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 290, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Stellarvue_Optimus_Wide_22mm': {'brand': 'Stellarvue', 'name': 'Optimus Wide 22mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 350, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Stellarvue_Optimus_Wide_32mm': {'brand': 'Stellarvue', 'name': 'Optimus Wide 32mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 500, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Stellarvue_Optimus_3_5mm_82(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_Optimus_3_5mm_82'])

    @classmethod
    def Stellarvue_Optimus_5mm_82(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_Optimus_5mm_82'])

    @classmethod
    def Stellarvue_Optimus_7mm_82(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_Optimus_7mm_82'])

    @classmethod
    def Stellarvue_Optimus_9mm_82(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_Optimus_9mm_82'])

    @classmethod
    def Stellarvue_Optimus_13mm_82(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_Optimus_13mm_82'])

    @classmethod
    def Stellarvue_Optimus_20mm_82(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_Optimus_20mm_82'])

    @classmethod
    def Stellarvue_Optimus_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_Optimus_3_5mm'])

    @classmethod
    def Stellarvue_Optimus_5mm(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_Optimus_5mm'])

    @classmethod
    def Stellarvue_Optimus_7mm(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_Optimus_7mm'])

    @classmethod
    def Stellarvue_Optimus_10mm(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_Optimus_10mm'])

    @classmethod
    def Stellarvue_Optimus_14mm(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_Optimus_14mm'])

    @classmethod
    def Stellarvue_Optimus_19mm(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_Optimus_19mm'])

    @classmethod
    def Stellarvue_Optimus_28mm(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_Optimus_28mm'])

    @classmethod
    def Stellarvue_Optimus_Wide_5mm(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_Optimus_Wide_5mm'])

    @classmethod
    def Stellarvue_Optimus_Wide_8mm(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_Optimus_Wide_8mm'])

    @classmethod
    def Stellarvue_Optimus_Wide_12mm(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_Optimus_Wide_12mm'])

    @classmethod
    def Stellarvue_Optimus_Wide_16mm(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_Optimus_Wide_16mm'])

    @classmethod
    def Stellarvue_Optimus_Wide_22mm(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_Optimus_Wide_22mm'])

    @classmethod
    def Stellarvue_Optimus_Wide_32mm(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_Optimus_Wide_32mm'])