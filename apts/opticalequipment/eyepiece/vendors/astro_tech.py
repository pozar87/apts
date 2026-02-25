from ...abstract import OutputOpticalEqipment
from ....constants import GraphConstants, OpticalType
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ..base import Eyepiece

class Astro_techEyepiece(Eyepiece):
    _DATABASE = {'Astro_Tech_Paradigm_3_5mm': {'brand': 'Astro-Tech', 'name': 'Paradigm 3.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 170, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Astro_Tech_Paradigm_5mm': {'brand': 'Astro-Tech', 'name': 'Paradigm 5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 180, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Astro_Tech_Paradigm_7mm': {'brand': 'Astro-Tech', 'name': 'Paradigm 7mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 190, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Astro_Tech_Paradigm_9mm': {'brand': 'Astro-Tech', 'name': 'Paradigm 9mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 200, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Astro_Tech_Paradigm_12mm': {'brand': 'Astro-Tech', 'name': 'Paradigm 12mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 220, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Astro_Tech_Paradigm_15mm': {'brand': 'Astro-Tech', 'name': 'Paradigm 15mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 240, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Astro_Tech_Paradigm_18mm': {'brand': 'Astro-Tech', 'name': 'Paradigm 18mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 260, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Astro_Tech_Paradigm_22mm': {'brand': 'Astro-Tech', 'name': 'Paradigm 22mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 290, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Astro_Tech_Paradigm_27mm': {'brand': 'Astro-Tech', 'name': 'Paradigm 27mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 350, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Astro_Tech_Titan_5mm_68': {'brand': 'Astro-Tech', 'name': 'Titan 5mm 68°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 130, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Astro_Tech_Titan_8mm_68': {'brand': 'Astro-Tech', 'name': 'Titan 8mm 68°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 140, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Astro_Tech_Titan_12mm_68': {'brand': 'Astro-Tech', 'name': 'Titan 12mm 68°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 155, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Astro_Tech_Titan_18mm_68': {'brand': 'Astro-Tech', 'name': 'Titan 18mm 68°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 180, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Astro_Tech_Titan_25mm_68': {'brand': 'Astro-Tech', 'name': 'Titan 25mm 68°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 210, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Astro_Tech_EF_4_5mm_70': {'brand': 'Astro-Tech', 'name': 'EF 4.5mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 160, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Astro_Tech_EF_6_5mm_70': {'brand': 'Astro-Tech', 'name': 'EF 6.5mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 170, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Astro_Tech_EF_8_5mm_70': {'brand': 'Astro-Tech', 'name': 'EF 8.5mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 180, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Astro_Tech_EF_11mm_70': {'brand': 'Astro-Tech', 'name': 'EF 11mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 200, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Astro_Tech_EF_14mm_70': {'brand': 'Astro-Tech', 'name': 'EF 14mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 220, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Astro_Tech_EF_18mm_70': {'brand': 'Astro-Tech', 'name': 'EF 18mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 250, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Astro_Tech_EF_24mm_70': {'brand': 'Astro-Tech', 'name': 'EF 24mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 320, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Astro_Tech_EF_30mm_70': {'brand': 'Astro-Tech', 'name': 'EF 30mm 70°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 450, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Astro_Tech_Paradigm_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Astro_Tech_Paradigm_3_5mm'])

    @classmethod
    def Astro_Tech_Paradigm_5mm(cls):
        return cls.from_database(cls._DATABASE['Astro_Tech_Paradigm_5mm'])

    @classmethod
    def Astro_Tech_Paradigm_7mm(cls):
        return cls.from_database(cls._DATABASE['Astro_Tech_Paradigm_7mm'])

    @classmethod
    def Astro_Tech_Paradigm_9mm(cls):
        return cls.from_database(cls._DATABASE['Astro_Tech_Paradigm_9mm'])

    @classmethod
    def Astro_Tech_Paradigm_12mm(cls):
        return cls.from_database(cls._DATABASE['Astro_Tech_Paradigm_12mm'])

    @classmethod
    def Astro_Tech_Paradigm_15mm(cls):
        return cls.from_database(cls._DATABASE['Astro_Tech_Paradigm_15mm'])

    @classmethod
    def Astro_Tech_Paradigm_18mm(cls):
        return cls.from_database(cls._DATABASE['Astro_Tech_Paradigm_18mm'])

    @classmethod
    def Astro_Tech_Paradigm_22mm(cls):
        return cls.from_database(cls._DATABASE['Astro_Tech_Paradigm_22mm'])

    @classmethod
    def Astro_Tech_Paradigm_27mm(cls):
        return cls.from_database(cls._DATABASE['Astro_Tech_Paradigm_27mm'])

    @classmethod
    def Astro_Tech_Titan_5mm_68(cls):
        return cls.from_database(cls._DATABASE['Astro_Tech_Titan_5mm_68'])

    @classmethod
    def Astro_Tech_Titan_8mm_68(cls):
        return cls.from_database(cls._DATABASE['Astro_Tech_Titan_8mm_68'])

    @classmethod
    def Astro_Tech_Titan_12mm_68(cls):
        return cls.from_database(cls._DATABASE['Astro_Tech_Titan_12mm_68'])

    @classmethod
    def Astro_Tech_Titan_18mm_68(cls):
        return cls.from_database(cls._DATABASE['Astro_Tech_Titan_18mm_68'])

    @classmethod
    def Astro_Tech_Titan_25mm_68(cls):
        return cls.from_database(cls._DATABASE['Astro_Tech_Titan_25mm_68'])

    @classmethod
    def Astro_Tech_EF_4_5mm_70(cls):
        return cls.from_database(cls._DATABASE['Astro_Tech_EF_4_5mm_70'])

    @classmethod
    def Astro_Tech_EF_6_5mm_70(cls):
        return cls.from_database(cls._DATABASE['Astro_Tech_EF_6_5mm_70'])

    @classmethod
    def Astro_Tech_EF_8_5mm_70(cls):
        return cls.from_database(cls._DATABASE['Astro_Tech_EF_8_5mm_70'])

    @classmethod
    def Astro_Tech_EF_11mm_70(cls):
        return cls.from_database(cls._DATABASE['Astro_Tech_EF_11mm_70'])

    @classmethod
    def Astro_Tech_EF_14mm_70(cls):
        return cls.from_database(cls._DATABASE['Astro_Tech_EF_14mm_70'])

    @classmethod
    def Astro_Tech_EF_18mm_70(cls):
        return cls.from_database(cls._DATABASE['Astro_Tech_EF_18mm_70'])

    @classmethod
    def Astro_Tech_EF_24mm_70(cls):
        return cls.from_database(cls._DATABASE['Astro_Tech_EF_24mm_70'])

    @classmethod
    def Astro_Tech_EF_30mm_70(cls):
        return cls.from_database(cls._DATABASE['Astro_Tech_EF_30mm_70'])