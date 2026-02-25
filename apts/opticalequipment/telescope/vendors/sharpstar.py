import numpy
from ...abstract import OpticalEquipment
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ....constants import GraphConstants
from enum import Enum
from typing import Optional
from ..base import TelescopeType, TubeMaterial, Telescope

class SharpstarTelescope(Telescope):
    _DATABASE = {'Sharpstar_61EDPH_II': {'brand': 'Sharpstar', 'name': '61EDPH II', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sharpstar_76EDPH_II': {'brand': 'Sharpstar', 'name': '76EDPH II', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sharpstar_94EDPH_II': {'brand': 'Sharpstar', 'name': '94EDPH II', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sharpstar_140PH': {'brand': 'Sharpstar', 'name': '140PH', 'type': 'type_refractor', 'optical_length': 0, 'mass': 6000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sharpstar_200PH': {'brand': 'Sharpstar', 'name': '200PH', 'type': 'type_refractor', 'optical_length': 0, 'mass': 10000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sharpstar_15028HNT': {'brand': 'Sharpstar', 'name': '15028HNT', 'type': 'type_telescope', 'optical_length': 0, 'mass': 9500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sharpstar_20032HNT': {'brand': 'Sharpstar', 'name': '20032HNT', 'type': 'type_telescope', 'optical_length': 0, 'mass': 13000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sharpstar_25040HNT': {'brand': 'Sharpstar', 'name': '25040HNT', 'type': 'type_telescope', 'optical_length': 0, 'mass': 18000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sharpstar_61EDPH_III': {'brand': 'Sharpstar', 'name': '61EDPH III', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2600, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sharpstar_76EDPH_III': {'brand': 'Sharpstar', 'name': '76EDPH III', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3300, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sharpstar_94EDPH_III': {'brand': 'Sharpstar', 'name': '94EDPH III', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4600, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sharpstar_100Q': {'brand': 'Sharpstar', 'name': '100Q', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sharpstar_120Q': {'brand': 'Sharpstar', 'name': '120Q', 'type': 'type_refractor', 'optical_length': 0, 'mass': 5500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sharpstar_140PH_v2': {'brand': 'Sharpstar', 'name': '140PH v2', 'type': 'type_refractor', 'optical_length': 0, 'mass': 6200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sharpstar_15028HNT_v2': {'brand': 'Sharpstar', 'name': '15028HNT v2', 'type': 'type_telescope', 'optical_length': 0, 'mass': 9700, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sharpstar_20032HNT_v2': {'brand': 'Sharpstar', 'name': '20032HNT v2', 'type': 'type_telescope', 'optical_length': 0, 'mass': 13200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Sharpstar_61EDPH_II(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_61EDPH_II'])

    @classmethod
    def Sharpstar_76EDPH_II(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_76EDPH_II'])

    @classmethod
    def Sharpstar_94EDPH_II(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_94EDPH_II'])

    @classmethod
    def Sharpstar_140PH(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_140PH'])

    @classmethod
    def Sharpstar_200PH(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_200PH'])

    @classmethod
    def Sharpstar_15028HNT(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_15028HNT'])

    @classmethod
    def Sharpstar_20032HNT(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_20032HNT'])

    @classmethod
    def Sharpstar_25040HNT(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_25040HNT'])

    @classmethod
    def Sharpstar_61EDPH_III(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_61EDPH_III'])

    @classmethod
    def Sharpstar_76EDPH_III(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_76EDPH_III'])

    @classmethod
    def Sharpstar_94EDPH_III(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_94EDPH_III'])

    @classmethod
    def Sharpstar_100Q(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_100Q'])

    @classmethod
    def Sharpstar_120Q(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_120Q'])

    @classmethod
    def Sharpstar_140PH_v2(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_140PH_v2'])

    @classmethod
    def Sharpstar_15028HNT_v2(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_15028HNT_v2'])

    @classmethod
    def Sharpstar_20032HNT_v2(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_20032HNT_v2'])