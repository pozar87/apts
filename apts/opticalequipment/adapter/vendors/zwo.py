from ...abstract import IntermediateOpticalEquipment
from ....constants import OpticalType
from ..base import Adapter, Spacer

class ZwoAdapter(Adapter):
    _DATABASE = {'ZWO_M42_M48_Adapter_5mm': {'brand': 'ZWO', 'name': 'M42→M48 Adapter (5mm)', 'type': 'type_adapter', 'optical_length': 5, 'mass': 25, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_M42_M54_Adapter_11mm': {'brand': 'ZWO', 'name': 'M42→M54 Adapter (11mm)', 'type': 'type_adapter', 'optical_length': 11, 'mass': 30, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_M48_M54_Adapter': {'brand': 'ZWO', 'name': 'M48→M54 Adapter', 'type': 'type_adapter', 'optical_length': 7, 'mass': 30, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_EOS_M42_T_Adapter_11mm': {'brand': 'ZWO', 'name': 'EOS→M42 T-Adapter (11mm)', 'type': 'type_adapter', 'optical_length': 11, 'mass': 35, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_EOS_M48_Adapter_8_5mm': {'brand': 'ZWO', 'name': 'EOS→M48 Adapter (8.5mm)', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 35, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_Nikon_M42_Adapter': {'brand': 'ZWO', 'name': 'Nikon→M42 Adapter', 'type': 'type_adapter', 'optical_length': 8, 'mass': 30, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_M42_M48_Adapter_short_1mm': {'brand': 'ZWO', 'name': 'M42→M48 Adapter (short, 1mm)', 'type': 'type_adapter', 'optical_length': 1, 'mass': 15, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_M48_M42_Adapter_short': {'brand': 'ZWO', 'name': 'M48→M42 Adapter (short)', 'type': 'type_adapter', 'optical_length': 1, 'mass': 15, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_1_25_M42_Adapter': {'brand': 'ZWO', 'name': '1.25"→M42 Adapter', 'type': 'type_adapter', 'optical_length': 0, 'mass': 10, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_2_M48_Adapter': {'brand': 'ZWO', 'name': '2"→M48 Adapter', 'type': 'type_adapter', 'optical_length': 0, 'mass': 15, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_M42_CS_Adapter': {'brand': 'ZWO', 'name': 'M42→CS Adapter', 'type': 'type_adapter', 'optical_length': 5, 'mass': 10, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'CS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_M54_M68_Adapter': {'brand': 'ZWO', 'name': 'M54→M68 Adapter', 'type': 'type_adapter', 'optical_length': 10, 'mass': 40, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_Canon_RF_M42_Adapter': {'brand': 'ZWO', 'name': 'Canon RF→M42 Adapter', 'type': 'type_adapter', 'optical_length': 5, 'mass': 25, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_Sony_E_M42_Adapter': {'brand': 'ZWO', 'name': 'Sony E→M42 Adapter', 'type': 'type_adapter', 'optical_length': 7, 'mass': 25, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_Nikon_Z_M42_Adapter': {'brand': 'ZWO', 'name': 'Nikon Z→M42 Adapter', 'type': 'type_adapter', 'optical_length': 6, 'mass': 25, 'tside_thread': 'Nikon Z', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_M54_M42_Adapter': {'brand': 'ZWO', 'name': 'M54→M42 Adapter', 'type': 'type_adapter', 'optical_length': 11, 'mass': 30, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_M42_M42_Extension_11mm': {'brand': 'ZWO', 'name': 'M42→M42 Extension 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 15, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_M42_M42_Extension_21mm': {'brand': 'ZWO', 'name': 'M42→M42 Extension 21mm', 'type': 'type_adapter', 'optical_length': 21, 'mass': 20, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_M42_Spacer_3mm': {'brand': 'ZWO', 'name': 'M42 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M42_Spacer_5mm': {'brand': 'ZWO', 'name': 'M42 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 8, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M42_Spacer_7mm': {'brand': 'ZWO', 'name': 'M42 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 9, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M42_Spacer_10mm': {'brand': 'ZWO', 'name': 'M42 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 12, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M42_Spacer_11mm': {'brand': 'ZWO', 'name': 'M42 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 12, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M42_Spacer_15mm': {'brand': 'ZWO', 'name': 'M42 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M42_Spacer_20mm': {'brand': 'ZWO', 'name': 'M42 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 20, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M42_Spacer_21mm': {'brand': 'ZWO', 'name': 'M42 Spacer 21mm', 'type': 'type_adapter', 'optical_length': 21, 'mass': 20, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M48_Spacer_5mm': {'brand': 'ZWO', 'name': 'M48 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 10, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M48_Spacer_7mm': {'brand': 'ZWO', 'name': 'M48 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 11, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M48_Spacer_10mm': {'brand': 'ZWO', 'name': 'M48 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 14, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M48_Spacer_15mm': {'brand': 'ZWO', 'name': 'M48 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M48_Spacer_20mm': {'brand': 'ZWO', 'name': 'M48 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 22, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M54_Spacer_5mm': {'brand': 'ZWO', 'name': 'M54 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 12, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M54_Spacer_10mm': {'brand': 'ZWO', 'name': 'M54 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 16, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_EFW_Camera_4_bolt_Adapter': {'brand': 'ZWO', 'name': 'EFW→Camera 4-bolt Adapter', 'type': 'type_adapter', 'optical_length': 1, 'mass': 20, 'tside_thread': 'ZWO 4-bolt', 'tside_gender': 'Female', 'cside_thread': 'ZWO 4-bolt', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_OAG_L_EFW_4_bolt_Adapter': {'brand': 'ZWO', 'name': 'OAG-L→EFW 4-bolt Adapter', 'type': 'type_adapter', 'optical_length': 1, 'mass': 20, 'tside_thread': 'ZWO 4-bolt', 'tside_gender': 'Female', 'cside_thread': 'ZWO 4-bolt', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_6_bolt_M54_Adapter_Ring': {'brand': 'ZWO', 'name': '6-bolt→M54 Adapter Ring', 'type': 'type_adapter', 'optical_length': 5, 'mass': 30, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_6_bolt_M42_Adapter_Ring': {'brand': 'ZWO', 'name': '6-bolt→M42 Adapter Ring', 'type': 'type_adapter', 'optical_length': 5, 'mass': 25, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_M42_Spacer_4mm': {'brand': 'ZWO', 'name': 'M42 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 7, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M42_Spacer_6mm': {'brand': 'ZWO', 'name': 'M42 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 8, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M42_Spacer_8mm': {'brand': 'ZWO', 'name': 'M42 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 10, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M42_Spacer_12mm': {'brand': 'ZWO', 'name': 'M42 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 13, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M42_Spacer_16mm': {'brand': 'ZWO', 'name': 'M42 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M42_Spacer_25mm': {'brand': 'ZWO', 'name': 'M42 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 24, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M42_Spacer_30mm': {'brand': 'ZWO', 'name': 'M42 Spacer 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 28, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M48_Spacer_3mm': {'brand': 'ZWO', 'name': 'M48 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M48_Spacer_4mm': {'brand': 'ZWO', 'name': 'M48 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 9, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M48_Spacer_6mm': {'brand': 'ZWO', 'name': 'M48 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 10, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M48_Spacer_8mm': {'brand': 'ZWO', 'name': 'M48 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 12, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M48_Spacer_12mm': {'brand': 'ZWO', 'name': 'M48 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 15, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M48_Spacer_25mm': {'brand': 'ZWO', 'name': 'M48 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 26, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M48_Spacer_30mm': {'brand': 'ZWO', 'name': 'M48 Spacer 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 30, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M54_Spacer_3mm': {'brand': 'ZWO', 'name': 'M54 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 10, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M54_Spacer_4mm': {'brand': 'ZWO', 'name': 'M54 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 11, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M54_Spacer_7mm': {'brand': 'ZWO', 'name': 'M54 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 13, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M54_Spacer_8mm': {'brand': 'ZWO', 'name': 'M54 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 14, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M54_Spacer_15mm': {'brand': 'ZWO', 'name': 'M54 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 20, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M54_Spacer_20mm': {'brand': 'ZWO', 'name': 'M54 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 24, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_ASI_2600_4_bolt_M42_Adapter': {'brand': 'ZWO', 'name': 'ASI 2600 4-bolt→M42 Adapter', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 20, 'tside_thread': 'ZWO 4-bolt', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_ASI_2600_6_bolt_M42_Adapter': {'brand': 'ZWO', 'name': 'ASI 2600 6-bolt→M42 Adapter', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 20, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_ASI_6200_4_bolt_M42_Adapter': {'brand': 'ZWO', 'name': 'ASI 6200 4-bolt→M42 Adapter', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 20, 'tside_thread': 'ZWO 4-bolt', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_ASI_6200_6_bolt_M42_Adapter': {'brand': 'ZWO', 'name': 'ASI 6200 6-bolt→M42 Adapter', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 20, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_ASI_294_4_bolt_M42_Adapter': {'brand': 'ZWO', 'name': 'ASI 294 4-bolt→M42 Adapter', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 20, 'tside_thread': 'ZWO 4-bolt', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_ASI_294_6_bolt_M42_Adapter': {'brand': 'ZWO', 'name': 'ASI 294 6-bolt→M42 Adapter', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 20, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_ASI_533_4_bolt_M42_Adapter': {'brand': 'ZWO', 'name': 'ASI 533 4-bolt→M42 Adapter', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 20, 'tside_thread': 'ZWO 4-bolt', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_ASI_533_6_bolt_M42_Adapter': {'brand': 'ZWO', 'name': 'ASI 533 6-bolt→M42 Adapter', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 20, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_ASI_183_4_bolt_M42_Adapter': {'brand': 'ZWO', 'name': 'ASI 183 4-bolt→M42 Adapter', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 20, 'tside_thread': 'ZWO 4-bolt', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_ASI_183_6_bolt_M42_Adapter': {'brand': 'ZWO', 'name': 'ASI 183 6-bolt→M42 Adapter', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 20, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_ASI_1600_4_bolt_M42_Adapter': {'brand': 'ZWO', 'name': 'ASI 1600 4-bolt→M42 Adapter', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 20, 'tside_thread': 'ZWO 4-bolt', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_ASI_1600_6_bolt_M42_Adapter': {'brand': 'ZWO', 'name': 'ASI 1600 6-bolt→M42 Adapter', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 20, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_ASI_071_4_bolt_M42_Adapter': {'brand': 'ZWO', 'name': 'ASI 071 4-bolt→M42 Adapter', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 20, 'tside_thread': 'ZWO 4-bolt', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_ASI_071_6_bolt_M42_Adapter': {'brand': 'ZWO', 'name': 'ASI 071 6-bolt→M42 Adapter', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 20, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_ASI_128_4_bolt_M42_Adapter': {'brand': 'ZWO', 'name': 'ASI 128 4-bolt→M42 Adapter', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 20, 'tside_thread': 'ZWO 4-bolt', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_ASI_128_6_bolt_M42_Adapter': {'brand': 'ZWO', 'name': 'ASI 128 6-bolt→M42 Adapter', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 20, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_ASI_2400_4_bolt_M42_Adapter': {'brand': 'ZWO', 'name': 'ASI 2400 4-bolt→M42 Adapter', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 20, 'tside_thread': 'ZWO 4-bolt', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_ASI_2400_6_bolt_M42_Adapter': {'brand': 'ZWO', 'name': 'ASI 2400 6-bolt→M42 Adapter', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 20, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_ASI_094_4_bolt_M42_Adapter': {'brand': 'ZWO', 'name': 'ASI 094 4-bolt→M42 Adapter', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 20, 'tside_thread': 'ZWO 4-bolt', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_ASI_094_6_bolt_M42_Adapter': {'brand': 'ZWO', 'name': 'ASI 094 6-bolt→M42 Adapter', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 20, 'tside_thread': 'ZWO 6-bolt', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_M42_Spacer_2_5mm': {'brand': 'ZWO', 'name': 'M42 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M42_Spacer_9mm': {'brand': 'ZWO', 'name': 'M42 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 11, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M42_Spacer_14mm': {'brand': 'ZWO', 'name': 'M42 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 15, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M42_Spacer_17mm': {'brand': 'ZWO', 'name': 'M42 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 17, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M42_Spacer_18mm': {'brand': 'ZWO', 'name': 'M42 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 18, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M42_Spacer_19mm': {'brand': 'ZWO', 'name': 'M42 Spacer 19mm', 'type': 'type_adapter', 'optical_length': 19, 'mass': 19, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M42_Spacer_22mm': {'brand': 'ZWO', 'name': 'M42 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 21, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M48_Spacer_2_5mm': {'brand': 'ZWO', 'name': 'M48 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M48_Spacer_9mm': {'brand': 'ZWO', 'name': 'M48 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 13, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M48_Spacer_11mm': {'brand': 'ZWO', 'name': 'M48 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 14, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M48_Spacer_14mm': {'brand': 'ZWO', 'name': 'M48 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 17, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M48_Spacer_17mm': {'brand': 'ZWO', 'name': 'M48 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 19, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M48_Spacer_22mm': {'brand': 'ZWO', 'name': 'M48 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 23, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M54_Spacer_6mm': {'brand': 'ZWO', 'name': 'M54 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 12, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M54_Spacer_9mm': {'brand': 'ZWO', 'name': 'M54 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 15, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M54_Spacer_11mm': {'brand': 'ZWO', 'name': 'M54 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 16, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M54_Spacer_12mm': {'brand': 'ZWO', 'name': 'M54 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 17, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M54_Spacer_14mm': {'brand': 'ZWO', 'name': 'M54 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 19, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M54_Spacer_17mm': {'brand': 'ZWO', 'name': 'M54 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 21, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M54_Spacer_25mm': {'brand': 'ZWO', 'name': 'M54 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 28, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M42_Spacer_2_3mm': {'brand': 'ZWO', 'name': 'M42 Spacer 2.3mm', 'type': 'type_adapter', 'optical_length': 2.3, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M42_Spacer_2_7mm': {'brand': 'ZWO', 'name': 'M42 Spacer 2.7mm', 'type': 'type_adapter', 'optical_length': 2.7, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M42_Spacer_3_5mm': {'brand': 'ZWO', 'name': 'M42 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M42_Spacer_4_5mm': {'brand': 'ZWO', 'name': 'M42 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 7, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M42_Spacer_5_5mm': {'brand': 'ZWO', 'name': 'M42 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 8, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M42_Spacer_6_5mm': {'brand': 'ZWO', 'name': 'M42 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 9, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M42_Spacer_8_5mm': {'brand': 'ZWO', 'name': 'M42 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 10, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M42_Spacer_13mm': {'brand': 'ZWO', 'name': 'M42 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 14, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M42_Spacer_23mm': {'brand': 'ZWO', 'name': 'M42 Spacer 23mm', 'type': 'type_adapter', 'optical_length': 23, 'mass': 22, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M42_Spacer_24mm': {'brand': 'ZWO', 'name': 'M42 Spacer 24mm', 'type': 'type_adapter', 'optical_length': 24, 'mass': 23, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M42_Spacer_26mm': {'brand': 'ZWO', 'name': 'M42 Spacer 26mm', 'type': 'type_adapter', 'optical_length': 26, 'mass': 24, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M42_Spacer_27mm': {'brand': 'ZWO', 'name': 'M42 Spacer 27mm', 'type': 'type_adapter', 'optical_length': 27, 'mass': 25, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M42_Spacer_28mm': {'brand': 'ZWO', 'name': 'M42 Spacer 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 26, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M48_Spacer_2_3mm': {'brand': 'ZWO', 'name': 'M48 Spacer 2.3mm', 'type': 'type_adapter', 'optical_length': 2.3, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M48_Spacer_3_5mm': {'brand': 'ZWO', 'name': 'M48 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M48_Spacer_4_5mm': {'brand': 'ZWO', 'name': 'M48 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 9, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M48_Spacer_5_5mm': {'brand': 'ZWO', 'name': 'M48 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 10, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M48_Spacer_6_5mm': {'brand': 'ZWO', 'name': 'M48 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 11, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M48_Spacer_8_5mm': {'brand': 'ZWO', 'name': 'M48 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 12, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M48_Spacer_9_5mm': {'brand': 'ZWO', 'name': 'M48 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 13, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M48_Spacer_13mm': {'brand': 'ZWO', 'name': 'M48 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 16, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M48_Spacer_16mm': {'brand': 'ZWO', 'name': 'M48 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M48_Spacer_18mm': {'brand': 'ZWO', 'name': 'M48 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 20, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M48_Spacer_19mm': {'brand': 'ZWO', 'name': 'M48 Spacer 19mm', 'type': 'type_adapter', 'optical_length': 19, 'mass': 21, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M48_Spacer_23mm': {'brand': 'ZWO', 'name': 'M48 Spacer 23mm', 'type': 'type_adapter', 'optical_length': 23, 'mass': 24, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M48_Spacer_24mm': {'brand': 'ZWO', 'name': 'M48 Spacer 24mm', 'type': 'type_adapter', 'optical_length': 24, 'mass': 25, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M48_Spacer_26mm': {'brand': 'ZWO', 'name': 'M48 Spacer 26mm', 'type': 'type_adapter', 'optical_length': 26, 'mass': 26, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ZWO_M42_Extension_Tube_3mm': {'brand': 'ZWO', 'name': 'M42 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 10, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_M42_Extension_Tube_6mm': {'brand': 'ZWO', 'name': 'M42 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 11, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_M42_Extension_Tube_9mm': {'brand': 'ZWO', 'name': 'M42 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 12, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_M42_Extension_Tube_11mm': {'brand': 'ZWO', 'name': 'M42 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 13, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_M42_Extension_Tube_13mm': {'brand': 'ZWO', 'name': 'M42 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 13, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_M42_Extension_Tube_16mm': {'brand': 'ZWO', 'name': 'M42 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 14, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_M42_Extension_Tube_22mm': {'brand': 'ZWO', 'name': 'M42 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_M42_Extension_Tube_28mm': {'brand': 'ZWO', 'name': 'M42 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 18, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_M42_Extension_Tube_35mm': {'brand': 'ZWO', 'name': 'M42 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 20, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_M42_Extension_Tube_45mm': {'brand': 'ZWO', 'name': 'M42 Extension Tube 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 23, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_M48_Extension_Tube_3mm': {'brand': 'ZWO', 'name': 'M48 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 14, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_M48_Extension_Tube_6mm': {'brand': 'ZWO', 'name': 'M48 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 15, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_M48_Extension_Tube_9mm': {'brand': 'ZWO', 'name': 'M48 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 16, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_M48_Extension_Tube_11mm': {'brand': 'ZWO', 'name': 'M48 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 17, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_M48_Extension_Tube_13mm': {'brand': 'ZWO', 'name': 'M48 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 17, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_M48_Extension_Tube_16mm': {'brand': 'ZWO', 'name': 'M48 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_M48_Extension_Tube_22mm': {'brand': 'ZWO', 'name': 'M48 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 20, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_M48_Extension_Tube_28mm': {'brand': 'ZWO', 'name': 'M48 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 22, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_M48_Extension_Tube_35mm': {'brand': 'ZWO', 'name': 'M48 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 24, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_M48_Extension_Tube_45mm': {'brand': 'ZWO', 'name': 'M48 Extension Tube 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 27, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_M54_Extension_Tube_3mm': {'brand': 'ZWO', 'name': 'M54 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 18, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_M54_Extension_Tube_6mm': {'brand': 'ZWO', 'name': 'M54 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 19, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_M54_Extension_Tube_9mm': {'brand': 'ZWO', 'name': 'M54 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 20, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_M54_Extension_Tube_11mm': {'brand': 'ZWO', 'name': 'M54 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 21, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_M54_Extension_Tube_13mm': {'brand': 'ZWO', 'name': 'M54 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 21, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_M54_Extension_Tube_16mm': {'brand': 'ZWO', 'name': 'M54 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 22, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_M54_Extension_Tube_22mm': {'brand': 'ZWO', 'name': 'M54 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 24, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_M54_Extension_Tube_28mm': {'brand': 'ZWO', 'name': 'M54 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 26, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_M54_Extension_Tube_35mm': {'brand': 'ZWO', 'name': 'M54 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 28, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ZWO_M54_Extension_Tube_45mm': {'brand': 'ZWO', 'name': 'M54 Extension Tube 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 31, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def ZWO_M42_M48_Adapter_5mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_M48_Adapter_5mm'])

    @classmethod
    def ZWO_M42_M54_Adapter_11mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_M54_Adapter_11mm'])

    @classmethod
    def ZWO_M48_M54_Adapter(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_M54_Adapter'])

    @classmethod
    def ZWO_EOS_M42_T_Adapter_11mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_EOS_M42_T_Adapter_11mm'])

    @classmethod
    def ZWO_EOS_M48_Adapter_8_5mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_EOS_M48_Adapter_8_5mm'])

    @classmethod
    def ZWO_Nikon_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['ZWO_Nikon_M42_Adapter'])

    @classmethod
    def ZWO_M42_M48_Adapter_short_1mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_M48_Adapter_short_1mm'])

    @classmethod
    def ZWO_M48_M42_Adapter_short(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_M42_Adapter_short'])

    @classmethod
    def ZWO_1_25_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['ZWO_1_25_M42_Adapter'])

    @classmethod
    def ZWO_2_M48_Adapter(cls):
        return cls.from_database(cls._DATABASE['ZWO_2_M48_Adapter'])

    @classmethod
    def ZWO_M42_CS_Adapter(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_CS_Adapter'])

    @classmethod
    def ZWO_M54_M68_Adapter(cls):
        return cls.from_database(cls._DATABASE['ZWO_M54_M68_Adapter'])

    @classmethod
    def ZWO_Canon_RF_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['ZWO_Canon_RF_M42_Adapter'])

    @classmethod
    def ZWO_Sony_E_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['ZWO_Sony_E_M42_Adapter'])

    @classmethod
    def ZWO_Nikon_Z_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['ZWO_Nikon_Z_M42_Adapter'])

    @classmethod
    def ZWO_M54_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['ZWO_M54_M42_Adapter'])

    @classmethod
    def ZWO_M42_M42_Extension_11mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_M42_Extension_11mm'])

    @classmethod
    def ZWO_M42_M42_Extension_21mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_M42_Extension_21mm'])

    @classmethod
    def ZWO_M42_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_3mm'])

    @classmethod
    def ZWO_M42_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_5mm'])

    @classmethod
    def ZWO_M42_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_7mm'])

    @classmethod
    def ZWO_M42_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_10mm'])

    @classmethod
    def ZWO_M42_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_11mm'])

    @classmethod
    def ZWO_M42_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_15mm'])

    @classmethod
    def ZWO_M42_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_20mm'])

    @classmethod
    def ZWO_M42_Spacer_21mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_21mm'])

    @classmethod
    def ZWO_M48_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Spacer_5mm'])

    @classmethod
    def ZWO_M48_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Spacer_7mm'])

    @classmethod
    def ZWO_M48_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Spacer_10mm'])

    @classmethod
    def ZWO_M48_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Spacer_15mm'])

    @classmethod
    def ZWO_M48_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Spacer_20mm'])

    @classmethod
    def ZWO_M54_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M54_Spacer_5mm'])

    @classmethod
    def ZWO_M54_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M54_Spacer_10mm'])

    @classmethod
    def ZWO_EFW_Camera_4_bolt_Adapter(cls):
        return cls.from_database(cls._DATABASE['ZWO_EFW_Camera_4_bolt_Adapter'])

    @classmethod
    def ZWO_OAG_L_EFW_4_bolt_Adapter(cls):
        return cls.from_database(cls._DATABASE['ZWO_OAG_L_EFW_4_bolt_Adapter'])

    @classmethod
    def ZWO_6_bolt_M54_Adapter_Ring(cls):
        return cls.from_database(cls._DATABASE['ZWO_6_bolt_M54_Adapter_Ring'])

    @classmethod
    def ZWO_6_bolt_M42_Adapter_Ring(cls):
        return cls.from_database(cls._DATABASE['ZWO_6_bolt_M42_Adapter_Ring'])

    @classmethod
    def ZWO_M42_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_4mm'])

    @classmethod
    def ZWO_M42_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_6mm'])

    @classmethod
    def ZWO_M42_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_8mm'])

    @classmethod
    def ZWO_M42_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_12mm'])

    @classmethod
    def ZWO_M42_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_16mm'])

    @classmethod
    def ZWO_M42_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_25mm'])

    @classmethod
    def ZWO_M42_Spacer_30mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_30mm'])

    @classmethod
    def ZWO_M48_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Spacer_3mm'])

    @classmethod
    def ZWO_M48_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Spacer_4mm'])

    @classmethod
    def ZWO_M48_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Spacer_6mm'])

    @classmethod
    def ZWO_M48_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Spacer_8mm'])

    @classmethod
    def ZWO_M48_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Spacer_12mm'])

    @classmethod
    def ZWO_M48_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Spacer_25mm'])

    @classmethod
    def ZWO_M48_Spacer_30mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Spacer_30mm'])

    @classmethod
    def ZWO_M54_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M54_Spacer_3mm'])

    @classmethod
    def ZWO_M54_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M54_Spacer_4mm'])

    @classmethod
    def ZWO_M54_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M54_Spacer_7mm'])

    @classmethod
    def ZWO_M54_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M54_Spacer_8mm'])

    @classmethod
    def ZWO_M54_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M54_Spacer_15mm'])

    @classmethod
    def ZWO_M54_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M54_Spacer_20mm'])

    @classmethod
    def ZWO_ASI_2600_4_bolt_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_2600_4_bolt_M42_Adapter'])

    @classmethod
    def ZWO_ASI_2600_6_bolt_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_2600_6_bolt_M42_Adapter'])

    @classmethod
    def ZWO_ASI_6200_4_bolt_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_6200_4_bolt_M42_Adapter'])

    @classmethod
    def ZWO_ASI_6200_6_bolt_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_6200_6_bolt_M42_Adapter'])

    @classmethod
    def ZWO_ASI_294_4_bolt_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_294_4_bolt_M42_Adapter'])

    @classmethod
    def ZWO_ASI_294_6_bolt_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_294_6_bolt_M42_Adapter'])

    @classmethod
    def ZWO_ASI_533_4_bolt_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_533_4_bolt_M42_Adapter'])

    @classmethod
    def ZWO_ASI_533_6_bolt_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_533_6_bolt_M42_Adapter'])

    @classmethod
    def ZWO_ASI_183_4_bolt_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_183_4_bolt_M42_Adapter'])

    @classmethod
    def ZWO_ASI_183_6_bolt_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_183_6_bolt_M42_Adapter'])

    @classmethod
    def ZWO_ASI_1600_4_bolt_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_1600_4_bolt_M42_Adapter'])

    @classmethod
    def ZWO_ASI_1600_6_bolt_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_1600_6_bolt_M42_Adapter'])

    @classmethod
    def ZWO_ASI_071_4_bolt_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_071_4_bolt_M42_Adapter'])

    @classmethod
    def ZWO_ASI_071_6_bolt_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_071_6_bolt_M42_Adapter'])

    @classmethod
    def ZWO_ASI_128_4_bolt_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_128_4_bolt_M42_Adapter'])

    @classmethod
    def ZWO_ASI_128_6_bolt_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_128_6_bolt_M42_Adapter'])

    @classmethod
    def ZWO_ASI_2400_4_bolt_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_2400_4_bolt_M42_Adapter'])

    @classmethod
    def ZWO_ASI_2400_6_bolt_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_2400_6_bolt_M42_Adapter'])

    @classmethod
    def ZWO_ASI_094_4_bolt_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_094_4_bolt_M42_Adapter'])

    @classmethod
    def ZWO_ASI_094_6_bolt_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['ZWO_ASI_094_6_bolt_M42_Adapter'])

    @classmethod
    def ZWO_M42_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_2_5mm'])

    @classmethod
    def ZWO_M42_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_9mm'])

    @classmethod
    def ZWO_M42_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_14mm'])

    @classmethod
    def ZWO_M42_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_17mm'])

    @classmethod
    def ZWO_M42_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_18mm'])

    @classmethod
    def ZWO_M42_Spacer_19mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_19mm'])

    @classmethod
    def ZWO_M42_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_22mm'])

    @classmethod
    def ZWO_M48_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Spacer_2_5mm'])

    @classmethod
    def ZWO_M48_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Spacer_9mm'])

    @classmethod
    def ZWO_M48_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Spacer_11mm'])

    @classmethod
    def ZWO_M48_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Spacer_14mm'])

    @classmethod
    def ZWO_M48_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Spacer_17mm'])

    @classmethod
    def ZWO_M48_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Spacer_22mm'])

    @classmethod
    def ZWO_M54_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M54_Spacer_6mm'])

    @classmethod
    def ZWO_M54_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M54_Spacer_9mm'])

    @classmethod
    def ZWO_M54_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M54_Spacer_11mm'])

    @classmethod
    def ZWO_M54_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M54_Spacer_12mm'])

    @classmethod
    def ZWO_M54_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M54_Spacer_14mm'])

    @classmethod
    def ZWO_M54_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M54_Spacer_17mm'])

    @classmethod
    def ZWO_M54_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M54_Spacer_25mm'])

    @classmethod
    def ZWO_M42_Spacer_2_3mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_2_3mm'])

    @classmethod
    def ZWO_M42_Spacer_2_7mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_2_7mm'])

    @classmethod
    def ZWO_M42_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_3_5mm'])

    @classmethod
    def ZWO_M42_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_4_5mm'])

    @classmethod
    def ZWO_M42_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_5_5mm'])

    @classmethod
    def ZWO_M42_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_6_5mm'])

    @classmethod
    def ZWO_M42_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_8_5mm'])

    @classmethod
    def ZWO_M42_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_13mm'])

    @classmethod
    def ZWO_M42_Spacer_23mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_23mm'])

    @classmethod
    def ZWO_M42_Spacer_24mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_24mm'])

    @classmethod
    def ZWO_M42_Spacer_26mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_26mm'])

    @classmethod
    def ZWO_M42_Spacer_27mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_27mm'])

    @classmethod
    def ZWO_M42_Spacer_28mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_28mm'])

    @classmethod
    def ZWO_M48_Spacer_2_3mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Spacer_2_3mm'])

    @classmethod
    def ZWO_M48_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Spacer_3_5mm'])

    @classmethod
    def ZWO_M48_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Spacer_4_5mm'])

    @classmethod
    def ZWO_M48_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Spacer_5_5mm'])

    @classmethod
    def ZWO_M48_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Spacer_6_5mm'])

    @classmethod
    def ZWO_M48_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Spacer_8_5mm'])

    @classmethod
    def ZWO_M48_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Spacer_9_5mm'])

    @classmethod
    def ZWO_M48_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Spacer_13mm'])

    @classmethod
    def ZWO_M48_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Spacer_16mm'])

    @classmethod
    def ZWO_M48_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Spacer_18mm'])

    @classmethod
    def ZWO_M48_Spacer_19mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Spacer_19mm'])

    @classmethod
    def ZWO_M48_Spacer_23mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Spacer_23mm'])

    @classmethod
    def ZWO_M48_Spacer_24mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Spacer_24mm'])

    @classmethod
    def ZWO_M48_Spacer_26mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Spacer_26mm'])

    @classmethod
    def ZWO_M42_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Extension_Tube_3mm'])

    @classmethod
    def ZWO_M42_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Extension_Tube_6mm'])

    @classmethod
    def ZWO_M42_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Extension_Tube_9mm'])

    @classmethod
    def ZWO_M42_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Extension_Tube_11mm'])

    @classmethod
    def ZWO_M42_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Extension_Tube_13mm'])

    @classmethod
    def ZWO_M42_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Extension_Tube_16mm'])

    @classmethod
    def ZWO_M42_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Extension_Tube_22mm'])

    @classmethod
    def ZWO_M42_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Extension_Tube_28mm'])

    @classmethod
    def ZWO_M42_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Extension_Tube_35mm'])

    @classmethod
    def ZWO_M42_Extension_Tube_45mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Extension_Tube_45mm'])

    @classmethod
    def ZWO_M48_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Extension_Tube_3mm'])

    @classmethod
    def ZWO_M48_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Extension_Tube_6mm'])

    @classmethod
    def ZWO_M48_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Extension_Tube_9mm'])

    @classmethod
    def ZWO_M48_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Extension_Tube_11mm'])

    @classmethod
    def ZWO_M48_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Extension_Tube_13mm'])

    @classmethod
    def ZWO_M48_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Extension_Tube_16mm'])

    @classmethod
    def ZWO_M48_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Extension_Tube_22mm'])

    @classmethod
    def ZWO_M48_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Extension_Tube_28mm'])

    @classmethod
    def ZWO_M48_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Extension_Tube_35mm'])

    @classmethod
    def ZWO_M48_Extension_Tube_45mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Extension_Tube_45mm'])

    @classmethod
    def ZWO_M54_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M54_Extension_Tube_3mm'])

    @classmethod
    def ZWO_M54_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M54_Extension_Tube_6mm'])

    @classmethod
    def ZWO_M54_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M54_Extension_Tube_9mm'])

    @classmethod
    def ZWO_M54_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M54_Extension_Tube_11mm'])

    @classmethod
    def ZWO_M54_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M54_Extension_Tube_13mm'])

    @classmethod
    def ZWO_M54_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M54_Extension_Tube_16mm'])

    @classmethod
    def ZWO_M54_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M54_Extension_Tube_22mm'])

    @classmethod
    def ZWO_M54_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M54_Extension_Tube_28mm'])

    @classmethod
    def ZWO_M54_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M54_Extension_Tube_35mm'])

    @classmethod
    def ZWO_M54_Extension_Tube_45mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M54_Extension_Tube_45mm'])

class ZwoSpacer(Spacer):
    _DATABASE = {'ZWO_M42_Spacer_1mm': {'brand': 'ZWO', 'name': 'M42 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ZWO_M42_Spacer_2mm': {'brand': 'ZWO', 'name': 'M42 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ZWO_M48_Spacer_1mm': {'brand': 'ZWO', 'name': 'M48 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ZWO_M48_Spacer_2mm': {'brand': 'ZWO', 'name': 'M48 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ZWO_M54_Spacer_2mm': {'brand': 'ZWO', 'name': 'M54 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ZWO_M42_Spacer_0_5mm': {'brand': 'ZWO', 'name': 'M42 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ZWO_M48_Spacer_0_5mm': {'brand': 'ZWO', 'name': 'M48 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ZWO_M54_Spacer_0_5mm': {'brand': 'ZWO', 'name': 'M54 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ZWO_M54_Spacer_1mm': {'brand': 'ZWO', 'name': 'M54 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ZWO_M42_Spacer_0_75mm': {'brand': 'ZWO', 'name': 'M42 Spacer 0.75mm', 'type': 'type_spacer', 'optical_length': 0.75, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ZWO_M42_Spacer_1_5mm': {'brand': 'ZWO', 'name': 'M42 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ZWO_M48_Spacer_0_75mm': {'brand': 'ZWO', 'name': 'M48 Spacer 0.75mm', 'type': 'type_spacer', 'optical_length': 0.75, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ZWO_M48_Spacer_1_5mm': {'brand': 'ZWO', 'name': 'M48 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ZWO_M54_Spacer_1_5mm': {'brand': 'ZWO', 'name': 'M54 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ZWO_M42_Spacer_1_3mm': {'brand': 'ZWO', 'name': 'M42 Spacer 1.3mm', 'type': 'type_spacer', 'optical_length': 1.3, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ZWO_M42_Spacer_1_7mm': {'brand': 'ZWO', 'name': 'M42 Spacer 1.7mm', 'type': 'type_spacer', 'optical_length': 1.7, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ZWO_M48_Spacer_1_3mm': {'brand': 'ZWO', 'name': 'M48 Spacer 1.3mm', 'type': 'type_spacer', 'optical_length': 1.3, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ZWO_M48_Spacer_1_7mm': {'brand': 'ZWO', 'name': 'M48 Spacer 1.7mm', 'type': 'type_spacer', 'optical_length': 1.7, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}}

    @classmethod
    def ZWO_M42_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_1mm'])

    @classmethod
    def ZWO_M42_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_2mm'])

    @classmethod
    def ZWO_M48_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Spacer_1mm'])

    @classmethod
    def ZWO_M48_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Spacer_2mm'])

    @classmethod
    def ZWO_M54_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M54_Spacer_2mm'])

    @classmethod
    def ZWO_M42_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_0_5mm'])

    @classmethod
    def ZWO_M48_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Spacer_0_5mm'])

    @classmethod
    def ZWO_M54_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M54_Spacer_0_5mm'])

    @classmethod
    def ZWO_M54_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M54_Spacer_1mm'])

    @classmethod
    def ZWO_M42_Spacer_0_75mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_0_75mm'])

    @classmethod
    def ZWO_M42_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_1_5mm'])

    @classmethod
    def ZWO_M48_Spacer_0_75mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Spacer_0_75mm'])

    @classmethod
    def ZWO_M48_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Spacer_1_5mm'])

    @classmethod
    def ZWO_M54_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M54_Spacer_1_5mm'])

    @classmethod
    def ZWO_M42_Spacer_1_3mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_1_3mm'])

    @classmethod
    def ZWO_M42_Spacer_1_7mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M42_Spacer_1_7mm'])

    @classmethod
    def ZWO_M48_Spacer_1_3mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Spacer_1_3mm'])

    @classmethod
    def ZWO_M48_Spacer_1_7mm(cls):
        return cls.from_database(cls._DATABASE['ZWO_M48_Spacer_1_7mm'])