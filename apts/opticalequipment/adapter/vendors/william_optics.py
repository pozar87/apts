from ...abstract import IntermediateOpticalEquipment
from ....constants import OpticalType
from ..base import Adapter, Spacer

class William_opticsAdapter(Adapter):
    _DATABASE = {'William_Optics_M48_M42_Adapter': {'brand': 'William Optics', 'name': 'M48→M42 Adapter', 'type': 'type_adapter', 'optical_length': 5, 'mass': 20, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'William_Optics_Rotolock_M48': {'brand': 'William Optics', 'name': 'Rotolock M48', 'type': 'type_adapter', 'optical_length': 8, 'mass': 50, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'William_Optics_Rotolock_M54': {'brand': 'William Optics', 'name': 'Rotolock M54', 'type': 'type_adapter', 'optical_length': 8, 'mass': 55, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'William_Optics_M48_Canon_EOS': {'brand': 'William Optics', 'name': 'M48→Canon EOS', 'type': 'type_adapter', 'optical_length': 8, 'mass': 35, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'William_Optics_M48_Nikon_F': {'brand': 'William Optics', 'name': 'M48→Nikon F', 'type': 'type_adapter', 'optical_length': 8, 'mass': 35, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'William_Optics_M48_Sony_E': {'brand': 'William Optics', 'name': 'M48→Sony E', 'type': 'type_adapter', 'optical_length': 7, 'mass': 30, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'William_Optics_M48_Canon_RF': {'brand': 'William Optics', 'name': 'M48→Canon RF', 'type': 'type_adapter', 'optical_length': 5, 'mass': 30, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'Canon RF', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'William_Optics_M48_Nikon_Z': {'brand': 'William Optics', 'name': 'M48→Nikon Z', 'type': 'type_adapter', 'optical_length': 6, 'mass': 30, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'Nikon Z', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'William_Optics_M48_Fuji_X': {'brand': 'William Optics', 'name': 'M48→Fuji X', 'type': 'type_adapter', 'optical_length': 7, 'mass': 30, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'Fuji X', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'William_Optics_M48_Spacer_5mm': {'brand': 'William Optics', 'name': 'M48 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 10, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M48_Spacer_10mm': {'brand': 'William Optics', 'name': 'M48 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 14, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M48_Spacer_15mm': {'brand': 'William Optics', 'name': 'M48 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M48_Spacer_20mm': {'brand': 'William Optics', 'name': 'M48 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 22, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M42_Spacer_3mm': {'brand': 'William Optics', 'name': 'M42 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M42_Spacer_5mm': {'brand': 'William Optics', 'name': 'M42 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 8, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M42_Spacer_7mm': {'brand': 'William Optics', 'name': 'M42 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 9, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M42_Spacer_10mm': {'brand': 'William Optics', 'name': 'M42 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 12, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M42_Spacer_15mm': {'brand': 'William Optics', 'name': 'M42 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M48_Spacer_3mm': {'brand': 'William Optics', 'name': 'M48 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M48_Spacer_7mm': {'brand': 'William Optics', 'name': 'M48 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 11, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M54_Spacer_5mm': {'brand': 'William Optics', 'name': 'M54 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 12, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M54_Spacer_10mm': {'brand': 'William Optics', 'name': 'M54 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 16, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M54_Spacer_15mm': {'brand': 'William Optics', 'name': 'M54 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 20, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M68_Spacer_5mm': {'brand': 'William Optics', 'name': 'M68 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 14, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M68_Spacer_10mm': {'brand': 'William Optics', 'name': 'M68 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 18, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M68_Spacer_15mm': {'brand': 'William Optics', 'name': 'M68 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 22, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M68_Spacer_20mm': {'brand': 'William Optics', 'name': 'M68 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 26, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M42_Spacer_2_5mm': {'brand': 'William Optics', 'name': 'M42 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M42_Spacer_3_5mm': {'brand': 'William Optics', 'name': 'M42 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M42_Spacer_4_5mm': {'brand': 'William Optics', 'name': 'M42 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 7, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M42_Spacer_5_5mm': {'brand': 'William Optics', 'name': 'M42 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 8, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M42_Spacer_6_5mm': {'brand': 'William Optics', 'name': 'M42 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 9, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M42_Spacer_7_5mm': {'brand': 'William Optics', 'name': 'M42 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 10, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M42_Spacer_8_5mm': {'brand': 'William Optics', 'name': 'M42 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 10, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M42_Spacer_9_5mm': {'brand': 'William Optics', 'name': 'M42 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 11, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M42_Spacer_11mm': {'brand': 'William Optics', 'name': 'M42 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 12, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M42_Spacer_12mm': {'brand': 'William Optics', 'name': 'M42 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 13, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M42_Spacer_13mm': {'brand': 'William Optics', 'name': 'M42 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 14, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M42_Spacer_14mm': {'brand': 'William Optics', 'name': 'M42 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 15, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M42_Spacer_16mm': {'brand': 'William Optics', 'name': 'M42 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M42_Spacer_18mm': {'brand': 'William Optics', 'name': 'M42 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 18, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M42_Spacer_22mm': {'brand': 'William Optics', 'name': 'M42 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 21, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M48_Spacer_2_5mm': {'brand': 'William Optics', 'name': 'M48 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M48_Spacer_3_5mm': {'brand': 'William Optics', 'name': 'M48 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M48_Spacer_4_5mm': {'brand': 'William Optics', 'name': 'M48 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 9, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M48_Spacer_5_5mm': {'brand': 'William Optics', 'name': 'M48 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 10, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M48_Spacer_6_5mm': {'brand': 'William Optics', 'name': 'M48 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 11, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M48_Spacer_7_5mm': {'brand': 'William Optics', 'name': 'M48 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 12, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M48_Spacer_8_5mm': {'brand': 'William Optics', 'name': 'M48 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 12, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M48_Spacer_9_5mm': {'brand': 'William Optics', 'name': 'M48 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 13, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M48_Spacer_11mm': {'brand': 'William Optics', 'name': 'M48 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 14, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M48_Spacer_12mm': {'brand': 'William Optics', 'name': 'M48 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 15, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M48_Spacer_13mm': {'brand': 'William Optics', 'name': 'M48 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 16, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M48_Spacer_14mm': {'brand': 'William Optics', 'name': 'M48 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 17, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M48_Spacer_16mm': {'brand': 'William Optics', 'name': 'M48 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M48_Spacer_18mm': {'brand': 'William Optics', 'name': 'M48 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 20, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M48_Spacer_22mm': {'brand': 'William Optics', 'name': 'M48 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 23, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M48_Spacer_25mm': {'brand': 'William Optics', 'name': 'M48 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 26, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'William_Optics_M42_Extension_Tube_3mm': {'brand': 'William Optics', 'name': 'M42 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 13, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'William_Optics_M42_Extension_Tube_6mm': {'brand': 'William Optics', 'name': 'M42 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 14, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'William_Optics_M42_Extension_Tube_9mm': {'brand': 'William Optics', 'name': 'M42 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 15, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'William_Optics_M42_Extension_Tube_11mm': {'brand': 'William Optics', 'name': 'M42 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'William_Optics_M42_Extension_Tube_13mm': {'brand': 'William Optics', 'name': 'M42 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'William_Optics_M42_Extension_Tube_16mm': {'brand': 'William Optics', 'name': 'M42 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 17, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'William_Optics_M42_Extension_Tube_22mm': {'brand': 'William Optics', 'name': 'M42 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 19, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'William_Optics_M42_Extension_Tube_28mm': {'brand': 'William Optics', 'name': 'M42 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 21, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'William_Optics_M42_Extension_Tube_35mm': {'brand': 'William Optics', 'name': 'M42 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 23, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'William_Optics_M42_Extension_Tube_45mm': {'brand': 'William Optics', 'name': 'M42 Extension Tube 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 26, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'William_Optics_M48_Extension_Tube_3mm': {'brand': 'William Optics', 'name': 'M48 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 17, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'William_Optics_M48_Extension_Tube_6mm': {'brand': 'William Optics', 'name': 'M48 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'William_Optics_M48_Extension_Tube_9mm': {'brand': 'William Optics', 'name': 'M48 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 19, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'William_Optics_M48_Extension_Tube_11mm': {'brand': 'William Optics', 'name': 'M48 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 20, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'William_Optics_M48_Extension_Tube_13mm': {'brand': 'William Optics', 'name': 'M48 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 20, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'William_Optics_M48_Extension_Tube_16mm': {'brand': 'William Optics', 'name': 'M48 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 21, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'William_Optics_M48_Extension_Tube_22mm': {'brand': 'William Optics', 'name': 'M48 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 23, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'William_Optics_M48_Extension_Tube_28mm': {'brand': 'William Optics', 'name': 'M48 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 25, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'William_Optics_M48_Extension_Tube_35mm': {'brand': 'William Optics', 'name': 'M48 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 27, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'William_Optics_M48_Extension_Tube_45mm': {'brand': 'William Optics', 'name': 'M48 Extension Tube 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 30, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'William_Optics_M54_Extension_Tube_3mm': {'brand': 'William Optics', 'name': 'M54 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 21, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'William_Optics_M54_Extension_Tube_6mm': {'brand': 'William Optics', 'name': 'M54 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 22, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'William_Optics_M54_Extension_Tube_9mm': {'brand': 'William Optics', 'name': 'M54 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 23, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'William_Optics_M54_Extension_Tube_11mm': {'brand': 'William Optics', 'name': 'M54 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 24, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'William_Optics_M54_Extension_Tube_13mm': {'brand': 'William Optics', 'name': 'M54 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 24, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'William_Optics_M54_Extension_Tube_16mm': {'brand': 'William Optics', 'name': 'M54 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 25, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'William_Optics_M54_Extension_Tube_22mm': {'brand': 'William Optics', 'name': 'M54 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 27, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'William_Optics_M54_Extension_Tube_28mm': {'brand': 'William Optics', 'name': 'M54 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 29, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'William_Optics_M54_Extension_Tube_35mm': {'brand': 'William Optics', 'name': 'M54 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 31, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'William_Optics_M54_Extension_Tube_45mm': {'brand': 'William Optics', 'name': 'M54 Extension Tube 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 34, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def William_Optics_M48_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_M42_Adapter'])

    @classmethod
    def William_Optics_Rotolock_M48(cls):
        return cls.from_database(cls._DATABASE['William_Optics_Rotolock_M48'])

    @classmethod
    def William_Optics_Rotolock_M54(cls):
        return cls.from_database(cls._DATABASE['William_Optics_Rotolock_M54'])

    @classmethod
    def William_Optics_M48_Canon_EOS(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Canon_EOS'])

    @classmethod
    def William_Optics_M48_Nikon_F(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Nikon_F'])

    @classmethod
    def William_Optics_M48_Sony_E(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Sony_E'])

    @classmethod
    def William_Optics_M48_Canon_RF(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Canon_RF'])

    @classmethod
    def William_Optics_M48_Nikon_Z(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Nikon_Z'])

    @classmethod
    def William_Optics_M48_Fuji_X(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Fuji_X'])

    @classmethod
    def William_Optics_M48_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Spacer_5mm'])

    @classmethod
    def William_Optics_M48_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Spacer_10mm'])

    @classmethod
    def William_Optics_M48_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Spacer_15mm'])

    @classmethod
    def William_Optics_M48_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Spacer_20mm'])

    @classmethod
    def William_Optics_M42_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M42_Spacer_3mm'])

    @classmethod
    def William_Optics_M42_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M42_Spacer_5mm'])

    @classmethod
    def William_Optics_M42_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M42_Spacer_7mm'])

    @classmethod
    def William_Optics_M42_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M42_Spacer_10mm'])

    @classmethod
    def William_Optics_M42_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M42_Spacer_15mm'])

    @classmethod
    def William_Optics_M48_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Spacer_3mm'])

    @classmethod
    def William_Optics_M48_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Spacer_7mm'])

    @classmethod
    def William_Optics_M54_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M54_Spacer_5mm'])

    @classmethod
    def William_Optics_M54_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M54_Spacer_10mm'])

    @classmethod
    def William_Optics_M54_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M54_Spacer_15mm'])

    @classmethod
    def William_Optics_M68_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M68_Spacer_5mm'])

    @classmethod
    def William_Optics_M68_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M68_Spacer_10mm'])

    @classmethod
    def William_Optics_M68_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M68_Spacer_15mm'])

    @classmethod
    def William_Optics_M68_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M68_Spacer_20mm'])

    @classmethod
    def William_Optics_M42_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M42_Spacer_2_5mm'])

    @classmethod
    def William_Optics_M42_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M42_Spacer_3_5mm'])

    @classmethod
    def William_Optics_M42_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M42_Spacer_4_5mm'])

    @classmethod
    def William_Optics_M42_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M42_Spacer_5_5mm'])

    @classmethod
    def William_Optics_M42_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M42_Spacer_6_5mm'])

    @classmethod
    def William_Optics_M42_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M42_Spacer_7_5mm'])

    @classmethod
    def William_Optics_M42_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M42_Spacer_8_5mm'])

    @classmethod
    def William_Optics_M42_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M42_Spacer_9_5mm'])

    @classmethod
    def William_Optics_M42_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M42_Spacer_11mm'])

    @classmethod
    def William_Optics_M42_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M42_Spacer_12mm'])

    @classmethod
    def William_Optics_M42_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M42_Spacer_13mm'])

    @classmethod
    def William_Optics_M42_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M42_Spacer_14mm'])

    @classmethod
    def William_Optics_M42_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M42_Spacer_16mm'])

    @classmethod
    def William_Optics_M42_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M42_Spacer_18mm'])

    @classmethod
    def William_Optics_M42_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M42_Spacer_22mm'])

    @classmethod
    def William_Optics_M48_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Spacer_2_5mm'])

    @classmethod
    def William_Optics_M48_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Spacer_3_5mm'])

    @classmethod
    def William_Optics_M48_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Spacer_4_5mm'])

    @classmethod
    def William_Optics_M48_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Spacer_5_5mm'])

    @classmethod
    def William_Optics_M48_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Spacer_6_5mm'])

    @classmethod
    def William_Optics_M48_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Spacer_7_5mm'])

    @classmethod
    def William_Optics_M48_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Spacer_8_5mm'])

    @classmethod
    def William_Optics_M48_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Spacer_9_5mm'])

    @classmethod
    def William_Optics_M48_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Spacer_11mm'])

    @classmethod
    def William_Optics_M48_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Spacer_12mm'])

    @classmethod
    def William_Optics_M48_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Spacer_13mm'])

    @classmethod
    def William_Optics_M48_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Spacer_14mm'])

    @classmethod
    def William_Optics_M48_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Spacer_16mm'])

    @classmethod
    def William_Optics_M48_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Spacer_18mm'])

    @classmethod
    def William_Optics_M48_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Spacer_22mm'])

    @classmethod
    def William_Optics_M48_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Spacer_25mm'])

    @classmethod
    def William_Optics_M42_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M42_Extension_Tube_3mm'])

    @classmethod
    def William_Optics_M42_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M42_Extension_Tube_6mm'])

    @classmethod
    def William_Optics_M42_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M42_Extension_Tube_9mm'])

    @classmethod
    def William_Optics_M42_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M42_Extension_Tube_11mm'])

    @classmethod
    def William_Optics_M42_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M42_Extension_Tube_13mm'])

    @classmethod
    def William_Optics_M42_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M42_Extension_Tube_16mm'])

    @classmethod
    def William_Optics_M42_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M42_Extension_Tube_22mm'])

    @classmethod
    def William_Optics_M42_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M42_Extension_Tube_28mm'])

    @classmethod
    def William_Optics_M42_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M42_Extension_Tube_35mm'])

    @classmethod
    def William_Optics_M42_Extension_Tube_45mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M42_Extension_Tube_45mm'])

    @classmethod
    def William_Optics_M48_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Extension_Tube_3mm'])

    @classmethod
    def William_Optics_M48_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Extension_Tube_6mm'])

    @classmethod
    def William_Optics_M48_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Extension_Tube_9mm'])

    @classmethod
    def William_Optics_M48_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Extension_Tube_11mm'])

    @classmethod
    def William_Optics_M48_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Extension_Tube_13mm'])

    @classmethod
    def William_Optics_M48_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Extension_Tube_16mm'])

    @classmethod
    def William_Optics_M48_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Extension_Tube_22mm'])

    @classmethod
    def William_Optics_M48_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Extension_Tube_28mm'])

    @classmethod
    def William_Optics_M48_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Extension_Tube_35mm'])

    @classmethod
    def William_Optics_M48_Extension_Tube_45mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Extension_Tube_45mm'])

    @classmethod
    def William_Optics_M54_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M54_Extension_Tube_3mm'])

    @classmethod
    def William_Optics_M54_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M54_Extension_Tube_6mm'])

    @classmethod
    def William_Optics_M54_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M54_Extension_Tube_9mm'])

    @classmethod
    def William_Optics_M54_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M54_Extension_Tube_11mm'])

    @classmethod
    def William_Optics_M54_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M54_Extension_Tube_13mm'])

    @classmethod
    def William_Optics_M54_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M54_Extension_Tube_16mm'])

    @classmethod
    def William_Optics_M54_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M54_Extension_Tube_22mm'])

    @classmethod
    def William_Optics_M54_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M54_Extension_Tube_28mm'])

    @classmethod
    def William_Optics_M54_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M54_Extension_Tube_35mm'])

    @classmethod
    def William_Optics_M54_Extension_Tube_45mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M54_Extension_Tube_45mm'])

class William_opticsSpacer(Spacer):
    _DATABASE = {'William_Optics_M48_Spacer_1mm': {'brand': 'William Optics', 'name': 'M48 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'William_Optics_M48_Spacer_2mm': {'brand': 'William Optics', 'name': 'M48 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'William_Optics_M42_Spacer_1mm': {'brand': 'William Optics', 'name': 'M42 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'William_Optics_M42_Spacer_2mm': {'brand': 'William Optics', 'name': 'M42 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'William_Optics_M54_Spacer_1mm': {'brand': 'William Optics', 'name': 'M54 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'William_Optics_M54_Spacer_2mm': {'brand': 'William Optics', 'name': 'M54 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'William_Optics_M68_Spacer_2mm': {'brand': 'William Optics', 'name': 'M68 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'William_Optics_M42_Spacer_0_5mm': {'brand': 'William Optics', 'name': 'M42 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'William_Optics_M42_Spacer_0_7mm': {'brand': 'William Optics', 'name': 'M42 Spacer 0.7mm', 'type': 'type_spacer', 'optical_length': 0.7, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'William_Optics_M42_Spacer_1_5mm': {'brand': 'William Optics', 'name': 'M42 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'William_Optics_M48_Spacer_0_5mm': {'brand': 'William Optics', 'name': 'M48 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'William_Optics_M48_Spacer_0_7mm': {'brand': 'William Optics', 'name': 'M48 Spacer 0.7mm', 'type': 'type_spacer', 'optical_length': 0.7, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'William_Optics_M48_Spacer_1_5mm': {'brand': 'William Optics', 'name': 'M48 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}}

    @classmethod
    def William_Optics_M48_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Spacer_1mm'])

    @classmethod
    def William_Optics_M48_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Spacer_2mm'])

    @classmethod
    def William_Optics_M42_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M42_Spacer_1mm'])

    @classmethod
    def William_Optics_M42_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M42_Spacer_2mm'])

    @classmethod
    def William_Optics_M54_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M54_Spacer_1mm'])

    @classmethod
    def William_Optics_M54_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M54_Spacer_2mm'])

    @classmethod
    def William_Optics_M68_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M68_Spacer_2mm'])

    @classmethod
    def William_Optics_M42_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M42_Spacer_0_5mm'])

    @classmethod
    def William_Optics_M42_Spacer_0_7mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M42_Spacer_0_7mm'])

    @classmethod
    def William_Optics_M42_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M42_Spacer_1_5mm'])

    @classmethod
    def William_Optics_M48_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Spacer_0_5mm'])

    @classmethod
    def William_Optics_M48_Spacer_0_7mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Spacer_0_7mm'])

    @classmethod
    def William_Optics_M48_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_M48_Spacer_1_5mm'])