import numpy
from ...abstract import OpticalEquipment
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ....constants import GraphConstants
from enum import Enum
from typing import Optional
from ..base import TelescopeType, TubeMaterial, Telescope

class National_geographicTelescope(Telescope):
    _DATABASE = {'National_Geographic_Nat_Geo_76_700_Newton': {'brand': 'National Geographic', 'name': 'Nat. Geo. 76/700 Newton', 'type': 'type_telescope', 'optical_length': 0, 'mass': 2500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'National_Geographic_Nat_Geo_114_900_Newton': {'brand': 'National Geographic', 'name': 'Nat. Geo. 114/900 Newton', 'type': 'type_telescope', 'optical_length': 0, 'mass': 4000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'National_Geographic_Nat_Geo_130_650_Newton': {'brand': 'National Geographic', 'name': 'Nat. Geo. 130/650 Newton', 'type': 'type_telescope', 'optical_length': 0, 'mass': 4500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def National_Geographic_Nat_Geo_76_700_Newton(cls):
        return cls.from_database(cls._DATABASE['National_Geographic_Nat_Geo_76_700_Newton'])

    @classmethod
    def National_Geographic_Nat_Geo_114_900_Newton(cls):
        return cls.from_database(cls._DATABASE['National_Geographic_Nat_Geo_114_900_Newton'])

    @classmethod
    def National_Geographic_Nat_Geo_130_650_Newton(cls):
        return cls.from_database(cls._DATABASE['National_Geographic_Nat_Geo_130_650_Newton'])