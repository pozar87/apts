import numpy
from ...abstract import OpticalEquipment
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ....constants import GraphConstants
from enum import Enum
from typing import Optional
from ..base import TelescopeType, TubeMaterial, Telescope

class UnistellarTelescope(Telescope):
    _DATABASE = {'Unistellar_eVscope_2': {'brand': 'Unistellar', 'name': 'eVscope 2', 'type': 'type_telescope', 'optical_length': 0, 'mass': 9000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Unistellar_eQuinox_2': {'brand': 'Unistellar', 'name': 'eQuinox 2', 'type': 'type_telescope', 'optical_length': 0, 'mass': 7000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Unistellar_Odyssey': {'brand': 'Unistellar', 'name': 'Odyssey', 'type': 'type_telescope', 'optical_length': 0, 'mass': 5000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Unistellar_Odyssey_Pro': {'brand': 'Unistellar', 'name': 'Odyssey Pro', 'type': 'type_telescope', 'optical_length': 0, 'mass': 6000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Unistellar_eVscope_2(cls):
        return cls.from_database(cls._DATABASE['Unistellar_eVscope_2'])

    @classmethod
    def Unistellar_eQuinox_2(cls):
        return cls.from_database(cls._DATABASE['Unistellar_eQuinox_2'])

    @classmethod
    def Unistellar_Odyssey(cls):
        return cls.from_database(cls._DATABASE['Unistellar_Odyssey'])

    @classmethod
    def Unistellar_Odyssey_Pro(cls):
        return cls.from_database(cls._DATABASE['Unistellar_Odyssey_Pro'])