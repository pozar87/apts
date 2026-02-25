from ...abstract import OutputOpticalEqipment
from ....constants import GraphConstants, OpticalType
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ..base import Eyepiece

class TmbEyepiece(Eyepiece):
    _DATABASE = {'TMB_Planetary_II_2_5mm_58': {'brand': 'TMB', 'name': 'Planetary II 2.5mm 58°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 120, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TMB_Planetary_II_3_2mm_58': {'brand': 'TMB', 'name': 'Planetary II 3.2mm 58°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 125, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TMB_Planetary_II_4mm_58': {'brand': 'TMB', 'name': 'Planetary II 4mm 58°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 130, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TMB_Planetary_II_5mm_58': {'brand': 'TMB', 'name': 'Planetary II 5mm 58°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 135, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TMB_Planetary_II_6mm_58': {'brand': 'TMB', 'name': 'Planetary II 6mm 58°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 140, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TMB_Planetary_II_7mm_58': {'brand': 'TMB', 'name': 'Planetary II 7mm 58°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 145, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TMB_Planetary_II_8mm_58': {'brand': 'TMB', 'name': 'Planetary II 8mm 58°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 150, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TMB_Planetary_II_9mm_58': {'brand': 'TMB', 'name': 'Planetary II 9mm 58°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 155, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TMB_Super_Mono_2_5mm': {'brand': 'TMB', 'name': 'Super Mono 2.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 150, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TMB_Super_Mono_3_2mm': {'brand': 'TMB', 'name': 'Super Mono 3.2mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 155, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TMB_Super_Mono_4mm': {'brand': 'TMB', 'name': 'Super Mono 4mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 160, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TMB_Super_Mono_5mm': {'brand': 'TMB', 'name': 'Super Mono 5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 168, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TMB_Super_Mono_6mm': {'brand': 'TMB', 'name': 'Super Mono 6mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 175, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TMB_Super_Mono_7mm': {'brand': 'TMB', 'name': 'Super Mono 7mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 180, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TMB_Super_Mono_8mm': {'brand': 'TMB', 'name': 'Super Mono 8mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 190, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TMB_Super_Mono_9mm': {'brand': 'TMB', 'name': 'Super Mono 9mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 195, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TMB_Super_Mono_10mm': {'brand': 'TMB', 'name': 'Super Mono 10mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 200, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TMB_Super_Mono_12_5mm': {'brand': 'TMB', 'name': 'Super Mono 12.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 220, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TMB_Super_Mono_16mm': {'brand': 'TMB', 'name': 'Super Mono 16mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 240, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TMB_Super_Mono_20mm': {'brand': 'TMB', 'name': 'Super Mono 20mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 260, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'TMB_Super_Mono_25mm': {'brand': 'TMB', 'name': 'Super Mono 25mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 290, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def TMB_Planetary_II_2_5mm_58(cls):
        return cls.from_database(cls._DATABASE['TMB_Planetary_II_2_5mm_58'])

    @classmethod
    def TMB_Planetary_II_3_2mm_58(cls):
        return cls.from_database(cls._DATABASE['TMB_Planetary_II_3_2mm_58'])

    @classmethod
    def TMB_Planetary_II_4mm_58(cls):
        return cls.from_database(cls._DATABASE['TMB_Planetary_II_4mm_58'])

    @classmethod
    def TMB_Planetary_II_5mm_58(cls):
        return cls.from_database(cls._DATABASE['TMB_Planetary_II_5mm_58'])

    @classmethod
    def TMB_Planetary_II_6mm_58(cls):
        return cls.from_database(cls._DATABASE['TMB_Planetary_II_6mm_58'])

    @classmethod
    def TMB_Planetary_II_7mm_58(cls):
        return cls.from_database(cls._DATABASE['TMB_Planetary_II_7mm_58'])

    @classmethod
    def TMB_Planetary_II_8mm_58(cls):
        return cls.from_database(cls._DATABASE['TMB_Planetary_II_8mm_58'])

    @classmethod
    def TMB_Planetary_II_9mm_58(cls):
        return cls.from_database(cls._DATABASE['TMB_Planetary_II_9mm_58'])

    @classmethod
    def TMB_Super_Mono_2_5mm(cls):
        return cls.from_database(cls._DATABASE['TMB_Super_Mono_2_5mm'])

    @classmethod
    def TMB_Super_Mono_3_2mm(cls):
        return cls.from_database(cls._DATABASE['TMB_Super_Mono_3_2mm'])

    @classmethod
    def TMB_Super_Mono_4mm(cls):
        return cls.from_database(cls._DATABASE['TMB_Super_Mono_4mm'])

    @classmethod
    def TMB_Super_Mono_5mm(cls):
        return cls.from_database(cls._DATABASE['TMB_Super_Mono_5mm'])

    @classmethod
    def TMB_Super_Mono_6mm(cls):
        return cls.from_database(cls._DATABASE['TMB_Super_Mono_6mm'])

    @classmethod
    def TMB_Super_Mono_7mm(cls):
        return cls.from_database(cls._DATABASE['TMB_Super_Mono_7mm'])

    @classmethod
    def TMB_Super_Mono_8mm(cls):
        return cls.from_database(cls._DATABASE['TMB_Super_Mono_8mm'])

    @classmethod
    def TMB_Super_Mono_9mm(cls):
        return cls.from_database(cls._DATABASE['TMB_Super_Mono_9mm'])

    @classmethod
    def TMB_Super_Mono_10mm(cls):
        return cls.from_database(cls._DATABASE['TMB_Super_Mono_10mm'])

    @classmethod
    def TMB_Super_Mono_12_5mm(cls):
        return cls.from_database(cls._DATABASE['TMB_Super_Mono_12_5mm'])

    @classmethod
    def TMB_Super_Mono_16mm(cls):
        return cls.from_database(cls._DATABASE['TMB_Super_Mono_16mm'])

    @classmethod
    def TMB_Super_Mono_20mm(cls):
        return cls.from_database(cls._DATABASE['TMB_Super_Mono_20mm'])

    @classmethod
    def TMB_Super_Mono_25mm(cls):
        return cls.from_database(cls._DATABASE['TMB_Super_Mono_25mm'])