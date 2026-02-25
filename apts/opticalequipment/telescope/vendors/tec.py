import numpy
from ...abstract import OpticalEquipment
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ....constants import GraphConstants
from enum import Enum
from typing import Optional
from ..base import TelescopeType, TubeMaterial, Telescope

class TecTelescope(Telescope):
    _DATABASE = {'TEC_TEC_110_FL': {'brand': 'TEC', 'name': 'TEC 110 FL', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TEC_TEC_140_FL': {'brand': 'TEC', 'name': 'TEC 140 FL', 'type': 'type_refractor', 'optical_length': 0, 'mass': 7000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TEC_TEC_160_FL': {'brand': 'TEC', 'name': 'TEC 160 FL', 'type': 'type_refractor', 'optical_length': 0, 'mass': 10000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TEC_TEC_180_FL': {'brand': 'TEC', 'name': 'TEC 180 FL', 'type': 'type_refractor', 'optical_length': 0, 'mass': 14000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TEC_TEC_200_FL': {'brand': 'TEC', 'name': 'TEC 200 FL', 'type': 'type_refractor', 'optical_length': 0, 'mass': 18000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def TEC_TEC_110_FL(cls):
        return cls.from_database(cls._DATABASE['TEC_TEC_110_FL'])

    @classmethod
    def TEC_TEC_140_FL(cls):
        return cls.from_database(cls._DATABASE['TEC_TEC_140_FL'])

    @classmethod
    def TEC_TEC_160_FL(cls):
        return cls.from_database(cls._DATABASE['TEC_TEC_160_FL'])

    @classmethod
    def TEC_TEC_180_FL(cls):
        return cls.from_database(cls._DATABASE['TEC_TEC_180_FL'])

    @classmethod
    def TEC_TEC_200_FL(cls):
        return cls.from_database(cls._DATABASE['TEC_TEC_200_FL'])