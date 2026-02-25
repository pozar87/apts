import numpy
import math
from typing import Any
from ...abstract import OutputOpticalEqipment
from ....constants import GraphConstants, OpticalType
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ..base import Camera

class SonyCamera(Camera):
    _DATABASE = {'Sony_A7_III': {'brand': 'Sony', 'name': 'A7 III', 'type': 'type_dslr', 'optical_length': 18, 'mass': 650, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Sony_A7_IV': {'brand': 'Sony', 'name': 'A7 IV', 'type': 'type_dslr', 'optical_length': 18, 'mass': 658, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Sony_A7R_IV': {'brand': 'Sony', 'name': 'A7R IV', 'type': 'type_dslr', 'optical_length': 18, 'mass': 665, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Sony_A7R_V': {'brand': 'Sony', 'name': 'A7R V', 'type': 'type_dslr', 'optical_length': 18, 'mass': 723, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Sony_A7S_III': {'brand': 'Sony', 'name': 'A7S III', 'type': 'type_dslr', 'optical_length': 18, 'mass': 699, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Sony_A7CR': {'brand': 'Sony', 'name': 'A7CR', 'type': 'type_dslr', 'optical_length': 18, 'mass': 515, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Sony_A7C': {'brand': 'Sony', 'name': 'A7C', 'type': 'type_dslr', 'optical_length': 18, 'mass': 509, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Sony_A7C_II': {'brand': 'Sony', 'name': 'A7C II', 'type': 'type_dslr', 'optical_length': 18, 'mass': 514, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Sony_A6700': {'brand': 'Sony', 'name': 'A6700', 'type': 'type_dslr', 'optical_length': 18, 'mass': 493, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Sony_A6400': {'brand': 'Sony', 'name': 'A6400', 'type': 'type_dslr', 'optical_length': 18, 'mass': 403, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Sony_A6300': {'brand': 'Sony', 'name': 'A6300', 'type': 'type_dslr', 'optical_length': 18, 'mass': 404, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Sony_A6100': {'brand': 'Sony', 'name': 'A6100', 'type': 'type_dslr', 'optical_length': 18, 'mass': 396, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Sony_A6000': {'brand': 'Sony', 'name': 'A6000', 'type': 'type_dslr', 'optical_length': 18, 'mass': 344, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Sony_A1': {'brand': 'Sony', 'name': 'A1', 'type': 'type_dslr', 'optical_length': 18, 'mass': 737, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Sony_A9_III': {'brand': 'Sony', 'name': 'A9 III', 'type': 'type_dslr', 'optical_length': 18, 'mass': 703, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Sony_A7_II': {'brand': 'Sony', 'name': 'A7 II', 'type': 'type_dslr', 'optical_length': 18, 'mass': 599, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Sony_A7R_III': {'brand': 'Sony', 'name': 'A7R III', 'type': 'type_dslr', 'optical_length': 18, 'mass': 657, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Sony_A7_V': {'brand': 'Sony', 'name': 'A7 V', 'type': 'type_dslr', 'optical_length': 18, 'mass': 700, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Sony_A6500': {'brand': 'Sony', 'name': 'A6500', 'type': 'type_dslr', 'optical_length': 18, 'mass': 453, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Sony_A5100': {'brand': 'Sony', 'name': 'A5100', 'type': 'type_dslr', 'optical_length': 18, 'mass': 283, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Sony_A6600': {'brand': 'Sony', 'name': 'A6600', 'type': 'type_dslr', 'optical_length': 18, 'mass': 503, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Sony_A77_II': {'brand': 'Sony', 'name': 'A77 II', 'type': 'type_dslr', 'optical_length': 18, 'mass': 647, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Sony_A99_II': {'brand': 'Sony', 'name': 'A99 II', 'type': 'type_dslr', 'optical_length': 18, 'mass': 849, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Sony_A5000': {'brand': 'Sony', 'name': 'A5000', 'type': 'type_dslr', 'optical_length': 18, 'mass': 269, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Sony_NEX_7': {'brand': 'Sony', 'name': 'NEX-7', 'type': 'type_dslr', 'optical_length': 18, 'mass': 353, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Sony_NEX_6': {'brand': 'Sony', 'name': 'NEX-6', 'type': 'type_dslr', 'optical_length': 18, 'mass': 345, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Sony_NEX_5T': {'brand': 'Sony', 'name': 'NEX-5T', 'type': 'type_dslr', 'optical_length': 18, 'mass': 276, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}}

    @classmethod
    def Sony_A7_III(cls):
        return cls.from_database(cls._DATABASE['Sony_A7_III'])

    @classmethod
    def Sony_A7_IV(cls):
        return cls.from_database(cls._DATABASE['Sony_A7_IV'])

    @classmethod
    def Sony_A7R_IV(cls):
        return cls.from_database(cls._DATABASE['Sony_A7R_IV'])

    @classmethod
    def Sony_A7R_V(cls):
        return cls.from_database(cls._DATABASE['Sony_A7R_V'])

    @classmethod
    def Sony_A7S_III(cls):
        return cls.from_database(cls._DATABASE['Sony_A7S_III'])

    @classmethod
    def Sony_A7CR(cls):
        return cls.from_database(cls._DATABASE['Sony_A7CR'])

    @classmethod
    def Sony_A7C(cls):
        return cls.from_database(cls._DATABASE['Sony_A7C'])

    @classmethod
    def Sony_A7C_II(cls):
        return cls.from_database(cls._DATABASE['Sony_A7C_II'])

    @classmethod
    def Sony_A6700(cls):
        return cls.from_database(cls._DATABASE['Sony_A6700'])

    @classmethod
    def Sony_A6400(cls):
        return cls.from_database(cls._DATABASE['Sony_A6400'])

    @classmethod
    def Sony_A6300(cls):
        return cls.from_database(cls._DATABASE['Sony_A6300'])

    @classmethod
    def Sony_A6100(cls):
        return cls.from_database(cls._DATABASE['Sony_A6100'])

    @classmethod
    def Sony_A6000(cls):
        return cls.from_database(cls._DATABASE['Sony_A6000'])

    @classmethod
    def Sony_A1(cls):
        return cls.from_database(cls._DATABASE['Sony_A1'])

    @classmethod
    def Sony_A9_III(cls):
        return cls.from_database(cls._DATABASE['Sony_A9_III'])

    @classmethod
    def Sony_A7_II(cls):
        return cls.from_database(cls._DATABASE['Sony_A7_II'])

    @classmethod
    def Sony_A7R_III(cls):
        return cls.from_database(cls._DATABASE['Sony_A7R_III'])

    @classmethod
    def Sony_A7_V(cls):
        return cls.from_database(cls._DATABASE['Sony_A7_V'])

    @classmethod
    def Sony_A6500(cls):
        return cls.from_database(cls._DATABASE['Sony_A6500'])

    @classmethod
    def Sony_A5100(cls):
        return cls.from_database(cls._DATABASE['Sony_A5100'])

    @classmethod
    def Sony_A6600(cls):
        return cls.from_database(cls._DATABASE['Sony_A6600'])

    @classmethod
    def Sony_A77_II(cls):
        return cls.from_database(cls._DATABASE['Sony_A77_II'])

    @classmethod
    def Sony_A99_II(cls):
        return cls.from_database(cls._DATABASE['Sony_A99_II'])

    @classmethod
    def Sony_A5000(cls):
        return cls.from_database(cls._DATABASE['Sony_A5000'])

    @classmethod
    def Sony_NEX_7(cls):
        return cls.from_database(cls._DATABASE['Sony_NEX_7'])

    @classmethod
    def Sony_NEX_6(cls):
        return cls.from_database(cls._DATABASE['Sony_NEX_6'])

    @classmethod
    def Sony_NEX_5T(cls):
        return cls.from_database(cls._DATABASE['Sony_NEX_5T'])