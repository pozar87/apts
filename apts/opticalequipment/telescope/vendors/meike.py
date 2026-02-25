import numpy
from ...abstract import OpticalEquipment
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ....constants import GraphConstants
from enum import Enum
from typing import Optional
from ..base import TelescopeType, TubeMaterial, Telescope

class MeikeTelescope(Telescope):
    _DATABASE = {'Meike_85mm_f_1_8_Sony_E': {'brand': 'Meike', 'name': '85mm f/1.8 (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 390, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meike_85mm_f_1_8_Fuji_X': {'brand': 'Meike', 'name': '85mm f/1.8 (Fuji X)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 390, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Fuji X', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meike_85mm_f_1_8_Nikon_Z': {'brand': 'Meike', 'name': '85mm f/1.8 (Nikon Z)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 390, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon Z', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meike_85mm_f_1_8_Canon_RF': {'brand': 'Meike', 'name': '85mm f/1.8 (Canon RF)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 390, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Canon RF', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meike_25mm_f_1_8_Sony_E': {'brand': 'Meike', 'name': '25mm f/1.8 (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 125, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meike_25mm_f_1_8_MFT': {'brand': 'Meike', 'name': '25mm f/1.8 (MFT)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 125, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'MFT', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meike_25mm_f_1_8_Fuji_X': {'brand': 'Meike', 'name': '25mm f/1.8 (Fuji X)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 125, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Fuji X', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meike_50mm_f_1_7_Sony_E': {'brand': 'Meike', 'name': '50mm f/1.7 (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 310, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meike_50mm_f_1_7_Fuji_X': {'brand': 'Meike', 'name': '50mm f/1.7 (Fuji X)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 310, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Fuji X', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meike_35mm_f_1_7_Sony_E': {'brand': 'Meike', 'name': '35mm f/1.7 (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 156, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Meike_6_5mm_f_2_0_Circular_Fisheye_MFT': {'brand': 'Meike', 'name': '6.5mm f/2.0 Circular Fisheye (MFT)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 210, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'MFT', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Meike_85mm_f_1_8_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Meike_85mm_f_1_8_Sony_E'])

    @classmethod
    def Meike_85mm_f_1_8_Fuji_X(cls):
        return cls.from_database(cls._DATABASE['Meike_85mm_f_1_8_Fuji_X'])

    @classmethod
    def Meike_85mm_f_1_8_Nikon_Z(cls):
        return cls.from_database(cls._DATABASE['Meike_85mm_f_1_8_Nikon_Z'])

    @classmethod
    def Meike_85mm_f_1_8_Canon_RF(cls):
        return cls.from_database(cls._DATABASE['Meike_85mm_f_1_8_Canon_RF'])

    @classmethod
    def Meike_25mm_f_1_8_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Meike_25mm_f_1_8_Sony_E'])

    @classmethod
    def Meike_25mm_f_1_8_MFT(cls):
        return cls.from_database(cls._DATABASE['Meike_25mm_f_1_8_MFT'])

    @classmethod
    def Meike_25mm_f_1_8_Fuji_X(cls):
        return cls.from_database(cls._DATABASE['Meike_25mm_f_1_8_Fuji_X'])

    @classmethod
    def Meike_50mm_f_1_7_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Meike_50mm_f_1_7_Sony_E'])

    @classmethod
    def Meike_50mm_f_1_7_Fuji_X(cls):
        return cls.from_database(cls._DATABASE['Meike_50mm_f_1_7_Fuji_X'])

    @classmethod
    def Meike_35mm_f_1_7_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Meike_35mm_f_1_7_Sony_E'])

    @classmethod
    def Meike_6_5mm_f_2_0_Circular_Fisheye_MFT(cls):
        return cls.from_database(cls._DATABASE['Meike_6_5mm_f_2_0_Circular_Fisheye_MFT'])