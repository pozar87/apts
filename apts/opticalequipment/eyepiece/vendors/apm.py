from ...abstract import OutputOpticalEqipment
from ....constants import GraphConstants, OpticalType
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ..base import Eyepiece

class ApmEyepiece(Eyepiece):
    _DATABASE = {'APM_XWA_3_5mm_100': {'brand': 'APM', 'name': 'XWA 3.5mm 100°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 320, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'APM_XWA_7mm_100': {'brand': 'APM', 'name': 'XWA 7mm 100°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 340, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'APM_XWA_9mm_100': {'brand': 'APM', 'name': 'XWA 9mm 100°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 360, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'APM_XWA_13mm_100': {'brand': 'APM', 'name': 'XWA 13mm 100°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 380, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'APM_XWA_20mm_100': {'brand': 'APM', 'name': 'XWA 20mm 100°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 600, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'APM_HDC_4mm': {'brand': 'APM', 'name': 'HDC 4mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 140, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'APM_HDC_6mm': {'brand': 'APM', 'name': 'HDC 6mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 145, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'APM_HDC_9mm': {'brand': 'APM', 'name': 'HDC 9mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 150, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'APM_HDC_12mm': {'brand': 'APM', 'name': 'HDC 12mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 160, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'APM_HDC_18mm': {'brand': 'APM', 'name': 'HDC 18mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 180, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'APM_HDC_25mm': {'brand': 'APM', 'name': 'HDC 25mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 210, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'APM_UFF_10mm': {'brand': 'APM', 'name': 'UFF 10mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 250, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'APM_UFF_15mm': {'brand': 'APM', 'name': 'UFF 15mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 280, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'APM_UFF_18mm': {'brand': 'APM', 'name': 'UFF 18mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 300, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'APM_UFF_24mm': {'brand': 'APM', 'name': 'UFF 24mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 450, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'APM_UFF_30mm': {'brand': 'APM', 'name': 'UFF 30mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 600, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'APM_Plossl_6_5mm': {'brand': 'APM', 'name': 'Plossl 6.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 100, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'APM_Plossl_10mm': {'brand': 'APM', 'name': 'Plossl 10mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 110, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'APM_Plossl_15mm': {'brand': 'APM', 'name': 'Plossl 15mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 125, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'APM_Plossl_20mm': {'brand': 'APM', 'name': 'Plossl 20mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 140, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'APM_Plossl_25mm': {'brand': 'APM', 'name': 'Plossl 25mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 155, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'APM_Plossl_32mm': {'brand': 'APM', 'name': 'Plossl 32mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 180, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'APM_Plossl_40mm': {'brand': 'APM', 'name': 'Plossl 40mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 210, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def APM_XWA_3_5mm_100(cls):
        return cls.from_database(cls._DATABASE['APM_XWA_3_5mm_100'])

    @classmethod
    def APM_XWA_7mm_100(cls):
        return cls.from_database(cls._DATABASE['APM_XWA_7mm_100'])

    @classmethod
    def APM_XWA_9mm_100(cls):
        return cls.from_database(cls._DATABASE['APM_XWA_9mm_100'])

    @classmethod
    def APM_XWA_13mm_100(cls):
        return cls.from_database(cls._DATABASE['APM_XWA_13mm_100'])

    @classmethod
    def APM_XWA_20mm_100(cls):
        return cls.from_database(cls._DATABASE['APM_XWA_20mm_100'])

    @classmethod
    def APM_HDC_4mm(cls):
        return cls.from_database(cls._DATABASE['APM_HDC_4mm'])

    @classmethod
    def APM_HDC_6mm(cls):
        return cls.from_database(cls._DATABASE['APM_HDC_6mm'])

    @classmethod
    def APM_HDC_9mm(cls):
        return cls.from_database(cls._DATABASE['APM_HDC_9mm'])

    @classmethod
    def APM_HDC_12mm(cls):
        return cls.from_database(cls._DATABASE['APM_HDC_12mm'])

    @classmethod
    def APM_HDC_18mm(cls):
        return cls.from_database(cls._DATABASE['APM_HDC_18mm'])

    @classmethod
    def APM_HDC_25mm(cls):
        return cls.from_database(cls._DATABASE['APM_HDC_25mm'])

    @classmethod
    def APM_UFF_10mm(cls):
        return cls.from_database(cls._DATABASE['APM_UFF_10mm'])

    @classmethod
    def APM_UFF_15mm(cls):
        return cls.from_database(cls._DATABASE['APM_UFF_15mm'])

    @classmethod
    def APM_UFF_18mm(cls):
        return cls.from_database(cls._DATABASE['APM_UFF_18mm'])

    @classmethod
    def APM_UFF_24mm(cls):
        return cls.from_database(cls._DATABASE['APM_UFF_24mm'])

    @classmethod
    def APM_UFF_30mm(cls):
        return cls.from_database(cls._DATABASE['APM_UFF_30mm'])

    @classmethod
    def APM_Plossl_6_5mm(cls):
        return cls.from_database(cls._DATABASE['APM_Plossl_6_5mm'])

    @classmethod
    def APM_Plossl_10mm(cls):
        return cls.from_database(cls._DATABASE['APM_Plossl_10mm'])

    @classmethod
    def APM_Plossl_15mm(cls):
        return cls.from_database(cls._DATABASE['APM_Plossl_15mm'])

    @classmethod
    def APM_Plossl_20mm(cls):
        return cls.from_database(cls._DATABASE['APM_Plossl_20mm'])

    @classmethod
    def APM_Plossl_25mm(cls):
        return cls.from_database(cls._DATABASE['APM_Plossl_25mm'])

    @classmethod
    def APM_Plossl_32mm(cls):
        return cls.from_database(cls._DATABASE['APM_Plossl_32mm'])

    @classmethod
    def APM_Plossl_40mm(cls):
        return cls.from_database(cls._DATABASE['APM_Plossl_40mm'])