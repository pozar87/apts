import numpy
from ...abstract import OpticalEquipment
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ....constants import GraphConstants
from enum import Enum
from typing import Optional
from ..base import TelescopeType, TubeMaterial, Telescope

class Lunt_solarTelescope(Telescope):
    _DATABASE = {'Lunt_Solar_LS60THa_60mm_H_alpha': {'brand': 'Lunt Solar', 'name': 'LS60THa 60mm H-alpha', 'type': 'type_telescope', 'optical_length': 0, 'mass': 2500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Lunt_Solar_LS80THa_80mm_H_alpha': {'brand': 'Lunt Solar', 'name': 'LS80THa 80mm H-alpha', 'type': 'type_telescope', 'optical_length': 0, 'mass': 4500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Lunt_Solar_LS100THa_100mm_H_alpha': {'brand': 'Lunt Solar', 'name': 'LS100THa 100mm H-alpha', 'type': 'type_telescope', 'optical_length': 0, 'mass': 7000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Lunt_Solar_LS130THa_130mm_H_alpha': {'brand': 'Lunt Solar', 'name': 'LS130THa 130mm H-alpha', 'type': 'type_telescope', 'optical_length': 0, 'mass': 12000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Lunt_Solar_LS50THa_50mm_H_alpha': {'brand': 'Lunt Solar', 'name': 'LS50THa 50mm H-alpha', 'type': 'type_telescope', 'optical_length': 0, 'mass': 1800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Lunt_Solar_LS60THa': {'brand': 'Lunt Solar', 'name': 'LS60THa', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Lunt_Solar_LS80THa': {'brand': 'Lunt Solar', 'name': 'LS80THa', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Lunt_Solar_LS100THa': {'brand': 'Lunt Solar', 'name': 'LS100THa', 'type': 'type_refractor', 'optical_length': 0, 'mass': 5500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Lunt_Solar_LS130THa': {'brand': 'Lunt Solar', 'name': 'LS130THa', 'type': 'type_refractor', 'optical_length': 0, 'mass': 8000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Lunt_Solar_LS152THa': {'brand': 'Lunt Solar', 'name': 'LS152THa', 'type': 'type_refractor', 'optical_length': 0, 'mass': 12000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Lunt_Solar_LS50C_Ca_K': {'brand': 'Lunt Solar', 'name': 'LS50C (Ca-K)', 'type': 'type_refractor', 'optical_length': 0, 'mass': 1200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Lunt_Solar_LS60MT': {'brand': 'Lunt Solar', 'name': 'LS60MT', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Lunt_Solar_LS80MT': {'brand': 'Lunt Solar', 'name': 'LS80MT', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Lunt_Solar_LS60THa_60mm_H_alpha(cls):
        return cls.from_database(cls._DATABASE['Lunt_Solar_LS60THa_60mm_H_alpha'])

    @classmethod
    def Lunt_Solar_LS80THa_80mm_H_alpha(cls):
        return cls.from_database(cls._DATABASE['Lunt_Solar_LS80THa_80mm_H_alpha'])

    @classmethod
    def Lunt_Solar_LS100THa_100mm_H_alpha(cls):
        return cls.from_database(cls._DATABASE['Lunt_Solar_LS100THa_100mm_H_alpha'])

    @classmethod
    def Lunt_Solar_LS130THa_130mm_H_alpha(cls):
        return cls.from_database(cls._DATABASE['Lunt_Solar_LS130THa_130mm_H_alpha'])

    @classmethod
    def Lunt_Solar_LS50THa_50mm_H_alpha(cls):
        return cls.from_database(cls._DATABASE['Lunt_Solar_LS50THa_50mm_H_alpha'])

    @classmethod
    def Lunt_Solar_LS60THa(cls):
        return cls.from_database(cls._DATABASE['Lunt_Solar_LS60THa'])

    @classmethod
    def Lunt_Solar_LS80THa(cls):
        return cls.from_database(cls._DATABASE['Lunt_Solar_LS80THa'])

    @classmethod
    def Lunt_Solar_LS100THa(cls):
        return cls.from_database(cls._DATABASE['Lunt_Solar_LS100THa'])

    @classmethod
    def Lunt_Solar_LS130THa(cls):
        return cls.from_database(cls._DATABASE['Lunt_Solar_LS130THa'])

    @classmethod
    def Lunt_Solar_LS152THa(cls):
        return cls.from_database(cls._DATABASE['Lunt_Solar_LS152THa'])

    @classmethod
    def Lunt_Solar_LS50C_Ca_K(cls):
        return cls.from_database(cls._DATABASE['Lunt_Solar_LS50C_Ca_K'])

    @classmethod
    def Lunt_Solar_LS60MT(cls):
        return cls.from_database(cls._DATABASE['Lunt_Solar_LS60MT'])

    @classmethod
    def Lunt_Solar_LS80MT(cls):
        return cls.from_database(cls._DATABASE['Lunt_Solar_LS80MT'])