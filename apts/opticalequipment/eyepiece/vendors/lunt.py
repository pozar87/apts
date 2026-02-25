from ...abstract import OutputOpticalEqipment
from ....constants import GraphConstants, OpticalType
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ..base import Eyepiece

class LuntEyepiece(Eyepiece):
    _DATABASE = {'Lunt_H_alpha_7_5mm': {'brand': 'Lunt', 'name': 'H-alpha 7.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 150, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Lunt_H_alpha_12mm': {'brand': 'Lunt', 'name': 'H-alpha 12mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 160, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Lunt_H_alpha_16mm': {'brand': 'Lunt', 'name': 'H-alpha 16mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 170, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Lunt_H_alpha_19mm': {'brand': 'Lunt', 'name': 'H-alpha 19mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 190, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Lunt_H_alpha_27mm': {'brand': 'Lunt', 'name': 'H-alpha 27mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 250, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Lunt_H_alpha_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Lunt_H_alpha_7_5mm'])

    @classmethod
    def Lunt_H_alpha_12mm(cls):
        return cls.from_database(cls._DATABASE['Lunt_H_alpha_12mm'])

    @classmethod
    def Lunt_H_alpha_16mm(cls):
        return cls.from_database(cls._DATABASE['Lunt_H_alpha_16mm'])

    @classmethod
    def Lunt_H_alpha_19mm(cls):
        return cls.from_database(cls._DATABASE['Lunt_H_alpha_19mm'])

    @classmethod
    def Lunt_H_alpha_27mm(cls):
        return cls.from_database(cls._DATABASE['Lunt_H_alpha_27mm'])