import numpy
import math
from typing import Any
from ...abstract import OutputOpticalEqipment
from ....constants import GraphConstants, OpticalType
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ..base import Camera

class Rising_camCamera(Camera):
    _DATABASE = {'Rising_Cam_IMX571_ATR': {'brand': 'Rising Cam', 'name': 'IMX571 (ATR)', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 600, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Rising_Cam_IMX533_ATR': {'brand': 'Rising Cam', 'name': 'IMX533 (ATR)', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 400, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Rising_Cam_IMX294_ATR': {'brand': 'Rising Cam', 'name': 'IMX294 (ATR)', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Rising_Cam_IMX585_ATR': {'brand': 'Rising Cam', 'name': 'IMX585 (ATR)', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 200, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Rising_Cam_IMX_678C': {'brand': 'Rising Cam', 'name': 'IMX 678C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 200, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Rising_Cam_IMX_462MC': {'brand': 'Rising Cam', 'name': 'IMX 462MC', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 150, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Rising_Cam_IMX_174MM': {'brand': 'Rising Cam', 'name': 'IMX 174MM', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 180, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Rising_Cam_IMX_290MM': {'brand': 'Rising Cam', 'name': 'IMX 290MM', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 170, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Rising_Cam_IMX_290MC': {'brand': 'Rising Cam', 'name': 'IMX 290MC', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 170, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Rising_Cam_IMX_120MM': {'brand': 'Rising Cam', 'name': 'IMX 120MM', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 90, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Rising_Cam_IMX_482MC': {'brand': 'Rising Cam', 'name': 'IMX 482MC', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 160, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Rising_Cam_IMX_385MC': {'brand': 'Rising Cam', 'name': 'IMX 385MC', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 140, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Rising_Cam_IMX_224MC': {'brand': 'Rising Cam', 'name': 'IMX 224MC', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 100, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Rising_Cam_IMX_178MM': {'brand': 'Rising Cam', 'name': 'IMX 178MM', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 130, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Rising_Cam_IMX_178MC': {'brand': 'Rising Cam', 'name': 'IMX 178MC', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 130, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}}

    @classmethod
    def Rising_Cam_IMX571_ATR(cls):
        return cls.from_database(cls._DATABASE['Rising_Cam_IMX571_ATR'])

    @classmethod
    def Rising_Cam_IMX533_ATR(cls):
        return cls.from_database(cls._DATABASE['Rising_Cam_IMX533_ATR'])

    @classmethod
    def Rising_Cam_IMX294_ATR(cls):
        return cls.from_database(cls._DATABASE['Rising_Cam_IMX294_ATR'])

    @classmethod
    def Rising_Cam_IMX585_ATR(cls):
        return cls.from_database(cls._DATABASE['Rising_Cam_IMX585_ATR'])

    @classmethod
    def Rising_Cam_IMX_678C(cls):
        return cls.from_database(cls._DATABASE['Rising_Cam_IMX_678C'])

    @classmethod
    def Rising_Cam_IMX_462MC(cls):
        return cls.from_database(cls._DATABASE['Rising_Cam_IMX_462MC'])

    @classmethod
    def Rising_Cam_IMX_174MM(cls):
        return cls.from_database(cls._DATABASE['Rising_Cam_IMX_174MM'])

    @classmethod
    def Rising_Cam_IMX_290MM(cls):
        return cls.from_database(cls._DATABASE['Rising_Cam_IMX_290MM'])

    @classmethod
    def Rising_Cam_IMX_290MC(cls):
        return cls.from_database(cls._DATABASE['Rising_Cam_IMX_290MC'])

    @classmethod
    def Rising_Cam_IMX_120MM(cls):
        return cls.from_database(cls._DATABASE['Rising_Cam_IMX_120MM'])

    @classmethod
    def Rising_Cam_IMX_482MC(cls):
        return cls.from_database(cls._DATABASE['Rising_Cam_IMX_482MC'])

    @classmethod
    def Rising_Cam_IMX_385MC(cls):
        return cls.from_database(cls._DATABASE['Rising_Cam_IMX_385MC'])

    @classmethod
    def Rising_Cam_IMX_224MC(cls):
        return cls.from_database(cls._DATABASE['Rising_Cam_IMX_224MC'])

    @classmethod
    def Rising_Cam_IMX_178MM(cls):
        return cls.from_database(cls._DATABASE['Rising_Cam_IMX_178MM'])

    @classmethod
    def Rising_Cam_IMX_178MC(cls):
        return cls.from_database(cls._DATABASE['Rising_Cam_IMX_178MC'])