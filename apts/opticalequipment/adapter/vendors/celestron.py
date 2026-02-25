from ...abstract import IntermediateOpticalEquipment
from ....constants import OpticalType
from ..base import Adapter, Spacer

class CelestronAdapter(Adapter):
    _DATABASE = {'Celestron_T_Adapter_SC_M42': {'brand': 'Celestron', 'name': 'T-Adapter (SC→M42)', 'type': 'type_adapter', 'optical_length': 30, 'mass': 60, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_SC_Visual_Back_SC_1_25': {'brand': 'Celestron', 'name': 'SC Visual Back (SC→1.25")', 'type': 'type_adapter', 'optical_length': 35, 'mass': 50, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_SC_2_Adapter': {'brand': 'Celestron', 'name': 'SC→2" Adapter', 'type': 'type_adapter', 'optical_length': 40, 'mass': 80, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_EdgeHD_M68_Adapter': {'brand': 'Celestron', 'name': 'EdgeHD→M68 Adapter', 'type': 'type_adapter', 'optical_length': 10, 'mass': 60, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_SC_M54_Adapter': {'brand': 'Celestron', 'name': 'SC→M54 Adapter', 'type': 'type_adapter', 'optical_length': 15, 'mass': 70, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_T_Adapter_1_25_M42': {'brand': 'Celestron', 'name': 'T-Adapter (1.25"→M42)', 'type': 'type_adapter', 'optical_length': 0, 'mass': 20, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_SC_M48_Adapter': {'brand': 'Celestron', 'name': 'SC→M48 Adapter', 'type': 'type_adapter', 'optical_length': 10, 'mass': 50, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_5mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 24, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_10mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 28, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_15mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 32, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_20mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 36, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_30mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 44, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_40mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 40mm', 'type': 'type_adapter', 'optical_length': 40, 'mass': 52, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_T_Ring_Canon_EOS': {'brand': 'Celestron', 'name': 'T-Ring Canon EOS', 'type': 'type_adapter', 'optical_length': 10.5, 'mass': 30, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_T_Ring_Nikon_F': {'brand': 'Celestron', 'name': 'T-Ring Nikon F', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 30, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_T_Ring_Sony_E': {'brand': 'Celestron', 'name': 'T-Ring Sony E', 'type': 'type_adapter', 'optical_length': 7, 'mass': 25, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_T_Ring_Canon_RF': {'brand': 'Celestron', 'name': 'T-Ring Canon RF', 'type': 'type_adapter', 'optical_length': 5, 'mass': 25, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_T_Ring_Nikon_Z': {'brand': 'Celestron', 'name': 'T-Ring Nikon Z', 'type': 'type_adapter', 'optical_length': 6, 'mass': 25, 'tside_thread': 'Nikon Z', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M42_Spacer_5mm': {'brand': 'Celestron', 'name': 'M42 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 8, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M42_Spacer_10mm': {'brand': 'Celestron', 'name': 'M42 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 12, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M42_Spacer_15mm': {'brand': 'Celestron', 'name': 'M42 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M42_Spacer_20mm': {'brand': 'Celestron', 'name': 'M42 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 20, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M48_Spacer_5mm': {'brand': 'Celestron', 'name': 'M48 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 10, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M48_Spacer_10mm': {'brand': 'Celestron', 'name': 'M48 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 14, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M48_Spacer_15mm': {'brand': 'Celestron', 'name': 'M48 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M48_Spacer_20mm': {'brand': 'Celestron', 'name': 'M48 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 22, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_T_Ring_Fuji_X': {'brand': 'Celestron', 'name': 'T-Ring Fuji X', 'type': 'type_adapter', 'optical_length': 7, 'mass': 25, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_T_Ring_MFT': {'brand': 'Celestron', 'name': 'T-Ring MFT', 'type': 'type_adapter', 'optical_length': 7, 'mass': 22, 'tside_thread': 'MFT', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M54_Spacer_5mm': {'brand': 'Celestron', 'name': 'M54 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 12, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M54_Spacer_10mm': {'brand': 'Celestron', 'name': 'M54 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 16, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M54_Spacer_15mm': {'brand': 'Celestron', 'name': 'M54 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 20, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M54_Spacer_20mm': {'brand': 'Celestron', 'name': 'M54 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 24, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_Starsense_Visual_Back_1_25': {'brand': 'Celestron', 'name': 'Starsense Visual Back (1.25")', 'type': 'type_adapter', 'optical_length': 35, 'mass': 50, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_2_1_25_Adapter': {'brand': 'Celestron', 'name': '2"→1.25" Adapter', 'type': 'type_adapter', 'optical_length': 0, 'mass': 15, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M42_Spacer_2_5mm': {'brand': 'Celestron', 'name': 'M42 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M42_Spacer_3mm': {'brand': 'Celestron', 'name': 'M42 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M42_Spacer_3_5mm': {'brand': 'Celestron', 'name': 'M42 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M42_Spacer_4mm': {'brand': 'Celestron', 'name': 'M42 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 7, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M42_Spacer_4_5mm': {'brand': 'Celestron', 'name': 'M42 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 7, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M42_Spacer_5_5mm': {'brand': 'Celestron', 'name': 'M42 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 8, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M42_Spacer_6mm': {'brand': 'Celestron', 'name': 'M42 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 8, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M42_Spacer_6_5mm': {'brand': 'Celestron', 'name': 'M42 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 9, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M42_Spacer_7mm': {'brand': 'Celestron', 'name': 'M42 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 9, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M42_Spacer_7_5mm': {'brand': 'Celestron', 'name': 'M42 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 10, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M42_Spacer_8mm': {'brand': 'Celestron', 'name': 'M42 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 10, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M42_Spacer_8_5mm': {'brand': 'Celestron', 'name': 'M42 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 10, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M42_Spacer_9mm': {'brand': 'Celestron', 'name': 'M42 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 11, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M42_Spacer_9_5mm': {'brand': 'Celestron', 'name': 'M42 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 11, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M42_Spacer_11mm': {'brand': 'Celestron', 'name': 'M42 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 12, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M42_Spacer_12mm': {'brand': 'Celestron', 'name': 'M42 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 13, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M42_Spacer_13mm': {'brand': 'Celestron', 'name': 'M42 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 14, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M42_Spacer_14mm': {'brand': 'Celestron', 'name': 'M42 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 15, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M42_Spacer_16mm': {'brand': 'Celestron', 'name': 'M42 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M42_Spacer_17mm': {'brand': 'Celestron', 'name': 'M42 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 17, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M42_Spacer_18mm': {'brand': 'Celestron', 'name': 'M42 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 18, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M42_Spacer_22mm': {'brand': 'Celestron', 'name': 'M42 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 21, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M42_Spacer_25mm': {'brand': 'Celestron', 'name': 'M42 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 24, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M48_Spacer_2_5mm': {'brand': 'Celestron', 'name': 'M48 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M48_Spacer_3mm': {'brand': 'Celestron', 'name': 'M48 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M48_Spacer_3_5mm': {'brand': 'Celestron', 'name': 'M48 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M48_Spacer_4mm': {'brand': 'Celestron', 'name': 'M48 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 9, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M48_Spacer_4_5mm': {'brand': 'Celestron', 'name': 'M48 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 9, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M48_Spacer_5_5mm': {'brand': 'Celestron', 'name': 'M48 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 10, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M48_Spacer_6mm': {'brand': 'Celestron', 'name': 'M48 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 10, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M48_Spacer_6_5mm': {'brand': 'Celestron', 'name': 'M48 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 11, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M48_Spacer_7mm': {'brand': 'Celestron', 'name': 'M48 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 11, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M48_Spacer_7_5mm': {'brand': 'Celestron', 'name': 'M48 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 12, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M48_Spacer_8mm': {'brand': 'Celestron', 'name': 'M48 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 12, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M48_Spacer_8_5mm': {'brand': 'Celestron', 'name': 'M48 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 12, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M48_Spacer_9mm': {'brand': 'Celestron', 'name': 'M48 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 13, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M48_Spacer_9_5mm': {'brand': 'Celestron', 'name': 'M48 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 13, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M48_Spacer_11mm': {'brand': 'Celestron', 'name': 'M48 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 14, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M48_Spacer_12mm': {'brand': 'Celestron', 'name': 'M48 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 15, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M48_Spacer_13mm': {'brand': 'Celestron', 'name': 'M48 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 16, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M48_Spacer_14mm': {'brand': 'Celestron', 'name': 'M48 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 17, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M48_Spacer_16mm': {'brand': 'Celestron', 'name': 'M48 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M48_Spacer_17mm': {'brand': 'Celestron', 'name': 'M48 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 19, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M48_Spacer_18mm': {'brand': 'Celestron', 'name': 'M48 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 20, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M48_Spacer_22mm': {'brand': 'Celestron', 'name': 'M48 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 23, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M48_Spacer_25mm': {'brand': 'Celestron', 'name': 'M48 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 26, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M54_Spacer_2_5mm': {'brand': 'Celestron', 'name': 'M54 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 10, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M54_Spacer_3_5mm': {'brand': 'Celestron', 'name': 'M54 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 10, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M54_Spacer_4_5mm': {'brand': 'Celestron', 'name': 'M54 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 11, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M54_Spacer_5_5mm': {'brand': 'Celestron', 'name': 'M54 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 12, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M54_Spacer_6_5mm': {'brand': 'Celestron', 'name': 'M54 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 13, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M54_Spacer_7mm': {'brand': 'Celestron', 'name': 'M54 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 13, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M54_Spacer_7_5mm': {'brand': 'Celestron', 'name': 'M54 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 14, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M54_Spacer_8mm': {'brand': 'Celestron', 'name': 'M54 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 14, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M54_Spacer_8_5mm': {'brand': 'Celestron', 'name': 'M54 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 14, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M54_Spacer_9mm': {'brand': 'Celestron', 'name': 'M54 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 15, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M54_Spacer_9_5mm': {'brand': 'Celestron', 'name': 'M54 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 15, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M54_Spacer_11mm': {'brand': 'Celestron', 'name': 'M54 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 16, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M54_Spacer_12mm': {'brand': 'Celestron', 'name': 'M54 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 17, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M54_Spacer_13mm': {'brand': 'Celestron', 'name': 'M54 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 18, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M54_Spacer_14mm': {'brand': 'Celestron', 'name': 'M54 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 19, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M54_Spacer_16mm': {'brand': 'Celestron', 'name': 'M54 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 20, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M54_Spacer_17mm': {'brand': 'Celestron', 'name': 'M54 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 21, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M54_Spacer_18mm': {'brand': 'Celestron', 'name': 'M54 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 22, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M54_Spacer_22mm': {'brand': 'Celestron', 'name': 'M54 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 25, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M54_Spacer_25mm': {'brand': 'Celestron', 'name': 'M54 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 28, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_3mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 22, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_4mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 23, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_6mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 24, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_7mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 25, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_8mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 26, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_9mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 27, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_11mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 28, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_12mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 29, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_14mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 31, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_16mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 32, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_17mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 33, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_18mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 34, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_22mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 37, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_25mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 40, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_28mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 42, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_35mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 48, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_M42_Extension_Tube_3mm': {'brand': 'Celestron', 'name': 'M42 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 14, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M42_Extension_Tube_6mm': {'brand': 'Celestron', 'name': 'M42 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 15, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M42_Extension_Tube_9mm': {'brand': 'Celestron', 'name': 'M42 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M42_Extension_Tube_11mm': {'brand': 'Celestron', 'name': 'M42 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 17, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M42_Extension_Tube_13mm': {'brand': 'Celestron', 'name': 'M42 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 17, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M42_Extension_Tube_16mm': {'brand': 'Celestron', 'name': 'M42 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 18, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M42_Extension_Tube_22mm': {'brand': 'Celestron', 'name': 'M42 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 20, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M42_Extension_Tube_28mm': {'brand': 'Celestron', 'name': 'M42 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 22, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M42_Extension_Tube_35mm': {'brand': 'Celestron', 'name': 'M42 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 24, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M42_Extension_Tube_45mm': {'brand': 'Celestron', 'name': 'M42 Extension Tube 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 27, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M48_Extension_Tube_3mm': {'brand': 'Celestron', 'name': 'M48 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M48_Extension_Tube_6mm': {'brand': 'Celestron', 'name': 'M48 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 19, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M48_Extension_Tube_9mm': {'brand': 'Celestron', 'name': 'M48 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 20, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M48_Extension_Tube_11mm': {'brand': 'Celestron', 'name': 'M48 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 21, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M48_Extension_Tube_13mm': {'brand': 'Celestron', 'name': 'M48 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 21, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M48_Extension_Tube_16mm': {'brand': 'Celestron', 'name': 'M48 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 22, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M48_Extension_Tube_22mm': {'brand': 'Celestron', 'name': 'M48 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 24, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M48_Extension_Tube_28mm': {'brand': 'Celestron', 'name': 'M48 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 26, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M48_Extension_Tube_35mm': {'brand': 'Celestron', 'name': 'M48 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 28, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M48_Extension_Tube_45mm': {'brand': 'Celestron', 'name': 'M48 Extension Tube 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 31, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M54_Extension_Tube_3mm': {'brand': 'Celestron', 'name': 'M54 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 22, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M54_Extension_Tube_6mm': {'brand': 'Celestron', 'name': 'M54 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 23, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M54_Extension_Tube_9mm': {'brand': 'Celestron', 'name': 'M54 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 24, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M54_Extension_Tube_11mm': {'brand': 'Celestron', 'name': 'M54 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 25, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M54_Extension_Tube_13mm': {'brand': 'Celestron', 'name': 'M54 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 25, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M54_Extension_Tube_16mm': {'brand': 'Celestron', 'name': 'M54 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 26, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M54_Extension_Tube_22mm': {'brand': 'Celestron', 'name': 'M54 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 28, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M54_Extension_Tube_28mm': {'brand': 'Celestron', 'name': 'M54 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 30, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M54_Extension_Tube_35mm': {'brand': 'Celestron', 'name': 'M54 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 32, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M54_Extension_Tube_45mm': {'brand': 'Celestron', 'name': 'M54 Extension Tube 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 35, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M68_Extension_Tube_3mm': {'brand': 'Celestron', 'name': 'M68 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 16, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M68_Extension_Tube_5mm': {'brand': 'Celestron', 'name': 'M68 Extension Tube 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 17, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M68_Extension_Tube_6mm': {'brand': 'Celestron', 'name': 'M68 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 17, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M68_Extension_Tube_8mm': {'brand': 'Celestron', 'name': 'M68 Extension Tube 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 18, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M68_Extension_Tube_9mm': {'brand': 'Celestron', 'name': 'M68 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 18, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M68_Extension_Tube_11mm': {'brand': 'Celestron', 'name': 'M68 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 19, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M68_Extension_Tube_13mm': {'brand': 'Celestron', 'name': 'M68 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 19, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M68_Extension_Tube_14mm': {'brand': 'Celestron', 'name': 'M68 Extension Tube 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 20, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M68_Extension_Tube_16mm': {'brand': 'Celestron', 'name': 'M68 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 20, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M68_Extension_Tube_18mm': {'brand': 'Celestron', 'name': 'M68 Extension Tube 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 21, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M68_Extension_Tube_22mm': {'brand': 'Celestron', 'name': 'M68 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 22, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M68_Extension_Tube_25mm': {'brand': 'Celestron', 'name': 'M68 Extension Tube 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 23, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M68_Extension_Tube_28mm': {'brand': 'Celestron', 'name': 'M68 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 24, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M68_Extension_Tube_30mm': {'brand': 'Celestron', 'name': 'M68 Extension Tube 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 25, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_M68_Extension_Tube_35mm': {'brand': 'Celestron', 'name': 'M68 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 26, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_SC_Extension_Tube_5mm': {'brand': 'Celestron', 'name': 'SC Extension Tube 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 23, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_SC_Extension_Tube_10mm': {'brand': 'Celestron', 'name': 'SC Extension Tube 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 25, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_SC_Extension_Tube_15mm': {'brand': 'Celestron', 'name': 'SC Extension Tube 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 26, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_SC_Extension_Tube_20mm': {'brand': 'Celestron', 'name': 'SC Extension Tube 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 28, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_SC_Extension_Tube_25mm': {'brand': 'Celestron', 'name': 'SC Extension Tube 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 29, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_SC_Extension_Tube_30mm': {'brand': 'Celestron', 'name': 'SC Extension Tube 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 31, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_SC_Extension_Tube_35mm': {'brand': 'Celestron', 'name': 'SC Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 32, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_SC_Extension_Tube_40mm': {'brand': 'Celestron', 'name': 'SC Extension Tube 40mm', 'type': 'type_adapter', 'optical_length': 40, 'mass': 34, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_SC_Extension_Tube_50mm': {'brand': 'Celestron', 'name': 'SC Extension Tube 50mm', 'type': 'type_adapter', 'optical_length': 50, 'mass': 37, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_SC_Extension_Tube_60mm': {'brand': 'Celestron', 'name': 'SC Extension Tube 60mm', 'type': 'type_adapter', 'optical_length': 60, 'mass': 40, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_SC_Extension_Tube_75mm': {'brand': 'Celestron', 'name': 'SC Extension Tube 75mm', 'type': 'type_adapter', 'optical_length': 75, 'mass': 44, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_2_5mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 22, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_3_5mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 22, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_4_5mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 23, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_5_5mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 24, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_6_5mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 25, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_7_5mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 26, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_8_5mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 26, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_9_5mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 27, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_13mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 30, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_19mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 19mm', 'type': 'type_adapter', 'optical_length': 19, 'mass': 35, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_21mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 21mm', 'type': 'type_adapter', 'optical_length': 21, 'mass': 36, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_23mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 23mm', 'type': 'type_adapter', 'optical_length': 23, 'mass': 38, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_24mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 24mm', 'type': 'type_adapter', 'optical_length': 24, 'mass': 39, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_26mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 26mm', 'type': 'type_adapter', 'optical_length': 26, 'mass': 40, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_27mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 27mm', 'type': 'type_adapter', 'optical_length': 27, 'mass': 41, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_32mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 32mm', 'type': 'type_adapter', 'optical_length': 32, 'mass': 45, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_1_25_Spacer_3mm': {'brand': 'Celestron', 'name': '1.25" Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 5, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_1_25_Spacer_4mm': {'brand': 'Celestron', 'name': '1.25" Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 6, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_1_25_Spacer_5mm': {'brand': 'Celestron', 'name': '1.25" Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 7, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_1_25_Spacer_6mm': {'brand': 'Celestron', 'name': '1.25" Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 7, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_1_25_Spacer_7mm': {'brand': 'Celestron', 'name': '1.25" Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 8, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_1_25_Spacer_8mm': {'brand': 'Celestron', 'name': '1.25" Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 9, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_1_25_Spacer_9mm': {'brand': 'Celestron', 'name': '1.25" Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 10, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_1_25_Spacer_10mm': {'brand': 'Celestron', 'name': '1.25" Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 11, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_1_25_Spacer_12mm': {'brand': 'Celestron', 'name': '1.25" Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 12, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_1_25_Spacer_15mm': {'brand': 'Celestron', 'name': '1.25" Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 15, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_1_25_Spacer_18mm': {'brand': 'Celestron', 'name': '1.25" Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 17, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_1_25_Spacer_20mm': {'brand': 'Celestron', 'name': '1.25" Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 19, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_1_25_Spacer_25mm': {'brand': 'Celestron', 'name': '1.25" Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 23, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_2_Spacer_3mm': {'brand': 'Celestron', 'name': '2" Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 10, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_2_Spacer_4mm': {'brand': 'Celestron', 'name': '2" Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 11, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_2_Spacer_5mm': {'brand': 'Celestron', 'name': '2" Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 12, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_2_Spacer_6mm': {'brand': 'Celestron', 'name': '2" Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 12, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_2_Spacer_7mm': {'brand': 'Celestron', 'name': '2" Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 13, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_2_Spacer_8mm': {'brand': 'Celestron', 'name': '2" Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 14, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_2_Spacer_9mm': {'brand': 'Celestron', 'name': '2" Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 15, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_2_Spacer_10mm': {'brand': 'Celestron', 'name': '2" Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 16, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_2_Spacer_12mm': {'brand': 'Celestron', 'name': '2" Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 17, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_2_Spacer_15mm': {'brand': 'Celestron', 'name': '2" Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 20, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_2_Spacer_18mm': {'brand': 'Celestron', 'name': '2" Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 22, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_2_Spacer_20mm': {'brand': 'Celestron', 'name': '2" Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 24, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_2_Spacer_25mm': {'brand': 'Celestron', 'name': '2" Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 28, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}}

    @classmethod
    def Celestron_T_Adapter_SC_M42(cls):
        return cls.from_database(cls._DATABASE['Celestron_T_Adapter_SC_M42'])

    @classmethod
    def Celestron_SC_Visual_Back_SC_1_25(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Visual_Back_SC_1_25'])

    @classmethod
    def Celestron_SC_2_Adapter(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_2_Adapter'])

    @classmethod
    def Celestron_EdgeHD_M68_Adapter(cls):
        return cls.from_database(cls._DATABASE['Celestron_EdgeHD_M68_Adapter'])

    @classmethod
    def Celestron_SC_M54_Adapter(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_M54_Adapter'])

    @classmethod
    def Celestron_T_Adapter_1_25_M42(cls):
        return cls.from_database(cls._DATABASE['Celestron_T_Adapter_1_25_M42'])

    @classmethod
    def Celestron_SC_M48_Adapter(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_M48_Adapter'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_5mm'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_10mm'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_15mm'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_20mm'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_30mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_30mm'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_40mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_40mm'])

    @classmethod
    def Celestron_T_Ring_Canon_EOS(cls):
        return cls.from_database(cls._DATABASE['Celestron_T_Ring_Canon_EOS'])

    @classmethod
    def Celestron_T_Ring_Nikon_F(cls):
        return cls.from_database(cls._DATABASE['Celestron_T_Ring_Nikon_F'])

    @classmethod
    def Celestron_T_Ring_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Celestron_T_Ring_Sony_E'])

    @classmethod
    def Celestron_T_Ring_Canon_RF(cls):
        return cls.from_database(cls._DATABASE['Celestron_T_Ring_Canon_RF'])

    @classmethod
    def Celestron_T_Ring_Nikon_Z(cls):
        return cls.from_database(cls._DATABASE['Celestron_T_Ring_Nikon_Z'])

    @classmethod
    def Celestron_M42_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Spacer_5mm'])

    @classmethod
    def Celestron_M42_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Spacer_10mm'])

    @classmethod
    def Celestron_M42_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Spacer_15mm'])

    @classmethod
    def Celestron_M42_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Spacer_20mm'])

    @classmethod
    def Celestron_M48_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Spacer_5mm'])

    @classmethod
    def Celestron_M48_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Spacer_10mm'])

    @classmethod
    def Celestron_M48_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Spacer_15mm'])

    @classmethod
    def Celestron_M48_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Spacer_20mm'])

    @classmethod
    def Celestron_T_Ring_Fuji_X(cls):
        return cls.from_database(cls._DATABASE['Celestron_T_Ring_Fuji_X'])

    @classmethod
    def Celestron_T_Ring_MFT(cls):
        return cls.from_database(cls._DATABASE['Celestron_T_Ring_MFT'])

    @classmethod
    def Celestron_M54_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M54_Spacer_5mm'])

    @classmethod
    def Celestron_M54_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M54_Spacer_10mm'])

    @classmethod
    def Celestron_M54_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M54_Spacer_15mm'])

    @classmethod
    def Celestron_M54_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M54_Spacer_20mm'])

    @classmethod
    def Celestron_Starsense_Visual_Back_1_25(cls):
        return cls.from_database(cls._DATABASE['Celestron_Starsense_Visual_Back_1_25'])

    @classmethod
    def Celestron_2_1_25_Adapter(cls):
        return cls.from_database(cls._DATABASE['Celestron_2_1_25_Adapter'])

    @classmethod
    def Celestron_M42_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Spacer_2_5mm'])

    @classmethod
    def Celestron_M42_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Spacer_3mm'])

    @classmethod
    def Celestron_M42_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Spacer_3_5mm'])

    @classmethod
    def Celestron_M42_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Spacer_4mm'])

    @classmethod
    def Celestron_M42_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Spacer_4_5mm'])

    @classmethod
    def Celestron_M42_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Spacer_5_5mm'])

    @classmethod
    def Celestron_M42_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Spacer_6mm'])

    @classmethod
    def Celestron_M42_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Spacer_6_5mm'])

    @classmethod
    def Celestron_M42_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Spacer_7mm'])

    @classmethod
    def Celestron_M42_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Spacer_7_5mm'])

    @classmethod
    def Celestron_M42_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Spacer_8mm'])

    @classmethod
    def Celestron_M42_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Spacer_8_5mm'])

    @classmethod
    def Celestron_M42_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Spacer_9mm'])

    @classmethod
    def Celestron_M42_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Spacer_9_5mm'])

    @classmethod
    def Celestron_M42_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Spacer_11mm'])

    @classmethod
    def Celestron_M42_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Spacer_12mm'])

    @classmethod
    def Celestron_M42_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Spacer_13mm'])

    @classmethod
    def Celestron_M42_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Spacer_14mm'])

    @classmethod
    def Celestron_M42_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Spacer_16mm'])

    @classmethod
    def Celestron_M42_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Spacer_17mm'])

    @classmethod
    def Celestron_M42_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Spacer_18mm'])

    @classmethod
    def Celestron_M42_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Spacer_22mm'])

    @classmethod
    def Celestron_M42_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Spacer_25mm'])

    @classmethod
    def Celestron_M48_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Spacer_2_5mm'])

    @classmethod
    def Celestron_M48_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Spacer_3mm'])

    @classmethod
    def Celestron_M48_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Spacer_3_5mm'])

    @classmethod
    def Celestron_M48_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Spacer_4mm'])

    @classmethod
    def Celestron_M48_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Spacer_4_5mm'])

    @classmethod
    def Celestron_M48_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Spacer_5_5mm'])

    @classmethod
    def Celestron_M48_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Spacer_6mm'])

    @classmethod
    def Celestron_M48_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Spacer_6_5mm'])

    @classmethod
    def Celestron_M48_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Spacer_7mm'])

    @classmethod
    def Celestron_M48_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Spacer_7_5mm'])

    @classmethod
    def Celestron_M48_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Spacer_8mm'])

    @classmethod
    def Celestron_M48_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Spacer_8_5mm'])

    @classmethod
    def Celestron_M48_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Spacer_9mm'])

    @classmethod
    def Celestron_M48_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Spacer_9_5mm'])

    @classmethod
    def Celestron_M48_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Spacer_11mm'])

    @classmethod
    def Celestron_M48_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Spacer_12mm'])

    @classmethod
    def Celestron_M48_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Spacer_13mm'])

    @classmethod
    def Celestron_M48_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Spacer_14mm'])

    @classmethod
    def Celestron_M48_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Spacer_16mm'])

    @classmethod
    def Celestron_M48_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Spacer_17mm'])

    @classmethod
    def Celestron_M48_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Spacer_18mm'])

    @classmethod
    def Celestron_M48_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Spacer_22mm'])

    @classmethod
    def Celestron_M48_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Spacer_25mm'])

    @classmethod
    def Celestron_M54_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M54_Spacer_2_5mm'])

    @classmethod
    def Celestron_M54_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M54_Spacer_3_5mm'])

    @classmethod
    def Celestron_M54_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M54_Spacer_4_5mm'])

    @classmethod
    def Celestron_M54_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M54_Spacer_5_5mm'])

    @classmethod
    def Celestron_M54_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M54_Spacer_6_5mm'])

    @classmethod
    def Celestron_M54_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M54_Spacer_7mm'])

    @classmethod
    def Celestron_M54_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M54_Spacer_7_5mm'])

    @classmethod
    def Celestron_M54_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M54_Spacer_8mm'])

    @classmethod
    def Celestron_M54_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M54_Spacer_8_5mm'])

    @classmethod
    def Celestron_M54_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M54_Spacer_9mm'])

    @classmethod
    def Celestron_M54_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M54_Spacer_9_5mm'])

    @classmethod
    def Celestron_M54_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M54_Spacer_11mm'])

    @classmethod
    def Celestron_M54_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M54_Spacer_12mm'])

    @classmethod
    def Celestron_M54_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M54_Spacer_13mm'])

    @classmethod
    def Celestron_M54_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M54_Spacer_14mm'])

    @classmethod
    def Celestron_M54_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M54_Spacer_16mm'])

    @classmethod
    def Celestron_M54_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M54_Spacer_17mm'])

    @classmethod
    def Celestron_M54_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M54_Spacer_18mm'])

    @classmethod
    def Celestron_M54_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M54_Spacer_22mm'])

    @classmethod
    def Celestron_M54_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M54_Spacer_25mm'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_3mm'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_4mm'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_6mm'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_7mm'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_8mm'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_9mm'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_11mm'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_12mm'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_14mm'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_16mm'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_17mm'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_18mm'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_22mm'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_25mm'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_28mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_28mm'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_35mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_35mm'])

    @classmethod
    def Celestron_M42_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Extension_Tube_3mm'])

    @classmethod
    def Celestron_M42_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Extension_Tube_6mm'])

    @classmethod
    def Celestron_M42_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Extension_Tube_9mm'])

    @classmethod
    def Celestron_M42_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Extension_Tube_11mm'])

    @classmethod
    def Celestron_M42_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Extension_Tube_13mm'])

    @classmethod
    def Celestron_M42_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Extension_Tube_16mm'])

    @classmethod
    def Celestron_M42_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Extension_Tube_22mm'])

    @classmethod
    def Celestron_M42_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Extension_Tube_28mm'])

    @classmethod
    def Celestron_M42_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Extension_Tube_35mm'])

    @classmethod
    def Celestron_M42_Extension_Tube_45mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Extension_Tube_45mm'])

    @classmethod
    def Celestron_M48_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Extension_Tube_3mm'])

    @classmethod
    def Celestron_M48_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Extension_Tube_6mm'])

    @classmethod
    def Celestron_M48_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Extension_Tube_9mm'])

    @classmethod
    def Celestron_M48_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Extension_Tube_11mm'])

    @classmethod
    def Celestron_M48_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Extension_Tube_13mm'])

    @classmethod
    def Celestron_M48_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Extension_Tube_16mm'])

    @classmethod
    def Celestron_M48_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Extension_Tube_22mm'])

    @classmethod
    def Celestron_M48_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Extension_Tube_28mm'])

    @classmethod
    def Celestron_M48_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Extension_Tube_35mm'])

    @classmethod
    def Celestron_M48_Extension_Tube_45mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Extension_Tube_45mm'])

    @classmethod
    def Celestron_M54_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M54_Extension_Tube_3mm'])

    @classmethod
    def Celestron_M54_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M54_Extension_Tube_6mm'])

    @classmethod
    def Celestron_M54_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M54_Extension_Tube_9mm'])

    @classmethod
    def Celestron_M54_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M54_Extension_Tube_11mm'])

    @classmethod
    def Celestron_M54_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M54_Extension_Tube_13mm'])

    @classmethod
    def Celestron_M54_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M54_Extension_Tube_16mm'])

    @classmethod
    def Celestron_M54_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M54_Extension_Tube_22mm'])

    @classmethod
    def Celestron_M54_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M54_Extension_Tube_28mm'])

    @classmethod
    def Celestron_M54_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M54_Extension_Tube_35mm'])

    @classmethod
    def Celestron_M54_Extension_Tube_45mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M54_Extension_Tube_45mm'])

    @classmethod
    def Celestron_M68_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M68_Extension_Tube_3mm'])

    @classmethod
    def Celestron_M68_Extension_Tube_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M68_Extension_Tube_5mm'])

    @classmethod
    def Celestron_M68_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M68_Extension_Tube_6mm'])

    @classmethod
    def Celestron_M68_Extension_Tube_8mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M68_Extension_Tube_8mm'])

    @classmethod
    def Celestron_M68_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M68_Extension_Tube_9mm'])

    @classmethod
    def Celestron_M68_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M68_Extension_Tube_11mm'])

    @classmethod
    def Celestron_M68_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M68_Extension_Tube_13mm'])

    @classmethod
    def Celestron_M68_Extension_Tube_14mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M68_Extension_Tube_14mm'])

    @classmethod
    def Celestron_M68_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M68_Extension_Tube_16mm'])

    @classmethod
    def Celestron_M68_Extension_Tube_18mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M68_Extension_Tube_18mm'])

    @classmethod
    def Celestron_M68_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M68_Extension_Tube_22mm'])

    @classmethod
    def Celestron_M68_Extension_Tube_25mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M68_Extension_Tube_25mm'])

    @classmethod
    def Celestron_M68_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M68_Extension_Tube_28mm'])

    @classmethod
    def Celestron_M68_Extension_Tube_30mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M68_Extension_Tube_30mm'])

    @classmethod
    def Celestron_M68_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M68_Extension_Tube_35mm'])

    @classmethod
    def Celestron_SC_Extension_Tube_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Extension_Tube_5mm'])

    @classmethod
    def Celestron_SC_Extension_Tube_10mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Extension_Tube_10mm'])

    @classmethod
    def Celestron_SC_Extension_Tube_15mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Extension_Tube_15mm'])

    @classmethod
    def Celestron_SC_Extension_Tube_20mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Extension_Tube_20mm'])

    @classmethod
    def Celestron_SC_Extension_Tube_25mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Extension_Tube_25mm'])

    @classmethod
    def Celestron_SC_Extension_Tube_30mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Extension_Tube_30mm'])

    @classmethod
    def Celestron_SC_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Extension_Tube_35mm'])

    @classmethod
    def Celestron_SC_Extension_Tube_40mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Extension_Tube_40mm'])

    @classmethod
    def Celestron_SC_Extension_Tube_50mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Extension_Tube_50mm'])

    @classmethod
    def Celestron_SC_Extension_Tube_60mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Extension_Tube_60mm'])

    @classmethod
    def Celestron_SC_Extension_Tube_75mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Extension_Tube_75mm'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_2_5mm'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_3_5mm'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_4_5mm'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_5_5mm'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_6_5mm'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_7_5mm'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_8_5mm'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_9_5mm'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_13mm'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_19mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_19mm'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_21mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_21mm'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_23mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_23mm'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_24mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_24mm'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_26mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_26mm'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_27mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_27mm'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_32mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_32mm'])

    @classmethod
    def Celestron_1_25_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_1_25_Spacer_3mm'])

    @classmethod
    def Celestron_1_25_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_1_25_Spacer_4mm'])

    @classmethod
    def Celestron_1_25_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_1_25_Spacer_5mm'])

    @classmethod
    def Celestron_1_25_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_1_25_Spacer_6mm'])

    @classmethod
    def Celestron_1_25_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_1_25_Spacer_7mm'])

    @classmethod
    def Celestron_1_25_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_1_25_Spacer_8mm'])

    @classmethod
    def Celestron_1_25_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_1_25_Spacer_9mm'])

    @classmethod
    def Celestron_1_25_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_1_25_Spacer_10mm'])

    @classmethod
    def Celestron_1_25_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_1_25_Spacer_12mm'])

    @classmethod
    def Celestron_1_25_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_1_25_Spacer_15mm'])

    @classmethod
    def Celestron_1_25_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_1_25_Spacer_18mm'])

    @classmethod
    def Celestron_1_25_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_1_25_Spacer_20mm'])

    @classmethod
    def Celestron_1_25_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_1_25_Spacer_25mm'])

    @classmethod
    def Celestron_2_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_2_Spacer_3mm'])

    @classmethod
    def Celestron_2_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_2_Spacer_4mm'])

    @classmethod
    def Celestron_2_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_2_Spacer_5mm'])

    @classmethod
    def Celestron_2_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_2_Spacer_6mm'])

    @classmethod
    def Celestron_2_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_2_Spacer_7mm'])

    @classmethod
    def Celestron_2_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_2_Spacer_8mm'])

    @classmethod
    def Celestron_2_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_2_Spacer_9mm'])

    @classmethod
    def Celestron_2_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_2_Spacer_10mm'])

    @classmethod
    def Celestron_2_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_2_Spacer_12mm'])

    @classmethod
    def Celestron_2_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_2_Spacer_15mm'])

    @classmethod
    def Celestron_2_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_2_Spacer_18mm'])

    @classmethod
    def Celestron_2_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_2_Spacer_20mm'])

    @classmethod
    def Celestron_2_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_2_Spacer_25mm'])

class CelestronSpacer(Spacer):
    _DATABASE = {'Celestron_M42_Spacer_2mm': {'brand': 'Celestron', 'name': 'M42 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Celestron_M48_Spacer_2mm': {'brand': 'Celestron', 'name': 'M48 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Celestron_M42_Spacer_1mm': {'brand': 'Celestron', 'name': 'M42 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Celestron_M48_Spacer_1mm': {'brand': 'Celestron', 'name': 'M48 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Celestron_M54_Spacer_2mm': {'brand': 'Celestron', 'name': 'M54 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Celestron_M42_Spacer_0_5mm': {'brand': 'Celestron', 'name': 'M42 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Celestron_M42_Spacer_0_7mm': {'brand': 'Celestron', 'name': 'M42 Spacer 0.7mm', 'type': 'type_spacer', 'optical_length': 0.7, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Celestron_M42_Spacer_1_5mm': {'brand': 'Celestron', 'name': 'M42 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Celestron_M48_Spacer_0_5mm': {'brand': 'Celestron', 'name': 'M48 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Celestron_M48_Spacer_0_7mm': {'brand': 'Celestron', 'name': 'M48 Spacer 0.7mm', 'type': 'type_spacer', 'optical_length': 0.7, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Celestron_M48_Spacer_1_5mm': {'brand': 'Celestron', 'name': 'M48 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Celestron_M54_Spacer_0_5mm': {'brand': 'Celestron', 'name': 'M54 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Celestron_M54_Spacer_1_5mm': {'brand': 'Celestron', 'name': 'M54 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_1mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 21, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_2mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 21, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_0_5mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 21, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Celestron_SC_Schmidt_Cassegrain_Spacer_1_5mm': {'brand': 'Celestron', 'name': 'SC (Schmidt-Cassegrain) Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 21, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Celestron_1_25_Spacer_0_5mm': {'brand': 'Celestron', 'name': '1.25" Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 4, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_1_25_Spacer_1mm': {'brand': 'Celestron', 'name': '1.25" Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 4, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_1_25_Spacer_1_5mm': {'brand': 'Celestron', 'name': '1.25" Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 4, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_1_25_Spacer_2mm': {'brand': 'Celestron', 'name': '1.25" Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 4, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_2_Spacer_0_5mm': {'brand': 'Celestron', 'name': '2" Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 9, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_2_Spacer_1mm': {'brand': 'Celestron', 'name': '2" Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 9, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_2_Spacer_1_5mm': {'brand': 'Celestron', 'name': '2" Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 9, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Celestron_2_Spacer_2mm': {'brand': 'Celestron', 'name': '2" Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 9, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}}

    @classmethod
    def Celestron_M42_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Spacer_2mm'])

    @classmethod
    def Celestron_M48_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Spacer_2mm'])

    @classmethod
    def Celestron_M42_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Spacer_1mm'])

    @classmethod
    def Celestron_M48_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Spacer_1mm'])

    @classmethod
    def Celestron_M54_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M54_Spacer_2mm'])

    @classmethod
    def Celestron_M42_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Spacer_0_5mm'])

    @classmethod
    def Celestron_M42_Spacer_0_7mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Spacer_0_7mm'])

    @classmethod
    def Celestron_M42_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M42_Spacer_1_5mm'])

    @classmethod
    def Celestron_M48_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Spacer_0_5mm'])

    @classmethod
    def Celestron_M48_Spacer_0_7mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Spacer_0_7mm'])

    @classmethod
    def Celestron_M48_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M48_Spacer_1_5mm'])

    @classmethod
    def Celestron_M54_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M54_Spacer_0_5mm'])

    @classmethod
    def Celestron_M54_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_M54_Spacer_1_5mm'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_1mm'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_2mm'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_0_5mm'])

    @classmethod
    def Celestron_SC_Schmidt_Cassegrain_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_SC_Schmidt_Cassegrain_Spacer_1_5mm'])

    @classmethod
    def Celestron_1_25_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_1_25_Spacer_0_5mm'])

    @classmethod
    def Celestron_1_25_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_1_25_Spacer_1mm'])

    @classmethod
    def Celestron_1_25_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_1_25_Spacer_1_5mm'])

    @classmethod
    def Celestron_1_25_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_1_25_Spacer_2mm'])

    @classmethod
    def Celestron_2_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_2_Spacer_0_5mm'])

    @classmethod
    def Celestron_2_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_2_Spacer_1mm'])

    @classmethod
    def Celestron_2_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_2_Spacer_1_5mm'])

    @classmethod
    def Celestron_2_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Celestron_2_Spacer_2mm'])