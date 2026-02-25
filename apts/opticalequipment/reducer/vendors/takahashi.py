from ...abstract import IntermediateOpticalEquipment
from ....constants import OpticalType
from ....units import get_unit_registry
from ....utils import Gender
from ..base import Reducer, Flattener, Corrector

class TakahashiReducer(Reducer):
    _DATABASE = {'Takahashi_QE_0_73x_Reducer_FSQ': {'brand': 'Takahashi', 'name': 'QE 0.73x Reducer (FSQ)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 350, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Takahashi_645_Reducer_0_72x_FSQ': {'brand': 'Takahashi', 'name': '645 Reducer 0.72x (FSQ)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 500, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Takahashi_TOA_35_Reducer_0_7x': {'brand': 'Takahashi', 'name': 'TOA-35 Reducer 0.7x', 'type': 'type_reducer', 'optical_length': 0, 'mass': 400, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Takahashi_FC_35_Reducer_0_66x': {'brand': 'Takahashi', 'name': 'FC-35 Reducer 0.66x', 'type': 'type_reducer', 'optical_length': 0, 'mass': 250, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Takahashi_Multi_Reducer_0_85x_S_FS_60': {'brand': 'Takahashi', 'name': 'Multi Reducer 0.85x-S (FS-60)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Takahashi_Multi_Reducer_0_85x_M_FCT_65': {'brand': 'Takahashi', 'name': 'Multi Reducer 0.85x-M (FCT-65)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Takahashi_Multi_Reducer_0_85x_L_FC_76': {'brand': 'Takahashi', 'name': 'Multi Reducer 0.85x-L (FC-76)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Takahashi_76D_Reducer_FC_76_FC_100': {'brand': 'Takahashi', 'name': '76D Reducer (FC-76/FC-100)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 190, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Takahashi_Focal_Reducer_C_0_72x_FS_60': {'brand': 'Takahashi', 'name': 'Focal Reducer-C 0.72x (FS-60)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 180, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Takahashi_Flattener_Reducer_SKY_90': {'brand': 'Takahashi', 'name': 'Flattener-Reducer (SKY-90)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Takahashi_Reducer_Corrector_0_8x_Mewlon': {'brand': 'Takahashi', 'name': 'Reducer-Corrector 0.8x (Mewlon)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 350, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Takahashi_Reducer_CR_0_73x_CCA_Mewlon_CRS': {'brand': 'Takahashi', 'name': 'Reducer-CR 0.73x (CCA/Mewlon CRS)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 500, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Takahashi_F3_Reducer_0_6x_FSQ_106ED': {'brand': 'Takahashi', 'name': 'F3 Reducer 0.6x (FSQ-106ED)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 600, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Takahashi_645_Reducer_CA_0_72x_CCA_250': {'brand': 'Takahashi', 'name': '645 Reducer-CA 0.72x (CCA-250)', 'type': 'type_reducer', 'optical_length': 0, 'mass': 700, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Takahashi_QE_0_73x_Reducer_FSQ(cls):
        return cls.from_database(cls._DATABASE['Takahashi_QE_0_73x_Reducer_FSQ'])

    @classmethod
    def Takahashi_645_Reducer_0_72x_FSQ(cls):
        return cls.from_database(cls._DATABASE['Takahashi_645_Reducer_0_72x_FSQ'])

    @classmethod
    def Takahashi_TOA_35_Reducer_0_7x(cls):
        return cls.from_database(cls._DATABASE['Takahashi_TOA_35_Reducer_0_7x'])

    @classmethod
    def Takahashi_FC_35_Reducer_0_66x(cls):
        return cls.from_database(cls._DATABASE['Takahashi_FC_35_Reducer_0_66x'])

    @classmethod
    def Takahashi_Multi_Reducer_0_85x_S_FS_60(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Multi_Reducer_0_85x_S_FS_60'])

    @classmethod
    def Takahashi_Multi_Reducer_0_85x_M_FCT_65(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Multi_Reducer_0_85x_M_FCT_65'])

    @classmethod
    def Takahashi_Multi_Reducer_0_85x_L_FC_76(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Multi_Reducer_0_85x_L_FC_76'])

    @classmethod
    def Takahashi_76D_Reducer_FC_76_FC_100(cls):
        return cls.from_database(cls._DATABASE['Takahashi_76D_Reducer_FC_76_FC_100'])

    @classmethod
    def Takahashi_Focal_Reducer_C_0_72x_FS_60(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Focal_Reducer_C_0_72x_FS_60'])

    @classmethod
    def Takahashi_Flattener_Reducer_SKY_90(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Flattener_Reducer_SKY_90'])

    @classmethod
    def Takahashi_Reducer_Corrector_0_8x_Mewlon(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Reducer_Corrector_0_8x_Mewlon'])

    @classmethod
    def Takahashi_Reducer_CR_0_73x_CCA_Mewlon_CRS(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Reducer_CR_0_73x_CCA_Mewlon_CRS'])

    @classmethod
    def Takahashi_F3_Reducer_0_6x_FSQ_106ED(cls):
        return cls.from_database(cls._DATABASE['Takahashi_F3_Reducer_0_6x_FSQ_106ED'])

    @classmethod
    def Takahashi_645_Reducer_CA_0_72x_CCA_250(cls):
        return cls.from_database(cls._DATABASE['Takahashi_645_Reducer_CA_0_72x_CCA_250'])

class TakahashiFlattener(Flattener):
    _DATABASE = {'Takahashi_Flattener_1_01x_FSQ': {'brand': 'Takahashi', 'name': 'Flattener 1.01x (FSQ)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 300, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Takahashi_TOA_35FL_Flattener': {'brand': 'Takahashi', 'name': 'TOA-35FL Flattener', 'type': 'type_flattener', 'optical_length': 0, 'mass': 350, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Takahashi_FC_Flattener': {'brand': 'Takahashi', 'name': 'FC Flattener', 'type': 'type_flattener', 'optical_length': 0, 'mass': 200, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Takahashi_Multi_Flattener_1_04x_FC_FS': {'brand': 'Takahashi', 'name': 'Multi Flattener 1.04x (FC/FS)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 110, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Takahashi_Flattener_0_93x_FOA_60': {'brand': 'Takahashi', 'name': 'Flattener 0.93x (FOA-60)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Takahashi_TOA_645_FL_Flattener_TOA_130': {'brand': 'Takahashi', 'name': 'TOA-645 FL Flattener (TOA-130)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 400, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}, 'Takahashi_TOA_645_FL_Flattener_TOA_150': {'brand': 'Takahashi', 'name': 'TOA-645 FL Flattener (TOA-150)', 'type': 'type_flattener', 'optical_length': 0, 'mass': 500, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Takahashi_Flattener_1_01x_FSQ(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Flattener_1_01x_FSQ'])

    @classmethod
    def Takahashi_TOA_35FL_Flattener(cls):
        return cls.from_database(cls._DATABASE['Takahashi_TOA_35FL_Flattener'])

    @classmethod
    def Takahashi_FC_Flattener(cls):
        return cls.from_database(cls._DATABASE['Takahashi_FC_Flattener'])

    @classmethod
    def Takahashi_Multi_Flattener_1_04x_FC_FS(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Multi_Flattener_1_04x_FC_FS'])

    @classmethod
    def Takahashi_Flattener_0_93x_FOA_60(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Flattener_0_93x_FOA_60'])

    @classmethod
    def Takahashi_TOA_645_FL_Flattener_TOA_130(cls):
        return cls.from_database(cls._DATABASE['Takahashi_TOA_645_FL_Flattener_TOA_130'])

    @classmethod
    def Takahashi_TOA_645_FL_Flattener_TOA_150(cls):
        return cls.from_database(cls._DATABASE['Takahashi_TOA_645_FL_Flattener_TOA_150'])

class TakahashiCorrector(Corrector):
    _DATABASE = {'Takahashi_Epsilon_Corrector': {'brand': 'Takahashi', 'name': 'Epsilon Corrector', 'type': 'type_corrector', 'optical_length': 0, 'mass': 300, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': 'start'}}

    @classmethod
    def Takahashi_Epsilon_Corrector(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Epsilon_Corrector'])