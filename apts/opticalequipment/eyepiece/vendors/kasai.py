from ...abstract import OutputOpticalEqipment
from ....constants import GraphConstants, OpticalType
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ..base import Eyepiece

class KasaiEyepiece(Eyepiece):
    _DATABASE = {'Kasai_Wide_View_5mm_84': {'brand': 'Kasai', 'name': 'Wide View 5mm 84°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 180, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Kasai_Wide_View_7_5mm_84': {'brand': 'Kasai', 'name': 'Wide View 7.5mm 84°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 190, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Kasai_Wide_View_10mm_84': {'brand': 'Kasai', 'name': 'Wide View 10mm 84°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 200, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Kasai_Wide_View_14mm_84': {'brand': 'Kasai', 'name': 'Wide View 14mm 84°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 220, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Kasai_Wide_View_20mm_84': {'brand': 'Kasai', 'name': 'Wide View 20mm 84°', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 250, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Kasai_HD_Ortho_4mm': {'brand': 'Kasai', 'name': 'HD Ortho 4mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 160, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Kasai_HD_Ortho_5mm': {'brand': 'Kasai', 'name': 'HD Ortho 5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 168, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Kasai_HD_Ortho_6mm': {'brand': 'Kasai', 'name': 'HD Ortho 6mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 175, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Kasai_HD_Ortho_8mm': {'brand': 'Kasai', 'name': 'HD Ortho 8mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 190, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Kasai_HD_Ortho_10mm': {'brand': 'Kasai', 'name': 'HD Ortho 10mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 200, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Kasai_HD_Ortho_12_5mm': {'brand': 'Kasai', 'name': 'HD Ortho 12.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 215, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Kasai_HD_Ortho_18mm': {'brand': 'Kasai', 'name': 'HD Ortho 18mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 250, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Kasai_HD_Ortho_25mm': {'brand': 'Kasai', 'name': 'HD Ortho 25mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 300, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Kasai_Wide_View_5mm_84(cls):
        return cls.from_database(cls._DATABASE['Kasai_Wide_View_5mm_84'])

    @classmethod
    def Kasai_Wide_View_7_5mm_84(cls):
        return cls.from_database(cls._DATABASE['Kasai_Wide_View_7_5mm_84'])

    @classmethod
    def Kasai_Wide_View_10mm_84(cls):
        return cls.from_database(cls._DATABASE['Kasai_Wide_View_10mm_84'])

    @classmethod
    def Kasai_Wide_View_14mm_84(cls):
        return cls.from_database(cls._DATABASE['Kasai_Wide_View_14mm_84'])

    @classmethod
    def Kasai_Wide_View_20mm_84(cls):
        return cls.from_database(cls._DATABASE['Kasai_Wide_View_20mm_84'])

    @classmethod
    def Kasai_HD_Ortho_4mm(cls):
        return cls.from_database(cls._DATABASE['Kasai_HD_Ortho_4mm'])

    @classmethod
    def Kasai_HD_Ortho_5mm(cls):
        return cls.from_database(cls._DATABASE['Kasai_HD_Ortho_5mm'])

    @classmethod
    def Kasai_HD_Ortho_6mm(cls):
        return cls.from_database(cls._DATABASE['Kasai_HD_Ortho_6mm'])

    @classmethod
    def Kasai_HD_Ortho_8mm(cls):
        return cls.from_database(cls._DATABASE['Kasai_HD_Ortho_8mm'])

    @classmethod
    def Kasai_HD_Ortho_10mm(cls):
        return cls.from_database(cls._DATABASE['Kasai_HD_Ortho_10mm'])

    @classmethod
    def Kasai_HD_Ortho_12_5mm(cls):
        return cls.from_database(cls._DATABASE['Kasai_HD_Ortho_12_5mm'])

    @classmethod
    def Kasai_HD_Ortho_18mm(cls):
        return cls.from_database(cls._DATABASE['Kasai_HD_Ortho_18mm'])

    @classmethod
    def Kasai_HD_Ortho_25mm(cls):
        return cls.from_database(cls._DATABASE['Kasai_HD_Ortho_25mm'])