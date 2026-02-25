from ...abstract import IntermediateOpticalEquipment
from ....constants import OpticalType
from ..base import Adapter, Spacer

class PrimaluceAdapter(Adapter):
    _DATABASE = {'PrimaLuce_M42_M48_Adapter': {'brand': 'PrimaLuce', 'name': 'M42→M48 Adapter', 'type': 'type_adapter', 'optical_length': 5, 'mass': 20, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'PrimaLuce_M48_M54_Adapter': {'brand': 'PrimaLuce', 'name': 'M48→M54 Adapter', 'type': 'type_adapter', 'optical_length': 7, 'mass': 25, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'PrimaLuce_M54_M68_Adapter': {'brand': 'PrimaLuce', 'name': 'M54→M68 Adapter', 'type': 'type_adapter', 'optical_length': 8, 'mass': 30, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'PrimaLuce_M42_M54_Adapter': {'brand': 'PrimaLuce', 'name': 'M42→M54 Adapter', 'type': 'type_adapter', 'optical_length': 10, 'mass': 25, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'PrimaLuce_M48_M68_Adapter': {'brand': 'PrimaLuce', 'name': 'M48→M68 Adapter', 'type': 'type_adapter', 'optical_length': 10, 'mass': 30, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'PrimaLuce_M42_Spacer_3mm': {'brand': 'PrimaLuce', 'name': 'M42 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M42_Spacer_5mm': {'brand': 'PrimaLuce', 'name': 'M42 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 8, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M42_Spacer_7mm': {'brand': 'PrimaLuce', 'name': 'M42 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 9, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M42_Spacer_10mm': {'brand': 'PrimaLuce', 'name': 'M42 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 12, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M42_Spacer_15mm': {'brand': 'PrimaLuce', 'name': 'M42 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M42_Spacer_20mm': {'brand': 'PrimaLuce', 'name': 'M42 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 20, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M48_Spacer_3mm': {'brand': 'PrimaLuce', 'name': 'M48 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M48_Spacer_5mm': {'brand': 'PrimaLuce', 'name': 'M48 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 10, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M48_Spacer_7mm': {'brand': 'PrimaLuce', 'name': 'M48 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 11, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M48_Spacer_10mm': {'brand': 'PrimaLuce', 'name': 'M48 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 14, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M48_Spacer_15mm': {'brand': 'PrimaLuce', 'name': 'M48 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M48_Spacer_20mm': {'brand': 'PrimaLuce', 'name': 'M48 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 22, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M54_Spacer_5mm': {'brand': 'PrimaLuce', 'name': 'M54 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 12, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M54_Spacer_10mm': {'brand': 'PrimaLuce', 'name': 'M54 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 16, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M54_Spacer_15mm': {'brand': 'PrimaLuce', 'name': 'M54 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 20, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M54_Spacer_20mm': {'brand': 'PrimaLuce', 'name': 'M54 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 24, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M56_Spacer_5mm': {'brand': 'PrimaLuce', 'name': 'M56 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 12, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M56_Spacer_10mm': {'brand': 'PrimaLuce', 'name': 'M56 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 16, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M56_Spacer_15mm': {'brand': 'PrimaLuce', 'name': 'M56 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 20, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M56_Spacer_20mm': {'brand': 'PrimaLuce', 'name': 'M56 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 24, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M56_M48_Adapter': {'brand': 'PrimaLuce', 'name': 'M56→M48 Adapter', 'type': 'type_adapter', 'optical_length': 3, 'mass': 30, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'PrimaLuce_M56_M54_Adapter': {'brand': 'PrimaLuce', 'name': 'M56→M54 Adapter', 'type': 'type_adapter', 'optical_length': 2, 'mass': 28, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'PrimaLuce_M56_M42_Adapter': {'brand': 'PrimaLuce', 'name': 'M56→M42 Adapter', 'type': 'type_adapter', 'optical_length': 5, 'mass': 25, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'PrimaLuce_M56_EOS_Adapter': {'brand': 'PrimaLuce', 'name': 'M56→EOS Adapter', 'type': 'type_adapter', 'optical_length': 8, 'mass': 35, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'PrimaLuce_M56_Nikon_F_Adapter': {'brand': 'PrimaLuce', 'name': 'M56→Nikon F Adapter', 'type': 'type_adapter', 'optical_length': 8, 'mass': 35, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'PrimaLuce_M56_Sony_E_Adapter': {'brand': 'PrimaLuce', 'name': 'M56→Sony E Adapter', 'type': 'type_adapter', 'optical_length': 7, 'mass': 30, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'PrimaLuce_M56_Canon_RF_Adapter': {'brand': 'PrimaLuce', 'name': 'M56→Canon RF Adapter', 'type': 'type_adapter', 'optical_length': 5, 'mass': 28, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'PrimaLuce_M56_Nikon_Z_Adapter': {'brand': 'PrimaLuce', 'name': 'M56→Nikon Z Adapter', 'type': 'type_adapter', 'optical_length': 6, 'mass': 28, 'tside_thread': 'Nikon Z', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'PrimaLuce_M42_Spacer_2_5mm': {'brand': 'PrimaLuce', 'name': 'M42 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M42_Spacer_3_5mm': {'brand': 'PrimaLuce', 'name': 'M42 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M42_Spacer_4mm': {'brand': 'PrimaLuce', 'name': 'M42 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 7, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M42_Spacer_4_5mm': {'brand': 'PrimaLuce', 'name': 'M42 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 7, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M42_Spacer_5_5mm': {'brand': 'PrimaLuce', 'name': 'M42 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 8, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M42_Spacer_6mm': {'brand': 'PrimaLuce', 'name': 'M42 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 8, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M42_Spacer_6_5mm': {'brand': 'PrimaLuce', 'name': 'M42 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 9, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M42_Spacer_7_5mm': {'brand': 'PrimaLuce', 'name': 'M42 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 10, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M42_Spacer_8mm': {'brand': 'PrimaLuce', 'name': 'M42 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 10, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M42_Spacer_8_5mm': {'brand': 'PrimaLuce', 'name': 'M42 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 10, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M42_Spacer_9mm': {'brand': 'PrimaLuce', 'name': 'M42 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 11, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M42_Spacer_9_5mm': {'brand': 'PrimaLuce', 'name': 'M42 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 11, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M42_Spacer_11mm': {'brand': 'PrimaLuce', 'name': 'M42 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 12, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M42_Spacer_12mm': {'brand': 'PrimaLuce', 'name': 'M42 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 13, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M42_Spacer_13mm': {'brand': 'PrimaLuce', 'name': 'M42 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 14, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M42_Spacer_14mm': {'brand': 'PrimaLuce', 'name': 'M42 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 15, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M42_Spacer_16mm': {'brand': 'PrimaLuce', 'name': 'M42 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M42_Spacer_17mm': {'brand': 'PrimaLuce', 'name': 'M42 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 17, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M42_Spacer_18mm': {'brand': 'PrimaLuce', 'name': 'M42 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 18, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M42_Spacer_22mm': {'brand': 'PrimaLuce', 'name': 'M42 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 21, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M42_Spacer_25mm': {'brand': 'PrimaLuce', 'name': 'M42 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 24, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M42_Spacer_28mm': {'brand': 'PrimaLuce', 'name': 'M42 Spacer 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 26, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M42_Spacer_30mm': {'brand': 'PrimaLuce', 'name': 'M42 Spacer 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 28, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M48_Spacer_2_5mm': {'brand': 'PrimaLuce', 'name': 'M48 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M48_Spacer_3_5mm': {'brand': 'PrimaLuce', 'name': 'M48 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M48_Spacer_4mm': {'brand': 'PrimaLuce', 'name': 'M48 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 9, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M48_Spacer_4_5mm': {'brand': 'PrimaLuce', 'name': 'M48 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 9, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M48_Spacer_5_5mm': {'brand': 'PrimaLuce', 'name': 'M48 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 10, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M48_Spacer_6mm': {'brand': 'PrimaLuce', 'name': 'M48 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 10, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M48_Spacer_6_5mm': {'brand': 'PrimaLuce', 'name': 'M48 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 11, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M48_Spacer_7_5mm': {'brand': 'PrimaLuce', 'name': 'M48 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 12, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M48_Spacer_8mm': {'brand': 'PrimaLuce', 'name': 'M48 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 12, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M48_Spacer_8_5mm': {'brand': 'PrimaLuce', 'name': 'M48 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 12, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M48_Spacer_9mm': {'brand': 'PrimaLuce', 'name': 'M48 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 13, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M48_Spacer_9_5mm': {'brand': 'PrimaLuce', 'name': 'M48 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 13, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M48_Spacer_11mm': {'brand': 'PrimaLuce', 'name': 'M48 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 14, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M48_Spacer_12mm': {'brand': 'PrimaLuce', 'name': 'M48 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 15, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M48_Spacer_13mm': {'brand': 'PrimaLuce', 'name': 'M48 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 16, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M48_Spacer_14mm': {'brand': 'PrimaLuce', 'name': 'M48 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 17, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M48_Spacer_16mm': {'brand': 'PrimaLuce', 'name': 'M48 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M48_Spacer_17mm': {'brand': 'PrimaLuce', 'name': 'M48 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 19, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M48_Spacer_18mm': {'brand': 'PrimaLuce', 'name': 'M48 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 20, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M48_Spacer_22mm': {'brand': 'PrimaLuce', 'name': 'M48 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 23, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M48_Spacer_25mm': {'brand': 'PrimaLuce', 'name': 'M48 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 26, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M48_Spacer_28mm': {'brand': 'PrimaLuce', 'name': 'M48 Spacer 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 28, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M48_Spacer_30mm': {'brand': 'PrimaLuce', 'name': 'M48 Spacer 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 30, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M54_Spacer_2_5mm': {'brand': 'PrimaLuce', 'name': 'M54 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 10, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M54_Spacer_3mm': {'brand': 'PrimaLuce', 'name': 'M54 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 10, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M54_Spacer_3_5mm': {'brand': 'PrimaLuce', 'name': 'M54 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 10, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M54_Spacer_4mm': {'brand': 'PrimaLuce', 'name': 'M54 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 11, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M54_Spacer_4_5mm': {'brand': 'PrimaLuce', 'name': 'M54 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 11, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M54_Spacer_5_5mm': {'brand': 'PrimaLuce', 'name': 'M54 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 12, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M54_Spacer_6mm': {'brand': 'PrimaLuce', 'name': 'M54 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 12, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M54_Spacer_6_5mm': {'brand': 'PrimaLuce', 'name': 'M54 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 13, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M54_Spacer_7mm': {'brand': 'PrimaLuce', 'name': 'M54 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 13, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M54_Spacer_7_5mm': {'brand': 'PrimaLuce', 'name': 'M54 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 14, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M54_Spacer_8mm': {'brand': 'PrimaLuce', 'name': 'M54 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 14, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M54_Spacer_8_5mm': {'brand': 'PrimaLuce', 'name': 'M54 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 14, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M54_Spacer_9mm': {'brand': 'PrimaLuce', 'name': 'M54 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 15, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M54_Spacer_9_5mm': {'brand': 'PrimaLuce', 'name': 'M54 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 15, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M54_Spacer_11mm': {'brand': 'PrimaLuce', 'name': 'M54 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 16, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M54_Spacer_12mm': {'brand': 'PrimaLuce', 'name': 'M54 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 17, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M54_Spacer_13mm': {'brand': 'PrimaLuce', 'name': 'M54 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 18, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M54_Spacer_14mm': {'brand': 'PrimaLuce', 'name': 'M54 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 19, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M54_Spacer_16mm': {'brand': 'PrimaLuce', 'name': 'M54 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 20, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M54_Spacer_17mm': {'brand': 'PrimaLuce', 'name': 'M54 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 21, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M54_Spacer_18mm': {'brand': 'PrimaLuce', 'name': 'M54 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 22, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M54_Spacer_22mm': {'brand': 'PrimaLuce', 'name': 'M54 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 25, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M54_Spacer_25mm': {'brand': 'PrimaLuce', 'name': 'M54 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 28, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M54_Spacer_28mm': {'brand': 'PrimaLuce', 'name': 'M54 Spacer 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 30, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M54_Spacer_30mm': {'brand': 'PrimaLuce', 'name': 'M54 Spacer 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 32, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M56_Spacer_2_5mm': {'brand': 'PrimaLuce', 'name': 'M56 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 10, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M56_Spacer_3mm': {'brand': 'PrimaLuce', 'name': 'M56 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 10, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M56_Spacer_3_5mm': {'brand': 'PrimaLuce', 'name': 'M56 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 10, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M56_Spacer_4mm': {'brand': 'PrimaLuce', 'name': 'M56 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 11, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M56_Spacer_4_5mm': {'brand': 'PrimaLuce', 'name': 'M56 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 11, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M56_Spacer_5_5mm': {'brand': 'PrimaLuce', 'name': 'M56 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 12, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M56_Spacer_6mm': {'brand': 'PrimaLuce', 'name': 'M56 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 12, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M56_Spacer_6_5mm': {'brand': 'PrimaLuce', 'name': 'M56 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 13, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M56_Spacer_7mm': {'brand': 'PrimaLuce', 'name': 'M56 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 13, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M56_Spacer_7_5mm': {'brand': 'PrimaLuce', 'name': 'M56 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 14, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M56_Spacer_8mm': {'brand': 'PrimaLuce', 'name': 'M56 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 14, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M56_Spacer_8_5mm': {'brand': 'PrimaLuce', 'name': 'M56 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 14, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M56_Spacer_9mm': {'brand': 'PrimaLuce', 'name': 'M56 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 15, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M56_Spacer_9_5mm': {'brand': 'PrimaLuce', 'name': 'M56 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 15, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M56_Spacer_11mm': {'brand': 'PrimaLuce', 'name': 'M56 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 16, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M56_Spacer_12mm': {'brand': 'PrimaLuce', 'name': 'M56 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 17, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M56_Spacer_13mm': {'brand': 'PrimaLuce', 'name': 'M56 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 18, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M56_Spacer_14mm': {'brand': 'PrimaLuce', 'name': 'M56 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 19, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M56_Spacer_16mm': {'brand': 'PrimaLuce', 'name': 'M56 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 20, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M56_Spacer_17mm': {'brand': 'PrimaLuce', 'name': 'M56 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 21, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M56_Spacer_18mm': {'brand': 'PrimaLuce', 'name': 'M56 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 22, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M56_Spacer_22mm': {'brand': 'PrimaLuce', 'name': 'M56 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 25, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M56_Spacer_25mm': {'brand': 'PrimaLuce', 'name': 'M56 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 28, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M56_Spacer_28mm': {'brand': 'PrimaLuce', 'name': 'M56 Spacer 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 30, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M56_Spacer_30mm': {'brand': 'PrimaLuce', 'name': 'M56 Spacer 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 32, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M68_Spacer_2_5mm': {'brand': 'PrimaLuce', 'name': 'M68 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 12, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M68_Spacer_3mm': {'brand': 'PrimaLuce', 'name': 'M68 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 12, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M68_Spacer_3_5mm': {'brand': 'PrimaLuce', 'name': 'M68 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 12, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M68_Spacer_4mm': {'brand': 'PrimaLuce', 'name': 'M68 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 13, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M68_Spacer_4_5mm': {'brand': 'PrimaLuce', 'name': 'M68 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 13, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M68_Spacer_5_5mm': {'brand': 'PrimaLuce', 'name': 'M68 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 14, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M68_Spacer_6mm': {'brand': 'PrimaLuce', 'name': 'M68 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 14, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M68_Spacer_6_5mm': {'brand': 'PrimaLuce', 'name': 'M68 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 15, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M68_Spacer_7mm': {'brand': 'PrimaLuce', 'name': 'M68 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 15, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M68_Spacer_7_5mm': {'brand': 'PrimaLuce', 'name': 'M68 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 16, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M68_Spacer_8mm': {'brand': 'PrimaLuce', 'name': 'M68 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 16, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M68_Spacer_8_5mm': {'brand': 'PrimaLuce', 'name': 'M68 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 16, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M68_Spacer_9mm': {'brand': 'PrimaLuce', 'name': 'M68 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 17, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M68_Spacer_9_5mm': {'brand': 'PrimaLuce', 'name': 'M68 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 17, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M68_Spacer_11mm': {'brand': 'PrimaLuce', 'name': 'M68 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 18, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M68_Spacer_12mm': {'brand': 'PrimaLuce', 'name': 'M68 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 19, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M68_Spacer_13mm': {'brand': 'PrimaLuce', 'name': 'M68 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 20, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M68_Spacer_14mm': {'brand': 'PrimaLuce', 'name': 'M68 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 21, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M68_Spacer_16mm': {'brand': 'PrimaLuce', 'name': 'M68 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 22, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M68_Spacer_17mm': {'brand': 'PrimaLuce', 'name': 'M68 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 23, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M68_Spacer_18mm': {'brand': 'PrimaLuce', 'name': 'M68 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 24, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M68_Spacer_22mm': {'brand': 'PrimaLuce', 'name': 'M68 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 27, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M68_Spacer_25mm': {'brand': 'PrimaLuce', 'name': 'M68 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 30, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M68_Spacer_28mm': {'brand': 'PrimaLuce', 'name': 'M68 Spacer 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 32, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}}

    @classmethod
    def PrimaLuce_M42_M48_Adapter(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M42_M48_Adapter'])

    @classmethod
    def PrimaLuce_M48_M54_Adapter(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M48_M54_Adapter'])

    @classmethod
    def PrimaLuce_M54_M68_Adapter(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M54_M68_Adapter'])

    @classmethod
    def PrimaLuce_M42_M54_Adapter(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M42_M54_Adapter'])

    @classmethod
    def PrimaLuce_M48_M68_Adapter(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M48_M68_Adapter'])

    @classmethod
    def PrimaLuce_M42_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M42_Spacer_3mm'])

    @classmethod
    def PrimaLuce_M42_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M42_Spacer_5mm'])

    @classmethod
    def PrimaLuce_M42_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M42_Spacer_7mm'])

    @classmethod
    def PrimaLuce_M42_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M42_Spacer_10mm'])

    @classmethod
    def PrimaLuce_M42_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M42_Spacer_15mm'])

    @classmethod
    def PrimaLuce_M42_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M42_Spacer_20mm'])

    @classmethod
    def PrimaLuce_M48_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M48_Spacer_3mm'])

    @classmethod
    def PrimaLuce_M48_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M48_Spacer_5mm'])

    @classmethod
    def PrimaLuce_M48_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M48_Spacer_7mm'])

    @classmethod
    def PrimaLuce_M48_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M48_Spacer_10mm'])

    @classmethod
    def PrimaLuce_M48_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M48_Spacer_15mm'])

    @classmethod
    def PrimaLuce_M48_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M48_Spacer_20mm'])

    @classmethod
    def PrimaLuce_M54_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M54_Spacer_5mm'])

    @classmethod
    def PrimaLuce_M54_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M54_Spacer_10mm'])

    @classmethod
    def PrimaLuce_M54_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M54_Spacer_15mm'])

    @classmethod
    def PrimaLuce_M54_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M54_Spacer_20mm'])

    @classmethod
    def PrimaLuce_M56_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_Spacer_5mm'])

    @classmethod
    def PrimaLuce_M56_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_Spacer_10mm'])

    @classmethod
    def PrimaLuce_M56_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_Spacer_15mm'])

    @classmethod
    def PrimaLuce_M56_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_Spacer_20mm'])

    @classmethod
    def PrimaLuce_M56_M48_Adapter(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_M48_Adapter'])

    @classmethod
    def PrimaLuce_M56_M54_Adapter(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_M54_Adapter'])

    @classmethod
    def PrimaLuce_M56_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_M42_Adapter'])

    @classmethod
    def PrimaLuce_M56_EOS_Adapter(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_EOS_Adapter'])

    @classmethod
    def PrimaLuce_M56_Nikon_F_Adapter(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_Nikon_F_Adapter'])

    @classmethod
    def PrimaLuce_M56_Sony_E_Adapter(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_Sony_E_Adapter'])

    @classmethod
    def PrimaLuce_M56_Canon_RF_Adapter(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_Canon_RF_Adapter'])

    @classmethod
    def PrimaLuce_M56_Nikon_Z_Adapter(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_Nikon_Z_Adapter'])

    @classmethod
    def PrimaLuce_M42_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M42_Spacer_2_5mm'])

    @classmethod
    def PrimaLuce_M42_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M42_Spacer_3_5mm'])

    @classmethod
    def PrimaLuce_M42_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M42_Spacer_4mm'])

    @classmethod
    def PrimaLuce_M42_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M42_Spacer_4_5mm'])

    @classmethod
    def PrimaLuce_M42_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M42_Spacer_5_5mm'])

    @classmethod
    def PrimaLuce_M42_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M42_Spacer_6mm'])

    @classmethod
    def PrimaLuce_M42_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M42_Spacer_6_5mm'])

    @classmethod
    def PrimaLuce_M42_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M42_Spacer_7_5mm'])

    @classmethod
    def PrimaLuce_M42_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M42_Spacer_8mm'])

    @classmethod
    def PrimaLuce_M42_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M42_Spacer_8_5mm'])

    @classmethod
    def PrimaLuce_M42_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M42_Spacer_9mm'])

    @classmethod
    def PrimaLuce_M42_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M42_Spacer_9_5mm'])

    @classmethod
    def PrimaLuce_M42_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M42_Spacer_11mm'])

    @classmethod
    def PrimaLuce_M42_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M42_Spacer_12mm'])

    @classmethod
    def PrimaLuce_M42_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M42_Spacer_13mm'])

    @classmethod
    def PrimaLuce_M42_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M42_Spacer_14mm'])

    @classmethod
    def PrimaLuce_M42_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M42_Spacer_16mm'])

    @classmethod
    def PrimaLuce_M42_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M42_Spacer_17mm'])

    @classmethod
    def PrimaLuce_M42_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M42_Spacer_18mm'])

    @classmethod
    def PrimaLuce_M42_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M42_Spacer_22mm'])

    @classmethod
    def PrimaLuce_M42_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M42_Spacer_25mm'])

    @classmethod
    def PrimaLuce_M42_Spacer_28mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M42_Spacer_28mm'])

    @classmethod
    def PrimaLuce_M42_Spacer_30mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M42_Spacer_30mm'])

    @classmethod
    def PrimaLuce_M48_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M48_Spacer_2_5mm'])

    @classmethod
    def PrimaLuce_M48_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M48_Spacer_3_5mm'])

    @classmethod
    def PrimaLuce_M48_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M48_Spacer_4mm'])

    @classmethod
    def PrimaLuce_M48_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M48_Spacer_4_5mm'])

    @classmethod
    def PrimaLuce_M48_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M48_Spacer_5_5mm'])

    @classmethod
    def PrimaLuce_M48_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M48_Spacer_6mm'])

    @classmethod
    def PrimaLuce_M48_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M48_Spacer_6_5mm'])

    @classmethod
    def PrimaLuce_M48_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M48_Spacer_7_5mm'])

    @classmethod
    def PrimaLuce_M48_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M48_Spacer_8mm'])

    @classmethod
    def PrimaLuce_M48_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M48_Spacer_8_5mm'])

    @classmethod
    def PrimaLuce_M48_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M48_Spacer_9mm'])

    @classmethod
    def PrimaLuce_M48_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M48_Spacer_9_5mm'])

    @classmethod
    def PrimaLuce_M48_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M48_Spacer_11mm'])

    @classmethod
    def PrimaLuce_M48_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M48_Spacer_12mm'])

    @classmethod
    def PrimaLuce_M48_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M48_Spacer_13mm'])

    @classmethod
    def PrimaLuce_M48_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M48_Spacer_14mm'])

    @classmethod
    def PrimaLuce_M48_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M48_Spacer_16mm'])

    @classmethod
    def PrimaLuce_M48_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M48_Spacer_17mm'])

    @classmethod
    def PrimaLuce_M48_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M48_Spacer_18mm'])

    @classmethod
    def PrimaLuce_M48_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M48_Spacer_22mm'])

    @classmethod
    def PrimaLuce_M48_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M48_Spacer_25mm'])

    @classmethod
    def PrimaLuce_M48_Spacer_28mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M48_Spacer_28mm'])

    @classmethod
    def PrimaLuce_M48_Spacer_30mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M48_Spacer_30mm'])

    @classmethod
    def PrimaLuce_M54_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M54_Spacer_2_5mm'])

    @classmethod
    def PrimaLuce_M54_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M54_Spacer_3mm'])

    @classmethod
    def PrimaLuce_M54_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M54_Spacer_3_5mm'])

    @classmethod
    def PrimaLuce_M54_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M54_Spacer_4mm'])

    @classmethod
    def PrimaLuce_M54_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M54_Spacer_4_5mm'])

    @classmethod
    def PrimaLuce_M54_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M54_Spacer_5_5mm'])

    @classmethod
    def PrimaLuce_M54_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M54_Spacer_6mm'])

    @classmethod
    def PrimaLuce_M54_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M54_Spacer_6_5mm'])

    @classmethod
    def PrimaLuce_M54_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M54_Spacer_7mm'])

    @classmethod
    def PrimaLuce_M54_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M54_Spacer_7_5mm'])

    @classmethod
    def PrimaLuce_M54_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M54_Spacer_8mm'])

    @classmethod
    def PrimaLuce_M54_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M54_Spacer_8_5mm'])

    @classmethod
    def PrimaLuce_M54_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M54_Spacer_9mm'])

    @classmethod
    def PrimaLuce_M54_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M54_Spacer_9_5mm'])

    @classmethod
    def PrimaLuce_M54_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M54_Spacer_11mm'])

    @classmethod
    def PrimaLuce_M54_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M54_Spacer_12mm'])

    @classmethod
    def PrimaLuce_M54_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M54_Spacer_13mm'])

    @classmethod
    def PrimaLuce_M54_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M54_Spacer_14mm'])

    @classmethod
    def PrimaLuce_M54_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M54_Spacer_16mm'])

    @classmethod
    def PrimaLuce_M54_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M54_Spacer_17mm'])

    @classmethod
    def PrimaLuce_M54_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M54_Spacer_18mm'])

    @classmethod
    def PrimaLuce_M54_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M54_Spacer_22mm'])

    @classmethod
    def PrimaLuce_M54_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M54_Spacer_25mm'])

    @classmethod
    def PrimaLuce_M54_Spacer_28mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M54_Spacer_28mm'])

    @classmethod
    def PrimaLuce_M54_Spacer_30mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M54_Spacer_30mm'])

    @classmethod
    def PrimaLuce_M56_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_Spacer_2_5mm'])

    @classmethod
    def PrimaLuce_M56_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_Spacer_3mm'])

    @classmethod
    def PrimaLuce_M56_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_Spacer_3_5mm'])

    @classmethod
    def PrimaLuce_M56_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_Spacer_4mm'])

    @classmethod
    def PrimaLuce_M56_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_Spacer_4_5mm'])

    @classmethod
    def PrimaLuce_M56_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_Spacer_5_5mm'])

    @classmethod
    def PrimaLuce_M56_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_Spacer_6mm'])

    @classmethod
    def PrimaLuce_M56_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_Spacer_6_5mm'])

    @classmethod
    def PrimaLuce_M56_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_Spacer_7mm'])

    @classmethod
    def PrimaLuce_M56_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_Spacer_7_5mm'])

    @classmethod
    def PrimaLuce_M56_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_Spacer_8mm'])

    @classmethod
    def PrimaLuce_M56_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_Spacer_8_5mm'])

    @classmethod
    def PrimaLuce_M56_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_Spacer_9mm'])

    @classmethod
    def PrimaLuce_M56_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_Spacer_9_5mm'])

    @classmethod
    def PrimaLuce_M56_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_Spacer_11mm'])

    @classmethod
    def PrimaLuce_M56_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_Spacer_12mm'])

    @classmethod
    def PrimaLuce_M56_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_Spacer_13mm'])

    @classmethod
    def PrimaLuce_M56_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_Spacer_14mm'])

    @classmethod
    def PrimaLuce_M56_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_Spacer_16mm'])

    @classmethod
    def PrimaLuce_M56_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_Spacer_17mm'])

    @classmethod
    def PrimaLuce_M56_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_Spacer_18mm'])

    @classmethod
    def PrimaLuce_M56_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_Spacer_22mm'])

    @classmethod
    def PrimaLuce_M56_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_Spacer_25mm'])

    @classmethod
    def PrimaLuce_M56_Spacer_28mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_Spacer_28mm'])

    @classmethod
    def PrimaLuce_M56_Spacer_30mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_Spacer_30mm'])

    @classmethod
    def PrimaLuce_M68_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M68_Spacer_2_5mm'])

    @classmethod
    def PrimaLuce_M68_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M68_Spacer_3mm'])

    @classmethod
    def PrimaLuce_M68_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M68_Spacer_3_5mm'])

    @classmethod
    def PrimaLuce_M68_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M68_Spacer_4mm'])

    @classmethod
    def PrimaLuce_M68_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M68_Spacer_4_5mm'])

    @classmethod
    def PrimaLuce_M68_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M68_Spacer_5_5mm'])

    @classmethod
    def PrimaLuce_M68_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M68_Spacer_6mm'])

    @classmethod
    def PrimaLuce_M68_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M68_Spacer_6_5mm'])

    @classmethod
    def PrimaLuce_M68_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M68_Spacer_7mm'])

    @classmethod
    def PrimaLuce_M68_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M68_Spacer_7_5mm'])

    @classmethod
    def PrimaLuce_M68_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M68_Spacer_8mm'])

    @classmethod
    def PrimaLuce_M68_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M68_Spacer_8_5mm'])

    @classmethod
    def PrimaLuce_M68_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M68_Spacer_9mm'])

    @classmethod
    def PrimaLuce_M68_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M68_Spacer_9_5mm'])

    @classmethod
    def PrimaLuce_M68_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M68_Spacer_11mm'])

    @classmethod
    def PrimaLuce_M68_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M68_Spacer_12mm'])

    @classmethod
    def PrimaLuce_M68_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M68_Spacer_13mm'])

    @classmethod
    def PrimaLuce_M68_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M68_Spacer_14mm'])

    @classmethod
    def PrimaLuce_M68_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M68_Spacer_16mm'])

    @classmethod
    def PrimaLuce_M68_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M68_Spacer_17mm'])

    @classmethod
    def PrimaLuce_M68_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M68_Spacer_18mm'])

    @classmethod
    def PrimaLuce_M68_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M68_Spacer_22mm'])

    @classmethod
    def PrimaLuce_M68_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M68_Spacer_25mm'])

    @classmethod
    def PrimaLuce_M68_Spacer_28mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M68_Spacer_28mm'])

class PrimaluceSpacer(Spacer):
    _DATABASE = {'PrimaLuce_M42_Spacer_1mm': {'brand': 'PrimaLuce', 'name': 'M42 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M42_Spacer_2mm': {'brand': 'PrimaLuce', 'name': 'M42 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M48_Spacer_1mm': {'brand': 'PrimaLuce', 'name': 'M48 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M48_Spacer_2mm': {'brand': 'PrimaLuce', 'name': 'M48 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M54_Spacer_1mm': {'brand': 'PrimaLuce', 'name': 'M54 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M54_Spacer_2mm': {'brand': 'PrimaLuce', 'name': 'M54 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M56_Spacer_1mm': {'brand': 'PrimaLuce', 'name': 'M56 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 9, 'tside_thread': 'M56', 'tside_gender': '', 'cside_thread': 'M56', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M56_Spacer_2mm': {'brand': 'PrimaLuce', 'name': 'M56 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 9, 'tside_thread': 'M56', 'tside_gender': '', 'cside_thread': 'M56', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M42_Spacer_0_5mm': {'brand': 'PrimaLuce', 'name': 'M42 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M42_Spacer_0_7mm': {'brand': 'PrimaLuce', 'name': 'M42 Spacer 0.7mm', 'type': 'type_spacer', 'optical_length': 0.7, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M42_Spacer_1_5mm': {'brand': 'PrimaLuce', 'name': 'M42 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M48_Spacer_0_5mm': {'brand': 'PrimaLuce', 'name': 'M48 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M48_Spacer_0_7mm': {'brand': 'PrimaLuce', 'name': 'M48 Spacer 0.7mm', 'type': 'type_spacer', 'optical_length': 0.7, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M48_Spacer_1_5mm': {'brand': 'PrimaLuce', 'name': 'M48 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M54_Spacer_0_5mm': {'brand': 'PrimaLuce', 'name': 'M54 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M54_Spacer_0_7mm': {'brand': 'PrimaLuce', 'name': 'M54 Spacer 0.7mm', 'type': 'type_spacer', 'optical_length': 0.7, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M54_Spacer_1_5mm': {'brand': 'PrimaLuce', 'name': 'M54 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M56_Spacer_0_5mm': {'brand': 'PrimaLuce', 'name': 'M56 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 9, 'tside_thread': 'M56', 'tside_gender': '', 'cside_thread': 'M56', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M56_Spacer_0_7mm': {'brand': 'PrimaLuce', 'name': 'M56 Spacer 0.7mm', 'type': 'type_spacer', 'optical_length': 0.7, 'mass': 9, 'tside_thread': 'M56', 'tside_gender': '', 'cside_thread': 'M56', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M56_Spacer_1_5mm': {'brand': 'PrimaLuce', 'name': 'M56 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 9, 'tside_thread': 'M56', 'tside_gender': '', 'cside_thread': 'M56', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M68_Spacer_0_5mm': {'brand': 'PrimaLuce', 'name': 'M68 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'PrimaLuce_M68_Spacer_1_5mm': {'brand': 'PrimaLuce', 'name': 'M68 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}}

    @classmethod
    def PrimaLuce_M42_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M42_Spacer_1mm'])

    @classmethod
    def PrimaLuce_M42_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M42_Spacer_2mm'])

    @classmethod
    def PrimaLuce_M48_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M48_Spacer_1mm'])

    @classmethod
    def PrimaLuce_M48_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M48_Spacer_2mm'])

    @classmethod
    def PrimaLuce_M54_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M54_Spacer_1mm'])

    @classmethod
    def PrimaLuce_M54_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M54_Spacer_2mm'])

    @classmethod
    def PrimaLuce_M56_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_Spacer_1mm'])

    @classmethod
    def PrimaLuce_M56_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_Spacer_2mm'])

    @classmethod
    def PrimaLuce_M42_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M42_Spacer_0_5mm'])

    @classmethod
    def PrimaLuce_M42_Spacer_0_7mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M42_Spacer_0_7mm'])

    @classmethod
    def PrimaLuce_M42_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M42_Spacer_1_5mm'])

    @classmethod
    def PrimaLuce_M48_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M48_Spacer_0_5mm'])

    @classmethod
    def PrimaLuce_M48_Spacer_0_7mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M48_Spacer_0_7mm'])

    @classmethod
    def PrimaLuce_M48_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M48_Spacer_1_5mm'])

    @classmethod
    def PrimaLuce_M54_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M54_Spacer_0_5mm'])

    @classmethod
    def PrimaLuce_M54_Spacer_0_7mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M54_Spacer_0_7mm'])

    @classmethod
    def PrimaLuce_M54_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M54_Spacer_1_5mm'])

    @classmethod
    def PrimaLuce_M56_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_Spacer_0_5mm'])

    @classmethod
    def PrimaLuce_M56_Spacer_0_7mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_Spacer_0_7mm'])

    @classmethod
    def PrimaLuce_M56_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M56_Spacer_1_5mm'])

    @classmethod
    def PrimaLuce_M68_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M68_Spacer_0_5mm'])

    @classmethod
    def PrimaLuce_M68_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_M68_Spacer_1_5mm'])