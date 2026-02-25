import numpy
import math
from typing import Any
from ...abstract import OutputOpticalEqipment
from ....constants import GraphConstants, OpticalType
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ..base import Camera

class PanasonicCamera(Camera):
    _DATABASE = {'Panasonic_GH6': {'brand': 'Panasonic', 'name': 'GH6', 'type': 'type_dslr', 'optical_length': 19.25, 'mass': 823, 'tside_thread': 'MFT', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Panasonic_GH5_II': {'brand': 'Panasonic', 'name': 'GH5 II', 'type': 'type_dslr', 'optical_length': 19.25, 'mass': 727, 'tside_thread': 'MFT', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Panasonic_GH5': {'brand': 'Panasonic', 'name': 'GH5', 'type': 'type_dslr', 'optical_length': 19.25, 'mass': 725, 'tside_thread': 'MFT', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Panasonic_G9_II': {'brand': 'Panasonic', 'name': 'G9 II', 'type': 'type_dslr', 'optical_length': 19.25, 'mass': 658, 'tside_thread': 'MFT', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Panasonic_G9': {'brand': 'Panasonic', 'name': 'G9', 'type': 'type_dslr', 'optical_length': 19.25, 'mass': 586, 'tside_thread': 'MFT', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Panasonic_G85': {'brand': 'Panasonic', 'name': 'G85', 'type': 'type_dslr', 'optical_length': 19.25, 'mass': 505, 'tside_thread': 'MFT', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Panasonic_GX85': {'brand': 'Panasonic', 'name': 'GX85', 'type': 'type_dslr', 'optical_length': 19.25, 'mass': 426, 'tside_thread': 'MFT', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Panasonic_G100': {'brand': 'Panasonic', 'name': 'G100', 'type': 'type_dslr', 'optical_length': 19.25, 'mass': 412, 'tside_thread': 'MFT', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Panasonic_Lumix_S5': {'brand': 'Panasonic', 'name': 'Lumix S5', 'type': 'type_dslr', 'optical_length': 20, 'mass': 714, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Panasonic_Lumix_S5_II': {'brand': 'Panasonic', 'name': 'Lumix S5 II', 'type': 'type_dslr', 'optical_length': 20, 'mass': 740, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Panasonic_Lumix_S1': {'brand': 'Panasonic', 'name': 'Lumix S1', 'type': 'type_dslr', 'optical_length': 20, 'mass': 899, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Panasonic_Lumix_S1R': {'brand': 'Panasonic', 'name': 'Lumix S1R', 'type': 'type_dslr', 'optical_length': 20, 'mass': 898, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Panasonic_Lumix_S1H': {'brand': 'Panasonic', 'name': 'Lumix S1H', 'type': 'type_dslr', 'optical_length': 20, 'mass': 1164, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}}

    @classmethod
    def Panasonic_GH6(cls):
        return cls.from_database(cls._DATABASE['Panasonic_GH6'])

    @classmethod
    def Panasonic_GH5_II(cls):
        return cls.from_database(cls._DATABASE['Panasonic_GH5_II'])

    @classmethod
    def Panasonic_GH5(cls):
        return cls.from_database(cls._DATABASE['Panasonic_GH5'])

    @classmethod
    def Panasonic_G9_II(cls):
        return cls.from_database(cls._DATABASE['Panasonic_G9_II'])

    @classmethod
    def Panasonic_G9(cls):
        return cls.from_database(cls._DATABASE['Panasonic_G9'])

    @classmethod
    def Panasonic_G85(cls):
        return cls.from_database(cls._DATABASE['Panasonic_G85'])

    @classmethod
    def Panasonic_GX85(cls):
        return cls.from_database(cls._DATABASE['Panasonic_GX85'])

    @classmethod
    def Panasonic_G100(cls):
        return cls.from_database(cls._DATABASE['Panasonic_G100'])

    @classmethod
    def Panasonic_Lumix_S5(cls):
        return cls.from_database(cls._DATABASE['Panasonic_Lumix_S5'])

    @classmethod
    def Panasonic_Lumix_S5_II(cls):
        return cls.from_database(cls._DATABASE['Panasonic_Lumix_S5_II'])

    @classmethod
    def Panasonic_Lumix_S1(cls):
        return cls.from_database(cls._DATABASE['Panasonic_Lumix_S1'])

    @classmethod
    def Panasonic_Lumix_S1R(cls):
        return cls.from_database(cls._DATABASE['Panasonic_Lumix_S1R'])

    @classmethod
    def Panasonic_Lumix_S1H(cls):
        return cls.from_database(cls._DATABASE['Panasonic_Lumix_S1H'])