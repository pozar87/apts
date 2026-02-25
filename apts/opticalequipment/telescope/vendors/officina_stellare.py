import numpy
from ...abstract import OpticalEquipment
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ....constants import GraphConstants
from enum import Enum
from typing import Optional
from ..base import TelescopeType, TubeMaterial, Telescope

class Officina_stellareTelescope(Telescope):
    _DATABASE = {'Officina_Stellare_RH200': {'brand': 'Officina Stellare', 'name': 'RH200', 'type': 'type_telescope', 'optical_length': 0, 'mass': 8000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Officina_Stellare_RH300': {'brand': 'Officina Stellare', 'name': 'RH300', 'type': 'type_telescope', 'optical_length': 0, 'mass': 14000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Officina_Stellare_RiDK_250': {'brand': 'Officina Stellare', 'name': 'RiDK 250', 'type': 'type_telescope', 'optical_length': 0, 'mass': 11000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Officina_Stellare_RiDK_300': {'brand': 'Officina Stellare', 'name': 'RiDK 300', 'type': 'type_telescope', 'optical_length': 0, 'mass': 15000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Officina_Stellare_RiDK_400': {'brand': 'Officina Stellare', 'name': 'RiDK 400', 'type': 'type_telescope', 'optical_length': 0, 'mass': 25000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Officina_Stellare_Ultra_CRC_250': {'brand': 'Officina Stellare', 'name': 'Ultra CRC 250', 'type': 'type_telescope', 'optical_length': 0, 'mass': 12000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Officina_Stellare_Ultra_CRC_300': {'brand': 'Officina Stellare', 'name': 'Ultra CRC 300', 'type': 'type_telescope', 'optical_length': 0, 'mass': 16000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Officina_Stellare_RH200(cls):
        return cls.from_database(cls._DATABASE['Officina_Stellare_RH200'])

    @classmethod
    def Officina_Stellare_RH300(cls):
        return cls.from_database(cls._DATABASE['Officina_Stellare_RH300'])

    @classmethod
    def Officina_Stellare_RiDK_250(cls):
        return cls.from_database(cls._DATABASE['Officina_Stellare_RiDK_250'])

    @classmethod
    def Officina_Stellare_RiDK_300(cls):
        return cls.from_database(cls._DATABASE['Officina_Stellare_RiDK_300'])

    @classmethod
    def Officina_Stellare_RiDK_400(cls):
        return cls.from_database(cls._DATABASE['Officina_Stellare_RiDK_400'])

    @classmethod
    def Officina_Stellare_Ultra_CRC_250(cls):
        return cls.from_database(cls._DATABASE['Officina_Stellare_Ultra_CRC_250'])

    @classmethod
    def Officina_Stellare_Ultra_CRC_300(cls):
        return cls.from_database(cls._DATABASE['Officina_Stellare_Ultra_CRC_300'])