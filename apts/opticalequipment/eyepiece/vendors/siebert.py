from ...abstract import OutputOpticalEqipment
from ....constants import GraphConstants, OpticalType
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ..base import Eyepiece

class SiebertEyepiece(Eyepiece):
    _DATABASE = {'Siebert_Stellar_4mm': {'brand': 'Siebert', 'name': 'Stellar 4mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 180, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Siebert_Stellar_6mm': {'brand': 'Siebert', 'name': 'Stellar 6mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 190, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Siebert_Stellar_8mm': {'brand': 'Siebert', 'name': 'Stellar 8mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 200, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Siebert_Stellar_10mm': {'brand': 'Siebert', 'name': 'Stellar 10mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 215, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Siebert_Stellar_13mm': {'brand': 'Siebert', 'name': 'Stellar 13mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 240, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Siebert_Stellar_18mm': {'brand': 'Siebert', 'name': 'Stellar 18mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 270, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Siebert_Stellar_24mm': {'brand': 'Siebert', 'name': 'Stellar 24mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 320, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Siebert_Stellar_36mm': {'brand': 'Siebert', 'name': 'Stellar 36mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 500, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Siebert_Stellar_4mm(cls):
        return cls.from_database(cls._DATABASE['Siebert_Stellar_4mm'])

    @classmethod
    def Siebert_Stellar_6mm(cls):
        return cls.from_database(cls._DATABASE['Siebert_Stellar_6mm'])

    @classmethod
    def Siebert_Stellar_8mm(cls):
        return cls.from_database(cls._DATABASE['Siebert_Stellar_8mm'])

    @classmethod
    def Siebert_Stellar_10mm(cls):
        return cls.from_database(cls._DATABASE['Siebert_Stellar_10mm'])

    @classmethod
    def Siebert_Stellar_13mm(cls):
        return cls.from_database(cls._DATABASE['Siebert_Stellar_13mm'])

    @classmethod
    def Siebert_Stellar_18mm(cls):
        return cls.from_database(cls._DATABASE['Siebert_Stellar_18mm'])

    @classmethod
    def Siebert_Stellar_24mm(cls):
        return cls.from_database(cls._DATABASE['Siebert_Stellar_24mm'])

    @classmethod
    def Siebert_Stellar_36mm(cls):
        return cls.from_database(cls._DATABASE['Siebert_Stellar_36mm'])