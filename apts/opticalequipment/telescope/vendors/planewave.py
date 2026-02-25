import numpy
from ...abstract import OpticalEquipment
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ....constants import GraphConstants
from enum import Enum
from typing import Optional
from ..base import TelescopeType, TubeMaterial, Telescope

class PlanewaveTelescope(Telescope):
    _DATABASE = {'PlaneWave_CDK12_5': {'brand': 'PlaneWave', 'name': 'CDK12.5', 'type': 'type_telescope', 'optical_length': 0, 'mass': 15000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'PlaneWave_CDK14': {'brand': 'PlaneWave', 'name': 'CDK14', 'type': 'type_telescope', 'optical_length': 0, 'mass': 21000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'PlaneWave_CDK17': {'brand': 'PlaneWave', 'name': 'CDK17', 'type': 'type_telescope', 'optical_length': 0, 'mass': 32000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'PlaneWave_CDK20': {'brand': 'PlaneWave', 'name': 'CDK20', 'type': 'type_telescope', 'optical_length': 0, 'mass': 50000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'PlaneWave_CDK24': {'brand': 'PlaneWave', 'name': 'CDK24', 'type': 'type_telescope', 'optical_length': 0, 'mass': 65000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def PlaneWave_CDK12_5(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_CDK12_5'])

    @classmethod
    def PlaneWave_CDK14(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_CDK14'])

    @classmethod
    def PlaneWave_CDK17(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_CDK17'])

    @classmethod
    def PlaneWave_CDK20(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_CDK20'])

    @classmethod
    def PlaneWave_CDK24(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_CDK24'])