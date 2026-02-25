import numpy
from ...abstract import OpticalEquipment
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ....constants import GraphConstants
from enum import Enum
from typing import Optional
from ..base import TelescopeType, TubeMaterial, Telescope

class LaowaTelescope(Telescope):
    _DATABASE = {'Laowa_15mm_f_2_Zero_D_EOS': {'brand': 'Laowa', 'name': '15mm f/2 Zero-D (EOS)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Laowa_15mm_f_2_Zero_D_Sony_E': {'brand': 'Laowa', 'name': '15mm f/2 Zero-D (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Laowa_15mm_f_2_Zero_D_Nikon_Z': {'brand': 'Laowa', 'name': '15mm f/2 Zero-D (Nikon Z)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon Z', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Laowa_15mm_f_2_Zero_D_Canon_RF': {'brand': 'Laowa', 'name': '15mm f/2 Zero-D (Canon RF)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Canon RF', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Laowa_100mm_f_2_8_2_1_Macro_EOS': {'brand': 'Laowa', 'name': '100mm f/2.8 2:1 Macro (EOS)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 638, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Laowa_100mm_f_2_8_2_1_Macro_Sony_E': {'brand': 'Laowa', 'name': '100mm f/2.8 2:1 Macro (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 638, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Laowa_10_18mm_f_4_5_5_6_Sony_E': {'brand': 'Laowa', 'name': '10-18mm f/4.5-5.6 (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 497, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Laowa_10_18mm_f_4_5_5_6_Nikon_Z': {'brand': 'Laowa', 'name': '10-18mm f/4.5-5.6 (Nikon Z)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 497, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon Z', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Laowa_12mm_f_2_8_Zero_D_EOS': {'brand': 'Laowa', 'name': '12mm f/2.8 Zero-D (EOS)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 210, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Laowa_12mm_f_2_8_Zero_D_Sony_E': {'brand': 'Laowa', 'name': '12mm f/2.8 Zero-D (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 210, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Laowa_9mm_f_2_8_Zero_D_MFT': {'brand': 'Laowa', 'name': '9mm f/2.8 Zero-D (MFT)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 215, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'MFT', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Laowa_9mm_f_2_8_Zero_D_Fuji_X': {'brand': 'Laowa', 'name': '9mm f/2.8 Zero-D (Fuji X)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 215, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Fuji X', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Laowa_9mm_f_5_6_FF_RL_Sony_E': {'brand': 'Laowa', 'name': '9mm f/5.6 FF RL (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 350, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Laowa_9mm_f_5_6_FF_RL_Nikon_Z': {'brand': 'Laowa', 'name': '9mm f/5.6 FF RL (Nikon Z)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 350, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon Z', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Laowa_14mm_f_4_Zero_D_Sony_E': {'brand': 'Laowa', 'name': '14mm f/4 Zero-D (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 320, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Laowa_14mm_f_4_Zero_D_Nikon_Z': {'brand': 'Laowa', 'name': '14mm f/4 Zero-D (Nikon Z)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 320, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon Z', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Laowa_24mm_f_14_Probe_EOS': {'brand': 'Laowa', 'name': '24mm f/14 Probe (EOS)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 474, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Laowa_65mm_f_2_8_2x_Macro_Sony_E': {'brand': 'Laowa', 'name': '65mm f/2.8 2x Macro (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 335, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Laowa_85mm_f_5_6_2x_Macro_Sony_E': {'brand': 'Laowa', 'name': '85mm f/5.6 2x Macro (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 247, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Laowa_15mm_f_2_Zero_D_EOS(cls):
        return cls.from_database(cls._DATABASE['Laowa_15mm_f_2_Zero_D_EOS'])

    @classmethod
    def Laowa_15mm_f_2_Zero_D_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Laowa_15mm_f_2_Zero_D_Sony_E'])

    @classmethod
    def Laowa_15mm_f_2_Zero_D_Nikon_Z(cls):
        return cls.from_database(cls._DATABASE['Laowa_15mm_f_2_Zero_D_Nikon_Z'])

    @classmethod
    def Laowa_15mm_f_2_Zero_D_Canon_RF(cls):
        return cls.from_database(cls._DATABASE['Laowa_15mm_f_2_Zero_D_Canon_RF'])

    @classmethod
    def Laowa_100mm_f_2_8_2_1_Macro_EOS(cls):
        return cls.from_database(cls._DATABASE['Laowa_100mm_f_2_8_2_1_Macro_EOS'])

    @classmethod
    def Laowa_100mm_f_2_8_2_1_Macro_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Laowa_100mm_f_2_8_2_1_Macro_Sony_E'])

    @classmethod
    def Laowa_10_18mm_f_4_5_5_6_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Laowa_10_18mm_f_4_5_5_6_Sony_E'])

    @classmethod
    def Laowa_10_18mm_f_4_5_5_6_Nikon_Z(cls):
        return cls.from_database(cls._DATABASE['Laowa_10_18mm_f_4_5_5_6_Nikon_Z'])

    @classmethod
    def Laowa_12mm_f_2_8_Zero_D_EOS(cls):
        return cls.from_database(cls._DATABASE['Laowa_12mm_f_2_8_Zero_D_EOS'])

    @classmethod
    def Laowa_12mm_f_2_8_Zero_D_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Laowa_12mm_f_2_8_Zero_D_Sony_E'])

    @classmethod
    def Laowa_9mm_f_2_8_Zero_D_MFT(cls):
        return cls.from_database(cls._DATABASE['Laowa_9mm_f_2_8_Zero_D_MFT'])

    @classmethod
    def Laowa_9mm_f_2_8_Zero_D_Fuji_X(cls):
        return cls.from_database(cls._DATABASE['Laowa_9mm_f_2_8_Zero_D_Fuji_X'])

    @classmethod
    def Laowa_9mm_f_5_6_FF_RL_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Laowa_9mm_f_5_6_FF_RL_Sony_E'])

    @classmethod
    def Laowa_9mm_f_5_6_FF_RL_Nikon_Z(cls):
        return cls.from_database(cls._DATABASE['Laowa_9mm_f_5_6_FF_RL_Nikon_Z'])

    @classmethod
    def Laowa_14mm_f_4_Zero_D_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Laowa_14mm_f_4_Zero_D_Sony_E'])

    @classmethod
    def Laowa_14mm_f_4_Zero_D_Nikon_Z(cls):
        return cls.from_database(cls._DATABASE['Laowa_14mm_f_4_Zero_D_Nikon_Z'])

    @classmethod
    def Laowa_24mm_f_14_Probe_EOS(cls):
        return cls.from_database(cls._DATABASE['Laowa_24mm_f_14_Probe_EOS'])

    @classmethod
    def Laowa_65mm_f_2_8_2x_Macro_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Laowa_65mm_f_2_8_2x_Macro_Sony_E'])

    @classmethod
    def Laowa_85mm_f_5_6_2x_Macro_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Laowa_85mm_f_5_6_2x_Macro_Sony_E'])