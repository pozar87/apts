import numpy
import math
from typing import Any
from ...abstract import OutputOpticalEqipment
from ....constants import GraphConstants, OpticalType
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ..base import Camera

class Wanderer_astroCamera(Camera):
    _DATABASE = {'Wanderer_Astro_WanderCam_585C': {'brand': 'Wanderer Astro', 'name': 'WanderCam 585C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 160, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}}

    @classmethod
    def Wanderer_Astro_WanderCam_585C(cls):
        return cls.from_database(cls._DATABASE['Wanderer_Astro_WanderCam_585C'])