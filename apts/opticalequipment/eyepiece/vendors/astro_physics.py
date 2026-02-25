from ...abstract import OutputOpticalEqipment
from ....constants import GraphConstants, OpticalType
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ..base import Eyepiece

class Astro_physicsEyepiece(Eyepiece):
    _DATABASE = {'Astro_Physics_MaxView_10mm': {'brand': 'Astro-Physics', 'name': 'MaxView 10mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 200, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Astro_Physics_MaxView_15mm': {'brand': 'Astro-Physics', 'name': 'MaxView 15mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 230, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Astro_Physics_MaxView_20mm': {'brand': 'Astro-Physics', 'name': 'MaxView 20mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 250, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Astro_Physics_MaxView_25mm': {'brand': 'Astro-Physics', 'name': 'MaxView 25mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 280, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Astro_Physics_MaxView_10mm(cls):
        return cls.from_database(cls._DATABASE['Astro_Physics_MaxView_10mm'])

    @classmethod
    def Astro_Physics_MaxView_15mm(cls):
        return cls.from_database(cls._DATABASE['Astro_Physics_MaxView_15mm'])

    @classmethod
    def Astro_Physics_MaxView_20mm(cls):
        return cls.from_database(cls._DATABASE['Astro_Physics_MaxView_20mm'])

    @classmethod
    def Astro_Physics_MaxView_25mm(cls):
        return cls.from_database(cls._DATABASE['Astro_Physics_MaxView_25mm'])