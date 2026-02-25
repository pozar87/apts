import numpy
from ...abstract import OpticalEquipment
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ....constants import GraphConstants
from enum import Enum
from typing import Optional
from ..base import TelescopeType, TubeMaterial, Telescope

class SaxonTelescope(Telescope):
    _DATABASE = {'Saxon_Saxon_72ED': {'brand': 'Saxon', 'name': 'Saxon 72ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 1800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Saxon_Saxon_80ED': {'brand': 'Saxon', 'name': 'Saxon 80ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2400, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Saxon_Saxon_102ED': {'brand': 'Saxon', 'name': 'Saxon 102ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Saxon_Saxon_127_Mak': {'brand': 'Saxon', 'name': 'Saxon 127 Mak', 'type': 'type_telescope', 'optical_length': 0, 'mass': 3400, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Saxon_Saxon_150_Mak': {'brand': 'Saxon', 'name': 'Saxon 150 Mak', 'type': 'type_telescope', 'optical_length': 0, 'mass': 5000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Saxon_Saxon_200P_Dob': {'brand': 'Saxon', 'name': 'Saxon 200P Dob', 'type': 'type_telescope', 'optical_length': 0, 'mass': 8000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Saxon_Saxon_250P_Dob': {'brand': 'Saxon', 'name': 'Saxon 250P Dob', 'type': 'type_telescope', 'optical_length': 0, 'mass': 11000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Saxon_Saxon_72ED(cls):
        return cls.from_database(cls._DATABASE['Saxon_Saxon_72ED'])

    @classmethod
    def Saxon_Saxon_80ED(cls):
        return cls.from_database(cls._DATABASE['Saxon_Saxon_80ED'])

    @classmethod
    def Saxon_Saxon_102ED(cls):
        return cls.from_database(cls._DATABASE['Saxon_Saxon_102ED'])

    @classmethod
    def Saxon_Saxon_127_Mak(cls):
        return cls.from_database(cls._DATABASE['Saxon_Saxon_127_Mak'])

    @classmethod
    def Saxon_Saxon_150_Mak(cls):
        return cls.from_database(cls._DATABASE['Saxon_Saxon_150_Mak'])

    @classmethod
    def Saxon_Saxon_200P_Dob(cls):
        return cls.from_database(cls._DATABASE['Saxon_Saxon_200P_Dob'])

    @classmethod
    def Saxon_Saxon_250P_Dob(cls):
        return cls.from_database(cls._DATABASE['Saxon_Saxon_250P_Dob'])