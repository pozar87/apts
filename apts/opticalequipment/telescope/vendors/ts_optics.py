import numpy
from ...abstract import OpticalEquipment
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ....constants import GraphConstants
from enum import Enum
from typing import Optional
from ..base import TelescopeType, TubeMaterial, Telescope

class Ts_opticsTelescope(Telescope):
    _DATABASE = {'TS_Optics_Photoline_72mm_APO': {'brand': 'TS-Optics', 'name': 'Photoline 72mm APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TS_Optics_Photoline_80mm_APO': {'brand': 'TS-Optics', 'name': 'Photoline 80mm APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TS_Optics_Photoline_100mm_APO': {'brand': 'TS-Optics', 'name': 'Photoline 100mm APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TS_Optics_Photoline_115mm_APO': {'brand': 'TS-Optics', 'name': 'Photoline 115mm APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 5500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TS_Optics_Photoline_130mm_APO': {'brand': 'TS-Optics', 'name': 'Photoline 130mm APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 6800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TS_Optics_ONTC_6_f_4_Newton': {'brand': 'TS-Optics', 'name': 'ONTC 6" f/4 Newton', 'type': 'type_telescope', 'optical_length': 0, 'mass': 5000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TS_Optics_ONTC_8_f_4_Newton': {'brand': 'TS-Optics', 'name': 'ONTC 8" f/4 Newton', 'type': 'type_telescope', 'optical_length': 0, 'mass': 8000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TS_Optics_ONTC_10_f_4_Newton': {'brand': 'TS-Optics', 'name': 'ONTC 10" f/4 Newton', 'type': 'type_telescope', 'optical_length': 0, 'mass': 12000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TS_Optics_Ritchey_Chretien_6': {'brand': 'TS-Optics', 'name': 'Ritchey-Chretien 6"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 5500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TS_Optics_Ritchey_Chretien_8': {'brand': 'TS-Optics', 'name': 'Ritchey-Chretien 8"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 9000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TS_Optics_Ritchey_Chretien_10': {'brand': 'TS-Optics', 'name': 'Ritchey-Chretien 10"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 13000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TS_Optics_Ritchey_Chretien_12': {'brand': 'TS-Optics', 'name': 'Ritchey-Chretien 12"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 18000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TS_Optics_PHOTON_6_f_9_Mak_Cass': {'brand': 'TS-Optics', 'name': 'PHOTON 6" f/9 Mak-Cass', 'type': 'type_telescope', 'optical_length': 0, 'mass': 5000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TS_Optics_CF_APO_80mm': {'brand': 'TS-Optics', 'name': 'CF-APO 80mm', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TS_Optics_CF_APO_102mm': {'brand': 'TS-Optics', 'name': 'CF-APO 102mm', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TS_Optics_CF_APO_130mm': {'brand': 'TS-Optics', 'name': 'CF-APO 130mm', 'type': 'type_refractor', 'optical_length': 0, 'mass': 7000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TS_Optics_CF_APO_152mm': {'brand': 'TS-Optics', 'name': 'CF-APO 152mm', 'type': 'type_refractor', 'optical_length': 0, 'mass': 10000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TS_Optics_Individual_65mm_Quad': {'brand': 'TS-Optics', 'name': 'Individual 65mm Quad', 'type': 'type_refractor', 'optical_length': 0, 'mass': 1800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TS_Optics_TS_6_f_6_Newton': {'brand': 'TS-Optics', 'name': 'TS 6" f/6 Newton', 'type': 'type_telescope', 'optical_length': 0, 'mass': 4800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TS_Optics_TS_8_f_5_Newton': {'brand': 'TS-Optics', 'name': 'TS 8" f/5 Newton', 'type': 'type_telescope', 'optical_length': 0, 'mass': 8200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TS_Optics_TS_8_f_4_Newton': {'brand': 'TS-Optics', 'name': 'TS 8" f/4 Newton', 'type': 'type_telescope', 'optical_length': 0, 'mass': 8000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TS_Optics_TS_10_f_4_Newton': {'brand': 'TS-Optics', 'name': 'TS 10" f/4 Newton', 'type': 'type_telescope', 'optical_length': 0, 'mass': 12000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TS_Optics_TS_10_f_5_Newton': {'brand': 'TS-Optics', 'name': 'TS 10" f/5 Newton', 'type': 'type_telescope', 'optical_length': 0, 'mass': 11500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TS_Optics_TS_12_f_4_Newton': {'brand': 'TS-Optics', 'name': 'TS 12" f/4 Newton', 'type': 'type_telescope', 'optical_length': 0, 'mass': 16000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TS_Optics_TS_12_f_5_Dobson': {'brand': 'TS-Optics', 'name': 'TS 12" f/5 Dobson', 'type': 'type_telescope', 'optical_length': 0, 'mass': 15000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TS_Optics_TS_14_f_4_6_Newton': {'brand': 'TS-Optics', 'name': 'TS 14" f/4.6 Newton', 'type': 'type_telescope', 'optical_length': 0, 'mass': 20000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TS_Optics_CF_APO_65mm_Quintuplet': {'brand': 'TS-Optics', 'name': 'CF-APO 65mm Quintuplet', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TS_Optics_CF_APO_90mm': {'brand': 'TS-Optics', 'name': 'CF-APO 90mm', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TS_Optics_RC_6_Pro': {'brand': 'TS-Optics', 'name': 'RC 6" Pro', 'type': 'type_telescope', 'optical_length': 0, 'mass': 5800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TS_Optics_RC_8_Pro': {'brand': 'TS-Optics', 'name': 'RC 8" Pro', 'type': 'type_telescope', 'optical_length': 0, 'mass': 9500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TS_Optics_RC_10_Pro': {'brand': 'TS-Optics', 'name': 'RC 10" Pro', 'type': 'type_telescope', 'optical_length': 0, 'mass': 13500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TS_Optics_RC_12_Pro': {'brand': 'TS-Optics', 'name': 'RC 12" Pro', 'type': 'type_telescope', 'optical_length': 0, 'mass': 18500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TS_Optics_ONTC_12_f_4': {'brand': 'TS-Optics', 'name': 'ONTC 12" f/4', 'type': 'type_telescope', 'optical_length': 0, 'mass': 18000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TS_Optics_ONTC_14_f_4': {'brand': 'TS-Optics', 'name': 'ONTC 14" f/4', 'type': 'type_telescope', 'optical_length': 0, 'mass': 22000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TS_Optics_ONTC_16_f_4': {'brand': 'TS-Optics', 'name': 'ONTC 16" f/4', 'type': 'type_telescope', 'optical_length': 0, 'mass': 28000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TS_Optics_Individual_80mm_Quad': {'brand': 'TS-Optics', 'name': 'Individual 80mm Quad', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TS_Optics_Individual_102mm_Quad': {'brand': 'TS-Optics', 'name': 'Individual 102mm Quad', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TS_Optics_Individual_115mm_Quad': {'brand': 'TS-Optics', 'name': 'Individual 115mm Quad', 'type': 'type_refractor', 'optical_length': 0, 'mass': 6000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'TS_Optics_Photoline_152mm_APO': {'brand': 'TS-Optics', 'name': 'Photoline 152mm APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 9500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def TS_Optics_Photoline_72mm_APO(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Photoline_72mm_APO'])

    @classmethod
    def TS_Optics_Photoline_80mm_APO(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Photoline_80mm_APO'])

    @classmethod
    def TS_Optics_Photoline_100mm_APO(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Photoline_100mm_APO'])

    @classmethod
    def TS_Optics_Photoline_115mm_APO(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Photoline_115mm_APO'])

    @classmethod
    def TS_Optics_Photoline_130mm_APO(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Photoline_130mm_APO'])

    @classmethod
    def TS_Optics_ONTC_6_f_4_Newton(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_ONTC_6_f_4_Newton'])

    @classmethod
    def TS_Optics_ONTC_8_f_4_Newton(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_ONTC_8_f_4_Newton'])

    @classmethod
    def TS_Optics_ONTC_10_f_4_Newton(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_ONTC_10_f_4_Newton'])

    @classmethod
    def TS_Optics_Ritchey_Chretien_6(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Ritchey_Chretien_6'])

    @classmethod
    def TS_Optics_Ritchey_Chretien_8(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Ritchey_Chretien_8'])

    @classmethod
    def TS_Optics_Ritchey_Chretien_10(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Ritchey_Chretien_10'])

    @classmethod
    def TS_Optics_Ritchey_Chretien_12(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Ritchey_Chretien_12'])

    @classmethod
    def TS_Optics_PHOTON_6_f_9_Mak_Cass(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_PHOTON_6_f_9_Mak_Cass'])

    @classmethod
    def TS_Optics_CF_APO_80mm(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_CF_APO_80mm'])

    @classmethod
    def TS_Optics_CF_APO_102mm(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_CF_APO_102mm'])

    @classmethod
    def TS_Optics_CF_APO_130mm(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_CF_APO_130mm'])

    @classmethod
    def TS_Optics_CF_APO_152mm(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_CF_APO_152mm'])

    @classmethod
    def TS_Optics_Individual_65mm_Quad(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Individual_65mm_Quad'])

    @classmethod
    def TS_Optics_TS_6_f_6_Newton(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_TS_6_f_6_Newton'])

    @classmethod
    def TS_Optics_TS_8_f_5_Newton(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_TS_8_f_5_Newton'])

    @classmethod
    def TS_Optics_TS_8_f_4_Newton(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_TS_8_f_4_Newton'])

    @classmethod
    def TS_Optics_TS_10_f_4_Newton(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_TS_10_f_4_Newton'])

    @classmethod
    def TS_Optics_TS_10_f_5_Newton(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_TS_10_f_5_Newton'])

    @classmethod
    def TS_Optics_TS_12_f_4_Newton(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_TS_12_f_4_Newton'])

    @classmethod
    def TS_Optics_TS_12_f_5_Dobson(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_TS_12_f_5_Dobson'])

    @classmethod
    def TS_Optics_TS_14_f_4_6_Newton(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_TS_14_f_4_6_Newton'])

    @classmethod
    def TS_Optics_CF_APO_65mm_Quintuplet(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_CF_APO_65mm_Quintuplet'])

    @classmethod
    def TS_Optics_CF_APO_90mm(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_CF_APO_90mm'])

    @classmethod
    def TS_Optics_RC_6_Pro(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_RC_6_Pro'])

    @classmethod
    def TS_Optics_RC_8_Pro(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_RC_8_Pro'])

    @classmethod
    def TS_Optics_RC_10_Pro(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_RC_10_Pro'])

    @classmethod
    def TS_Optics_RC_12_Pro(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_RC_12_Pro'])

    @classmethod
    def TS_Optics_ONTC_12_f_4(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_ONTC_12_f_4'])

    @classmethod
    def TS_Optics_ONTC_14_f_4(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_ONTC_14_f_4'])

    @classmethod
    def TS_Optics_ONTC_16_f_4(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_ONTC_16_f_4'])

    @classmethod
    def TS_Optics_Individual_80mm_Quad(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Individual_80mm_Quad'])

    @classmethod
    def TS_Optics_Individual_102mm_Quad(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Individual_102mm_Quad'])

    @classmethod
    def TS_Optics_Individual_115mm_Quad(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Individual_115mm_Quad'])

    @classmethod
    def TS_Optics_Photoline_152mm_APO(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_Photoline_152mm_APO'])