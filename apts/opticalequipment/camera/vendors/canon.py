import numpy
import math
from typing import Any
from ...abstract import OutputOpticalEqipment
from ....constants import GraphConstants, OpticalType
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ..base import Camera

class CanonCamera(Camera):
    _DATABASE = {'Canon_EOS_Ra': {'brand': 'Canon', 'name': 'EOS Ra', 'type': 'type_dslr', 'optical_length': 44, 'mass': 660, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_6D_II': {'brand': 'Canon', 'name': 'EOS 6D II', 'type': 'type_dslr', 'optical_length': 44, 'mass': 765, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_5D_IV': {'brand': 'Canon', 'name': 'EOS 5D IV', 'type': 'type_dslr', 'optical_length': 44, 'mass': 890, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_5D_III': {'brand': 'Canon', 'name': 'EOS 5D III', 'type': 'type_dslr', 'optical_length': 44, 'mass': 860, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_60Da': {'brand': 'Canon', 'name': 'EOS 60Da', 'type': 'type_dslr', 'optical_length': 44, 'mass': 675, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_1000Da': {'brand': 'Canon', 'name': 'EOS 1000Da', 'type': 'type_dslr', 'optical_length': 44, 'mass': 480, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_2000D': {'brand': 'Canon', 'name': 'EOS 2000D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 475, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_850D': {'brand': 'Canon', 'name': 'EOS 850D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 515, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_90D': {'brand': 'Canon', 'name': 'EOS 90D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 619, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_80D': {'brand': 'Canon', 'name': 'EOS 80D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 650, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_77D': {'brand': 'Canon', 'name': 'EOS 77D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 540, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_4000D': {'brand': 'Canon', 'name': 'EOS 4000D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 436, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_750D': {'brand': 'Canon', 'name': 'EOS 750D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 510, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_700D': {'brand': 'Canon', 'name': 'EOS 700D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 525, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_650D': {'brand': 'Canon', 'name': 'EOS 650D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 520, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_600D': {'brand': 'Canon', 'name': 'EOS 600D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 515, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_550D': {'brand': 'Canon', 'name': 'EOS 550D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 530, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_450D': {'brand': 'Canon', 'name': 'EOS 450D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 475, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_350D': {'brand': 'Canon', 'name': 'EOS 350D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 485, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_1100D': {'brand': 'Canon', 'name': 'EOS 1100D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 440, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_7D_II': {'brand': 'Canon', 'name': 'EOS 7D II', 'type': 'type_dslr', 'optical_length': 44, 'mass': 820, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_6D': {'brand': 'Canon', 'name': 'EOS 6D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 755, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_5D_II': {'brand': 'Canon', 'name': 'EOS 5D II', 'type': 'type_dslr', 'optical_length': 44, 'mass': 810, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_1200D': {'brand': 'Canon', 'name': 'EOS 1200D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 435, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_R': {'brand': 'Canon', 'name': 'EOS R', 'type': 'type_dslr', 'optical_length': 20, 'mass': 660, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_R5': {'brand': 'Canon', 'name': 'EOS R5', 'type': 'type_dslr', 'optical_length': 20, 'mass': 738, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_R5_II': {'brand': 'Canon', 'name': 'EOS R5 II', 'type': 'type_dslr', 'optical_length': 20, 'mass': 746, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_R6': {'brand': 'Canon', 'name': 'EOS R6', 'type': 'type_dslr', 'optical_length': 20, 'mass': 680, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_R6_II': {'brand': 'Canon', 'name': 'EOS R6 II', 'type': 'type_dslr', 'optical_length': 20, 'mass': 670, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_R7': {'brand': 'Canon', 'name': 'EOS R7', 'type': 'type_dslr', 'optical_length': 20, 'mass': 612, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_R8': {'brand': 'Canon', 'name': 'EOS R8', 'type': 'type_dslr', 'optical_length': 20, 'mass': 461, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_R10': {'brand': 'Canon', 'name': 'EOS R10', 'type': 'type_dslr', 'optical_length': 20, 'mass': 429, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_R50': {'brand': 'Canon', 'name': 'EOS R50', 'type': 'type_dslr', 'optical_length': 20, 'mass': 375, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_R100': {'brand': 'Canon', 'name': 'EOS R100', 'type': 'type_dslr', 'optical_length': 20, 'mass': 356, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_RP': {'brand': 'Canon', 'name': 'EOS RP', 'type': 'type_dslr', 'optical_length': 20, 'mass': 485, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_R3': {'brand': 'Canon', 'name': 'EOS R3', 'type': 'type_dslr', 'optical_length': 20, 'mass': 1015, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_R6_III': {'brand': 'Canon', 'name': 'EOS R6 III', 'type': 'type_dslr', 'optical_length': 20, 'mass': 690, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_R1': {'brand': 'Canon', 'name': 'EOS R1', 'type': 'type_dslr', 'optical_length': 20, 'mass': 1000, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_M50_II': {'brand': 'Canon', 'name': 'EOS M50 II', 'type': 'type_dslr', 'optical_length': 20, 'mass': 387, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_20Da': {'brand': 'Canon', 'name': 'EOS 20Da', 'type': 'type_dslr', 'optical_length': 44, 'mass': 685, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_300D': {'brand': 'Canon', 'name': 'EOS 300D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 560, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_400D': {'brand': 'Canon', 'name': 'EOS 400D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 510, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_500D': {'brand': 'Canon', 'name': 'EOS 500D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 520, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_1000D': {'brand': 'Canon', 'name': 'EOS 1000D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 450, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_1300D': {'brand': 'Canon', 'name': 'EOS 1300D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 440, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_M6_II': {'brand': 'Canon', 'name': 'EOS M6 II', 'type': 'type_dslr', 'optical_length': 20, 'mass': 408, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_200D': {'brand': 'Canon', 'name': 'EOS 200D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 453, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_250D': {'brand': 'Canon', 'name': 'EOS 250D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 449, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_M200': {'brand': 'Canon', 'name': 'EOS M200', 'type': 'type_dslr', 'optical_length': 18, 'mass': 299, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_70D': {'brand': 'Canon', 'name': 'EOS 70D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 755, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_5DS_R': {'brand': 'Canon', 'name': 'EOS 5DS R', 'type': 'type_dslr', 'optical_length': 44, 'mass': 930, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_5DS': {'brand': 'Canon', 'name': 'EOS 5DS', 'type': 'type_dslr', 'optical_length': 44, 'mass': 845, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_1DX_III': {'brand': 'Canon', 'name': 'EOS 1DX III', 'type': 'type_dslr', 'optical_length': 44, 'mass': 1440, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_1DX_II': {'brand': 'Canon', 'name': 'EOS 1DX II', 'type': 'type_dslr', 'optical_length': 44, 'mass': 1340, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_5D': {'brand': 'Canon', 'name': 'EOS 5D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 810, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_100D': {'brand': 'Canon', 'name': 'EOS 100D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 407, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_40D': {'brand': 'Canon', 'name': 'EOS 40D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 740, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_50D': {'brand': 'Canon', 'name': 'EOS 50D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 730, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_30D': {'brand': 'Canon', 'name': 'EOS 30D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 700, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Canon_EOS_20D': {'brand': 'Canon', 'name': 'EOS 20D', 'type': 'type_dslr', 'optical_length': 44, 'mass': 685, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}}

    @classmethod
    def Canon_EOS_Ra(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_Ra'])

    @classmethod
    def Canon_EOS_6D_II(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_6D_II'])

    @classmethod
    def Canon_EOS_5D_IV(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_5D_IV'])

    @classmethod
    def Canon_EOS_5D_III(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_5D_III'])

    @classmethod
    def Canon_EOS_60Da(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_60Da'])

    @classmethod
    def Canon_EOS_1000Da(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_1000Da'])

    @classmethod
    def Canon_EOS_2000D(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_2000D'])

    @classmethod
    def Canon_EOS_850D(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_850D'])

    @classmethod
    def Canon_EOS_90D(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_90D'])

    @classmethod
    def Canon_EOS_80D(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_80D'])

    @classmethod
    def Canon_EOS_77D(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_77D'])

    @classmethod
    def Canon_EOS_4000D(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_4000D'])

    @classmethod
    def Canon_EOS_750D(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_750D'])

    @classmethod
    def Canon_EOS_700D(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_700D'])

    @classmethod
    def Canon_EOS_650D(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_650D'])

    @classmethod
    def Canon_EOS_600D(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_600D'])

    @classmethod
    def Canon_EOS_550D(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_550D'])

    @classmethod
    def Canon_EOS_450D(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_450D'])

    @classmethod
    def Canon_EOS_350D(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_350D'])

    @classmethod
    def Canon_EOS_1100D(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_1100D'])

    @classmethod
    def Canon_EOS_7D_II(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_7D_II'])

    @classmethod
    def Canon_EOS_6D(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_6D'])

    @classmethod
    def Canon_EOS_5D_II(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_5D_II'])

    @classmethod
    def Canon_EOS_1200D(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_1200D'])

    @classmethod
    def Canon_EOS_R(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_R'])

    @classmethod
    def Canon_EOS_R5(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_R5'])

    @classmethod
    def Canon_EOS_R5_II(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_R5_II'])

    @classmethod
    def Canon_EOS_R6(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_R6'])

    @classmethod
    def Canon_EOS_R6_II(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_R6_II'])

    @classmethod
    def Canon_EOS_R7(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_R7'])

    @classmethod
    def Canon_EOS_R8(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_R8'])

    @classmethod
    def Canon_EOS_R10(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_R10'])

    @classmethod
    def Canon_EOS_R50(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_R50'])

    @classmethod
    def Canon_EOS_R100(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_R100'])

    @classmethod
    def Canon_EOS_RP(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_RP'])

    @classmethod
    def Canon_EOS_R3(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_R3'])

    @classmethod
    def Canon_EOS_R6_III(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_R6_III'])

    @classmethod
    def Canon_EOS_R1(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_R1'])

    @classmethod
    def Canon_EOS_M50_II(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_M50_II'])

    @classmethod
    def Canon_EOS_20Da(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_20Da'])

    @classmethod
    def Canon_EOS_300D(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_300D'])

    @classmethod
    def Canon_EOS_400D(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_400D'])

    @classmethod
    def Canon_EOS_500D(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_500D'])

    @classmethod
    def Canon_EOS_1000D(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_1000D'])

    @classmethod
    def Canon_EOS_1300D(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_1300D'])

    @classmethod
    def Canon_EOS_M6_II(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_M6_II'])

    @classmethod
    def Canon_EOS_200D(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_200D'])

    @classmethod
    def Canon_EOS_250D(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_250D'])

    @classmethod
    def Canon_EOS_M200(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_M200'])

    @classmethod
    def Canon_EOS_70D(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_70D'])

    @classmethod
    def Canon_EOS_5DS_R(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_5DS_R'])

    @classmethod
    def Canon_EOS_5DS(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_5DS'])

    @classmethod
    def Canon_EOS_1DX_III(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_1DX_III'])

    @classmethod
    def Canon_EOS_1DX_II(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_1DX_II'])

    @classmethod
    def Canon_EOS_5D(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_5D'])

    @classmethod
    def Canon_EOS_100D(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_100D'])

    @classmethod
    def Canon_EOS_40D(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_40D'])

    @classmethod
    def Canon_EOS_50D(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_50D'])

    @classmethod
    def Canon_EOS_30D(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_30D'])

    @classmethod
    def Canon_EOS_20D(cls):
        return cls.from_database(cls._DATABASE['Canon_EOS_20D'])