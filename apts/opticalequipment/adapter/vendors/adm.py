from ...abstract import IntermediateOpticalEquipment
from ....constants import OpticalType
from ..base import Adapter, Spacer

class AdmAdapter(Adapter):
    _DATABASE = {'ADM_M42_Spacer_3mm': {'brand': 'ADM', 'name': 'M42 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M42_Spacer_5mm': {'brand': 'ADM', 'name': 'M42 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 8, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M42_Spacer_7mm': {'brand': 'ADM', 'name': 'M42 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 9, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M42_Spacer_10mm': {'brand': 'ADM', 'name': 'M42 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 12, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M42_Spacer_15mm': {'brand': 'ADM', 'name': 'M42 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M42_Spacer_20mm': {'brand': 'ADM', 'name': 'M42 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 20, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M48_Spacer_3mm': {'brand': 'ADM', 'name': 'M48 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M48_Spacer_5mm': {'brand': 'ADM', 'name': 'M48 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 10, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M48_Spacer_7mm': {'brand': 'ADM', 'name': 'M48 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 11, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M48_Spacer_10mm': {'brand': 'ADM', 'name': 'M48 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 14, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M48_Spacer_15mm': {'brand': 'ADM', 'name': 'M48 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M48_Spacer_20mm': {'brand': 'ADM', 'name': 'M48 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 22, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M54_Spacer_3mm': {'brand': 'ADM', 'name': 'M54 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 10, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M54_Spacer_5mm': {'brand': 'ADM', 'name': 'M54 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 12, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M54_Spacer_10mm': {'brand': 'ADM', 'name': 'M54 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 16, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M54_Spacer_15mm': {'brand': 'ADM', 'name': 'M54 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 20, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M54_Spacer_20mm': {'brand': 'ADM', 'name': 'M54 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 24, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M68_Spacer_2_5mm': {'brand': 'ADM', 'name': 'M68 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M68_Spacer_3mm': {'brand': 'ADM', 'name': 'M68 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M68_Spacer_4mm': {'brand': 'ADM', 'name': 'M68 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 12, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M68_Spacer_5mm': {'brand': 'ADM', 'name': 'M68 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 13, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M68_Spacer_6mm': {'brand': 'ADM', 'name': 'M68 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 13, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M68_Spacer_7mm': {'brand': 'ADM', 'name': 'M68 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 14, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M68_Spacer_8mm': {'brand': 'ADM', 'name': 'M68 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 15, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M68_Spacer_9mm': {'brand': 'ADM', 'name': 'M68 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 16, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M68_Spacer_10mm': {'brand': 'ADM', 'name': 'M68 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 17, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M68_Spacer_12mm': {'brand': 'ADM', 'name': 'M68 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 18, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M68_Spacer_15mm': {'brand': 'ADM', 'name': 'M68 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 21, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M68_Spacer_18mm': {'brand': 'ADM', 'name': 'M68 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 23, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M68_Spacer_20mm': {'brand': 'ADM', 'name': 'M68 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 25, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M42_Spacer_2_1mm': {'brand': 'ADM', 'name': 'M42 Spacer 2.1mm', 'type': 'type_adapter', 'optical_length': 2.1, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M42_Spacer_2_3mm': {'brand': 'ADM', 'name': 'M42 Spacer 2.3mm', 'type': 'type_adapter', 'optical_length': 2.3, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M42_Spacer_2_7mm': {'brand': 'ADM', 'name': 'M42 Spacer 2.7mm', 'type': 'type_adapter', 'optical_length': 2.7, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M42_Spacer_3_2mm': {'brand': 'ADM', 'name': 'M42 Spacer 3.2mm', 'type': 'type_adapter', 'optical_length': 3.2, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M42_Spacer_3_5mm': {'brand': 'ADM', 'name': 'M42 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M42_Spacer_4mm': {'brand': 'ADM', 'name': 'M42 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 7, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M42_Spacer_4_5mm': {'brand': 'ADM', 'name': 'M42 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 7, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M42_Spacer_5_5mm': {'brand': 'ADM', 'name': 'M42 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 8, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M42_Spacer_6mm': {'brand': 'ADM', 'name': 'M42 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 8, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M42_Spacer_6_5mm': {'brand': 'ADM', 'name': 'M42 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 9, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M42_Spacer_8mm': {'brand': 'ADM', 'name': 'M42 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 10, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M42_Spacer_8_5mm': {'brand': 'ADM', 'name': 'M42 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 10, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M42_Spacer_9mm': {'brand': 'ADM', 'name': 'M42 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 11, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M42_Spacer_9_5mm': {'brand': 'ADM', 'name': 'M42 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 11, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M42_Spacer_11mm': {'brand': 'ADM', 'name': 'M42 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 12, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M42_Spacer_13mm': {'brand': 'ADM', 'name': 'M42 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 14, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M42_Spacer_14mm': {'brand': 'ADM', 'name': 'M42 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 15, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M42_Spacer_16mm': {'brand': 'ADM', 'name': 'M42 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M42_Spacer_17mm': {'brand': 'ADM', 'name': 'M42 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 17, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M42_Spacer_18mm': {'brand': 'ADM', 'name': 'M42 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 18, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M42_Spacer_22mm': {'brand': 'ADM', 'name': 'M42 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 21, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M42_Spacer_25mm': {'brand': 'ADM', 'name': 'M42 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 24, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M42_Spacer_28mm': {'brand': 'ADM', 'name': 'M42 Spacer 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 26, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M48_Spacer_2_1mm': {'brand': 'ADM', 'name': 'M48 Spacer 2.1mm', 'type': 'type_adapter', 'optical_length': 2.1, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M48_Spacer_2_3mm': {'brand': 'ADM', 'name': 'M48 Spacer 2.3mm', 'type': 'type_adapter', 'optical_length': 2.3, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M48_Spacer_2_7mm': {'brand': 'ADM', 'name': 'M48 Spacer 2.7mm', 'type': 'type_adapter', 'optical_length': 2.7, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M48_Spacer_3_2mm': {'brand': 'ADM', 'name': 'M48 Spacer 3.2mm', 'type': 'type_adapter', 'optical_length': 3.2, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M48_Spacer_3_5mm': {'brand': 'ADM', 'name': 'M48 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M48_Spacer_4mm': {'brand': 'ADM', 'name': 'M48 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 9, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M48_Spacer_4_5mm': {'brand': 'ADM', 'name': 'M48 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 9, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M48_Spacer_5_5mm': {'brand': 'ADM', 'name': 'M48 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 10, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M48_Spacer_6mm': {'brand': 'ADM', 'name': 'M48 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 10, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M48_Spacer_6_5mm': {'brand': 'ADM', 'name': 'M48 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 11, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M48_Spacer_8mm': {'brand': 'ADM', 'name': 'M48 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 12, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M48_Spacer_8_5mm': {'brand': 'ADM', 'name': 'M48 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 12, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M48_Spacer_9mm': {'brand': 'ADM', 'name': 'M48 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 13, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M48_Spacer_9_5mm': {'brand': 'ADM', 'name': 'M48 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 13, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M48_Spacer_11mm': {'brand': 'ADM', 'name': 'M48 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 14, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M48_Spacer_13mm': {'brand': 'ADM', 'name': 'M48 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 16, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M48_Spacer_14mm': {'brand': 'ADM', 'name': 'M48 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 17, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M48_Spacer_16mm': {'brand': 'ADM', 'name': 'M48 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M48_Spacer_17mm': {'brand': 'ADM', 'name': 'M48 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 19, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M48_Spacer_18mm': {'brand': 'ADM', 'name': 'M48 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 20, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M48_Spacer_22mm': {'brand': 'ADM', 'name': 'M48 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 23, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M48_Spacer_25mm': {'brand': 'ADM', 'name': 'M48 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 26, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M48_Spacer_28mm': {'brand': 'ADM', 'name': 'M48 Spacer 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 28, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M54_Spacer_2_1mm': {'brand': 'ADM', 'name': 'M54 Spacer 2.1mm', 'type': 'type_adapter', 'optical_length': 2.1, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M54_Spacer_2_3mm': {'brand': 'ADM', 'name': 'M54 Spacer 2.3mm', 'type': 'type_adapter', 'optical_length': 2.3, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M54_Spacer_2_7mm': {'brand': 'ADM', 'name': 'M54 Spacer 2.7mm', 'type': 'type_adapter', 'optical_length': 2.7, 'mass': 10, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M54_Spacer_3_2mm': {'brand': 'ADM', 'name': 'M54 Spacer 3.2mm', 'type': 'type_adapter', 'optical_length': 3.2, 'mass': 10, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M54_Spacer_3_5mm': {'brand': 'ADM', 'name': 'M54 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 10, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M54_Spacer_4mm': {'brand': 'ADM', 'name': 'M54 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 11, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M54_Spacer_4_5mm': {'brand': 'ADM', 'name': 'M54 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 11, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M54_Spacer_5_5mm': {'brand': 'ADM', 'name': 'M54 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 12, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M54_Spacer_6mm': {'brand': 'ADM', 'name': 'M54 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 12, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M54_Spacer_6_5mm': {'brand': 'ADM', 'name': 'M54 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 13, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M54_Spacer_7_5mm': {'brand': 'ADM', 'name': 'M54 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 14, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M54_Spacer_8mm': {'brand': 'ADM', 'name': 'M54 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 14, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M54_Spacer_8_5mm': {'brand': 'ADM', 'name': 'M54 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 14, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M54_Spacer_9mm': {'brand': 'ADM', 'name': 'M54 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 15, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M54_Spacer_9_5mm': {'brand': 'ADM', 'name': 'M54 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 15, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M54_Spacer_11mm': {'brand': 'ADM', 'name': 'M54 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 16, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M54_Spacer_13mm': {'brand': 'ADM', 'name': 'M54 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 18, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M54_Spacer_14mm': {'brand': 'ADM', 'name': 'M54 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 19, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M54_Spacer_16mm': {'brand': 'ADM', 'name': 'M54 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 20, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M54_Spacer_17mm': {'brand': 'ADM', 'name': 'M54 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 21, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M54_Spacer_18mm': {'brand': 'ADM', 'name': 'M54 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 22, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M54_Spacer_22mm': {'brand': 'ADM', 'name': 'M54 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 25, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M54_Spacer_25mm': {'brand': 'ADM', 'name': 'M54 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 28, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M68_Spacer_2_1mm': {'brand': 'ADM', 'name': 'M68 Spacer 2.1mm', 'type': 'type_adapter', 'optical_length': 2.1, 'mass': 10, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M68_Spacer_2_3mm': {'brand': 'ADM', 'name': 'M68 Spacer 2.3mm', 'type': 'type_adapter', 'optical_length': 2.3, 'mass': 10, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M68_Spacer_2_7mm': {'brand': 'ADM', 'name': 'M68 Spacer 2.7mm', 'type': 'type_adapter', 'optical_length': 2.7, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M68_Spacer_3_5mm': {'brand': 'ADM', 'name': 'M68 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M68_Spacer_4_5mm': {'brand': 'ADM', 'name': 'M68 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 12, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M68_Spacer_5_5mm': {'brand': 'ADM', 'name': 'M68 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 13, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M68_Spacer_6_5mm': {'brand': 'ADM', 'name': 'M68 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 14, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M68_Spacer_7_5mm': {'brand': 'ADM', 'name': 'M68 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 15, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M68_Spacer_8_5mm': {'brand': 'ADM', 'name': 'M68 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 15, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M68_Spacer_9_5mm': {'brand': 'ADM', 'name': 'M68 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 16, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M68_Spacer_11mm': {'brand': 'ADM', 'name': 'M68 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 17, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M68_Spacer_13mm': {'brand': 'ADM', 'name': 'M68 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 19, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M68_Spacer_14mm': {'brand': 'ADM', 'name': 'M68 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 20, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M68_Spacer_16mm': {'brand': 'ADM', 'name': 'M68 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 21, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M68_Spacer_17mm': {'brand': 'ADM', 'name': 'M68 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 22, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M68_Spacer_22mm': {'brand': 'ADM', 'name': 'M68 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 26, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M68_Spacer_25mm': {'brand': 'ADM', 'name': 'M68 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 29, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M72_Spacer_2_5mm': {'brand': 'ADM', 'name': 'M72 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 13, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M72_Spacer_3mm': {'brand': 'ADM', 'name': 'M72 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 13, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M72_Spacer_3_5mm': {'brand': 'ADM', 'name': 'M72 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 13, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M72_Spacer_4mm': {'brand': 'ADM', 'name': 'M72 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 14, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M72_Spacer_4_5mm': {'brand': 'ADM', 'name': 'M72 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 14, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M72_Spacer_5mm': {'brand': 'ADM', 'name': 'M72 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 15, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M72_Spacer_5_5mm': {'brand': 'ADM', 'name': 'M72 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 15, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M72_Spacer_6mm': {'brand': 'ADM', 'name': 'M72 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 15, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M72_Spacer_6_5mm': {'brand': 'ADM', 'name': 'M72 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 16, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M72_Spacer_7mm': {'brand': 'ADM', 'name': 'M72 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 16, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M72_Spacer_7_5mm': {'brand': 'ADM', 'name': 'M72 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 17, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M72_Spacer_8mm': {'brand': 'ADM', 'name': 'M72 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 17, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M72_Spacer_8_5mm': {'brand': 'ADM', 'name': 'M72 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 17, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M72_Spacer_9mm': {'brand': 'ADM', 'name': 'M72 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 18, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M72_Spacer_9_5mm': {'brand': 'ADM', 'name': 'M72 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 18, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M72_Spacer_10mm': {'brand': 'ADM', 'name': 'M72 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 19, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M72_Spacer_11mm': {'brand': 'ADM', 'name': 'M72 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 19, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M72_Spacer_12mm': {'brand': 'ADM', 'name': 'M72 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 20, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M72_Spacer_13mm': {'brand': 'ADM', 'name': 'M72 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 21, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M72_Spacer_14mm': {'brand': 'ADM', 'name': 'M72 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 22, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M72_Spacer_16mm': {'brand': 'ADM', 'name': 'M72 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 23, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M72_Spacer_17mm': {'brand': 'ADM', 'name': 'M72 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 24, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M72_Spacer_18mm': {'brand': 'ADM', 'name': 'M72 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 25, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M72_Spacer_22mm': {'brand': 'ADM', 'name': 'M72 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 28, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M72_Spacer_25mm': {'brand': 'ADM', 'name': 'M72 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 31, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M42_Extension_Tube_3mm': {'brand': 'ADM', 'name': 'M42 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 13, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M42_Extension_Tube_6mm': {'brand': 'ADM', 'name': 'M42 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 14, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M42_Extension_Tube_9mm': {'brand': 'ADM', 'name': 'M42 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 15, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M42_Extension_Tube_11mm': {'brand': 'ADM', 'name': 'M42 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M42_Extension_Tube_13mm': {'brand': 'ADM', 'name': 'M42 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M42_Extension_Tube_16mm': {'brand': 'ADM', 'name': 'M42 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 17, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M42_Extension_Tube_22mm': {'brand': 'ADM', 'name': 'M42 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 19, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M42_Extension_Tube_28mm': {'brand': 'ADM', 'name': 'M42 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 21, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M42_Extension_Tube_35mm': {'brand': 'ADM', 'name': 'M42 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 23, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M42_Extension_Tube_45mm': {'brand': 'ADM', 'name': 'M42 Extension Tube 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 26, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M48_Extension_Tube_3mm': {'brand': 'ADM', 'name': 'M48 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 17, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M48_Extension_Tube_6mm': {'brand': 'ADM', 'name': 'M48 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M48_Extension_Tube_9mm': {'brand': 'ADM', 'name': 'M48 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 19, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M48_Extension_Tube_11mm': {'brand': 'ADM', 'name': 'M48 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 20, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M48_Extension_Tube_13mm': {'brand': 'ADM', 'name': 'M48 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 20, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M48_Extension_Tube_16mm': {'brand': 'ADM', 'name': 'M48 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 21, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M48_Extension_Tube_22mm': {'brand': 'ADM', 'name': 'M48 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 23, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M48_Extension_Tube_28mm': {'brand': 'ADM', 'name': 'M48 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 25, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M48_Extension_Tube_35mm': {'brand': 'ADM', 'name': 'M48 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 27, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M48_Extension_Tube_45mm': {'brand': 'ADM', 'name': 'M48 Extension Tube 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 30, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M54_Extension_Tube_3mm': {'brand': 'ADM', 'name': 'M54 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 21, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M54_Extension_Tube_6mm': {'brand': 'ADM', 'name': 'M54 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 22, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M54_Extension_Tube_9mm': {'brand': 'ADM', 'name': 'M54 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 23, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M54_Extension_Tube_11mm': {'brand': 'ADM', 'name': 'M54 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 24, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M54_Extension_Tube_13mm': {'brand': 'ADM', 'name': 'M54 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 24, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M54_Extension_Tube_16mm': {'brand': 'ADM', 'name': 'M54 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 25, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M54_Extension_Tube_22mm': {'brand': 'ADM', 'name': 'M54 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 27, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M54_Extension_Tube_28mm': {'brand': 'ADM', 'name': 'M54 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 29, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M54_Extension_Tube_35mm': {'brand': 'ADM', 'name': 'M54 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 31, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M54_Extension_Tube_45mm': {'brand': 'ADM', 'name': 'M54 Extension Tube 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 34, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M68_Extension_Tube_3mm': {'brand': 'ADM', 'name': 'M68 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 17, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M68_Extension_Tube_5mm': {'brand': 'ADM', 'name': 'M68 Extension Tube 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 18, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M68_Extension_Tube_6mm': {'brand': 'ADM', 'name': 'M68 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 18, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M68_Extension_Tube_8mm': {'brand': 'ADM', 'name': 'M68 Extension Tube 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 19, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M68_Extension_Tube_9mm': {'brand': 'ADM', 'name': 'M68 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 19, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M68_Extension_Tube_11mm': {'brand': 'ADM', 'name': 'M68 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 20, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M68_Extension_Tube_13mm': {'brand': 'ADM', 'name': 'M68 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 20, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M68_Extension_Tube_14mm': {'brand': 'ADM', 'name': 'M68 Extension Tube 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 21, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M68_Extension_Tube_16mm': {'brand': 'ADM', 'name': 'M68 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 21, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M68_Extension_Tube_18mm': {'brand': 'ADM', 'name': 'M68 Extension Tube 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 22, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M68_Extension_Tube_22mm': {'brand': 'ADM', 'name': 'M68 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 23, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M68_Extension_Tube_25mm': {'brand': 'ADM', 'name': 'M68 Extension Tube 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 24, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M68_Extension_Tube_28mm': {'brand': 'ADM', 'name': 'M68 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 25, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M68_Extension_Tube_30mm': {'brand': 'ADM', 'name': 'M68 Extension Tube 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 26, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M68_Extension_Tube_35mm': {'brand': 'ADM', 'name': 'M68 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 27, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M72_Extension_Tube_3mm': {'brand': 'ADM', 'name': 'M72 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 19, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M72_Extension_Tube_5mm': {'brand': 'ADM', 'name': 'M72 Extension Tube 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 20, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M72_Extension_Tube_8mm': {'brand': 'ADM', 'name': 'M72 Extension Tube 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 21, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M72_Extension_Tube_10mm': {'brand': 'ADM', 'name': 'M72 Extension Tube 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 22, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M72_Extension_Tube_12mm': {'brand': 'ADM', 'name': 'M72 Extension Tube 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 22, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M72_Extension_Tube_15mm': {'brand': 'ADM', 'name': 'M72 Extension Tube 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 23, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M72_Extension_Tube_18mm': {'brand': 'ADM', 'name': 'M72 Extension Tube 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 24, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M72_Extension_Tube_20mm': {'brand': 'ADM', 'name': 'M72 Extension Tube 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 25, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M72_Extension_Tube_25mm': {'brand': 'ADM', 'name': 'M72 Extension Tube 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 26, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M72_Extension_Tube_30mm': {'brand': 'ADM', 'name': 'M72 Extension Tube 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 28, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M82_Extension_Tube_3mm': {'brand': 'ADM', 'name': 'M82 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 21, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M82_Extension_Tube_5mm': {'brand': 'ADM', 'name': 'M82 Extension Tube 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 22, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M82_Extension_Tube_8mm': {'brand': 'ADM', 'name': 'M82 Extension Tube 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 23, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M82_Extension_Tube_10mm': {'brand': 'ADM', 'name': 'M82 Extension Tube 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 24, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M82_Extension_Tube_12mm': {'brand': 'ADM', 'name': 'M82 Extension Tube 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 24, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M82_Extension_Tube_15mm': {'brand': 'ADM', 'name': 'M82 Extension Tube 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 25, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M82_Extension_Tube_18mm': {'brand': 'ADM', 'name': 'M82 Extension Tube 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 26, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M82_Extension_Tube_20mm': {'brand': 'ADM', 'name': 'M82 Extension Tube 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 27, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M82_Extension_Tube_25mm': {'brand': 'ADM', 'name': 'M82 Extension Tube 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 28, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M82_Extension_Tube_30mm': {'brand': 'ADM', 'name': 'M82 Extension Tube 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 30, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'ADM_M92_Spacer_2_5mm': {'brand': 'ADM', 'name': 'M92 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 18, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M92_Spacer_3mm': {'brand': 'ADM', 'name': 'M92 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 18, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M92_Spacer_3_5mm': {'brand': 'ADM', 'name': 'M92 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 18, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M92_Spacer_4mm': {'brand': 'ADM', 'name': 'M92 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 19, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M92_Spacer_5mm': {'brand': 'ADM', 'name': 'M92 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 20, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M92_Spacer_6mm': {'brand': 'ADM', 'name': 'M92 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 20, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M92_Spacer_7mm': {'brand': 'ADM', 'name': 'M92 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 21, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M92_Spacer_8mm': {'brand': 'ADM', 'name': 'M92 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 22, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M92_Spacer_9mm': {'brand': 'ADM', 'name': 'M92 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 23, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M92_Spacer_10mm': {'brand': 'ADM', 'name': 'M92 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 24, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M92_Spacer_12mm': {'brand': 'ADM', 'name': 'M92 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 25, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M92_Spacer_15mm': {'brand': 'ADM', 'name': 'M92 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 28, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M92_Spacer_18mm': {'brand': 'ADM', 'name': 'M92 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 30, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M92_Spacer_20mm': {'brand': 'ADM', 'name': 'M92 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 32, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'ADM_M92_Spacer_25mm': {'brand': 'ADM', 'name': 'M92 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 36, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}}

    @classmethod
    def ADM_M42_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Spacer_3mm'])

    @classmethod
    def ADM_M42_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Spacer_5mm'])

    @classmethod
    def ADM_M42_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Spacer_7mm'])

    @classmethod
    def ADM_M42_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Spacer_10mm'])

    @classmethod
    def ADM_M42_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Spacer_15mm'])

    @classmethod
    def ADM_M42_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Spacer_20mm'])

    @classmethod
    def ADM_M48_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Spacer_3mm'])

    @classmethod
    def ADM_M48_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Spacer_5mm'])

    @classmethod
    def ADM_M48_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Spacer_7mm'])

    @classmethod
    def ADM_M48_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Spacer_10mm'])

    @classmethod
    def ADM_M48_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Spacer_15mm'])

    @classmethod
    def ADM_M48_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Spacer_20mm'])

    @classmethod
    def ADM_M54_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Spacer_3mm'])

    @classmethod
    def ADM_M54_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Spacer_5mm'])

    @classmethod
    def ADM_M54_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Spacer_10mm'])

    @classmethod
    def ADM_M54_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Spacer_15mm'])

    @classmethod
    def ADM_M54_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Spacer_20mm'])

    @classmethod
    def ADM_M68_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Spacer_2_5mm'])

    @classmethod
    def ADM_M68_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Spacer_3mm'])

    @classmethod
    def ADM_M68_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Spacer_4mm'])

    @classmethod
    def ADM_M68_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Spacer_5mm'])

    @classmethod
    def ADM_M68_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Spacer_6mm'])

    @classmethod
    def ADM_M68_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Spacer_7mm'])

    @classmethod
    def ADM_M68_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Spacer_8mm'])

    @classmethod
    def ADM_M68_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Spacer_9mm'])

    @classmethod
    def ADM_M68_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Spacer_10mm'])

    @classmethod
    def ADM_M68_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Spacer_12mm'])

    @classmethod
    def ADM_M68_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Spacer_15mm'])

    @classmethod
    def ADM_M68_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Spacer_18mm'])

    @classmethod
    def ADM_M68_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Spacer_20mm'])

    @classmethod
    def ADM_M42_Spacer_2_1mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Spacer_2_1mm'])

    @classmethod
    def ADM_M42_Spacer_2_3mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Spacer_2_3mm'])

    @classmethod
    def ADM_M42_Spacer_2_7mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Spacer_2_7mm'])

    @classmethod
    def ADM_M42_Spacer_3_2mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Spacer_3_2mm'])

    @classmethod
    def ADM_M42_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Spacer_3_5mm'])

    @classmethod
    def ADM_M42_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Spacer_4mm'])

    @classmethod
    def ADM_M42_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Spacer_4_5mm'])

    @classmethod
    def ADM_M42_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Spacer_5_5mm'])

    @classmethod
    def ADM_M42_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Spacer_6mm'])

    @classmethod
    def ADM_M42_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Spacer_6_5mm'])

    @classmethod
    def ADM_M42_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Spacer_8mm'])

    @classmethod
    def ADM_M42_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Spacer_8_5mm'])

    @classmethod
    def ADM_M42_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Spacer_9mm'])

    @classmethod
    def ADM_M42_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Spacer_9_5mm'])

    @classmethod
    def ADM_M42_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Spacer_11mm'])

    @classmethod
    def ADM_M42_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Spacer_13mm'])

    @classmethod
    def ADM_M42_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Spacer_14mm'])

    @classmethod
    def ADM_M42_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Spacer_16mm'])

    @classmethod
    def ADM_M42_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Spacer_17mm'])

    @classmethod
    def ADM_M42_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Spacer_18mm'])

    @classmethod
    def ADM_M42_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Spacer_22mm'])

    @classmethod
    def ADM_M42_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Spacer_25mm'])

    @classmethod
    def ADM_M42_Spacer_28mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Spacer_28mm'])

    @classmethod
    def ADM_M48_Spacer_2_1mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Spacer_2_1mm'])

    @classmethod
    def ADM_M48_Spacer_2_3mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Spacer_2_3mm'])

    @classmethod
    def ADM_M48_Spacer_2_7mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Spacer_2_7mm'])

    @classmethod
    def ADM_M48_Spacer_3_2mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Spacer_3_2mm'])

    @classmethod
    def ADM_M48_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Spacer_3_5mm'])

    @classmethod
    def ADM_M48_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Spacer_4mm'])

    @classmethod
    def ADM_M48_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Spacer_4_5mm'])

    @classmethod
    def ADM_M48_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Spacer_5_5mm'])

    @classmethod
    def ADM_M48_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Spacer_6mm'])

    @classmethod
    def ADM_M48_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Spacer_6_5mm'])

    @classmethod
    def ADM_M48_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Spacer_8mm'])

    @classmethod
    def ADM_M48_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Spacer_8_5mm'])

    @classmethod
    def ADM_M48_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Spacer_9mm'])

    @classmethod
    def ADM_M48_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Spacer_9_5mm'])

    @classmethod
    def ADM_M48_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Spacer_11mm'])

    @classmethod
    def ADM_M48_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Spacer_13mm'])

    @classmethod
    def ADM_M48_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Spacer_14mm'])

    @classmethod
    def ADM_M48_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Spacer_16mm'])

    @classmethod
    def ADM_M48_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Spacer_17mm'])

    @classmethod
    def ADM_M48_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Spacer_18mm'])

    @classmethod
    def ADM_M48_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Spacer_22mm'])

    @classmethod
    def ADM_M48_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Spacer_25mm'])

    @classmethod
    def ADM_M48_Spacer_28mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Spacer_28mm'])

    @classmethod
    def ADM_M54_Spacer_2_1mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Spacer_2_1mm'])

    @classmethod
    def ADM_M54_Spacer_2_3mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Spacer_2_3mm'])

    @classmethod
    def ADM_M54_Spacer_2_7mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Spacer_2_7mm'])

    @classmethod
    def ADM_M54_Spacer_3_2mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Spacer_3_2mm'])

    @classmethod
    def ADM_M54_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Spacer_3_5mm'])

    @classmethod
    def ADM_M54_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Spacer_4mm'])

    @classmethod
    def ADM_M54_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Spacer_4_5mm'])

    @classmethod
    def ADM_M54_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Spacer_5_5mm'])

    @classmethod
    def ADM_M54_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Spacer_6mm'])

    @classmethod
    def ADM_M54_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Spacer_6_5mm'])

    @classmethod
    def ADM_M54_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Spacer_7_5mm'])

    @classmethod
    def ADM_M54_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Spacer_8mm'])

    @classmethod
    def ADM_M54_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Spacer_8_5mm'])

    @classmethod
    def ADM_M54_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Spacer_9mm'])

    @classmethod
    def ADM_M54_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Spacer_9_5mm'])

    @classmethod
    def ADM_M54_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Spacer_11mm'])

    @classmethod
    def ADM_M54_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Spacer_13mm'])

    @classmethod
    def ADM_M54_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Spacer_14mm'])

    @classmethod
    def ADM_M54_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Spacer_16mm'])

    @classmethod
    def ADM_M54_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Spacer_17mm'])

    @classmethod
    def ADM_M54_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Spacer_18mm'])

    @classmethod
    def ADM_M54_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Spacer_22mm'])

    @classmethod
    def ADM_M54_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Spacer_25mm'])

    @classmethod
    def ADM_M68_Spacer_2_1mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Spacer_2_1mm'])

    @classmethod
    def ADM_M68_Spacer_2_3mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Spacer_2_3mm'])

    @classmethod
    def ADM_M68_Spacer_2_7mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Spacer_2_7mm'])

    @classmethod
    def ADM_M68_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Spacer_3_5mm'])

    @classmethod
    def ADM_M68_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Spacer_4_5mm'])

    @classmethod
    def ADM_M68_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Spacer_5_5mm'])

    @classmethod
    def ADM_M68_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Spacer_6_5mm'])

    @classmethod
    def ADM_M68_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Spacer_7_5mm'])

    @classmethod
    def ADM_M68_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Spacer_8_5mm'])

    @classmethod
    def ADM_M68_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Spacer_9_5mm'])

    @classmethod
    def ADM_M68_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Spacer_11mm'])

    @classmethod
    def ADM_M68_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Spacer_13mm'])

    @classmethod
    def ADM_M68_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Spacer_14mm'])

    @classmethod
    def ADM_M68_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Spacer_16mm'])

    @classmethod
    def ADM_M68_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Spacer_17mm'])

    @classmethod
    def ADM_M68_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Spacer_22mm'])

    @classmethod
    def ADM_M68_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Spacer_25mm'])

    @classmethod
    def ADM_M72_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M72_Spacer_2_5mm'])

    @classmethod
    def ADM_M72_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M72_Spacer_3mm'])

    @classmethod
    def ADM_M72_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M72_Spacer_3_5mm'])

    @classmethod
    def ADM_M72_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M72_Spacer_4mm'])

    @classmethod
    def ADM_M72_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M72_Spacer_4_5mm'])

    @classmethod
    def ADM_M72_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M72_Spacer_5mm'])

    @classmethod
    def ADM_M72_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M72_Spacer_5_5mm'])

    @classmethod
    def ADM_M72_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M72_Spacer_6mm'])

    @classmethod
    def ADM_M72_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M72_Spacer_6_5mm'])

    @classmethod
    def ADM_M72_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M72_Spacer_7mm'])

    @classmethod
    def ADM_M72_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M72_Spacer_7_5mm'])

    @classmethod
    def ADM_M72_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M72_Spacer_8mm'])

    @classmethod
    def ADM_M72_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M72_Spacer_8_5mm'])

    @classmethod
    def ADM_M72_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M72_Spacer_9mm'])

    @classmethod
    def ADM_M72_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M72_Spacer_9_5mm'])

    @classmethod
    def ADM_M72_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M72_Spacer_10mm'])

    @classmethod
    def ADM_M72_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M72_Spacer_11mm'])

    @classmethod
    def ADM_M72_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M72_Spacer_12mm'])

    @classmethod
    def ADM_M72_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M72_Spacer_13mm'])

    @classmethod
    def ADM_M72_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M72_Spacer_14mm'])

    @classmethod
    def ADM_M72_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M72_Spacer_16mm'])

    @classmethod
    def ADM_M72_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M72_Spacer_17mm'])

    @classmethod
    def ADM_M72_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M72_Spacer_18mm'])

    @classmethod
    def ADM_M72_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M72_Spacer_22mm'])

    @classmethod
    def ADM_M72_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M72_Spacer_25mm'])

    @classmethod
    def ADM_M42_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Extension_Tube_3mm'])

    @classmethod
    def ADM_M42_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Extension_Tube_6mm'])

    @classmethod
    def ADM_M42_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Extension_Tube_9mm'])

    @classmethod
    def ADM_M42_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Extension_Tube_11mm'])

    @classmethod
    def ADM_M42_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Extension_Tube_13mm'])

    @classmethod
    def ADM_M42_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Extension_Tube_16mm'])

    @classmethod
    def ADM_M42_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Extension_Tube_22mm'])

    @classmethod
    def ADM_M42_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Extension_Tube_28mm'])

    @classmethod
    def ADM_M42_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Extension_Tube_35mm'])

    @classmethod
    def ADM_M42_Extension_Tube_45mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Extension_Tube_45mm'])

    @classmethod
    def ADM_M48_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Extension_Tube_3mm'])

    @classmethod
    def ADM_M48_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Extension_Tube_6mm'])

    @classmethod
    def ADM_M48_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Extension_Tube_9mm'])

    @classmethod
    def ADM_M48_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Extension_Tube_11mm'])

    @classmethod
    def ADM_M48_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Extension_Tube_13mm'])

    @classmethod
    def ADM_M48_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Extension_Tube_16mm'])

    @classmethod
    def ADM_M48_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Extension_Tube_22mm'])

    @classmethod
    def ADM_M48_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Extension_Tube_28mm'])

    @classmethod
    def ADM_M48_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Extension_Tube_35mm'])

    @classmethod
    def ADM_M48_Extension_Tube_45mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Extension_Tube_45mm'])

    @classmethod
    def ADM_M54_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Extension_Tube_3mm'])

    @classmethod
    def ADM_M54_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Extension_Tube_6mm'])

    @classmethod
    def ADM_M54_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Extension_Tube_9mm'])

    @classmethod
    def ADM_M54_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Extension_Tube_11mm'])

    @classmethod
    def ADM_M54_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Extension_Tube_13mm'])

    @classmethod
    def ADM_M54_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Extension_Tube_16mm'])

    @classmethod
    def ADM_M54_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Extension_Tube_22mm'])

    @classmethod
    def ADM_M54_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Extension_Tube_28mm'])

    @classmethod
    def ADM_M54_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Extension_Tube_35mm'])

    @classmethod
    def ADM_M54_Extension_Tube_45mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Extension_Tube_45mm'])

    @classmethod
    def ADM_M68_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Extension_Tube_3mm'])

    @classmethod
    def ADM_M68_Extension_Tube_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Extension_Tube_5mm'])

    @classmethod
    def ADM_M68_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Extension_Tube_6mm'])

    @classmethod
    def ADM_M68_Extension_Tube_8mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Extension_Tube_8mm'])

    @classmethod
    def ADM_M68_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Extension_Tube_9mm'])

    @classmethod
    def ADM_M68_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Extension_Tube_11mm'])

    @classmethod
    def ADM_M68_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Extension_Tube_13mm'])

    @classmethod
    def ADM_M68_Extension_Tube_14mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Extension_Tube_14mm'])

    @classmethod
    def ADM_M68_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Extension_Tube_16mm'])

    @classmethod
    def ADM_M68_Extension_Tube_18mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Extension_Tube_18mm'])

    @classmethod
    def ADM_M68_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Extension_Tube_22mm'])

    @classmethod
    def ADM_M68_Extension_Tube_25mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Extension_Tube_25mm'])

    @classmethod
    def ADM_M68_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Extension_Tube_28mm'])

    @classmethod
    def ADM_M68_Extension_Tube_30mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Extension_Tube_30mm'])

    @classmethod
    def ADM_M68_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Extension_Tube_35mm'])

    @classmethod
    def ADM_M72_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M72_Extension_Tube_3mm'])

    @classmethod
    def ADM_M72_Extension_Tube_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M72_Extension_Tube_5mm'])

    @classmethod
    def ADM_M72_Extension_Tube_8mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M72_Extension_Tube_8mm'])

    @classmethod
    def ADM_M72_Extension_Tube_10mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M72_Extension_Tube_10mm'])

    @classmethod
    def ADM_M72_Extension_Tube_12mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M72_Extension_Tube_12mm'])

    @classmethod
    def ADM_M72_Extension_Tube_15mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M72_Extension_Tube_15mm'])

    @classmethod
    def ADM_M72_Extension_Tube_18mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M72_Extension_Tube_18mm'])

    @classmethod
    def ADM_M72_Extension_Tube_20mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M72_Extension_Tube_20mm'])

    @classmethod
    def ADM_M72_Extension_Tube_25mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M72_Extension_Tube_25mm'])

    @classmethod
    def ADM_M72_Extension_Tube_30mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M72_Extension_Tube_30mm'])

    @classmethod
    def ADM_M82_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M82_Extension_Tube_3mm'])

    @classmethod
    def ADM_M82_Extension_Tube_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M82_Extension_Tube_5mm'])

    @classmethod
    def ADM_M82_Extension_Tube_8mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M82_Extension_Tube_8mm'])

    @classmethod
    def ADM_M82_Extension_Tube_10mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M82_Extension_Tube_10mm'])

    @classmethod
    def ADM_M82_Extension_Tube_12mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M82_Extension_Tube_12mm'])

    @classmethod
    def ADM_M82_Extension_Tube_15mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M82_Extension_Tube_15mm'])

    @classmethod
    def ADM_M82_Extension_Tube_18mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M82_Extension_Tube_18mm'])

    @classmethod
    def ADM_M82_Extension_Tube_20mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M82_Extension_Tube_20mm'])

    @classmethod
    def ADM_M82_Extension_Tube_25mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M82_Extension_Tube_25mm'])

    @classmethod
    def ADM_M82_Extension_Tube_30mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M82_Extension_Tube_30mm'])

    @classmethod
    def ADM_M92_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M92_Spacer_2_5mm'])

    @classmethod
    def ADM_M92_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M92_Spacer_3mm'])

    @classmethod
    def ADM_M92_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M92_Spacer_3_5mm'])

    @classmethod
    def ADM_M92_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M92_Spacer_4mm'])

    @classmethod
    def ADM_M92_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M92_Spacer_5mm'])

    @classmethod
    def ADM_M92_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M92_Spacer_6mm'])

    @classmethod
    def ADM_M92_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M92_Spacer_7mm'])

    @classmethod
    def ADM_M92_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M92_Spacer_8mm'])

    @classmethod
    def ADM_M92_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M92_Spacer_9mm'])

    @classmethod
    def ADM_M92_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M92_Spacer_10mm'])

    @classmethod
    def ADM_M92_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M92_Spacer_12mm'])

    @classmethod
    def ADM_M92_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M92_Spacer_15mm'])

    @classmethod
    def ADM_M92_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M92_Spacer_18mm'])

    @classmethod
    def ADM_M92_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M92_Spacer_20mm'])

    @classmethod
    def ADM_M92_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M92_Spacer_25mm'])

class AdmSpacer(Spacer):
    _DATABASE = {'ADM_M42_Spacer_0_1mm': {'brand': 'ADM', 'name': 'M42 Spacer 0.1mm', 'type': 'type_spacer', 'optical_length': 0.1, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M42_Spacer_0_2mm': {'brand': 'ADM', 'name': 'M42 Spacer 0.2mm', 'type': 'type_spacer', 'optical_length': 0.2, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M42_Spacer_0_3mm': {'brand': 'ADM', 'name': 'M42 Spacer 0.3mm', 'type': 'type_spacer', 'optical_length': 0.3, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M42_Spacer_0_5mm': {'brand': 'ADM', 'name': 'M42 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M42_Spacer_0_7mm': {'brand': 'ADM', 'name': 'M42 Spacer 0.7mm', 'type': 'type_spacer', 'optical_length': 0.7, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M42_Spacer_1mm': {'brand': 'ADM', 'name': 'M42 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M42_Spacer_1_5mm': {'brand': 'ADM', 'name': 'M42 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M42_Spacer_2mm': {'brand': 'ADM', 'name': 'M42 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M48_Spacer_0_1mm': {'brand': 'ADM', 'name': 'M48 Spacer 0.1mm', 'type': 'type_spacer', 'optical_length': 0.1, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M48_Spacer_0_2mm': {'brand': 'ADM', 'name': 'M48 Spacer 0.2mm', 'type': 'type_spacer', 'optical_length': 0.2, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M48_Spacer_0_3mm': {'brand': 'ADM', 'name': 'M48 Spacer 0.3mm', 'type': 'type_spacer', 'optical_length': 0.3, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M48_Spacer_0_5mm': {'brand': 'ADM', 'name': 'M48 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M48_Spacer_0_7mm': {'brand': 'ADM', 'name': 'M48 Spacer 0.7mm', 'type': 'type_spacer', 'optical_length': 0.7, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M48_Spacer_1mm': {'brand': 'ADM', 'name': 'M48 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M48_Spacer_1_5mm': {'brand': 'ADM', 'name': 'M48 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M48_Spacer_2mm': {'brand': 'ADM', 'name': 'M48 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M54_Spacer_0_1mm': {'brand': 'ADM', 'name': 'M54 Spacer 0.1mm', 'type': 'type_spacer', 'optical_length': 0.1, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M54_Spacer_0_2mm': {'brand': 'ADM', 'name': 'M54 Spacer 0.2mm', 'type': 'type_spacer', 'optical_length': 0.2, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M54_Spacer_0_5mm': {'brand': 'ADM', 'name': 'M54 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M54_Spacer_1mm': {'brand': 'ADM', 'name': 'M54 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M54_Spacer_2mm': {'brand': 'ADM', 'name': 'M54 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M68_Spacer_0_3mm': {'brand': 'ADM', 'name': 'M68 Spacer 0.3mm', 'type': 'type_spacer', 'optical_length': 0.3, 'mass': 10, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M68_Spacer_0_5mm': {'brand': 'ADM', 'name': 'M68 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 10, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M68_Spacer_0_7mm': {'brand': 'ADM', 'name': 'M68 Spacer 0.7mm', 'type': 'type_spacer', 'optical_length': 0.7, 'mass': 10, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M68_Spacer_1mm': {'brand': 'ADM', 'name': 'M68 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 10, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M68_Spacer_1_5mm': {'brand': 'ADM', 'name': 'M68 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 10, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M68_Spacer_2mm': {'brand': 'ADM', 'name': 'M68 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 10, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M42_Spacer_1_1mm': {'brand': 'ADM', 'name': 'M42 Spacer 1.1mm', 'type': 'type_spacer', 'optical_length': 1.1, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M42_Spacer_1_3mm': {'brand': 'ADM', 'name': 'M42 Spacer 1.3mm', 'type': 'type_spacer', 'optical_length': 1.3, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M42_Spacer_1_7mm': {'brand': 'ADM', 'name': 'M42 Spacer 1.7mm', 'type': 'type_spacer', 'optical_length': 1.7, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M48_Spacer_1_1mm': {'brand': 'ADM', 'name': 'M48 Spacer 1.1mm', 'type': 'type_spacer', 'optical_length': 1.1, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M48_Spacer_1_3mm': {'brand': 'ADM', 'name': 'M48 Spacer 1.3mm', 'type': 'type_spacer', 'optical_length': 1.3, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M48_Spacer_1_7mm': {'brand': 'ADM', 'name': 'M48 Spacer 1.7mm', 'type': 'type_spacer', 'optical_length': 1.7, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M54_Spacer_1_1mm': {'brand': 'ADM', 'name': 'M54 Spacer 1.1mm', 'type': 'type_spacer', 'optical_length': 1.1, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M54_Spacer_1_3mm': {'brand': 'ADM', 'name': 'M54 Spacer 1.3mm', 'type': 'type_spacer', 'optical_length': 1.3, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M54_Spacer_1_7mm': {'brand': 'ADM', 'name': 'M54 Spacer 1.7mm', 'type': 'type_spacer', 'optical_length': 1.7, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M68_Spacer_1_1mm': {'brand': 'ADM', 'name': 'M68 Spacer 1.1mm', 'type': 'type_spacer', 'optical_length': 1.1, 'mass': 10, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M68_Spacer_1_3mm': {'brand': 'ADM', 'name': 'M68 Spacer 1.3mm', 'type': 'type_spacer', 'optical_length': 1.3, 'mass': 10, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M68_Spacer_1_7mm': {'brand': 'ADM', 'name': 'M68 Spacer 1.7mm', 'type': 'type_spacer', 'optical_length': 1.7, 'mass': 10, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M72_Spacer_0_5mm': {'brand': 'ADM', 'name': 'M72 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 12, 'tside_thread': 'M72', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M72_Spacer_0_7mm': {'brand': 'ADM', 'name': 'M72 Spacer 0.7mm', 'type': 'type_spacer', 'optical_length': 0.7, 'mass': 12, 'tside_thread': 'M72', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M72_Spacer_1mm': {'brand': 'ADM', 'name': 'M72 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 12, 'tside_thread': 'M72', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M72_Spacer_1_5mm': {'brand': 'ADM', 'name': 'M72 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 12, 'tside_thread': 'M72', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M72_Spacer_2mm': {'brand': 'ADM', 'name': 'M72 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 12, 'tside_thread': 'M72', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M92_Spacer_0_5mm': {'brand': 'ADM', 'name': 'M92 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 17, 'tside_thread': 'M92', 'tside_gender': '', 'cside_thread': 'M92', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M92_Spacer_1mm': {'brand': 'ADM', 'name': 'M92 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 17, 'tside_thread': 'M92', 'tside_gender': '', 'cside_thread': 'M92', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M92_Spacer_1_5mm': {'brand': 'ADM', 'name': 'M92 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 17, 'tside_thread': 'M92', 'tside_gender': '', 'cside_thread': 'M92', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'ADM_M92_Spacer_2mm': {'brand': 'ADM', 'name': 'M92 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 17, 'tside_thread': 'M92', 'tside_gender': '', 'cside_thread': 'M92', 'cside_gender': '', 'reversible': True, 'bf_role': ''}}

    @classmethod
    def ADM_M42_Spacer_0_1mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Spacer_0_1mm'])

    @classmethod
    def ADM_M42_Spacer_0_2mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Spacer_0_2mm'])

    @classmethod
    def ADM_M42_Spacer_0_3mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Spacer_0_3mm'])

    @classmethod
    def ADM_M42_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Spacer_0_5mm'])

    @classmethod
    def ADM_M42_Spacer_0_7mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Spacer_0_7mm'])

    @classmethod
    def ADM_M42_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Spacer_1mm'])

    @classmethod
    def ADM_M42_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Spacer_1_5mm'])

    @classmethod
    def ADM_M42_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Spacer_2mm'])

    @classmethod
    def ADM_M48_Spacer_0_1mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Spacer_0_1mm'])

    @classmethod
    def ADM_M48_Spacer_0_2mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Spacer_0_2mm'])

    @classmethod
    def ADM_M48_Spacer_0_3mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Spacer_0_3mm'])

    @classmethod
    def ADM_M48_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Spacer_0_5mm'])

    @classmethod
    def ADM_M48_Spacer_0_7mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Spacer_0_7mm'])

    @classmethod
    def ADM_M48_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Spacer_1mm'])

    @classmethod
    def ADM_M48_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Spacer_1_5mm'])

    @classmethod
    def ADM_M48_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Spacer_2mm'])

    @classmethod
    def ADM_M54_Spacer_0_1mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Spacer_0_1mm'])

    @classmethod
    def ADM_M54_Spacer_0_2mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Spacer_0_2mm'])

    @classmethod
    def ADM_M54_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Spacer_0_5mm'])

    @classmethod
    def ADM_M54_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Spacer_1mm'])

    @classmethod
    def ADM_M54_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Spacer_2mm'])

    @classmethod
    def ADM_M68_Spacer_0_3mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Spacer_0_3mm'])

    @classmethod
    def ADM_M68_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Spacer_0_5mm'])

    @classmethod
    def ADM_M68_Spacer_0_7mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Spacer_0_7mm'])

    @classmethod
    def ADM_M68_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Spacer_1mm'])

    @classmethod
    def ADM_M68_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Spacer_1_5mm'])

    @classmethod
    def ADM_M68_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Spacer_2mm'])

    @classmethod
    def ADM_M42_Spacer_1_1mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Spacer_1_1mm'])

    @classmethod
    def ADM_M42_Spacer_1_3mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Spacer_1_3mm'])

    @classmethod
    def ADM_M42_Spacer_1_7mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M42_Spacer_1_7mm'])

    @classmethod
    def ADM_M48_Spacer_1_1mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Spacer_1_1mm'])

    @classmethod
    def ADM_M48_Spacer_1_3mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Spacer_1_3mm'])

    @classmethod
    def ADM_M48_Spacer_1_7mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M48_Spacer_1_7mm'])

    @classmethod
    def ADM_M54_Spacer_1_1mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Spacer_1_1mm'])

    @classmethod
    def ADM_M54_Spacer_1_3mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Spacer_1_3mm'])

    @classmethod
    def ADM_M54_Spacer_1_7mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M54_Spacer_1_7mm'])

    @classmethod
    def ADM_M68_Spacer_1_1mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Spacer_1_1mm'])

    @classmethod
    def ADM_M68_Spacer_1_3mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Spacer_1_3mm'])

    @classmethod
    def ADM_M68_Spacer_1_7mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M68_Spacer_1_7mm'])

    @classmethod
    def ADM_M72_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M72_Spacer_0_5mm'])

    @classmethod
    def ADM_M72_Spacer_0_7mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M72_Spacer_0_7mm'])

    @classmethod
    def ADM_M72_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M72_Spacer_1mm'])

    @classmethod
    def ADM_M72_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M72_Spacer_1_5mm'])

    @classmethod
    def ADM_M72_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M72_Spacer_2mm'])

    @classmethod
    def ADM_M92_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M92_Spacer_0_5mm'])

    @classmethod
    def ADM_M92_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M92_Spacer_1mm'])

    @classmethod
    def ADM_M92_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M92_Spacer_1_5mm'])

    @classmethod
    def ADM_M92_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['ADM_M92_Spacer_2mm'])