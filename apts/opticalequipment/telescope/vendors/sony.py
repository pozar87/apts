import numpy
from ...abstract import OpticalEquipment
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ....constants import GraphConstants
from enum import Enum
from typing import Optional
from ..base import TelescopeType, TubeMaterial, Telescope

class SonyTelescope(Telescope):
    _DATABASE = {'Sony_FE_135mm_f_1_8_GM': {'brand': 'Sony', 'name': 'FE 135mm f/1.8 GM', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 950, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sony_FE_200_600mm_f_5_6_6_3_G': {'brand': 'Sony', 'name': 'FE 200-600mm f/5.6-6.3 G', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 2115, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sony_FE_85mm_f_1_4_GM': {'brand': 'Sony', 'name': 'FE 85mm f/1.4 GM', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 820, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sony_FE_50mm_f_1_4_GM': {'brand': 'Sony', 'name': 'FE 50mm f/1.4 GM', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 516, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sony_FE_100_400mm_f_4_5_5_6_GM': {'brand': 'Sony', 'name': 'FE 100-400mm f/4.5-5.6 GM', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 1395, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sony_FE_70_200mm_f_2_8_GM_II': {'brand': 'Sony', 'name': 'FE 70-200mm f/2.8 GM II', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 1045, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sony_FE_200_600mm_f_5_6_6_3_G_OSS': {'brand': 'Sony', 'name': 'FE 200-600mm f/5.6-6.3 G OSS', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 2115, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sony_FE_400mm_f_2_8_GM_OSS': {'brand': 'Sony', 'name': 'FE 400mm f/2.8 GM OSS', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 2895, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sony_FE_600mm_f_4_GM_OSS': {'brand': 'Sony', 'name': 'FE 600mm f/4 GM OSS', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 3040, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sony_FE_70_200mm_f_2_8_GM_OSS_II': {'brand': 'Sony', 'name': 'FE 70-200mm f/2.8 GM OSS II', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 1045, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sony_FE_100_400mm_f_4_5_5_6_GM_OSS': {'brand': 'Sony', 'name': 'FE 100-400mm f/4.5-5.6 GM OSS', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 1395, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sony_FE_50mm_f_1_2_GM': {'brand': 'Sony', 'name': 'FE 50mm f/1.2 GM', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 778, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sony_FE_24_70mm_f_2_8_GM_II': {'brand': 'Sony', 'name': 'FE 24-70mm f/2.8 GM II', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 695, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sony_FE_14mm_f_1_8_GM': {'brand': 'Sony', 'name': 'FE 14mm f/1.8 GM', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 460, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sony_FE_20mm_f_1_8_G': {'brand': 'Sony', 'name': 'FE 20mm f/1.8 G', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 373, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sony_FE_35mm_f_1_4_GM': {'brand': 'Sony', 'name': 'FE 35mm f/1.4 GM', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 524, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sony_FE_300mm_f_2_8_GM_OSS': {'brand': 'Sony', 'name': 'FE 300mm f/2.8 GM OSS', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 2230, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sony_FE_90mm_f_2_8_Macro_G_OSS': {'brand': 'Sony', 'name': 'FE 90mm f/2.8 Macro G OSS', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 602, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sony_FE_50mm_f_2_8_Macro': {'brand': 'Sony', 'name': 'FE 50mm f/2.8 Macro', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 236, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Sony_FE_135mm_f_1_8_GM(cls):
        return cls.from_database(cls._DATABASE['Sony_FE_135mm_f_1_8_GM'])

    @classmethod
    def Sony_FE_200_600mm_f_5_6_6_3_G(cls):
        return cls.from_database(cls._DATABASE['Sony_FE_200_600mm_f_5_6_6_3_G'])

    @classmethod
    def Sony_FE_85mm_f_1_4_GM(cls):
        return cls.from_database(cls._DATABASE['Sony_FE_85mm_f_1_4_GM'])

    @classmethod
    def Sony_FE_50mm_f_1_4_GM(cls):
        return cls.from_database(cls._DATABASE['Sony_FE_50mm_f_1_4_GM'])

    @classmethod
    def Sony_FE_100_400mm_f_4_5_5_6_GM(cls):
        return cls.from_database(cls._DATABASE['Sony_FE_100_400mm_f_4_5_5_6_GM'])

    @classmethod
    def Sony_FE_70_200mm_f_2_8_GM_II(cls):
        return cls.from_database(cls._DATABASE['Sony_FE_70_200mm_f_2_8_GM_II'])

    @classmethod
    def Sony_FE_200_600mm_f_5_6_6_3_G_OSS(cls):
        return cls.from_database(cls._DATABASE['Sony_FE_200_600mm_f_5_6_6_3_G_OSS'])

    @classmethod
    def Sony_FE_400mm_f_2_8_GM_OSS(cls):
        return cls.from_database(cls._DATABASE['Sony_FE_400mm_f_2_8_GM_OSS'])

    @classmethod
    def Sony_FE_600mm_f_4_GM_OSS(cls):
        return cls.from_database(cls._DATABASE['Sony_FE_600mm_f_4_GM_OSS'])

    @classmethod
    def Sony_FE_70_200mm_f_2_8_GM_OSS_II(cls):
        return cls.from_database(cls._DATABASE['Sony_FE_70_200mm_f_2_8_GM_OSS_II'])

    @classmethod
    def Sony_FE_100_400mm_f_4_5_5_6_GM_OSS(cls):
        return cls.from_database(cls._DATABASE['Sony_FE_100_400mm_f_4_5_5_6_GM_OSS'])

    @classmethod
    def Sony_FE_50mm_f_1_2_GM(cls):
        return cls.from_database(cls._DATABASE['Sony_FE_50mm_f_1_2_GM'])

    @classmethod
    def Sony_FE_24_70mm_f_2_8_GM_II(cls):
        return cls.from_database(cls._DATABASE['Sony_FE_24_70mm_f_2_8_GM_II'])

    @classmethod
    def Sony_FE_14mm_f_1_8_GM(cls):
        return cls.from_database(cls._DATABASE['Sony_FE_14mm_f_1_8_GM'])

    @classmethod
    def Sony_FE_20mm_f_1_8_G(cls):
        return cls.from_database(cls._DATABASE['Sony_FE_20mm_f_1_8_G'])

    @classmethod
    def Sony_FE_35mm_f_1_4_GM(cls):
        return cls.from_database(cls._DATABASE['Sony_FE_35mm_f_1_4_GM'])

    @classmethod
    def Sony_FE_300mm_f_2_8_GM_OSS(cls):
        return cls.from_database(cls._DATABASE['Sony_FE_300mm_f_2_8_GM_OSS'])

    @classmethod
    def Sony_FE_90mm_f_2_8_Macro_G_OSS(cls):
        return cls.from_database(cls._DATABASE['Sony_FE_90mm_f_2_8_Macro_G_OSS'])

    @classmethod
    def Sony_FE_50mm_f_2_8_Macro(cls):
        return cls.from_database(cls._DATABASE['Sony_FE_50mm_f_2_8_Macro'])