from ...abstract import IntermediateOpticalEquipment
from ....constants import OpticalType
from ..base import Adapter, Spacer

class BaaderAdapter(Adapter):
    _DATABASE = {'Baader_M42_M48_Adapter_0_5mm': {'brand': 'Baader', 'name': 'M42→M48 Adapter (0.5mm)', 'type': 'type_adapter', 'optical_length': 0.5, 'mass': 30, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_M42_Adapter_16_5mm': {'brand': 'Baader', 'name': 'M48→M42 Adapter (16.5mm)', 'type': 'type_adapter', 'optical_length': 16.5, 'mass': 40, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M48_M54_Adapter_7_5mm': {'brand': 'Baader', 'name': 'M48→M54 Adapter (7.5mm)', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 40, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M54_M48_Adapter_7_5mm': {'brand': 'Baader', 'name': 'M54→M48 Adapter (7.5mm)', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 40, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M54_M68_Adapter_1_4mm': {'brand': 'Baader', 'name': 'M54→M68 Adapter (1.4mm)', 'type': 'type_adapter', 'optical_length': 1.4, 'mass': 30, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M54_M68_Adapter_10_4mm': {'brand': 'Baader', 'name': 'M54→M68 Adapter (10.4mm)', 'type': 'type_adapter', 'optical_length': 10.4, 'mass': 50, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M68_M54_Adapter_1_4mm': {'brand': 'Baader', 'name': 'M68→M54 Adapter (1.4mm)', 'type': 'type_adapter', 'optical_length': 1.4, 'mass': 30, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M68_M72_Adapter_10mm': {'brand': 'Baader', 'name': 'M68→M72 Adapter (10mm)', 'type': 'type_adapter', 'optical_length': 10, 'mass': 60, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M68_M72_Adapter_35mm': {'brand': 'Baader', 'name': 'M68→M72 Adapter (35mm)', 'type': 'type_adapter', 'optical_length': 35, 'mass': 100, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M81_M68_Adapter': {'brand': 'Baader', 'name': 'M81→M68 Adapter', 'type': 'type_adapter', 'optical_length': 4, 'mass': 60, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M81', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_SC_M42_Adapter_50mm': {'brand': 'Baader', 'name': 'SC→M42 Adapter (50mm)', 'type': 'type_adapter', 'optical_length': 50, 'mass': 80, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_SC_M48_Adapter_2mm': {'brand': 'Baader', 'name': 'SC→M48 Adapter (2mm)', 'type': 'type_adapter', 'optical_length': 2, 'mass': 40, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_SC_M48_Adapter_20mm': {'brand': 'Baader', 'name': 'SC→M48 Adapter (20mm)', 'type': 'type_adapter', 'optical_length': 20, 'mass': 80, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_SC_M54_Adapter': {'brand': 'Baader', 'name': 'SC→M54 Adapter', 'type': 'type_adapter', 'optical_length': 15, 'mass': 70, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_SC_M68_Adapter_15mm': {'brand': 'Baader', 'name': 'SC→M68 Adapter (15mm)', 'type': 'type_adapter', 'optical_length': 15, 'mass': 80, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_SC_M72_Adapter_20mm': {'brand': 'Baader', 'name': 'SC→M72 Adapter (20mm)', 'type': 'type_adapter', 'optical_length': 20, 'mass': 80, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_EOS_M48_Adapter_8mm': {'brand': 'Baader', 'name': 'EOS→M48 Adapter (8mm)', 'type': 'type_adapter', 'optical_length': 8, 'mass': 40, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_EOS_M54_Adapter_9_5mm': {'brand': 'Baader', 'name': 'EOS→M54 Adapter (9.5mm)', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 50, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_T2_Ring_Canon_EOS_10_5mm': {'brand': 'Baader', 'name': 'T2 Ring Canon EOS (10.5mm)', 'type': 'type_adapter', 'optical_length': 10.5, 'mass': 30, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_T2_Ring_Nikon_F_8_5mm': {'brand': 'Baader', 'name': 'T2 Ring Nikon F (8.5mm)', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 30, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_T2_Ring_Sony_E': {'brand': 'Baader', 'name': 'T2 Ring Sony E', 'type': 'type_adapter', 'optical_length': 7, 'mass': 30, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M56_M54_Adapter': {'brand': 'Baader', 'name': 'M56→M54 Adapter', 'type': 'type_adapter', 'optical_length': 2, 'mass': 25, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M63_M68_Adapter': {'brand': 'Baader', 'name': 'M63→M68 Adapter', 'type': 'type_adapter', 'optical_length': 5, 'mass': 40, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M63', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M82_M68_Adapter': {'brand': 'Baader', 'name': 'M82→M68 Adapter', 'type': 'type_adapter', 'optical_length': 6, 'mass': 50, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M92_M82_Adapter': {'brand': 'Baader', 'name': 'M92→M82 Adapter', 'type': 'type_adapter', 'optical_length': 8, 'mass': 60, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M68_M42_Adapter': {'brand': 'Baader', 'name': 'M68→M42 Adapter', 'type': 'type_adapter', 'optical_length': 10, 'mass': 40, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M54_M42_Adapter_11mm': {'brand': 'Baader', 'name': 'M54→M42 Adapter (11mm)', 'type': 'type_adapter', 'optical_length': 11, 'mass': 35, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M42_Coupling_Ring_F_F': {'brand': 'Baader', 'name': 'M42 Coupling Ring (F-F)', 'type': 'type_adapter', 'optical_length': 2, 'mass': 15, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Coupling_Ring_F_F': {'brand': 'Baader', 'name': 'M48 Coupling Ring (F-F)', 'type': 'type_adapter', 'optical_length': 2, 'mass': 20, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Coupling_Ring_F_F': {'brand': 'Baader', 'name': 'M54 Coupling Ring (F-F)', 'type': 'type_adapter', 'optical_length': 2, 'mass': 25, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Coupling_Ring_F_F': {'brand': 'Baader', 'name': 'M68 Coupling Ring (F-F)', 'type': 'type_adapter', 'optical_length': 3, 'mass': 30, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': True, 'bf_role': ''}, 'Baader_2_M48_Adapter': {'brand': 'Baader', 'name': '2"→M48 Adapter', 'type': 'type_adapter', 'optical_length': 0, 'mass': 20, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_2_M42_Adapter': {'brand': 'Baader', 'name': '2"→M42 Adapter', 'type': 'type_adapter', 'optical_length': 0, 'mass': 15, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_1_25_M42_Adapter': {'brand': 'Baader', 'name': '1.25"→M42 Adapter', 'type': 'type_adapter', 'optical_length': 0, 'mass': 10, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_Nikon_M48_Adapter': {'brand': 'Baader', 'name': 'Nikon→M48 Adapter', 'type': 'type_adapter', 'optical_length': 8, 'mass': 35, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_ClickLock_M42_Clamp': {'brand': 'Baader', 'name': 'ClickLock M42 Clamp', 'type': 'type_adapter', 'optical_length': 2, 'mass': 30, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_ClickLock_M48_Clamp': {'brand': 'Baader', 'name': 'ClickLock M48 Clamp', 'type': 'type_adapter', 'optical_length': 2, 'mass': 35, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_ClickLock_M54_Clamp': {'brand': 'Baader', 'name': 'ClickLock M54 Clamp', 'type': 'type_adapter', 'optical_length': 3, 'mass': 40, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_ClickLock_M68_Clamp': {'brand': 'Baader', 'name': 'ClickLock M68 Clamp', 'type': 'type_adapter', 'optical_length': 3, 'mass': 45, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_ClickLock_SC_Clamp': {'brand': 'Baader', 'name': 'ClickLock SC Clamp', 'type': 'type_adapter', 'optical_length': 3, 'mass': 50, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_ClickLock_2_Clamp_M48': {'brand': 'Baader', 'name': 'ClickLock 2" Clamp (M48)', 'type': 'type_adapter', 'optical_length': 3, 'mass': 35, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M42_M68_Adapter': {'brand': 'Baader', 'name': 'M42→M68 Adapter', 'type': 'type_adapter', 'optical_length': 10, 'mass': 40, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M48_M68_Adapter': {'brand': 'Baader', 'name': 'M48→M68 Adapter', 'type': 'type_adapter', 'optical_length': 8, 'mass': 40, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M72_M82_Adapter': {'brand': 'Baader', 'name': 'M72→M82 Adapter', 'type': 'type_adapter', 'optical_length': 6, 'mass': 50, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_Canon_RF_M48_Adapter': {'brand': 'Baader', 'name': 'Canon RF→M48 Adapter', 'type': 'type_adapter', 'optical_length': 5, 'mass': 35, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'Canon RF', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_Nikon_Z_M48_Adapter': {'brand': 'Baader', 'name': 'Nikon Z→M48 Adapter', 'type': 'type_adapter', 'optical_length': 6, 'mass': 35, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'Nikon Z', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_Sony_E_M48_Adapter': {'brand': 'Baader', 'name': 'Sony E→M48 Adapter', 'type': 'type_adapter', 'optical_length': 7, 'mass': 35, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M42_Spacer_3mm': {'brand': 'Baader', 'name': 'M42 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_5mm': {'brand': 'Baader', 'name': 'M42 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 8, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_7mm': {'brand': 'Baader', 'name': 'M42 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 9, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_7_5mm': {'brand': 'Baader', 'name': 'M42 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 10, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_10mm': {'brand': 'Baader', 'name': 'M42 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 12, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_11mm': {'brand': 'Baader', 'name': 'M42 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 12, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_15mm': {'brand': 'Baader', 'name': 'M42 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_20mm': {'brand': 'Baader', 'name': 'M42 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 20, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_25mm': {'brand': 'Baader', 'name': 'M42 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 24, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_30mm': {'brand': 'Baader', 'name': 'M42 Spacer 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 28, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_40mm': {'brand': 'Baader', 'name': 'M42 Spacer 40mm', 'type': 'type_adapter', 'optical_length': 40, 'mass': 36, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_3mm': {'brand': 'Baader', 'name': 'M48 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_5mm': {'brand': 'Baader', 'name': 'M48 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 10, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_7mm': {'brand': 'Baader', 'name': 'M48 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 11, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_10mm': {'brand': 'Baader', 'name': 'M48 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 14, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_15mm': {'brand': 'Baader', 'name': 'M48 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_16mm': {'brand': 'Baader', 'name': 'M48 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_20mm': {'brand': 'Baader', 'name': 'M48 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 22, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_25mm': {'brand': 'Baader', 'name': 'M48 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 26, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_30mm': {'brand': 'Baader', 'name': 'M48 Spacer 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 30, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_40mm': {'brand': 'Baader', 'name': 'M48 Spacer 40mm', 'type': 'type_adapter', 'optical_length': 40, 'mass': 38, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_5mm': {'brand': 'Baader', 'name': 'M54 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 12, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_9mm': {'brand': 'Baader', 'name': 'M54 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 15, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_10mm': {'brand': 'Baader', 'name': 'M54 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 16, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_15mm': {'brand': 'Baader', 'name': 'M54 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 20, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_16mm': {'brand': 'Baader', 'name': 'M54 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 20, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_20mm': {'brand': 'Baader', 'name': 'M54 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 24, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_3mm': {'brand': 'Baader', 'name': 'M68 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 12, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_5mm': {'brand': 'Baader', 'name': 'M68 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 14, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_7mm': {'brand': 'Baader', 'name': 'M68 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 15, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_10mm': {'brand': 'Baader', 'name': 'M68 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 18, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_15mm': {'brand': 'Baader', 'name': 'M68 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 22, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_20mm': {'brand': 'Baader', 'name': 'M68 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 26, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_25mm': {'brand': 'Baader', 'name': 'M68 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 30, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_30mm': {'brand': 'Baader', 'name': 'M68 Spacer 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 34, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_32mm': {'brand': 'Baader', 'name': 'M68 Spacer 32mm', 'type': 'type_adapter', 'optical_length': 32, 'mass': 35, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M72_Spacer_3mm': {'brand': 'Baader', 'name': 'M72 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 14, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M72_Spacer_5mm': {'brand': 'Baader', 'name': 'M72 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 16, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M72_Spacer_10mm': {'brand': 'Baader', 'name': 'M72 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 20, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M72_Spacer_15mm': {'brand': 'Baader', 'name': 'M72 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 24, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M72_Spacer_20mm': {'brand': 'Baader', 'name': 'M72 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 28, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M82_Spacer_5mm': {'brand': 'Baader', 'name': 'M82 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 19, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M82_Spacer_10mm': {'brand': 'Baader', 'name': 'M82 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 23, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M82_Spacer_15mm': {'brand': 'Baader', 'name': 'M82 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 27, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M82_Spacer_20mm': {'brand': 'Baader', 'name': 'M82 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 31, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M92_Spacer_5mm': {'brand': 'Baader', 'name': 'M92 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 22, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M92_Spacer_10mm': {'brand': 'Baader', 'name': 'M92 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 26, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M92_Spacer_15mm': {'brand': 'Baader', 'name': 'M92 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 30, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M92_Spacer_20mm': {'brand': 'Baader', 'name': 'M92 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 34, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_M_M_Coupling': {'brand': 'Baader', 'name': 'M42 M-M Coupling', 'type': 'type_adapter', 'optical_length': 2, 'mass': 15, 'tside_thread': 'M42', 'tside_gender': 'Male', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_M_M_Coupling': {'brand': 'Baader', 'name': 'M48 M-M Coupling', 'type': 'type_adapter', 'optical_length': 2, 'mass': 20, 'tside_thread': 'M48', 'tside_gender': 'Male', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M54_M_M_Coupling': {'brand': 'Baader', 'name': 'M54 M-M Coupling', 'type': 'type_adapter', 'optical_length': 2, 'mass': 25, 'tside_thread': 'M54', 'tside_gender': 'Male', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M68_M_M_Coupling': {'brand': 'Baader', 'name': 'M68 M-M Coupling', 'type': 'type_adapter', 'optical_length': 3, 'mass': 30, 'tside_thread': 'M68', 'tside_gender': 'Male', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_SC_Schmidt_Cassegrain_Spacer_5mm': {'brand': 'Baader', 'name': 'SC (Schmidt-Cassegrain) Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 24, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_SC_Schmidt_Cassegrain_Spacer_10mm': {'brand': 'Baader', 'name': 'SC (Schmidt-Cassegrain) Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 28, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_SC_Schmidt_Cassegrain_Spacer_15mm': {'brand': 'Baader', 'name': 'SC (Schmidt-Cassegrain) Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 32, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_SC_Schmidt_Cassegrain_Spacer_20mm': {'brand': 'Baader', 'name': 'SC (Schmidt-Cassegrain) Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 36, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_SC_Schmidt_Cassegrain_Spacer_25mm': {'brand': 'Baader', 'name': 'SC (Schmidt-Cassegrain) Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 40, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_SC_Schmidt_Cassegrain_Spacer_30mm': {'brand': 'Baader', 'name': 'SC (Schmidt-Cassegrain) Spacer 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 44, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_SC_Schmidt_Cassegrain_Spacer_40mm': {'brand': 'Baader', 'name': 'SC (Schmidt-Cassegrain) Spacer 40mm', 'type': 'type_adapter', 'optical_length': 40, 'mass': 52, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_4mm': {'brand': 'Baader', 'name': 'M42 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 7, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_6mm': {'brand': 'Baader', 'name': 'M42 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 8, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_8mm': {'brand': 'Baader', 'name': 'M42 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 10, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_12mm': {'brand': 'Baader', 'name': 'M42 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 13, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_14mm': {'brand': 'Baader', 'name': 'M42 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 15, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_17mm': {'brand': 'Baader', 'name': 'M42 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 17, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_22mm': {'brand': 'Baader', 'name': 'M42 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 21, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_28mm': {'brand': 'Baader', 'name': 'M42 Spacer 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 26, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_35mm': {'brand': 'Baader', 'name': 'M42 Spacer 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 32, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_4mm': {'brand': 'Baader', 'name': 'M48 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 9, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_6mm': {'brand': 'Baader', 'name': 'M48 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 10, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_8mm': {'brand': 'Baader', 'name': 'M48 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 12, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_9mm': {'brand': 'Baader', 'name': 'M48 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 13, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_11mm': {'brand': 'Baader', 'name': 'M48 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 14, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_12mm': {'brand': 'Baader', 'name': 'M48 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 15, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_14mm': {'brand': 'Baader', 'name': 'M48 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 17, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_17mm': {'brand': 'Baader', 'name': 'M48 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 19, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_22mm': {'brand': 'Baader', 'name': 'M48 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 23, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_28mm': {'brand': 'Baader', 'name': 'M48 Spacer 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 28, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_35mm': {'brand': 'Baader', 'name': 'M48 Spacer 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 34, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_3mm': {'brand': 'Baader', 'name': 'M54 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 10, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_4mm': {'brand': 'Baader', 'name': 'M54 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 11, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_7mm': {'brand': 'Baader', 'name': 'M54 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 13, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_8mm': {'brand': 'Baader', 'name': 'M54 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 14, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_11mm': {'brand': 'Baader', 'name': 'M54 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 16, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_12mm': {'brand': 'Baader', 'name': 'M54 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 17, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_14mm': {'brand': 'Baader', 'name': 'M54 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 19, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_18mm': {'brand': 'Baader', 'name': 'M54 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 22, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_22mm': {'brand': 'Baader', 'name': 'M54 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 25, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_25mm': {'brand': 'Baader', 'name': 'M54 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 28, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_4mm': {'brand': 'Baader', 'name': 'M68 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 13, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_6mm': {'brand': 'Baader', 'name': 'M68 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 14, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_8mm': {'brand': 'Baader', 'name': 'M68 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 16, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_9mm': {'brand': 'Baader', 'name': 'M68 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 17, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_11mm': {'brand': 'Baader', 'name': 'M68 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 18, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_12mm': {'brand': 'Baader', 'name': 'M68 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 19, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_14mm': {'brand': 'Baader', 'name': 'M68 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 21, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_17mm': {'brand': 'Baader', 'name': 'M68 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 23, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_22mm': {'brand': 'Baader', 'name': 'M68 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 27, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_28mm': {'brand': 'Baader', 'name': 'M68 Spacer 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 32, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_35mm': {'brand': 'Baader', 'name': 'M68 Spacer 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 38, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Varilock_25_35mm': {'brand': 'Baader', 'name': 'M42 Varilock (25-35mm)', 'type': 'type_adapter', 'optical_length': 30, 'mass': 55, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M48_Varilock_25_35mm': {'brand': 'Baader', 'name': 'M48 Varilock (25-35mm)', 'type': 'type_adapter', 'optical_length': 30, 'mass': 65, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M54_Varilock_25_35mm': {'brand': 'Baader', 'name': 'M54 Varilock (25-35mm)', 'type': 'type_adapter', 'optical_length': 30, 'mass': 75, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M42_Male_Male_Ring': {'brand': 'Baader', 'name': 'M42 Male-Male Ring', 'type': 'type_adapter', 'optical_length': 2, 'mass': 15, 'tside_thread': 'M42', 'tside_gender': 'Male', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Male_Male_Ring': {'brand': 'Baader', 'name': 'M48 Male-Male Ring', 'type': 'type_adapter', 'optical_length': 2, 'mass': 20, 'tside_thread': 'M48', 'tside_gender': 'Male', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Male_Male_Ring': {'brand': 'Baader', 'name': 'M54 Male-Male Ring', 'type': 'type_adapter', 'optical_length': 2, 'mass': 25, 'tside_thread': 'M54', 'tside_gender': 'Male', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M56_Spacer_5mm': {'brand': 'Baader', 'name': 'M56 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 12, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M56_Spacer_10mm': {'brand': 'Baader', 'name': 'M56 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 16, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M56_Spacer_15mm': {'brand': 'Baader', 'name': 'M56 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 20, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M63_Spacer_5mm': {'brand': 'Baader', 'name': 'M63 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 14, 'tside_thread': 'M63', 'tside_gender': 'Female', 'cside_thread': 'M63', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M63_Spacer_10mm': {'brand': 'Baader', 'name': 'M63 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 18, 'tside_thread': 'M63', 'tside_gender': 'Female', 'cside_thread': 'M63', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M63_Spacer_15mm': {'brand': 'Baader', 'name': 'M63 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 22, 'tside_thread': 'M63', 'tside_gender': 'Female', 'cside_thread': 'M63', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M84_Spacer_5mm': {'brand': 'Baader', 'name': 'M84 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 18, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M84_Spacer_10mm': {'brand': 'Baader', 'name': 'M84 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 22, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M84_Spacer_15mm': {'brand': 'Baader', 'name': 'M84 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 26, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M84_Spacer_20mm': {'brand': 'Baader', 'name': 'M84 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 30, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_2_1_25_Reducer_short': {'brand': 'Baader', 'name': '2"→1.25" Reducer (short)', 'type': 'type_adapter', 'optical_length': 0, 'mass': 15, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_SC_T2_M42_Ultra_Short': {'brand': 'Baader', 'name': 'SC→T2 (M42) Ultra-Short', 'type': 'type_adapter', 'optical_length': 3, 'mass': 35, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_SC_M54_Diamond_Adapter': {'brand': 'Baader', 'name': 'SC→M54 Diamond Adapter', 'type': 'type_adapter', 'optical_length': 8, 'mass': 55, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_SC_M68_Diamond_Adapter': {'brand': 'Baader', 'name': 'SC→M68 Diamond Adapter', 'type': 'type_adapter', 'optical_length': 10, 'mass': 65, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M42_Spacer_2_5mm': {'brand': 'Baader', 'name': 'M42 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_3_5mm': {'brand': 'Baader', 'name': 'M42 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_9mm': {'brand': 'Baader', 'name': 'M42 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 11, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_2_5mm': {'brand': 'Baader', 'name': 'M48 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_3_5mm': {'brand': 'Baader', 'name': 'M48 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_2_5mm': {'brand': 'Baader', 'name': 'M54 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 10, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_6mm': {'brand': 'Baader', 'name': 'M54 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 12, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_17mm': {'brand': 'Baader', 'name': 'M54 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 21, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_28mm': {'brand': 'Baader', 'name': 'M54 Spacer 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 30, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_2_5mm': {'brand': 'Baader', 'name': 'M68 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 12, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_2_1mm': {'brand': 'Baader', 'name': 'M42 Spacer 2.1mm', 'type': 'type_adapter', 'optical_length': 2.1, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_2_3mm': {'brand': 'Baader', 'name': 'M42 Spacer 2.3mm', 'type': 'type_adapter', 'optical_length': 2.3, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_2_7mm': {'brand': 'Baader', 'name': 'M42 Spacer 2.7mm', 'type': 'type_adapter', 'optical_length': 2.7, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_3_2mm': {'brand': 'Baader', 'name': 'M42 Spacer 3.2mm', 'type': 'type_adapter', 'optical_length': 3.2, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_3_3mm': {'brand': 'Baader', 'name': 'M42 Spacer 3.3mm', 'type': 'type_adapter', 'optical_length': 3.3, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_3_7mm': {'brand': 'Baader', 'name': 'M42 Spacer 3.7mm', 'type': 'type_adapter', 'optical_length': 3.7, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_4_5mm': {'brand': 'Baader', 'name': 'M42 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 7, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_5_5mm': {'brand': 'Baader', 'name': 'M42 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 8, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_6_5mm': {'brand': 'Baader', 'name': 'M42 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 9, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_8_5mm': {'brand': 'Baader', 'name': 'M42 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 10, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_9_5mm': {'brand': 'Baader', 'name': 'M42 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 11, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_13mm': {'brand': 'Baader', 'name': 'M42 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 14, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_16mm': {'brand': 'Baader', 'name': 'M42 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_18mm': {'brand': 'Baader', 'name': 'M42 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 18, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_19mm': {'brand': 'Baader', 'name': 'M42 Spacer 19mm', 'type': 'type_adapter', 'optical_length': 19, 'mass': 19, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_21mm': {'brand': 'Baader', 'name': 'M42 Spacer 21mm', 'type': 'type_adapter', 'optical_length': 21, 'mass': 20, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_23mm': {'brand': 'Baader', 'name': 'M42 Spacer 23mm', 'type': 'type_adapter', 'optical_length': 23, 'mass': 22, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_24mm': {'brand': 'Baader', 'name': 'M42 Spacer 24mm', 'type': 'type_adapter', 'optical_length': 24, 'mass': 23, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_26mm': {'brand': 'Baader', 'name': 'M42 Spacer 26mm', 'type': 'type_adapter', 'optical_length': 26, 'mass': 24, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_27mm': {'brand': 'Baader', 'name': 'M42 Spacer 27mm', 'type': 'type_adapter', 'optical_length': 27, 'mass': 25, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_29mm': {'brand': 'Baader', 'name': 'M42 Spacer 29mm', 'type': 'type_adapter', 'optical_length': 29, 'mass': 27, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_32mm': {'brand': 'Baader', 'name': 'M42 Spacer 32mm', 'type': 'type_adapter', 'optical_length': 32, 'mass': 29, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_33mm': {'brand': 'Baader', 'name': 'M42 Spacer 33mm', 'type': 'type_adapter', 'optical_length': 33, 'mass': 30, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_36mm': {'brand': 'Baader', 'name': 'M42 Spacer 36mm', 'type': 'type_adapter', 'optical_length': 36, 'mass': 32, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_37mm': {'brand': 'Baader', 'name': 'M42 Spacer 37mm', 'type': 'type_adapter', 'optical_length': 37, 'mass': 33, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_38mm': {'brand': 'Baader', 'name': 'M42 Spacer 38mm', 'type': 'type_adapter', 'optical_length': 38, 'mass': 34, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_2_1mm': {'brand': 'Baader', 'name': 'M48 Spacer 2.1mm', 'type': 'type_adapter', 'optical_length': 2.1, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_2_3mm': {'brand': 'Baader', 'name': 'M48 Spacer 2.3mm', 'type': 'type_adapter', 'optical_length': 2.3, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_2_7mm': {'brand': 'Baader', 'name': 'M48 Spacer 2.7mm', 'type': 'type_adapter', 'optical_length': 2.7, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_3_2mm': {'brand': 'Baader', 'name': 'M48 Spacer 3.2mm', 'type': 'type_adapter', 'optical_length': 3.2, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_3_3mm': {'brand': 'Baader', 'name': 'M48 Spacer 3.3mm', 'type': 'type_adapter', 'optical_length': 3.3, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_3_7mm': {'brand': 'Baader', 'name': 'M48 Spacer 3.7mm', 'type': 'type_adapter', 'optical_length': 3.7, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_4_5mm': {'brand': 'Baader', 'name': 'M48 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 9, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_5_5mm': {'brand': 'Baader', 'name': 'M48 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 10, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_6_5mm': {'brand': 'Baader', 'name': 'M48 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 11, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_8_5mm': {'brand': 'Baader', 'name': 'M48 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 12, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_9_5mm': {'brand': 'Baader', 'name': 'M48 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 13, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_13mm': {'brand': 'Baader', 'name': 'M48 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 16, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_18mm': {'brand': 'Baader', 'name': 'M48 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 20, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_19mm': {'brand': 'Baader', 'name': 'M48 Spacer 19mm', 'type': 'type_adapter', 'optical_length': 19, 'mass': 21, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_21mm': {'brand': 'Baader', 'name': 'M48 Spacer 21mm', 'type': 'type_adapter', 'optical_length': 21, 'mass': 22, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_23mm': {'brand': 'Baader', 'name': 'M48 Spacer 23mm', 'type': 'type_adapter', 'optical_length': 23, 'mass': 24, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_24mm': {'brand': 'Baader', 'name': 'M48 Spacer 24mm', 'type': 'type_adapter', 'optical_length': 24, 'mass': 25, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_26mm': {'brand': 'Baader', 'name': 'M48 Spacer 26mm', 'type': 'type_adapter', 'optical_length': 26, 'mass': 26, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_27mm': {'brand': 'Baader', 'name': 'M48 Spacer 27mm', 'type': 'type_adapter', 'optical_length': 27, 'mass': 27, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_29mm': {'brand': 'Baader', 'name': 'M48 Spacer 29mm', 'type': 'type_adapter', 'optical_length': 29, 'mass': 29, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_32mm': {'brand': 'Baader', 'name': 'M48 Spacer 32mm', 'type': 'type_adapter', 'optical_length': 32, 'mass': 31, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_33mm': {'brand': 'Baader', 'name': 'M48 Spacer 33mm', 'type': 'type_adapter', 'optical_length': 33, 'mass': 32, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_36mm': {'brand': 'Baader', 'name': 'M48 Spacer 36mm', 'type': 'type_adapter', 'optical_length': 36, 'mass': 34, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_37mm': {'brand': 'Baader', 'name': 'M48 Spacer 37mm', 'type': 'type_adapter', 'optical_length': 37, 'mass': 35, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_38mm': {'brand': 'Baader', 'name': 'M48 Spacer 38mm', 'type': 'type_adapter', 'optical_length': 38, 'mass': 36, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_2_1mm': {'brand': 'Baader', 'name': 'M54 Spacer 2.1mm', 'type': 'type_adapter', 'optical_length': 2.1, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_2_3mm': {'brand': 'Baader', 'name': 'M54 Spacer 2.3mm', 'type': 'type_adapter', 'optical_length': 2.3, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_2_7mm': {'brand': 'Baader', 'name': 'M54 Spacer 2.7mm', 'type': 'type_adapter', 'optical_length': 2.7, 'mass': 10, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_3_2mm': {'brand': 'Baader', 'name': 'M54 Spacer 3.2mm', 'type': 'type_adapter', 'optical_length': 3.2, 'mass': 10, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_3_5mm': {'brand': 'Baader', 'name': 'M54 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 10, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_4_5mm': {'brand': 'Baader', 'name': 'M54 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 11, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_5_5mm': {'brand': 'Baader', 'name': 'M54 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 12, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_6_5mm': {'brand': 'Baader', 'name': 'M54 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 13, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_7_5mm': {'brand': 'Baader', 'name': 'M54 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 14, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_8_5mm': {'brand': 'Baader', 'name': 'M54 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 14, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_13mm': {'brand': 'Baader', 'name': 'M54 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 18, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_19mm': {'brand': 'Baader', 'name': 'M54 Spacer 19mm', 'type': 'type_adapter', 'optical_length': 19, 'mass': 23, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_21mm': {'brand': 'Baader', 'name': 'M54 Spacer 21mm', 'type': 'type_adapter', 'optical_length': 21, 'mass': 24, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_23mm': {'brand': 'Baader', 'name': 'M54 Spacer 23mm', 'type': 'type_adapter', 'optical_length': 23, 'mass': 26, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_24mm': {'brand': 'Baader', 'name': 'M54 Spacer 24mm', 'type': 'type_adapter', 'optical_length': 24, 'mass': 27, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_26mm': {'brand': 'Baader', 'name': 'M54 Spacer 26mm', 'type': 'type_adapter', 'optical_length': 26, 'mass': 28, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_27mm': {'brand': 'Baader', 'name': 'M54 Spacer 27mm', 'type': 'type_adapter', 'optical_length': 27, 'mass': 29, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_29mm': {'brand': 'Baader', 'name': 'M54 Spacer 29mm', 'type': 'type_adapter', 'optical_length': 29, 'mass': 31, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_2_1mm': {'brand': 'Baader', 'name': 'M68 Spacer 2.1mm', 'type': 'type_adapter', 'optical_length': 2.1, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_2_3mm': {'brand': 'Baader', 'name': 'M68 Spacer 2.3mm', 'type': 'type_adapter', 'optical_length': 2.3, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_2_7mm': {'brand': 'Baader', 'name': 'M68 Spacer 2.7mm', 'type': 'type_adapter', 'optical_length': 2.7, 'mass': 12, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_3_5mm': {'brand': 'Baader', 'name': 'M68 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 12, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_4_5mm': {'brand': 'Baader', 'name': 'M68 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 13, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_5_5mm': {'brand': 'Baader', 'name': 'M68 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 14, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_6_5mm': {'brand': 'Baader', 'name': 'M68 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 15, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_7_5mm': {'brand': 'Baader', 'name': 'M68 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 16, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_8_5mm': {'brand': 'Baader', 'name': 'M68 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 16, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_9_5mm': {'brand': 'Baader', 'name': 'M68 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 17, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_13mm': {'brand': 'Baader', 'name': 'M68 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 20, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_16mm': {'brand': 'Baader', 'name': 'M68 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 22, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_18mm': {'brand': 'Baader', 'name': 'M68 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 24, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_19mm': {'brand': 'Baader', 'name': 'M68 Spacer 19mm', 'type': 'type_adapter', 'optical_length': 19, 'mass': 25, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_21mm': {'brand': 'Baader', 'name': 'M68 Spacer 21mm', 'type': 'type_adapter', 'optical_length': 21, 'mass': 26, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_23mm': {'brand': 'Baader', 'name': 'M68 Spacer 23mm', 'type': 'type_adapter', 'optical_length': 23, 'mass': 28, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_24mm': {'brand': 'Baader', 'name': 'M68 Spacer 24mm', 'type': 'type_adapter', 'optical_length': 24, 'mass': 29, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_26mm': {'brand': 'Baader', 'name': 'M68 Spacer 26mm', 'type': 'type_adapter', 'optical_length': 26, 'mass': 30, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_27mm': {'brand': 'Baader', 'name': 'M68 Spacer 27mm', 'type': 'type_adapter', 'optical_length': 27, 'mass': 31, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M72_Spacer_2_5mm': {'brand': 'Baader', 'name': 'M72 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 14, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M72_Spacer_3_5mm': {'brand': 'Baader', 'name': 'M72 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 14, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M72_Spacer_4mm': {'brand': 'Baader', 'name': 'M72 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 15, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M72_Spacer_4_5mm': {'brand': 'Baader', 'name': 'M72 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 15, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M72_Spacer_5_5mm': {'brand': 'Baader', 'name': 'M72 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 16, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M72_Spacer_6mm': {'brand': 'Baader', 'name': 'M72 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 16, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M72_Spacer_6_5mm': {'brand': 'Baader', 'name': 'M72 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 17, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M72_Spacer_7mm': {'brand': 'Baader', 'name': 'M72 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 17, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M72_Spacer_7_5mm': {'brand': 'Baader', 'name': 'M72 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 18, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M72_Spacer_8mm': {'brand': 'Baader', 'name': 'M72 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 18, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M72_Spacer_8_5mm': {'brand': 'Baader', 'name': 'M72 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 18, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M72_Spacer_9mm': {'brand': 'Baader', 'name': 'M72 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 19, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M72_Spacer_9_5mm': {'brand': 'Baader', 'name': 'M72 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 19, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M72_Spacer_11mm': {'brand': 'Baader', 'name': 'M72 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 20, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M72_Spacer_12mm': {'brand': 'Baader', 'name': 'M72 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 21, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M72_Spacer_13mm': {'brand': 'Baader', 'name': 'M72 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 22, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M72_Spacer_14mm': {'brand': 'Baader', 'name': 'M72 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 23, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M72_Spacer_16mm': {'brand': 'Baader', 'name': 'M72 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 24, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M72_Spacer_17mm': {'brand': 'Baader', 'name': 'M72 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 25, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M72_Spacer_18mm': {'brand': 'Baader', 'name': 'M72 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 26, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M72_Spacer_22mm': {'brand': 'Baader', 'name': 'M72 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 29, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M72_Spacer_25mm': {'brand': 'Baader', 'name': 'M72 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 32, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M72_Spacer_28mm': {'brand': 'Baader', 'name': 'M72 Spacer 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 34, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M72_Spacer_30mm': {'brand': 'Baader', 'name': 'M72 Spacer 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 36, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M82_Spacer_2_5mm': {'brand': 'Baader', 'name': 'M82 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 17, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M82_Spacer_3mm': {'brand': 'Baader', 'name': 'M82 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 17, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M82_Spacer_3_5mm': {'brand': 'Baader', 'name': 'M82 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 17, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M82_Spacer_4mm': {'brand': 'Baader', 'name': 'M82 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 18, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M82_Spacer_4_5mm': {'brand': 'Baader', 'name': 'M82 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 18, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M82_Spacer_5_5mm': {'brand': 'Baader', 'name': 'M82 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 19, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M82_Spacer_6mm': {'brand': 'Baader', 'name': 'M82 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 19, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M82_Spacer_6_5mm': {'brand': 'Baader', 'name': 'M82 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 20, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M82_Spacer_7mm': {'brand': 'Baader', 'name': 'M82 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 20, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M82_Spacer_7_5mm': {'brand': 'Baader', 'name': 'M82 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 21, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M82_Spacer_8mm': {'brand': 'Baader', 'name': 'M82 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 21, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M82_Spacer_8_5mm': {'brand': 'Baader', 'name': 'M82 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 21, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M82_Spacer_9mm': {'brand': 'Baader', 'name': 'M82 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 22, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M82_Spacer_9_5mm': {'brand': 'Baader', 'name': 'M82 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 22, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M82_Spacer_11mm': {'brand': 'Baader', 'name': 'M82 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 23, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M82_Spacer_12mm': {'brand': 'Baader', 'name': 'M82 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 24, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M82_Spacer_13mm': {'brand': 'Baader', 'name': 'M82 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 25, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M82_Spacer_14mm': {'brand': 'Baader', 'name': 'M82 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 26, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M82_Spacer_16mm': {'brand': 'Baader', 'name': 'M82 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 27, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M82_Spacer_17mm': {'brand': 'Baader', 'name': 'M82 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 28, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M82_Spacer_18mm': {'brand': 'Baader', 'name': 'M82 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 29, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M82_Spacer_22mm': {'brand': 'Baader', 'name': 'M82 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 32, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M82_Spacer_25mm': {'brand': 'Baader', 'name': 'M82 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 35, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M82_Spacer_28mm': {'brand': 'Baader', 'name': 'M82 Spacer 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 37, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M82_Spacer_30mm': {'brand': 'Baader', 'name': 'M82 Spacer 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 39, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M92_Spacer_2_5mm': {'brand': 'Baader', 'name': 'M92 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 20, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M92_Spacer_3mm': {'brand': 'Baader', 'name': 'M92 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 20, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M92_Spacer_3_5mm': {'brand': 'Baader', 'name': 'M92 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 20, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M92_Spacer_4mm': {'brand': 'Baader', 'name': 'M92 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 21, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M92_Spacer_4_5mm': {'brand': 'Baader', 'name': 'M92 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 21, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M92_Spacer_6mm': {'brand': 'Baader', 'name': 'M92 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 22, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M92_Spacer_6_5mm': {'brand': 'Baader', 'name': 'M92 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 23, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M92_Spacer_7mm': {'brand': 'Baader', 'name': 'M92 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 23, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M92_Spacer_7_5mm': {'brand': 'Baader', 'name': 'M92 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 24, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M92_Spacer_8mm': {'brand': 'Baader', 'name': 'M92 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 24, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M92_Spacer_8_5mm': {'brand': 'Baader', 'name': 'M92 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 24, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M92_Spacer_9mm': {'brand': 'Baader', 'name': 'M92 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 25, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M92_Spacer_9_5mm': {'brand': 'Baader', 'name': 'M92 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 25, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M92_Spacer_11mm': {'brand': 'Baader', 'name': 'M92 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 26, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M92_Spacer_12mm': {'brand': 'Baader', 'name': 'M92 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 27, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M92_Spacer_13mm': {'brand': 'Baader', 'name': 'M92 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 28, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M92_Spacer_14mm': {'brand': 'Baader', 'name': 'M92 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 29, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M92_Spacer_16mm': {'brand': 'Baader', 'name': 'M92 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 30, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M92_Spacer_17mm': {'brand': 'Baader', 'name': 'M92 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 31, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M92_Spacer_18mm': {'brand': 'Baader', 'name': 'M92 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 32, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M92_Spacer_22mm': {'brand': 'Baader', 'name': 'M92 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 35, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M92_Spacer_25mm': {'brand': 'Baader', 'name': 'M92 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 38, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M92_Spacer_28mm': {'brand': 'Baader', 'name': 'M92 Spacer 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 40, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M92_Spacer_30mm': {'brand': 'Baader', 'name': 'M92 Spacer 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 42, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Extension_Tube_3mm': {'brand': 'Baader', 'name': 'M42 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 15, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M42_Extension_Tube_6mm': {'brand': 'Baader', 'name': 'M42 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M42_Extension_Tube_9mm': {'brand': 'Baader', 'name': 'M42 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 17, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M42_Extension_Tube_11mm': {'brand': 'Baader', 'name': 'M42 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 18, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M42_Extension_Tube_13mm': {'brand': 'Baader', 'name': 'M42 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 18, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M42_Extension_Tube_16mm': {'brand': 'Baader', 'name': 'M42 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 19, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M42_Extension_Tube_22mm': {'brand': 'Baader', 'name': 'M42 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 21, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M42_Extension_Tube_28mm': {'brand': 'Baader', 'name': 'M42 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 23, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M42_Extension_Tube_35mm': {'brand': 'Baader', 'name': 'M42 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 25, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M42_Extension_Tube_45mm': {'brand': 'Baader', 'name': 'M42 Extension Tube 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 28, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M48_Extension_Tube_3mm': {'brand': 'Baader', 'name': 'M48 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 19, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M48_Extension_Tube_6mm': {'brand': 'Baader', 'name': 'M48 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 20, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M48_Extension_Tube_9mm': {'brand': 'Baader', 'name': 'M48 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 21, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M48_Extension_Tube_11mm': {'brand': 'Baader', 'name': 'M48 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 22, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M48_Extension_Tube_13mm': {'brand': 'Baader', 'name': 'M48 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 22, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M48_Extension_Tube_16mm': {'brand': 'Baader', 'name': 'M48 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 23, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M48_Extension_Tube_22mm': {'brand': 'Baader', 'name': 'M48 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 25, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M48_Extension_Tube_28mm': {'brand': 'Baader', 'name': 'M48 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 27, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M48_Extension_Tube_35mm': {'brand': 'Baader', 'name': 'M48 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 29, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M48_Extension_Tube_45mm': {'brand': 'Baader', 'name': 'M48 Extension Tube 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 32, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M54_Extension_Tube_3mm': {'brand': 'Baader', 'name': 'M54 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 23, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M54_Extension_Tube_6mm': {'brand': 'Baader', 'name': 'M54 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 24, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M54_Extension_Tube_9mm': {'brand': 'Baader', 'name': 'M54 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 25, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M54_Extension_Tube_11mm': {'brand': 'Baader', 'name': 'M54 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 26, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M54_Extension_Tube_13mm': {'brand': 'Baader', 'name': 'M54 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 26, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M54_Extension_Tube_16mm': {'brand': 'Baader', 'name': 'M54 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 27, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M54_Extension_Tube_22mm': {'brand': 'Baader', 'name': 'M54 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 29, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M54_Extension_Tube_28mm': {'brand': 'Baader', 'name': 'M54 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 31, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M54_Extension_Tube_35mm': {'brand': 'Baader', 'name': 'M54 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 33, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M54_Extension_Tube_45mm': {'brand': 'Baader', 'name': 'M54 Extension Tube 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 36, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M68_Extension_Tube_3mm': {'brand': 'Baader', 'name': 'M68 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 18, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M68_Extension_Tube_5mm': {'brand': 'Baader', 'name': 'M68 Extension Tube 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 19, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M68_Extension_Tube_6mm': {'brand': 'Baader', 'name': 'M68 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 19, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M68_Extension_Tube_8mm': {'brand': 'Baader', 'name': 'M68 Extension Tube 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 20, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M68_Extension_Tube_9mm': {'brand': 'Baader', 'name': 'M68 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 20, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M68_Extension_Tube_11mm': {'brand': 'Baader', 'name': 'M68 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 21, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M68_Extension_Tube_13mm': {'brand': 'Baader', 'name': 'M68 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 21, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M68_Extension_Tube_14mm': {'brand': 'Baader', 'name': 'M68 Extension Tube 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 22, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M68_Extension_Tube_16mm': {'brand': 'Baader', 'name': 'M68 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 22, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M68_Extension_Tube_18mm': {'brand': 'Baader', 'name': 'M68 Extension Tube 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 23, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M68_Extension_Tube_22mm': {'brand': 'Baader', 'name': 'M68 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 24, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M68_Extension_Tube_25mm': {'brand': 'Baader', 'name': 'M68 Extension Tube 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 25, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M68_Extension_Tube_28mm': {'brand': 'Baader', 'name': 'M68 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 26, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M68_Extension_Tube_30mm': {'brand': 'Baader', 'name': 'M68 Extension Tube 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 27, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M68_Extension_Tube_35mm': {'brand': 'Baader', 'name': 'M68 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 28, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M72_Extension_Tube_3mm': {'brand': 'Baader', 'name': 'M72 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 20, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M72_Extension_Tube_5mm': {'brand': 'Baader', 'name': 'M72 Extension Tube 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 21, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M72_Extension_Tube_8mm': {'brand': 'Baader', 'name': 'M72 Extension Tube 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 22, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M72_Extension_Tube_10mm': {'brand': 'Baader', 'name': 'M72 Extension Tube 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 23, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M72_Extension_Tube_12mm': {'brand': 'Baader', 'name': 'M72 Extension Tube 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 23, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M72_Extension_Tube_15mm': {'brand': 'Baader', 'name': 'M72 Extension Tube 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 24, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M72_Extension_Tube_18mm': {'brand': 'Baader', 'name': 'M72 Extension Tube 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 25, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M72_Extension_Tube_20mm': {'brand': 'Baader', 'name': 'M72 Extension Tube 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 26, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M72_Extension_Tube_25mm': {'brand': 'Baader', 'name': 'M72 Extension Tube 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 27, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M72_Extension_Tube_30mm': {'brand': 'Baader', 'name': 'M72 Extension Tube 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 29, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M82_Extension_Tube_3mm': {'brand': 'Baader', 'name': 'M82 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 22, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M82_Extension_Tube_5mm': {'brand': 'Baader', 'name': 'M82 Extension Tube 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 23, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M82_Extension_Tube_8mm': {'brand': 'Baader', 'name': 'M82 Extension Tube 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 24, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M82_Extension_Tube_10mm': {'brand': 'Baader', 'name': 'M82 Extension Tube 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 25, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M82_Extension_Tube_12mm': {'brand': 'Baader', 'name': 'M82 Extension Tube 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 25, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M82_Extension_Tube_15mm': {'brand': 'Baader', 'name': 'M82 Extension Tube 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 26, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M82_Extension_Tube_18mm': {'brand': 'Baader', 'name': 'M82 Extension Tube 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 27, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M82_Extension_Tube_20mm': {'brand': 'Baader', 'name': 'M82 Extension Tube 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 28, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M82_Extension_Tube_25mm': {'brand': 'Baader', 'name': 'M82 Extension Tube 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 29, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_M82_Extension_Tube_30mm': {'brand': 'Baader', 'name': 'M82 Extension Tube 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 31, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_SC_Extension_Tube_5mm': {'brand': 'Baader', 'name': 'SC Extension Tube 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 25, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_SC_Extension_Tube_10mm': {'brand': 'Baader', 'name': 'SC Extension Tube 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 27, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_SC_Extension_Tube_15mm': {'brand': 'Baader', 'name': 'SC Extension Tube 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 28, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_SC_Extension_Tube_20mm': {'brand': 'Baader', 'name': 'SC Extension Tube 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 30, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_SC_Extension_Tube_25mm': {'brand': 'Baader', 'name': 'SC Extension Tube 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 31, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_SC_Extension_Tube_30mm': {'brand': 'Baader', 'name': 'SC Extension Tube 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 33, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_SC_Extension_Tube_35mm': {'brand': 'Baader', 'name': 'SC Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 34, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_SC_Extension_Tube_40mm': {'brand': 'Baader', 'name': 'SC Extension Tube 40mm', 'type': 'type_adapter', 'optical_length': 40, 'mass': 36, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_SC_Extension_Tube_50mm': {'brand': 'Baader', 'name': 'SC Extension Tube 50mm', 'type': 'type_adapter', 'optical_length': 50, 'mass': 39, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_SC_Extension_Tube_60mm': {'brand': 'Baader', 'name': 'SC Extension Tube 60mm', 'type': 'type_adapter', 'optical_length': 60, 'mass': 42, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_SC_Extension_Tube_75mm': {'brand': 'Baader', 'name': 'SC Extension Tube 75mm', 'type': 'type_adapter', 'optical_length': 75, 'mass': 46, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Baader_SC_Schmidt_Cassegrain_Spacer_2_5mm': {'brand': 'Baader', 'name': 'SC (Schmidt-Cassegrain) Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 22, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_SC_Schmidt_Cassegrain_Spacer_3mm': {'brand': 'Baader', 'name': 'SC (Schmidt-Cassegrain) Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 22, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_SC_Schmidt_Cassegrain_Spacer_3_5mm': {'brand': 'Baader', 'name': 'SC (Schmidt-Cassegrain) Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 22, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_SC_Schmidt_Cassegrain_Spacer_4_5mm': {'brand': 'Baader', 'name': 'SC (Schmidt-Cassegrain) Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 23, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_SC_Schmidt_Cassegrain_Spacer_5_5mm': {'brand': 'Baader', 'name': 'SC (Schmidt-Cassegrain) Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 24, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_SC_Schmidt_Cassegrain_Spacer_6mm': {'brand': 'Baader', 'name': 'SC (Schmidt-Cassegrain) Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 24, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_SC_Schmidt_Cassegrain_Spacer_6_5mm': {'brand': 'Baader', 'name': 'SC (Schmidt-Cassegrain) Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 25, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_SC_Schmidt_Cassegrain_Spacer_7_5mm': {'brand': 'Baader', 'name': 'SC (Schmidt-Cassegrain) Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 26, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_SC_Schmidt_Cassegrain_Spacer_8_5mm': {'brand': 'Baader', 'name': 'SC (Schmidt-Cassegrain) Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 26, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_SC_Schmidt_Cassegrain_Spacer_9_5mm': {'brand': 'Baader', 'name': 'SC (Schmidt-Cassegrain) Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 27, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_SC_Schmidt_Cassegrain_Spacer_11mm': {'brand': 'Baader', 'name': 'SC (Schmidt-Cassegrain) Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 28, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_SC_Schmidt_Cassegrain_Spacer_12mm': {'brand': 'Baader', 'name': 'SC (Schmidt-Cassegrain) Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 29, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_SC_Schmidt_Cassegrain_Spacer_13mm': {'brand': 'Baader', 'name': 'SC (Schmidt-Cassegrain) Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 30, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_SC_Schmidt_Cassegrain_Spacer_14mm': {'brand': 'Baader', 'name': 'SC (Schmidt-Cassegrain) Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 31, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_SC_Schmidt_Cassegrain_Spacer_16mm': {'brand': 'Baader', 'name': 'SC (Schmidt-Cassegrain) Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 32, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_SC_Schmidt_Cassegrain_Spacer_17mm': {'brand': 'Baader', 'name': 'SC (Schmidt-Cassegrain) Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 33, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_SC_Schmidt_Cassegrain_Spacer_18mm': {'brand': 'Baader', 'name': 'SC (Schmidt-Cassegrain) Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 34, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_SC_Schmidt_Cassegrain_Spacer_19mm': {'brand': 'Baader', 'name': 'SC (Schmidt-Cassegrain) Spacer 19mm', 'type': 'type_adapter', 'optical_length': 19, 'mass': 35, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_SC_Schmidt_Cassegrain_Spacer_21mm': {'brand': 'Baader', 'name': 'SC (Schmidt-Cassegrain) Spacer 21mm', 'type': 'type_adapter', 'optical_length': 21, 'mass': 36, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_SC_Schmidt_Cassegrain_Spacer_22mm': {'brand': 'Baader', 'name': 'SC (Schmidt-Cassegrain) Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 37, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_SC_Schmidt_Cassegrain_Spacer_23mm': {'brand': 'Baader', 'name': 'SC (Schmidt-Cassegrain) Spacer 23mm', 'type': 'type_adapter', 'optical_length': 23, 'mass': 38, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_SC_Schmidt_Cassegrain_Spacer_28mm': {'brand': 'Baader', 'name': 'SC (Schmidt-Cassegrain) Spacer 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 42, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_SC_Schmidt_Cassegrain_Spacer_32mm': {'brand': 'Baader', 'name': 'SC (Schmidt-Cassegrain) Spacer 32mm', 'type': 'type_adapter', 'optical_length': 32, 'mass': 45, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_SC_Schmidt_Cassegrain_Spacer_35mm': {'brand': 'Baader', 'name': 'SC (Schmidt-Cassegrain) Spacer 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 48, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M92_Spacer_5_5mm': {'brand': 'Baader', 'name': 'M92 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 22, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_1_25_Spacer_2_5mm': {'brand': 'Baader', 'name': '1.25" Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 5, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_1_25_Spacer_3mm': {'brand': 'Baader', 'name': '1.25" Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 5, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_1_25_Spacer_3_5mm': {'brand': 'Baader', 'name': '1.25" Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 5, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_1_25_Spacer_4mm': {'brand': 'Baader', 'name': '1.25" Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 6, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_1_25_Spacer_5mm': {'brand': 'Baader', 'name': '1.25" Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 7, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_1_25_Spacer_6mm': {'brand': 'Baader', 'name': '1.25" Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 7, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_1_25_Spacer_7mm': {'brand': 'Baader', 'name': '1.25" Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 8, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_1_25_Spacer_8mm': {'brand': 'Baader', 'name': '1.25" Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 9, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_1_25_Spacer_9mm': {'brand': 'Baader', 'name': '1.25" Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 10, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_1_25_Spacer_10mm': {'brand': 'Baader', 'name': '1.25" Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 11, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_1_25_Spacer_12mm': {'brand': 'Baader', 'name': '1.25" Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 12, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_1_25_Spacer_15mm': {'brand': 'Baader', 'name': '1.25" Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 15, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_1_25_Spacer_18mm': {'brand': 'Baader', 'name': '1.25" Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 17, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_1_25_Spacer_20mm': {'brand': 'Baader', 'name': '1.25" Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 19, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_1_25_Spacer_25mm': {'brand': 'Baader', 'name': '1.25" Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 23, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_2_Spacer_2_5mm': {'brand': 'Baader', 'name': '2" Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 10, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_2_Spacer_3mm': {'brand': 'Baader', 'name': '2" Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 10, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_2_Spacer_3_5mm': {'brand': 'Baader', 'name': '2" Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 10, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_2_Spacer_4mm': {'brand': 'Baader', 'name': '2" Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 11, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_2_Spacer_5mm': {'brand': 'Baader', 'name': '2" Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 12, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_2_Spacer_6mm': {'brand': 'Baader', 'name': '2" Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 12, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_2_Spacer_7mm': {'brand': 'Baader', 'name': '2" Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 13, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_2_Spacer_8mm': {'brand': 'Baader', 'name': '2" Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 14, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_2_Spacer_9mm': {'brand': 'Baader', 'name': '2" Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 15, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_2_Spacer_10mm': {'brand': 'Baader', 'name': '2" Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 16, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_2_Spacer_12mm': {'brand': 'Baader', 'name': '2" Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 17, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_2_Spacer_15mm': {'brand': 'Baader', 'name': '2" Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 20, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_2_Spacer_18mm': {'brand': 'Baader', 'name': '2" Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 22, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_2_Spacer_20mm': {'brand': 'Baader', 'name': '2" Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 24, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_2_Spacer_25mm': {'brand': 'Baader', 'name': '2" Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 28, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M84_Spacer_3mm': {'brand': 'Baader', 'name': 'M84 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 16, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M84_Spacer_4mm': {'brand': 'Baader', 'name': 'M84 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 17, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M84_Spacer_5_5mm': {'brand': 'Baader', 'name': 'M84 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 18, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M84_Spacer_6mm': {'brand': 'Baader', 'name': 'M84 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 18, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M84_Spacer_6_5mm': {'brand': 'Baader', 'name': 'M84 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 19, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M84_Spacer_7mm': {'brand': 'Baader', 'name': 'M84 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 19, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M84_Spacer_7_5mm': {'brand': 'Baader', 'name': 'M84 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 20, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M84_Spacer_8mm': {'brand': 'Baader', 'name': 'M84 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 20, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M84_Spacer_8_5mm': {'brand': 'Baader', 'name': 'M84 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 20, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M84_Spacer_9mm': {'brand': 'Baader', 'name': 'M84 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 21, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M84_Spacer_9_5mm': {'brand': 'Baader', 'name': 'M84 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 21, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M84_Spacer_11mm': {'brand': 'Baader', 'name': 'M84 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 22, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M84_Spacer_13mm': {'brand': 'Baader', 'name': 'M84 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 24, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M84_Spacer_16mm': {'brand': 'Baader', 'name': 'M84 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 26, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M84_Spacer_18mm': {'brand': 'Baader', 'name': 'M84 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 28, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M84_Spacer_22mm': {'brand': 'Baader', 'name': 'M84 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 31, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M84_Spacer_25mm': {'brand': 'Baader', 'name': 'M84 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 34, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}}

    @classmethod
    def Baader_M42_M48_Adapter_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_M48_Adapter_0_5mm'])

    @classmethod
    def Baader_M48_M42_Adapter_16_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_M42_Adapter_16_5mm'])

    @classmethod
    def Baader_M48_M54_Adapter_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_M54_Adapter_7_5mm'])

    @classmethod
    def Baader_M54_M48_Adapter_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_M48_Adapter_7_5mm'])

    @classmethod
    def Baader_M54_M68_Adapter_1_4mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_M68_Adapter_1_4mm'])

    @classmethod
    def Baader_M54_M68_Adapter_10_4mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_M68_Adapter_10_4mm'])

    @classmethod
    def Baader_M68_M54_Adapter_1_4mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_M54_Adapter_1_4mm'])

    @classmethod
    def Baader_M68_M72_Adapter_10mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_M72_Adapter_10mm'])

    @classmethod
    def Baader_M68_M72_Adapter_35mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_M72_Adapter_35mm'])

    @classmethod
    def Baader_M81_M68_Adapter(cls):
        return cls.from_database(cls._DATABASE['Baader_M81_M68_Adapter'])

    @classmethod
    def Baader_SC_M42_Adapter_50mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_M42_Adapter_50mm'])

    @classmethod
    def Baader_SC_M48_Adapter_2mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_M48_Adapter_2mm'])

    @classmethod
    def Baader_SC_M48_Adapter_20mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_M48_Adapter_20mm'])

    @classmethod
    def Baader_SC_M54_Adapter(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_M54_Adapter'])

    @classmethod
    def Baader_SC_M68_Adapter_15mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_M68_Adapter_15mm'])

    @classmethod
    def Baader_SC_M72_Adapter_20mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_M72_Adapter_20mm'])

    @classmethod
    def Baader_EOS_M48_Adapter_8mm(cls):
        return cls.from_database(cls._DATABASE['Baader_EOS_M48_Adapter_8mm'])

    @classmethod
    def Baader_EOS_M54_Adapter_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_EOS_M54_Adapter_9_5mm'])

    @classmethod
    def Baader_T2_Ring_Canon_EOS_10_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_T2_Ring_Canon_EOS_10_5mm'])

    @classmethod
    def Baader_T2_Ring_Nikon_F_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_T2_Ring_Nikon_F_8_5mm'])

    @classmethod
    def Baader_T2_Ring_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Baader_T2_Ring_Sony_E'])

    @classmethod
    def Baader_M56_M54_Adapter(cls):
        return cls.from_database(cls._DATABASE['Baader_M56_M54_Adapter'])

    @classmethod
    def Baader_M63_M68_Adapter(cls):
        return cls.from_database(cls._DATABASE['Baader_M63_M68_Adapter'])

    @classmethod
    def Baader_M82_M68_Adapter(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_M68_Adapter'])

    @classmethod
    def Baader_M92_M82_Adapter(cls):
        return cls.from_database(cls._DATABASE['Baader_M92_M82_Adapter'])

    @classmethod
    def Baader_M68_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_M42_Adapter'])

    @classmethod
    def Baader_M54_M42_Adapter_11mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_M42_Adapter_11mm'])

    @classmethod
    def Baader_M42_Coupling_Ring_F_F(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Coupling_Ring_F_F'])

    @classmethod
    def Baader_M48_Coupling_Ring_F_F(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Coupling_Ring_F_F'])

    @classmethod
    def Baader_M54_Coupling_Ring_F_F(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Coupling_Ring_F_F'])

    @classmethod
    def Baader_M68_Coupling_Ring_F_F(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Coupling_Ring_F_F'])

    @classmethod
    def Baader_2_M48_Adapter(cls):
        return cls.from_database(cls._DATABASE['Baader_2_M48_Adapter'])

    @classmethod
    def Baader_2_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['Baader_2_M42_Adapter'])

    @classmethod
    def Baader_1_25_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['Baader_1_25_M42_Adapter'])

    @classmethod
    def Baader_Nikon_M48_Adapter(cls):
        return cls.from_database(cls._DATABASE['Baader_Nikon_M48_Adapter'])

    @classmethod
    def Baader_ClickLock_M42_Clamp(cls):
        return cls.from_database(cls._DATABASE['Baader_ClickLock_M42_Clamp'])

    @classmethod
    def Baader_ClickLock_M48_Clamp(cls):
        return cls.from_database(cls._DATABASE['Baader_ClickLock_M48_Clamp'])

    @classmethod
    def Baader_ClickLock_M54_Clamp(cls):
        return cls.from_database(cls._DATABASE['Baader_ClickLock_M54_Clamp'])

    @classmethod
    def Baader_ClickLock_M68_Clamp(cls):
        return cls.from_database(cls._DATABASE['Baader_ClickLock_M68_Clamp'])

    @classmethod
    def Baader_ClickLock_SC_Clamp(cls):
        return cls.from_database(cls._DATABASE['Baader_ClickLock_SC_Clamp'])

    @classmethod
    def Baader_ClickLock_2_Clamp_M48(cls):
        return cls.from_database(cls._DATABASE['Baader_ClickLock_2_Clamp_M48'])

    @classmethod
    def Baader_M42_M68_Adapter(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_M68_Adapter'])

    @classmethod
    def Baader_M48_M68_Adapter(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_M68_Adapter'])

    @classmethod
    def Baader_M72_M82_Adapter(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_M82_Adapter'])

    @classmethod
    def Baader_Canon_RF_M48_Adapter(cls):
        return cls.from_database(cls._DATABASE['Baader_Canon_RF_M48_Adapter'])

    @classmethod
    def Baader_Nikon_Z_M48_Adapter(cls):
        return cls.from_database(cls._DATABASE['Baader_Nikon_Z_M48_Adapter'])

    @classmethod
    def Baader_Sony_E_M48_Adapter(cls):
        return cls.from_database(cls._DATABASE['Baader_Sony_E_M48_Adapter'])

    @classmethod
    def Baader_M42_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_3mm'])

    @classmethod
    def Baader_M42_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_5mm'])

    @classmethod
    def Baader_M42_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_7mm'])

    @classmethod
    def Baader_M42_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_7_5mm'])

    @classmethod
    def Baader_M42_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_10mm'])

    @classmethod
    def Baader_M42_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_11mm'])

    @classmethod
    def Baader_M42_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_15mm'])

    @classmethod
    def Baader_M42_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_20mm'])

    @classmethod
    def Baader_M42_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_25mm'])

    @classmethod
    def Baader_M42_Spacer_30mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_30mm'])

    @classmethod
    def Baader_M42_Spacer_40mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_40mm'])

    @classmethod
    def Baader_M48_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_3mm'])

    @classmethod
    def Baader_M48_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_5mm'])

    @classmethod
    def Baader_M48_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_7mm'])

    @classmethod
    def Baader_M48_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_10mm'])

    @classmethod
    def Baader_M48_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_15mm'])

    @classmethod
    def Baader_M48_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_16mm'])

    @classmethod
    def Baader_M48_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_20mm'])

    @classmethod
    def Baader_M48_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_25mm'])

    @classmethod
    def Baader_M48_Spacer_30mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_30mm'])

    @classmethod
    def Baader_M48_Spacer_40mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_40mm'])

    @classmethod
    def Baader_M54_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_5mm'])

    @classmethod
    def Baader_M54_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_9mm'])

    @classmethod
    def Baader_M54_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_10mm'])

    @classmethod
    def Baader_M54_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_15mm'])

    @classmethod
    def Baader_M54_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_16mm'])

    @classmethod
    def Baader_M54_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_20mm'])

    @classmethod
    def Baader_M68_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_3mm'])

    @classmethod
    def Baader_M68_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_5mm'])

    @classmethod
    def Baader_M68_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_7mm'])

    @classmethod
    def Baader_M68_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_10mm'])

    @classmethod
    def Baader_M68_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_15mm'])

    @classmethod
    def Baader_M68_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_20mm'])

    @classmethod
    def Baader_M68_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_25mm'])

    @classmethod
    def Baader_M68_Spacer_30mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_30mm'])

    @classmethod
    def Baader_M68_Spacer_32mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_32mm'])

    @classmethod
    def Baader_M72_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Spacer_3mm'])

    @classmethod
    def Baader_M72_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Spacer_5mm'])

    @classmethod
    def Baader_M72_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Spacer_10mm'])

    @classmethod
    def Baader_M72_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Spacer_15mm'])

    @classmethod
    def Baader_M72_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Spacer_20mm'])

    @classmethod
    def Baader_M82_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Spacer_5mm'])

    @classmethod
    def Baader_M82_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Spacer_10mm'])

    @classmethod
    def Baader_M82_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Spacer_15mm'])

    @classmethod
    def Baader_M82_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Spacer_20mm'])

    @classmethod
    def Baader_M92_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M92_Spacer_5mm'])

    @classmethod
    def Baader_M92_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M92_Spacer_10mm'])

    @classmethod
    def Baader_M92_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M92_Spacer_15mm'])

    @classmethod
    def Baader_M92_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M92_Spacer_20mm'])

    @classmethod
    def Baader_M42_M_M_Coupling(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_M_M_Coupling'])

    @classmethod
    def Baader_M48_M_M_Coupling(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_M_M_Coupling'])

    @classmethod
    def Baader_M54_M_M_Coupling(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_M_M_Coupling'])

    @classmethod
    def Baader_M68_M_M_Coupling(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_M_M_Coupling'])

    @classmethod
    def Baader_SC_Schmidt_Cassegrain_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Schmidt_Cassegrain_Spacer_5mm'])

    @classmethod
    def Baader_SC_Schmidt_Cassegrain_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Schmidt_Cassegrain_Spacer_10mm'])

    @classmethod
    def Baader_SC_Schmidt_Cassegrain_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Schmidt_Cassegrain_Spacer_15mm'])

    @classmethod
    def Baader_SC_Schmidt_Cassegrain_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Schmidt_Cassegrain_Spacer_20mm'])

    @classmethod
    def Baader_SC_Schmidt_Cassegrain_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Schmidt_Cassegrain_Spacer_25mm'])

    @classmethod
    def Baader_SC_Schmidt_Cassegrain_Spacer_30mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Schmidt_Cassegrain_Spacer_30mm'])

    @classmethod
    def Baader_SC_Schmidt_Cassegrain_Spacer_40mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Schmidt_Cassegrain_Spacer_40mm'])

    @classmethod
    def Baader_M42_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_4mm'])

    @classmethod
    def Baader_M42_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_6mm'])

    @classmethod
    def Baader_M42_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_8mm'])

    @classmethod
    def Baader_M42_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_12mm'])

    @classmethod
    def Baader_M42_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_14mm'])

    @classmethod
    def Baader_M42_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_17mm'])

    @classmethod
    def Baader_M42_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_22mm'])

    @classmethod
    def Baader_M42_Spacer_28mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_28mm'])

    @classmethod
    def Baader_M42_Spacer_35mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_35mm'])

    @classmethod
    def Baader_M48_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_4mm'])

    @classmethod
    def Baader_M48_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_6mm'])

    @classmethod
    def Baader_M48_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_8mm'])

    @classmethod
    def Baader_M48_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_9mm'])

    @classmethod
    def Baader_M48_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_11mm'])

    @classmethod
    def Baader_M48_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_12mm'])

    @classmethod
    def Baader_M48_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_14mm'])

    @classmethod
    def Baader_M48_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_17mm'])

    @classmethod
    def Baader_M48_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_22mm'])

    @classmethod
    def Baader_M48_Spacer_28mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_28mm'])

    @classmethod
    def Baader_M48_Spacer_35mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_35mm'])

    @classmethod
    def Baader_M54_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_3mm'])

    @classmethod
    def Baader_M54_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_4mm'])

    @classmethod
    def Baader_M54_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_7mm'])

    @classmethod
    def Baader_M54_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_8mm'])

    @classmethod
    def Baader_M54_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_11mm'])

    @classmethod
    def Baader_M54_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_12mm'])

    @classmethod
    def Baader_M54_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_14mm'])

    @classmethod
    def Baader_M54_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_18mm'])

    @classmethod
    def Baader_M54_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_22mm'])

    @classmethod
    def Baader_M54_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_25mm'])

    @classmethod
    def Baader_M68_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_4mm'])

    @classmethod
    def Baader_M68_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_6mm'])

    @classmethod
    def Baader_M68_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_8mm'])

    @classmethod
    def Baader_M68_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_9mm'])

    @classmethod
    def Baader_M68_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_11mm'])

    @classmethod
    def Baader_M68_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_12mm'])

    @classmethod
    def Baader_M68_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_14mm'])

    @classmethod
    def Baader_M68_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_17mm'])

    @classmethod
    def Baader_M68_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_22mm'])

    @classmethod
    def Baader_M68_Spacer_28mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_28mm'])

    @classmethod
    def Baader_M68_Spacer_35mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_35mm'])

    @classmethod
    def Baader_M42_Varilock_25_35mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Varilock_25_35mm'])

    @classmethod
    def Baader_M48_Varilock_25_35mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Varilock_25_35mm'])

    @classmethod
    def Baader_M54_Varilock_25_35mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Varilock_25_35mm'])

    @classmethod
    def Baader_M42_Male_Male_Ring(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Male_Male_Ring'])

    @classmethod
    def Baader_M48_Male_Male_Ring(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Male_Male_Ring'])

    @classmethod
    def Baader_M54_Male_Male_Ring(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Male_Male_Ring'])

    @classmethod
    def Baader_M56_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M56_Spacer_5mm'])

    @classmethod
    def Baader_M56_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M56_Spacer_10mm'])

    @classmethod
    def Baader_M56_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M56_Spacer_15mm'])

    @classmethod
    def Baader_M63_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M63_Spacer_5mm'])

    @classmethod
    def Baader_M63_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M63_Spacer_10mm'])

    @classmethod
    def Baader_M63_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M63_Spacer_15mm'])

    @classmethod
    def Baader_M84_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M84_Spacer_5mm'])

    @classmethod
    def Baader_M84_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M84_Spacer_10mm'])

    @classmethod
    def Baader_M84_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M84_Spacer_15mm'])

    @classmethod
    def Baader_M84_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M84_Spacer_20mm'])

    @classmethod
    def Baader_2_1_25_Reducer_short(cls):
        return cls.from_database(cls._DATABASE['Baader_2_1_25_Reducer_short'])

    @classmethod
    def Baader_SC_T2_M42_Ultra_Short(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_T2_M42_Ultra_Short'])

    @classmethod
    def Baader_SC_M54_Diamond_Adapter(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_M54_Diamond_Adapter'])

    @classmethod
    def Baader_SC_M68_Diamond_Adapter(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_M68_Diamond_Adapter'])

    @classmethod
    def Baader_M42_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_2_5mm'])

    @classmethod
    def Baader_M42_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_3_5mm'])

    @classmethod
    def Baader_M42_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_9mm'])

    @classmethod
    def Baader_M48_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_2_5mm'])

    @classmethod
    def Baader_M48_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_3_5mm'])

    @classmethod
    def Baader_M54_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_2_5mm'])

    @classmethod
    def Baader_M54_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_6mm'])

    @classmethod
    def Baader_M54_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_17mm'])

    @classmethod
    def Baader_M54_Spacer_28mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_28mm'])

    @classmethod
    def Baader_M68_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_2_5mm'])

    @classmethod
    def Baader_M42_Spacer_2_1mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_2_1mm'])

    @classmethod
    def Baader_M42_Spacer_2_3mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_2_3mm'])

    @classmethod
    def Baader_M42_Spacer_2_7mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_2_7mm'])

    @classmethod
    def Baader_M42_Spacer_3_2mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_3_2mm'])

    @classmethod
    def Baader_M42_Spacer_3_3mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_3_3mm'])

    @classmethod
    def Baader_M42_Spacer_3_7mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_3_7mm'])

    @classmethod
    def Baader_M42_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_4_5mm'])

    @classmethod
    def Baader_M42_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_5_5mm'])

    @classmethod
    def Baader_M42_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_6_5mm'])

    @classmethod
    def Baader_M42_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_8_5mm'])

    @classmethod
    def Baader_M42_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_9_5mm'])

    @classmethod
    def Baader_M42_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_13mm'])

    @classmethod
    def Baader_M42_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_16mm'])

    @classmethod
    def Baader_M42_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_18mm'])

    @classmethod
    def Baader_M42_Spacer_19mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_19mm'])

    @classmethod
    def Baader_M42_Spacer_21mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_21mm'])

    @classmethod
    def Baader_M42_Spacer_23mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_23mm'])

    @classmethod
    def Baader_M42_Spacer_24mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_24mm'])

    @classmethod
    def Baader_M42_Spacer_26mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_26mm'])

    @classmethod
    def Baader_M42_Spacer_27mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_27mm'])

    @classmethod
    def Baader_M42_Spacer_29mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_29mm'])

    @classmethod
    def Baader_M42_Spacer_32mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_32mm'])

    @classmethod
    def Baader_M42_Spacer_33mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_33mm'])

    @classmethod
    def Baader_M42_Spacer_36mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_36mm'])

    @classmethod
    def Baader_M42_Spacer_37mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_37mm'])

    @classmethod
    def Baader_M42_Spacer_38mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_38mm'])

    @classmethod
    def Baader_M48_Spacer_2_1mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_2_1mm'])

    @classmethod
    def Baader_M48_Spacer_2_3mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_2_3mm'])

    @classmethod
    def Baader_M48_Spacer_2_7mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_2_7mm'])

    @classmethod
    def Baader_M48_Spacer_3_2mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_3_2mm'])

    @classmethod
    def Baader_M48_Spacer_3_3mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_3_3mm'])

    @classmethod
    def Baader_M48_Spacer_3_7mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_3_7mm'])

    @classmethod
    def Baader_M48_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_4_5mm'])

    @classmethod
    def Baader_M48_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_5_5mm'])

    @classmethod
    def Baader_M48_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_6_5mm'])

    @classmethod
    def Baader_M48_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_8_5mm'])

    @classmethod
    def Baader_M48_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_9_5mm'])

    @classmethod
    def Baader_M48_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_13mm'])

    @classmethod
    def Baader_M48_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_18mm'])

    @classmethod
    def Baader_M48_Spacer_19mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_19mm'])

    @classmethod
    def Baader_M48_Spacer_21mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_21mm'])

    @classmethod
    def Baader_M48_Spacer_23mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_23mm'])

    @classmethod
    def Baader_M48_Spacer_24mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_24mm'])

    @classmethod
    def Baader_M48_Spacer_26mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_26mm'])

    @classmethod
    def Baader_M48_Spacer_27mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_27mm'])

    @classmethod
    def Baader_M48_Spacer_29mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_29mm'])

    @classmethod
    def Baader_M48_Spacer_32mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_32mm'])

    @classmethod
    def Baader_M48_Spacer_33mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_33mm'])

    @classmethod
    def Baader_M48_Spacer_36mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_36mm'])

    @classmethod
    def Baader_M48_Spacer_37mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_37mm'])

    @classmethod
    def Baader_M48_Spacer_38mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_38mm'])

    @classmethod
    def Baader_M54_Spacer_2_1mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_2_1mm'])

    @classmethod
    def Baader_M54_Spacer_2_3mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_2_3mm'])

    @classmethod
    def Baader_M54_Spacer_2_7mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_2_7mm'])

    @classmethod
    def Baader_M54_Spacer_3_2mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_3_2mm'])

    @classmethod
    def Baader_M54_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_3_5mm'])

    @classmethod
    def Baader_M54_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_4_5mm'])

    @classmethod
    def Baader_M54_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_5_5mm'])

    @classmethod
    def Baader_M54_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_6_5mm'])

    @classmethod
    def Baader_M54_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_7_5mm'])

    @classmethod
    def Baader_M54_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_8_5mm'])

    @classmethod
    def Baader_M54_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_13mm'])

    @classmethod
    def Baader_M54_Spacer_19mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_19mm'])

    @classmethod
    def Baader_M54_Spacer_21mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_21mm'])

    @classmethod
    def Baader_M54_Spacer_23mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_23mm'])

    @classmethod
    def Baader_M54_Spacer_24mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_24mm'])

    @classmethod
    def Baader_M54_Spacer_26mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_26mm'])

    @classmethod
    def Baader_M54_Spacer_27mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_27mm'])

    @classmethod
    def Baader_M54_Spacer_29mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_29mm'])

    @classmethod
    def Baader_M68_Spacer_2_1mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_2_1mm'])

    @classmethod
    def Baader_M68_Spacer_2_3mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_2_3mm'])

    @classmethod
    def Baader_M68_Spacer_2_7mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_2_7mm'])

    @classmethod
    def Baader_M68_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_3_5mm'])

    @classmethod
    def Baader_M68_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_4_5mm'])

    @classmethod
    def Baader_M68_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_5_5mm'])

    @classmethod
    def Baader_M68_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_6_5mm'])

    @classmethod
    def Baader_M68_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_7_5mm'])

    @classmethod
    def Baader_M68_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_8_5mm'])

    @classmethod
    def Baader_M68_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_9_5mm'])

    @classmethod
    def Baader_M68_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_13mm'])

    @classmethod
    def Baader_M68_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_16mm'])

    @classmethod
    def Baader_M68_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_18mm'])

    @classmethod
    def Baader_M68_Spacer_19mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_19mm'])

    @classmethod
    def Baader_M68_Spacer_21mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_21mm'])

    @classmethod
    def Baader_M68_Spacer_23mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_23mm'])

    @classmethod
    def Baader_M68_Spacer_24mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_24mm'])

    @classmethod
    def Baader_M68_Spacer_26mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_26mm'])

    @classmethod
    def Baader_M68_Spacer_27mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_27mm'])

    @classmethod
    def Baader_M72_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Spacer_2_5mm'])

    @classmethod
    def Baader_M72_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Spacer_3_5mm'])

    @classmethod
    def Baader_M72_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Spacer_4mm'])

    @classmethod
    def Baader_M72_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Spacer_4_5mm'])

    @classmethod
    def Baader_M72_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Spacer_5_5mm'])

    @classmethod
    def Baader_M72_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Spacer_6mm'])

    @classmethod
    def Baader_M72_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Spacer_6_5mm'])

    @classmethod
    def Baader_M72_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Spacer_7mm'])

    @classmethod
    def Baader_M72_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Spacer_7_5mm'])

    @classmethod
    def Baader_M72_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Spacer_8mm'])

    @classmethod
    def Baader_M72_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Spacer_8_5mm'])

    @classmethod
    def Baader_M72_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Spacer_9mm'])

    @classmethod
    def Baader_M72_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Spacer_9_5mm'])

    @classmethod
    def Baader_M72_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Spacer_11mm'])

    @classmethod
    def Baader_M72_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Spacer_12mm'])

    @classmethod
    def Baader_M72_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Spacer_13mm'])

    @classmethod
    def Baader_M72_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Spacer_14mm'])

    @classmethod
    def Baader_M72_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Spacer_16mm'])

    @classmethod
    def Baader_M72_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Spacer_17mm'])

    @classmethod
    def Baader_M72_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Spacer_18mm'])

    @classmethod
    def Baader_M72_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Spacer_22mm'])

    @classmethod
    def Baader_M72_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Spacer_25mm'])

    @classmethod
    def Baader_M72_Spacer_28mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Spacer_28mm'])

    @classmethod
    def Baader_M72_Spacer_30mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Spacer_30mm'])

    @classmethod
    def Baader_M82_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Spacer_2_5mm'])

    @classmethod
    def Baader_M82_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Spacer_3mm'])

    @classmethod
    def Baader_M82_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Spacer_3_5mm'])

    @classmethod
    def Baader_M82_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Spacer_4mm'])

    @classmethod
    def Baader_M82_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Spacer_4_5mm'])

    @classmethod
    def Baader_M82_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Spacer_5_5mm'])

    @classmethod
    def Baader_M82_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Spacer_6mm'])

    @classmethod
    def Baader_M82_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Spacer_6_5mm'])

    @classmethod
    def Baader_M82_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Spacer_7mm'])

    @classmethod
    def Baader_M82_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Spacer_7_5mm'])

    @classmethod
    def Baader_M82_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Spacer_8mm'])

    @classmethod
    def Baader_M82_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Spacer_8_5mm'])

    @classmethod
    def Baader_M82_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Spacer_9mm'])

    @classmethod
    def Baader_M82_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Spacer_9_5mm'])

    @classmethod
    def Baader_M82_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Spacer_11mm'])

    @classmethod
    def Baader_M82_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Spacer_12mm'])

    @classmethod
    def Baader_M82_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Spacer_13mm'])

    @classmethod
    def Baader_M82_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Spacer_14mm'])

    @classmethod
    def Baader_M82_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Spacer_16mm'])

    @classmethod
    def Baader_M82_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Spacer_17mm'])

    @classmethod
    def Baader_M82_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Spacer_18mm'])

    @classmethod
    def Baader_M82_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Spacer_22mm'])

    @classmethod
    def Baader_M82_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Spacer_25mm'])

    @classmethod
    def Baader_M82_Spacer_28mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Spacer_28mm'])

    @classmethod
    def Baader_M82_Spacer_30mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Spacer_30mm'])

    @classmethod
    def Baader_M92_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M92_Spacer_2_5mm'])

    @classmethod
    def Baader_M92_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M92_Spacer_3mm'])

    @classmethod
    def Baader_M92_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M92_Spacer_3_5mm'])

    @classmethod
    def Baader_M92_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M92_Spacer_4mm'])

    @classmethod
    def Baader_M92_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M92_Spacer_4_5mm'])

    @classmethod
    def Baader_M92_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M92_Spacer_6mm'])

    @classmethod
    def Baader_M92_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M92_Spacer_6_5mm'])

    @classmethod
    def Baader_M92_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M92_Spacer_7mm'])

    @classmethod
    def Baader_M92_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M92_Spacer_7_5mm'])

    @classmethod
    def Baader_M92_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M92_Spacer_8mm'])

    @classmethod
    def Baader_M92_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M92_Spacer_8_5mm'])

    @classmethod
    def Baader_M92_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M92_Spacer_9mm'])

    @classmethod
    def Baader_M92_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M92_Spacer_9_5mm'])

    @classmethod
    def Baader_M92_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M92_Spacer_11mm'])

    @classmethod
    def Baader_M92_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M92_Spacer_12mm'])

    @classmethod
    def Baader_M92_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M92_Spacer_13mm'])

    @classmethod
    def Baader_M92_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M92_Spacer_14mm'])

    @classmethod
    def Baader_M92_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M92_Spacer_16mm'])

    @classmethod
    def Baader_M92_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M92_Spacer_17mm'])

    @classmethod
    def Baader_M92_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M92_Spacer_18mm'])

    @classmethod
    def Baader_M92_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M92_Spacer_22mm'])

    @classmethod
    def Baader_M92_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M92_Spacer_25mm'])

    @classmethod
    def Baader_M92_Spacer_28mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M92_Spacer_28mm'])

    @classmethod
    def Baader_M92_Spacer_30mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M92_Spacer_30mm'])

    @classmethod
    def Baader_M42_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Extension_Tube_3mm'])

    @classmethod
    def Baader_M42_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Extension_Tube_6mm'])

    @classmethod
    def Baader_M42_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Extension_Tube_9mm'])

    @classmethod
    def Baader_M42_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Extension_Tube_11mm'])

    @classmethod
    def Baader_M42_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Extension_Tube_13mm'])

    @classmethod
    def Baader_M42_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Extension_Tube_16mm'])

    @classmethod
    def Baader_M42_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Extension_Tube_22mm'])

    @classmethod
    def Baader_M42_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Extension_Tube_28mm'])

    @classmethod
    def Baader_M42_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Extension_Tube_35mm'])

    @classmethod
    def Baader_M42_Extension_Tube_45mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Extension_Tube_45mm'])

    @classmethod
    def Baader_M48_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Extension_Tube_3mm'])

    @classmethod
    def Baader_M48_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Extension_Tube_6mm'])

    @classmethod
    def Baader_M48_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Extension_Tube_9mm'])

    @classmethod
    def Baader_M48_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Extension_Tube_11mm'])

    @classmethod
    def Baader_M48_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Extension_Tube_13mm'])

    @classmethod
    def Baader_M48_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Extension_Tube_16mm'])

    @classmethod
    def Baader_M48_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Extension_Tube_22mm'])

    @classmethod
    def Baader_M48_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Extension_Tube_28mm'])

    @classmethod
    def Baader_M48_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Extension_Tube_35mm'])

    @classmethod
    def Baader_M48_Extension_Tube_45mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Extension_Tube_45mm'])

    @classmethod
    def Baader_M54_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Extension_Tube_3mm'])

    @classmethod
    def Baader_M54_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Extension_Tube_6mm'])

    @classmethod
    def Baader_M54_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Extension_Tube_9mm'])

    @classmethod
    def Baader_M54_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Extension_Tube_11mm'])

    @classmethod
    def Baader_M54_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Extension_Tube_13mm'])

    @classmethod
    def Baader_M54_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Extension_Tube_16mm'])

    @classmethod
    def Baader_M54_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Extension_Tube_22mm'])

    @classmethod
    def Baader_M54_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Extension_Tube_28mm'])

    @classmethod
    def Baader_M54_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Extension_Tube_35mm'])

    @classmethod
    def Baader_M54_Extension_Tube_45mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Extension_Tube_45mm'])

    @classmethod
    def Baader_M68_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Extension_Tube_3mm'])

    @classmethod
    def Baader_M68_Extension_Tube_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Extension_Tube_5mm'])

    @classmethod
    def Baader_M68_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Extension_Tube_6mm'])

    @classmethod
    def Baader_M68_Extension_Tube_8mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Extension_Tube_8mm'])

    @classmethod
    def Baader_M68_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Extension_Tube_9mm'])

    @classmethod
    def Baader_M68_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Extension_Tube_11mm'])

    @classmethod
    def Baader_M68_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Extension_Tube_13mm'])

    @classmethod
    def Baader_M68_Extension_Tube_14mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Extension_Tube_14mm'])

    @classmethod
    def Baader_M68_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Extension_Tube_16mm'])

    @classmethod
    def Baader_M68_Extension_Tube_18mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Extension_Tube_18mm'])

    @classmethod
    def Baader_M68_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Extension_Tube_22mm'])

    @classmethod
    def Baader_M68_Extension_Tube_25mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Extension_Tube_25mm'])

    @classmethod
    def Baader_M68_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Extension_Tube_28mm'])

    @classmethod
    def Baader_M68_Extension_Tube_30mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Extension_Tube_30mm'])

    @classmethod
    def Baader_M68_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Extension_Tube_35mm'])

    @classmethod
    def Baader_M72_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Extension_Tube_3mm'])

    @classmethod
    def Baader_M72_Extension_Tube_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Extension_Tube_5mm'])

    @classmethod
    def Baader_M72_Extension_Tube_8mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Extension_Tube_8mm'])

    @classmethod
    def Baader_M72_Extension_Tube_10mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Extension_Tube_10mm'])

    @classmethod
    def Baader_M72_Extension_Tube_12mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Extension_Tube_12mm'])

    @classmethod
    def Baader_M72_Extension_Tube_15mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Extension_Tube_15mm'])

    @classmethod
    def Baader_M72_Extension_Tube_18mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Extension_Tube_18mm'])

    @classmethod
    def Baader_M72_Extension_Tube_20mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Extension_Tube_20mm'])

    @classmethod
    def Baader_M72_Extension_Tube_25mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Extension_Tube_25mm'])

    @classmethod
    def Baader_M72_Extension_Tube_30mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Extension_Tube_30mm'])

    @classmethod
    def Baader_M82_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Extension_Tube_3mm'])

    @classmethod
    def Baader_M82_Extension_Tube_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Extension_Tube_5mm'])

    @classmethod
    def Baader_M82_Extension_Tube_8mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Extension_Tube_8mm'])

    @classmethod
    def Baader_M82_Extension_Tube_10mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Extension_Tube_10mm'])

    @classmethod
    def Baader_M82_Extension_Tube_12mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Extension_Tube_12mm'])

    @classmethod
    def Baader_M82_Extension_Tube_15mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Extension_Tube_15mm'])

    @classmethod
    def Baader_M82_Extension_Tube_18mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Extension_Tube_18mm'])

    @classmethod
    def Baader_M82_Extension_Tube_20mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Extension_Tube_20mm'])

    @classmethod
    def Baader_M82_Extension_Tube_25mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Extension_Tube_25mm'])

    @classmethod
    def Baader_M82_Extension_Tube_30mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Extension_Tube_30mm'])

    @classmethod
    def Baader_SC_Extension_Tube_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Extension_Tube_5mm'])

    @classmethod
    def Baader_SC_Extension_Tube_10mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Extension_Tube_10mm'])

    @classmethod
    def Baader_SC_Extension_Tube_15mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Extension_Tube_15mm'])

    @classmethod
    def Baader_SC_Extension_Tube_20mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Extension_Tube_20mm'])

    @classmethod
    def Baader_SC_Extension_Tube_25mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Extension_Tube_25mm'])

    @classmethod
    def Baader_SC_Extension_Tube_30mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Extension_Tube_30mm'])

    @classmethod
    def Baader_SC_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Extension_Tube_35mm'])

    @classmethod
    def Baader_SC_Extension_Tube_40mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Extension_Tube_40mm'])

    @classmethod
    def Baader_SC_Extension_Tube_50mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Extension_Tube_50mm'])

    @classmethod
    def Baader_SC_Extension_Tube_60mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Extension_Tube_60mm'])

    @classmethod
    def Baader_SC_Extension_Tube_75mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Extension_Tube_75mm'])

    @classmethod
    def Baader_SC_Schmidt_Cassegrain_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Schmidt_Cassegrain_Spacer_2_5mm'])

    @classmethod
    def Baader_SC_Schmidt_Cassegrain_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Schmidt_Cassegrain_Spacer_3mm'])

    @classmethod
    def Baader_SC_Schmidt_Cassegrain_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Schmidt_Cassegrain_Spacer_3_5mm'])

    @classmethod
    def Baader_SC_Schmidt_Cassegrain_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Schmidt_Cassegrain_Spacer_4_5mm'])

    @classmethod
    def Baader_SC_Schmidt_Cassegrain_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Schmidt_Cassegrain_Spacer_5_5mm'])

    @classmethod
    def Baader_SC_Schmidt_Cassegrain_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Schmidt_Cassegrain_Spacer_6mm'])

    @classmethod
    def Baader_SC_Schmidt_Cassegrain_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Schmidt_Cassegrain_Spacer_6_5mm'])

    @classmethod
    def Baader_SC_Schmidt_Cassegrain_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Schmidt_Cassegrain_Spacer_7_5mm'])

    @classmethod
    def Baader_SC_Schmidt_Cassegrain_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Schmidt_Cassegrain_Spacer_8_5mm'])

    @classmethod
    def Baader_SC_Schmidt_Cassegrain_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Schmidt_Cassegrain_Spacer_9_5mm'])

    @classmethod
    def Baader_SC_Schmidt_Cassegrain_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Schmidt_Cassegrain_Spacer_11mm'])

    @classmethod
    def Baader_SC_Schmidt_Cassegrain_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Schmidt_Cassegrain_Spacer_12mm'])

    @classmethod
    def Baader_SC_Schmidt_Cassegrain_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Schmidt_Cassegrain_Spacer_13mm'])

    @classmethod
    def Baader_SC_Schmidt_Cassegrain_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Schmidt_Cassegrain_Spacer_14mm'])

    @classmethod
    def Baader_SC_Schmidt_Cassegrain_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Schmidt_Cassegrain_Spacer_16mm'])

    @classmethod
    def Baader_SC_Schmidt_Cassegrain_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Schmidt_Cassegrain_Spacer_17mm'])

    @classmethod
    def Baader_SC_Schmidt_Cassegrain_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Schmidt_Cassegrain_Spacer_18mm'])

    @classmethod
    def Baader_SC_Schmidt_Cassegrain_Spacer_19mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Schmidt_Cassegrain_Spacer_19mm'])

    @classmethod
    def Baader_SC_Schmidt_Cassegrain_Spacer_21mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Schmidt_Cassegrain_Spacer_21mm'])

    @classmethod
    def Baader_SC_Schmidt_Cassegrain_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Schmidt_Cassegrain_Spacer_22mm'])

    @classmethod
    def Baader_SC_Schmidt_Cassegrain_Spacer_23mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Schmidt_Cassegrain_Spacer_23mm'])

    @classmethod
    def Baader_SC_Schmidt_Cassegrain_Spacer_28mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Schmidt_Cassegrain_Spacer_28mm'])

    @classmethod
    def Baader_SC_Schmidt_Cassegrain_Spacer_32mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Schmidt_Cassegrain_Spacer_32mm'])

    @classmethod
    def Baader_SC_Schmidt_Cassegrain_Spacer_35mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Schmidt_Cassegrain_Spacer_35mm'])

    @classmethod
    def Baader_M92_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M92_Spacer_5_5mm'])

    @classmethod
    def Baader_1_25_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_1_25_Spacer_2_5mm'])

    @classmethod
    def Baader_1_25_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Baader_1_25_Spacer_3mm'])

    @classmethod
    def Baader_1_25_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_1_25_Spacer_3_5mm'])

    @classmethod
    def Baader_1_25_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Baader_1_25_Spacer_4mm'])

    @classmethod
    def Baader_1_25_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_1_25_Spacer_5mm'])

    @classmethod
    def Baader_1_25_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Baader_1_25_Spacer_6mm'])

    @classmethod
    def Baader_1_25_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Baader_1_25_Spacer_7mm'])

    @classmethod
    def Baader_1_25_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Baader_1_25_Spacer_8mm'])

    @classmethod
    def Baader_1_25_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Baader_1_25_Spacer_9mm'])

    @classmethod
    def Baader_1_25_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Baader_1_25_Spacer_10mm'])

    @classmethod
    def Baader_1_25_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Baader_1_25_Spacer_12mm'])

    @classmethod
    def Baader_1_25_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Baader_1_25_Spacer_15mm'])

    @classmethod
    def Baader_1_25_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Baader_1_25_Spacer_18mm'])

    @classmethod
    def Baader_1_25_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Baader_1_25_Spacer_20mm'])

    @classmethod
    def Baader_1_25_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Baader_1_25_Spacer_25mm'])

    @classmethod
    def Baader_2_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_2_Spacer_2_5mm'])

    @classmethod
    def Baader_2_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Baader_2_Spacer_3mm'])

    @classmethod
    def Baader_2_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_2_Spacer_3_5mm'])

    @classmethod
    def Baader_2_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Baader_2_Spacer_4mm'])

    @classmethod
    def Baader_2_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_2_Spacer_5mm'])

    @classmethod
    def Baader_2_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Baader_2_Spacer_6mm'])

    @classmethod
    def Baader_2_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Baader_2_Spacer_7mm'])

    @classmethod
    def Baader_2_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Baader_2_Spacer_8mm'])

    @classmethod
    def Baader_2_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Baader_2_Spacer_9mm'])

    @classmethod
    def Baader_2_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Baader_2_Spacer_10mm'])

    @classmethod
    def Baader_2_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Baader_2_Spacer_12mm'])

    @classmethod
    def Baader_2_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Baader_2_Spacer_15mm'])

    @classmethod
    def Baader_2_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Baader_2_Spacer_18mm'])

    @classmethod
    def Baader_2_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Baader_2_Spacer_20mm'])

    @classmethod
    def Baader_2_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Baader_2_Spacer_25mm'])

    @classmethod
    def Baader_M84_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M84_Spacer_3mm'])

    @classmethod
    def Baader_M84_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M84_Spacer_4mm'])

    @classmethod
    def Baader_M84_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M84_Spacer_5_5mm'])

    @classmethod
    def Baader_M84_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M84_Spacer_6mm'])

    @classmethod
    def Baader_M84_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M84_Spacer_6_5mm'])

    @classmethod
    def Baader_M84_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M84_Spacer_7mm'])

    @classmethod
    def Baader_M84_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M84_Spacer_7_5mm'])

    @classmethod
    def Baader_M84_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M84_Spacer_8mm'])

    @classmethod
    def Baader_M84_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M84_Spacer_8_5mm'])

    @classmethod
    def Baader_M84_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M84_Spacer_9mm'])

    @classmethod
    def Baader_M84_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M84_Spacer_9_5mm'])

    @classmethod
    def Baader_M84_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M84_Spacer_11mm'])

    @classmethod
    def Baader_M84_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M84_Spacer_13mm'])

    @classmethod
    def Baader_M84_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M84_Spacer_16mm'])

    @classmethod
    def Baader_M84_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M84_Spacer_18mm'])

    @classmethod
    def Baader_M84_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M84_Spacer_22mm'])

    @classmethod
    def Baader_M84_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M84_Spacer_25mm'])

class BaaderSpacer(Spacer):
    _DATABASE = {'Baader_M42_Spacer_0_3mm': {'brand': 'Baader', 'name': 'M42 Spacer 0.3mm', 'type': 'type_spacer', 'optical_length': 0.3, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_0_5mm': {'brand': 'Baader', 'name': 'M42 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_1mm': {'brand': 'Baader', 'name': 'M42 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_1_5mm': {'brand': 'Baader', 'name': 'M42 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_2mm': {'brand': 'Baader', 'name': 'M42 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_0_3mm': {'brand': 'Baader', 'name': 'M48 Spacer 0.3mm', 'type': 'type_spacer', 'optical_length': 0.3, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_0_5mm': {'brand': 'Baader', 'name': 'M48 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_1mm': {'brand': 'Baader', 'name': 'M48 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_2mm': {'brand': 'Baader', 'name': 'M48 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_0_5mm': {'brand': 'Baader', 'name': 'M54 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_1mm': {'brand': 'Baader', 'name': 'M54 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_2mm': {'brand': 'Baader', 'name': 'M54 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_0_5mm': {'brand': 'Baader', 'name': 'M68 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_1mm': {'brand': 'Baader', 'name': 'M68 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_2mm': {'brand': 'Baader', 'name': 'M68 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M72_Spacer_1mm': {'brand': 'Baader', 'name': 'M72 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 13, 'tside_thread': 'M72', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M72_Spacer_2mm': {'brand': 'Baader', 'name': 'M72 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 13, 'tside_thread': 'M72', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M82_Spacer_2mm': {'brand': 'Baader', 'name': 'M82 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 16, 'tside_thread': 'M82', 'tside_gender': '', 'cside_thread': 'M82', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_0_15mm': {'brand': 'Baader', 'name': 'M42 Spacer 0.15mm', 'type': 'type_spacer', 'optical_length': 0.15, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M56_Spacer_1mm': {'brand': 'Baader', 'name': 'M56 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 9, 'tside_thread': 'M56', 'tside_gender': '', 'cside_thread': 'M56', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M56_Spacer_2mm': {'brand': 'Baader', 'name': 'M56 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 9, 'tside_thread': 'M56', 'tside_gender': '', 'cside_thread': 'M56', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M63_Spacer_1mm': {'brand': 'Baader', 'name': 'M63 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 11, 'tside_thread': 'M63', 'tside_gender': '', 'cside_thread': 'M63', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M63_Spacer_2mm': {'brand': 'Baader', 'name': 'M63 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 11, 'tside_thread': 'M63', 'tside_gender': '', 'cside_thread': 'M63', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_0_25mm': {'brand': 'Baader', 'name': 'M42 Spacer 0.25mm', 'type': 'type_spacer', 'optical_length': 0.25, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_0_35mm': {'brand': 'Baader', 'name': 'M42 Spacer 0.35mm', 'type': 'type_spacer', 'optical_length': 0.35, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_0_6mm': {'brand': 'Baader', 'name': 'M42 Spacer 0.6mm', 'type': 'type_spacer', 'optical_length': 0.6, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_0_75mm': {'brand': 'Baader', 'name': 'M42 Spacer 0.75mm', 'type': 'type_spacer', 'optical_length': 0.75, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_0_8mm': {'brand': 'Baader', 'name': 'M42 Spacer 0.8mm', 'type': 'type_spacer', 'optical_length': 0.8, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_0_9mm': {'brand': 'Baader', 'name': 'M42 Spacer 0.9mm', 'type': 'type_spacer', 'optical_length': 0.9, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_1_2mm': {'brand': 'Baader', 'name': 'M42 Spacer 1.2mm', 'type': 'type_spacer', 'optical_length': 1.2, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_1_8mm': {'brand': 'Baader', 'name': 'M42 Spacer 1.8mm', 'type': 'type_spacer', 'optical_length': 1.8, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_0_15mm': {'brand': 'Baader', 'name': 'M48 Spacer 0.15mm', 'type': 'type_spacer', 'optical_length': 0.15, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_0_25mm': {'brand': 'Baader', 'name': 'M48 Spacer 0.25mm', 'type': 'type_spacer', 'optical_length': 0.25, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_0_35mm': {'brand': 'Baader', 'name': 'M48 Spacer 0.35mm', 'type': 'type_spacer', 'optical_length': 0.35, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_0_6mm': {'brand': 'Baader', 'name': 'M48 Spacer 0.6mm', 'type': 'type_spacer', 'optical_length': 0.6, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_0_75mm': {'brand': 'Baader', 'name': 'M48 Spacer 0.75mm', 'type': 'type_spacer', 'optical_length': 0.75, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_0_8mm': {'brand': 'Baader', 'name': 'M48 Spacer 0.8mm', 'type': 'type_spacer', 'optical_length': 0.8, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_0_9mm': {'brand': 'Baader', 'name': 'M48 Spacer 0.9mm', 'type': 'type_spacer', 'optical_length': 0.9, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_1_2mm': {'brand': 'Baader', 'name': 'M48 Spacer 1.2mm', 'type': 'type_spacer', 'optical_length': 1.2, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_1_8mm': {'brand': 'Baader', 'name': 'M48 Spacer 1.8mm', 'type': 'type_spacer', 'optical_length': 1.8, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_0_25mm': {'brand': 'Baader', 'name': 'M54 Spacer 0.25mm', 'type': 'type_spacer', 'optical_length': 0.25, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_0_3mm': {'brand': 'Baader', 'name': 'M54 Spacer 0.3mm', 'type': 'type_spacer', 'optical_length': 0.3, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_0_6mm': {'brand': 'Baader', 'name': 'M54 Spacer 0.6mm', 'type': 'type_spacer', 'optical_length': 0.6, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_0_75mm': {'brand': 'Baader', 'name': 'M54 Spacer 0.75mm', 'type': 'type_spacer', 'optical_length': 0.75, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_0_8mm': {'brand': 'Baader', 'name': 'M54 Spacer 0.8mm', 'type': 'type_spacer', 'optical_length': 0.8, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_1_2mm': {'brand': 'Baader', 'name': 'M54 Spacer 1.2mm', 'type': 'type_spacer', 'optical_length': 1.2, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_1_5mm': {'brand': 'Baader', 'name': 'M54 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_0_25mm': {'brand': 'Baader', 'name': 'M68 Spacer 0.25mm', 'type': 'type_spacer', 'optical_length': 0.25, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_0_3mm': {'brand': 'Baader', 'name': 'M68 Spacer 0.3mm', 'type': 'type_spacer', 'optical_length': 0.3, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_0_6mm': {'brand': 'Baader', 'name': 'M68 Spacer 0.6mm', 'type': 'type_spacer', 'optical_length': 0.6, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_0_75mm': {'brand': 'Baader', 'name': 'M68 Spacer 0.75mm', 'type': 'type_spacer', 'optical_length': 0.75, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_0_8mm': {'brand': 'Baader', 'name': 'M68 Spacer 0.8mm', 'type': 'type_spacer', 'optical_length': 0.8, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_1_2mm': {'brand': 'Baader', 'name': 'M68 Spacer 1.2mm', 'type': 'type_spacer', 'optical_length': 1.2, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_1_5mm': {'brand': 'Baader', 'name': 'M68 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_1_1mm': {'brand': 'Baader', 'name': 'M42 Spacer 1.1mm', 'type': 'type_spacer', 'optical_length': 1.1, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_1_3mm': {'brand': 'Baader', 'name': 'M42 Spacer 1.3mm', 'type': 'type_spacer', 'optical_length': 1.3, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_1_7mm': {'brand': 'Baader', 'name': 'M42 Spacer 1.7mm', 'type': 'type_spacer', 'optical_length': 1.7, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M42_Spacer_1_9mm': {'brand': 'Baader', 'name': 'M42 Spacer 1.9mm', 'type': 'type_spacer', 'optical_length': 1.9, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_1_1mm': {'brand': 'Baader', 'name': 'M48 Spacer 1.1mm', 'type': 'type_spacer', 'optical_length': 1.1, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_1_3mm': {'brand': 'Baader', 'name': 'M48 Spacer 1.3mm', 'type': 'type_spacer', 'optical_length': 1.3, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_1_7mm': {'brand': 'Baader', 'name': 'M48 Spacer 1.7mm', 'type': 'type_spacer', 'optical_length': 1.7, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M48_Spacer_1_9mm': {'brand': 'Baader', 'name': 'M48 Spacer 1.9mm', 'type': 'type_spacer', 'optical_length': 1.9, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_1_1mm': {'brand': 'Baader', 'name': 'M54 Spacer 1.1mm', 'type': 'type_spacer', 'optical_length': 1.1, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_1_3mm': {'brand': 'Baader', 'name': 'M54 Spacer 1.3mm', 'type': 'type_spacer', 'optical_length': 1.3, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_1_7mm': {'brand': 'Baader', 'name': 'M54 Spacer 1.7mm', 'type': 'type_spacer', 'optical_length': 1.7, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M54_Spacer_1_9mm': {'brand': 'Baader', 'name': 'M54 Spacer 1.9mm', 'type': 'type_spacer', 'optical_length': 1.9, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_1_1mm': {'brand': 'Baader', 'name': 'M68 Spacer 1.1mm', 'type': 'type_spacer', 'optical_length': 1.1, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_1_3mm': {'brand': 'Baader', 'name': 'M68 Spacer 1.3mm', 'type': 'type_spacer', 'optical_length': 1.3, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_1_7mm': {'brand': 'Baader', 'name': 'M68 Spacer 1.7mm', 'type': 'type_spacer', 'optical_length': 1.7, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M68_Spacer_1_9mm': {'brand': 'Baader', 'name': 'M68 Spacer 1.9mm', 'type': 'type_spacer', 'optical_length': 1.9, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M72_Spacer_0_3mm': {'brand': 'Baader', 'name': 'M72 Spacer 0.3mm', 'type': 'type_spacer', 'optical_length': 0.3, 'mass': 13, 'tside_thread': 'M72', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M72_Spacer_0_5mm': {'brand': 'Baader', 'name': 'M72 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 13, 'tside_thread': 'M72', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M72_Spacer_0_7mm': {'brand': 'Baader', 'name': 'M72 Spacer 0.7mm', 'type': 'type_spacer', 'optical_length': 0.7, 'mass': 13, 'tside_thread': 'M72', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M72_Spacer_0_8mm': {'brand': 'Baader', 'name': 'M72 Spacer 0.8mm', 'type': 'type_spacer', 'optical_length': 0.8, 'mass': 13, 'tside_thread': 'M72', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M72_Spacer_1_1mm': {'brand': 'Baader', 'name': 'M72 Spacer 1.1mm', 'type': 'type_spacer', 'optical_length': 1.1, 'mass': 13, 'tside_thread': 'M72', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M72_Spacer_1_3mm': {'brand': 'Baader', 'name': 'M72 Spacer 1.3mm', 'type': 'type_spacer', 'optical_length': 1.3, 'mass': 13, 'tside_thread': 'M72', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M72_Spacer_1_5mm': {'brand': 'Baader', 'name': 'M72 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 13, 'tside_thread': 'M72', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M72_Spacer_1_7mm': {'brand': 'Baader', 'name': 'M72 Spacer 1.7mm', 'type': 'type_spacer', 'optical_length': 1.7, 'mass': 13, 'tside_thread': 'M72', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M82_Spacer_0_5mm': {'brand': 'Baader', 'name': 'M82 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 16, 'tside_thread': 'M82', 'tside_gender': '', 'cside_thread': 'M82', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M82_Spacer_0_7mm': {'brand': 'Baader', 'name': 'M82 Spacer 0.7mm', 'type': 'type_spacer', 'optical_length': 0.7, 'mass': 16, 'tside_thread': 'M82', 'tside_gender': '', 'cside_thread': 'M82', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M82_Spacer_1mm': {'brand': 'Baader', 'name': 'M82 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 16, 'tside_thread': 'M82', 'tside_gender': '', 'cside_thread': 'M82', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M82_Spacer_1_5mm': {'brand': 'Baader', 'name': 'M82 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 16, 'tside_thread': 'M82', 'tside_gender': '', 'cside_thread': 'M82', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M92_Spacer_0_5mm': {'brand': 'Baader', 'name': 'M92 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 19, 'tside_thread': 'M92', 'tside_gender': '', 'cside_thread': 'M92', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M92_Spacer_1mm': {'brand': 'Baader', 'name': 'M92 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 19, 'tside_thread': 'M92', 'tside_gender': '', 'cside_thread': 'M92', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M92_Spacer_1_5mm': {'brand': 'Baader', 'name': 'M92 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 19, 'tside_thread': 'M92', 'tside_gender': '', 'cside_thread': 'M92', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M92_Spacer_2mm': {'brand': 'Baader', 'name': 'M92 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 19, 'tside_thread': 'M92', 'tside_gender': '', 'cside_thread': 'M92', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_SC_Schmidt_Cassegrain_Spacer_0_5mm': {'brand': 'Baader', 'name': 'SC (Schmidt-Cassegrain) Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 21, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_SC_Schmidt_Cassegrain_Spacer_1mm': {'brand': 'Baader', 'name': 'SC (Schmidt-Cassegrain) Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 21, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_SC_Schmidt_Cassegrain_Spacer_1_5mm': {'brand': 'Baader', 'name': 'SC (Schmidt-Cassegrain) Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 21, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_SC_Schmidt_Cassegrain_Spacer_2mm': {'brand': 'Baader', 'name': 'SC (Schmidt-Cassegrain) Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 21, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_1_25_Spacer_0_5mm': {'brand': 'Baader', 'name': '1.25" Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 4, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_1_25_Spacer_1mm': {'brand': 'Baader', 'name': '1.25" Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 4, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_1_25_Spacer_1_5mm': {'brand': 'Baader', 'name': '1.25" Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 4, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_1_25_Spacer_2mm': {'brand': 'Baader', 'name': '1.25" Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 4, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_2_Spacer_0_5mm': {'brand': 'Baader', 'name': '2" Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 9, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_2_Spacer_1mm': {'brand': 'Baader', 'name': '2" Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 9, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_2_Spacer_1_5mm': {'brand': 'Baader', 'name': '2" Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 9, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_2_Spacer_2mm': {'brand': 'Baader', 'name': '2" Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 9, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Baader_M84_Spacer_0_5mm': {'brand': 'Baader', 'name': 'M84 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 15, 'tside_thread': 'M84', 'tside_gender': '', 'cside_thread': 'M84', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M84_Spacer_1mm': {'brand': 'Baader', 'name': 'M84 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 15, 'tside_thread': 'M84', 'tside_gender': '', 'cside_thread': 'M84', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M84_Spacer_1_5mm': {'brand': 'Baader', 'name': 'M84 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 15, 'tside_thread': 'M84', 'tside_gender': '', 'cside_thread': 'M84', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Baader_M84_Spacer_2mm': {'brand': 'Baader', 'name': 'M84 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 15, 'tside_thread': 'M84', 'tside_gender': '', 'cside_thread': 'M84', 'cside_gender': '', 'reversible': True, 'bf_role': ''}}

    @classmethod
    def Baader_M42_Spacer_0_3mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_0_3mm'])

    @classmethod
    def Baader_M42_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_0_5mm'])

    @classmethod
    def Baader_M42_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_1mm'])

    @classmethod
    def Baader_M42_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_1_5mm'])

    @classmethod
    def Baader_M42_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_2mm'])

    @classmethod
    def Baader_M48_Spacer_0_3mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_0_3mm'])

    @classmethod
    def Baader_M48_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_0_5mm'])

    @classmethod
    def Baader_M48_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_1mm'])

    @classmethod
    def Baader_M48_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_2mm'])

    @classmethod
    def Baader_M54_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_0_5mm'])

    @classmethod
    def Baader_M54_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_1mm'])

    @classmethod
    def Baader_M54_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_2mm'])

    @classmethod
    def Baader_M68_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_0_5mm'])

    @classmethod
    def Baader_M68_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_1mm'])

    @classmethod
    def Baader_M68_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_2mm'])

    @classmethod
    def Baader_M72_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Spacer_1mm'])

    @classmethod
    def Baader_M72_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Spacer_2mm'])

    @classmethod
    def Baader_M82_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Spacer_2mm'])

    @classmethod
    def Baader_M42_Spacer_0_15mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_0_15mm'])

    @classmethod
    def Baader_M56_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M56_Spacer_1mm'])

    @classmethod
    def Baader_M56_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M56_Spacer_2mm'])

    @classmethod
    def Baader_M63_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M63_Spacer_1mm'])

    @classmethod
    def Baader_M63_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M63_Spacer_2mm'])

    @classmethod
    def Baader_M42_Spacer_0_25mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_0_25mm'])

    @classmethod
    def Baader_M42_Spacer_0_35mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_0_35mm'])

    @classmethod
    def Baader_M42_Spacer_0_6mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_0_6mm'])

    @classmethod
    def Baader_M42_Spacer_0_75mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_0_75mm'])

    @classmethod
    def Baader_M42_Spacer_0_8mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_0_8mm'])

    @classmethod
    def Baader_M42_Spacer_0_9mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_0_9mm'])

    @classmethod
    def Baader_M42_Spacer_1_2mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_1_2mm'])

    @classmethod
    def Baader_M42_Spacer_1_8mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_1_8mm'])

    @classmethod
    def Baader_M48_Spacer_0_15mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_0_15mm'])

    @classmethod
    def Baader_M48_Spacer_0_25mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_0_25mm'])

    @classmethod
    def Baader_M48_Spacer_0_35mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_0_35mm'])

    @classmethod
    def Baader_M48_Spacer_0_6mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_0_6mm'])

    @classmethod
    def Baader_M48_Spacer_0_75mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_0_75mm'])

    @classmethod
    def Baader_M48_Spacer_0_8mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_0_8mm'])

    @classmethod
    def Baader_M48_Spacer_0_9mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_0_9mm'])

    @classmethod
    def Baader_M48_Spacer_1_2mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_1_2mm'])

    @classmethod
    def Baader_M48_Spacer_1_8mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_1_8mm'])

    @classmethod
    def Baader_M54_Spacer_0_25mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_0_25mm'])

    @classmethod
    def Baader_M54_Spacer_0_3mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_0_3mm'])

    @classmethod
    def Baader_M54_Spacer_0_6mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_0_6mm'])

    @classmethod
    def Baader_M54_Spacer_0_75mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_0_75mm'])

    @classmethod
    def Baader_M54_Spacer_0_8mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_0_8mm'])

    @classmethod
    def Baader_M54_Spacer_1_2mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_1_2mm'])

    @classmethod
    def Baader_M54_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_1_5mm'])

    @classmethod
    def Baader_M68_Spacer_0_25mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_0_25mm'])

    @classmethod
    def Baader_M68_Spacer_0_3mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_0_3mm'])

    @classmethod
    def Baader_M68_Spacer_0_6mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_0_6mm'])

    @classmethod
    def Baader_M68_Spacer_0_75mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_0_75mm'])

    @classmethod
    def Baader_M68_Spacer_0_8mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_0_8mm'])

    @classmethod
    def Baader_M68_Spacer_1_2mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_1_2mm'])

    @classmethod
    def Baader_M68_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_1_5mm'])

    @classmethod
    def Baader_M42_Spacer_1_1mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_1_1mm'])

    @classmethod
    def Baader_M42_Spacer_1_3mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_1_3mm'])

    @classmethod
    def Baader_M42_Spacer_1_7mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_1_7mm'])

    @classmethod
    def Baader_M42_Spacer_1_9mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M42_Spacer_1_9mm'])

    @classmethod
    def Baader_M48_Spacer_1_1mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_1_1mm'])

    @classmethod
    def Baader_M48_Spacer_1_3mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_1_3mm'])

    @classmethod
    def Baader_M48_Spacer_1_7mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_1_7mm'])

    @classmethod
    def Baader_M48_Spacer_1_9mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M48_Spacer_1_9mm'])

    @classmethod
    def Baader_M54_Spacer_1_1mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_1_1mm'])

    @classmethod
    def Baader_M54_Spacer_1_3mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_1_3mm'])

    @classmethod
    def Baader_M54_Spacer_1_7mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_1_7mm'])

    @classmethod
    def Baader_M54_Spacer_1_9mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M54_Spacer_1_9mm'])

    @classmethod
    def Baader_M68_Spacer_1_1mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_1_1mm'])

    @classmethod
    def Baader_M68_Spacer_1_3mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_1_3mm'])

    @classmethod
    def Baader_M68_Spacer_1_7mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_1_7mm'])

    @classmethod
    def Baader_M68_Spacer_1_9mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M68_Spacer_1_9mm'])

    @classmethod
    def Baader_M72_Spacer_0_3mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Spacer_0_3mm'])

    @classmethod
    def Baader_M72_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Spacer_0_5mm'])

    @classmethod
    def Baader_M72_Spacer_0_7mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Spacer_0_7mm'])

    @classmethod
    def Baader_M72_Spacer_0_8mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Spacer_0_8mm'])

    @classmethod
    def Baader_M72_Spacer_1_1mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Spacer_1_1mm'])

    @classmethod
    def Baader_M72_Spacer_1_3mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Spacer_1_3mm'])

    @classmethod
    def Baader_M72_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Spacer_1_5mm'])

    @classmethod
    def Baader_M72_Spacer_1_7mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M72_Spacer_1_7mm'])

    @classmethod
    def Baader_M82_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Spacer_0_5mm'])

    @classmethod
    def Baader_M82_Spacer_0_7mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Spacer_0_7mm'])

    @classmethod
    def Baader_M82_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Spacer_1mm'])

    @classmethod
    def Baader_M82_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M82_Spacer_1_5mm'])

    @classmethod
    def Baader_M92_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M92_Spacer_0_5mm'])

    @classmethod
    def Baader_M92_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M92_Spacer_1mm'])

    @classmethod
    def Baader_M92_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M92_Spacer_1_5mm'])

    @classmethod
    def Baader_M92_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M92_Spacer_2mm'])

    @classmethod
    def Baader_SC_Schmidt_Cassegrain_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Schmidt_Cassegrain_Spacer_0_5mm'])

    @classmethod
    def Baader_SC_Schmidt_Cassegrain_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Schmidt_Cassegrain_Spacer_1mm'])

    @classmethod
    def Baader_SC_Schmidt_Cassegrain_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Schmidt_Cassegrain_Spacer_1_5mm'])

    @classmethod
    def Baader_SC_Schmidt_Cassegrain_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Baader_SC_Schmidt_Cassegrain_Spacer_2mm'])

    @classmethod
    def Baader_1_25_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_1_25_Spacer_0_5mm'])

    @classmethod
    def Baader_1_25_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Baader_1_25_Spacer_1mm'])

    @classmethod
    def Baader_1_25_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_1_25_Spacer_1_5mm'])

    @classmethod
    def Baader_1_25_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Baader_1_25_Spacer_2mm'])

    @classmethod
    def Baader_2_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_2_Spacer_0_5mm'])

    @classmethod
    def Baader_2_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Baader_2_Spacer_1mm'])

    @classmethod
    def Baader_2_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_2_Spacer_1_5mm'])

    @classmethod
    def Baader_2_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Baader_2_Spacer_2mm'])

    @classmethod
    def Baader_M84_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M84_Spacer_0_5mm'])

    @classmethod
    def Baader_M84_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M84_Spacer_1mm'])

    @classmethod
    def Baader_M84_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M84_Spacer_1_5mm'])

    @classmethod
    def Baader_M84_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Baader_M84_Spacer_2mm'])