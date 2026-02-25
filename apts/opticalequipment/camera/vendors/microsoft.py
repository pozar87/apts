import numpy
import math
from typing import Any
from ...abstract import OutputOpticalEqipment
from ....constants import GraphConstants, OpticalType
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ..base import Camera

class MicrosoftCamera(Camera):
    _DATABASE = {'Microsoft_LifeCam_HD_3000_afocal': {'brand': 'Microsoft', 'name': 'LifeCam HD-3000 (afocal)', 'type': 'type_camera', 'optical_length': 0, 'mass': 110, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}}

    @classmethod
    def Microsoft_LifeCam_HD_3000_afocal(cls):
        return cls.from_database(cls._DATABASE['Microsoft_LifeCam_HD_3000_afocal'])