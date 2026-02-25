import numpy
import math
from typing import Any
from ...abstract import OutputOpticalEqipment
from ....constants import GraphConstants, OpticalType
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ..base import Camera

class MeadeCamera(Camera):
    _DATABASE = {'Meade_LPI_G_Color': {'brand': 'Meade', 'name': 'LPI-G (Color)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Meade_LPI_G_Mono': {'brand': 'Meade', 'name': 'LPI-G (Mono)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Meade_LPI_G_Advanced_Color': {'brand': 'Meade', 'name': 'LPI-G Advanced (Color)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 120, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Meade_Deep_Sky_Imager_IV_Color': {'brand': 'Meade', 'name': 'Deep Sky Imager IV (Color)', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 250, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Meade_Deep_Sky_Imager_IV_Mono': {'brand': 'Meade', 'name': 'Deep Sky Imager IV (Mono)', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 250, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Meade_Deep_Sky_Imager_Pro': {'brand': 'Meade', 'name': 'Deep Sky Imager Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 350, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}}

    @classmethod
    def Meade_LPI_G_Color(cls):
        return cls.from_database(cls._DATABASE['Meade_LPI_G_Color'])

    @classmethod
    def Meade_LPI_G_Mono(cls):
        return cls.from_database(cls._DATABASE['Meade_LPI_G_Mono'])

    @classmethod
    def Meade_LPI_G_Advanced_Color(cls):
        return cls.from_database(cls._DATABASE['Meade_LPI_G_Advanced_Color'])

    @classmethod
    def Meade_Deep_Sky_Imager_IV_Color(cls):
        return cls.from_database(cls._DATABASE['Meade_Deep_Sky_Imager_IV_Color'])

    @classmethod
    def Meade_Deep_Sky_Imager_IV_Mono(cls):
        return cls.from_database(cls._DATABASE['Meade_Deep_Sky_Imager_IV_Mono'])

    @classmethod
    def Meade_Deep_Sky_Imager_Pro(cls):
        return cls.from_database(cls._DATABASE['Meade_Deep_Sky_Imager_Pro'])