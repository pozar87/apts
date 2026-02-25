from ...abstract import IntermediateOpticalEquipment
from ....constants import OpticalType
from ..base import Adapter, Spacer

class BresserAdapter(Adapter):
    _DATABASE = {'Bresser_T2_Ring_Canon_EOS': {'brand': 'Bresser', 'name': 'T2 Ring Canon EOS', 'type': 'type_adapter', 'optical_length': 10.5, 'mass': 25, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_T2_Ring_Nikon_F': {'brand': 'Bresser', 'name': 'T2 Ring Nikon F', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 25, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_T2_Ring_Sony_E': {'brand': 'Bresser', 'name': 'T2 Ring Sony E', 'type': 'type_adapter', 'optical_length': 7, 'mass': 25, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_1_25_M42_Adapter': {'brand': 'Bresser', 'name': '1.25"→M42 Adapter', 'type': 'type_adapter', 'optical_length': 0, 'mass': 10, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_M42_M48_Adapter': {'brand': 'Bresser', 'name': 'M42→M48 Adapter', 'type': 'type_adapter', 'optical_length': 5, 'mass': 20, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_M42_Spacer_5mm': {'brand': 'Bresser', 'name': 'M42 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 8, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M42_Spacer_10mm': {'brand': 'Bresser', 'name': 'M42 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 12, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M42_Spacer_15mm': {'brand': 'Bresser', 'name': 'M42 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M42_Spacer_20mm': {'brand': 'Bresser', 'name': 'M42 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 20, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M48_Spacer_5mm': {'brand': 'Bresser', 'name': 'M48 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 10, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M48_Spacer_10mm': {'brand': 'Bresser', 'name': 'M48 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 14, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M48_Spacer_15mm': {'brand': 'Bresser', 'name': 'M48 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M48_Spacer_20mm': {'brand': 'Bresser', 'name': 'M48 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 22, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_T_Ring_Canon_RF': {'brand': 'Bresser', 'name': 'T-Ring Canon RF', 'type': 'type_adapter', 'optical_length': 5, 'mass': 25, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_T_Ring_Nikon_Z': {'brand': 'Bresser', 'name': 'T-Ring Nikon Z', 'type': 'type_adapter', 'optical_length': 6, 'mass': 25, 'tside_thread': 'Nikon Z', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_T_Ring_Fuji_X': {'brand': 'Bresser', 'name': 'T-Ring Fuji X', 'type': 'type_adapter', 'optical_length': 7, 'mass': 25, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_T_Ring_MFT': {'brand': 'Bresser', 'name': 'T-Ring MFT', 'type': 'type_adapter', 'optical_length': 7, 'mass': 22, 'tside_thread': 'MFT', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_EOS_M42_T_Ring': {'brand': 'Bresser', 'name': 'EOS→M42 T-Ring', 'type': 'type_adapter', 'optical_length': 10.5, 'mass': 28, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_Nikon_F_M42_T_Ring': {'brand': 'Bresser', 'name': 'Nikon F→M42 T-Ring', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 28, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_M48_M42_Adapter': {'brand': 'Bresser', 'name': 'M48→M42 Adapter', 'type': 'type_adapter', 'optical_length': 5, 'mass': 18, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_SC_M42_Adapter': {'brand': 'Bresser', 'name': 'SC→M42 Adapter', 'type': 'type_adapter', 'optical_length': 20, 'mass': 45, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_2_M42_Adapter': {'brand': 'Bresser', 'name': '2"→M42 Adapter', 'type': 'type_adapter', 'optical_length': 0, 'mass': 12, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_2_1_25_Adapter': {'brand': 'Bresser', 'name': '2"→1.25" Adapter', 'type': 'type_adapter', 'optical_length': 0, 'mass': 12, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_M42_Spacer_2_5mm': {'brand': 'Bresser', 'name': 'M42 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M42_Spacer_3_5mm': {'brand': 'Bresser', 'name': 'M42 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M42_Spacer_4mm': {'brand': 'Bresser', 'name': 'M42 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 7, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M42_Spacer_4_5mm': {'brand': 'Bresser', 'name': 'M42 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 7, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M42_Spacer_5_5mm': {'brand': 'Bresser', 'name': 'M42 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 8, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M42_Spacer_6mm': {'brand': 'Bresser', 'name': 'M42 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 8, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M42_Spacer_6_5mm': {'brand': 'Bresser', 'name': 'M42 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 9, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M42_Spacer_7mm': {'brand': 'Bresser', 'name': 'M42 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 9, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M42_Spacer_7_5mm': {'brand': 'Bresser', 'name': 'M42 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 10, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M42_Spacer_8mm': {'brand': 'Bresser', 'name': 'M42 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 10, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M42_Spacer_8_5mm': {'brand': 'Bresser', 'name': 'M42 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 10, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M42_Spacer_9mm': {'brand': 'Bresser', 'name': 'M42 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 11, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M42_Spacer_9_5mm': {'brand': 'Bresser', 'name': 'M42 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 11, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M42_Spacer_11mm': {'brand': 'Bresser', 'name': 'M42 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 12, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M42_Spacer_12mm': {'brand': 'Bresser', 'name': 'M42 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 13, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M42_Spacer_13mm': {'brand': 'Bresser', 'name': 'M42 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 14, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M42_Spacer_14mm': {'brand': 'Bresser', 'name': 'M42 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 15, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M42_Spacer_16mm': {'brand': 'Bresser', 'name': 'M42 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M42_Spacer_17mm': {'brand': 'Bresser', 'name': 'M42 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 17, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M42_Spacer_18mm': {'brand': 'Bresser', 'name': 'M42 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 18, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M42_Spacer_22mm': {'brand': 'Bresser', 'name': 'M42 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 21, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M42_Spacer_25mm': {'brand': 'Bresser', 'name': 'M42 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 24, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M48_Spacer_2_5mm': {'brand': 'Bresser', 'name': 'M48 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M48_Spacer_3_5mm': {'brand': 'Bresser', 'name': 'M48 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M48_Spacer_4mm': {'brand': 'Bresser', 'name': 'M48 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 9, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M48_Spacer_4_5mm': {'brand': 'Bresser', 'name': 'M48 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 9, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M48_Spacer_5_5mm': {'brand': 'Bresser', 'name': 'M48 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 10, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M48_Spacer_6mm': {'brand': 'Bresser', 'name': 'M48 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 10, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M48_Spacer_6_5mm': {'brand': 'Bresser', 'name': 'M48 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 11, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M48_Spacer_7mm': {'brand': 'Bresser', 'name': 'M48 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 11, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M48_Spacer_7_5mm': {'brand': 'Bresser', 'name': 'M48 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 12, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M48_Spacer_8mm': {'brand': 'Bresser', 'name': 'M48 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 12, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M48_Spacer_8_5mm': {'brand': 'Bresser', 'name': 'M48 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 12, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M48_Spacer_9mm': {'brand': 'Bresser', 'name': 'M48 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 13, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M48_Spacer_9_5mm': {'brand': 'Bresser', 'name': 'M48 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 13, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M48_Spacer_11mm': {'brand': 'Bresser', 'name': 'M48 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 14, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M48_Spacer_12mm': {'brand': 'Bresser', 'name': 'M48 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 15, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M48_Spacer_13mm': {'brand': 'Bresser', 'name': 'M48 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 16, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M48_Spacer_14mm': {'brand': 'Bresser', 'name': 'M48 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 17, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M48_Spacer_16mm': {'brand': 'Bresser', 'name': 'M48 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M48_Spacer_17mm': {'brand': 'Bresser', 'name': 'M48 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 19, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M48_Spacer_18mm': {'brand': 'Bresser', 'name': 'M48 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 20, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M48_Spacer_22mm': {'brand': 'Bresser', 'name': 'M48 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 23, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M48_Spacer_25mm': {'brand': 'Bresser', 'name': 'M48 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 26, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_M42_Extension_Tube_3mm': {'brand': 'Bresser', 'name': 'M42 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 11, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_M42_Extension_Tube_6mm': {'brand': 'Bresser', 'name': 'M42 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 12, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_M42_Extension_Tube_9mm': {'brand': 'Bresser', 'name': 'M42 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 13, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_M42_Extension_Tube_11mm': {'brand': 'Bresser', 'name': 'M42 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 14, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_M42_Extension_Tube_13mm': {'brand': 'Bresser', 'name': 'M42 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 14, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_M42_Extension_Tube_16mm': {'brand': 'Bresser', 'name': 'M42 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 15, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_M42_Extension_Tube_22mm': {'brand': 'Bresser', 'name': 'M42 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 17, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_M42_Extension_Tube_28mm': {'brand': 'Bresser', 'name': 'M42 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 19, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_M42_Extension_Tube_35mm': {'brand': 'Bresser', 'name': 'M42 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 21, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_M42_Extension_Tube_45mm': {'brand': 'Bresser', 'name': 'M42 Extension Tube 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 24, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_M48_Extension_Tube_3mm': {'brand': 'Bresser', 'name': 'M48 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 15, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_M48_Extension_Tube_6mm': {'brand': 'Bresser', 'name': 'M48 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 16, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_M48_Extension_Tube_9mm': {'brand': 'Bresser', 'name': 'M48 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 17, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_M48_Extension_Tube_11mm': {'brand': 'Bresser', 'name': 'M48 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_M48_Extension_Tube_13mm': {'brand': 'Bresser', 'name': 'M48 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_M48_Extension_Tube_16mm': {'brand': 'Bresser', 'name': 'M48 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 19, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_M48_Extension_Tube_22mm': {'brand': 'Bresser', 'name': 'M48 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 21, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_M48_Extension_Tube_28mm': {'brand': 'Bresser', 'name': 'M48 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 23, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_M48_Extension_Tube_35mm': {'brand': 'Bresser', 'name': 'M48 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 25, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_M48_Extension_Tube_45mm': {'brand': 'Bresser', 'name': 'M48 Extension Tube 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 28, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_M54_Extension_Tube_3mm': {'brand': 'Bresser', 'name': 'M54 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 19, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_M54_Extension_Tube_6mm': {'brand': 'Bresser', 'name': 'M54 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 20, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_M54_Extension_Tube_9mm': {'brand': 'Bresser', 'name': 'M54 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 21, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_M54_Extension_Tube_11mm': {'brand': 'Bresser', 'name': 'M54 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 22, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_M54_Extension_Tube_13mm': {'brand': 'Bresser', 'name': 'M54 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 22, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_M54_Extension_Tube_16mm': {'brand': 'Bresser', 'name': 'M54 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 23, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_M54_Extension_Tube_22mm': {'brand': 'Bresser', 'name': 'M54 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 25, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_M54_Extension_Tube_28mm': {'brand': 'Bresser', 'name': 'M54 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 27, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_M54_Extension_Tube_35mm': {'brand': 'Bresser', 'name': 'M54 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 29, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_M54_Extension_Tube_45mm': {'brand': 'Bresser', 'name': 'M54 Extension Tube 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 32, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Bresser_1_25_Spacer_3mm': {'brand': 'Bresser', 'name': '1.25" Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 5, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_1_25_Spacer_4mm': {'brand': 'Bresser', 'name': '1.25" Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 6, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_1_25_Spacer_5mm': {'brand': 'Bresser', 'name': '1.25" Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 7, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_1_25_Spacer_6mm': {'brand': 'Bresser', 'name': '1.25" Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 7, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_1_25_Spacer_7mm': {'brand': 'Bresser', 'name': '1.25" Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 8, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_1_25_Spacer_8mm': {'brand': 'Bresser', 'name': '1.25" Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 9, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_1_25_Spacer_9mm': {'brand': 'Bresser', 'name': '1.25" Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 10, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_1_25_Spacer_10mm': {'brand': 'Bresser', 'name': '1.25" Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 11, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_1_25_Spacer_12mm': {'brand': 'Bresser', 'name': '1.25" Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 12, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_1_25_Spacer_15mm': {'brand': 'Bresser', 'name': '1.25" Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 15, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_1_25_Spacer_18mm': {'brand': 'Bresser', 'name': '1.25" Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 17, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_1_25_Spacer_20mm': {'brand': 'Bresser', 'name': '1.25" Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 19, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_1_25_Spacer_25mm': {'brand': 'Bresser', 'name': '1.25" Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 23, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_2_Spacer_3mm': {'brand': 'Bresser', 'name': '2" Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 10, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_2_Spacer_4mm': {'brand': 'Bresser', 'name': '2" Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 11, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_2_Spacer_5mm': {'brand': 'Bresser', 'name': '2" Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 12, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_2_Spacer_6mm': {'brand': 'Bresser', 'name': '2" Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 12, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_2_Spacer_7mm': {'brand': 'Bresser', 'name': '2" Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 13, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_2_Spacer_8mm': {'brand': 'Bresser', 'name': '2" Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 14, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_2_Spacer_9mm': {'brand': 'Bresser', 'name': '2" Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 15, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_2_Spacer_10mm': {'brand': 'Bresser', 'name': '2" Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 16, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_2_Spacer_12mm': {'brand': 'Bresser', 'name': '2" Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 17, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_2_Spacer_15mm': {'brand': 'Bresser', 'name': '2" Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 20, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_2_Spacer_18mm': {'brand': 'Bresser', 'name': '2" Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 22, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_2_Spacer_20mm': {'brand': 'Bresser', 'name': '2" Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 24, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_2_Spacer_25mm': {'brand': 'Bresser', 'name': '2" Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 28, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}}

    @classmethod
    def Bresser_T2_Ring_Canon_EOS(cls):
        return cls.from_database(cls._DATABASE['Bresser_T2_Ring_Canon_EOS'])

    @classmethod
    def Bresser_T2_Ring_Nikon_F(cls):
        return cls.from_database(cls._DATABASE['Bresser_T2_Ring_Nikon_F'])

    @classmethod
    def Bresser_T2_Ring_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Bresser_T2_Ring_Sony_E'])

    @classmethod
    def Bresser_1_25_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['Bresser_1_25_M42_Adapter'])

    @classmethod
    def Bresser_M42_M48_Adapter(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_M48_Adapter'])

    @classmethod
    def Bresser_M42_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_Spacer_5mm'])

    @classmethod
    def Bresser_M42_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_Spacer_10mm'])

    @classmethod
    def Bresser_M42_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_Spacer_15mm'])

    @classmethod
    def Bresser_M42_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_Spacer_20mm'])

    @classmethod
    def Bresser_M48_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_Spacer_5mm'])

    @classmethod
    def Bresser_M48_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_Spacer_10mm'])

    @classmethod
    def Bresser_M48_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_Spacer_15mm'])

    @classmethod
    def Bresser_M48_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_Spacer_20mm'])

    @classmethod
    def Bresser_T_Ring_Canon_RF(cls):
        return cls.from_database(cls._DATABASE['Bresser_T_Ring_Canon_RF'])

    @classmethod
    def Bresser_T_Ring_Nikon_Z(cls):
        return cls.from_database(cls._DATABASE['Bresser_T_Ring_Nikon_Z'])

    @classmethod
    def Bresser_T_Ring_Fuji_X(cls):
        return cls.from_database(cls._DATABASE['Bresser_T_Ring_Fuji_X'])

    @classmethod
    def Bresser_T_Ring_MFT(cls):
        return cls.from_database(cls._DATABASE['Bresser_T_Ring_MFT'])

    @classmethod
    def Bresser_EOS_M42_T_Ring(cls):
        return cls.from_database(cls._DATABASE['Bresser_EOS_M42_T_Ring'])

    @classmethod
    def Bresser_Nikon_F_M42_T_Ring(cls):
        return cls.from_database(cls._DATABASE['Bresser_Nikon_F_M42_T_Ring'])

    @classmethod
    def Bresser_M48_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_M42_Adapter'])

    @classmethod
    def Bresser_SC_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['Bresser_SC_M42_Adapter'])

    @classmethod
    def Bresser_2_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['Bresser_2_M42_Adapter'])

    @classmethod
    def Bresser_2_1_25_Adapter(cls):
        return cls.from_database(cls._DATABASE['Bresser_2_1_25_Adapter'])

    @classmethod
    def Bresser_M42_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_Spacer_2_5mm'])

    @classmethod
    def Bresser_M42_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_Spacer_3_5mm'])

    @classmethod
    def Bresser_M42_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_Spacer_4mm'])

    @classmethod
    def Bresser_M42_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_Spacer_4_5mm'])

    @classmethod
    def Bresser_M42_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_Spacer_5_5mm'])

    @classmethod
    def Bresser_M42_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_Spacer_6mm'])

    @classmethod
    def Bresser_M42_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_Spacer_6_5mm'])

    @classmethod
    def Bresser_M42_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_Spacer_7mm'])

    @classmethod
    def Bresser_M42_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_Spacer_7_5mm'])

    @classmethod
    def Bresser_M42_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_Spacer_8mm'])

    @classmethod
    def Bresser_M42_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_Spacer_8_5mm'])

    @classmethod
    def Bresser_M42_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_Spacer_9mm'])

    @classmethod
    def Bresser_M42_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_Spacer_9_5mm'])

    @classmethod
    def Bresser_M42_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_Spacer_11mm'])

    @classmethod
    def Bresser_M42_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_Spacer_12mm'])

    @classmethod
    def Bresser_M42_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_Spacer_13mm'])

    @classmethod
    def Bresser_M42_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_Spacer_14mm'])

    @classmethod
    def Bresser_M42_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_Spacer_16mm'])

    @classmethod
    def Bresser_M42_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_Spacer_17mm'])

    @classmethod
    def Bresser_M42_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_Spacer_18mm'])

    @classmethod
    def Bresser_M42_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_Spacer_22mm'])

    @classmethod
    def Bresser_M42_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_Spacer_25mm'])

    @classmethod
    def Bresser_M48_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_Spacer_2_5mm'])

    @classmethod
    def Bresser_M48_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_Spacer_3_5mm'])

    @classmethod
    def Bresser_M48_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_Spacer_4mm'])

    @classmethod
    def Bresser_M48_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_Spacer_4_5mm'])

    @classmethod
    def Bresser_M48_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_Spacer_5_5mm'])

    @classmethod
    def Bresser_M48_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_Spacer_6mm'])

    @classmethod
    def Bresser_M48_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_Spacer_6_5mm'])

    @classmethod
    def Bresser_M48_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_Spacer_7mm'])

    @classmethod
    def Bresser_M48_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_Spacer_7_5mm'])

    @classmethod
    def Bresser_M48_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_Spacer_8mm'])

    @classmethod
    def Bresser_M48_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_Spacer_8_5mm'])

    @classmethod
    def Bresser_M48_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_Spacer_9mm'])

    @classmethod
    def Bresser_M48_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_Spacer_9_5mm'])

    @classmethod
    def Bresser_M48_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_Spacer_11mm'])

    @classmethod
    def Bresser_M48_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_Spacer_12mm'])

    @classmethod
    def Bresser_M48_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_Spacer_13mm'])

    @classmethod
    def Bresser_M48_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_Spacer_14mm'])

    @classmethod
    def Bresser_M48_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_Spacer_16mm'])

    @classmethod
    def Bresser_M48_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_Spacer_17mm'])

    @classmethod
    def Bresser_M48_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_Spacer_18mm'])

    @classmethod
    def Bresser_M48_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_Spacer_22mm'])

    @classmethod
    def Bresser_M48_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_Spacer_25mm'])

    @classmethod
    def Bresser_M42_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_Extension_Tube_3mm'])

    @classmethod
    def Bresser_M42_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_Extension_Tube_6mm'])

    @classmethod
    def Bresser_M42_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_Extension_Tube_9mm'])

    @classmethod
    def Bresser_M42_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_Extension_Tube_11mm'])

    @classmethod
    def Bresser_M42_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_Extension_Tube_13mm'])

    @classmethod
    def Bresser_M42_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_Extension_Tube_16mm'])

    @classmethod
    def Bresser_M42_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_Extension_Tube_22mm'])

    @classmethod
    def Bresser_M42_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_Extension_Tube_28mm'])

    @classmethod
    def Bresser_M42_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_Extension_Tube_35mm'])

    @classmethod
    def Bresser_M42_Extension_Tube_45mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_Extension_Tube_45mm'])

    @classmethod
    def Bresser_M48_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_Extension_Tube_3mm'])

    @classmethod
    def Bresser_M48_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_Extension_Tube_6mm'])

    @classmethod
    def Bresser_M48_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_Extension_Tube_9mm'])

    @classmethod
    def Bresser_M48_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_Extension_Tube_11mm'])

    @classmethod
    def Bresser_M48_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_Extension_Tube_13mm'])

    @classmethod
    def Bresser_M48_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_Extension_Tube_16mm'])

    @classmethod
    def Bresser_M48_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_Extension_Tube_22mm'])

    @classmethod
    def Bresser_M48_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_Extension_Tube_28mm'])

    @classmethod
    def Bresser_M48_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_Extension_Tube_35mm'])

    @classmethod
    def Bresser_M48_Extension_Tube_45mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_Extension_Tube_45mm'])

    @classmethod
    def Bresser_M54_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M54_Extension_Tube_3mm'])

    @classmethod
    def Bresser_M54_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M54_Extension_Tube_6mm'])

    @classmethod
    def Bresser_M54_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M54_Extension_Tube_9mm'])

    @classmethod
    def Bresser_M54_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M54_Extension_Tube_11mm'])

    @classmethod
    def Bresser_M54_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M54_Extension_Tube_13mm'])

    @classmethod
    def Bresser_M54_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M54_Extension_Tube_16mm'])

    @classmethod
    def Bresser_M54_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M54_Extension_Tube_22mm'])

    @classmethod
    def Bresser_M54_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M54_Extension_Tube_28mm'])

    @classmethod
    def Bresser_M54_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M54_Extension_Tube_35mm'])

    @classmethod
    def Bresser_M54_Extension_Tube_45mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M54_Extension_Tube_45mm'])

    @classmethod
    def Bresser_1_25_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_1_25_Spacer_3mm'])

    @classmethod
    def Bresser_1_25_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_1_25_Spacer_4mm'])

    @classmethod
    def Bresser_1_25_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_1_25_Spacer_5mm'])

    @classmethod
    def Bresser_1_25_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_1_25_Spacer_6mm'])

    @classmethod
    def Bresser_1_25_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_1_25_Spacer_7mm'])

    @classmethod
    def Bresser_1_25_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_1_25_Spacer_8mm'])

    @classmethod
    def Bresser_1_25_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_1_25_Spacer_9mm'])

    @classmethod
    def Bresser_1_25_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_1_25_Spacer_10mm'])

    @classmethod
    def Bresser_1_25_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_1_25_Spacer_12mm'])

    @classmethod
    def Bresser_1_25_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_1_25_Spacer_15mm'])

    @classmethod
    def Bresser_1_25_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_1_25_Spacer_18mm'])

    @classmethod
    def Bresser_1_25_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_1_25_Spacer_20mm'])

    @classmethod
    def Bresser_1_25_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_1_25_Spacer_25mm'])

    @classmethod
    def Bresser_2_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_2_Spacer_3mm'])

    @classmethod
    def Bresser_2_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_2_Spacer_4mm'])

    @classmethod
    def Bresser_2_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_2_Spacer_5mm'])

    @classmethod
    def Bresser_2_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_2_Spacer_6mm'])

    @classmethod
    def Bresser_2_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_2_Spacer_7mm'])

    @classmethod
    def Bresser_2_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_2_Spacer_8mm'])

    @classmethod
    def Bresser_2_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_2_Spacer_9mm'])

    @classmethod
    def Bresser_2_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_2_Spacer_10mm'])

    @classmethod
    def Bresser_2_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_2_Spacer_12mm'])

    @classmethod
    def Bresser_2_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_2_Spacer_15mm'])

    @classmethod
    def Bresser_2_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_2_Spacer_18mm'])

    @classmethod
    def Bresser_2_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_2_Spacer_20mm'])

    @classmethod
    def Bresser_2_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_2_Spacer_25mm'])

class BresserSpacer(Spacer):
    _DATABASE = {'Bresser_M42_Spacer_1mm': {'brand': 'Bresser', 'name': 'M42 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Bresser_M42_Spacer_2mm': {'brand': 'Bresser', 'name': 'M42 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Bresser_M48_Spacer_1mm': {'brand': 'Bresser', 'name': 'M48 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Bresser_M48_Spacer_2mm': {'brand': 'Bresser', 'name': 'M48 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Bresser_M42_Spacer_0_5mm': {'brand': 'Bresser', 'name': 'M42 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Bresser_M42_Spacer_0_7mm': {'brand': 'Bresser', 'name': 'M42 Spacer 0.7mm', 'type': 'type_spacer', 'optical_length': 0.7, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Bresser_M42_Spacer_1_5mm': {'brand': 'Bresser', 'name': 'M42 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Bresser_M48_Spacer_0_5mm': {'brand': 'Bresser', 'name': 'M48 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Bresser_M48_Spacer_0_7mm': {'brand': 'Bresser', 'name': 'M48 Spacer 0.7mm', 'type': 'type_spacer', 'optical_length': 0.7, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Bresser_M48_Spacer_1_5mm': {'brand': 'Bresser', 'name': 'M48 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Bresser_1_25_Spacer_0_5mm': {'brand': 'Bresser', 'name': '1.25" Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 4, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_1_25_Spacer_1mm': {'brand': 'Bresser', 'name': '1.25" Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 4, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_1_25_Spacer_1_5mm': {'brand': 'Bresser', 'name': '1.25" Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 4, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_1_25_Spacer_2mm': {'brand': 'Bresser', 'name': '1.25" Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 4, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_2_Spacer_0_5mm': {'brand': 'Bresser', 'name': '2" Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 9, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_2_Spacer_1mm': {'brand': 'Bresser', 'name': '2" Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 9, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_2_Spacer_1_5mm': {'brand': 'Bresser', 'name': '2" Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 9, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Bresser_2_Spacer_2mm': {'brand': 'Bresser', 'name': '2" Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 9, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}}

    @classmethod
    def Bresser_M42_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_Spacer_1mm'])

    @classmethod
    def Bresser_M42_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_Spacer_2mm'])

    @classmethod
    def Bresser_M48_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_Spacer_1mm'])

    @classmethod
    def Bresser_M48_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_Spacer_2mm'])

    @classmethod
    def Bresser_M42_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_Spacer_0_5mm'])

    @classmethod
    def Bresser_M42_Spacer_0_7mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_Spacer_0_7mm'])

    @classmethod
    def Bresser_M42_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M42_Spacer_1_5mm'])

    @classmethod
    def Bresser_M48_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_Spacer_0_5mm'])

    @classmethod
    def Bresser_M48_Spacer_0_7mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_Spacer_0_7mm'])

    @classmethod
    def Bresser_M48_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_M48_Spacer_1_5mm'])

    @classmethod
    def Bresser_1_25_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_1_25_Spacer_0_5mm'])

    @classmethod
    def Bresser_1_25_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_1_25_Spacer_1mm'])

    @classmethod
    def Bresser_1_25_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_1_25_Spacer_1_5mm'])

    @classmethod
    def Bresser_1_25_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_1_25_Spacer_2mm'])

    @classmethod
    def Bresser_2_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_2_Spacer_0_5mm'])

    @classmethod
    def Bresser_2_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_2_Spacer_1mm'])

    @classmethod
    def Bresser_2_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_2_Spacer_1_5mm'])

    @classmethod
    def Bresser_2_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Bresser_2_Spacer_2mm'])