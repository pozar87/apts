from ...abstract import OutputOpticalEqipment
from ....constants import GraphConstants, OpticalType
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ..base import Eyepiece

class William_opticsEyepiece(Eyepiece):
    _DATABASE = {'William_Optics_SWAN_3_5mm': {'brand': 'William Optics', 'name': 'SWAN 3.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 170, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'William_Optics_SWAN_7mm': {'brand': 'William Optics', 'name': 'SWAN 7mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 185, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'William_Optics_SWAN_11mm': {'brand': 'William Optics', 'name': 'SWAN 11mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 200, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'William_Optics_SWAN_16mm': {'brand': 'William Optics', 'name': 'SWAN 16mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 230, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'William_Optics_SWAN_20mm': {'brand': 'William Optics', 'name': 'SWAN 20mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 250, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'William_Optics_SWAN_33mm': {'brand': 'William Optics', 'name': 'SWAN 33mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 500, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'William_Optics_UWAN_3mm': {'brand': 'William Optics', 'name': 'UWAN 3mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 200, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'William_Optics_UWAN_6mm': {'brand': 'William Optics', 'name': 'UWAN 6mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 210, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'William_Optics_UWAN_10mm': {'brand': 'William Optics', 'name': 'UWAN 10mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 230, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'William_Optics_UWAN_15mm': {'brand': 'William Optics', 'name': 'UWAN 15mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 250, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'William_Optics_UWAN_20mm': {'brand': 'William Optics', 'name': 'UWAN 20mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 270, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'William_Optics_SPL_3mm': {'brand': 'William Optics', 'name': 'SPL 3mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 160, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'William_Optics_SPL_6mm': {'brand': 'William Optics', 'name': 'SPL 6mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 165, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'William_Optics_SPL_10mm': {'brand': 'William Optics', 'name': 'SPL 10mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 175, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'William_Optics_SPL_15mm': {'brand': 'William Optics', 'name': 'SPL 15mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 185, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'William_Optics_SPL_20mm': {'brand': 'William Optics', 'name': 'SPL 20mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 195, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'William_Optics_Pleiades_3mm_55': {'brand': 'William Optics', 'name': 'Pleiades 3mm 55°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 170, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'William_Optics_Pleiades_6mm_55': {'brand': 'William Optics', 'name': 'Pleiades 6mm 55°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 180, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'William_Optics_Pleiades_10mm_55': {'brand': 'William Optics', 'name': 'Pleiades 10mm 55°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 195, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'William_Optics_Pleiades_15mm_55': {'brand': 'William Optics', 'name': 'Pleiades 15mm 55°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 215, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'William_Optics_Pleiades_20mm_55': {'brand': 'William Optics', 'name': 'Pleiades 20mm 55°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 240, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'William_Optics_XWA_3_5mm_110': {'brand': 'William Optics', 'name': 'XWA 3.5mm 110°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 280, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'William_Optics_XWA_7mm_110': {'brand': 'William Optics', 'name': 'XWA 7mm 110°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 300, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'William_Optics_XWA_13mm_110': {'brand': 'William Optics', 'name': 'XWA 13mm 110°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 350, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'William_Optics_XWA_20mm_110': {'brand': 'William Optics', 'name': 'XWA 20mm 110°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 500, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def William_Optics_SWAN_3_5mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_SWAN_3_5mm'])

    @classmethod
    def William_Optics_SWAN_7mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_SWAN_7mm'])

    @classmethod
    def William_Optics_SWAN_11mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_SWAN_11mm'])

    @classmethod
    def William_Optics_SWAN_16mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_SWAN_16mm'])

    @classmethod
    def William_Optics_SWAN_20mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_SWAN_20mm'])

    @classmethod
    def William_Optics_SWAN_33mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_SWAN_33mm'])

    @classmethod
    def William_Optics_UWAN_3mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_UWAN_3mm'])

    @classmethod
    def William_Optics_UWAN_6mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_UWAN_6mm'])

    @classmethod
    def William_Optics_UWAN_10mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_UWAN_10mm'])

    @classmethod
    def William_Optics_UWAN_15mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_UWAN_15mm'])

    @classmethod
    def William_Optics_UWAN_20mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_UWAN_20mm'])

    @classmethod
    def William_Optics_SPL_3mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_SPL_3mm'])

    @classmethod
    def William_Optics_SPL_6mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_SPL_6mm'])

    @classmethod
    def William_Optics_SPL_10mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_SPL_10mm'])

    @classmethod
    def William_Optics_SPL_15mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_SPL_15mm'])

    @classmethod
    def William_Optics_SPL_20mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_SPL_20mm'])

    @classmethod
    def William_Optics_Pleiades_3mm_55(cls):
        return cls.from_database(cls._DATABASE['William_Optics_Pleiades_3mm_55'])

    @classmethod
    def William_Optics_Pleiades_6mm_55(cls):
        return cls.from_database(cls._DATABASE['William_Optics_Pleiades_6mm_55'])

    @classmethod
    def William_Optics_Pleiades_10mm_55(cls):
        return cls.from_database(cls._DATABASE['William_Optics_Pleiades_10mm_55'])

    @classmethod
    def William_Optics_Pleiades_15mm_55(cls):
        return cls.from_database(cls._DATABASE['William_Optics_Pleiades_15mm_55'])

    @classmethod
    def William_Optics_Pleiades_20mm_55(cls):
        return cls.from_database(cls._DATABASE['William_Optics_Pleiades_20mm_55'])

    @classmethod
    def William_Optics_XWA_3_5mm_110(cls):
        return cls.from_database(cls._DATABASE['William_Optics_XWA_3_5mm_110'])

    @classmethod
    def William_Optics_XWA_7mm_110(cls):
        return cls.from_database(cls._DATABASE['William_Optics_XWA_7mm_110'])

    @classmethod
    def William_Optics_XWA_13mm_110(cls):
        return cls.from_database(cls._DATABASE['William_Optics_XWA_13mm_110'])

    @classmethod
    def William_Optics_XWA_20mm_110(cls):
        return cls.from_database(cls._DATABASE['William_Optics_XWA_20mm_110'])