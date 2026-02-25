from ...abstract import IntermediateOpticalEquipment
from ....constants import OpticalType
from ....units import get_unit_registry
from ....utils import Gender
from ..base import Reducer, Flattener, Corrector

class StarizonaReducer(Reducer):
    _DATABASE = {'Starizona_SCT_Corrector_IV_0_63x': {'brand': 'Starizona', 'name': 'SCT Corrector IV (0.63x)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 300, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Starizona_HyperStar_C8_0_2x': {'brand': 'Starizona', 'name': 'HyperStar C8 (0.2x)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 400, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''}, 'Starizona_HyperStar_C11_0_2x': {'brand': 'Starizona', 'name': 'HyperStar C11 (0.2x)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''}, 'Starizona_HyperStar_C14_0_2x': {'brand': 'Starizona', 'name': 'HyperStar C14 (0.2x)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 600, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''}, 'Starizona_Night_Owl_0_4x': {'brand': 'Starizona', 'name': 'Night Owl 0.4x', 'type': 'type_reducer', 'optical_length': 0, 'mass': 600, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Starizona_Apex_ED_0_65x_M42': {'brand': 'Starizona', 'name': 'Apex ED 0.65x (M42)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Starizona_SCT_Corrector_IV_0_63x(cls):
        return cls.from_database(cls._DATABASE['Starizona_SCT_Corrector_IV_0_63x'])

    @classmethod
    def Starizona_HyperStar_C8_0_2x(cls):
        return cls.from_database(cls._DATABASE['Starizona_HyperStar_C8_0_2x'])

    @classmethod
    def Starizona_HyperStar_C11_0_2x(cls):
        return cls.from_database(cls._DATABASE['Starizona_HyperStar_C11_0_2x'])

    @classmethod
    def Starizona_HyperStar_C14_0_2x(cls):
        return cls.from_database(cls._DATABASE['Starizona_HyperStar_C14_0_2x'])

    @classmethod
    def Starizona_Night_Owl_0_4x(cls):
        return cls.from_database(cls._DATABASE['Starizona_Night_Owl_0_4x'])

    @classmethod
    def Starizona_Apex_ED_0_65x_M42(cls):
        return cls.from_database(cls._DATABASE['Starizona_Apex_ED_0_65x_M42'])