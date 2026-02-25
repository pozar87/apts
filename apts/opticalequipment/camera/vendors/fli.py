import numpy
import math
from typing import Any
from ...abstract import OutputOpticalEqipment
from ....constants import GraphConstants, OpticalType
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ..base import Camera

class FliCamera(Camera):
    _DATABASE = {'FLI_ML16200': {'brand': 'FLI', 'name': 'ML16200', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1500, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'FLI_Kepler_KL400': {'brand': 'FLI', 'name': 'Kepler KL400', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1200, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'FLI_ProLine_16803': {'brand': 'FLI', 'name': 'ProLine 16803', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1800, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'FLI_ML50100': {'brand': 'FLI', 'name': 'ML50100', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 2000, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'FLI_Kepler_KL4040': {'brand': 'FLI', 'name': 'Kepler KL4040', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1500, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'FLI_ML8300': {'brand': 'FLI', 'name': 'ML8300', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 800, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'FLI_ProLine_PL09000': {'brand': 'FLI', 'name': 'ProLine PL09000', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1500, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'FLI_ProLine_PL4710': {'brand': 'FLI', 'name': 'ProLine PL4710', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1000, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'FLI_ProLine_PL11002': {'brand': 'FLI', 'name': 'ProLine PL11002', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1600, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'FLI_Kepler_KL4040M': {'brand': 'FLI', 'name': 'Kepler KL4040M', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1500, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'FLI_Kepler_KL16070': {'brand': 'FLI', 'name': 'Kepler KL16070', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1800, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'FLI_MicroLine_ML4710': {'brand': 'FLI', 'name': 'MicroLine ML4710', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 700, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'FLI_MicroLine_ML1109': {'brand': 'FLI', 'name': 'MicroLine ML1109', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 600, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'FLI_MicroLine_ML29050': {'brand': 'FLI', 'name': 'MicroLine ML29050', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 900, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'FLI_ML16070': {'brand': 'FLI', 'name': 'ML16070', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1600, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'FLI_ML8050': {'brand': 'FLI', 'name': 'ML8050', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 900, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'FLI_ML4710': {'brand': 'FLI', 'name': 'ML4710', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 700, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'FLI_ProLine_PL16803': {'brand': 'FLI', 'name': 'ProLine PL16803', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1800, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'FLI_Kepler_KL4040_FG': {'brand': 'FLI', 'name': 'Kepler KL4040 FG', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1550, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}}

    @classmethod
    def FLI_ML16200(cls):
        return cls.from_database(cls._DATABASE['FLI_ML16200'])

    @classmethod
    def FLI_Kepler_KL400(cls):
        return cls.from_database(cls._DATABASE['FLI_Kepler_KL400'])

    @classmethod
    def FLI_ProLine_16803(cls):
        return cls.from_database(cls._DATABASE['FLI_ProLine_16803'])

    @classmethod
    def FLI_ML50100(cls):
        return cls.from_database(cls._DATABASE['FLI_ML50100'])

    @classmethod
    def FLI_Kepler_KL4040(cls):
        return cls.from_database(cls._DATABASE['FLI_Kepler_KL4040'])

    @classmethod
    def FLI_ML8300(cls):
        return cls.from_database(cls._DATABASE['FLI_ML8300'])

    @classmethod
    def FLI_ProLine_PL09000(cls):
        return cls.from_database(cls._DATABASE['FLI_ProLine_PL09000'])

    @classmethod
    def FLI_ProLine_PL4710(cls):
        return cls.from_database(cls._DATABASE['FLI_ProLine_PL4710'])

    @classmethod
    def FLI_ProLine_PL11002(cls):
        return cls.from_database(cls._DATABASE['FLI_ProLine_PL11002'])

    @classmethod
    def FLI_Kepler_KL4040M(cls):
        return cls.from_database(cls._DATABASE['FLI_Kepler_KL4040M'])

    @classmethod
    def FLI_Kepler_KL16070(cls):
        return cls.from_database(cls._DATABASE['FLI_Kepler_KL16070'])

    @classmethod
    def FLI_MicroLine_ML4710(cls):
        return cls.from_database(cls._DATABASE['FLI_MicroLine_ML4710'])

    @classmethod
    def FLI_MicroLine_ML1109(cls):
        return cls.from_database(cls._DATABASE['FLI_MicroLine_ML1109'])

    @classmethod
    def FLI_MicroLine_ML29050(cls):
        return cls.from_database(cls._DATABASE['FLI_MicroLine_ML29050'])

    @classmethod
    def FLI_ML16070(cls):
        return cls.from_database(cls._DATABASE['FLI_ML16070'])

    @classmethod
    def FLI_ML8050(cls):
        return cls.from_database(cls._DATABASE['FLI_ML8050'])

    @classmethod
    def FLI_ML4710(cls):
        return cls.from_database(cls._DATABASE['FLI_ML4710'])

    @classmethod
    def FLI_ProLine_PL16803(cls):
        return cls.from_database(cls._DATABASE['FLI_ProLine_PL16803'])

    @classmethod
    def FLI_Kepler_KL4040_FG(cls):
        return cls.from_database(cls._DATABASE['FLI_Kepler_KL4040_FG'])