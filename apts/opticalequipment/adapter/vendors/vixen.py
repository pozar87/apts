from ...abstract import IntermediateOpticalEquipment
from ....constants import OpticalType
from ..base import Adapter, Spacer

class VixenAdapter(Adapter):
    _DATABASE = {'Vixen_T_Ring_Canon_EOS': {'brand': 'Vixen', 'name': 'T-Ring Canon EOS', 'type': 'type_adapter', 'optical_length': 10.5, 'mass': 25, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_T_Ring_Nikon_F': {'brand': 'Vixen', 'name': 'T-Ring Nikon F', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 25, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_M42_M54_Adapter': {'brand': 'Vixen', 'name': 'M42→M54 Adapter', 'type': 'type_adapter', 'optical_length': 10, 'mass': 25, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_M48_M42_Adapter': {'brand': 'Vixen', 'name': 'M48→M42 Adapter', 'type': 'type_adapter', 'optical_length': 5, 'mass': 20, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_60mm_2_Adapter': {'brand': 'Vixen', 'name': '60mm→2" Adapter', 'type': 'type_adapter', 'optical_length': 0, 'mass': 40, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_M42_Spacer_5mm': {'brand': 'Vixen', 'name': 'M42 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 8, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M42_Spacer_10mm': {'brand': 'Vixen', 'name': 'M42 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 12, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M42_Spacer_15mm': {'brand': 'Vixen', 'name': 'M42 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M42_Spacer_20mm': {'brand': 'Vixen', 'name': 'M42 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 20, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M48_Spacer_5mm': {'brand': 'Vixen', 'name': 'M48 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 10, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M48_Spacer_10mm': {'brand': 'Vixen', 'name': 'M48 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 14, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M48_Spacer_15mm': {'brand': 'Vixen', 'name': 'M48 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M48_Spacer_20mm': {'brand': 'Vixen', 'name': 'M48 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 22, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M42_M48_Adapter': {'brand': 'Vixen', 'name': 'M42→M48 Adapter', 'type': 'type_adapter', 'optical_length': 5, 'mass': 20, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_M54_M68_Adapter': {'brand': 'Vixen', 'name': 'M54→M68 Adapter', 'type': 'type_adapter', 'optical_length': 8, 'mass': 30, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_EOS_M42_T_Ring': {'brand': 'Vixen', 'name': 'EOS→M42 T-Ring', 'type': 'type_adapter', 'optical_length': 10.5, 'mass': 28, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_Nikon_F_M42_T_Ring': {'brand': 'Vixen', 'name': 'Nikon F→M42 T-Ring', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 28, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_Sony_E_M42_Adapter': {'brand': 'Vixen', 'name': 'Sony E→M42 Adapter', 'type': 'type_adapter', 'optical_length': 7, 'mass': 22, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_Canon_RF_M42_Adapter': {'brand': 'Vixen', 'name': 'Canon RF→M42 Adapter', 'type': 'type_adapter', 'optical_length': 5, 'mass': 22, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_2_M42_Adapter': {'brand': 'Vixen', 'name': '2"→M42 Adapter', 'type': 'type_adapter', 'optical_length': 0, 'mass': 14, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_2_1_25_Adapter': {'brand': 'Vixen', 'name': '2"→1.25" Adapter', 'type': 'type_adapter', 'optical_length': 0, 'mass': 14, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_M42_Spacer_2_5mm': {'brand': 'Vixen', 'name': 'M42 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M42_Spacer_3_5mm': {'brand': 'Vixen', 'name': 'M42 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M42_Spacer_4_5mm': {'brand': 'Vixen', 'name': 'M42 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 7, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M42_Spacer_5_5mm': {'brand': 'Vixen', 'name': 'M42 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 8, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M42_Spacer_6_5mm': {'brand': 'Vixen', 'name': 'M42 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 9, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M42_Spacer_7_5mm': {'brand': 'Vixen', 'name': 'M42 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 10, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M42_Spacer_8_5mm': {'brand': 'Vixen', 'name': 'M42 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 10, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M42_Spacer_9_5mm': {'brand': 'Vixen', 'name': 'M42 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 11, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M42_Spacer_11mm': {'brand': 'Vixen', 'name': 'M42 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 12, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M42_Spacer_12mm': {'brand': 'Vixen', 'name': 'M42 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 13, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M42_Spacer_13mm': {'brand': 'Vixen', 'name': 'M42 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 14, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M42_Spacer_14mm': {'brand': 'Vixen', 'name': 'M42 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 15, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M42_Spacer_16mm': {'brand': 'Vixen', 'name': 'M42 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M42_Spacer_17mm': {'brand': 'Vixen', 'name': 'M42 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 17, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M42_Spacer_18mm': {'brand': 'Vixen', 'name': 'M42 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 18, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M42_Spacer_22mm': {'brand': 'Vixen', 'name': 'M42 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 21, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M42_Spacer_25mm': {'brand': 'Vixen', 'name': 'M42 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 24, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M48_Spacer_2_5mm': {'brand': 'Vixen', 'name': 'M48 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M48_Spacer_3_5mm': {'brand': 'Vixen', 'name': 'M48 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M48_Spacer_4_5mm': {'brand': 'Vixen', 'name': 'M48 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 9, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M48_Spacer_5_5mm': {'brand': 'Vixen', 'name': 'M48 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 10, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M48_Spacer_6_5mm': {'brand': 'Vixen', 'name': 'M48 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 11, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M48_Spacer_7_5mm': {'brand': 'Vixen', 'name': 'M48 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 12, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M48_Spacer_8_5mm': {'brand': 'Vixen', 'name': 'M48 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 12, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M48_Spacer_9_5mm': {'brand': 'Vixen', 'name': 'M48 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 13, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M48_Spacer_11mm': {'brand': 'Vixen', 'name': 'M48 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 14, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M48_Spacer_12mm': {'brand': 'Vixen', 'name': 'M48 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 15, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M48_Spacer_13mm': {'brand': 'Vixen', 'name': 'M48 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 16, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M48_Spacer_14mm': {'brand': 'Vixen', 'name': 'M48 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 17, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M48_Spacer_16mm': {'brand': 'Vixen', 'name': 'M48 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M48_Spacer_17mm': {'brand': 'Vixen', 'name': 'M48 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 19, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M48_Spacer_18mm': {'brand': 'Vixen', 'name': 'M48 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 20, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M48_Spacer_22mm': {'brand': 'Vixen', 'name': 'M48 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 23, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M48_Spacer_25mm': {'brand': 'Vixen', 'name': 'M48 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 26, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Vixen_M42_Extension_Tube_3mm': {'brand': 'Vixen', 'name': 'M42 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 13, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_M42_Extension_Tube_6mm': {'brand': 'Vixen', 'name': 'M42 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 14, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_M42_Extension_Tube_9mm': {'brand': 'Vixen', 'name': 'M42 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 15, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_M42_Extension_Tube_11mm': {'brand': 'Vixen', 'name': 'M42 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_M42_Extension_Tube_13mm': {'brand': 'Vixen', 'name': 'M42 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_M42_Extension_Tube_16mm': {'brand': 'Vixen', 'name': 'M42 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 17, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_M42_Extension_Tube_22mm': {'brand': 'Vixen', 'name': 'M42 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 19, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_M42_Extension_Tube_28mm': {'brand': 'Vixen', 'name': 'M42 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 21, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_M42_Extension_Tube_35mm': {'brand': 'Vixen', 'name': 'M42 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 23, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_M42_Extension_Tube_45mm': {'brand': 'Vixen', 'name': 'M42 Extension Tube 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 26, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_M48_Extension_Tube_3mm': {'brand': 'Vixen', 'name': 'M48 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 17, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_M48_Extension_Tube_6mm': {'brand': 'Vixen', 'name': 'M48 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_M48_Extension_Tube_9mm': {'brand': 'Vixen', 'name': 'M48 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 19, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_M48_Extension_Tube_11mm': {'brand': 'Vixen', 'name': 'M48 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 20, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_M48_Extension_Tube_13mm': {'brand': 'Vixen', 'name': 'M48 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 20, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_M48_Extension_Tube_16mm': {'brand': 'Vixen', 'name': 'M48 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 21, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_M48_Extension_Tube_22mm': {'brand': 'Vixen', 'name': 'M48 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 23, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_M48_Extension_Tube_28mm': {'brand': 'Vixen', 'name': 'M48 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 25, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_M48_Extension_Tube_35mm': {'brand': 'Vixen', 'name': 'M48 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 27, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_M48_Extension_Tube_45mm': {'brand': 'Vixen', 'name': 'M48 Extension Tube 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 30, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_M54_Extension_Tube_3mm': {'brand': 'Vixen', 'name': 'M54 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 21, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_M54_Extension_Tube_6mm': {'brand': 'Vixen', 'name': 'M54 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 22, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_M54_Extension_Tube_9mm': {'brand': 'Vixen', 'name': 'M54 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 23, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_M54_Extension_Tube_11mm': {'brand': 'Vixen', 'name': 'M54 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 24, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_M54_Extension_Tube_13mm': {'brand': 'Vixen', 'name': 'M54 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 24, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_M54_Extension_Tube_16mm': {'brand': 'Vixen', 'name': 'M54 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 25, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_M54_Extension_Tube_22mm': {'brand': 'Vixen', 'name': 'M54 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 27, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_M54_Extension_Tube_28mm': {'brand': 'Vixen', 'name': 'M54 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 29, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_M54_Extension_Tube_35mm': {'brand': 'Vixen', 'name': 'M54 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 31, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vixen_M54_Extension_Tube_45mm': {'brand': 'Vixen', 'name': 'M54 Extension Tube 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 34, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Vixen_T_Ring_Canon_EOS(cls):
        return cls.from_database(cls._DATABASE['Vixen_T_Ring_Canon_EOS'])

    @classmethod
    def Vixen_T_Ring_Nikon_F(cls):
        return cls.from_database(cls._DATABASE['Vixen_T_Ring_Nikon_F'])

    @classmethod
    def Vixen_M42_M54_Adapter(cls):
        return cls.from_database(cls._DATABASE['Vixen_M42_M54_Adapter'])

    @classmethod
    def Vixen_M48_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['Vixen_M48_M42_Adapter'])

    @classmethod
    def Vixen_60mm_2_Adapter(cls):
        return cls.from_database(cls._DATABASE['Vixen_60mm_2_Adapter'])

    @classmethod
    def Vixen_M42_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M42_Spacer_5mm'])

    @classmethod
    def Vixen_M42_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M42_Spacer_10mm'])

    @classmethod
    def Vixen_M42_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M42_Spacer_15mm'])

    @classmethod
    def Vixen_M42_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M42_Spacer_20mm'])

    @classmethod
    def Vixen_M48_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M48_Spacer_5mm'])

    @classmethod
    def Vixen_M48_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M48_Spacer_10mm'])

    @classmethod
    def Vixen_M48_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M48_Spacer_15mm'])

    @classmethod
    def Vixen_M48_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M48_Spacer_20mm'])

    @classmethod
    def Vixen_M42_M48_Adapter(cls):
        return cls.from_database(cls._DATABASE['Vixen_M42_M48_Adapter'])

    @classmethod
    def Vixen_M54_M68_Adapter(cls):
        return cls.from_database(cls._DATABASE['Vixen_M54_M68_Adapter'])

    @classmethod
    def Vixen_EOS_M42_T_Ring(cls):
        return cls.from_database(cls._DATABASE['Vixen_EOS_M42_T_Ring'])

    @classmethod
    def Vixen_Nikon_F_M42_T_Ring(cls):
        return cls.from_database(cls._DATABASE['Vixen_Nikon_F_M42_T_Ring'])

    @classmethod
    def Vixen_Sony_E_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['Vixen_Sony_E_M42_Adapter'])

    @classmethod
    def Vixen_Canon_RF_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['Vixen_Canon_RF_M42_Adapter'])

    @classmethod
    def Vixen_2_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['Vixen_2_M42_Adapter'])

    @classmethod
    def Vixen_2_1_25_Adapter(cls):
        return cls.from_database(cls._DATABASE['Vixen_2_1_25_Adapter'])

    @classmethod
    def Vixen_M42_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M42_Spacer_2_5mm'])

    @classmethod
    def Vixen_M42_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M42_Spacer_3_5mm'])

    @classmethod
    def Vixen_M42_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M42_Spacer_4_5mm'])

    @classmethod
    def Vixen_M42_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M42_Spacer_5_5mm'])

    @classmethod
    def Vixen_M42_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M42_Spacer_6_5mm'])

    @classmethod
    def Vixen_M42_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M42_Spacer_7_5mm'])

    @classmethod
    def Vixen_M42_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M42_Spacer_8_5mm'])

    @classmethod
    def Vixen_M42_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M42_Spacer_9_5mm'])

    @classmethod
    def Vixen_M42_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M42_Spacer_11mm'])

    @classmethod
    def Vixen_M42_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M42_Spacer_12mm'])

    @classmethod
    def Vixen_M42_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M42_Spacer_13mm'])

    @classmethod
    def Vixen_M42_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M42_Spacer_14mm'])

    @classmethod
    def Vixen_M42_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M42_Spacer_16mm'])

    @classmethod
    def Vixen_M42_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M42_Spacer_17mm'])

    @classmethod
    def Vixen_M42_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M42_Spacer_18mm'])

    @classmethod
    def Vixen_M42_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M42_Spacer_22mm'])

    @classmethod
    def Vixen_M42_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M42_Spacer_25mm'])

    @classmethod
    def Vixen_M48_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M48_Spacer_2_5mm'])

    @classmethod
    def Vixen_M48_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M48_Spacer_3_5mm'])

    @classmethod
    def Vixen_M48_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M48_Spacer_4_5mm'])

    @classmethod
    def Vixen_M48_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M48_Spacer_5_5mm'])

    @classmethod
    def Vixen_M48_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M48_Spacer_6_5mm'])

    @classmethod
    def Vixen_M48_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M48_Spacer_7_5mm'])

    @classmethod
    def Vixen_M48_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M48_Spacer_8_5mm'])

    @classmethod
    def Vixen_M48_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M48_Spacer_9_5mm'])

    @classmethod
    def Vixen_M48_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M48_Spacer_11mm'])

    @classmethod
    def Vixen_M48_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M48_Spacer_12mm'])

    @classmethod
    def Vixen_M48_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M48_Spacer_13mm'])

    @classmethod
    def Vixen_M48_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M48_Spacer_14mm'])

    @classmethod
    def Vixen_M48_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M48_Spacer_16mm'])

    @classmethod
    def Vixen_M48_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M48_Spacer_17mm'])

    @classmethod
    def Vixen_M48_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M48_Spacer_18mm'])

    @classmethod
    def Vixen_M48_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M48_Spacer_22mm'])

    @classmethod
    def Vixen_M48_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M48_Spacer_25mm'])

    @classmethod
    def Vixen_M42_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M42_Extension_Tube_3mm'])

    @classmethod
    def Vixen_M42_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M42_Extension_Tube_6mm'])

    @classmethod
    def Vixen_M42_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M42_Extension_Tube_9mm'])

    @classmethod
    def Vixen_M42_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M42_Extension_Tube_11mm'])

    @classmethod
    def Vixen_M42_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M42_Extension_Tube_13mm'])

    @classmethod
    def Vixen_M42_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M42_Extension_Tube_16mm'])

    @classmethod
    def Vixen_M42_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M42_Extension_Tube_22mm'])

    @classmethod
    def Vixen_M42_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M42_Extension_Tube_28mm'])

    @classmethod
    def Vixen_M42_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M42_Extension_Tube_35mm'])

    @classmethod
    def Vixen_M42_Extension_Tube_45mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M42_Extension_Tube_45mm'])

    @classmethod
    def Vixen_M48_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M48_Extension_Tube_3mm'])

    @classmethod
    def Vixen_M48_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M48_Extension_Tube_6mm'])

    @classmethod
    def Vixen_M48_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M48_Extension_Tube_9mm'])

    @classmethod
    def Vixen_M48_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M48_Extension_Tube_11mm'])

    @classmethod
    def Vixen_M48_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M48_Extension_Tube_13mm'])

    @classmethod
    def Vixen_M48_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M48_Extension_Tube_16mm'])

    @classmethod
    def Vixen_M48_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M48_Extension_Tube_22mm'])

    @classmethod
    def Vixen_M48_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M48_Extension_Tube_28mm'])

    @classmethod
    def Vixen_M48_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M48_Extension_Tube_35mm'])

    @classmethod
    def Vixen_M48_Extension_Tube_45mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M48_Extension_Tube_45mm'])

    @classmethod
    def Vixen_M54_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M54_Extension_Tube_3mm'])

    @classmethod
    def Vixen_M54_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M54_Extension_Tube_6mm'])

    @classmethod
    def Vixen_M54_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M54_Extension_Tube_9mm'])

    @classmethod
    def Vixen_M54_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M54_Extension_Tube_11mm'])

    @classmethod
    def Vixen_M54_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M54_Extension_Tube_13mm'])

    @classmethod
    def Vixen_M54_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M54_Extension_Tube_16mm'])

    @classmethod
    def Vixen_M54_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M54_Extension_Tube_22mm'])

    @classmethod
    def Vixen_M54_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M54_Extension_Tube_28mm'])

    @classmethod
    def Vixen_M54_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M54_Extension_Tube_35mm'])

    @classmethod
    def Vixen_M54_Extension_Tube_45mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M54_Extension_Tube_45mm'])

class VixenSpacer(Spacer):
    _DATABASE = {'Vixen_M42_Spacer_1mm': {'brand': 'Vixen', 'name': 'M42 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Vixen_M42_Spacer_2mm': {'brand': 'Vixen', 'name': 'M42 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Vixen_M48_Spacer_1mm': {'brand': 'Vixen', 'name': 'M48 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Vixen_M48_Spacer_2mm': {'brand': 'Vixen', 'name': 'M48 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Vixen_M42_Spacer_0_5mm': {'brand': 'Vixen', 'name': 'M42 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Vixen_M42_Spacer_0_7mm': {'brand': 'Vixen', 'name': 'M42 Spacer 0.7mm', 'type': 'type_spacer', 'optical_length': 0.7, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Vixen_M42_Spacer_1_5mm': {'brand': 'Vixen', 'name': 'M42 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Vixen_M48_Spacer_0_5mm': {'brand': 'Vixen', 'name': 'M48 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Vixen_M48_Spacer_0_7mm': {'brand': 'Vixen', 'name': 'M48 Spacer 0.7mm', 'type': 'type_spacer', 'optical_length': 0.7, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Vixen_M48_Spacer_1_5mm': {'brand': 'Vixen', 'name': 'M48 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}}

    @classmethod
    def Vixen_M42_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M42_Spacer_1mm'])

    @classmethod
    def Vixen_M42_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M42_Spacer_2mm'])

    @classmethod
    def Vixen_M48_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M48_Spacer_1mm'])

    @classmethod
    def Vixen_M48_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M48_Spacer_2mm'])

    @classmethod
    def Vixen_M42_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M42_Spacer_0_5mm'])

    @classmethod
    def Vixen_M42_Spacer_0_7mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M42_Spacer_0_7mm'])

    @classmethod
    def Vixen_M42_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M42_Spacer_1_5mm'])

    @classmethod
    def Vixen_M48_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M48_Spacer_0_5mm'])

    @classmethod
    def Vixen_M48_Spacer_0_7mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M48_Spacer_0_7mm'])

    @classmethod
    def Vixen_M48_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Vixen_M48_Spacer_1_5mm'])