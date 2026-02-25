from ...abstract import OutputOpticalEqipment
from ....constants import GraphConstants, OpticalType
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ..base import Eyepiece

class BrandonEyepiece(Eyepiece):
    _DATABASE = {'Brandon_8mm': {'brand': 'Brandon', 'name': '8mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 130, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Brandon_12mm': {'brand': 'Brandon', 'name': '12mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 140, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Brandon_16mm': {'brand': 'Brandon', 'name': '16mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 150, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Brandon_24mm': {'brand': 'Brandon', 'name': '24mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 170, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Brandon_32mm': {'brand': 'Brandon', 'name': '32mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 200, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Brandon_8mm(cls):
        return cls.from_database(cls._DATABASE['Brandon_8mm'])

    @classmethod
    def Brandon_12mm(cls):
        return cls.from_database(cls._DATABASE['Brandon_12mm'])

    @classmethod
    def Brandon_16mm(cls):
        return cls.from_database(cls._DATABASE['Brandon_16mm'])

    @classmethod
    def Brandon_24mm(cls):
        return cls.from_database(cls._DATABASE['Brandon_24mm'])

    @classmethod
    def Brandon_32mm(cls):
        return cls.from_database(cls._DATABASE['Brandon_32mm'])