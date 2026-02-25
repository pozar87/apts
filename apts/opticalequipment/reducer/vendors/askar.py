from ...abstract import IntermediateOpticalEquipment
from ....constants import OpticalType
from ....units import get_unit_registry
from ....utils import Gender
from ..base import Reducer, Flattener, Corrector

class AskarReducer(Reducer):
    _DATABASE = {'Askar_0_7x_Reducer_FRA_series': {'brand': 'Askar', 'name': '0.7x Reducer (FRA series)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Askar_103APO_Reducer_0_6x': {'brand': 'Askar', 'name': '103APO Reducer 0.6x', 'type': 'type_reducer', 'optical_length': 0, 'mass': 300, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Askar_151PHQ_Reducer_0_7x': {'brand': 'Askar', 'name': '151PHQ Reducer 0.7x', 'type': 'type_reducer', 'optical_length': 0, 'mass': 350, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Askar_0_76x_Reducer_PHQ': {'brand': 'Askar', 'name': '0.76x Reducer (PHQ)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 280, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Askar_0_7x_Reducer_65PHQ': {'brand': 'Askar', 'name': '0.7x Reducer (65PHQ)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Askar_0_76x_Reducer_80PHQ': {'brand': 'Askar', 'name': '0.76x Reducer (80PHQ)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Askar_0_7x_Reducer_107PHQ': {'brand': 'Askar', 'name': '0.7x Reducer (107PHQ)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 300, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Askar_0_6x_Reducer_FRA400': {'brand': 'Askar', 'name': '0.6x Reducer (FRA400)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 220, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Askar_0_7x_Reducer_FRA_series(cls):
        return cls.from_database(cls._DATABASE['Askar_0_7x_Reducer_FRA_series'])

    @classmethod
    def Askar_103APO_Reducer_0_6x(cls):
        return cls.from_database(cls._DATABASE['Askar_103APO_Reducer_0_6x'])

    @classmethod
    def Askar_151PHQ_Reducer_0_7x(cls):
        return cls.from_database(cls._DATABASE['Askar_151PHQ_Reducer_0_7x'])

    @classmethod
    def Askar_0_76x_Reducer_PHQ(cls):
        return cls.from_database(cls._DATABASE['Askar_0_76x_Reducer_PHQ'])

    @classmethod
    def Askar_0_7x_Reducer_65PHQ(cls):
        return cls.from_database(cls._DATABASE['Askar_0_7x_Reducer_65PHQ'])

    @classmethod
    def Askar_0_76x_Reducer_80PHQ(cls):
        return cls.from_database(cls._DATABASE['Askar_0_76x_Reducer_80PHQ'])

    @classmethod
    def Askar_0_7x_Reducer_107PHQ(cls):
        return cls.from_database(cls._DATABASE['Askar_0_7x_Reducer_107PHQ'])

    @classmethod
    def Askar_0_6x_Reducer_FRA400(cls):
        return cls.from_database(cls._DATABASE['Askar_0_6x_Reducer_FRA400'])

class AskarFlattener(Flattener):
    _DATABASE = {'Askar_Full_frame_Flattener': {'brand': 'Askar', 'name': 'Full-frame Flattener', 'type': 'type_flattener', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Askar_2_Flattener_M48': {'brand': 'Askar', 'name': '2" Flattener (M48)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 230, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Askar_Full_frame_Flattener(cls):
        return cls.from_database(cls._DATABASE['Askar_Full_frame_Flattener'])

    @classmethod
    def Askar_2_Flattener_M48(cls):
        return cls.from_database(cls._DATABASE['Askar_2_Flattener_M48'])

class AskarCorrector(Corrector):
    _DATABASE = {'Askar_Color_Magic_Corrector': {'brand': 'Askar', 'name': 'Color-Magic Corrector', 'type': 'type_corrector', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Askar_Color_Magic_Corrector(cls):
        return cls.from_database(cls._DATABASE['Askar_Color_Magic_Corrector'])