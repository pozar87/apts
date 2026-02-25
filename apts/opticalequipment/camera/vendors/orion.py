import numpy
import math
from typing import Any
from ...abstract import OutputOpticalEqipment
from ....constants import GraphConstants, OpticalType
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ..base import Camera

class OrionCamera(Camera):
    _DATABASE = {'Orion_StarShoot_G21': {'brand': 'Orion', 'name': 'StarShoot G21', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 350, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Orion_StarShoot_G26_Deep_Space': {'brand': 'Orion', 'name': 'StarShoot G26 Deep Space', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Orion_StarShoot_Solar_System_V': {'brand': 'Orion', 'name': 'StarShoot Solar System V', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 150, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Orion_StarShoot_Autoguider': {'brand': 'Orion', 'name': 'StarShoot Autoguider', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 100, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Orion_StarShoot_Deep_Space_3': {'brand': 'Orion', 'name': 'StarShoot Deep Space 3', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 400, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Orion_StarShoot_Mini': {'brand': 'Orion', 'name': 'StarShoot Mini', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}}

    @classmethod
    def Orion_StarShoot_G21(cls):
        return cls.from_database(cls._DATABASE['Orion_StarShoot_G21'])

    @classmethod
    def Orion_StarShoot_G26_Deep_Space(cls):
        return cls.from_database(cls._DATABASE['Orion_StarShoot_G26_Deep_Space'])

    @classmethod
    def Orion_StarShoot_Solar_System_V(cls):
        return cls.from_database(cls._DATABASE['Orion_StarShoot_Solar_System_V'])

    @classmethod
    def Orion_StarShoot_Autoguider(cls):
        return cls.from_database(cls._DATABASE['Orion_StarShoot_Autoguider'])

    @classmethod
    def Orion_StarShoot_Deep_Space_3(cls):
        return cls.from_database(cls._DATABASE['Orion_StarShoot_Deep_Space_3'])

    @classmethod
    def Orion_StarShoot_Mini(cls):
        return cls.from_database(cls._DATABASE['Orion_StarShoot_Mini'])