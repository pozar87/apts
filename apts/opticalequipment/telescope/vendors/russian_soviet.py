import numpy
from ...abstract import OpticalEquipment
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ....constants import GraphConstants
from enum import Enum
from typing import Optional
from ..base import TelescopeType, TubeMaterial, Telescope

class Russian_sovietTelescope(Telescope):
    _DATABASE = {'Russian_Soviet_Jupiter_37A_135mm_f_3_5': {'brand': 'Russian/Soviet', 'name': 'Jupiter-37A 135mm f/3.5', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 600, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Russian_Soviet_MTO_1000A_1000mm_f_10': {'brand': 'Russian/Soviet', 'name': 'MTO-1000A 1000mm f/10', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 1600, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Russian_Soviet_Helios_44_2_58mm_f_2': {'brand': 'Russian/Soviet', 'name': 'Helios 44-2 58mm f/2', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 230, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Russian_Soviet_Tair_3S_300mm_f_4_5': {'brand': 'Russian/Soviet', 'name': 'Tair-3S 300mm f/4.5', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 700, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Russian_Soviet_Jupiter_37A_135mm_f_3_5(cls):
        return cls.from_database(cls._DATABASE['Russian_Soviet_Jupiter_37A_135mm_f_3_5'])

    @classmethod
    def Russian_Soviet_MTO_1000A_1000mm_f_10(cls):
        return cls.from_database(cls._DATABASE['Russian_Soviet_MTO_1000A_1000mm_f_10'])

    @classmethod
    def Russian_Soviet_Helios_44_2_58mm_f_2(cls):
        return cls.from_database(cls._DATABASE['Russian_Soviet_Helios_44_2_58mm_f_2'])

    @classmethod
    def Russian_Soviet_Tair_3S_300mm_f_4_5(cls):
        return cls.from_database(cls._DATABASE['Russian_Soviet_Tair_3S_300mm_f_4_5'])