import numpy
from ...abstract import OpticalEquipment
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ....constants import GraphConstants
from enum import Enum
from typing import Optional
from ..base import TelescopeType, TubeMaterial, Telescope

class VixenTelescope(Telescope):
    _DATABASE = {'Vixen_VC200L': {'brand': 'Vixen', 'name': 'VC200L', 'type': 'type_telescope', 'optical_length': 0, 'mass': 6900, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_VSD100_F3_8': {'brand': 'Vixen', 'name': 'VSD100 F3.8', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_VSD90SS': {'brand': 'Vixen', 'name': 'VSD90SS', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_A80Mf': {'brand': 'Vixen', 'name': 'A80Mf', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_A80M': {'brand': 'Vixen', 'name': 'A80M', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2700, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_SD81S': {'brand': 'Vixen', 'name': 'SD81S', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_SD103S': {'brand': 'Vixen', 'name': 'SD103S', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_SD115S': {'brand': 'Vixen', 'name': 'SD115S', 'type': 'type_refractor', 'optical_length': 0, 'mass': 6000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_AX103S': {'brand': 'Vixen', 'name': 'AX103S', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_FL55SS': {'brand': 'Vixen', 'name': 'FL55SS', 'type': 'type_refractor', 'optical_length': 0, 'mass': 1500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_R200SS': {'brand': 'Vixen', 'name': 'R200SS', 'type': 'type_telescope', 'optical_length': 0, 'mass': 5500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_VMC200L': {'brand': 'Vixen', 'name': 'VMC200L', 'type': 'type_telescope', 'optical_length': 0, 'mass': 6800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_A62SS': {'brand': 'Vixen', 'name': 'A62SS', 'type': 'type_refractor', 'optical_length': 0, 'mass': 1100, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_A70Lf': {'brand': 'Vixen', 'name': 'A70Lf', 'type': 'type_refractor', 'optical_length': 0, 'mass': 1400, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_A105M': {'brand': 'Vixen', 'name': 'A105M', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_VSD100_F3_8_V2': {'brand': 'Vixen', 'name': 'VSD100 F3.8 V2', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_R130Sf': {'brand': 'Vixen', 'name': 'R130Sf', 'type': 'type_telescope', 'optical_length': 0, 'mass': 3000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_VMC95L': {'brand': 'Vixen', 'name': 'VMC95L', 'type': 'type_telescope', 'optical_length': 0, 'mass': 2000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_VMC110L': {'brand': 'Vixen', 'name': 'VMC110L', 'type': 'type_telescope', 'optical_length': 0, 'mass': 2800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_VMC260L': {'brand': 'Vixen', 'name': 'VMC260L', 'type': 'type_telescope', 'optical_length': 0, 'mass': 12000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_ED80Sf': {'brand': 'Vixen', 'name': 'ED80Sf', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_ED81SII': {'brand': 'Vixen', 'name': 'ED81SII', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_ED103S': {'brand': 'Vixen', 'name': 'ED103S', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_ED115S_v2': {'brand': 'Vixen', 'name': 'ED115S v2', 'type': 'type_refractor', 'optical_length': 0, 'mass': 6200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_NA140SSf': {'brand': 'Vixen', 'name': 'NA140SSf', 'type': 'type_refractor', 'optical_length': 0, 'mass': 6000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_VC200L_v2': {'brand': 'Vixen', 'name': 'VC200L v2', 'type': 'type_telescope', 'optical_length': 0, 'mass': 7000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_VMC200L_v2': {'brand': 'Vixen', 'name': 'VMC200L v2', 'type': 'type_telescope', 'optical_length': 0, 'mass': 6900, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_R200SS_v2': {'brand': 'Vixen', 'name': 'R200SS v2', 'type': 'type_telescope', 'optical_length': 0, 'mass': 5600, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Vixen_VC200L(cls):
        return cls.from_database(cls._DATABASE['Vixen_VC200L'])

    @classmethod
    def Vixen_VSD100_F3_8(cls):
        return cls.from_database(cls._DATABASE['Vixen_VSD100_F3_8'])

    @classmethod
    def Vixen_VSD90SS(cls):
        return cls.from_database(cls._DATABASE['Vixen_VSD90SS'])

    @classmethod
    def Vixen_A80Mf(cls):
        return cls.from_database(cls._DATABASE['Vixen_A80Mf'])

    @classmethod
    def Vixen_A80M(cls):
        return cls.from_database(cls._DATABASE['Vixen_A80M'])

    @classmethod
    def Vixen_SD81S(cls):
        return cls.from_database(cls._DATABASE['Vixen_SD81S'])

    @classmethod
    def Vixen_SD103S(cls):
        return cls.from_database(cls._DATABASE['Vixen_SD103S'])

    @classmethod
    def Vixen_SD115S(cls):
        return cls.from_database(cls._DATABASE['Vixen_SD115S'])

    @classmethod
    def Vixen_AX103S(cls):
        return cls.from_database(cls._DATABASE['Vixen_AX103S'])

    @classmethod
    def Vixen_FL55SS(cls):
        return cls.from_database(cls._DATABASE['Vixen_FL55SS'])

    @classmethod
    def Vixen_R200SS(cls):
        return cls.from_database(cls._DATABASE['Vixen_R200SS'])

    @classmethod
    def Vixen_VMC200L(cls):
        return cls.from_database(cls._DATABASE['Vixen_VMC200L'])

    @classmethod
    def Vixen_A62SS(cls):
        return cls.from_database(cls._DATABASE['Vixen_A62SS'])

    @classmethod
    def Vixen_A70Lf(cls):
        return cls.from_database(cls._DATABASE['Vixen_A70Lf'])

    @classmethod
    def Vixen_A105M(cls):
        return cls.from_database(cls._DATABASE['Vixen_A105M'])

    @classmethod
    def Vixen_VSD100_F3_8_V2(cls):
        return cls.from_database(cls._DATABASE['Vixen_VSD100_F3_8_V2'])

    @classmethod
    def Vixen_R130Sf(cls):
        return cls.from_database(cls._DATABASE['Vixen_R130Sf'])

    @classmethod
    def Vixen_VMC95L(cls):
        return cls.from_database(cls._DATABASE['Vixen_VMC95L'])

    @classmethod
    def Vixen_VMC110L(cls):
        return cls.from_database(cls._DATABASE['Vixen_VMC110L'])

    @classmethod
    def Vixen_VMC260L(cls):
        return cls.from_database(cls._DATABASE['Vixen_VMC260L'])

    @classmethod
    def Vixen_ED80Sf(cls):
        return cls.from_database(cls._DATABASE['Vixen_ED80Sf'])

    @classmethod
    def Vixen_ED81SII(cls):
        return cls.from_database(cls._DATABASE['Vixen_ED81SII'])

    @classmethod
    def Vixen_ED103S(cls):
        return cls.from_database(cls._DATABASE['Vixen_ED103S'])

    @classmethod
    def Vixen_ED115S_v2(cls):
        return cls.from_database(cls._DATABASE['Vixen_ED115S_v2'])

    @classmethod
    def Vixen_NA140SSf(cls):
        return cls.from_database(cls._DATABASE['Vixen_NA140SSf'])

    @classmethod
    def Vixen_VC200L_v2(cls):
        return cls.from_database(cls._DATABASE['Vixen_VC200L_v2'])

    @classmethod
    def Vixen_VMC200L_v2(cls):
        return cls.from_database(cls._DATABASE['Vixen_VMC200L_v2'])

    @classmethod
    def Vixen_R200SS_v2(cls):
        return cls.from_database(cls._DATABASE['Vixen_R200SS_v2'])