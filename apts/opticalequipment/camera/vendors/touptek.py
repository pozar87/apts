import numpy
import math
from typing import Any
from ...abstract import OutputOpticalEqipment
from ....constants import GraphConstants, OpticalType
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ..base import Camera

class TouptekCamera(Camera):
    _DATABASE = {'ToupTek_ATR3CMOS26000KPA': {'brand': 'ToupTek', 'name': 'ATR3CMOS26000KPA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 700, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ToupTek_ATR3CMOS16000KPA': {'brand': 'ToupTek', 'name': 'ATR3CMOS16000KPA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ToupTek_ATR3CMOS02000KMA': {'brand': 'ToupTek', 'name': 'ATR3CMOS02000KMA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 350, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ToupTek_ATR3CMOS06300KPA': {'brand': 'ToupTek', 'name': 'ATR3CMOS06300KPA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 450, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ToupTek_ATR3CMOS26000KMA': {'brand': 'ToupTek', 'name': 'ATR3CMOS26000KMA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 720, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ToupTek_ATR3CMOS07100KPA': {'brand': 'ToupTek', 'name': 'ATR3CMOS07100KPA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 480, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ToupTek_ATR3CMOS21000KPA': {'brand': 'ToupTek', 'name': 'ATR3CMOS21000KPA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 600, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ToupTek_GP_CMOS02000KMA': {'brand': 'ToupTek', 'name': 'GP-CMOS02000KMA', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ToupTek_GP_CMOS02900KPA': {'brand': 'ToupTek', 'name': 'GP-CMOS02900KPA', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ToupTek_GP_CMOS04600KPA': {'brand': 'ToupTek', 'name': 'GP-CMOS04600KPA', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ToupTek_ATR3CMOS09440KPA': {'brand': 'ToupTek', 'name': 'ATR3CMOS09440KPA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 520, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ToupTek_ATR3CMOS04600KPA': {'brand': 'ToupTek', 'name': 'ATR3CMOS04600KPA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 420, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ToupTek_ATR3CMOS12000KPA': {'brand': 'ToupTek', 'name': 'ATR3CMOS12000KPA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 550, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ToupTek_ATR3CMOS09120KPA': {'brand': 'ToupTek', 'name': 'ATR3CMOS09120KPA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ToupTek_ATR3CMOS02100KPA': {'brand': 'ToupTek', 'name': 'ATR3CMOS02100KPA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 360, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ToupTek_ATR3CMOS08000KPA': {'brand': 'ToupTek', 'name': 'ATR3CMOS08000KPA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 480, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ToupTek_GCMOS01200KPA': {'brand': 'ToupTek', 'name': 'GCMOS01200KPA', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 70, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ToupTek_GCMOS01200KMA': {'brand': 'ToupTek', 'name': 'GCMOS01200KMA', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 70, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ToupTek_ATR3CMOS16000KMA': {'brand': 'ToupTek', 'name': 'ATR3CMOS16000KMA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 510, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ToupTek_ATR3CMOS02900KPA': {'brand': 'ToupTek', 'name': 'ATR3CMOS02900KPA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 370, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ToupTek_ATR3CMOS04600KMA': {'brand': 'ToupTek', 'name': 'ATR3CMOS04600KMA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 430, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ToupTek_ATR3CMOS09440KMA': {'brand': 'ToupTek', 'name': 'ATR3CMOS09440KMA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 530, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ToupTek_ATR3CMOS12000KMA': {'brand': 'ToupTek', 'name': 'ATR3CMOS12000KMA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 560, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ToupTek_ATR3CMOS09120KMA': {'brand': 'ToupTek', 'name': 'ATR3CMOS09120KMA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 510, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ToupTek_ATR3CMOS02100KMA': {'brand': 'ToupTek', 'name': 'ATR3CMOS02100KMA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 365, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ToupTek_ATR3CMOS08000KMA': {'brand': 'ToupTek', 'name': 'ATR3CMOS08000KMA', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 490, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ToupTek_GP_CMOS01200KPA': {'brand': 'ToupTek', 'name': 'GP-CMOS01200KPA', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 65, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ToupTek_GP_CMOS01200KMA': {'brand': 'ToupTek', 'name': 'GP-CMOS01200KMA', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 65, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ToupTek_GP_CMOS05780KPA': {'brand': 'ToupTek', 'name': 'GP-CMOS05780KPA', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 85, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'ToupTek_GP_CMOS05780KMA': {'brand': 'ToupTek', 'name': 'GP-CMOS05780KMA', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 85, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}}

    @classmethod
    def ToupTek_ATR3CMOS26000KPA(cls):
        return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS26000KPA'])

    @classmethod
    def ToupTek_ATR3CMOS16000KPA(cls):
        return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS16000KPA'])

    @classmethod
    def ToupTek_ATR3CMOS02000KMA(cls):
        return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS02000KMA'])

    @classmethod
    def ToupTek_ATR3CMOS06300KPA(cls):
        return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS06300KPA'])

    @classmethod
    def ToupTek_ATR3CMOS26000KMA(cls):
        return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS26000KMA'])

    @classmethod
    def ToupTek_ATR3CMOS07100KPA(cls):
        return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS07100KPA'])

    @classmethod
    def ToupTek_ATR3CMOS21000KPA(cls):
        return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS21000KPA'])

    @classmethod
    def ToupTek_GP_CMOS02000KMA(cls):
        return cls.from_database(cls._DATABASE['ToupTek_GP_CMOS02000KMA'])

    @classmethod
    def ToupTek_GP_CMOS02900KPA(cls):
        return cls.from_database(cls._DATABASE['ToupTek_GP_CMOS02900KPA'])

    @classmethod
    def ToupTek_GP_CMOS04600KPA(cls):
        return cls.from_database(cls._DATABASE['ToupTek_GP_CMOS04600KPA'])

    @classmethod
    def ToupTek_ATR3CMOS09440KPA(cls):
        return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS09440KPA'])

    @classmethod
    def ToupTek_ATR3CMOS04600KPA(cls):
        return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS04600KPA'])

    @classmethod
    def ToupTek_ATR3CMOS12000KPA(cls):
        return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS12000KPA'])

    @classmethod
    def ToupTek_ATR3CMOS09120KPA(cls):
        return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS09120KPA'])

    @classmethod
    def ToupTek_ATR3CMOS02100KPA(cls):
        return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS02100KPA'])

    @classmethod
    def ToupTek_ATR3CMOS08000KPA(cls):
        return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS08000KPA'])

    @classmethod
    def ToupTek_GCMOS01200KPA(cls):
        return cls.from_database(cls._DATABASE['ToupTek_GCMOS01200KPA'])

    @classmethod
    def ToupTek_GCMOS01200KMA(cls):
        return cls.from_database(cls._DATABASE['ToupTek_GCMOS01200KMA'])

    @classmethod
    def ToupTek_ATR3CMOS16000KMA(cls):
        return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS16000KMA'])

    @classmethod
    def ToupTek_ATR3CMOS02900KPA(cls):
        return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS02900KPA'])

    @classmethod
    def ToupTek_ATR3CMOS04600KMA(cls):
        return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS04600KMA'])

    @classmethod
    def ToupTek_ATR3CMOS09440KMA(cls):
        return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS09440KMA'])

    @classmethod
    def ToupTek_ATR3CMOS12000KMA(cls):
        return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS12000KMA'])

    @classmethod
    def ToupTek_ATR3CMOS09120KMA(cls):
        return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS09120KMA'])

    @classmethod
    def ToupTek_ATR3CMOS02100KMA(cls):
        return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS02100KMA'])

    @classmethod
    def ToupTek_ATR3CMOS08000KMA(cls):
        return cls.from_database(cls._DATABASE['ToupTek_ATR3CMOS08000KMA'])

    @classmethod
    def ToupTek_GP_CMOS01200KPA(cls):
        return cls.from_database(cls._DATABASE['ToupTek_GP_CMOS01200KPA'])

    @classmethod
    def ToupTek_GP_CMOS01200KMA(cls):
        return cls.from_database(cls._DATABASE['ToupTek_GP_CMOS01200KMA'])

    @classmethod
    def ToupTek_GP_CMOS05780KPA(cls):
        return cls.from_database(cls._DATABASE['ToupTek_GP_CMOS05780KPA'])

    @classmethod
    def ToupTek_GP_CMOS05780KMA(cls):
        return cls.from_database(cls._DATABASE['ToupTek_GP_CMOS05780KMA'])