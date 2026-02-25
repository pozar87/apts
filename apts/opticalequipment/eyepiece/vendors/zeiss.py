from ...abstract import OutputOpticalEqipment
from ....constants import GraphConstants, OpticalType
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ..base import Eyepiece

class ZeissEyepiece(Eyepiece):
    _DATABASE = {'Zeiss_Abbe_Ortho_4mm': {'brand': 'Zeiss', 'name': 'Abbe Ortho 4mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 250, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Zeiss_Abbe_Ortho_6mm': {'brand': 'Zeiss', 'name': 'Abbe Ortho 6mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 260, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Zeiss_Abbe_Ortho_10mm': {'brand': 'Zeiss', 'name': 'Abbe Ortho 10mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 280, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Zeiss_Abbe_Ortho_16mm': {'brand': 'Zeiss', 'name': 'Abbe Ortho 16mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 320, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Zeiss_Abbe_Ortho_25mm': {'brand': 'Zeiss', 'name': 'Abbe Ortho 25mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 380, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Zeiss_Abbe_Ortho_4mm(cls):
        return cls.from_database(cls._DATABASE['Zeiss_Abbe_Ortho_4mm'])

    @classmethod
    def Zeiss_Abbe_Ortho_6mm(cls):
        return cls.from_database(cls._DATABASE['Zeiss_Abbe_Ortho_6mm'])

    @classmethod
    def Zeiss_Abbe_Ortho_10mm(cls):
        return cls.from_database(cls._DATABASE['Zeiss_Abbe_Ortho_10mm'])

    @classmethod
    def Zeiss_Abbe_Ortho_16mm(cls):
        return cls.from_database(cls._DATABASE['Zeiss_Abbe_Ortho_16mm'])

    @classmethod
    def Zeiss_Abbe_Ortho_25mm(cls):
        return cls.from_database(cls._DATABASE['Zeiss_Abbe_Ortho_25mm'])