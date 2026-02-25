import numpy
import math
from typing import Any
from ...abstract import OutputOpticalEqipment
from ....constants import GraphConstants, OpticalType
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ..base import Camera

class InovaCamera(Camera):
    _DATABASE = {'iNova_PLB_Cx2_178C': {'brand': 'iNova', 'name': 'PLB-Cx2 178C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'iNova_PLB_Cx2_290C': {'brand': 'iNova', 'name': 'PLB-Cx2 290C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'iNova_PLB_Cx2_462C': {'brand': 'iNova', 'name': 'PLB-Cx2 462C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 85, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'iNova_PLB_Cx2_585C': {'brand': 'iNova', 'name': 'PLB-Cx2 585C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 90, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'iNova_PLB_Mx2_IMX290': {'brand': 'iNova', 'name': 'PLB-Mx2 (IMX290)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 180, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'iNova_PLB_Cx2_IMX290': {'brand': 'iNova', 'name': 'PLB-Cx2 (IMX290)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 180, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'iNova_PLB_Mx2_IMX178': {'brand': 'iNova', 'name': 'PLB-Mx2 (IMX178)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 160, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'iNova_PLB_Cx2_IMX178': {'brand': 'iNova', 'name': 'PLB-Cx2 (IMX178)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 160, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}}

    @classmethod
    def iNova_PLB_Cx2_178C(cls):
        return cls.from_database(cls._DATABASE['iNova_PLB_Cx2_178C'])

    @classmethod
    def iNova_PLB_Cx2_290C(cls):
        return cls.from_database(cls._DATABASE['iNova_PLB_Cx2_290C'])

    @classmethod
    def iNova_PLB_Cx2_462C(cls):
        return cls.from_database(cls._DATABASE['iNova_PLB_Cx2_462C'])

    @classmethod
    def iNova_PLB_Cx2_585C(cls):
        return cls.from_database(cls._DATABASE['iNova_PLB_Cx2_585C'])

    @classmethod
    def iNova_PLB_Mx2_IMX290(cls):
        return cls.from_database(cls._DATABASE['iNova_PLB_Mx2_IMX290'])

    @classmethod
    def iNova_PLB_Cx2_IMX290(cls):
        return cls.from_database(cls._DATABASE['iNova_PLB_Cx2_IMX290'])

    @classmethod
    def iNova_PLB_Mx2_IMX178(cls):
        return cls.from_database(cls._DATABASE['iNova_PLB_Mx2_IMX178'])

    @classmethod
    def iNova_PLB_Cx2_IMX178(cls):
        return cls.from_database(cls._DATABASE['iNova_PLB_Cx2_IMX178'])