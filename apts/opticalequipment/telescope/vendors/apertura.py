import numpy
from ...abstract import OpticalEquipment
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ....constants import GraphConstants
from enum import Enum
from typing import Optional
from ..base import TelescopeType, TubeMaterial, Telescope

class AperturaTelescope(Telescope):
    _DATABASE = {'Apertura_AD6_Dobsonian': {'brand': 'Apertura', 'name': 'AD6 Dobsonian', 'type': 'type_telescope', 'optical_length': 0, 'mass': 5000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Apertura_AD8_Dobsonian': {'brand': 'Apertura', 'name': 'AD8 Dobsonian', 'type': 'type_telescope', 'optical_length': 0, 'mass': 7500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Apertura_AD10_Dobsonian': {'brand': 'Apertura', 'name': 'AD10 Dobsonian', 'type': 'type_telescope', 'optical_length': 0, 'mass': 10000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Apertura_AD12_Dobsonian': {'brand': 'Apertura', 'name': 'AD12 Dobsonian', 'type': 'type_telescope', 'optical_length': 0, 'mass': 14000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Apertura_AD14_Dobsonian': {'brand': 'Apertura', 'name': 'AD14 Dobsonian', 'type': 'type_telescope', 'optical_length': 0, 'mass': 19000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Apertura_AD16_Dobsonian': {'brand': 'Apertura', 'name': 'AD16 Dobsonian', 'type': 'type_telescope', 'optical_length': 0, 'mass': 27000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Apertura_AD6_Dobsonian(cls):
        return cls.from_database(cls._DATABASE['Apertura_AD6_Dobsonian'])

    @classmethod
    def Apertura_AD8_Dobsonian(cls):
        return cls.from_database(cls._DATABASE['Apertura_AD8_Dobsonian'])

    @classmethod
    def Apertura_AD10_Dobsonian(cls):
        return cls.from_database(cls._DATABASE['Apertura_AD10_Dobsonian'])

    @classmethod
    def Apertura_AD12_Dobsonian(cls):
        return cls.from_database(cls._DATABASE['Apertura_AD12_Dobsonian'])

    @classmethod
    def Apertura_AD14_Dobsonian(cls):
        return cls.from_database(cls._DATABASE['Apertura_AD14_Dobsonian'])

    @classmethod
    def Apertura_AD16_Dobsonian(cls):
        return cls.from_database(cls._DATABASE['Apertura_AD16_Dobsonian'])