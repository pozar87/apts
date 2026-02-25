import numpy
from ...abstract import OpticalEquipment
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ....constants import GraphConstants
from enum import Enum
from typing import Optional
from ..base import TelescopeType, TubeMaterial, Telescope

class GenericTelescope(Telescope):

    @classmethod
    def ID_7Artisans_50mm_f_1_05_Sony_E(cls):
        return cls.from_database(cls._DATABASE['ID_7Artisans_50mm_f_1_05_Sony_E'])

    @classmethod
    def ID_7Artisans_35mm_f_0_95_Sony_E(cls):
        return cls.from_database(cls._DATABASE['ID_7Artisans_35mm_f_0_95_Sony_E'])

    @classmethod
    def ID_7Artisans_55mm_f_1_4_Sony_E(cls):
        return cls.from_database(cls._DATABASE['ID_7Artisans_55mm_f_1_4_Sony_E'])

    @classmethod
    def ID_7Artisans_25mm_f_1_8_Sony_E(cls):
        return cls.from_database(cls._DATABASE['ID_7Artisans_25mm_f_1_8_Sony_E'])

    @classmethod
    def ID_7Artisans_35mm_f_1_2_Sony_E(cls):
        return cls.from_database(cls._DATABASE['ID_7Artisans_35mm_f_1_2_Sony_E'])

    @classmethod
    def ID_7Artisans_60mm_f_2_8_Macro_Sony_E(cls):
        return cls.from_database(cls._DATABASE['ID_7Artisans_60mm_f_2_8_Macro_Sony_E'])

    @classmethod
    def ID_7Artisans_12mm_f_2_8_Sony_E(cls):
        return cls.from_database(cls._DATABASE['ID_7Artisans_12mm_f_2_8_Sony_E'])

    @classmethod
    def ID_7Artisans_50mm_f_1_05_Nikon_Z(cls):
        return cls.from_database(cls._DATABASE['ID_7Artisans_50mm_f_1_05_Nikon_Z'])

    @classmethod
    def ID_7Artisans_50mm_f_1_05_Canon_RF(cls):
        return cls.from_database(cls._DATABASE['ID_7Artisans_50mm_f_1_05_Canon_RF'])

    @classmethod
    def ID_7Artisans_35mm_f_0_95_MFT(cls):
        return cls.from_database(cls._DATABASE['ID_7Artisans_35mm_f_0_95_MFT'])

    @classmethod
    def ID_7Artisans_35mm_f_0_95_Fuji_X(cls):
        return cls.from_database(cls._DATABASE['ID_7Artisans_35mm_f_0_95_Fuji_X'])

    @classmethod
    def ID_7Artisans_25mm_f_0_95_MFT(cls):
        return cls.from_database(cls._DATABASE['ID_7Artisans_25mm_f_0_95_MFT'])

    @classmethod
    def ID_7Artisans_55mm_f_1_4_Fuji_X(cls):
        return cls.from_database(cls._DATABASE['ID_7Artisans_55mm_f_1_4_Fuji_X'])

    @classmethod
    def ID_7Artisans_55mm_f_1_4_MFT(cls):
        return cls.from_database(cls._DATABASE['ID_7Artisans_55mm_f_1_4_MFT'])

    @classmethod
    def ID_7Artisans_12mm_f_2_8_EOS(cls):
        return cls.from_database(cls._DATABASE['ID_7Artisans_12mm_f_2_8_EOS'])