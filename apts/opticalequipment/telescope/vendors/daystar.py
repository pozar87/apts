import numpy
from ...abstract import OpticalEquipment
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ....constants import GraphConstants
from enum import Enum
from typing import Optional
from ..base import TelescopeType, TubeMaterial, Telescope

class DaystarTelescope(Telescope):
    _DATABASE = {'DayStar_Solar_Scout_60mm': {'brand': 'DayStar', 'name': 'Solar Scout 60mm', 'type': 'type_telescope', 'optical_length': 0, 'mass': 2000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'DayStar_Solar_Scout_80mm': {'brand': 'DayStar', 'name': 'Solar Scout 80mm', 'type': 'type_telescope', 'optical_length': 0, 'mass': 3500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'DayStar_SOLO_60_SE': {'brand': 'DayStar', 'name': 'SOLO 60 SE', 'type': 'type_refractor', 'optical_length': 0, 'mass': 1800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'DayStar_SOLO_60_PE': {'brand': 'DayStar', 'name': 'SOLO 60 PE', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'DayStar_SOLO_80_SE': {'brand': 'DayStar', 'name': 'SOLO 80 SE', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'DayStar_SolaREDi_66': {'brand': 'DayStar', 'name': 'SolaREDi 66', 'type': 'type_refractor', 'optical_length': 0, 'mass': 1200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'DayStar_SolaREDi_127': {'brand': 'DayStar', 'name': 'SolaREDi 127', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def DayStar_Solar_Scout_60mm(cls):
        return cls.from_database(cls._DATABASE['DayStar_Solar_Scout_60mm'])

    @classmethod
    def DayStar_Solar_Scout_80mm(cls):
        return cls.from_database(cls._DATABASE['DayStar_Solar_Scout_80mm'])

    @classmethod
    def DayStar_SOLO_60_SE(cls):
        return cls.from_database(cls._DATABASE['DayStar_SOLO_60_SE'])

    @classmethod
    def DayStar_SOLO_60_PE(cls):
        return cls.from_database(cls._DATABASE['DayStar_SOLO_60_PE'])

    @classmethod
    def DayStar_SOLO_80_SE(cls):
        return cls.from_database(cls._DATABASE['DayStar_SOLO_80_SE'])

    @classmethod
    def DayStar_SolaREDi_66(cls):
        return cls.from_database(cls._DATABASE['DayStar_SolaREDi_66'])

    @classmethod
    def DayStar_SolaREDi_127(cls):
        return cls.from_database(cls._DATABASE['DayStar_SolaREDi_127'])