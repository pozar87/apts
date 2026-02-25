import numpy
from ...abstract import OpticalEquipment
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ....constants import GraphConstants
from enum import Enum
from typing import Optional
from ..base import TelescopeType, TubeMaterial, Telescope

class TelevueTelescope(Telescope):
    _DATABASE = {'TeleVue_NP101is': {'brand': 'TeleVue', 'name': 'NP101is', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TeleVue_NP127fli': {'brand': 'TeleVue', 'name': 'NP127fli', 'type': 'type_refractor', 'optical_length': 0, 'mass': 6500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TeleVue_TV_60': {'brand': 'TeleVue', 'name': 'TV-60', 'type': 'type_refractor', 'optical_length': 0, 'mass': 900, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TeleVue_TV_76': {'brand': 'TeleVue', 'name': 'TV-76', 'type': 'type_refractor', 'optical_length': 0, 'mass': 1500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TeleVue_TV_85': {'brand': 'TeleVue', 'name': 'TV-85', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TeleVue_TV_102': {'brand': 'TeleVue', 'name': 'TV-102', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TeleVue_TV_NP127is': {'brand': 'TeleVue', 'name': 'TV-NP127is', 'type': 'type_refractor', 'optical_length': 0, 'mass': 6800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TeleVue_TV_NP101': {'brand': 'TeleVue', 'name': 'TV-NP101', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def TeleVue_NP101is(cls):
        return cls.from_database(cls._DATABASE['TeleVue_NP101is'])

    @classmethod
    def TeleVue_NP127fli(cls):
        return cls.from_database(cls._DATABASE['TeleVue_NP127fli'])

    @classmethod
    def TeleVue_TV_60(cls):
        return cls.from_database(cls._DATABASE['TeleVue_TV_60'])

    @classmethod
    def TeleVue_TV_76(cls):
        return cls.from_database(cls._DATABASE['TeleVue_TV_76'])

    @classmethod
    def TeleVue_TV_85(cls):
        return cls.from_database(cls._DATABASE['TeleVue_TV_85'])

    @classmethod
    def TeleVue_TV_102(cls):
        return cls.from_database(cls._DATABASE['TeleVue_TV_102'])

    @classmethod
    def TeleVue_TV_NP127is(cls):
        return cls.from_database(cls._DATABASE['TeleVue_TV_NP127is'])

    @classmethod
    def TeleVue_TV_NP101(cls):
        return cls.from_database(cls._DATABASE['TeleVue_TV_NP101'])