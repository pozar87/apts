from ...abstract import OutputOpticalEqipment
from ....constants import GraphConstants, OpticalType
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ..base import Eyepiece

class IstarEyepiece(Eyepiece):
    _DATABASE = {'Istar_UWA_3_5mm_100': {'brand': 'Istar', 'name': 'UWA 3.5mm 100°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 250, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Istar_UWA_5mm_100': {'brand': 'Istar', 'name': 'UWA 5mm 100°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 260, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Istar_UWA_7mm_100': {'brand': 'Istar', 'name': 'UWA 7mm 100°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 270, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Istar_UWA_10mm_100': {'brand': 'Istar', 'name': 'UWA 10mm 100°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 290, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Istar_UWA_14mm_100': {'brand': 'Istar', 'name': 'UWA 14mm 100°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 320, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Istar_UWA_18mm_100': {'brand': 'Istar', 'name': 'UWA 18mm 100°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 350, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Istar_UWA_22mm_100': {'brand': 'Istar', 'name': 'UWA 22mm 100°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 400, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Istar_UWA_30mm_100': {'brand': 'Istar', 'name': 'UWA 30mm 100°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 600, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Istar_UWA_3_5mm_100(cls):
        return cls.from_database(cls._DATABASE['Istar_UWA_3_5mm_100'])

    @classmethod
    def Istar_UWA_5mm_100(cls):
        return cls.from_database(cls._DATABASE['Istar_UWA_5mm_100'])

    @classmethod
    def Istar_UWA_7mm_100(cls):
        return cls.from_database(cls._DATABASE['Istar_UWA_7mm_100'])

    @classmethod
    def Istar_UWA_10mm_100(cls):
        return cls.from_database(cls._DATABASE['Istar_UWA_10mm_100'])

    @classmethod
    def Istar_UWA_14mm_100(cls):
        return cls.from_database(cls._DATABASE['Istar_UWA_14mm_100'])

    @classmethod
    def Istar_UWA_18mm_100(cls):
        return cls.from_database(cls._DATABASE['Istar_UWA_18mm_100'])

    @classmethod
    def Istar_UWA_22mm_100(cls):
        return cls.from_database(cls._DATABASE['Istar_UWA_22mm_100'])

    @classmethod
    def Istar_UWA_30mm_100(cls):
        return cls.from_database(cls._DATABASE['Istar_UWA_30mm_100'])