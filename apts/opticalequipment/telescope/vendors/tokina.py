import numpy
from ...abstract import OpticalEquipment
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ....constants import GraphConstants
from enum import Enum
from typing import Optional
from ..base import TelescopeType, TubeMaterial, Telescope

class TokinaTelescope(Telescope):
    _DATABASE = {'Tokina_opera_50mm_f_1_4_Canon': {'brand': 'Tokina', 'name': 'opera 50mm f/1.4 (Canon)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 950, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Tokina_opera_50mm_f_1_4_Nikon': {'brand': 'Tokina', 'name': 'opera 50mm f/1.4 (Nikon)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 950, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Tokina_ATX_i_11_16mm_f_2_8_Canon': {'brand': 'Tokina', 'name': 'ATX-i 11-16mm f/2.8 (Canon)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 555, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Tokina_ATX_i_11_16mm_f_2_8_Nikon': {'brand': 'Tokina', 'name': 'ATX-i 11-16mm f/2.8 (Nikon)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 555, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Tokina_SZ_500mm_f_8_Reflex_MF': {'brand': 'Tokina', 'name': 'SZ 500mm f/8 Reflex (MF)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 530, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Tokina_opera_50mm_f_1_4_EOS': {'brand': 'Tokina', 'name': 'opera 50mm f/1.4 (EOS)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 950, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Tokina_opera_50mm_f_1_4_Nikon_F': {'brand': 'Tokina', 'name': 'opera 50mm f/1.4 (Nikon F)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 950, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Tokina_AT_X_11_20mm_f_2_8_EOS': {'brand': 'Tokina', 'name': 'AT-X 11-20mm f/2.8 (EOS)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 560, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Tokina_AT_X_11_20mm_f_2_8_Nikon_F': {'brand': 'Tokina', 'name': 'AT-X 11-20mm f/2.8 (Nikon F)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 560, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Tokina_AT_X_14_20mm_f_2_EOS': {'brand': 'Tokina', 'name': 'AT-X 14-20mm f/2 (EOS)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 735, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Tokina_AT_X_14_20mm_f_2_Nikon_F': {'brand': 'Tokina', 'name': 'AT-X 14-20mm f/2 (Nikon F)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 735, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Tokina_SZX_400mm_f_8_Reflex': {'brand': 'Tokina', 'name': 'SZX 400mm f/8 Reflex', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 355, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Tokina_SZ_500mm_f_8_Reflex_Sony_E': {'brand': 'Tokina', 'name': 'SZ 500mm f/8 Reflex (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 380, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Tokina_atx_m_85mm_f_1_8_Sony_E': {'brand': 'Tokina', 'name': 'atx-m 85mm f/1.8 (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 645, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Tokina_atx_m_33mm_f_1_4_Fuji_X': {'brand': 'Tokina', 'name': 'atx-m 33mm f/1.4 (Fuji X)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 285, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Fuji X', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Tokina_atx_m_23mm_f_1_4_Fuji_X': {'brand': 'Tokina', 'name': 'atx-m 23mm f/1.4 (Fuji X)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 263, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Fuji X', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Tokina_ATX_i_100mm_f_2_8_Macro_EOS': {'brand': 'Tokina', 'name': 'ATX-i 100mm f/2.8 Macro (EOS)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 515, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Tokina_opera_50mm_f_1_4_Canon(cls):
        return cls.from_database(cls._DATABASE['Tokina_opera_50mm_f_1_4_Canon'])

    @classmethod
    def Tokina_opera_50mm_f_1_4_Nikon(cls):
        return cls.from_database(cls._DATABASE['Tokina_opera_50mm_f_1_4_Nikon'])

    @classmethod
    def Tokina_ATX_i_11_16mm_f_2_8_Canon(cls):
        return cls.from_database(cls._DATABASE['Tokina_ATX_i_11_16mm_f_2_8_Canon'])

    @classmethod
    def Tokina_ATX_i_11_16mm_f_2_8_Nikon(cls):
        return cls.from_database(cls._DATABASE['Tokina_ATX_i_11_16mm_f_2_8_Nikon'])

    @classmethod
    def Tokina_SZ_500mm_f_8_Reflex_MF(cls):
        return cls.from_database(cls._DATABASE['Tokina_SZ_500mm_f_8_Reflex_MF'])

    @classmethod
    def Tokina_opera_50mm_f_1_4_EOS(cls):
        return cls.from_database(cls._DATABASE['Tokina_opera_50mm_f_1_4_EOS'])

    @classmethod
    def Tokina_opera_50mm_f_1_4_Nikon_F(cls):
        return cls.from_database(cls._DATABASE['Tokina_opera_50mm_f_1_4_Nikon_F'])

    @classmethod
    def Tokina_AT_X_11_20mm_f_2_8_EOS(cls):
        return cls.from_database(cls._DATABASE['Tokina_AT_X_11_20mm_f_2_8_EOS'])

    @classmethod
    def Tokina_AT_X_11_20mm_f_2_8_Nikon_F(cls):
        return cls.from_database(cls._DATABASE['Tokina_AT_X_11_20mm_f_2_8_Nikon_F'])

    @classmethod
    def Tokina_AT_X_14_20mm_f_2_EOS(cls):
        return cls.from_database(cls._DATABASE['Tokina_AT_X_14_20mm_f_2_EOS'])

    @classmethod
    def Tokina_AT_X_14_20mm_f_2_Nikon_F(cls):
        return cls.from_database(cls._DATABASE['Tokina_AT_X_14_20mm_f_2_Nikon_F'])

    @classmethod
    def Tokina_SZX_400mm_f_8_Reflex(cls):
        return cls.from_database(cls._DATABASE['Tokina_SZX_400mm_f_8_Reflex'])

    @classmethod
    def Tokina_SZ_500mm_f_8_Reflex_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Tokina_SZ_500mm_f_8_Reflex_Sony_E'])

    @classmethod
    def Tokina_atx_m_85mm_f_1_8_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Tokina_atx_m_85mm_f_1_8_Sony_E'])

    @classmethod
    def Tokina_atx_m_33mm_f_1_4_Fuji_X(cls):
        return cls.from_database(cls._DATABASE['Tokina_atx_m_33mm_f_1_4_Fuji_X'])

    @classmethod
    def Tokina_atx_m_23mm_f_1_4_Fuji_X(cls):
        return cls.from_database(cls._DATABASE['Tokina_atx_m_23mm_f_1_4_Fuji_X'])

    @classmethod
    def Tokina_ATX_i_100mm_f_2_8_Macro_EOS(cls):
        return cls.from_database(cls._DATABASE['Tokina_ATX_i_100mm_f_2_8_Macro_EOS'])