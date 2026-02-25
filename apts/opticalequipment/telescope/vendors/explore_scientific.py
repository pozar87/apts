import numpy
from ...abstract import OpticalEquipment
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ....constants import GraphConstants
from enum import Enum
from typing import Optional
from ..base import TelescopeType, TubeMaterial, Telescope

class Explore_scientificTelescope(Telescope):
    _DATABASE = {'Explore_Scientific_ED80_FCD100': {'brand': 'Explore Scientific', 'name': 'ED80 FCD100', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Explore_Scientific_ED102_FCD100': {'brand': 'Explore Scientific', 'name': 'ED102 FCD100', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Explore_Scientific_ED127_FCD100': {'brand': 'Explore Scientific', 'name': 'ED127 FCD100', 'type': 'type_refractor', 'optical_length': 0, 'mass': 7000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Explore_Scientific_ED152_FCD100': {'brand': 'Explore Scientific', 'name': 'ED152 FCD100', 'type': 'type_refractor', 'optical_length': 0, 'mass': 11000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Explore_Scientific_ED80_Essential': {'brand': 'Explore Scientific', 'name': 'ED80 Essential', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Explore_Scientific_ED102_Essential': {'brand': 'Explore Scientific', 'name': 'ED102 Essential', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Explore_Scientific_ED127_Essential': {'brand': 'Explore Scientific', 'name': 'ED127 Essential', 'type': 'type_refractor', 'optical_length': 0, 'mass': 5500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Explore_Scientific_FCD1_80': {'brand': 'Explore Scientific', 'name': 'FCD1-80', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Explore_Scientific_FCD1_102': {'brand': 'Explore Scientific', 'name': 'FCD1-102', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Explore_Scientific_FCD100_127_Triplet': {'brand': 'Explore Scientific', 'name': 'FCD100-127 Triplet', 'type': 'type_refractor', 'optical_length': 0, 'mass': 7500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Explore_Scientific_DAR152065_6_f_5_Newton': {'brand': 'Explore Scientific', 'name': 'DAR152065 (6" f/5 Newton)', 'type': 'type_telescope', 'optical_length': 0, 'mass': 5500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Explore_Scientific_DAR20010001_8_f_5_Newton': {'brand': 'Explore Scientific', 'name': 'DAR20010001 (8" f/5 Newton)', 'type': 'type_telescope', 'optical_length': 0, 'mass': 8500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Explore_Scientific_Truss_Dob_10': {'brand': 'Explore Scientific', 'name': 'Truss Dob 10"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 10000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Explore_Scientific_Truss_Dob_12': {'brand': 'Explore Scientific', 'name': 'Truss Dob 12"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 14000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Explore_Scientific_Truss_Dob_16': {'brand': 'Explore Scientific', 'name': 'Truss Dob 16"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 22000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Explore_Scientific_305mm_f_5_Newton': {'brand': 'Explore Scientific', 'name': '305mm f/5 Newton', 'type': 'type_telescope', 'optical_length': 0, 'mass': 11000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Explore_Scientific_Ultra_Light_10': {'brand': 'Explore Scientific', 'name': 'Ultra Light 10"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 10500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Explore_Scientific_Ultra_Light_12': {'brand': 'Explore Scientific', 'name': 'Ultra Light 12"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 14000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Explore_Scientific_Ultra_Light_16': {'brand': 'Explore Scientific', 'name': 'Ultra Light 16"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 22000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Explore_Scientific_AR102_Air_Spaced_Doublet': {'brand': 'Explore Scientific', 'name': 'AR102 Air-Spaced Doublet', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Explore_Scientific_AR127_Air_Spaced': {'brand': 'Explore Scientific', 'name': 'AR127 Air-Spaced', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Explore_Scientific_AR152_Air_Spaced': {'brand': 'Explore Scientific', 'name': 'AR152 Air-Spaced', 'type': 'type_refractor', 'optical_length': 0, 'mass': 6000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Explore_Scientific_FirstLight_130mm_f_4_6_Newton': {'brand': 'Explore Scientific', 'name': 'FirstLight 130mm f/4.6 Newton', 'type': 'type_telescope', 'optical_length': 0, 'mass': 4000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Explore_Scientific_FirstLight_150mm_f_5_Newton': {'brand': 'Explore Scientific', 'name': 'FirstLight 150mm f/5 Newton', 'type': 'type_telescope', 'optical_length': 0, 'mass': 5000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Explore_Scientific_FirstLight_200mm_f_5_Newton': {'brand': 'Explore Scientific', 'name': 'FirstLight 200mm f/5 Newton', 'type': 'type_telescope', 'optical_length': 0, 'mass': 8000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Explore_Scientific_FirstLight_102mm_Mak': {'brand': 'Explore Scientific', 'name': 'FirstLight 102mm Mak', 'type': 'type_telescope', 'optical_length': 0, 'mass': 2800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Explore_Scientific_FirstLight_127mm_Mak': {'brand': 'Explore Scientific', 'name': 'FirstLight 127mm Mak', 'type': 'type_telescope', 'optical_length': 0, 'mass': 3500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Explore_Scientific_FirstLight_80mm_APO': {'brand': 'Explore Scientific', 'name': 'FirstLight 80mm APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Explore_Scientific_FirstLight_102mm_APO': {'brand': 'Explore Scientific', 'name': 'FirstLight 102mm APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Explore_Scientific_ED_APO_80mm_CF': {'brand': 'Explore Scientific', 'name': 'ED APO 80mm CF', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Explore_Scientific_ED_APO_102mm_CF': {'brand': 'Explore Scientific', 'name': 'ED APO 102mm CF', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Explore_Scientific_ED_APO_127mm_CF': {'brand': 'Explore Scientific', 'name': 'ED APO 127mm CF', 'type': 'type_refractor', 'optical_length': 0, 'mass': 7500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Explore_Scientific_ED_APO_152mm_CF': {'brand': 'Explore Scientific', 'name': 'ED APO 152mm CF', 'type': 'type_refractor', 'optical_length': 0, 'mass': 12000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Explore_Scientific_FirstLight_90mm_Mak': {'brand': 'Explore Scientific', 'name': 'FirstLight 90mm Mak', 'type': 'type_telescope', 'optical_length': 0, 'mass': 2000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Explore_Scientific_FirstLight_114mm_Newton': {'brand': 'Explore Scientific', 'name': 'FirstLight 114mm Newton', 'type': 'type_telescope', 'optical_length': 0, 'mass': 2500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Explore_Scientific_FirstLight_130mm_Newton': {'brand': 'Explore Scientific', 'name': 'FirstLight 130mm Newton', 'type': 'type_telescope', 'optical_length': 0, 'mass': 3500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Explore_Scientific_FirstLight_152mm_Newton': {'brand': 'Explore Scientific', 'name': 'FirstLight 152mm Newton', 'type': 'type_telescope', 'optical_length': 0, 'mass': 5500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Explore_Scientific_StarGate_18_Truss_Dob': {'brand': 'Explore Scientific', 'name': 'StarGate 18" Truss Dob', 'type': 'type_telescope', 'optical_length': 0, 'mass': 25000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Explore_Scientific_StarGate_20_Truss_Dob': {'brand': 'Explore Scientific', 'name': 'StarGate 20" Truss Dob', 'type': 'type_telescope', 'optical_length': 0, 'mass': 32000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Explore_Scientific_ED165_FCD100_CF': {'brand': 'Explore Scientific', 'name': 'ED165 FCD100 CF', 'type': 'type_refractor', 'optical_length': 0, 'mass': 14000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Explore_Scientific_ED127_FCD1_CF': {'brand': 'Explore Scientific', 'name': 'ED127 FCD1 CF', 'type': 'type_refractor', 'optical_length': 0, 'mass': 7200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Explore_Scientific_ED80_FCD100(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_ED80_FCD100'])

    @classmethod
    def Explore_Scientific_ED102_FCD100(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_ED102_FCD100'])

    @classmethod
    def Explore_Scientific_ED127_FCD100(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_ED127_FCD100'])

    @classmethod
    def Explore_Scientific_ED152_FCD100(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_ED152_FCD100'])

    @classmethod
    def Explore_Scientific_ED80_Essential(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_ED80_Essential'])

    @classmethod
    def Explore_Scientific_ED102_Essential(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_ED102_Essential'])

    @classmethod
    def Explore_Scientific_ED127_Essential(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_ED127_Essential'])

    @classmethod
    def Explore_Scientific_FCD1_80(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_FCD1_80'])

    @classmethod
    def Explore_Scientific_FCD1_102(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_FCD1_102'])

    @classmethod
    def Explore_Scientific_FCD100_127_Triplet(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_FCD100_127_Triplet'])

    @classmethod
    def Explore_Scientific_DAR152065_6_f_5_Newton(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_DAR152065_6_f_5_Newton'])

    @classmethod
    def Explore_Scientific_DAR20010001_8_f_5_Newton(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_DAR20010001_8_f_5_Newton'])

    @classmethod
    def Explore_Scientific_Truss_Dob_10(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_Truss_Dob_10'])

    @classmethod
    def Explore_Scientific_Truss_Dob_12(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_Truss_Dob_12'])

    @classmethod
    def Explore_Scientific_Truss_Dob_16(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_Truss_Dob_16'])

    @classmethod
    def Explore_Scientific_305mm_f_5_Newton(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_305mm_f_5_Newton'])

    @classmethod
    def Explore_Scientific_Ultra_Light_10(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_Ultra_Light_10'])

    @classmethod
    def Explore_Scientific_Ultra_Light_12(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_Ultra_Light_12'])

    @classmethod
    def Explore_Scientific_Ultra_Light_16(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_Ultra_Light_16'])

    @classmethod
    def Explore_Scientific_AR102_Air_Spaced_Doublet(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_AR102_Air_Spaced_Doublet'])

    @classmethod
    def Explore_Scientific_AR127_Air_Spaced(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_AR127_Air_Spaced'])

    @classmethod
    def Explore_Scientific_AR152_Air_Spaced(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_AR152_Air_Spaced'])

    @classmethod
    def Explore_Scientific_FirstLight_130mm_f_4_6_Newton(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_FirstLight_130mm_f_4_6_Newton'])

    @classmethod
    def Explore_Scientific_FirstLight_150mm_f_5_Newton(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_FirstLight_150mm_f_5_Newton'])

    @classmethod
    def Explore_Scientific_FirstLight_200mm_f_5_Newton(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_FirstLight_200mm_f_5_Newton'])

    @classmethod
    def Explore_Scientific_FirstLight_102mm_Mak(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_FirstLight_102mm_Mak'])

    @classmethod
    def Explore_Scientific_FirstLight_127mm_Mak(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_FirstLight_127mm_Mak'])

    @classmethod
    def Explore_Scientific_FirstLight_80mm_APO(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_FirstLight_80mm_APO'])

    @classmethod
    def Explore_Scientific_FirstLight_102mm_APO(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_FirstLight_102mm_APO'])

    @classmethod
    def Explore_Scientific_ED_APO_80mm_CF(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_ED_APO_80mm_CF'])

    @classmethod
    def Explore_Scientific_ED_APO_102mm_CF(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_ED_APO_102mm_CF'])

    @classmethod
    def Explore_Scientific_ED_APO_127mm_CF(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_ED_APO_127mm_CF'])

    @classmethod
    def Explore_Scientific_ED_APO_152mm_CF(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_ED_APO_152mm_CF'])

    @classmethod
    def Explore_Scientific_FirstLight_90mm_Mak(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_FirstLight_90mm_Mak'])

    @classmethod
    def Explore_Scientific_FirstLight_114mm_Newton(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_FirstLight_114mm_Newton'])

    @classmethod
    def Explore_Scientific_FirstLight_130mm_Newton(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_FirstLight_130mm_Newton'])

    @classmethod
    def Explore_Scientific_FirstLight_152mm_Newton(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_FirstLight_152mm_Newton'])

    @classmethod
    def Explore_Scientific_StarGate_18_Truss_Dob(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_StarGate_18_Truss_Dob'])

    @classmethod
    def Explore_Scientific_StarGate_20_Truss_Dob(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_StarGate_20_Truss_Dob'])

    @classmethod
    def Explore_Scientific_ED165_FCD100_CF(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_ED165_FCD100_CF'])

    @classmethod
    def Explore_Scientific_ED127_FCD1_CF(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_ED127_FCD1_CF'])