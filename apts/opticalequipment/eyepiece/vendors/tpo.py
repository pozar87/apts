from ...abstract import OutputOpticalEqipment
from ....constants import GraphConstants, OpticalType
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ..base import Eyepiece

class TpoEyepiece(Eyepiece):
    _DATABASE = {'TPO_SWA_5mm_68': {'brand': 'TPO', 'name': 'SWA 5mm 68°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 120, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TPO_SWA_8mm_68': {'brand': 'TPO', 'name': 'SWA 8mm 68°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 130, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TPO_SWA_12mm_68': {'brand': 'TPO', 'name': 'SWA 12mm 68°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 145, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TPO_SWA_18mm_68': {'brand': 'TPO', 'name': 'SWA 18mm 68°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 170, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TPO_SWA_25mm_68': {'brand': 'TPO', 'name': 'SWA 25mm 68°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 200, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TPO_SWA_32mm_68': {'brand': 'TPO', 'name': 'SWA 32mm 68°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 250, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TPO_Plossl_6mm': {'brand': 'TPO', 'name': 'Plossl 6mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 80, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TPO_Plossl_10mm': {'brand': 'TPO', 'name': 'Plossl 10mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 88, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TPO_Plossl_15mm': {'brand': 'TPO', 'name': 'Plossl 15mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 100, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TPO_Plossl_20mm': {'brand': 'TPO', 'name': 'Plossl 20mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 112, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TPO_Plossl_25mm': {'brand': 'TPO', 'name': 'Plossl 25mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 125, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TPO_Plossl_32mm': {'brand': 'TPO', 'name': 'Plossl 32mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 150, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def TPO_SWA_5mm_68(cls):
        return cls.from_database(cls._DATABASE['TPO_SWA_5mm_68'])

    @classmethod
    def TPO_SWA_8mm_68(cls):
        return cls.from_database(cls._DATABASE['TPO_SWA_8mm_68'])

    @classmethod
    def TPO_SWA_12mm_68(cls):
        return cls.from_database(cls._DATABASE['TPO_SWA_12mm_68'])

    @classmethod
    def TPO_SWA_18mm_68(cls):
        return cls.from_database(cls._DATABASE['TPO_SWA_18mm_68'])

    @classmethod
    def TPO_SWA_25mm_68(cls):
        return cls.from_database(cls._DATABASE['TPO_SWA_25mm_68'])

    @classmethod
    def TPO_SWA_32mm_68(cls):
        return cls.from_database(cls._DATABASE['TPO_SWA_32mm_68'])

    @classmethod
    def TPO_Plossl_6mm(cls):
        return cls.from_database(cls._DATABASE['TPO_Plossl_6mm'])

    @classmethod
    def TPO_Plossl_10mm(cls):
        return cls.from_database(cls._DATABASE['TPO_Plossl_10mm'])

    @classmethod
    def TPO_Plossl_15mm(cls):
        return cls.from_database(cls._DATABASE['TPO_Plossl_15mm'])

    @classmethod
    def TPO_Plossl_20mm(cls):
        return cls.from_database(cls._DATABASE['TPO_Plossl_20mm'])

    @classmethod
    def TPO_Plossl_25mm(cls):
        return cls.from_database(cls._DATABASE['TPO_Plossl_25mm'])

    @classmethod
    def TPO_Plossl_32mm(cls):
        return cls.from_database(cls._DATABASE['TPO_Plossl_32mm'])