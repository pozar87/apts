import numpy
from ...abstract import OpticalEquipment
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ....constants import GraphConstants
from enum import Enum
from typing import Optional
from ..base import TelescopeType, TubeMaterial, Telescope

class MeadeTelescope(Telescope):
    _DATABASE = {'Meade_LX85_ACF_6': {'brand': 'Meade', 'name': 'LX85 ACF 6"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 4200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meade_LX85_ACF_8': {'brand': 'Meade', 'name': 'LX85 ACF 8"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 5700, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meade_LX200_ACF_8': {'brand': 'Meade', 'name': 'LX200 ACF 8"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 6000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meade_LX200_ACF_10': {'brand': 'Meade', 'name': 'LX200 ACF 10"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 11000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meade_LX200_ACF_12': {'brand': 'Meade', 'name': 'LX200 ACF 12"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 14000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meade_LX200_ACF_14': {'brand': 'Meade', 'name': 'LX200 ACF 14"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 18000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meade_LX200_ACF_16': {'brand': 'Meade', 'name': 'LX200 ACF 16"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 26000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meade_LX600_ACF_10': {'brand': 'Meade', 'name': 'LX600 ACF 10"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 11500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meade_LX600_ACF_12': {'brand': 'Meade', 'name': 'LX600 ACF 12"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 15000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meade_LX600_ACF_14': {'brand': 'Meade', 'name': 'LX600 ACF 14"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 22000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meade_ETX_90': {'brand': 'Meade', 'name': 'ETX-90', 'type': 'type_telescope', 'optical_length': 0, 'mass': 1500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meade_ETX_125': {'brand': 'Meade', 'name': 'ETX-125', 'type': 'type_telescope', 'optical_length': 0, 'mass': 3000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meade_LightBridge_10_Dob': {'brand': 'Meade', 'name': 'LightBridge 10" Dob', 'type': 'type_telescope', 'optical_length': 0, 'mass': 10000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meade_LightBridge_12_Dob': {'brand': 'Meade', 'name': 'LightBridge 12" Dob', 'type': 'type_telescope', 'optical_length': 0, 'mass': 14000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meade_LightBridge_16_Dob': {'brand': 'Meade', 'name': 'LightBridge 16" Dob', 'type': 'type_telescope', 'optical_length': 0, 'mass': 24000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meade_LightBridge_8_Dob': {'brand': 'Meade', 'name': 'LightBridge 8" Dob', 'type': 'type_telescope', 'optical_length': 0, 'mass': 7000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meade_LX90_ACF_8': {'brand': 'Meade', 'name': 'LX90 ACF 8"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 5800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meade_LX90_ACF_10': {'brand': 'Meade', 'name': 'LX90 ACF 10"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 10000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meade_LX90_ACF_12': {'brand': 'Meade', 'name': 'LX90 ACF 12"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 13000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meade_StarNavigator_NG_102mm': {'brand': 'Meade', 'name': 'StarNavigator NG 102mm', 'type': 'type_telescope', 'optical_length': 0, 'mass': 2800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meade_StarNavigator_NG_130mm': {'brand': 'Meade', 'name': 'StarNavigator NG 130mm', 'type': 'type_telescope', 'optical_length': 0, 'mass': 3200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meade_Polaris_127mm_EQ': {'brand': 'Meade', 'name': 'Polaris 127mm EQ', 'type': 'type_telescope', 'optical_length': 0, 'mass': 3600, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meade_Polaris_130mm_EQ': {'brand': 'Meade', 'name': 'Polaris 130mm EQ', 'type': 'type_telescope', 'optical_length': 0, 'mass': 3500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meade_S102_102mm_APO': {'brand': 'Meade', 'name': 'S102 102mm APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meade_S130_130mm_APO': {'brand': 'Meade', 'name': 'S130 130mm APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 7000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meade_ETX_105': {'brand': 'Meade', 'name': 'ETX-105', 'type': 'type_telescope', 'optical_length': 0, 'mass': 3800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meade_ETX_80_AT': {'brand': 'Meade', 'name': 'ETX-80 AT', 'type': 'type_telescope', 'optical_length': 0, 'mass': 1500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meade_Infinity_70mm_AZ': {'brand': 'Meade', 'name': 'Infinity 70mm AZ', 'type': 'type_telescope', 'optical_length': 0, 'mass': 900, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meade_Infinity_80mm_AZ': {'brand': 'Meade', 'name': 'Infinity 80mm AZ', 'type': 'type_telescope', 'optical_length': 0, 'mass': 1200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meade_Infinity_90mm_AZ': {'brand': 'Meade', 'name': 'Infinity 90mm AZ', 'type': 'type_telescope', 'optical_length': 0, 'mass': 1800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meade_Infinity_102mm_AZ': {'brand': 'Meade', 'name': 'Infinity 102mm AZ', 'type': 'type_telescope', 'optical_length': 0, 'mass': 2500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meade_Polaris_114mm_EQ': {'brand': 'Meade', 'name': 'Polaris 114mm EQ', 'type': 'type_telescope', 'optical_length': 0, 'mass': 2400, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meade_Polaris_70mm_EQ': {'brand': 'Meade', 'name': 'Polaris 70mm EQ', 'type': 'type_telescope', 'optical_length': 0, 'mass': 1100, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meade_Polaris_90mm_EQ': {'brand': 'Meade', 'name': 'Polaris 90mm EQ', 'type': 'type_telescope', 'optical_length': 0, 'mass': 1500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meade_Polaris_80mm_EQ': {'brand': 'Meade', 'name': 'Polaris 80mm EQ', 'type': 'type_telescope', 'optical_length': 0, 'mass': 1300, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Meade_LX85_ACF_6(cls):
        return cls.from_database(cls._DATABASE['Meade_LX85_ACF_6'])

    @classmethod
    def Meade_LX85_ACF_8(cls):
        return cls.from_database(cls._DATABASE['Meade_LX85_ACF_8'])

    @classmethod
    def Meade_LX200_ACF_8(cls):
        return cls.from_database(cls._DATABASE['Meade_LX200_ACF_8'])

    @classmethod
    def Meade_LX200_ACF_10(cls):
        return cls.from_database(cls._DATABASE['Meade_LX200_ACF_10'])

    @classmethod
    def Meade_LX200_ACF_12(cls):
        return cls.from_database(cls._DATABASE['Meade_LX200_ACF_12'])

    @classmethod
    def Meade_LX200_ACF_14(cls):
        return cls.from_database(cls._DATABASE['Meade_LX200_ACF_14'])

    @classmethod
    def Meade_LX200_ACF_16(cls):
        return cls.from_database(cls._DATABASE['Meade_LX200_ACF_16'])

    @classmethod
    def Meade_LX600_ACF_10(cls):
        return cls.from_database(cls._DATABASE['Meade_LX600_ACF_10'])

    @classmethod
    def Meade_LX600_ACF_12(cls):
        return cls.from_database(cls._DATABASE['Meade_LX600_ACF_12'])

    @classmethod
    def Meade_LX600_ACF_14(cls):
        return cls.from_database(cls._DATABASE['Meade_LX600_ACF_14'])

    @classmethod
    def Meade_ETX_90(cls):
        return cls.from_database(cls._DATABASE['Meade_ETX_90'])

    @classmethod
    def Meade_ETX_125(cls):
        return cls.from_database(cls._DATABASE['Meade_ETX_125'])

    @classmethod
    def Meade_LightBridge_10_Dob(cls):
        return cls.from_database(cls._DATABASE['Meade_LightBridge_10_Dob'])

    @classmethod
    def Meade_LightBridge_12_Dob(cls):
        return cls.from_database(cls._DATABASE['Meade_LightBridge_12_Dob'])

    @classmethod
    def Meade_LightBridge_16_Dob(cls):
        return cls.from_database(cls._DATABASE['Meade_LightBridge_16_Dob'])

    @classmethod
    def Meade_LightBridge_8_Dob(cls):
        return cls.from_database(cls._DATABASE['Meade_LightBridge_8_Dob'])

    @classmethod
    def Meade_LX90_ACF_8(cls):
        return cls.from_database(cls._DATABASE['Meade_LX90_ACF_8'])

    @classmethod
    def Meade_LX90_ACF_10(cls):
        return cls.from_database(cls._DATABASE['Meade_LX90_ACF_10'])

    @classmethod
    def Meade_LX90_ACF_12(cls):
        return cls.from_database(cls._DATABASE['Meade_LX90_ACF_12'])

    @classmethod
    def Meade_StarNavigator_NG_102mm(cls):
        return cls.from_database(cls._DATABASE['Meade_StarNavigator_NG_102mm'])

    @classmethod
    def Meade_StarNavigator_NG_130mm(cls):
        return cls.from_database(cls._DATABASE['Meade_StarNavigator_NG_130mm'])

    @classmethod
    def Meade_Polaris_127mm_EQ(cls):
        return cls.from_database(cls._DATABASE['Meade_Polaris_127mm_EQ'])

    @classmethod
    def Meade_Polaris_130mm_EQ(cls):
        return cls.from_database(cls._DATABASE['Meade_Polaris_130mm_EQ'])

    @classmethod
    def Meade_S102_102mm_APO(cls):
        return cls.from_database(cls._DATABASE['Meade_S102_102mm_APO'])

    @classmethod
    def Meade_S130_130mm_APO(cls):
        return cls.from_database(cls._DATABASE['Meade_S130_130mm_APO'])

    @classmethod
    def Meade_ETX_105(cls):
        return cls.from_database(cls._DATABASE['Meade_ETX_105'])

    @classmethod
    def Meade_ETX_80_AT(cls):
        return cls.from_database(cls._DATABASE['Meade_ETX_80_AT'])

    @classmethod
    def Meade_Infinity_70mm_AZ(cls):
        return cls.from_database(cls._DATABASE['Meade_Infinity_70mm_AZ'])

    @classmethod
    def Meade_Infinity_80mm_AZ(cls):
        return cls.from_database(cls._DATABASE['Meade_Infinity_80mm_AZ'])

    @classmethod
    def Meade_Infinity_90mm_AZ(cls):
        return cls.from_database(cls._DATABASE['Meade_Infinity_90mm_AZ'])

    @classmethod
    def Meade_Infinity_102mm_AZ(cls):
        return cls.from_database(cls._DATABASE['Meade_Infinity_102mm_AZ'])

    @classmethod
    def Meade_Polaris_114mm_EQ(cls):
        return cls.from_database(cls._DATABASE['Meade_Polaris_114mm_EQ'])

    @classmethod
    def Meade_Polaris_70mm_EQ(cls):
        return cls.from_database(cls._DATABASE['Meade_Polaris_70mm_EQ'])

    @classmethod
    def Meade_Polaris_90mm_EQ(cls):
        return cls.from_database(cls._DATABASE['Meade_Polaris_90mm_EQ'])

    @classmethod
    def Meade_Polaris_80mm_EQ(cls):
        return cls.from_database(cls._DATABASE['Meade_Polaris_80mm_EQ'])