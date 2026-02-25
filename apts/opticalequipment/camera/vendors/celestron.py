import numpy
import math
from typing import Any
from ...abstract import OutputOpticalEqipment
from ....constants import GraphConstants, OpticalType
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ..base import Camera

class CelestronCamera(Camera):
    _DATABASE = {'Celestron_NexImage_10': {'brand': 'Celestron', 'name': 'NexImage 10', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 120, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Celestron_NexImage_Burst': {'brand': 'Celestron', 'name': 'NexImage Burst', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 100, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Celestron_NexImage_5': {'brand': 'Celestron', 'name': 'NexImage 5', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 90, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Celestron_Skyris_132M': {'brand': 'Celestron', 'name': 'Skyris 132M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 150, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Celestron_Skyris_236M': {'brand': 'Celestron', 'name': 'Skyris 236M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 160, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Celestron_Skyris_618M': {'brand': 'Celestron', 'name': 'Skyris 618M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 200, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Celestron_Skyris_445M': {'brand': 'Celestron', 'name': 'Skyris 445M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 180, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Celestron_Skyris_274M': {'brand': 'Celestron', 'name': 'Skyris 274M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 170, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}}

    @classmethod
    def Celestron_NexImage_10(cls):
        return cls.from_database(cls._DATABASE['Celestron_NexImage_10'])

    @classmethod
    def Celestron_NexImage_Burst(cls):
        return cls.from_database(cls._DATABASE['Celestron_NexImage_Burst'])

    @classmethod
    def Celestron_NexImage_5(cls):
        return cls.from_database(cls._DATABASE['Celestron_NexImage_5'])

    @classmethod
    def Celestron_Skyris_132M(cls):
        return cls.from_database(cls._DATABASE['Celestron_Skyris_132M'])

    @classmethod
    def Celestron_Skyris_236M(cls):
        return cls.from_database(cls._DATABASE['Celestron_Skyris_236M'])

    @classmethod
    def Celestron_Skyris_618M(cls):
        return cls.from_database(cls._DATABASE['Celestron_Skyris_618M'])

    @classmethod
    def Celestron_Skyris_445M(cls):
        return cls.from_database(cls._DATABASE['Celestron_Skyris_445M'])

    @classmethod
    def Celestron_Skyris_274M(cls):
        return cls.from_database(cls._DATABASE['Celestron_Skyris_274M'])