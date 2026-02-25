from ...abstract import OutputOpticalEqipment
from ....constants import GraphConstants, OpticalType
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ..base import Eyepiece

class Ts_opticsEyepiece(Eyepiece):
    _DATABASE = {'TS_Optics_Planetary_HR_2_5mm': {'brand': 'TS-Optics', 'name': 'Planetary HR 2.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 140, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TS_Optics_Planetary_HR_3_2mm': {'brand': 'TS-Optics', 'name': 'Planetary HR 3.2mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 145, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TS_Optics_Planetary_HR_4mm': {'brand': 'TS-Optics', 'name': 'Planetary HR 4mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 150, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TS_Optics_Planetary_HR_5mm': {'brand': 'TS-Optics', 'name': 'Planetary HR 5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 155, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TS_Optics_Planetary_HR_7mm': {'brand': 'TS-Optics', 'name': 'Planetary HR 7mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 165, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TS_Optics_Planetary_HR_9mm': {'brand': 'TS-Optics', 'name': 'Planetary HR 9mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 175, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TS_Optics_UWA_82_5_5mm': {'brand': 'TS-Optics', 'name': 'UWA 82° 5.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 190, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TS_Optics_UWA_82_7mm': {'brand': 'TS-Optics', 'name': 'UWA 82° 7mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 200, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TS_Optics_UWA_82_10mm': {'brand': 'TS-Optics', 'name': 'UWA 82° 10mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 210, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TS_Optics_UWA_82_15mm': {'brand': 'TS-Optics', 'name': 'UWA 82° 15mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 230, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TS_Optics_UWA_82_20mm': {'brand': 'TS-Optics', 'name': 'UWA 82° 20mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 260, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TS_Optics_UWA_82_30mm': {'brand': 'TS-Optics', 'name': 'UWA 82° 30mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 550, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TS_Optics_WA_72_5mm': {'brand': 'TS-Optics', 'name': 'WA 72° 5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 140, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TS_Optics_WA_72_7mm': {'brand': 'TS-Optics', 'name': 'WA 72° 7mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 150, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TS_Optics_WA_72_10mm': {'brand': 'TS-Optics', 'name': 'WA 72° 10mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 160, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TS_Optics_WA_72_15mm': {'brand': 'TS-Optics', 'name': 'WA 72° 15mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 175, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TS_Optics_WA_72_20mm': {'brand': 'TS-Optics', 'name': 'WA 72° 20mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 195, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TS_Optics_WA_72_25mm': {'brand': 'TS-Optics', 'name': 'WA 72° 25mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 220, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TS_Optics_Expanse_4mm_70': {'brand': 'TS-Optics', 'name': 'Expanse 4mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 130, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TS_Optics_Expanse_6mm_70': {'brand': 'TS-Optics', 'name': 'Expanse 6mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 135, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TS_Optics_Expanse_8mm_70': {'brand': 'TS-Optics', 'name': 'Expanse 8mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 140, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TS_Optics_Expanse_10mm_70': {'brand': 'TS-Optics', 'name': 'Expanse 10mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 150, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TS_Optics_Expanse_13mm_70': {'brand': 'TS-Optics', 'name': 'Expanse 13mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 160, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TS_Optics_Expanse_17mm_70': {'brand': 'TS-Optics', 'name': 'Expanse 17mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 175, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TS_Optics_Expanse_22mm_70': {'brand': 'TS-Optics', 'name': 'Expanse 22mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 200, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TS_Optics_Plossl_4mm': {'brand': 'TS-Optics', 'name': 'Plossl 4mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 80, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TS_Optics_Plossl_6_3mm': {'brand': 'TS-Optics', 'name': 'Plossl 6.3mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 85, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TS_Optics_Plossl_10mm': {'brand': 'TS-Optics', 'name': 'Plossl 10mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 95, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TS_Optics_Plossl_15mm': {'brand': 'TS-Optics', 'name': 'Plossl 15mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 105, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TS_Optics_Plossl_20mm': {'brand': 'TS-Optics', 'name': 'Plossl 20mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 115, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TS_Optics_Plossl_25mm': {'brand': 'TS-Optics', 'name': 'Plossl 25mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 130, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TS_Optics_Plossl_32mm': {'brand': 'TS-Optics', 'name': 'Plossl 32mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 155, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TS_Optics_Plossl_40mm': {'brand': 'TS-Optics', 'name': 'Plossl 40mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 185, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TS_Optics_SuperFlat_4mm': {'brand': 'TS-Optics', 'name': 'SuperFlat 4mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 160, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TS_Optics_SuperFlat_6mm': {'brand': 'TS-Optics', 'name': 'SuperFlat 6mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 170, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TS_Optics_SuperFlat_8mm': {'brand': 'TS-Optics', 'name': 'SuperFlat 8mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 180, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TS_Optics_SuperFlat_10mm': {'brand': 'TS-Optics', 'name': 'SuperFlat 10mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 190, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TS_Optics_SuperFlat_13mm': {'brand': 'TS-Optics', 'name': 'SuperFlat 13mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 210, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TS_Optics_SuperFlat_16mm': {'brand': 'TS-Optics', 'name': 'SuperFlat 16mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 230, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TS_Optics_SuperFlat_22mm': {'brand': 'TS-Optics', 'name': 'SuperFlat 22mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 290, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TS_Optics_SuperFlat_30mm': {'brand': 'TS-Optics', 'name': 'SuperFlat 30mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 450, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def TS_Optics_Planetary_HR_2_5mm(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Planetary_HR_2_5mm'])

    @classmethod
    def TS_Optics_Planetary_HR_3_2mm(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Planetary_HR_3_2mm'])

    @classmethod
    def TS_Optics_Planetary_HR_4mm(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Planetary_HR_4mm'])

    @classmethod
    def TS_Optics_Planetary_HR_5mm(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Planetary_HR_5mm'])

    @classmethod
    def TS_Optics_Planetary_HR_7mm(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Planetary_HR_7mm'])

    @classmethod
    def TS_Optics_Planetary_HR_9mm(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Planetary_HR_9mm'])

    @classmethod
    def TS_Optics_UWA_82_5_5mm(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_UWA_82_5_5mm'])

    @classmethod
    def TS_Optics_UWA_82_7mm(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_UWA_82_7mm'])

    @classmethod
    def TS_Optics_UWA_82_10mm(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_UWA_82_10mm'])

    @classmethod
    def TS_Optics_UWA_82_15mm(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_UWA_82_15mm'])

    @classmethod
    def TS_Optics_UWA_82_20mm(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_UWA_82_20mm'])

    @classmethod
    def TS_Optics_UWA_82_30mm(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_UWA_82_30mm'])

    @classmethod
    def TS_Optics_WA_72_5mm(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_WA_72_5mm'])

    @classmethod
    def TS_Optics_WA_72_7mm(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_WA_72_7mm'])

    @classmethod
    def TS_Optics_WA_72_10mm(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_WA_72_10mm'])

    @classmethod
    def TS_Optics_WA_72_15mm(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_WA_72_15mm'])

    @classmethod
    def TS_Optics_WA_72_20mm(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_WA_72_20mm'])

    @classmethod
    def TS_Optics_WA_72_25mm(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_WA_72_25mm'])

    @classmethod
    def TS_Optics_Expanse_4mm_70(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Expanse_4mm_70'])

    @classmethod
    def TS_Optics_Expanse_6mm_70(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Expanse_6mm_70'])

    @classmethod
    def TS_Optics_Expanse_8mm_70(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Expanse_8mm_70'])

    @classmethod
    def TS_Optics_Expanse_10mm_70(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Expanse_10mm_70'])

    @classmethod
    def TS_Optics_Expanse_13mm_70(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Expanse_13mm_70'])

    @classmethod
    def TS_Optics_Expanse_17mm_70(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Expanse_17mm_70'])

    @classmethod
    def TS_Optics_Expanse_22mm_70(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Expanse_22mm_70'])

    @classmethod
    def TS_Optics_Plossl_4mm(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Plossl_4mm'])

    @classmethod
    def TS_Optics_Plossl_6_3mm(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Plossl_6_3mm'])

    @classmethod
    def TS_Optics_Plossl_10mm(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Plossl_10mm'])

    @classmethod
    def TS_Optics_Plossl_15mm(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Plossl_15mm'])

    @classmethod
    def TS_Optics_Plossl_20mm(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Plossl_20mm'])

    @classmethod
    def TS_Optics_Plossl_25mm(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Plossl_25mm'])

    @classmethod
    def TS_Optics_Plossl_32mm(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Plossl_32mm'])

    @classmethod
    def TS_Optics_Plossl_40mm(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Plossl_40mm'])

    @classmethod
    def TS_Optics_SuperFlat_4mm(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_SuperFlat_4mm'])

    @classmethod
    def TS_Optics_SuperFlat_6mm(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_SuperFlat_6mm'])

    @classmethod
    def TS_Optics_SuperFlat_8mm(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_SuperFlat_8mm'])

    @classmethod
    def TS_Optics_SuperFlat_10mm(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_SuperFlat_10mm'])

    @classmethod
    def TS_Optics_SuperFlat_13mm(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_SuperFlat_13mm'])

    @classmethod
    def TS_Optics_SuperFlat_16mm(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_SuperFlat_16mm'])

    @classmethod
    def TS_Optics_SuperFlat_22mm(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_SuperFlat_22mm'])

    @classmethod
    def TS_Optics_SuperFlat_30mm(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_SuperFlat_30mm'])