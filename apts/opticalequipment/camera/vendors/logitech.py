import numpy
import math
from typing import Any
from ...abstract import OutputOpticalEqipment
from ....constants import GraphConstants, OpticalType
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ..base import Camera

class LogitechCamera(Camera):
    _DATABASE = {'Logitech_C920_Webcam_afocal': {'brand': 'Logitech', 'name': 'C920 Webcam (afocal)', 'type': 'type_camera', 'optical_length': 0, 'mass': 162, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Logitech_C930e_Webcam_afocal': {'brand': 'Logitech', 'name': 'C930e Webcam (afocal)', 'type': 'type_camera', 'optical_length': 0, 'mass': 175, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}}

    @classmethod
    def Logitech_C920_Webcam_afocal(cls):
        return cls.from_database(cls._DATABASE['Logitech_C920_Webcam_afocal'])

    @classmethod
    def Logitech_C930e_Webcam_afocal(cls):
        return cls.from_database(cls._DATABASE['Logitech_C930e_Webcam_afocal'])