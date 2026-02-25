from ...abstract import OutputOpticalEqipment
from ....constants import GraphConstants, OpticalType
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ..base import Eyepiece

class MasuyamaEyepiece(Eyepiece):
    _DATABASE = {'Masuyama_5mm_85': {'brand': 'Masuyama', 'name': '5mm 85°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 160, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Masuyama_8mm_85': {'brand': 'Masuyama', 'name': '8mm 85°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 165, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Masuyama_10mm_85': {'brand': 'Masuyama', 'name': '10mm 85°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 170, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Masuyama_15mm_85': {'brand': 'Masuyama', 'name': '15mm 85°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 180, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Masuyama_20mm_85': {'brand': 'Masuyama', 'name': '20mm 85°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 200, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Masuyama_25mm_85': {'brand': 'Masuyama', 'name': '25mm 85°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 220, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Masuyama_32mm_85': {'brand': 'Masuyama', 'name': '32mm 85°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 280, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Masuyama_12_5mm_85': {'brand': 'Masuyama', 'name': '12.5mm 85°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 180, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Masuyama_5mm_85(cls):
        return cls.from_database(cls._DATABASE['Masuyama_5mm_85'])

    @classmethod
    def Masuyama_8mm_85(cls):
        return cls.from_database(cls._DATABASE['Masuyama_8mm_85'])

    @classmethod
    def Masuyama_10mm_85(cls):
        return cls.from_database(cls._DATABASE['Masuyama_10mm_85'])

    @classmethod
    def Masuyama_15mm_85(cls):
        return cls.from_database(cls._DATABASE['Masuyama_15mm_85'])

    @classmethod
    def Masuyama_20mm_85(cls):
        return cls.from_database(cls._DATABASE['Masuyama_20mm_85'])

    @classmethod
    def Masuyama_25mm_85(cls):
        return cls.from_database(cls._DATABASE['Masuyama_25mm_85'])

    @classmethod
    def Masuyama_32mm_85(cls):
        return cls.from_database(cls._DATABASE['Masuyama_32mm_85'])

    @classmethod
    def Masuyama_12_5mm_85(cls):
        return cls.from_database(cls._DATABASE['Masuyama_12_5mm_85'])