from ...abstract import OutputOpticalEqipment
from ....constants import GraphConstants, OpticalType
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ..base import Eyepiece

class GenericEyepiece(Eyepiece):
    _DATABASE = {'Generic_Plossl_4mm': {'brand': 'Generic', 'name': 'Plossl 4mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 70, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Generic_Plossl_6mm': {'brand': 'Generic', 'name': 'Plossl 6mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 75, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Generic_Plossl_8mm': {'brand': 'Generic', 'name': 'Plossl 8mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 80, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Generic_Plossl_10mm': {'brand': 'Generic', 'name': 'Plossl 10mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 85, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Generic_Plossl_12_5mm': {'brand': 'Generic', 'name': 'Plossl 12.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 90, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Generic_Plossl_15mm': {'brand': 'Generic', 'name': 'Plossl 15mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 95, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Generic_Plossl_20mm': {'brand': 'Generic', 'name': 'Plossl 20mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 105, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Generic_Plossl_25mm': {'brand': 'Generic', 'name': 'Plossl 25mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 115, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Generic_Plossl_30mm': {'brand': 'Generic', 'name': 'Plossl 30mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 130, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Generic_Plossl_40mm': {'brand': 'Generic', 'name': 'Plossl 40mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 160, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Generic_Wide_Angle_66_6mm': {'brand': 'Generic', 'name': 'Wide Angle 66° 6mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 120, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Generic_Wide_Angle_66_9mm': {'brand': 'Generic', 'name': 'Wide Angle 66° 9mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 130, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Generic_Wide_Angle_66_12mm': {'brand': 'Generic', 'name': 'Wide Angle 66° 12mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 140, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Generic_Wide_Angle_66_15mm': {'brand': 'Generic', 'name': 'Wide Angle 66° 15mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 150, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Generic_Wide_Angle_66_20mm': {'brand': 'Generic', 'name': 'Wide Angle 66° 20mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 170, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Generic_Wide_Angle_66_25mm': {'brand': 'Generic', 'name': 'Wide Angle 66° 25mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 190, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Generic_Plossl_32mm': {'brand': 'Generic', 'name': 'Plossl 32mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 140, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Generic_SWA_6mm_70': {'brand': 'Generic', 'name': 'SWA 6mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 90, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Generic_SWA_10mm_70': {'brand': 'Generic', 'name': 'SWA 10mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 100, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Generic_SWA_15mm_70': {'brand': 'Generic', 'name': 'SWA 15mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 115, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Generic_SWA_20mm_70': {'brand': 'Generic', 'name': 'SWA 20mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 135, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Generic_SWA_25mm_70': {'brand': 'Generic', 'name': 'SWA 25mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 155, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Generic_SWA_32mm_70': {'brand': 'Generic', 'name': 'SWA 32mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 190, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Generic_WA_6mm_68': {'brand': 'Generic', 'name': 'WA 6mm 68°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 120, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Generic_WA_9mm_68': {'brand': 'Generic', 'name': 'WA 9mm 68°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 130, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Generic_WA_12mm_68': {'brand': 'Generic', 'name': 'WA 12mm 68°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 145, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Generic_WA_15mm_68': {'brand': 'Generic', 'name': 'WA 15mm 68°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 165, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Generic_WA_20mm_68': {'brand': 'Generic', 'name': 'WA 20mm 68°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 190, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Generic_Plossl_4mm(cls):
        return cls.from_database(cls._DATABASE['Generic_Plossl_4mm'])

    @classmethod
    def Generic_Plossl_6mm(cls):
        return cls.from_database(cls._DATABASE['Generic_Plossl_6mm'])

    @classmethod
    def Generic_Plossl_8mm(cls):
        return cls.from_database(cls._DATABASE['Generic_Plossl_8mm'])

    @classmethod
    def Generic_Plossl_10mm(cls):
        return cls.from_database(cls._DATABASE['Generic_Plossl_10mm'])

    @classmethod
    def Generic_Plossl_12_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_Plossl_12_5mm'])

    @classmethod
    def Generic_Plossl_15mm(cls):
        return cls.from_database(cls._DATABASE['Generic_Plossl_15mm'])

    @classmethod
    def Generic_Plossl_20mm(cls):
        return cls.from_database(cls._DATABASE['Generic_Plossl_20mm'])

    @classmethod
    def Generic_Plossl_25mm(cls):
        return cls.from_database(cls._DATABASE['Generic_Plossl_25mm'])

    @classmethod
    def Generic_Plossl_30mm(cls):
        return cls.from_database(cls._DATABASE['Generic_Plossl_30mm'])

    @classmethod
    def Generic_Plossl_40mm(cls):
        return cls.from_database(cls._DATABASE['Generic_Plossl_40mm'])

    @classmethod
    def Generic_Wide_Angle_66_6mm(cls):
        return cls.from_database(cls._DATABASE['Generic_Wide_Angle_66_6mm'])

    @classmethod
    def Generic_Wide_Angle_66_9mm(cls):
        return cls.from_database(cls._DATABASE['Generic_Wide_Angle_66_9mm'])

    @classmethod
    def Generic_Wide_Angle_66_12mm(cls):
        return cls.from_database(cls._DATABASE['Generic_Wide_Angle_66_12mm'])

    @classmethod
    def Generic_Wide_Angle_66_15mm(cls):
        return cls.from_database(cls._DATABASE['Generic_Wide_Angle_66_15mm'])

    @classmethod
    def Generic_Wide_Angle_66_20mm(cls):
        return cls.from_database(cls._DATABASE['Generic_Wide_Angle_66_20mm'])

    @classmethod
    def Generic_Wide_Angle_66_25mm(cls):
        return cls.from_database(cls._DATABASE['Generic_Wide_Angle_66_25mm'])

    @classmethod
    def Generic_Plossl_32mm(cls):
        return cls.from_database(cls._DATABASE['Generic_Plossl_32mm'])

    @classmethod
    def Generic_SWA_6mm_70(cls):
        return cls.from_database(cls._DATABASE['Generic_SWA_6mm_70'])

    @classmethod
    def Generic_SWA_10mm_70(cls):
        return cls.from_database(cls._DATABASE['Generic_SWA_10mm_70'])

    @classmethod
    def Generic_SWA_15mm_70(cls):
        return cls.from_database(cls._DATABASE['Generic_SWA_15mm_70'])

    @classmethod
    def Generic_SWA_20mm_70(cls):
        return cls.from_database(cls._DATABASE['Generic_SWA_20mm_70'])

    @classmethod
    def Generic_SWA_25mm_70(cls):
        return cls.from_database(cls._DATABASE['Generic_SWA_25mm_70'])

    @classmethod
    def Generic_SWA_32mm_70(cls):
        return cls.from_database(cls._DATABASE['Generic_SWA_32mm_70'])

    @classmethod
    def Generic_WA_6mm_68(cls):
        return cls.from_database(cls._DATABASE['Generic_WA_6mm_68'])

    @classmethod
    def Generic_WA_9mm_68(cls):
        return cls.from_database(cls._DATABASE['Generic_WA_9mm_68'])

    @classmethod
    def Generic_WA_12mm_68(cls):
        return cls.from_database(cls._DATABASE['Generic_WA_12mm_68'])

    @classmethod
    def Generic_WA_15mm_68(cls):
        return cls.from_database(cls._DATABASE['Generic_WA_15mm_68'])

    @classmethod
    def Generic_WA_20mm_68(cls):
        return cls.from_database(cls._DATABASE['Generic_WA_20mm_68'])