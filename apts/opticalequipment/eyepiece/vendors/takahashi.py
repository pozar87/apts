from ...abstract import OutputOpticalEqipment
from ....constants import GraphConstants, OpticalType
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ..base import Eyepiece

class TakahashiEyepiece(Eyepiece):
    _DATABASE = {'Takahashi_Abbe_Ortho_2_8mm': {'brand': 'Takahashi', 'name': 'Abbe Ortho 2.8mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 250, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Takahashi_Abbe_Ortho_5mm': {'brand': 'Takahashi', 'name': 'Abbe Ortho 5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 200, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Takahashi_Abbe_Ortho_7_5mm': {'brand': 'Takahashi', 'name': 'Abbe Ortho 7.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 210, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Takahashi_Abbe_Ortho_10mm': {'brand': 'Takahashi', 'name': 'Abbe Ortho 10mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 220, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Takahashi_Abbe_Ortho_15mm': {'brand': 'Takahashi', 'name': 'Abbe Ortho 15mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 240, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Takahashi_Abbe_Ortho_20mm': {'brand': 'Takahashi', 'name': 'Abbe Ortho 20mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 260, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Takahashi_Abbe_Ortho_25mm': {'brand': 'Takahashi', 'name': 'Abbe Ortho 25mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 290, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Takahashi_TOE_12_5mm': {'brand': 'Takahashi', 'name': 'TOE 12.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 300, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Takahashi_TOE_20mm': {'brand': 'Takahashi', 'name': 'TOE 20mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 350, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Takahashi_TOE_25mm': {'brand': 'Takahashi', 'name': 'TOE 25mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 400, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Takahashi_TPL_2_5mm': {'brand': 'Takahashi', 'name': 'TPL 2.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 130, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Takahashi_TPL_3_6mm': {'brand': 'Takahashi', 'name': 'TPL 3.6mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 135, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Takahashi_TPL_5mm': {'brand': 'Takahashi', 'name': 'TPL 5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 145, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Takahashi_TPL_6_4mm': {'brand': 'Takahashi', 'name': 'TPL 6.4mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 150, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Takahashi_TPL_8mm': {'brand': 'Takahashi', 'name': 'TPL 8mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 160, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Takahashi_TPL_12_5mm': {'brand': 'Takahashi', 'name': 'TPL 12.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 180, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Takahashi_TPL_18mm': {'brand': 'Takahashi', 'name': 'TPL 18mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 200, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Takahashi_TPL_25mm': {'brand': 'Takahashi', 'name': 'TPL 25mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 230, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Takahashi_TPL_40mm': {'brand': 'Takahashi', 'name': 'TPL 40mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 350, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Takahashi_Abbe_Ortho_4mm': {'brand': 'Takahashi', 'name': 'Abbe Ortho 4mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 120, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Takahashi_Abbe_Ortho_6mm': {'brand': 'Takahashi', 'name': 'Abbe Ortho 6mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 130, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Takahashi_Abbe_Ortho_9mm': {'brand': 'Takahashi', 'name': 'Abbe Ortho 9mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 145, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Takahashi_Abbe_Ortho_12_5mm': {'brand': 'Takahashi', 'name': 'Abbe Ortho 12.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 160, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Takahashi_Abbe_Ortho_18mm': {'brand': 'Takahashi', 'name': 'Abbe Ortho 18mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 180, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Takahashi_Abbe_Ortho_32mm': {'brand': 'Takahashi', 'name': 'Abbe Ortho 32mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 260, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Takahashi_TOE_2_5mm': {'brand': 'Takahashi', 'name': 'TOE 2.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 200, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Takahashi_TOE_4mm': {'brand': 'Takahashi', 'name': 'TOE 4mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 210, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Takahashi_TOE_6mm': {'brand': 'Takahashi', 'name': 'TOE 6mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 220, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Takahashi_TOE_8mm': {'brand': 'Takahashi', 'name': 'TOE 8mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 235, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Takahashi_TOE_10mm': {'brand': 'Takahashi', 'name': 'TOE 10mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 250, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Takahashi_TOE_18mm': {'brand': 'Takahashi', 'name': 'TOE 18mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 310, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Takahashi_Abbe_Ortho_2_8mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Abbe_Ortho_2_8mm'])

    @classmethod
    def Takahashi_Abbe_Ortho_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Abbe_Ortho_5mm'])

    @classmethod
    def Takahashi_Abbe_Ortho_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Abbe_Ortho_7_5mm'])

    @classmethod
    def Takahashi_Abbe_Ortho_10mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Abbe_Ortho_10mm'])

    @classmethod
    def Takahashi_Abbe_Ortho_15mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Abbe_Ortho_15mm'])

    @classmethod
    def Takahashi_Abbe_Ortho_20mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Abbe_Ortho_20mm'])

    @classmethod
    def Takahashi_Abbe_Ortho_25mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Abbe_Ortho_25mm'])

    @classmethod
    def Takahashi_TOE_12_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_TOE_12_5mm'])

    @classmethod
    def Takahashi_TOE_20mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_TOE_20mm'])

    @classmethod
    def Takahashi_TOE_25mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_TOE_25mm'])

    @classmethod
    def Takahashi_TPL_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_TPL_2_5mm'])

    @classmethod
    def Takahashi_TPL_3_6mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_TPL_3_6mm'])

    @classmethod
    def Takahashi_TPL_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_TPL_5mm'])

    @classmethod
    def Takahashi_TPL_6_4mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_TPL_6_4mm'])

    @classmethod
    def Takahashi_TPL_8mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_TPL_8mm'])

    @classmethod
    def Takahashi_TPL_12_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_TPL_12_5mm'])

    @classmethod
    def Takahashi_TPL_18mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_TPL_18mm'])

    @classmethod
    def Takahashi_TPL_25mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_TPL_25mm'])

    @classmethod
    def Takahashi_TPL_40mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_TPL_40mm'])

    @classmethod
    def Takahashi_Abbe_Ortho_4mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Abbe_Ortho_4mm'])

    @classmethod
    def Takahashi_Abbe_Ortho_6mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Abbe_Ortho_6mm'])

    @classmethod
    def Takahashi_Abbe_Ortho_9mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Abbe_Ortho_9mm'])

    @classmethod
    def Takahashi_Abbe_Ortho_12_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Abbe_Ortho_12_5mm'])

    @classmethod
    def Takahashi_Abbe_Ortho_18mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Abbe_Ortho_18mm'])

    @classmethod
    def Takahashi_Abbe_Ortho_32mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Abbe_Ortho_32mm'])

    @classmethod
    def Takahashi_TOE_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_TOE_2_5mm'])

    @classmethod
    def Takahashi_TOE_4mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_TOE_4mm'])

    @classmethod
    def Takahashi_TOE_6mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_TOE_6mm'])

    @classmethod
    def Takahashi_TOE_8mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_TOE_8mm'])

    @classmethod
    def Takahashi_TOE_10mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_TOE_10mm'])

    @classmethod
    def Takahashi_TOE_18mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_TOE_18mm'])