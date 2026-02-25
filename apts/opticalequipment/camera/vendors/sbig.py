import numpy
import math
from typing import Any
from ...abstract import OutputOpticalEqipment
from ....constants import GraphConstants, OpticalType
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ..base import Camera

class SbigCamera(Camera):
    _DATABASE = {'SBIG_STF_8300M': {'brand': 'SBIG', 'name': 'STF-8300M', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 600, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'SBIG_STT_8300M': {'brand': 'SBIG', 'name': 'STT-8300M', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 800, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'SBIG_STX_16803': {'brand': 'SBIG', 'name': 'STX-16803', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1200, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'SBIG_STXL_11002': {'brand': 'SBIG', 'name': 'STXL-11002', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1400, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'SBIG_STF_8050M': {'brand': 'SBIG', 'name': 'STF-8050M', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 650, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'SBIG_STT_1603M': {'brand': 'SBIG', 'name': 'STT-1603M', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'SBIG_Aluma_AC694': {'brand': 'SBIG', 'name': 'Aluma AC694', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 400, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'SBIG_STT_1603ME': {'brand': 'SBIG', 'name': 'STT-1603ME', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 550, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'SBIG_STT_3200ME': {'brand': 'SBIG', 'name': 'STT-3200ME', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 700, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'SBIG_ST_i': {'brand': 'SBIG', 'name': 'ST-i', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 180, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'SBIG_ST_402ME': {'brand': 'SBIG', 'name': 'ST-402ME', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 350, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'SBIG_ST_8300M': {'brand': 'SBIG', 'name': 'ST-8300M', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 600, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'SBIG_STF_4070M': {'brand': 'SBIG', 'name': 'STF-4070M', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'SBIG_Aluma_AC4040': {'brand': 'SBIG', 'name': 'Aluma AC4040', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 600, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'SBIG_Aluma_AC2020': {'brand': 'SBIG', 'name': 'Aluma AC2020', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 450, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'SBIG_STF_8050': {'brand': 'SBIG', 'name': 'STF-8050', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 650, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'SBIG_ST_10XME': {'brand': 'SBIG', 'name': 'ST-10XME', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'SBIG_ST_8XME': {'brand': 'SBIG', 'name': 'ST-8XME', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 450, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'SBIG_ST_7XME': {'brand': 'SBIG', 'name': 'ST-7XME', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 400, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}}

    @classmethod
    def SBIG_STF_8300M(cls):
        return cls.from_database(cls._DATABASE['SBIG_STF_8300M'])

    @classmethod
    def SBIG_STT_8300M(cls):
        return cls.from_database(cls._DATABASE['SBIG_STT_8300M'])

    @classmethod
    def SBIG_STX_16803(cls):
        return cls.from_database(cls._DATABASE['SBIG_STX_16803'])

    @classmethod
    def SBIG_STXL_11002(cls):
        return cls.from_database(cls._DATABASE['SBIG_STXL_11002'])

    @classmethod
    def SBIG_STF_8050M(cls):
        return cls.from_database(cls._DATABASE['SBIG_STF_8050M'])

    @classmethod
    def SBIG_STT_1603M(cls):
        return cls.from_database(cls._DATABASE['SBIG_STT_1603M'])

    @classmethod
    def SBIG_Aluma_AC694(cls):
        return cls.from_database(cls._DATABASE['SBIG_Aluma_AC694'])

    @classmethod
    def SBIG_STT_1603ME(cls):
        return cls.from_database(cls._DATABASE['SBIG_STT_1603ME'])

    @classmethod
    def SBIG_STT_3200ME(cls):
        return cls.from_database(cls._DATABASE['SBIG_STT_3200ME'])

    @classmethod
    def SBIG_ST_i(cls):
        return cls.from_database(cls._DATABASE['SBIG_ST_i'])

    @classmethod
    def SBIG_ST_402ME(cls):
        return cls.from_database(cls._DATABASE['SBIG_ST_402ME'])

    @classmethod
    def SBIG_ST_8300M(cls):
        return cls.from_database(cls._DATABASE['SBIG_ST_8300M'])

    @classmethod
    def SBIG_STF_4070M(cls):
        return cls.from_database(cls._DATABASE['SBIG_STF_4070M'])

    @classmethod
    def SBIG_Aluma_AC4040(cls):
        return cls.from_database(cls._DATABASE['SBIG_Aluma_AC4040'])

    @classmethod
    def SBIG_Aluma_AC2020(cls):
        return cls.from_database(cls._DATABASE['SBIG_Aluma_AC2020'])

    @classmethod
    def SBIG_STF_8050(cls):
        return cls.from_database(cls._DATABASE['SBIG_STF_8050'])

    @classmethod
    def SBIG_ST_10XME(cls):
        return cls.from_database(cls._DATABASE['SBIG_ST_10XME'])

    @classmethod
    def SBIG_ST_8XME(cls):
        return cls.from_database(cls._DATABASE['SBIG_ST_8XME'])

    @classmethod
    def SBIG_ST_7XME(cls):
        return cls.from_database(cls._DATABASE['SBIG_ST_7XME'])