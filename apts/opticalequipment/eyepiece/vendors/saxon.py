from ...abstract import OutputOpticalEqipment
from ....constants import GraphConstants, OpticalType
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ..base import Eyepiece

class SaxonEyepiece(Eyepiece):
    _DATABASE = {'Saxon_Plossl_4mm': {'brand': 'Saxon', 'name': 'Plossl 4mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 100, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Saxon_Plossl_6mm': {'brand': 'Saxon', 'name': 'Plossl 6mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 105, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Saxon_Plossl_9mm': {'brand': 'Saxon', 'name': 'Plossl 9mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 110, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Saxon_Plossl_12_5mm': {'brand': 'Saxon', 'name': 'Plossl 12.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 120, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Saxon_Plossl_16mm': {'brand': 'Saxon', 'name': 'Plossl 16mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 130, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Saxon_Plossl_20mm': {'brand': 'Saxon', 'name': 'Plossl 20mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 140, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Saxon_Plossl_25mm': {'brand': 'Saxon', 'name': 'Plossl 25mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 160, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Saxon_Plossl_4mm(cls):
        return cls.from_database(cls._DATABASE['Saxon_Plossl_4mm'])

    @classmethod
    def Saxon_Plossl_6mm(cls):
        return cls.from_database(cls._DATABASE['Saxon_Plossl_6mm'])

    @classmethod
    def Saxon_Plossl_9mm(cls):
        return cls.from_database(cls._DATABASE['Saxon_Plossl_9mm'])

    @classmethod
    def Saxon_Plossl_12_5mm(cls):
        return cls.from_database(cls._DATABASE['Saxon_Plossl_12_5mm'])

    @classmethod
    def Saxon_Plossl_16mm(cls):
        return cls.from_database(cls._DATABASE['Saxon_Plossl_16mm'])

    @classmethod
    def Saxon_Plossl_20mm(cls):
        return cls.from_database(cls._DATABASE['Saxon_Plossl_20mm'])

    @classmethod
    def Saxon_Plossl_25mm(cls):
        return cls.from_database(cls._DATABASE['Saxon_Plossl_25mm'])