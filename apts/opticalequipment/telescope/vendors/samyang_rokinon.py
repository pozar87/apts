import numpy
from ...abstract import OpticalEquipment
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ....constants import GraphConstants
from enum import Enum
from typing import Optional
from ..base import TelescopeType, TubeMaterial, Telescope

class Samyang_rokinonTelescope(Telescope):
    _DATABASE = {'Samyang_Rokinon_135mm_f_2_0_ED_UMC': {'brand': 'Samyang/Rokinon', 'name': '135mm f/2.0 ED UMC', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 730, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Samyang_Rokinon_85mm_f_1_4_UMC': {'brand': 'Samyang/Rokinon', 'name': '85mm f/1.4 UMC', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 530, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Samyang_Rokinon_14mm_f_2_8_ED_UMC': {'brand': 'Samyang/Rokinon', 'name': '14mm f/2.8 ED UMC', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 550, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Samyang_Rokinon_24mm_f_1_4_ED_UMC': {'brand': 'Samyang/Rokinon', 'name': '24mm f/1.4 ED UMC', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 680, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Samyang_Rokinon_135mm_f_2_0_Canon_RF': {'brand': 'Samyang/Rokinon', 'name': '135mm f/2.0 (Canon RF)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 730, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Canon RF', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Samyang_Rokinon_135mm_f_2_0_Sony_E': {'brand': 'Samyang/Rokinon', 'name': '135mm f/2.0 (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 730, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Samyang_Rokinon_135mm_f_2_0_Nikon_Z': {'brand': 'Samyang/Rokinon', 'name': '135mm f/2.0 (Nikon Z)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 730, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon Z', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Samyang_Rokinon_135mm_f_2_0_Nikon_F': {'brand': 'Samyang/Rokinon', 'name': '135mm f/2.0 (Nikon F)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 730, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Samyang_Rokinon_85mm_f_1_4_EOS': {'brand': 'Samyang/Rokinon', 'name': '85mm f/1.4 (EOS)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 530, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Samyang_Rokinon_85mm_f_1_4_Sony_E': {'brand': 'Samyang/Rokinon', 'name': '85mm f/1.4 (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 530, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Samyang_Rokinon_85mm_f_1_4_Nikon_F': {'brand': 'Samyang/Rokinon', 'name': '85mm f/1.4 (Nikon F)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 530, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Samyang_Rokinon_14mm_f_2_8_Sony_E': {'brand': 'Samyang/Rokinon', 'name': '14mm f/2.8 (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 550, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Samyang_Rokinon_14mm_f_2_8_Nikon_F': {'brand': 'Samyang/Rokinon', 'name': '14mm f/2.8 (Nikon F)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 550, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Samyang_Rokinon_24mm_f_1_4_Sony_E': {'brand': 'Samyang/Rokinon', 'name': '24mm f/1.4 (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 680, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Samyang_Rokinon_24mm_f_1_4_Nikon_F': {'brand': 'Samyang/Rokinon', 'name': '24mm f/1.4 (Nikon F)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 680, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Samyang_Rokinon_50mm_f_1_4_EOS': {'brand': 'Samyang/Rokinon', 'name': '50mm f/1.4 (EOS)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 550, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Samyang_Rokinon_50mm_f_1_4_Sony_E': {'brand': 'Samyang/Rokinon', 'name': '50mm f/1.4 (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 550, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Samyang_Rokinon_12mm_f_2_0_Sony_E': {'brand': 'Samyang/Rokinon', 'name': '12mm f/2.0 (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 260, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Samyang_Rokinon_12mm_f_2_0_MFT': {'brand': 'Samyang/Rokinon', 'name': '12mm f/2.0 (MFT)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 260, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'MFT', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Samyang_Rokinon_12mm_f_2_0_Fuji_X': {'brand': 'Samyang/Rokinon', 'name': '12mm f/2.0 (Fuji X)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 260, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Fuji X', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Samyang_Rokinon_8mm_f_3_5_Fisheye_EOS': {'brand': 'Samyang/Rokinon', 'name': '8mm f/3.5 Fisheye (EOS)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 435, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Samyang_Rokinon_8mm_f_3_5_Fisheye_Nikon_F': {'brand': 'Samyang/Rokinon', 'name': '8mm f/3.5 Fisheye (Nikon F)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 435, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Samyang_Rokinon_35mm_f_1_4_EOS': {'brand': 'Samyang/Rokinon', 'name': '35mm f/1.4 (EOS)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 660, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Samyang_Rokinon_35mm_f_1_4_Sony_E': {'brand': 'Samyang/Rokinon', 'name': '35mm f/1.4 (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 660, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Samyang_Rokinon_100mm_f_2_8_Macro_EOS': {'brand': 'Samyang/Rokinon', 'name': '100mm f/2.8 Macro (EOS)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 720, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Samyang_Rokinon_135mm_f_2_0_ED_UMC(cls):
        return cls.from_database(cls._DATABASE['Samyang_Rokinon_135mm_f_2_0_ED_UMC'])

    @classmethod
    def Samyang_Rokinon_85mm_f_1_4_UMC(cls):
        return cls.from_database(cls._DATABASE['Samyang_Rokinon_85mm_f_1_4_UMC'])

    @classmethod
    def Samyang_Rokinon_14mm_f_2_8_ED_UMC(cls):
        return cls.from_database(cls._DATABASE['Samyang_Rokinon_14mm_f_2_8_ED_UMC'])

    @classmethod
    def Samyang_Rokinon_24mm_f_1_4_ED_UMC(cls):
        return cls.from_database(cls._DATABASE['Samyang_Rokinon_24mm_f_1_4_ED_UMC'])

    @classmethod
    def Samyang_Rokinon_135mm_f_2_0_Canon_RF(cls):
        return cls.from_database(cls._DATABASE['Samyang_Rokinon_135mm_f_2_0_Canon_RF'])

    @classmethod
    def Samyang_Rokinon_135mm_f_2_0_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Samyang_Rokinon_135mm_f_2_0_Sony_E'])

    @classmethod
    def Samyang_Rokinon_135mm_f_2_0_Nikon_Z(cls):
        return cls.from_database(cls._DATABASE['Samyang_Rokinon_135mm_f_2_0_Nikon_Z'])

    @classmethod
    def Samyang_Rokinon_135mm_f_2_0_Nikon_F(cls):
        return cls.from_database(cls._DATABASE['Samyang_Rokinon_135mm_f_2_0_Nikon_F'])

    @classmethod
    def Samyang_Rokinon_85mm_f_1_4_EOS(cls):
        return cls.from_database(cls._DATABASE['Samyang_Rokinon_85mm_f_1_4_EOS'])

    @classmethod
    def Samyang_Rokinon_85mm_f_1_4_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Samyang_Rokinon_85mm_f_1_4_Sony_E'])

    @classmethod
    def Samyang_Rokinon_85mm_f_1_4_Nikon_F(cls):
        return cls.from_database(cls._DATABASE['Samyang_Rokinon_85mm_f_1_4_Nikon_F'])

    @classmethod
    def Samyang_Rokinon_14mm_f_2_8_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Samyang_Rokinon_14mm_f_2_8_Sony_E'])

    @classmethod
    def Samyang_Rokinon_14mm_f_2_8_Nikon_F(cls):
        return cls.from_database(cls._DATABASE['Samyang_Rokinon_14mm_f_2_8_Nikon_F'])

    @classmethod
    def Samyang_Rokinon_24mm_f_1_4_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Samyang_Rokinon_24mm_f_1_4_Sony_E'])

    @classmethod
    def Samyang_Rokinon_24mm_f_1_4_Nikon_F(cls):
        return cls.from_database(cls._DATABASE['Samyang_Rokinon_24mm_f_1_4_Nikon_F'])

    @classmethod
    def Samyang_Rokinon_50mm_f_1_4_EOS(cls):
        return cls.from_database(cls._DATABASE['Samyang_Rokinon_50mm_f_1_4_EOS'])

    @classmethod
    def Samyang_Rokinon_50mm_f_1_4_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Samyang_Rokinon_50mm_f_1_4_Sony_E'])

    @classmethod
    def Samyang_Rokinon_12mm_f_2_0_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Samyang_Rokinon_12mm_f_2_0_Sony_E'])

    @classmethod
    def Samyang_Rokinon_12mm_f_2_0_MFT(cls):
        return cls.from_database(cls._DATABASE['Samyang_Rokinon_12mm_f_2_0_MFT'])

    @classmethod
    def Samyang_Rokinon_12mm_f_2_0_Fuji_X(cls):
        return cls.from_database(cls._DATABASE['Samyang_Rokinon_12mm_f_2_0_Fuji_X'])

    @classmethod
    def Samyang_Rokinon_8mm_f_3_5_Fisheye_EOS(cls):
        return cls.from_database(cls._DATABASE['Samyang_Rokinon_8mm_f_3_5_Fisheye_EOS'])

    @classmethod
    def Samyang_Rokinon_8mm_f_3_5_Fisheye_Nikon_F(cls):
        return cls.from_database(cls._DATABASE['Samyang_Rokinon_8mm_f_3_5_Fisheye_Nikon_F'])

    @classmethod
    def Samyang_Rokinon_35mm_f_1_4_EOS(cls):
        return cls.from_database(cls._DATABASE['Samyang_Rokinon_35mm_f_1_4_EOS'])

    @classmethod
    def Samyang_Rokinon_35mm_f_1_4_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Samyang_Rokinon_35mm_f_1_4_Sony_E'])

    @classmethod
    def Samyang_Rokinon_100mm_f_2_8_Macro_EOS(cls):
        return cls.from_database(cls._DATABASE['Samyang_Rokinon_100mm_f_2_8_Macro_EOS'])