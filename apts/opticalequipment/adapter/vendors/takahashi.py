from ..base import Adapter, Spacer

class TakahashiAdapter(Adapter):
    _DATABASE = {'Takahashi_CA_35_M82_M54': {'brand': 'Takahashi', 'name': 'CA-35 (M82→M54)', 'type': 'type_adapter', 'optical_length': 8, 'mass': 50, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_DX_WR_Wide_Ring_M72': {'brand': 'Takahashi', 'name': 'DX-WR Wide Ring (M72)', 'type': 'type_adapter', 'optical_length': 5, 'mass': 40, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M72_M82_Adapter': {'brand': 'Takahashi', 'name': 'M72→M82 Adapter', 'type': 'type_adapter', 'optical_length': 6, 'mass': 50, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M82_M54_Adapter': {'brand': 'Takahashi', 'name': 'M82→M54 Adapter', 'type': 'type_adapter', 'optical_length': 8, 'mass': 40, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M92_M82_Adapter': {'brand': 'Takahashi', 'name': 'M92→M82 Adapter', 'type': 'type_adapter', 'optical_length': 8, 'mass': 60, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M54_M42_Adapter': {'brand': 'Takahashi', 'name': 'M54→M42 Adapter', 'type': 'type_adapter', 'optical_length': 8, 'mass': 30, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_Wide_T_Adapter_M42': {'brand': 'Takahashi', 'name': 'Wide T-Adapter (M42)', 'type': 'type_adapter', 'optical_length': 10, 'mass': 30, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M72_M54_Adapter': {'brand': 'Takahashi', 'name': 'M72→M54 Adapter', 'type': 'type_adapter', 'optical_length': 8, 'mass': 40, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M92_M72_Adapter': {'brand': 'Takahashi', 'name': 'M92→M72 Adapter', 'type': 'type_adapter', 'optical_length': 8, 'mass': 55, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M42_EOS_Adapter': {'brand': 'Takahashi', 'name': 'M42→EOS Adapter', 'type': 'type_adapter', 'optical_length': 10, 'mass': 30, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M42_Nikon_F_Adapter': {'brand': 'Takahashi', 'name': 'M42→Nikon F Adapter', 'type': 'type_adapter', 'optical_length': 10, 'mass': 30, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M42_Sony_E_Adapter': {'brand': 'Takahashi', 'name': 'M42→Sony E Adapter', 'type': 'type_adapter', 'optical_length': 8, 'mass': 25, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M42_Canon_RF_Adapter': {'brand': 'Takahashi', 'name': 'M42→Canon RF Adapter', 'type': 'type_adapter', 'optical_length': 6, 'mass': 25, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M72_M68_Adapter': {'brand': 'Takahashi', 'name': 'M72→M68 Adapter', 'type': 'type_adapter', 'optical_length': 6, 'mass': 45, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_DX_60W_Camera_Mount_EOS': {'brand': 'Takahashi', 'name': 'DX-60W Camera Mount (EOS)', 'type': 'type_adapter', 'optical_length': 12, 'mass': 50, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': 'M52', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_DX_WR_Camera_Mount_EOS': {'brand': 'Takahashi', 'name': 'DX-WR Camera Mount (EOS)', 'type': 'type_adapter', 'optical_length': 12, 'mass': 145, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_CA_35_SKY90': {'brand': 'Takahashi', 'name': 'CA-35 (SKY90)', 'type': 'type_adapter', 'optical_length': 16, 'mass': 23, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''}, 'Takahashi_Multi_CA_Ring_76': {'brand': 'Takahashi', 'name': 'Multi-CA Ring 76', 'type': 'type_adapter', 'optical_length': 18.8, 'mass': 30, 'tside_thread': 'M52', 'tside_gender': 'Female', 'cside_thread': 'M52', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M42_Spacer_5mm': {'brand': 'Takahashi', 'name': 'M42 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 8, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M42_Spacer_10mm': {'brand': 'Takahashi', 'name': 'M42 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 12, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M42_Spacer_15mm': {'brand': 'Takahashi', 'name': 'M42 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M54_Spacer_5mm': {'brand': 'Takahashi', 'name': 'M54 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 12, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M54_Spacer_10mm': {'brand': 'Takahashi', 'name': 'M54 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 16, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M54_Spacer_15mm': {'brand': 'Takahashi', 'name': 'M54 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 20, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M72_Spacer_5mm': {'brand': 'Takahashi', 'name': 'M72 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 16, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M72_Spacer_10mm': {'brand': 'Takahashi', 'name': 'M72 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 20, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M82_Spacer_5mm': {'brand': 'Takahashi', 'name': 'M82 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 19, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M82_Spacer_10mm': {'brand': 'Takahashi', 'name': 'M82 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 23, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M82_Spacer_15mm': {'brand': 'Takahashi', 'name': 'M82 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 27, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M82_Spacer_20mm': {'brand': 'Takahashi', 'name': 'M82 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 31, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M54_EOS_Adapter_CA_35EOS': {'brand': 'Takahashi', 'name': 'M54→EOS Adapter (CA-35EOS)', 'type': 'type_adapter', 'optical_length': 10, 'mass': 40, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M42_M54_Adapter': {'brand': 'Takahashi', 'name': 'M42→M54 Adapter', 'type': 'type_adapter', 'optical_length': 8, 'mass': 30, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M92_M54_Adapter': {'brand': 'Takahashi', 'name': 'M92→M54 Adapter', 'type': 'type_adapter', 'optical_length': 12, 'mass': 50, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M82_M72_Adapter': {'brand': 'Takahashi', 'name': 'M82→M72 Adapter', 'type': 'type_adapter', 'optical_length': 6, 'mass': 45, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M82_M42_Adapter': {'brand': 'Takahashi', 'name': 'M82→M42 Adapter', 'type': 'type_adapter', 'optical_length': 12, 'mass': 35, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M54_Nikon_F_Adapter': {'brand': 'Takahashi', 'name': 'M54→Nikon F Adapter', 'type': 'type_adapter', 'optical_length': 8, 'mass': 35, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M54_Sony_E_Adapter': {'brand': 'Takahashi', 'name': 'M54→Sony E Adapter', 'type': 'type_adapter', 'optical_length': 7, 'mass': 30, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M54_Canon_RF_Adapter': {'brand': 'Takahashi', 'name': 'M54→Canon RF Adapter', 'type': 'type_adapter', 'optical_length': 5, 'mass': 28, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M42_Spacer_3mm': {'brand': 'Takahashi', 'name': 'M42 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M54_Spacer_3mm': {'brand': 'Takahashi', 'name': 'M54 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 10, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M72_Spacer_15mm': {'brand': 'Takahashi', 'name': 'M72 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 24, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M92_Spacer_5mm': {'brand': 'Takahashi', 'name': 'M92 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 20, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M92_Spacer_10mm': {'brand': 'Takahashi', 'name': 'M92 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 24, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M92_Spacer_15mm': {'brand': 'Takahashi', 'name': 'M92 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 28, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M92_Spacer_20mm': {'brand': 'Takahashi', 'name': 'M92 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 32, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M42_Spacer_2_5mm': {'brand': 'Takahashi', 'name': 'M42 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M42_Spacer_3_5mm': {'brand': 'Takahashi', 'name': 'M42 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M42_Spacer_4mm': {'brand': 'Takahashi', 'name': 'M42 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 7, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M42_Spacer_4_5mm': {'brand': 'Takahashi', 'name': 'M42 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 7, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M42_Spacer_5_5mm': {'brand': 'Takahashi', 'name': 'M42 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 8, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M42_Spacer_6mm': {'brand': 'Takahashi', 'name': 'M42 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 8, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M42_Spacer_6_5mm': {'brand': 'Takahashi', 'name': 'M42 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 9, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M42_Spacer_7mm': {'brand': 'Takahashi', 'name': 'M42 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 9, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M42_Spacer_7_5mm': {'brand': 'Takahashi', 'name': 'M42 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 10, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M42_Spacer_8mm': {'brand': 'Takahashi', 'name': 'M42 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 10, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M42_Spacer_8_5mm': {'brand': 'Takahashi', 'name': 'M42 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 10, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M42_Spacer_9mm': {'brand': 'Takahashi', 'name': 'M42 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 11, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M42_Spacer_9_5mm': {'brand': 'Takahashi', 'name': 'M42 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 11, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M42_Spacer_11mm': {'brand': 'Takahashi', 'name': 'M42 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 12, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M42_Spacer_12mm': {'brand': 'Takahashi', 'name': 'M42 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 13, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M42_Spacer_13mm': {'brand': 'Takahashi', 'name': 'M42 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 14, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M42_Spacer_14mm': {'brand': 'Takahashi', 'name': 'M42 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 15, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M42_Spacer_16mm': {'brand': 'Takahashi', 'name': 'M42 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M42_Spacer_17mm': {'brand': 'Takahashi', 'name': 'M42 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 17, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M42_Spacer_18mm': {'brand': 'Takahashi', 'name': 'M42 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 18, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M42_Spacer_22mm': {'brand': 'Takahashi', 'name': 'M42 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 21, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M42_Spacer_25mm': {'brand': 'Takahashi', 'name': 'M42 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 24, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M54_Spacer_2_5mm': {'brand': 'Takahashi', 'name': 'M54 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 10, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M54_Spacer_3_5mm': {'brand': 'Takahashi', 'name': 'M54 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 10, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M54_Spacer_4mm': {'brand': 'Takahashi', 'name': 'M54 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 11, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M54_Spacer_4_5mm': {'brand': 'Takahashi', 'name': 'M54 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 11, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M54_Spacer_5_5mm': {'brand': 'Takahashi', 'name': 'M54 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 12, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M54_Spacer_6mm': {'brand': 'Takahashi', 'name': 'M54 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 12, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M54_Spacer_6_5mm': {'brand': 'Takahashi', 'name': 'M54 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 13, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M54_Spacer_7mm': {'brand': 'Takahashi', 'name': 'M54 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 13, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M54_Spacer_7_5mm': {'brand': 'Takahashi', 'name': 'M54 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 14, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M54_Spacer_8mm': {'brand': 'Takahashi', 'name': 'M54 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 14, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M54_Spacer_8_5mm': {'brand': 'Takahashi', 'name': 'M54 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 14, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M54_Spacer_9mm': {'brand': 'Takahashi', 'name': 'M54 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 15, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M54_Spacer_9_5mm': {'brand': 'Takahashi', 'name': 'M54 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 15, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M54_Spacer_11mm': {'brand': 'Takahashi', 'name': 'M54 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 16, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M54_Spacer_12mm': {'brand': 'Takahashi', 'name': 'M54 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 17, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M54_Spacer_13mm': {'brand': 'Takahashi', 'name': 'M54 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 18, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M54_Spacer_14mm': {'brand': 'Takahashi', 'name': 'M54 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 19, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M54_Spacer_16mm': {'brand': 'Takahashi', 'name': 'M54 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 20, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M54_Spacer_17mm': {'brand': 'Takahashi', 'name': 'M54 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 21, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M54_Spacer_18mm': {'brand': 'Takahashi', 'name': 'M54 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 22, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M54_Spacer_22mm': {'brand': 'Takahashi', 'name': 'M54 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 25, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M54_Spacer_25mm': {'brand': 'Takahashi', 'name': 'M54 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 28, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M72_Spacer_2_5mm': {'brand': 'Takahashi', 'name': 'M72 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 14, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M72_Spacer_3mm': {'brand': 'Takahashi', 'name': 'M72 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 14, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M72_Spacer_3_5mm': {'brand': 'Takahashi', 'name': 'M72 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 14, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M72_Spacer_4mm': {'brand': 'Takahashi', 'name': 'M72 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 15, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M72_Spacer_4_5mm': {'brand': 'Takahashi', 'name': 'M72 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 15, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M72_Spacer_5_5mm': {'brand': 'Takahashi', 'name': 'M72 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 16, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M72_Spacer_6mm': {'brand': 'Takahashi', 'name': 'M72 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 16, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M72_Spacer_6_5mm': {'brand': 'Takahashi', 'name': 'M72 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 17, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M72_Spacer_7mm': {'brand': 'Takahashi', 'name': 'M72 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 17, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M72_Spacer_7_5mm': {'brand': 'Takahashi', 'name': 'M72 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 18, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M72_Spacer_8mm': {'brand': 'Takahashi', 'name': 'M72 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 18, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M72_Spacer_8_5mm': {'brand': 'Takahashi', 'name': 'M72 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 18, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M72_Spacer_9mm': {'brand': 'Takahashi', 'name': 'M72 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 19, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M72_Spacer_9_5mm': {'brand': 'Takahashi', 'name': 'M72 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 19, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M72_Spacer_11mm': {'brand': 'Takahashi', 'name': 'M72 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 20, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M72_Spacer_12mm': {'brand': 'Takahashi', 'name': 'M72 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 21, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M72_Spacer_13mm': {'brand': 'Takahashi', 'name': 'M72 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 22, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M72_Spacer_16mm': {'brand': 'Takahashi', 'name': 'M72 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 24, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M72_Spacer_17mm': {'brand': 'Takahashi', 'name': 'M72 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 25, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M72_Spacer_18mm': {'brand': 'Takahashi', 'name': 'M72 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 26, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M72_Spacer_22mm': {'brand': 'Takahashi', 'name': 'M72 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 29, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M72_Spacer_25mm': {'brand': 'Takahashi', 'name': 'M72 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 32, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M82_Spacer_2_5mm': {'brand': 'Takahashi', 'name': 'M82 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 17, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M82_Spacer_3mm': {'brand': 'Takahashi', 'name': 'M82 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 17, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M82_Spacer_3_5mm': {'brand': 'Takahashi', 'name': 'M82 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 17, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M82_Spacer_4mm': {'brand': 'Takahashi', 'name': 'M82 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 18, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M82_Spacer_4_5mm': {'brand': 'Takahashi', 'name': 'M82 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 18, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M82_Spacer_5_5mm': {'brand': 'Takahashi', 'name': 'M82 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 19, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M82_Spacer_6mm': {'brand': 'Takahashi', 'name': 'M82 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 19, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M82_Spacer_6_5mm': {'brand': 'Takahashi', 'name': 'M82 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 20, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M82_Spacer_7mm': {'brand': 'Takahashi', 'name': 'M82 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 20, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M82_Spacer_7_5mm': {'brand': 'Takahashi', 'name': 'M82 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 21, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M82_Spacer_8mm': {'brand': 'Takahashi', 'name': 'M82 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 21, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M82_Spacer_8_5mm': {'brand': 'Takahashi', 'name': 'M82 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 21, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M82_Spacer_9mm': {'brand': 'Takahashi', 'name': 'M82 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 22, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M82_Spacer_9_5mm': {'brand': 'Takahashi', 'name': 'M82 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 22, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M82_Spacer_11mm': {'brand': 'Takahashi', 'name': 'M82 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 23, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M82_Spacer_12mm': {'brand': 'Takahashi', 'name': 'M82 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 24, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M82_Spacer_13mm': {'brand': 'Takahashi', 'name': 'M82 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 25, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M82_Spacer_14mm': {'brand': 'Takahashi', 'name': 'M82 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 26, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M82_Spacer_16mm': {'brand': 'Takahashi', 'name': 'M82 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 27, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M82_Spacer_17mm': {'brand': 'Takahashi', 'name': 'M82 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 28, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M82_Spacer_18mm': {'brand': 'Takahashi', 'name': 'M82 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 29, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M82_Spacer_22mm': {'brand': 'Takahashi', 'name': 'M82 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 32, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M82_Spacer_25mm': {'brand': 'Takahashi', 'name': 'M82 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 35, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M92_Spacer_2_5mm': {'brand': 'Takahashi', 'name': 'M92 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 18, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M92_Spacer_3mm': {'brand': 'Takahashi', 'name': 'M92 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 18, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M92_Spacer_3_5mm': {'brand': 'Takahashi', 'name': 'M92 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 18, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M92_Spacer_4mm': {'brand': 'Takahashi', 'name': 'M92 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 19, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M92_Spacer_4_5mm': {'brand': 'Takahashi', 'name': 'M92 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 19, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M92_Spacer_5_5mm': {'brand': 'Takahashi', 'name': 'M92 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 20, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M92_Spacer_6mm': {'brand': 'Takahashi', 'name': 'M92 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 20, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M92_Spacer_6_5mm': {'brand': 'Takahashi', 'name': 'M92 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 21, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M92_Spacer_7mm': {'brand': 'Takahashi', 'name': 'M92 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 21, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M92_Spacer_7_5mm': {'brand': 'Takahashi', 'name': 'M92 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 22, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M92_Spacer_8mm': {'brand': 'Takahashi', 'name': 'M92 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 22, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M92_Spacer_8_5mm': {'brand': 'Takahashi', 'name': 'M92 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 22, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M92_Spacer_9mm': {'brand': 'Takahashi', 'name': 'M92 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 23, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M92_Spacer_9_5mm': {'brand': 'Takahashi', 'name': 'M92 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 23, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M92_Spacer_11mm': {'brand': 'Takahashi', 'name': 'M92 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 24, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M92_Spacer_12mm': {'brand': 'Takahashi', 'name': 'M92 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 25, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M92_Spacer_13mm': {'brand': 'Takahashi', 'name': 'M92 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 26, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M92_Spacer_14mm': {'brand': 'Takahashi', 'name': 'M92 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 27, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M92_Spacer_16mm': {'brand': 'Takahashi', 'name': 'M92 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 28, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M92_Spacer_17mm': {'brand': 'Takahashi', 'name': 'M92 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 29, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M92_Spacer_18mm': {'brand': 'Takahashi', 'name': 'M92 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 30, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M92_Spacer_22mm': {'brand': 'Takahashi', 'name': 'M92 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 33, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M92_Spacer_25mm': {'brand': 'Takahashi', 'name': 'M92 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 36, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M42_Extension_Tube_3mm': {'brand': 'Takahashi', 'name': 'M42 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 15, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M42_Extension_Tube_6mm': {'brand': 'Takahashi', 'name': 'M42 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M42_Extension_Tube_9mm': {'brand': 'Takahashi', 'name': 'M42 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 17, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M42_Extension_Tube_11mm': {'brand': 'Takahashi', 'name': 'M42 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 18, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M42_Extension_Tube_13mm': {'brand': 'Takahashi', 'name': 'M42 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 18, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M42_Extension_Tube_16mm': {'brand': 'Takahashi', 'name': 'M42 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 19, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M42_Extension_Tube_22mm': {'brand': 'Takahashi', 'name': 'M42 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 21, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M42_Extension_Tube_28mm': {'brand': 'Takahashi', 'name': 'M42 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 23, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M42_Extension_Tube_35mm': {'brand': 'Takahashi', 'name': 'M42 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 25, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M42_Extension_Tube_45mm': {'brand': 'Takahashi', 'name': 'M42 Extension Tube 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 28, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M48_Extension_Tube_3mm': {'brand': 'Takahashi', 'name': 'M48 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 19, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M48_Extension_Tube_6mm': {'brand': 'Takahashi', 'name': 'M48 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 20, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M48_Extension_Tube_9mm': {'brand': 'Takahashi', 'name': 'M48 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 21, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M48_Extension_Tube_11mm': {'brand': 'Takahashi', 'name': 'M48 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 22, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M48_Extension_Tube_13mm': {'brand': 'Takahashi', 'name': 'M48 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 22, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M48_Extension_Tube_16mm': {'brand': 'Takahashi', 'name': 'M48 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 23, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M48_Extension_Tube_22mm': {'brand': 'Takahashi', 'name': 'M48 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 25, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M48_Extension_Tube_28mm': {'brand': 'Takahashi', 'name': 'M48 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 27, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M48_Extension_Tube_35mm': {'brand': 'Takahashi', 'name': 'M48 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 29, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M48_Extension_Tube_45mm': {'brand': 'Takahashi', 'name': 'M48 Extension Tube 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 32, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M54_Extension_Tube_3mm': {'brand': 'Takahashi', 'name': 'M54 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 23, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M54_Extension_Tube_6mm': {'brand': 'Takahashi', 'name': 'M54 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 24, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M54_Extension_Tube_9mm': {'brand': 'Takahashi', 'name': 'M54 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 25, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M54_Extension_Tube_11mm': {'brand': 'Takahashi', 'name': 'M54 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 26, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M54_Extension_Tube_13mm': {'brand': 'Takahashi', 'name': 'M54 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 26, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M54_Extension_Tube_16mm': {'brand': 'Takahashi', 'name': 'M54 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 27, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M54_Extension_Tube_22mm': {'brand': 'Takahashi', 'name': 'M54 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 29, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M54_Extension_Tube_28mm': {'brand': 'Takahashi', 'name': 'M54 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 31, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M54_Extension_Tube_35mm': {'brand': 'Takahashi', 'name': 'M54 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 33, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M54_Extension_Tube_45mm': {'brand': 'Takahashi', 'name': 'M54 Extension Tube 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 36, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M68_Extension_Tube_3mm': {'brand': 'Takahashi', 'name': 'M68 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 18, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M68_Extension_Tube_5mm': {'brand': 'Takahashi', 'name': 'M68 Extension Tube 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 19, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M68_Extension_Tube_6mm': {'brand': 'Takahashi', 'name': 'M68 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 19, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M68_Extension_Tube_8mm': {'brand': 'Takahashi', 'name': 'M68 Extension Tube 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 20, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M68_Extension_Tube_9mm': {'brand': 'Takahashi', 'name': 'M68 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 20, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M68_Extension_Tube_11mm': {'brand': 'Takahashi', 'name': 'M68 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 21, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M68_Extension_Tube_13mm': {'brand': 'Takahashi', 'name': 'M68 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 21, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M68_Extension_Tube_14mm': {'brand': 'Takahashi', 'name': 'M68 Extension Tube 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 22, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M68_Extension_Tube_16mm': {'brand': 'Takahashi', 'name': 'M68 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 22, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M68_Extension_Tube_18mm': {'brand': 'Takahashi', 'name': 'M68 Extension Tube 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 23, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M68_Extension_Tube_22mm': {'brand': 'Takahashi', 'name': 'M68 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 24, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M68_Extension_Tube_25mm': {'brand': 'Takahashi', 'name': 'M68 Extension Tube 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 25, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M68_Extension_Tube_28mm': {'brand': 'Takahashi', 'name': 'M68 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 26, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M68_Extension_Tube_30mm': {'brand': 'Takahashi', 'name': 'M68 Extension Tube 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 27, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M68_Extension_Tube_35mm': {'brand': 'Takahashi', 'name': 'M68 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 28, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M72_Extension_Tube_3mm': {'brand': 'Takahashi', 'name': 'M72 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 20, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M72_Extension_Tube_5mm': {'brand': 'Takahashi', 'name': 'M72 Extension Tube 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 21, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M72_Extension_Tube_8mm': {'brand': 'Takahashi', 'name': 'M72 Extension Tube 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 22, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M72_Extension_Tube_10mm': {'brand': 'Takahashi', 'name': 'M72 Extension Tube 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 23, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M72_Extension_Tube_12mm': {'brand': 'Takahashi', 'name': 'M72 Extension Tube 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 23, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M72_Extension_Tube_15mm': {'brand': 'Takahashi', 'name': 'M72 Extension Tube 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 24, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M72_Extension_Tube_18mm': {'brand': 'Takahashi', 'name': 'M72 Extension Tube 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 25, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M72_Extension_Tube_20mm': {'brand': 'Takahashi', 'name': 'M72 Extension Tube 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 26, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M72_Extension_Tube_25mm': {'brand': 'Takahashi', 'name': 'M72 Extension Tube 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 27, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M72_Extension_Tube_30mm': {'brand': 'Takahashi', 'name': 'M72 Extension Tube 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 29, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M82_Extension_Tube_3mm': {'brand': 'Takahashi', 'name': 'M82 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 24, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M82_Extension_Tube_5mm': {'brand': 'Takahashi', 'name': 'M82 Extension Tube 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 25, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M82_Extension_Tube_8mm': {'brand': 'Takahashi', 'name': 'M82 Extension Tube 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 26, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M82_Extension_Tube_10mm': {'brand': 'Takahashi', 'name': 'M82 Extension Tube 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 27, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M82_Extension_Tube_12mm': {'brand': 'Takahashi', 'name': 'M82 Extension Tube 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 27, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M82_Extension_Tube_15mm': {'brand': 'Takahashi', 'name': 'M82 Extension Tube 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 28, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M82_Extension_Tube_18mm': {'brand': 'Takahashi', 'name': 'M82 Extension Tube 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 29, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M82_Extension_Tube_20mm': {'brand': 'Takahashi', 'name': 'M82 Extension Tube 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 30, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M82_Extension_Tube_25mm': {'brand': 'Takahashi', 'name': 'M82 Extension Tube 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 31, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M82_Extension_Tube_30mm': {'brand': 'Takahashi', 'name': 'M82 Extension Tube 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 33, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Takahashi_M92_Spacer_28mm': {'brand': 'Takahashi', 'name': 'M92 Spacer 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 38, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Takahashi_M92_Spacer_30mm': {'brand': 'Takahashi', 'name': 'M92 Spacer 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 40, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}}

    @classmethod
    def Takahashi_CA_35_M82_M54(cls):
        return cls.from_database(cls._DATABASE['Takahashi_CA_35_M82_M54'])

    @classmethod
    def Takahashi_DX_WR_Wide_Ring_M72(cls):
        return cls.from_database(cls._DATABASE['Takahashi_DX_WR_Wide_Ring_M72'])

    @classmethod
    def Takahashi_M72_M82_Adapter(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_M82_Adapter'])

    @classmethod
    def Takahashi_M82_M54_Adapter(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_M54_Adapter'])

    @classmethod
    def Takahashi_M92_M82_Adapter(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M92_M82_Adapter'])

    @classmethod
    def Takahashi_M54_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_M42_Adapter'])

    @classmethod
    def Takahashi_Wide_T_Adapter_M42(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Wide_T_Adapter_M42'])

    @classmethod
    def Takahashi_M72_M54_Adapter(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_M54_Adapter'])

    @classmethod
    def Takahashi_M92_M72_Adapter(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M92_M72_Adapter'])

    @classmethod
    def Takahashi_M42_EOS_Adapter(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_EOS_Adapter'])

    @classmethod
    def Takahashi_M42_Nikon_F_Adapter(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Nikon_F_Adapter'])

    @classmethod
    def Takahashi_M42_Sony_E_Adapter(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Sony_E_Adapter'])

    @classmethod
    def Takahashi_M42_Canon_RF_Adapter(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Canon_RF_Adapter'])

    @classmethod
    def Takahashi_M72_M68_Adapter(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_M68_Adapter'])

    @classmethod
    def Takahashi_DX_60W_Camera_Mount_EOS(cls):
        return cls.from_database(cls._DATABASE['Takahashi_DX_60W_Camera_Mount_EOS'])

    @classmethod
    def Takahashi_DX_WR_Camera_Mount_EOS(cls):
        return cls.from_database(cls._DATABASE['Takahashi_DX_WR_Camera_Mount_EOS'])

    @classmethod
    def Takahashi_CA_35_SKY90(cls):
        return cls.from_database(cls._DATABASE['Takahashi_CA_35_SKY90'])

    @classmethod
    def Takahashi_Multi_CA_Ring_76(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Multi_CA_Ring_76'])

    @classmethod
    def Takahashi_M42_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Spacer_5mm'])

    @classmethod
    def Takahashi_M42_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Spacer_10mm'])

    @classmethod
    def Takahashi_M42_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Spacer_15mm'])

    @classmethod
    def Takahashi_M54_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Spacer_5mm'])

    @classmethod
    def Takahashi_M54_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Spacer_10mm'])

    @classmethod
    def Takahashi_M54_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Spacer_15mm'])

    @classmethod
    def Takahashi_M72_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_Spacer_5mm'])

    @classmethod
    def Takahashi_M72_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_Spacer_10mm'])

    @classmethod
    def Takahashi_M82_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_Spacer_5mm'])

    @classmethod
    def Takahashi_M82_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_Spacer_10mm'])

    @classmethod
    def Takahashi_M82_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_Spacer_15mm'])

    @classmethod
    def Takahashi_M82_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_Spacer_20mm'])

    @classmethod
    def Takahashi_M54_EOS_Adapter_CA_35EOS(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_EOS_Adapter_CA_35EOS'])

    @classmethod
    def Takahashi_M42_M54_Adapter(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_M54_Adapter'])

    @classmethod
    def Takahashi_M92_M54_Adapter(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M92_M54_Adapter'])

    @classmethod
    def Takahashi_M82_M72_Adapter(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_M72_Adapter'])

    @classmethod
    def Takahashi_M82_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_M42_Adapter'])

    @classmethod
    def Takahashi_M54_Nikon_F_Adapter(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Nikon_F_Adapter'])

    @classmethod
    def Takahashi_M54_Sony_E_Adapter(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Sony_E_Adapter'])

    @classmethod
    def Takahashi_M54_Canon_RF_Adapter(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Canon_RF_Adapter'])

    @classmethod
    def Takahashi_M42_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Spacer_3mm'])

    @classmethod
    def Takahashi_M54_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Spacer_3mm'])

    @classmethod
    def Takahashi_M72_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_Spacer_15mm'])

    @classmethod
    def Takahashi_M92_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M92_Spacer_5mm'])

    @classmethod
    def Takahashi_M92_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M92_Spacer_10mm'])

    @classmethod
    def Takahashi_M92_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M92_Spacer_15mm'])

    @classmethod
    def Takahashi_M92_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M92_Spacer_20mm'])

    @classmethod
    def Takahashi_M42_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Spacer_2_5mm'])

    @classmethod
    def Takahashi_M42_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Spacer_3_5mm'])

    @classmethod
    def Takahashi_M42_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Spacer_4mm'])

    @classmethod
    def Takahashi_M42_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Spacer_4_5mm'])

    @classmethod
    def Takahashi_M42_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Spacer_5_5mm'])

    @classmethod
    def Takahashi_M42_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Spacer_6mm'])

    @classmethod
    def Takahashi_M42_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Spacer_6_5mm'])

    @classmethod
    def Takahashi_M42_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Spacer_7mm'])

    @classmethod
    def Takahashi_M42_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Spacer_7_5mm'])

    @classmethod
    def Takahashi_M42_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Spacer_8mm'])

    @classmethod
    def Takahashi_M42_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Spacer_8_5mm'])

    @classmethod
    def Takahashi_M42_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Spacer_9mm'])

    @classmethod
    def Takahashi_M42_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Spacer_9_5mm'])

    @classmethod
    def Takahashi_M42_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Spacer_11mm'])

    @classmethod
    def Takahashi_M42_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Spacer_12mm'])

    @classmethod
    def Takahashi_M42_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Spacer_13mm'])

    @classmethod
    def Takahashi_M42_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Spacer_14mm'])

    @classmethod
    def Takahashi_M42_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Spacer_16mm'])

    @classmethod
    def Takahashi_M42_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Spacer_17mm'])

    @classmethod
    def Takahashi_M42_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Spacer_18mm'])

    @classmethod
    def Takahashi_M42_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Spacer_22mm'])

    @classmethod
    def Takahashi_M42_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Spacer_25mm'])

    @classmethod
    def Takahashi_M54_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Spacer_2_5mm'])

    @classmethod
    def Takahashi_M54_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Spacer_3_5mm'])

    @classmethod
    def Takahashi_M54_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Spacer_4mm'])

    @classmethod
    def Takahashi_M54_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Spacer_4_5mm'])

    @classmethod
    def Takahashi_M54_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Spacer_5_5mm'])

    @classmethod
    def Takahashi_M54_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Spacer_6mm'])

    @classmethod
    def Takahashi_M54_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Spacer_6_5mm'])

    @classmethod
    def Takahashi_M54_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Spacer_7mm'])

    @classmethod
    def Takahashi_M54_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Spacer_7_5mm'])

    @classmethod
    def Takahashi_M54_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Spacer_8mm'])

    @classmethod
    def Takahashi_M54_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Spacer_8_5mm'])

    @classmethod
    def Takahashi_M54_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Spacer_9mm'])

    @classmethod
    def Takahashi_M54_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Spacer_9_5mm'])

    @classmethod
    def Takahashi_M54_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Spacer_11mm'])

    @classmethod
    def Takahashi_M54_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Spacer_12mm'])

    @classmethod
    def Takahashi_M54_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Spacer_13mm'])

    @classmethod
    def Takahashi_M54_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Spacer_14mm'])

    @classmethod
    def Takahashi_M54_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Spacer_16mm'])

    @classmethod
    def Takahashi_M54_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Spacer_17mm'])

    @classmethod
    def Takahashi_M54_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Spacer_18mm'])

    @classmethod
    def Takahashi_M54_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Spacer_22mm'])

    @classmethod
    def Takahashi_M54_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Spacer_25mm'])

    @classmethod
    def Takahashi_M72_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_Spacer_2_5mm'])

    @classmethod
    def Takahashi_M72_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_Spacer_3mm'])

    @classmethod
    def Takahashi_M72_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_Spacer_3_5mm'])

    @classmethod
    def Takahashi_M72_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_Spacer_4mm'])

    @classmethod
    def Takahashi_M72_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_Spacer_4_5mm'])

    @classmethod
    def Takahashi_M72_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_Spacer_5_5mm'])

    @classmethod
    def Takahashi_M72_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_Spacer_6mm'])

    @classmethod
    def Takahashi_M72_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_Spacer_6_5mm'])

    @classmethod
    def Takahashi_M72_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_Spacer_7mm'])

    @classmethod
    def Takahashi_M72_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_Spacer_7_5mm'])

    @classmethod
    def Takahashi_M72_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_Spacer_8mm'])

    @classmethod
    def Takahashi_M72_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_Spacer_8_5mm'])

    @classmethod
    def Takahashi_M72_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_Spacer_9mm'])

    @classmethod
    def Takahashi_M72_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_Spacer_9_5mm'])

    @classmethod
    def Takahashi_M72_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_Spacer_11mm'])

    @classmethod
    def Takahashi_M72_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_Spacer_12mm'])

    @classmethod
    def Takahashi_M72_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_Spacer_13mm'])

    @classmethod
    def Takahashi_M72_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_Spacer_16mm'])

    @classmethod
    def Takahashi_M72_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_Spacer_17mm'])

    @classmethod
    def Takahashi_M72_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_Spacer_18mm'])

    @classmethod
    def Takahashi_M72_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_Spacer_22mm'])

    @classmethod
    def Takahashi_M72_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_Spacer_25mm'])

    @classmethod
    def Takahashi_M82_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_Spacer_2_5mm'])

    @classmethod
    def Takahashi_M82_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_Spacer_3mm'])

    @classmethod
    def Takahashi_M82_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_Spacer_3_5mm'])

    @classmethod
    def Takahashi_M82_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_Spacer_4mm'])

    @classmethod
    def Takahashi_M82_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_Spacer_4_5mm'])

    @classmethod
    def Takahashi_M82_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_Spacer_5_5mm'])

    @classmethod
    def Takahashi_M82_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_Spacer_6mm'])

    @classmethod
    def Takahashi_M82_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_Spacer_6_5mm'])

    @classmethod
    def Takahashi_M82_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_Spacer_7mm'])

    @classmethod
    def Takahashi_M82_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_Spacer_7_5mm'])

    @classmethod
    def Takahashi_M82_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_Spacer_8mm'])

    @classmethod
    def Takahashi_M82_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_Spacer_8_5mm'])

    @classmethod
    def Takahashi_M82_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_Spacer_9mm'])

    @classmethod
    def Takahashi_M82_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_Spacer_9_5mm'])

    @classmethod
    def Takahashi_M82_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_Spacer_11mm'])

    @classmethod
    def Takahashi_M82_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_Spacer_12mm'])

    @classmethod
    def Takahashi_M82_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_Spacer_13mm'])

    @classmethod
    def Takahashi_M82_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_Spacer_14mm'])

    @classmethod
    def Takahashi_M82_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_Spacer_16mm'])

    @classmethod
    def Takahashi_M82_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_Spacer_17mm'])

    @classmethod
    def Takahashi_M82_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_Spacer_18mm'])

    @classmethod
    def Takahashi_M82_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_Spacer_22mm'])

    @classmethod
    def Takahashi_M82_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_Spacer_25mm'])

    @classmethod
    def Takahashi_M92_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M92_Spacer_2_5mm'])

    @classmethod
    def Takahashi_M92_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M92_Spacer_3mm'])

    @classmethod
    def Takahashi_M92_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M92_Spacer_3_5mm'])

    @classmethod
    def Takahashi_M92_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M92_Spacer_4mm'])

    @classmethod
    def Takahashi_M92_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M92_Spacer_4_5mm'])

    @classmethod
    def Takahashi_M92_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M92_Spacer_5_5mm'])

    @classmethod
    def Takahashi_M92_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M92_Spacer_6mm'])

    @classmethod
    def Takahashi_M92_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M92_Spacer_6_5mm'])

    @classmethod
    def Takahashi_M92_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M92_Spacer_7mm'])

    @classmethod
    def Takahashi_M92_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M92_Spacer_7_5mm'])

    @classmethod
    def Takahashi_M92_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M92_Spacer_8mm'])

    @classmethod
    def Takahashi_M92_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M92_Spacer_8_5mm'])

    @classmethod
    def Takahashi_M92_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M92_Spacer_9mm'])

    @classmethod
    def Takahashi_M92_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M92_Spacer_9_5mm'])

    @classmethod
    def Takahashi_M92_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M92_Spacer_11mm'])

    @classmethod
    def Takahashi_M92_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M92_Spacer_12mm'])

    @classmethod
    def Takahashi_M92_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M92_Spacer_13mm'])

    @classmethod
    def Takahashi_M92_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M92_Spacer_14mm'])

    @classmethod
    def Takahashi_M92_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M92_Spacer_16mm'])

    @classmethod
    def Takahashi_M92_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M92_Spacer_17mm'])

    @classmethod
    def Takahashi_M92_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M92_Spacer_18mm'])

    @classmethod
    def Takahashi_M92_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M92_Spacer_22mm'])

    @classmethod
    def Takahashi_M92_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M92_Spacer_25mm'])

    @classmethod
    def Takahashi_M42_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Extension_Tube_3mm'])

    @classmethod
    def Takahashi_M42_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Extension_Tube_6mm'])

    @classmethod
    def Takahashi_M42_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Extension_Tube_9mm'])

    @classmethod
    def Takahashi_M42_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Extension_Tube_11mm'])

    @classmethod
    def Takahashi_M42_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Extension_Tube_13mm'])

    @classmethod
    def Takahashi_M42_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Extension_Tube_16mm'])

    @classmethod
    def Takahashi_M42_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Extension_Tube_22mm'])

    @classmethod
    def Takahashi_M42_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Extension_Tube_28mm'])

    @classmethod
    def Takahashi_M42_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Extension_Tube_35mm'])

    @classmethod
    def Takahashi_M42_Extension_Tube_45mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Extension_Tube_45mm'])

    @classmethod
    def Takahashi_M48_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M48_Extension_Tube_3mm'])

    @classmethod
    def Takahashi_M48_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M48_Extension_Tube_6mm'])

    @classmethod
    def Takahashi_M48_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M48_Extension_Tube_9mm'])

    @classmethod
    def Takahashi_M48_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M48_Extension_Tube_11mm'])

    @classmethod
    def Takahashi_M48_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M48_Extension_Tube_13mm'])

    @classmethod
    def Takahashi_M48_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M48_Extension_Tube_16mm'])

    @classmethod
    def Takahashi_M48_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M48_Extension_Tube_22mm'])

    @classmethod
    def Takahashi_M48_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M48_Extension_Tube_28mm'])

    @classmethod
    def Takahashi_M48_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M48_Extension_Tube_35mm'])

    @classmethod
    def Takahashi_M48_Extension_Tube_45mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M48_Extension_Tube_45mm'])

    @classmethod
    def Takahashi_M54_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Extension_Tube_3mm'])

    @classmethod
    def Takahashi_M54_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Extension_Tube_6mm'])

    @classmethod
    def Takahashi_M54_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Extension_Tube_9mm'])

    @classmethod
    def Takahashi_M54_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Extension_Tube_11mm'])

    @classmethod
    def Takahashi_M54_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Extension_Tube_13mm'])

    @classmethod
    def Takahashi_M54_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Extension_Tube_16mm'])

    @classmethod
    def Takahashi_M54_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Extension_Tube_22mm'])

    @classmethod
    def Takahashi_M54_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Extension_Tube_28mm'])

    @classmethod
    def Takahashi_M54_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Extension_Tube_35mm'])

    @classmethod
    def Takahashi_M54_Extension_Tube_45mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Extension_Tube_45mm'])

    @classmethod
    def Takahashi_M68_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M68_Extension_Tube_3mm'])

    @classmethod
    def Takahashi_M68_Extension_Tube_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M68_Extension_Tube_5mm'])

    @classmethod
    def Takahashi_M68_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M68_Extension_Tube_6mm'])

    @classmethod
    def Takahashi_M68_Extension_Tube_8mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M68_Extension_Tube_8mm'])

    @classmethod
    def Takahashi_M68_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M68_Extension_Tube_9mm'])

    @classmethod
    def Takahashi_M68_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M68_Extension_Tube_11mm'])

    @classmethod
    def Takahashi_M68_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M68_Extension_Tube_13mm'])

    @classmethod
    def Takahashi_M68_Extension_Tube_14mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M68_Extension_Tube_14mm'])

    @classmethod
    def Takahashi_M68_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M68_Extension_Tube_16mm'])

    @classmethod
    def Takahashi_M68_Extension_Tube_18mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M68_Extension_Tube_18mm'])

    @classmethod
    def Takahashi_M68_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M68_Extension_Tube_22mm'])

    @classmethod
    def Takahashi_M68_Extension_Tube_25mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M68_Extension_Tube_25mm'])

    @classmethod
    def Takahashi_M68_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M68_Extension_Tube_28mm'])

    @classmethod
    def Takahashi_M68_Extension_Tube_30mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M68_Extension_Tube_30mm'])

    @classmethod
    def Takahashi_M68_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M68_Extension_Tube_35mm'])

    @classmethod
    def Takahashi_M72_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_Extension_Tube_3mm'])

    @classmethod
    def Takahashi_M72_Extension_Tube_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_Extension_Tube_5mm'])

    @classmethod
    def Takahashi_M72_Extension_Tube_8mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_Extension_Tube_8mm'])

    @classmethod
    def Takahashi_M72_Extension_Tube_10mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_Extension_Tube_10mm'])

    @classmethod
    def Takahashi_M72_Extension_Tube_12mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_Extension_Tube_12mm'])

    @classmethod
    def Takahashi_M72_Extension_Tube_15mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_Extension_Tube_15mm'])

    @classmethod
    def Takahashi_M72_Extension_Tube_18mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_Extension_Tube_18mm'])

    @classmethod
    def Takahashi_M72_Extension_Tube_20mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_Extension_Tube_20mm'])

    @classmethod
    def Takahashi_M72_Extension_Tube_25mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_Extension_Tube_25mm'])

    @classmethod
    def Takahashi_M72_Extension_Tube_30mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_Extension_Tube_30mm'])

    @classmethod
    def Takahashi_M82_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_Extension_Tube_3mm'])

    @classmethod
    def Takahashi_M82_Extension_Tube_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_Extension_Tube_5mm'])

    @classmethod
    def Takahashi_M82_Extension_Tube_8mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_Extension_Tube_8mm'])

    @classmethod
    def Takahashi_M82_Extension_Tube_10mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_Extension_Tube_10mm'])

    @classmethod
    def Takahashi_M82_Extension_Tube_12mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_Extension_Tube_12mm'])

    @classmethod
    def Takahashi_M82_Extension_Tube_15mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_Extension_Tube_15mm'])

    @classmethod
    def Takahashi_M82_Extension_Tube_18mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_Extension_Tube_18mm'])

    @classmethod
    def Takahashi_M82_Extension_Tube_20mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_Extension_Tube_20mm'])

    @classmethod
    def Takahashi_M82_Extension_Tube_25mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_Extension_Tube_25mm'])

    @classmethod
    def Takahashi_M82_Extension_Tube_30mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_Extension_Tube_30mm'])

    @classmethod
    def Takahashi_M92_Spacer_28mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M92_Spacer_28mm'])

    @classmethod
    def Takahashi_M92_Spacer_30mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M92_Spacer_30mm'])

class TakahashiSpacer(Spacer):
    _DATABASE = {'Takahashi_M42_Spacer_1mm': {'brand': 'Takahashi', 'name': 'M42 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Takahashi_M42_Spacer_2mm': {'brand': 'Takahashi', 'name': 'M42 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Takahashi_M54_Spacer_1mm': {'brand': 'Takahashi', 'name': 'M54 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Takahashi_M54_Spacer_2mm': {'brand': 'Takahashi', 'name': 'M54 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Takahashi_M72_Spacer_1mm': {'brand': 'Takahashi', 'name': 'M72 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 13, 'tside_thread': 'M72', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Takahashi_M72_Spacer_2mm': {'brand': 'Takahashi', 'name': 'M72 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 13, 'tside_thread': 'M72', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Takahashi_M82_Spacer_2mm': {'brand': 'Takahashi', 'name': 'M82 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 16, 'tside_thread': 'M82', 'tside_gender': '', 'cside_thread': 'M82', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Takahashi_M42_Spacer_0_5mm': {'brand': 'Takahashi', 'name': 'M42 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Takahashi_M42_Spacer_0_7mm': {'brand': 'Takahashi', 'name': 'M42 Spacer 0.7mm', 'type': 'type_spacer', 'optical_length': 0.7, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Takahashi_M42_Spacer_1_5mm': {'brand': 'Takahashi', 'name': 'M42 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Takahashi_M54_Spacer_0_5mm': {'brand': 'Takahashi', 'name': 'M54 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Takahashi_M54_Spacer_0_7mm': {'brand': 'Takahashi', 'name': 'M54 Spacer 0.7mm', 'type': 'type_spacer', 'optical_length': 0.7, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Takahashi_M54_Spacer_1_5mm': {'brand': 'Takahashi', 'name': 'M54 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Takahashi_M72_Spacer_0_5mm': {'brand': 'Takahashi', 'name': 'M72 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 13, 'tside_thread': 'M72', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Takahashi_M72_Spacer_1_5mm': {'brand': 'Takahashi', 'name': 'M72 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 13, 'tside_thread': 'M72', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Takahashi_M82_Spacer_0_5mm': {'brand': 'Takahashi', 'name': 'M82 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 16, 'tside_thread': 'M82', 'tside_gender': '', 'cside_thread': 'M82', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Takahashi_M82_Spacer_1mm': {'brand': 'Takahashi', 'name': 'M82 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 16, 'tside_thread': 'M82', 'tside_gender': '', 'cside_thread': 'M82', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Takahashi_M82_Spacer_1_5mm': {'brand': 'Takahashi', 'name': 'M82 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 16, 'tside_thread': 'M82', 'tside_gender': '', 'cside_thread': 'M82', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Takahashi_M92_Spacer_0_5mm': {'brand': 'Takahashi', 'name': 'M92 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 17, 'tside_thread': 'M92', 'tside_gender': '', 'cside_thread': 'M92', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Takahashi_M92_Spacer_1mm': {'brand': 'Takahashi', 'name': 'M92 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 17, 'tside_thread': 'M92', 'tside_gender': '', 'cside_thread': 'M92', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Takahashi_M92_Spacer_1_5mm': {'brand': 'Takahashi', 'name': 'M92 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 17, 'tside_thread': 'M92', 'tside_gender': '', 'cside_thread': 'M92', 'cside_gender': '', 'reversible': True, 'bf_role': ''}}

    @classmethod
    def Takahashi_M42_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Spacer_1mm'])

    @classmethod
    def Takahashi_M42_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Spacer_2mm'])

    @classmethod
    def Takahashi_M54_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Spacer_1mm'])

    @classmethod
    def Takahashi_M54_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Spacer_2mm'])

    @classmethod
    def Takahashi_M72_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_Spacer_1mm'])

    @classmethod
    def Takahashi_M72_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_Spacer_2mm'])

    @classmethod
    def Takahashi_M82_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_Spacer_2mm'])

    @classmethod
    def Takahashi_M42_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Spacer_0_5mm'])

    @classmethod
    def Takahashi_M42_Spacer_0_7mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Spacer_0_7mm'])

    @classmethod
    def Takahashi_M42_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M42_Spacer_1_5mm'])

    @classmethod
    def Takahashi_M54_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Spacer_0_5mm'])

    @classmethod
    def Takahashi_M54_Spacer_0_7mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Spacer_0_7mm'])

    @classmethod
    def Takahashi_M54_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M54_Spacer_1_5mm'])

    @classmethod
    def Takahashi_M72_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_Spacer_0_5mm'])

    @classmethod
    def Takahashi_M72_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M72_Spacer_1_5mm'])

    @classmethod
    def Takahashi_M82_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_Spacer_0_5mm'])

    @classmethod
    def Takahashi_M82_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_Spacer_1mm'])

    @classmethod
    def Takahashi_M82_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M82_Spacer_1_5mm'])

    @classmethod
    def Takahashi_M92_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M92_Spacer_0_5mm'])

    @classmethod
    def Takahashi_M92_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M92_Spacer_1mm'])

    @classmethod
    def Takahashi_M92_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Takahashi_M92_Spacer_1_5mm'])