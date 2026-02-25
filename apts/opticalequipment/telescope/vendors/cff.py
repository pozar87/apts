import numpy
from ...abstract import OpticalEquipment
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ....constants import GraphConstants
from enum import Enum
from typing import Optional
from ..base import TelescopeType, TubeMaterial, Telescope

class CffTelescope(Telescope):
    _DATABASE = {'CFF_RC_250_10': {'brand': 'CFF', 'name': 'RC 250 (10")', 'type': 'type_telescope', 'optical_length': 0, 'mass': 11000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'CFF_RC_300_12': {'brand': 'CFF', 'name': 'RC 300 (12")', 'type': 'type_telescope', 'optical_length': 0, 'mass': 16000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def CFF_RC_250_10(cls):
        return cls.from_database(cls._DATABASE['CFF_RC_250_10'])

    @classmethod
    def CFF_RC_300_12(cls):
        return cls.from_database(cls._DATABASE['CFF_RC_300_12'])