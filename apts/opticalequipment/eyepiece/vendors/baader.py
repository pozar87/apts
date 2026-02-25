from ...abstract import OutputOpticalEqipment
from ....constants import GraphConstants, OpticalType
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ..base import Eyepiece

class BaaderEyepiece(Eyepiece):
    _DATABASE = {'Baader_Hyperion_5mm': {'brand': 'Baader', 'name': 'Hyperion 5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 170, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Baader_Hyperion_8mm': {'brand': 'Baader', 'name': 'Hyperion 8mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 180, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Baader_Hyperion_10mm': {'brand': 'Baader', 'name': 'Hyperion 10mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 190, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Baader_Hyperion_13mm': {'brand': 'Baader', 'name': 'Hyperion 13mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 200, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Baader_Hyperion_17mm': {'brand': 'Baader', 'name': 'Hyperion 17mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 220, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Baader_Hyperion_21mm': {'brand': 'Baader', 'name': 'Hyperion 21mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 240, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Baader_Hyperion_24mm': {'brand': 'Baader', 'name': 'Hyperion 24mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 260, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Baader_Hyperion_36mm': {'brand': 'Baader', 'name': 'Hyperion 36mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 400, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Baader_Morpheus_4_5mm': {'brand': 'Baader', 'name': 'Morpheus 4.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 200, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Baader_Morpheus_6_5mm': {'brand': 'Baader', 'name': 'Morpheus 6.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 220, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Baader_Morpheus_9mm': {'brand': 'Baader', 'name': 'Morpheus 9mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 230, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Baader_Morpheus_12_5mm': {'brand': 'Baader', 'name': 'Morpheus 12.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 250, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Baader_Morpheus_14mm': {'brand': 'Baader', 'name': 'Morpheus 14mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 260, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Baader_Morpheus_17_5mm': {'brand': 'Baader', 'name': 'Morpheus 17.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 280, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Baader_Classic_Ortho_6mm': {'brand': 'Baader', 'name': 'Classic Ortho 6mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 80, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Baader_Classic_Ortho_10mm': {'brand': 'Baader', 'name': 'Classic Ortho 10mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 85, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Baader_Classic_Ortho_18mm': {'brand': 'Baader', 'name': 'Classic Ortho 18mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 90, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Baader_Hyperion_Mark_IV_8_24mm_Zoom': {'brand': 'Baader', 'name': 'Hyperion Mark IV 8-24mm Zoom', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 400, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Baader_Classic_Ortho_3_5mm_v2': {'brand': 'Baader', 'name': 'Classic Ortho 3.5mm (v2)', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 75, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Baader_Classic_Ortho_5mm_v2': {'brand': 'Baader', 'name': 'Classic Ortho 5mm (v2)', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 78, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Baader_Classic_Ortho_7mm_v2': {'brand': 'Baader', 'name': 'Classic Ortho 7mm (v2)', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 82, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Baader_Classic_Ortho_12_5mm_v2': {'brand': 'Baader', 'name': 'Classic Ortho 12.5mm (v2)', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 88, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Baader_Classic_Ortho_18mm_v2': {'brand': 'Baader', 'name': 'Classic Ortho 18mm (v2)', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 92, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Baader_Classic_Ortho_25mm_v2': {'brand': 'Baader', 'name': 'Classic Ortho 25mm (v2)', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 100, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Baader_Genuine_Ortho_4mm': {'brand': 'Baader', 'name': 'Genuine Ortho 4mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 85, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Baader_Genuine_Ortho_5mm': {'brand': 'Baader', 'name': 'Genuine Ortho 5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 88, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Baader_Genuine_Ortho_6mm': {'brand': 'Baader', 'name': 'Genuine Ortho 6mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 92, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Baader_Genuine_Ortho_7mm': {'brand': 'Baader', 'name': 'Genuine Ortho 7mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 95, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Baader_Genuine_Ortho_9mm': {'brand': 'Baader', 'name': 'Genuine Ortho 9mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 100, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Baader_Genuine_Ortho_10mm': {'brand': 'Baader', 'name': 'Genuine Ortho 10mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 105, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Baader_Genuine_Ortho_12_5mm': {'brand': 'Baader', 'name': 'Genuine Ortho 12.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 112, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Baader_Genuine_Ortho_18mm': {'brand': 'Baader', 'name': 'Genuine Ortho 18mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 128, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Baader_Genuine_Ortho_25mm': {'brand': 'Baader', 'name': 'Genuine Ortho 25mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 145, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Baader_Micro_Guide_Eyepiece_12_5mm': {'brand': 'Baader', 'name': 'Micro Guide Eyepiece 12.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 200, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Baader_Hyperion_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_Hyperion_5mm'])

    @classmethod
    def Baader_Hyperion_8mm(cls):
        return cls.from_database(cls._DATABASE['Baader_Hyperion_8mm'])

    @classmethod
    def Baader_Hyperion_10mm(cls):
        return cls.from_database(cls._DATABASE['Baader_Hyperion_10mm'])

    @classmethod
    def Baader_Hyperion_13mm(cls):
        return cls.from_database(cls._DATABASE['Baader_Hyperion_13mm'])

    @classmethod
    def Baader_Hyperion_17mm(cls):
        return cls.from_database(cls._DATABASE['Baader_Hyperion_17mm'])

    @classmethod
    def Baader_Hyperion_21mm(cls):
        return cls.from_database(cls._DATABASE['Baader_Hyperion_21mm'])

    @classmethod
    def Baader_Hyperion_24mm(cls):
        return cls.from_database(cls._DATABASE['Baader_Hyperion_24mm'])

    @classmethod
    def Baader_Hyperion_36mm(cls):
        return cls.from_database(cls._DATABASE['Baader_Hyperion_36mm'])

    @classmethod
    def Baader_Morpheus_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_Morpheus_4_5mm'])

    @classmethod
    def Baader_Morpheus_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_Morpheus_6_5mm'])

    @classmethod
    def Baader_Morpheus_9mm(cls):
        return cls.from_database(cls._DATABASE['Baader_Morpheus_9mm'])

    @classmethod
    def Baader_Morpheus_12_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_Morpheus_12_5mm'])

    @classmethod
    def Baader_Morpheus_14mm(cls):
        return cls.from_database(cls._DATABASE['Baader_Morpheus_14mm'])

    @classmethod
    def Baader_Morpheus_17_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_Morpheus_17_5mm'])

    @classmethod
    def Baader_Classic_Ortho_6mm(cls):
        return cls.from_database(cls._DATABASE['Baader_Classic_Ortho_6mm'])

    @classmethod
    def Baader_Classic_Ortho_10mm(cls):
        return cls.from_database(cls._DATABASE['Baader_Classic_Ortho_10mm'])

    @classmethod
    def Baader_Classic_Ortho_18mm(cls):
        return cls.from_database(cls._DATABASE['Baader_Classic_Ortho_18mm'])

    @classmethod
    def Baader_Hyperion_Mark_IV_8_24mm_Zoom(cls):
        return cls.from_database(cls._DATABASE['Baader_Hyperion_Mark_IV_8_24mm_Zoom'])

    @classmethod
    def Baader_Classic_Ortho_3_5mm_v2(cls):
        return cls.from_database(cls._DATABASE['Baader_Classic_Ortho_3_5mm_v2'])

    @classmethod
    def Baader_Classic_Ortho_5mm_v2(cls):
        return cls.from_database(cls._DATABASE['Baader_Classic_Ortho_5mm_v2'])

    @classmethod
    def Baader_Classic_Ortho_7mm_v2(cls):
        return cls.from_database(cls._DATABASE['Baader_Classic_Ortho_7mm_v2'])

    @classmethod
    def Baader_Classic_Ortho_12_5mm_v2(cls):
        return cls.from_database(cls._DATABASE['Baader_Classic_Ortho_12_5mm_v2'])

    @classmethod
    def Baader_Classic_Ortho_18mm_v2(cls):
        return cls.from_database(cls._DATABASE['Baader_Classic_Ortho_18mm_v2'])

    @classmethod
    def Baader_Classic_Ortho_25mm_v2(cls):
        return cls.from_database(cls._DATABASE['Baader_Classic_Ortho_25mm_v2'])

    @classmethod
    def Baader_Genuine_Ortho_4mm(cls):
        return cls.from_database(cls._DATABASE['Baader_Genuine_Ortho_4mm'])

    @classmethod
    def Baader_Genuine_Ortho_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_Genuine_Ortho_5mm'])

    @classmethod
    def Baader_Genuine_Ortho_6mm(cls):
        return cls.from_database(cls._DATABASE['Baader_Genuine_Ortho_6mm'])

    @classmethod
    def Baader_Genuine_Ortho_7mm(cls):
        return cls.from_database(cls._DATABASE['Baader_Genuine_Ortho_7mm'])

    @classmethod
    def Baader_Genuine_Ortho_9mm(cls):
        return cls.from_database(cls._DATABASE['Baader_Genuine_Ortho_9mm'])

    @classmethod
    def Baader_Genuine_Ortho_10mm(cls):
        return cls.from_database(cls._DATABASE['Baader_Genuine_Ortho_10mm'])

    @classmethod
    def Baader_Genuine_Ortho_12_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_Genuine_Ortho_12_5mm'])

    @classmethod
    def Baader_Genuine_Ortho_18mm(cls):
        return cls.from_database(cls._DATABASE['Baader_Genuine_Ortho_18mm'])

    @classmethod
    def Baader_Genuine_Ortho_25mm(cls):
        return cls.from_database(cls._DATABASE['Baader_Genuine_Ortho_25mm'])

    @classmethod
    def Baader_Micro_Guide_Eyepiece_12_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_Micro_Guide_Eyepiece_12_5mm'])