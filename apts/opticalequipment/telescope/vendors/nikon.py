import numpy
from ...abstract import OpticalEquipment
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ....constants import GraphConstants
from enum import Enum
from typing import Optional
from ..base import TelescopeType, TubeMaterial, Telescope

class NikonTelescope(Telescope):
    _DATABASE = {'Nikon_AF_S_200mm_f_2G_ED_VR': {'brand': 'Nikon', 'name': 'AF-S 200mm f/2G ED VR', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 2930, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Nikon_AF_S_105mm_f_1_4E_ED': {'brand': 'Nikon', 'name': 'AF-S 105mm f/1.4E ED', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 985, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Nikon_AF_S_50mm_f_1_8G': {'brand': 'Nikon', 'name': 'AF-S 50mm f/1.8G', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 185, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Nikon_AF_S_85mm_f_1_8G': {'brand': 'Nikon', 'name': 'AF-S 85mm f/1.8G', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 350, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Nikon_AF_S_300mm_f_4E_PF_ED_VR': {'brand': 'Nikon', 'name': 'AF-S 300mm f/4E PF ED VR', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 755, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Nikon_AF_S_70_200mm_f_2_8E_FL_ED_VR': {'brand': 'Nikon', 'name': 'AF-S 70-200mm f/2.8E FL ED VR', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 1430, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Nikon_Z_135mm_f_1_8_S_Plena': {'brand': 'Nikon', 'name': 'Z 135mm f/1.8 S Plena', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 995, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon Z', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Nikon_Z_50mm_f_1_8_S': {'brand': 'Nikon', 'name': 'Z 50mm f/1.8 S', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 415, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon Z', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Nikon_Z_85mm_f_1_8_S': {'brand': 'Nikon', 'name': 'Z 85mm f/1.8 S', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 470, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon Z', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Nikon_Z_200_600mm_f_5_6_6_3_VR': {'brand': 'Nikon', 'name': 'Z 200-600mm f/5.6-6.3 VR', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 2115, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon Z', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Nikon_Z_100_400mm_f_4_5_5_6_VR_S': {'brand': 'Nikon', 'name': 'Z 100-400mm f/4.5-5.6 VR S', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 1355, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon Z', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Nikon_AF_S_200mm_f_2G_ED_VR_II': {'brand': 'Nikon', 'name': 'AF-S 200mm f/2G ED VR II', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 2930, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Nikon_AF_S_300mm_f_2_8G_ED_VR_II': {'brand': 'Nikon', 'name': 'AF-S 300mm f/2.8G ED VR II', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 2870, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Nikon_AF_S_500mm_f_4E_FL_ED_VR': {'brand': 'Nikon', 'name': 'AF-S 500mm f/4E FL ED VR', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 3090, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Nikon_AF_S_600mm_f_4E_FL_ED_VR': {'brand': 'Nikon', 'name': 'AF-S 600mm f/4E FL ED VR', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 3810, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Nikon_AF_S_85mm_f_1_4G': {'brand': 'Nikon', 'name': 'AF-S 85mm f/1.4G', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 595, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Nikon_AF_S_50mm_f_1_4G': {'brand': 'Nikon', 'name': 'AF-S 50mm f/1.4G', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 280, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Nikon_AF_S_14_24mm_f_2_8G_ED': {'brand': 'Nikon', 'name': 'AF-S 14-24mm f/2.8G ED', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 970, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Nikon_AF_S_24_70mm_f_2_8E_ED_VR': {'brand': 'Nikon', 'name': 'AF-S 24-70mm f/2.8E ED VR', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 1070, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Nikon_AF_S_180_400mm_f_4E_TC': {'brand': 'Nikon', 'name': 'AF-S 180-400mm f/4E TC', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 3500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Nikon_AF_S_200_500mm_f_5_6E_ED_VR': {'brand': 'Nikon', 'name': 'AF-S 200-500mm f/5.6E ED VR', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 2300, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Nikon_Z_50mm_f_1_2_S': {'brand': 'Nikon', 'name': 'Z 50mm f/1.2 S', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 1090, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon Z', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Nikon_Z_85mm_f_1_2_S': {'brand': 'Nikon', 'name': 'Z 85mm f/1.2 S', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 1160, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon Z', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Nikon_Z_400mm_f_4_5_VR_S': {'brand': 'Nikon', 'name': 'Z 400mm f/4.5 VR S', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 1245, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon Z', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Nikon_Z_600mm_f_4_TC_VR_S': {'brand': 'Nikon', 'name': 'Z 600mm f/4 TC VR S', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 3260, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon Z', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Nikon_Z_800mm_f_6_3_VR_S': {'brand': 'Nikon', 'name': 'Z 800mm f/6.3 VR S', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 2385, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon Z', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Nikon_Z_70_200mm_f_2_8_VR_S': {'brand': 'Nikon', 'name': 'Z 70-200mm f/2.8 VR S', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 1360, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon Z', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Nikon_Z_24_70mm_f_2_8_S': {'brand': 'Nikon', 'name': 'Z 24-70mm f/2.8 S', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 805, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon Z', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Nikon_Z_14_24mm_f_2_8_S': {'brand': 'Nikon', 'name': 'Z 14-24mm f/2.8 S', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 650, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon Z', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Nikon_Z_180_600mm_f_5_6_6_3_VR': {'brand': 'Nikon', 'name': 'Z 180-600mm f/5.6-6.3 VR', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 1955, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon Z', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Nikon_Z_MC_105mm_f_2_8_VR_S': {'brand': 'Nikon', 'name': 'Z MC 105mm f/2.8 VR S', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 630, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon Z', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Nikon_Z_MC_50mm_f_2_8': {'brand': 'Nikon', 'name': 'Z MC 50mm f/2.8', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 260, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon Z', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Nikon_AF_S_Micro_105mm_f_2_8G_VR': {'brand': 'Nikon', 'name': 'AF-S Micro 105mm f/2.8G VR', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 720, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Nikon_AF_S_200mm_f_2G_ED_VR(cls):
        return cls.from_database(cls._DATABASE['Nikon_AF_S_200mm_f_2G_ED_VR'])

    @classmethod
    def Nikon_AF_S_105mm_f_1_4E_ED(cls):
        return cls.from_database(cls._DATABASE['Nikon_AF_S_105mm_f_1_4E_ED'])

    @classmethod
    def Nikon_AF_S_50mm_f_1_8G(cls):
        return cls.from_database(cls._DATABASE['Nikon_AF_S_50mm_f_1_8G'])

    @classmethod
    def Nikon_AF_S_85mm_f_1_8G(cls):
        return cls.from_database(cls._DATABASE['Nikon_AF_S_85mm_f_1_8G'])

    @classmethod
    def Nikon_AF_S_300mm_f_4E_PF_ED_VR(cls):
        return cls.from_database(cls._DATABASE['Nikon_AF_S_300mm_f_4E_PF_ED_VR'])

    @classmethod
    def Nikon_AF_S_70_200mm_f_2_8E_FL_ED_VR(cls):
        return cls.from_database(cls._DATABASE['Nikon_AF_S_70_200mm_f_2_8E_FL_ED_VR'])

    @classmethod
    def Nikon_Z_135mm_f_1_8_S_Plena(cls):
        return cls.from_database(cls._DATABASE['Nikon_Z_135mm_f_1_8_S_Plena'])

    @classmethod
    def Nikon_Z_50mm_f_1_8_S(cls):
        return cls.from_database(cls._DATABASE['Nikon_Z_50mm_f_1_8_S'])

    @classmethod
    def Nikon_Z_85mm_f_1_8_S(cls):
        return cls.from_database(cls._DATABASE['Nikon_Z_85mm_f_1_8_S'])

    @classmethod
    def Nikon_Z_200_600mm_f_5_6_6_3_VR(cls):
        return cls.from_database(cls._DATABASE['Nikon_Z_200_600mm_f_5_6_6_3_VR'])

    @classmethod
    def Nikon_Z_100_400mm_f_4_5_5_6_VR_S(cls):
        return cls.from_database(cls._DATABASE['Nikon_Z_100_400mm_f_4_5_5_6_VR_S'])

    @classmethod
    def Nikon_AF_S_200mm_f_2G_ED_VR_II(cls):
        return cls.from_database(cls._DATABASE['Nikon_AF_S_200mm_f_2G_ED_VR_II'])

    @classmethod
    def Nikon_AF_S_300mm_f_2_8G_ED_VR_II(cls):
        return cls.from_database(cls._DATABASE['Nikon_AF_S_300mm_f_2_8G_ED_VR_II'])

    @classmethod
    def Nikon_AF_S_500mm_f_4E_FL_ED_VR(cls):
        return cls.from_database(cls._DATABASE['Nikon_AF_S_500mm_f_4E_FL_ED_VR'])

    @classmethod
    def Nikon_AF_S_600mm_f_4E_FL_ED_VR(cls):
        return cls.from_database(cls._DATABASE['Nikon_AF_S_600mm_f_4E_FL_ED_VR'])

    @classmethod
    def Nikon_AF_S_85mm_f_1_4G(cls):
        return cls.from_database(cls._DATABASE['Nikon_AF_S_85mm_f_1_4G'])

    @classmethod
    def Nikon_AF_S_50mm_f_1_4G(cls):
        return cls.from_database(cls._DATABASE['Nikon_AF_S_50mm_f_1_4G'])

    @classmethod
    def Nikon_AF_S_14_24mm_f_2_8G_ED(cls):
        return cls.from_database(cls._DATABASE['Nikon_AF_S_14_24mm_f_2_8G_ED'])

    @classmethod
    def Nikon_AF_S_24_70mm_f_2_8E_ED_VR(cls):
        return cls.from_database(cls._DATABASE['Nikon_AF_S_24_70mm_f_2_8E_ED_VR'])

    @classmethod
    def Nikon_AF_S_180_400mm_f_4E_TC(cls):
        return cls.from_database(cls._DATABASE['Nikon_AF_S_180_400mm_f_4E_TC'])

    @classmethod
    def Nikon_AF_S_200_500mm_f_5_6E_ED_VR(cls):
        return cls.from_database(cls._DATABASE['Nikon_AF_S_200_500mm_f_5_6E_ED_VR'])

    @classmethod
    def Nikon_Z_50mm_f_1_2_S(cls):
        return cls.from_database(cls._DATABASE['Nikon_Z_50mm_f_1_2_S'])

    @classmethod
    def Nikon_Z_85mm_f_1_2_S(cls):
        return cls.from_database(cls._DATABASE['Nikon_Z_85mm_f_1_2_S'])

    @classmethod
    def Nikon_Z_400mm_f_4_5_VR_S(cls):
        return cls.from_database(cls._DATABASE['Nikon_Z_400mm_f_4_5_VR_S'])

    @classmethod
    def Nikon_Z_600mm_f_4_TC_VR_S(cls):
        return cls.from_database(cls._DATABASE['Nikon_Z_600mm_f_4_TC_VR_S'])

    @classmethod
    def Nikon_Z_800mm_f_6_3_VR_S(cls):
        return cls.from_database(cls._DATABASE['Nikon_Z_800mm_f_6_3_VR_S'])

    @classmethod
    def Nikon_Z_70_200mm_f_2_8_VR_S(cls):
        return cls.from_database(cls._DATABASE['Nikon_Z_70_200mm_f_2_8_VR_S'])

    @classmethod
    def Nikon_Z_24_70mm_f_2_8_S(cls):
        return cls.from_database(cls._DATABASE['Nikon_Z_24_70mm_f_2_8_S'])

    @classmethod
    def Nikon_Z_14_24mm_f_2_8_S(cls):
        return cls.from_database(cls._DATABASE['Nikon_Z_14_24mm_f_2_8_S'])

    @classmethod
    def Nikon_Z_180_600mm_f_5_6_6_3_VR(cls):
        return cls.from_database(cls._DATABASE['Nikon_Z_180_600mm_f_5_6_6_3_VR'])

    @classmethod
    def Nikon_Z_MC_105mm_f_2_8_VR_S(cls):
        return cls.from_database(cls._DATABASE['Nikon_Z_MC_105mm_f_2_8_VR_S'])

    @classmethod
    def Nikon_Z_MC_50mm_f_2_8(cls):
        return cls.from_database(cls._DATABASE['Nikon_Z_MC_50mm_f_2_8'])

    @classmethod
    def Nikon_AF_S_Micro_105mm_f_2_8G_VR(cls):
        return cls.from_database(cls._DATABASE['Nikon_AF_S_Micro_105mm_f_2_8G_VR'])