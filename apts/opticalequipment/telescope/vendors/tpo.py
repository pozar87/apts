import numpy
from ...abstract import OpticalEquipment
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ....constants import GraphConstants
from enum import Enum
from typing import Optional
from ..base import TelescopeType, TubeMaterial, Telescope

class TpoTelescope(Telescope):
    _DATABASE = {'TPO_RC_6': {'brand': 'TPO', 'name': 'RC 6"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 5200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TPO_RC_8': {'brand': 'TPO', 'name': 'RC 8"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 8700, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TPO_RC_10': {'brand': 'TPO', 'name': 'RC 10"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 12500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TPO_RC_12': {'brand': 'TPO', 'name': 'RC 12"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 17000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TPO_RC_14': {'brand': 'TPO', 'name': 'RC 14"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 22000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TPO_TPO_6_f_4_Newton': {'brand': 'TPO', 'name': 'TPO 6" f/4 Newton', 'type': 'type_telescope', 'optical_length': 0, 'mass': 4800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TPO_TPO_8_f_4_Newton': {'brand': 'TPO', 'name': 'TPO 8" f/4 Newton', 'type': 'type_telescope', 'optical_length': 0, 'mass': 7800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TPO_TPO_10_f_4_Newton': {'brand': 'TPO', 'name': 'TPO 10" f/4 Newton', 'type': 'type_telescope', 'optical_length': 0, 'mass': 12000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TPO_TPO_80mm_ED_APO': {'brand': 'TPO', 'name': 'TPO 80mm ED APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2600, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TPO_TPO_102mm_ED_APO': {'brand': 'TPO', 'name': 'TPO 102mm ED APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TPO_UltraWide_6_f_2_8_Astrograph': {'brand': 'TPO', 'name': 'UltraWide 6" f/2.8 Astrograph', 'type': 'type_telescope', 'optical_length': 0, 'mass': 6000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def TPO_RC_6(cls):
        return cls.from_database(cls._DATABASE['TPO_RC_6'])

    @classmethod
    def TPO_RC_8(cls):
        return cls.from_database(cls._DATABASE['TPO_RC_8'])

    @classmethod
    def TPO_RC_10(cls):
        return cls.from_database(cls._DATABASE['TPO_RC_10'])

    @classmethod
    def TPO_RC_12(cls):
        return cls.from_database(cls._DATABASE['TPO_RC_12'])

    @classmethod
    def TPO_RC_14(cls):
        return cls.from_database(cls._DATABASE['TPO_RC_14'])

    @classmethod
    def TPO_TPO_6_f_4_Newton(cls):
        return cls.from_database(cls._DATABASE['TPO_TPO_6_f_4_Newton'])

    @classmethod
    def TPO_TPO_8_f_4_Newton(cls):
        return cls.from_database(cls._DATABASE['TPO_TPO_8_f_4_Newton'])

    @classmethod
    def TPO_TPO_10_f_4_Newton(cls):
        return cls.from_database(cls._DATABASE['TPO_TPO_10_f_4_Newton'])

    @classmethod
    def TPO_TPO_80mm_ED_APO(cls):
        return cls.from_database(cls._DATABASE['TPO_TPO_80mm_ED_APO'])

    @classmethod
    def TPO_TPO_102mm_ED_APO(cls):
        return cls.from_database(cls._DATABASE['TPO_TPO_102mm_ED_APO'])

    @classmethod
    def TPO_UltraWide_6_f_2_8_Astrograph(cls):
        return cls.from_database(cls._DATABASE['TPO_UltraWide_6_f_2_8_Astrograph'])