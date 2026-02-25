from ...abstract import OutputOpticalEqipment
from ....constants import GraphConstants, OpticalType
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ..base import Eyepiece

class National_geographicEyepiece(Eyepiece):
    _DATABASE = {'National_Geographic_Plossl_4mm': {'brand': 'National Geographic', 'name': 'Plossl 4mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 95, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'National_Geographic_Plossl_6mm': {'brand': 'National Geographic', 'name': 'Plossl 6mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 100, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'National_Geographic_Plossl_9mm': {'brand': 'National Geographic', 'name': 'Plossl 9mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 105, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'National_Geographic_Plossl_12_5mm': {'brand': 'National Geographic', 'name': 'Plossl 12.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 115, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'National_Geographic_Plossl_20mm': {'brand': 'National Geographic', 'name': 'Plossl 20mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 130, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'National_Geographic_Plossl_25mm': {'brand': 'National Geographic', 'name': 'Plossl 25mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 145, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'National_Geographic_Plossl_32mm': {'brand': 'National Geographic', 'name': 'Plossl 32mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 170, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def National_Geographic_Plossl_4mm(cls):
        return cls.from_database(cls._DATABASE['National_Geographic_Plossl_4mm'])

    @classmethod
    def National_Geographic_Plossl_6mm(cls):
        return cls.from_database(cls._DATABASE['National_Geographic_Plossl_6mm'])

    @classmethod
    def National_Geographic_Plossl_9mm(cls):
        return cls.from_database(cls._DATABASE['National_Geographic_Plossl_9mm'])

    @classmethod
    def National_Geographic_Plossl_12_5mm(cls):
        return cls.from_database(cls._DATABASE['National_Geographic_Plossl_12_5mm'])

    @classmethod
    def National_Geographic_Plossl_20mm(cls):
        return cls.from_database(cls._DATABASE['National_Geographic_Plossl_20mm'])

    @classmethod
    def National_Geographic_Plossl_25mm(cls):
        return cls.from_database(cls._DATABASE['National_Geographic_Plossl_25mm'])

    @classmethod
    def National_Geographic_Plossl_32mm(cls):
        return cls.from_database(cls._DATABASE['National_Geographic_Plossl_32mm'])