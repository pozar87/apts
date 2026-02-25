import numpy
from ...abstract import OpticalEquipment
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ....constants import GraphConstants
from enum import Enum
from typing import Optional
from ..base import TelescopeType, TubeMaterial, Telescope

class TecnoskyTelescope(Telescope):
    _DATABASE = {'Tecnosky_Tecnosky_60_360_APO': {'brand': 'Tecnosky', 'name': 'Tecnosky 60/360 APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 1200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Tecnosky_Tecnosky_80_480_APO': {'brand': 'Tecnosky', 'name': 'Tecnosky 80/480 APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Tecnosky_Tecnosky_102_714_APO': {'brand': 'Tecnosky', 'name': 'Tecnosky 102/714 APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Tecnosky_Tecnosky_130_910_APO': {'brand': 'Tecnosky', 'name': 'Tecnosky 130/910 APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 6500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Tecnosky_Tecnosky_RC_6': {'brand': 'Tecnosky', 'name': 'Tecnosky RC 6"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 5200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Tecnosky_Tecnosky_RC_8': {'brand': 'Tecnosky', 'name': 'Tecnosky RC 8"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 8500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Tecnosky_Tecnosky_RC_10': {'brand': 'Tecnosky', 'name': 'Tecnosky RC 10"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 12000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Tecnosky_Tecnosky_RC_12': {'brand': 'Tecnosky', 'name': 'Tecnosky RC 12"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 16000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Tecnosky_Tecnosky_60_360_APO(cls):
        return cls.from_database(cls._DATABASE['Tecnosky_Tecnosky_60_360_APO'])

    @classmethod
    def Tecnosky_Tecnosky_80_480_APO(cls):
        return cls.from_database(cls._DATABASE['Tecnosky_Tecnosky_80_480_APO'])

    @classmethod
    def Tecnosky_Tecnosky_102_714_APO(cls):
        return cls.from_database(cls._DATABASE['Tecnosky_Tecnosky_102_714_APO'])

    @classmethod
    def Tecnosky_Tecnosky_130_910_APO(cls):
        return cls.from_database(cls._DATABASE['Tecnosky_Tecnosky_130_910_APO'])

    @classmethod
    def Tecnosky_Tecnosky_RC_6(cls):
        return cls.from_database(cls._DATABASE['Tecnosky_Tecnosky_RC_6'])

    @classmethod
    def Tecnosky_Tecnosky_RC_8(cls):
        return cls.from_database(cls._DATABASE['Tecnosky_Tecnosky_RC_8'])

    @classmethod
    def Tecnosky_Tecnosky_RC_10(cls):
        return cls.from_database(cls._DATABASE['Tecnosky_Tecnosky_RC_10'])

    @classmethod
    def Tecnosky_Tecnosky_RC_12(cls):
        return cls.from_database(cls._DATABASE['Tecnosky_Tecnosky_RC_12'])