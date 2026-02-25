from ..base import Adapter, Spacer

class GenericAdapter(Adapter):
    _DATABASE = {'Generic_M42_M48_Adapter': {'brand': 'Generic', 'name': 'M42→M48 Adapter', 'type': 'type_adapter', 'optical_length': 5, 'mass': 20, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M48_M42_Adapter': {'brand': 'Generic', 'name': 'M48→M42 Adapter', 'type': 'type_adapter', 'optical_length': 5, 'mass': 20, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M42_M54_Adapter': {'brand': 'Generic', 'name': 'M42→M54 Adapter', 'type': 'type_adapter', 'optical_length': 10, 'mass': 25, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M54_M42_Adapter': {'brand': 'Generic', 'name': 'M54→M42 Adapter', 'type': 'type_adapter', 'optical_length': 10, 'mass': 25, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M42_M68_Adapter': {'brand': 'Generic', 'name': 'M42→M68 Adapter', 'type': 'type_adapter', 'optical_length': 15, 'mass': 35, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M68_M42_Adapter': {'brand': 'Generic', 'name': 'M68→M42 Adapter', 'type': 'type_adapter', 'optical_length': 15, 'mass': 35, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M48_M54_Adapter': {'brand': 'Generic', 'name': 'M48→M54 Adapter', 'type': 'type_adapter', 'optical_length': 7, 'mass': 25, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M54_M48_Adapter': {'brand': 'Generic', 'name': 'M54→M48 Adapter', 'type': 'type_adapter', 'optical_length': 7, 'mass': 25, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M48_M68_Adapter': {'brand': 'Generic', 'name': 'M48→M68 Adapter', 'type': 'type_adapter', 'optical_length': 10, 'mass': 35, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M68_M48_Adapter': {'brand': 'Generic', 'name': 'M68→M48 Adapter', 'type': 'type_adapter', 'optical_length': 10, 'mass': 35, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M48_M72_Adapter': {'brand': 'Generic', 'name': 'M48→M72 Adapter', 'type': 'type_adapter', 'optical_length': 12, 'mass': 40, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M72_M48_Adapter': {'brand': 'Generic', 'name': 'M72→M48 Adapter', 'type': 'type_adapter', 'optical_length': 12, 'mass': 40, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M54_M68_Adapter': {'brand': 'Generic', 'name': 'M54→M68 Adapter', 'type': 'type_adapter', 'optical_length': 8, 'mass': 30, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M68_M54_Adapter': {'brand': 'Generic', 'name': 'M68→M54 Adapter', 'type': 'type_adapter', 'optical_length': 8, 'mass': 30, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M54_M72_Adapter': {'brand': 'Generic', 'name': 'M54→M72 Adapter', 'type': 'type_adapter', 'optical_length': 10, 'mass': 35, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M72_M54_Adapter': {'brand': 'Generic', 'name': 'M72→M54 Adapter', 'type': 'type_adapter', 'optical_length': 10, 'mass': 35, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M54_M82_Adapter': {'brand': 'Generic', 'name': 'M54→M82 Adapter', 'type': 'type_adapter', 'optical_length': 12, 'mass': 40, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M82_M54_Adapter': {'brand': 'Generic', 'name': 'M82→M54 Adapter', 'type': 'type_adapter', 'optical_length': 12, 'mass': 40, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M68_M72_Adapter': {'brand': 'Generic', 'name': 'M68→M72 Adapter', 'type': 'type_adapter', 'optical_length': 5, 'mass': 30, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M72_M68_Adapter': {'brand': 'Generic', 'name': 'M72→M68 Adapter', 'type': 'type_adapter', 'optical_length': 5, 'mass': 30, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M68_M82_Adapter': {'brand': 'Generic', 'name': 'M68→M82 Adapter', 'type': 'type_adapter', 'optical_length': 6, 'mass': 35, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M82_M68_Adapter': {'brand': 'Generic', 'name': 'M82→M68 Adapter', 'type': 'type_adapter', 'optical_length': 6, 'mass': 35, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M68_M84_Adapter': {'brand': 'Generic', 'name': 'M68→M84 Adapter', 'type': 'type_adapter', 'optical_length': 8, 'mass': 40, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M84_M68_Adapter': {'brand': 'Generic', 'name': 'M84→M68 Adapter', 'type': 'type_adapter', 'optical_length': 8, 'mass': 40, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M72_M82_Adapter': {'brand': 'Generic', 'name': 'M72→M82 Adapter', 'type': 'type_adapter', 'optical_length': 6, 'mass': 35, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M82_M72_Adapter': {'brand': 'Generic', 'name': 'M82→M72 Adapter', 'type': 'type_adapter', 'optical_length': 6, 'mass': 35, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M72_M84_Adapter': {'brand': 'Generic', 'name': 'M72→M84 Adapter', 'type': 'type_adapter', 'optical_length': 8, 'mass': 40, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M84_M72_Adapter': {'brand': 'Generic', 'name': 'M84→M72 Adapter', 'type': 'type_adapter', 'optical_length': 8, 'mass': 40, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M82_M84_Adapter': {'brand': 'Generic', 'name': 'M82→M84 Adapter', 'type': 'type_adapter', 'optical_length': 4, 'mass': 30, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M84_M82_Adapter': {'brand': 'Generic', 'name': 'M84→M82 Adapter', 'type': 'type_adapter', 'optical_length': 4, 'mass': 30, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M82_M92_Adapter': {'brand': 'Generic', 'name': 'M82→M92 Adapter', 'type': 'type_adapter', 'optical_length': 8, 'mass': 40, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M92_M82_Adapter': {'brand': 'Generic', 'name': 'M92→M82 Adapter', 'type': 'type_adapter', 'optical_length': 8, 'mass': 40, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M84_M92_Adapter': {'brand': 'Generic', 'name': 'M84→M92 Adapter', 'type': 'type_adapter', 'optical_length': 6, 'mass': 35, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M92_M84_Adapter': {'brand': 'Generic', 'name': 'M92→M84 Adapter', 'type': 'type_adapter', 'optical_length': 6, 'mass': 35, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M92_M117_Adapter': {'brand': 'Generic', 'name': 'M92→M117 Adapter', 'type': 'type_adapter', 'optical_length': 10, 'mass': 60, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M117_M92_Adapter': {'brand': 'Generic', 'name': 'M117→M92 Adapter', 'type': 'type_adapter', 'optical_length': 10, 'mass': 60, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M84_M117_Adapter': {'brand': 'Generic', 'name': 'M84→M117 Adapter', 'type': 'type_adapter', 'optical_length': 12, 'mass': 65, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M117_M84_Adapter': {'brand': 'Generic', 'name': 'M117→M84 Adapter', 'type': 'type_adapter', 'optical_length': 12, 'mass': 65, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M68_M117_Adapter': {'brand': 'Generic', 'name': 'M68→M117 Adapter', 'type': 'type_adapter', 'optical_length': 43, 'mass': 200, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M117_M68_Adapter': {'brand': 'Generic', 'name': 'M117→M68 Adapter', 'type': 'type_adapter', 'optical_length': 43, 'mass': 200, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M82_M117_Adapter': {'brand': 'Generic', 'name': 'M82→M117 Adapter', 'type': 'type_adapter', 'optical_length': 15, 'mass': 70, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M117_M82_Adapter': {'brand': 'Generic', 'name': 'M117→M82 Adapter', 'type': 'type_adapter', 'optical_length': 15, 'mass': 70, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M42_Extension_Tube_5mm': {'brand': 'Generic', 'name': 'M42 Extension Tube 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M42_Extension_Tube_10mm': {'brand': 'Generic', 'name': 'M42 Extension Tube 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 18, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M42_Extension_Tube_15mm': {'brand': 'Generic', 'name': 'M42 Extension Tube 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 19, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M42_Extension_Tube_20mm': {'brand': 'Generic', 'name': 'M42 Extension Tube 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 21, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M42_Extension_Tube_25mm': {'brand': 'Generic', 'name': 'M42 Extension Tube 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 22, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M42_Extension_Tube_30mm': {'brand': 'Generic', 'name': 'M42 Extension Tube 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 24, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M42_Extension_Tube_40mm': {'brand': 'Generic', 'name': 'M42 Extension Tube 40mm', 'type': 'type_adapter', 'optical_length': 40, 'mass': 27, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M42_Extension_Tube_50mm': {'brand': 'Generic', 'name': 'M42 Extension Tube 50mm', 'type': 'type_adapter', 'optical_length': 50, 'mass': 30, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M48_Extension_Tube_5mm': {'brand': 'Generic', 'name': 'M48 Extension Tube 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 21, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M48_Extension_Tube_10mm': {'brand': 'Generic', 'name': 'M48 Extension Tube 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 23, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M48_Extension_Tube_15mm': {'brand': 'Generic', 'name': 'M48 Extension Tube 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 24, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M48_Extension_Tube_20mm': {'brand': 'Generic', 'name': 'M48 Extension Tube 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 26, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M48_Extension_Tube_25mm': {'brand': 'Generic', 'name': 'M48 Extension Tube 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 27, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M48_Extension_Tube_30mm': {'brand': 'Generic', 'name': 'M48 Extension Tube 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 29, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M48_Extension_Tube_40mm': {'brand': 'Generic', 'name': 'M48 Extension Tube 40mm', 'type': 'type_adapter', 'optical_length': 40, 'mass': 32, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M48_Extension_Tube_50mm': {'brand': 'Generic', 'name': 'M48 Extension Tube 50mm', 'type': 'type_adapter', 'optical_length': 50, 'mass': 35, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M54_Extension_Tube_5mm': {'brand': 'Generic', 'name': 'M54 Extension Tube 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 26, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M54_Extension_Tube_10mm': {'brand': 'Generic', 'name': 'M54 Extension Tube 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 28, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M54_Extension_Tube_15mm': {'brand': 'Generic', 'name': 'M54 Extension Tube 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 29, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M54_Extension_Tube_20mm': {'brand': 'Generic', 'name': 'M54 Extension Tube 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 31, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M54_Extension_Tube_25mm': {'brand': 'Generic', 'name': 'M54 Extension Tube 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 32, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M54_Extension_Tube_30mm': {'brand': 'Generic', 'name': 'M54 Extension Tube 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 34, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M54_Extension_Tube_40mm': {'brand': 'Generic', 'name': 'M54 Extension Tube 40mm', 'type': 'type_adapter', 'optical_length': 40, 'mass': 37, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M54_Extension_Tube_50mm': {'brand': 'Generic', 'name': 'M54 Extension Tube 50mm', 'type': 'type_adapter', 'optical_length': 50, 'mass': 40, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M68_Extension_Tube_5mm': {'brand': 'Generic', 'name': 'M68 Extension Tube 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 31, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M68_Extension_Tube_10mm': {'brand': 'Generic', 'name': 'M68 Extension Tube 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 33, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M68_Extension_Tube_15mm': {'brand': 'Generic', 'name': 'M68 Extension Tube 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 34, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M68_Extension_Tube_20mm': {'brand': 'Generic', 'name': 'M68 Extension Tube 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 36, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M68_Extension_Tube_25mm': {'brand': 'Generic', 'name': 'M68 Extension Tube 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 37, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M68_Extension_Tube_30mm': {'brand': 'Generic', 'name': 'M68 Extension Tube 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 39, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M68_Extension_Tube_40mm': {'brand': 'Generic', 'name': 'M68 Extension Tube 40mm', 'type': 'type_adapter', 'optical_length': 40, 'mass': 42, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M68_Extension_Tube_50mm': {'brand': 'Generic', 'name': 'M68 Extension Tube 50mm', 'type': 'type_adapter', 'optical_length': 50, 'mass': 45, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M72_Extension_Tube_5mm': {'brand': 'Generic', 'name': 'M72 Extension Tube 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 36, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M72_Extension_Tube_10mm': {'brand': 'Generic', 'name': 'M72 Extension Tube 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 38, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M72_Extension_Tube_15mm': {'brand': 'Generic', 'name': 'M72 Extension Tube 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 39, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M72_Extension_Tube_20mm': {'brand': 'Generic', 'name': 'M72 Extension Tube 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 41, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M72_Extension_Tube_25mm': {'brand': 'Generic', 'name': 'M72 Extension Tube 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 42, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M72_Extension_Tube_30mm': {'brand': 'Generic', 'name': 'M72 Extension Tube 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 44, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M72_Extension_Tube_40mm': {'brand': 'Generic', 'name': 'M72 Extension Tube 40mm', 'type': 'type_adapter', 'optical_length': 40, 'mass': 47, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M72_Extension_Tube_50mm': {'brand': 'Generic', 'name': 'M72 Extension Tube 50mm', 'type': 'type_adapter', 'optical_length': 50, 'mass': 50, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_T2_Ring_EOS': {'brand': 'Generic', 'name': 'T2 Ring EOS', 'type': 'type_adapter', 'optical_length': 10.5, 'mass': 30, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_EOS_M48_Adapter': {'brand': 'Generic', 'name': 'EOS→M48 Adapter', 'type': 'type_adapter', 'optical_length': 10.5, 'mass': 35, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_T2_Ring_Canon_RF': {'brand': 'Generic', 'name': 'T2 Ring Canon RF', 'type': 'type_adapter', 'optical_length': 5, 'mass': 25, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_Canon_RF_M48_Adapter': {'brand': 'Generic', 'name': 'Canon RF→M48 Adapter', 'type': 'type_adapter', 'optical_length': 5, 'mass': 30, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'Canon RF', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_T2_Ring_Nikon_F': {'brand': 'Generic', 'name': 'T2 Ring Nikon F', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 30, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_Nikon_F_M48_Adapter': {'brand': 'Generic', 'name': 'Nikon F→M48 Adapter', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 35, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_T2_Ring_Nikon_Z': {'brand': 'Generic', 'name': 'T2 Ring Nikon Z', 'type': 'type_adapter', 'optical_length': 6, 'mass': 25, 'tside_thread': 'Nikon Z', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_Nikon_Z_M48_Adapter': {'brand': 'Generic', 'name': 'Nikon Z→M48 Adapter', 'type': 'type_adapter', 'optical_length': 6, 'mass': 30, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'Nikon Z', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_T2_Ring_Sony_E': {'brand': 'Generic', 'name': 'T2 Ring Sony E', 'type': 'type_adapter', 'optical_length': 7, 'mass': 25, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_Sony_E_M48_Adapter': {'brand': 'Generic', 'name': 'Sony E→M48 Adapter', 'type': 'type_adapter', 'optical_length': 7, 'mass': 30, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_T2_Ring_Fuji_X': {'brand': 'Generic', 'name': 'T2 Ring Fuji X', 'type': 'type_adapter', 'optical_length': 7, 'mass': 25, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_Fuji_X_M48_Adapter': {'brand': 'Generic', 'name': 'Fuji X→M48 Adapter', 'type': 'type_adapter', 'optical_length': 7, 'mass': 30, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'Fuji X', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_T2_Ring_MFT': {'brand': 'Generic', 'name': 'T2 Ring MFT', 'type': 'type_adapter', 'optical_length': 7, 'mass': 25, 'tside_thread': 'MFT', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_MFT_M48_Adapter': {'brand': 'Generic', 'name': 'MFT→M48 Adapter', 'type': 'type_adapter', 'optical_length': 7, 'mass': 30, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'MFT', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_T2_Ring_Pentax_K': {'brand': 'Generic', 'name': 'T2 Ring Pentax K', 'type': 'type_adapter', 'optical_length': 8, 'mass': 30, 'tside_thread': 'Pentax K', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_Pentax_K_M48_Adapter': {'brand': 'Generic', 'name': 'Pentax K→M48 Adapter', 'type': 'type_adapter', 'optical_length': 8, 'mass': 35, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'Pentax K', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_Canon_RF_M42_Adapter': {'brand': 'Generic', 'name': 'Canon RF→M42 Adapter', 'type': 'type_adapter', 'optical_length': 5, 'mass': 25, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_Sony_E_M42_Adapter': {'brand': 'Generic', 'name': 'Sony E→M42 Adapter', 'type': 'type_adapter', 'optical_length': 7, 'mass': 25, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_Nikon_Z_M42_Adapter': {'brand': 'Generic', 'name': 'Nikon Z→M42 Adapter', 'type': 'type_adapter', 'optical_length': 6, 'mass': 25, 'tside_thread': 'Nikon Z', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_Fuji_X_M42_Adapter': {'brand': 'Generic', 'name': 'Fuji X→M42 Adapter', 'type': 'type_adapter', 'optical_length': 7, 'mass': 25, 'tside_thread': 'Fuji X', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_MFT_M42_Adapter': {'brand': 'Generic', 'name': 'MFT→M42 Adapter', 'type': 'type_adapter', 'optical_length': 7, 'mass': 25, 'tside_thread': 'MFT', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_Pentax_K_M42_Adapter': {'brand': 'Generic', 'name': 'Pentax K→M42 Adapter', 'type': 'type_adapter', 'optical_length': 8, 'mass': 25, 'tside_thread': 'Pentax K', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_1_25_CS_Adapter': {'brand': 'Generic', 'name': '1.25"→CS Adapter', 'type': 'type_adapter', 'optical_length': 0, 'mass': 10, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': 'CS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_2_1_25_Adapter': {'brand': 'Generic', 'name': '2"→1.25" Adapter', 'type': 'type_adapter', 'optical_length': 0, 'mass': 15, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_2_M42_Adapter': {'brand': 'Generic', 'name': '2"→M42 Adapter', 'type': 'type_adapter', 'optical_length': 0, 'mass': 15, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_2_M48_Adapter': {'brand': 'Generic', 'name': '2"→M48 Adapter', 'type': 'type_adapter', 'optical_length': 0, 'mass': 20, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_2_M54_Adapter': {'brand': 'Generic', 'name': '2"→M54 Adapter', 'type': 'type_adapter', 'optical_length': 0, 'mass': 25, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_1_25_M42_Adapter': {'brand': 'Generic', 'name': '1.25"→M42 Adapter', 'type': 'type_adapter', 'optical_length': 0, 'mass': 10, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_1_25_M48_Adapter': {'brand': 'Generic', 'name': '1.25"→M48 Adapter', 'type': 'type_adapter', 'optical_length': 0, 'mass': 12, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_SC_M42_Adapter_short': {'brand': 'Generic', 'name': 'SC→M42 Adapter (short)', 'type': 'type_adapter', 'optical_length': 15, 'mass': 40, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_SC_M42_Adapter_long': {'brand': 'Generic', 'name': 'SC→M42 Adapter (long)', 'type': 'type_adapter', 'optical_length': 45, 'mass': 70, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_SC_M48_Adapter': {'brand': 'Generic', 'name': 'SC→M48 Adapter', 'type': 'type_adapter', 'optical_length': 10, 'mass': 50, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_SC_M54_Adapter': {'brand': 'Generic', 'name': 'SC→M54 Adapter', 'type': 'type_adapter', 'optical_length': 15, 'mass': 60, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_SC_M68_Adapter': {'brand': 'Generic', 'name': 'SC→M68 Adapter', 'type': 'type_adapter', 'optical_length': 15, 'mass': 70, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_SC_2_Adapter': {'brand': 'Generic', 'name': 'SC→2" Adapter', 'type': 'type_adapter', 'optical_length': 40, 'mass': 80, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M42_Spacer_3mm': {'brand': 'Generic', 'name': 'M42 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_5mm': {'brand': 'Generic', 'name': 'M42 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 8, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_7mm': {'brand': 'Generic', 'name': 'M42 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 9, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_10mm': {'brand': 'Generic', 'name': 'M42 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 12, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_15mm': {'brand': 'Generic', 'name': 'M42 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_20mm': {'brand': 'Generic', 'name': 'M42 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 20, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_25mm': {'brand': 'Generic', 'name': 'M42 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 24, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_30mm': {'brand': 'Generic', 'name': 'M42 Spacer 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 28, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_3mm': {'brand': 'Generic', 'name': 'M48 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_5mm': {'brand': 'Generic', 'name': 'M48 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 10, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_7mm': {'brand': 'Generic', 'name': 'M48 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 11, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_10mm': {'brand': 'Generic', 'name': 'M48 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 14, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_15mm': {'brand': 'Generic', 'name': 'M48 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_20mm': {'brand': 'Generic', 'name': 'M48 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 22, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_25mm': {'brand': 'Generic', 'name': 'M48 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 26, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_30mm': {'brand': 'Generic', 'name': 'M48 Spacer 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 30, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_3mm': {'brand': 'Generic', 'name': 'M54 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 10, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_5mm': {'brand': 'Generic', 'name': 'M54 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 12, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_10mm': {'brand': 'Generic', 'name': 'M54 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 16, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_15mm': {'brand': 'Generic', 'name': 'M54 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 20, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_20mm': {'brand': 'Generic', 'name': 'M54 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 24, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_25mm': {'brand': 'Generic', 'name': 'M54 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 28, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_30mm': {'brand': 'Generic', 'name': 'M54 Spacer 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 32, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_3mm': {'brand': 'Generic', 'name': 'M68 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 12, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_5mm': {'brand': 'Generic', 'name': 'M68 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 14, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_10mm': {'brand': 'Generic', 'name': 'M68 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 18, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_15mm': {'brand': 'Generic', 'name': 'M68 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 22, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_20mm': {'brand': 'Generic', 'name': 'M68 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 26, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_25mm': {'brand': 'Generic', 'name': 'M68 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 30, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_30mm': {'brand': 'Generic', 'name': 'M68 Spacer 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 34, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M72_Spacer_5mm': {'brand': 'Generic', 'name': 'M72 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 16, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M72_Spacer_10mm': {'brand': 'Generic', 'name': 'M72 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 20, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M72_Spacer_15mm': {'brand': 'Generic', 'name': 'M72 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 24, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M72_Spacer_20mm': {'brand': 'Generic', 'name': 'M72 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 28, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M82_Spacer_5mm': {'brand': 'Generic', 'name': 'M82 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 19, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M82_Spacer_10mm': {'brand': 'Generic', 'name': 'M82 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 23, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M82_Spacer_15mm': {'brand': 'Generic', 'name': 'M82 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 27, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M82_Spacer_20mm': {'brand': 'Generic', 'name': 'M82 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 31, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_4mm': {'brand': 'Generic', 'name': 'M42 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 7, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_6mm': {'brand': 'Generic', 'name': 'M42 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 8, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_8mm': {'brand': 'Generic', 'name': 'M42 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 10, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_12mm': {'brand': 'Generic', 'name': 'M42 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 13, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_35mm': {'brand': 'Generic', 'name': 'M42 Spacer 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 32, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_40mm': {'brand': 'Generic', 'name': 'M42 Spacer 40mm', 'type': 'type_adapter', 'optical_length': 40, 'mass': 36, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_50mm': {'brand': 'Generic', 'name': 'M42 Spacer 50mm', 'type': 'type_adapter', 'optical_length': 50, 'mass': 44, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_4mm': {'brand': 'Generic', 'name': 'M48 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 9, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_6mm': {'brand': 'Generic', 'name': 'M48 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 10, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_8mm': {'brand': 'Generic', 'name': 'M48 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 12, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_12mm': {'brand': 'Generic', 'name': 'M48 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 15, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_35mm': {'brand': 'Generic', 'name': 'M48 Spacer 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 34, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_40mm': {'brand': 'Generic', 'name': 'M48 Spacer 40mm', 'type': 'type_adapter', 'optical_length': 40, 'mass': 38, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_50mm': {'brand': 'Generic', 'name': 'M48 Spacer 50mm', 'type': 'type_adapter', 'optical_length': 50, 'mass': 46, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_4mm': {'brand': 'Generic', 'name': 'M54 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 11, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_7mm': {'brand': 'Generic', 'name': 'M54 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 13, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_8mm': {'brand': 'Generic', 'name': 'M54 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 14, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_12mm': {'brand': 'Generic', 'name': 'M54 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 17, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_35mm': {'brand': 'Generic', 'name': 'M54 Spacer 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 36, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_40mm': {'brand': 'Generic', 'name': 'M54 Spacer 40mm', 'type': 'type_adapter', 'optical_length': 40, 'mass': 40, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_4mm': {'brand': 'Generic', 'name': 'M68 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 13, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_7mm': {'brand': 'Generic', 'name': 'M68 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 15, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_8mm': {'brand': 'Generic', 'name': 'M68 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 16, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_12mm': {'brand': 'Generic', 'name': 'M68 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 19, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_35mm': {'brand': 'Generic', 'name': 'M68 Spacer 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 38, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_40mm': {'brand': 'Generic', 'name': 'M68 Spacer 40mm', 'type': 'type_adapter', 'optical_length': 40, 'mass': 42, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M72_Spacer_3mm': {'brand': 'Generic', 'name': 'M72 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 14, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M72_Spacer_7mm': {'brand': 'Generic', 'name': 'M72 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 17, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M72_Spacer_25mm': {'brand': 'Generic', 'name': 'M72 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 32, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M72_Spacer_30mm': {'brand': 'Generic', 'name': 'M72 Spacer 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 36, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Extension_Tube_2mm': {'brand': 'Generic', 'name': 'M42 Extension Tube 2mm', 'type': 'type_adapter', 'optical_length': 2, 'mass': 12, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M42_Extension_Tube_3mm': {'brand': 'Generic', 'name': 'M42 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 12, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M42_Extension_Tube_7mm': {'brand': 'Generic', 'name': 'M42 Extension Tube 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 14, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M42_Extension_Tube_8mm': {'brand': 'Generic', 'name': 'M42 Extension Tube 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 14, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M42_Extension_Tube_12mm': {'brand': 'Generic', 'name': 'M42 Extension Tube 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 15, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M42_Extension_Tube_35mm': {'brand': 'Generic', 'name': 'M42 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 22, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M42_Extension_Tube_45mm': {'brand': 'Generic', 'name': 'M42 Extension Tube 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 25, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M42_Extension_Tube_60mm': {'brand': 'Generic', 'name': 'M42 Extension Tube 60mm', 'type': 'type_adapter', 'optical_length': 60, 'mass': 30, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M48_Extension_Tube_2mm': {'brand': 'Generic', 'name': 'M48 Extension Tube 2mm', 'type': 'type_adapter', 'optical_length': 2, 'mass': 16, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M48_Extension_Tube_3mm': {'brand': 'Generic', 'name': 'M48 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 16, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M48_Extension_Tube_7mm': {'brand': 'Generic', 'name': 'M48 Extension Tube 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M48_Extension_Tube_8mm': {'brand': 'Generic', 'name': 'M48 Extension Tube 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M48_Extension_Tube_12mm': {'brand': 'Generic', 'name': 'M48 Extension Tube 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 19, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M48_Extension_Tube_35mm': {'brand': 'Generic', 'name': 'M48 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 26, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M48_Extension_Tube_45mm': {'brand': 'Generic', 'name': 'M48 Extension Tube 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 29, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M48_Extension_Tube_60mm': {'brand': 'Generic', 'name': 'M48 Extension Tube 60mm', 'type': 'type_adapter', 'optical_length': 60, 'mass': 34, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M54_Extension_Tube_2mm': {'brand': 'Generic', 'name': 'M54 Extension Tube 2mm', 'type': 'type_adapter', 'optical_length': 2, 'mass': 20, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M54_Extension_Tube_3mm': {'brand': 'Generic', 'name': 'M54 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 20, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M54_Extension_Tube_7mm': {'brand': 'Generic', 'name': 'M54 Extension Tube 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 22, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M54_Extension_Tube_8mm': {'brand': 'Generic', 'name': 'M54 Extension Tube 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 22, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M54_Extension_Tube_12mm': {'brand': 'Generic', 'name': 'M54 Extension Tube 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 23, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M54_Extension_Tube_35mm': {'brand': 'Generic', 'name': 'M54 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 30, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M54_Extension_Tube_45mm': {'brand': 'Generic', 'name': 'M54 Extension Tube 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 33, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M54_Extension_Tube_60mm': {'brand': 'Generic', 'name': 'M54 Extension Tube 60mm', 'type': 'type_adapter', 'optical_length': 60, 'mass': 38, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M68_Extension_Tube_2mm': {'brand': 'Generic', 'name': 'M68 Extension Tube 2mm', 'type': 'type_adapter', 'optical_length': 2, 'mass': 25, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M68_Extension_Tube_3mm': {'brand': 'Generic', 'name': 'M68 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 25, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M68_Extension_Tube_7mm': {'brand': 'Generic', 'name': 'M68 Extension Tube 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 27, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M68_Extension_Tube_8mm': {'brand': 'Generic', 'name': 'M68 Extension Tube 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 27, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M68_Extension_Tube_12mm': {'brand': 'Generic', 'name': 'M68 Extension Tube 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 28, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M68_Extension_Tube_35mm': {'brand': 'Generic', 'name': 'M68 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 35, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M68_Extension_Tube_45mm': {'brand': 'Generic', 'name': 'M68 Extension Tube 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 38, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M68_Extension_Tube_60mm': {'brand': 'Generic', 'name': 'M68 Extension Tube 60mm', 'type': 'type_adapter', 'optical_length': 60, 'mass': 43, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_Eyepiece_Projection_Adapter_1_25': {'brand': 'Generic', 'name': 'Eyepiece Projection Adapter (1.25")', 'type': 'type_adapter', 'optical_length': 40, 'mass': 60, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_Eyepiece_Projection_Adapter_2': {'brand': 'Generic', 'name': 'Eyepiece Projection Adapter (2")', 'type': 'type_adapter', 'optical_length': 50, 'mass': 80, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_T_Thread_Extension_10mm': {'brand': 'Generic', 'name': 'T-Thread Extension 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 15, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_T_Thread_Extension_30mm': {'brand': 'Generic', 'name': 'T-Thread Extension 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 25, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_T_Thread_Extension_50mm': {'brand': 'Generic', 'name': 'T-Thread Extension 50mm', 'type': 'type_adapter', 'optical_length': 50, 'mass': 35, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M48_M54_Adapter_short_2mm': {'brand': 'Generic', 'name': 'M48→M54 Adapter (short, 2mm)', 'type': 'type_adapter', 'optical_length': 2, 'mass': 20, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M54_M68_Adapter_short_2mm': {'brand': 'Generic', 'name': 'M54→M68 Adapter (short, 2mm)', 'type': 'type_adapter', 'optical_length': 2, 'mass': 25, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M68_M72_Adapter_short_2mm': {'brand': 'Generic', 'name': 'M68→M72 Adapter (short, 2mm)', 'type': 'type_adapter', 'optical_length': 2, 'mass': 30, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M72_M82_Adapter_short_2mm': {'brand': 'Generic', 'name': 'M72→M82 Adapter (short, 2mm)', 'type': 'type_adapter', 'optical_length': 2, 'mass': 30, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M92_Spacer_5mm': {'brand': 'Generic', 'name': 'M92 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 22, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M92_Spacer_10mm': {'brand': 'Generic', 'name': 'M92 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 26, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M92_Spacer_15mm': {'brand': 'Generic', 'name': 'M92 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 30, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M117_Spacer_5mm': {'brand': 'Generic', 'name': 'M117 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 25, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M117_Spacer_10mm': {'brand': 'Generic', 'name': 'M117 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 30, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M117_Spacer_20mm': {'brand': 'Generic', 'name': 'M117 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 40, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M117_Spacer_30mm': {'brand': 'Generic', 'name': 'M117 Spacer 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 50, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Male_Male_Ring': {'brand': 'Generic', 'name': 'M42 Male-Male Ring', 'type': 'type_adapter', 'optical_length': 2, 'mass': 15, 'tside_thread': 'M42', 'tside_gender': 'Male', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Male_Male_Ring': {'brand': 'Generic', 'name': 'M48 Male-Male Ring', 'type': 'type_adapter', 'optical_length': 2, 'mass': 20, 'tside_thread': 'M48', 'tside_gender': 'Male', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Male_Male_Ring': {'brand': 'Generic', 'name': 'M54 Male-Male Ring', 'type': 'type_adapter', 'optical_length': 2, 'mass': 25, 'tside_thread': 'M54', 'tside_gender': 'Male', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M56_Spacer_5mm': {'brand': 'Generic', 'name': 'M56 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 12, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M56_Spacer_10mm': {'brand': 'Generic', 'name': 'M56 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 16, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M56_Spacer_15mm': {'brand': 'Generic', 'name': 'M56 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 20, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M56_Spacer_20mm': {'brand': 'Generic', 'name': 'M56 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 24, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M63_Spacer_5mm': {'brand': 'Generic', 'name': 'M63 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 14, 'tside_thread': 'M63', 'tside_gender': 'Female', 'cside_thread': 'M63', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M63_Spacer_10mm': {'brand': 'Generic', 'name': 'M63 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 18, 'tside_thread': 'M63', 'tside_gender': 'Female', 'cside_thread': 'M63', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M63_Spacer_15mm': {'brand': 'Generic', 'name': 'M63 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 22, 'tside_thread': 'M63', 'tside_gender': 'Female', 'cside_thread': 'M63', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M63_Spacer_20mm': {'brand': 'Generic', 'name': 'M63 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 26, 'tside_thread': 'M63', 'tside_gender': 'Female', 'cside_thread': 'M63', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M84_Spacer_5mm': {'brand': 'Generic', 'name': 'M84 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 18, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M84_Spacer_10mm': {'brand': 'Generic', 'name': 'M84 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 22, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M84_Spacer_15mm': {'brand': 'Generic', 'name': 'M84 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 26, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M84_Spacer_20mm': {'brand': 'Generic', 'name': 'M84 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 30, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_SC_Schmidt_Cassegrain_Spacer_3mm': {'brand': 'Generic', 'name': 'SC (Schmidt-Cassegrain) Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 22, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_SC_Schmidt_Cassegrain_Spacer_5mm': {'brand': 'Generic', 'name': 'SC (Schmidt-Cassegrain) Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 24, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_SC_Schmidt_Cassegrain_Spacer_7mm': {'brand': 'Generic', 'name': 'SC (Schmidt-Cassegrain) Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 25, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_SC_Schmidt_Cassegrain_Spacer_10mm': {'brand': 'Generic', 'name': 'SC (Schmidt-Cassegrain) Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 28, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_SC_Schmidt_Cassegrain_Spacer_15mm': {'brand': 'Generic', 'name': 'SC (Schmidt-Cassegrain) Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 32, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_SC_Schmidt_Cassegrain_Spacer_20mm': {'brand': 'Generic', 'name': 'SC (Schmidt-Cassegrain) Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 36, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_SC_Schmidt_Cassegrain_Spacer_25mm': {'brand': 'Generic', 'name': 'SC (Schmidt-Cassegrain) Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 40, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_SC_Schmidt_Cassegrain_Spacer_30mm': {'brand': 'Generic', 'name': 'SC (Schmidt-Cassegrain) Spacer 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 44, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_SC_Schmidt_Cassegrain_Spacer_40mm': {'brand': 'Generic', 'name': 'SC (Schmidt-Cassegrain) Spacer 40mm', 'type': 'type_adapter', 'optical_length': 40, 'mass': 52, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_SC_Schmidt_Cassegrain_Spacer_50mm': {'brand': 'Generic', 'name': 'SC (Schmidt-Cassegrain) Spacer 50mm', 'type': 'type_adapter', 'optical_length': 50, 'mass': 60, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_1_25_Spacer_5mm': {'brand': 'Generic', 'name': '1.25" Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 7, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_1_25_Spacer_10mm': {'brand': 'Generic', 'name': '1.25" Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 11, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_1_25_Spacer_15mm': {'brand': 'Generic', 'name': '1.25" Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 15, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_1_25_Spacer_20mm': {'brand': 'Generic', 'name': '1.25" Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 19, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_1_25_Spacer_25mm': {'brand': 'Generic', 'name': '1.25" Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 23, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_1_25_Spacer_30mm': {'brand': 'Generic', 'name': '1.25" Spacer 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 27, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_2_Spacer_5mm': {'brand': 'Generic', 'name': '2" Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 12, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_2_Spacer_10mm': {'brand': 'Generic', 'name': '2" Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 16, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_2_Spacer_15mm': {'brand': 'Generic', 'name': '2" Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 20, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_2_Spacer_20mm': {'brand': 'Generic', 'name': '2" Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 24, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_2_Spacer_25mm': {'brand': 'Generic', 'name': '2" Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 28, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_2_Spacer_30mm': {'brand': 'Generic', 'name': '2" Spacer 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 32, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_SC_Visual_Back_1_25': {'brand': 'Generic', 'name': 'SC Visual Back (1.25")', 'type': 'type_adapter', 'optical_length': 35, 'mass': 45, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_SC_Visual_Back_2': {'brand': 'Generic', 'name': 'SC Visual Back (2")', 'type': 'type_adapter', 'optical_length': 40, 'mass': 70, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M42_Spacer_9mm': {'brand': 'Generic', 'name': 'M42 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 11, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_14mm': {'brand': 'Generic', 'name': 'M42 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 15, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_17mm': {'brand': 'Generic', 'name': 'M42 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 17, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_22mm': {'brand': 'Generic', 'name': 'M42 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 21, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_28mm': {'brand': 'Generic', 'name': 'M42 Spacer 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 26, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_45mm': {'brand': 'Generic', 'name': 'M42 Spacer 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 40, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_9mm': {'brand': 'Generic', 'name': 'M48 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 13, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_14mm': {'brand': 'Generic', 'name': 'M48 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 17, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_17mm': {'brand': 'Generic', 'name': 'M48 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 19, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_22mm': {'brand': 'Generic', 'name': 'M48 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 23, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_28mm': {'brand': 'Generic', 'name': 'M48 Spacer 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 28, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_45mm': {'brand': 'Generic', 'name': 'M48 Spacer 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 42, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_6mm': {'brand': 'Generic', 'name': 'M54 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 12, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_9mm': {'brand': 'Generic', 'name': 'M54 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 15, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_14mm': {'brand': 'Generic', 'name': 'M54 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 19, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_17mm': {'brand': 'Generic', 'name': 'M54 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 21, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_22mm': {'brand': 'Generic', 'name': 'M54 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 25, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_28mm': {'brand': 'Generic', 'name': 'M54 Spacer 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 30, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_2_5mm': {'brand': 'Generic', 'name': 'M68 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 12, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_6mm': {'brand': 'Generic', 'name': 'M68 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 14, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_9mm': {'brand': 'Generic', 'name': 'M68 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 17, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_14mm': {'brand': 'Generic', 'name': 'M68 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 21, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_17mm': {'brand': 'Generic', 'name': 'M68 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 23, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_22mm': {'brand': 'Generic', 'name': 'M68 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 27, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_28mm': {'brand': 'Generic', 'name': 'M68 Spacer 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 32, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M72_Spacer_2_5mm': {'brand': 'Generic', 'name': 'M72 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 14, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M72_Spacer_4mm': {'brand': 'Generic', 'name': 'M72 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 15, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M72_Spacer_6mm': {'brand': 'Generic', 'name': 'M72 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 16, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M72_Spacer_8mm': {'brand': 'Generic', 'name': 'M72 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 18, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M72_Spacer_12mm': {'brand': 'Generic', 'name': 'M72 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 21, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M72_Spacer_17mm': {'brand': 'Generic', 'name': 'M72 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 25, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M82_Spacer_2_5mm': {'brand': 'Generic', 'name': 'M82 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 17, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M82_Spacer_3mm': {'brand': 'Generic', 'name': 'M82 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 17, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M82_Spacer_4mm': {'brand': 'Generic', 'name': 'M82 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 18, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M82_Spacer_6mm': {'brand': 'Generic', 'name': 'M82 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 19, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M82_Spacer_7mm': {'brand': 'Generic', 'name': 'M82 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 20, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M82_Spacer_8mm': {'brand': 'Generic', 'name': 'M82 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 21, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M82_Spacer_12mm': {'brand': 'Generic', 'name': 'M82 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 24, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M82_Spacer_17mm': {'brand': 'Generic', 'name': 'M82 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 28, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M82_Spacer_25mm': {'brand': 'Generic', 'name': 'M82 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 35, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M82_Spacer_30mm': {'brand': 'Generic', 'name': 'M82 Spacer 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 39, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M84_Spacer_3mm': {'brand': 'Generic', 'name': 'M84 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 16, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M84_Spacer_4mm': {'brand': 'Generic', 'name': 'M84 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 17, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M84_Spacer_6mm': {'brand': 'Generic', 'name': 'M84 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 18, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M84_Spacer_7mm': {'brand': 'Generic', 'name': 'M84 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 19, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M84_Spacer_8mm': {'brand': 'Generic', 'name': 'M84 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 20, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M84_Spacer_12mm': {'brand': 'Generic', 'name': 'M84 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 23, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M84_Spacer_25mm': {'brand': 'Generic', 'name': 'M84 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 34, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M84_Spacer_30mm': {'brand': 'Generic', 'name': 'M84 Spacer 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 38, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M92_Spacer_3mm': {'brand': 'Generic', 'name': 'M92 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 18, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M92_Spacer_4mm': {'brand': 'Generic', 'name': 'M92 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 19, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M92_Spacer_6mm': {'brand': 'Generic', 'name': 'M92 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 20, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M92_Spacer_7mm': {'brand': 'Generic', 'name': 'M92 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 21, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M92_Spacer_8mm': {'brand': 'Generic', 'name': 'M92 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 22, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M92_Spacer_12mm': {'brand': 'Generic', 'name': 'M92 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 25, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M92_Spacer_20mm': {'brand': 'Generic', 'name': 'M92 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 32, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M92_Spacer_25mm': {'brand': 'Generic', 'name': 'M92 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 36, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M92_Spacer_30mm': {'brand': 'Generic', 'name': 'M92 Spacer 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 40, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M117_Spacer_3mm': {'brand': 'Generic', 'name': 'M117 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 24, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M117_Spacer_4mm': {'brand': 'Generic', 'name': 'M117 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 25, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M117_Spacer_7mm': {'brand': 'Generic', 'name': 'M117 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 27, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M117_Spacer_8mm': {'brand': 'Generic', 'name': 'M117 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 28, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M117_Spacer_12mm': {'brand': 'Generic', 'name': 'M117 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 31, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M117_Spacer_15mm': {'brand': 'Generic', 'name': 'M117 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 34, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M117_Spacer_25mm': {'brand': 'Generic', 'name': 'M117 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 42, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M117_Spacer_40mm': {'brand': 'Generic', 'name': 'M117 Spacer 40mm', 'type': 'type_adapter', 'optical_length': 40, 'mass': 54, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_2_1mm': {'brand': 'Generic', 'name': 'M42 Spacer 2.1mm', 'type': 'type_adapter', 'optical_length': 2.1, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_2_3mm': {'brand': 'Generic', 'name': 'M42 Spacer 2.3mm', 'type': 'type_adapter', 'optical_length': 2.3, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_2_7mm': {'brand': 'Generic', 'name': 'M42 Spacer 2.7mm', 'type': 'type_adapter', 'optical_length': 2.7, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_3_2mm': {'brand': 'Generic', 'name': 'M42 Spacer 3.2mm', 'type': 'type_adapter', 'optical_length': 3.2, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_3_5mm': {'brand': 'Generic', 'name': 'M42 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_4_5mm': {'brand': 'Generic', 'name': 'M42 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 7, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_5_5mm': {'brand': 'Generic', 'name': 'M42 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 8, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_6_5mm': {'brand': 'Generic', 'name': 'M42 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 9, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_8_5mm': {'brand': 'Generic', 'name': 'M42 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 10, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_9_5mm': {'brand': 'Generic', 'name': 'M42 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 11, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_11mm': {'brand': 'Generic', 'name': 'M42 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 12, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_13mm': {'brand': 'Generic', 'name': 'M42 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 14, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_16mm': {'brand': 'Generic', 'name': 'M42 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_18mm': {'brand': 'Generic', 'name': 'M42 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 18, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_19mm': {'brand': 'Generic', 'name': 'M42 Spacer 19mm', 'type': 'type_adapter', 'optical_length': 19, 'mass': 19, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_21mm': {'brand': 'Generic', 'name': 'M42 Spacer 21mm', 'type': 'type_adapter', 'optical_length': 21, 'mass': 20, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_23mm': {'brand': 'Generic', 'name': 'M42 Spacer 23mm', 'type': 'type_adapter', 'optical_length': 23, 'mass': 22, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_24mm': {'brand': 'Generic', 'name': 'M42 Spacer 24mm', 'type': 'type_adapter', 'optical_length': 24, 'mass': 23, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_26mm': {'brand': 'Generic', 'name': 'M42 Spacer 26mm', 'type': 'type_adapter', 'optical_length': 26, 'mass': 24, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_27mm': {'brand': 'Generic', 'name': 'M42 Spacer 27mm', 'type': 'type_adapter', 'optical_length': 27, 'mass': 25, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_29mm': {'brand': 'Generic', 'name': 'M42 Spacer 29mm', 'type': 'type_adapter', 'optical_length': 29, 'mass': 27, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_32mm': {'brand': 'Generic', 'name': 'M42 Spacer 32mm', 'type': 'type_adapter', 'optical_length': 32, 'mass': 29, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_33mm': {'brand': 'Generic', 'name': 'M42 Spacer 33mm', 'type': 'type_adapter', 'optical_length': 33, 'mass': 30, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_36mm': {'brand': 'Generic', 'name': 'M42 Spacer 36mm', 'type': 'type_adapter', 'optical_length': 36, 'mass': 32, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_37mm': {'brand': 'Generic', 'name': 'M42 Spacer 37mm', 'type': 'type_adapter', 'optical_length': 37, 'mass': 33, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_38mm': {'brand': 'Generic', 'name': 'M42 Spacer 38mm', 'type': 'type_adapter', 'optical_length': 38, 'mass': 34, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_42mm': {'brand': 'Generic', 'name': 'M42 Spacer 42mm', 'type': 'type_adapter', 'optical_length': 42, 'mass': 37, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_44mm': {'brand': 'Generic', 'name': 'M42 Spacer 44mm', 'type': 'type_adapter', 'optical_length': 44, 'mass': 39, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_46mm': {'brand': 'Generic', 'name': 'M42 Spacer 46mm', 'type': 'type_adapter', 'optical_length': 46, 'mass': 40, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_48mm': {'brand': 'Generic', 'name': 'M42 Spacer 48mm', 'type': 'type_adapter', 'optical_length': 48, 'mass': 42, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_2_1mm': {'brand': 'Generic', 'name': 'M48 Spacer 2.1mm', 'type': 'type_adapter', 'optical_length': 2.1, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_2_3mm': {'brand': 'Generic', 'name': 'M48 Spacer 2.3mm', 'type': 'type_adapter', 'optical_length': 2.3, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_2_7mm': {'brand': 'Generic', 'name': 'M48 Spacer 2.7mm', 'type': 'type_adapter', 'optical_length': 2.7, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_3_2mm': {'brand': 'Generic', 'name': 'M48 Spacer 3.2mm', 'type': 'type_adapter', 'optical_length': 3.2, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_3_5mm': {'brand': 'Generic', 'name': 'M48 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_4_5mm': {'brand': 'Generic', 'name': 'M48 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 9, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_5_5mm': {'brand': 'Generic', 'name': 'M48 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 10, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_6_5mm': {'brand': 'Generic', 'name': 'M48 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 11, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_8_5mm': {'brand': 'Generic', 'name': 'M48 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 12, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_9_5mm': {'brand': 'Generic', 'name': 'M48 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 13, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_11mm': {'brand': 'Generic', 'name': 'M48 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 14, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_13mm': {'brand': 'Generic', 'name': 'M48 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 16, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_16mm': {'brand': 'Generic', 'name': 'M48 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_18mm': {'brand': 'Generic', 'name': 'M48 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 20, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_19mm': {'brand': 'Generic', 'name': 'M48 Spacer 19mm', 'type': 'type_adapter', 'optical_length': 19, 'mass': 21, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_21mm': {'brand': 'Generic', 'name': 'M48 Spacer 21mm', 'type': 'type_adapter', 'optical_length': 21, 'mass': 22, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_23mm': {'brand': 'Generic', 'name': 'M48 Spacer 23mm', 'type': 'type_adapter', 'optical_length': 23, 'mass': 24, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_24mm': {'brand': 'Generic', 'name': 'M48 Spacer 24mm', 'type': 'type_adapter', 'optical_length': 24, 'mass': 25, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_26mm': {'brand': 'Generic', 'name': 'M48 Spacer 26mm', 'type': 'type_adapter', 'optical_length': 26, 'mass': 26, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_27mm': {'brand': 'Generic', 'name': 'M48 Spacer 27mm', 'type': 'type_adapter', 'optical_length': 27, 'mass': 27, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_29mm': {'brand': 'Generic', 'name': 'M48 Spacer 29mm', 'type': 'type_adapter', 'optical_length': 29, 'mass': 29, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_32mm': {'brand': 'Generic', 'name': 'M48 Spacer 32mm', 'type': 'type_adapter', 'optical_length': 32, 'mass': 31, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_33mm': {'brand': 'Generic', 'name': 'M48 Spacer 33mm', 'type': 'type_adapter', 'optical_length': 33, 'mass': 32, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_36mm': {'brand': 'Generic', 'name': 'M48 Spacer 36mm', 'type': 'type_adapter', 'optical_length': 36, 'mass': 34, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_37mm': {'brand': 'Generic', 'name': 'M48 Spacer 37mm', 'type': 'type_adapter', 'optical_length': 37, 'mass': 35, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_38mm': {'brand': 'Generic', 'name': 'M48 Spacer 38mm', 'type': 'type_adapter', 'optical_length': 38, 'mass': 36, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_42mm': {'brand': 'Generic', 'name': 'M48 Spacer 42mm', 'type': 'type_adapter', 'optical_length': 42, 'mass': 39, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_44mm': {'brand': 'Generic', 'name': 'M48 Spacer 44mm', 'type': 'type_adapter', 'optical_length': 44, 'mass': 41, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_46mm': {'brand': 'Generic', 'name': 'M48 Spacer 46mm', 'type': 'type_adapter', 'optical_length': 46, 'mass': 42, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_48mm': {'brand': 'Generic', 'name': 'M48 Spacer 48mm', 'type': 'type_adapter', 'optical_length': 48, 'mass': 44, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_2_1mm': {'brand': 'Generic', 'name': 'M54 Spacer 2.1mm', 'type': 'type_adapter', 'optical_length': 2.1, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_2_3mm': {'brand': 'Generic', 'name': 'M54 Spacer 2.3mm', 'type': 'type_adapter', 'optical_length': 2.3, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_2_7mm': {'brand': 'Generic', 'name': 'M54 Spacer 2.7mm', 'type': 'type_adapter', 'optical_length': 2.7, 'mass': 10, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_3_2mm': {'brand': 'Generic', 'name': 'M54 Spacer 3.2mm', 'type': 'type_adapter', 'optical_length': 3.2, 'mass': 10, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_3_5mm': {'brand': 'Generic', 'name': 'M54 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 10, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_4_5mm': {'brand': 'Generic', 'name': 'M54 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 11, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_5_5mm': {'brand': 'Generic', 'name': 'M54 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 12, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_6_5mm': {'brand': 'Generic', 'name': 'M54 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 13, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_7_5mm': {'brand': 'Generic', 'name': 'M54 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 14, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_8_5mm': {'brand': 'Generic', 'name': 'M54 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 14, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_9_5mm': {'brand': 'Generic', 'name': 'M54 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 15, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_11mm': {'brand': 'Generic', 'name': 'M54 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 16, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_13mm': {'brand': 'Generic', 'name': 'M54 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 18, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_16mm': {'brand': 'Generic', 'name': 'M54 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 20, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_18mm': {'brand': 'Generic', 'name': 'M54 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 22, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_19mm': {'brand': 'Generic', 'name': 'M54 Spacer 19mm', 'type': 'type_adapter', 'optical_length': 19, 'mass': 23, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_21mm': {'brand': 'Generic', 'name': 'M54 Spacer 21mm', 'type': 'type_adapter', 'optical_length': 21, 'mass': 24, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_23mm': {'brand': 'Generic', 'name': 'M54 Spacer 23mm', 'type': 'type_adapter', 'optical_length': 23, 'mass': 26, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_24mm': {'brand': 'Generic', 'name': 'M54 Spacer 24mm', 'type': 'type_adapter', 'optical_length': 24, 'mass': 27, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_26mm': {'brand': 'Generic', 'name': 'M54 Spacer 26mm', 'type': 'type_adapter', 'optical_length': 26, 'mass': 28, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_27mm': {'brand': 'Generic', 'name': 'M54 Spacer 27mm', 'type': 'type_adapter', 'optical_length': 27, 'mass': 29, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_2_1mm': {'brand': 'Generic', 'name': 'M68 Spacer 2.1mm', 'type': 'type_adapter', 'optical_length': 2.1, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_2_3mm': {'brand': 'Generic', 'name': 'M68 Spacer 2.3mm', 'type': 'type_adapter', 'optical_length': 2.3, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_2_7mm': {'brand': 'Generic', 'name': 'M68 Spacer 2.7mm', 'type': 'type_adapter', 'optical_length': 2.7, 'mass': 12, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_3_5mm': {'brand': 'Generic', 'name': 'M68 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 12, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_4_5mm': {'brand': 'Generic', 'name': 'M68 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 13, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_5_5mm': {'brand': 'Generic', 'name': 'M68 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 14, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_6_5mm': {'brand': 'Generic', 'name': 'M68 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 15, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_7_5mm': {'brand': 'Generic', 'name': 'M68 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 16, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_8_5mm': {'brand': 'Generic', 'name': 'M68 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 16, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_9_5mm': {'brand': 'Generic', 'name': 'M68 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 17, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_11mm': {'brand': 'Generic', 'name': 'M68 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 18, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_13mm': {'brand': 'Generic', 'name': 'M68 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 20, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_16mm': {'brand': 'Generic', 'name': 'M68 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 22, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_18mm': {'brand': 'Generic', 'name': 'M68 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 24, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_19mm': {'brand': 'Generic', 'name': 'M68 Spacer 19mm', 'type': 'type_adapter', 'optical_length': 19, 'mass': 25, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_21mm': {'brand': 'Generic', 'name': 'M68 Spacer 21mm', 'type': 'type_adapter', 'optical_length': 21, 'mass': 26, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_23mm': {'brand': 'Generic', 'name': 'M68 Spacer 23mm', 'type': 'type_adapter', 'optical_length': 23, 'mass': 28, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_24mm': {'brand': 'Generic', 'name': 'M68 Spacer 24mm', 'type': 'type_adapter', 'optical_length': 24, 'mass': 29, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_26mm': {'brand': 'Generic', 'name': 'M68 Spacer 26mm', 'type': 'type_adapter', 'optical_length': 26, 'mass': 30, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_27mm': {'brand': 'Generic', 'name': 'M68 Spacer 27mm', 'type': 'type_adapter', 'optical_length': 27, 'mass': 31, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Extension_Tube_6mm': {'brand': 'Generic', 'name': 'M42 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 13, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M42_Extension_Tube_9mm': {'brand': 'Generic', 'name': 'M42 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 14, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M42_Extension_Tube_11mm': {'brand': 'Generic', 'name': 'M42 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 15, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M42_Extension_Tube_13mm': {'brand': 'Generic', 'name': 'M42 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 15, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M42_Extension_Tube_14mm': {'brand': 'Generic', 'name': 'M42 Extension Tube 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M42_Extension_Tube_16mm': {'brand': 'Generic', 'name': 'M42 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M42_Extension_Tube_17mm': {'brand': 'Generic', 'name': 'M42 Extension Tube 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 17, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M42_Extension_Tube_18mm': {'brand': 'Generic', 'name': 'M42 Extension Tube 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 17, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M42_Extension_Tube_22mm': {'brand': 'Generic', 'name': 'M42 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 18, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M42_Extension_Tube_28mm': {'brand': 'Generic', 'name': 'M42 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 20, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M42_Extension_Tube_55mm': {'brand': 'Generic', 'name': 'M42 Extension Tube 55mm', 'type': 'type_adapter', 'optical_length': 55, 'mass': 28, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M42_Extension_Tube_75mm': {'brand': 'Generic', 'name': 'M42 Extension Tube 75mm', 'type': 'type_adapter', 'optical_length': 75, 'mass': 34, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M42_Extension_Tube_100mm': {'brand': 'Generic', 'name': 'M42 Extension Tube 100mm', 'type': 'type_adapter', 'optical_length': 100, 'mass': 42, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M48_Extension_Tube_6mm': {'brand': 'Generic', 'name': 'M48 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 17, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M48_Extension_Tube_9mm': {'brand': 'Generic', 'name': 'M48 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M48_Extension_Tube_11mm': {'brand': 'Generic', 'name': 'M48 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 19, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M48_Extension_Tube_13mm': {'brand': 'Generic', 'name': 'M48 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 19, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M48_Extension_Tube_14mm': {'brand': 'Generic', 'name': 'M48 Extension Tube 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 20, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M48_Extension_Tube_16mm': {'brand': 'Generic', 'name': 'M48 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 20, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M48_Extension_Tube_17mm': {'brand': 'Generic', 'name': 'M48 Extension Tube 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 21, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M48_Extension_Tube_18mm': {'brand': 'Generic', 'name': 'M48 Extension Tube 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 21, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M48_Extension_Tube_22mm': {'brand': 'Generic', 'name': 'M48 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 22, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M48_Extension_Tube_28mm': {'brand': 'Generic', 'name': 'M48 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 24, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M48_Extension_Tube_55mm': {'brand': 'Generic', 'name': 'M48 Extension Tube 55mm', 'type': 'type_adapter', 'optical_length': 55, 'mass': 32, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M48_Extension_Tube_75mm': {'brand': 'Generic', 'name': 'M48 Extension Tube 75mm', 'type': 'type_adapter', 'optical_length': 75, 'mass': 38, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M48_Extension_Tube_100mm': {'brand': 'Generic', 'name': 'M48 Extension Tube 100mm', 'type': 'type_adapter', 'optical_length': 100, 'mass': 46, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M54_Extension_Tube_6mm': {'brand': 'Generic', 'name': 'M54 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 21, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M54_Extension_Tube_9mm': {'brand': 'Generic', 'name': 'M54 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 22, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M54_Extension_Tube_11mm': {'brand': 'Generic', 'name': 'M54 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 23, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M54_Extension_Tube_13mm': {'brand': 'Generic', 'name': 'M54 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 23, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M54_Extension_Tube_14mm': {'brand': 'Generic', 'name': 'M54 Extension Tube 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 24, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M54_Extension_Tube_16mm': {'brand': 'Generic', 'name': 'M54 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 24, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M54_Extension_Tube_17mm': {'brand': 'Generic', 'name': 'M54 Extension Tube 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 25, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M54_Extension_Tube_18mm': {'brand': 'Generic', 'name': 'M54 Extension Tube 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 25, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M54_Extension_Tube_22mm': {'brand': 'Generic', 'name': 'M54 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 26, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M54_Extension_Tube_28mm': {'brand': 'Generic', 'name': 'M54 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 28, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M54_Extension_Tube_55mm': {'brand': 'Generic', 'name': 'M54 Extension Tube 55mm', 'type': 'type_adapter', 'optical_length': 55, 'mass': 36, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M54_Extension_Tube_75mm': {'brand': 'Generic', 'name': 'M54 Extension Tube 75mm', 'type': 'type_adapter', 'optical_length': 75, 'mass': 42, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M54_Extension_Tube_100mm': {'brand': 'Generic', 'name': 'M54 Extension Tube 100mm', 'type': 'type_adapter', 'optical_length': 100, 'mass': 50, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M68_Extension_Tube_6mm': {'brand': 'Generic', 'name': 'M68 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 26, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M68_Extension_Tube_9mm': {'brand': 'Generic', 'name': 'M68 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 27, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M68_Extension_Tube_11mm': {'brand': 'Generic', 'name': 'M68 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 28, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M68_Extension_Tube_13mm': {'brand': 'Generic', 'name': 'M68 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 28, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M68_Extension_Tube_14mm': {'brand': 'Generic', 'name': 'M68 Extension Tube 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 29, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M68_Extension_Tube_16mm': {'brand': 'Generic', 'name': 'M68 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 29, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M68_Extension_Tube_17mm': {'brand': 'Generic', 'name': 'M68 Extension Tube 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 30, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M68_Extension_Tube_18mm': {'brand': 'Generic', 'name': 'M68 Extension Tube 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 30, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M68_Extension_Tube_22mm': {'brand': 'Generic', 'name': 'M68 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 31, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M68_Extension_Tube_28mm': {'brand': 'Generic', 'name': 'M68 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 33, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M68_Extension_Tube_55mm': {'brand': 'Generic', 'name': 'M68 Extension Tube 55mm', 'type': 'type_adapter', 'optical_length': 55, 'mass': 41, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M68_Extension_Tube_75mm': {'brand': 'Generic', 'name': 'M68 Extension Tube 75mm', 'type': 'type_adapter', 'optical_length': 75, 'mass': 47, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M68_Extension_Tube_100mm': {'brand': 'Generic', 'name': 'M68 Extension Tube 100mm', 'type': 'type_adapter', 'optical_length': 100, 'mass': 55, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M72_Extension_Tube_3mm': {'brand': 'Generic', 'name': 'M72 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 30, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M72_Extension_Tube_6mm': {'brand': 'Generic', 'name': 'M72 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 31, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M72_Extension_Tube_7mm': {'brand': 'Generic', 'name': 'M72 Extension Tube 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 32, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M72_Extension_Tube_8mm': {'brand': 'Generic', 'name': 'M72 Extension Tube 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 32, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M72_Extension_Tube_9mm': {'brand': 'Generic', 'name': 'M72 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 32, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M72_Extension_Tube_11mm': {'brand': 'Generic', 'name': 'M72 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 33, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M72_Extension_Tube_12mm': {'brand': 'Generic', 'name': 'M72 Extension Tube 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 33, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M72_Extension_Tube_13mm': {'brand': 'Generic', 'name': 'M72 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 33, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M72_Extension_Tube_14mm': {'brand': 'Generic', 'name': 'M72 Extension Tube 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 34, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M72_Extension_Tube_16mm': {'brand': 'Generic', 'name': 'M72 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 34, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M72_Extension_Tube_17mm': {'brand': 'Generic', 'name': 'M72 Extension Tube 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 35, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M72_Extension_Tube_18mm': {'brand': 'Generic', 'name': 'M72 Extension Tube 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 35, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M72_Extension_Tube_22mm': {'brand': 'Generic', 'name': 'M72 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 36, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M72_Extension_Tube_28mm': {'brand': 'Generic', 'name': 'M72 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 38, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M72_Extension_Tube_35mm': {'brand': 'Generic', 'name': 'M72 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 40, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M72_Extension_Tube_45mm': {'brand': 'Generic', 'name': 'M72 Extension Tube 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 43, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M72_Extension_Tube_55mm': {'brand': 'Generic', 'name': 'M72 Extension Tube 55mm', 'type': 'type_adapter', 'optical_length': 55, 'mass': 46, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M72_Extension_Tube_60mm': {'brand': 'Generic', 'name': 'M72 Extension Tube 60mm', 'type': 'type_adapter', 'optical_length': 60, 'mass': 48, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M72_Extension_Tube_75mm': {'brand': 'Generic', 'name': 'M72 Extension Tube 75mm', 'type': 'type_adapter', 'optical_length': 75, 'mass': 52, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M72_Extension_Tube_100mm': {'brand': 'Generic', 'name': 'M72 Extension Tube 100mm', 'type': 'type_adapter', 'optical_length': 100, 'mass': 60, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M82_Extension_Tube_3mm': {'brand': 'Generic', 'name': 'M82 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 35, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M82_Extension_Tube_6mm': {'brand': 'Generic', 'name': 'M82 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 36, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M82_Extension_Tube_7mm': {'brand': 'Generic', 'name': 'M82 Extension Tube 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 37, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M82_Extension_Tube_8mm': {'brand': 'Generic', 'name': 'M82 Extension Tube 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 37, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M82_Extension_Tube_9mm': {'brand': 'Generic', 'name': 'M82 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 37, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M82_Extension_Tube_11mm': {'brand': 'Generic', 'name': 'M82 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 38, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M82_Extension_Tube_12mm': {'brand': 'Generic', 'name': 'M82 Extension Tube 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 38, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M82_Extension_Tube_13mm': {'brand': 'Generic', 'name': 'M82 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 38, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M82_Extension_Tube_14mm': {'brand': 'Generic', 'name': 'M82 Extension Tube 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 39, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M82_Extension_Tube_16mm': {'brand': 'Generic', 'name': 'M82 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 39, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M82_Extension_Tube_17mm': {'brand': 'Generic', 'name': 'M82 Extension Tube 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 40, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M82_Extension_Tube_18mm': {'brand': 'Generic', 'name': 'M82 Extension Tube 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 40, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M82_Extension_Tube_22mm': {'brand': 'Generic', 'name': 'M82 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 41, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M82_Extension_Tube_28mm': {'brand': 'Generic', 'name': 'M82 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 43, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M82_Extension_Tube_35mm': {'brand': 'Generic', 'name': 'M82 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 45, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M82_Extension_Tube_45mm': {'brand': 'Generic', 'name': 'M82 Extension Tube 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 48, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M82_Extension_Tube_55mm': {'brand': 'Generic', 'name': 'M82 Extension Tube 55mm', 'type': 'type_adapter', 'optical_length': 55, 'mass': 51, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M82_Extension_Tube_60mm': {'brand': 'Generic', 'name': 'M82 Extension Tube 60mm', 'type': 'type_adapter', 'optical_length': 60, 'mass': 53, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M82_Extension_Tube_75mm': {'brand': 'Generic', 'name': 'M82 Extension Tube 75mm', 'type': 'type_adapter', 'optical_length': 75, 'mass': 57, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M82_Extension_Tube_100mm': {'brand': 'Generic', 'name': 'M82 Extension Tube 100mm', 'type': 'type_adapter', 'optical_length': 100, 'mass': 65, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M84_Extension_Tube_3mm': {'brand': 'Generic', 'name': 'M84 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 38, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M84_Extension_Tube_6mm': {'brand': 'Generic', 'name': 'M84 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 39, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M84_Extension_Tube_7mm': {'brand': 'Generic', 'name': 'M84 Extension Tube 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 40, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M84_Extension_Tube_8mm': {'brand': 'Generic', 'name': 'M84 Extension Tube 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 40, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M84_Extension_Tube_9mm': {'brand': 'Generic', 'name': 'M84 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 40, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M84_Extension_Tube_11mm': {'brand': 'Generic', 'name': 'M84 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 41, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M84_Extension_Tube_12mm': {'brand': 'Generic', 'name': 'M84 Extension Tube 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 41, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M84_Extension_Tube_13mm': {'brand': 'Generic', 'name': 'M84 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 41, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M84_Extension_Tube_14mm': {'brand': 'Generic', 'name': 'M84 Extension Tube 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 42, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M84_Extension_Tube_16mm': {'brand': 'Generic', 'name': 'M84 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 42, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M84_Extension_Tube_17mm': {'brand': 'Generic', 'name': 'M84 Extension Tube 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 43, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M84_Extension_Tube_18mm': {'brand': 'Generic', 'name': 'M84 Extension Tube 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 43, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M84_Extension_Tube_22mm': {'brand': 'Generic', 'name': 'M84 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 44, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M84_Extension_Tube_28mm': {'brand': 'Generic', 'name': 'M84 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 46, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M84_Extension_Tube_35mm': {'brand': 'Generic', 'name': 'M84 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 48, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M84_Extension_Tube_45mm': {'brand': 'Generic', 'name': 'M84 Extension Tube 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 51, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M84_Extension_Tube_55mm': {'brand': 'Generic', 'name': 'M84 Extension Tube 55mm', 'type': 'type_adapter', 'optical_length': 55, 'mass': 54, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M84_Extension_Tube_60mm': {'brand': 'Generic', 'name': 'M84 Extension Tube 60mm', 'type': 'type_adapter', 'optical_length': 60, 'mass': 56, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M84_Extension_Tube_75mm': {'brand': 'Generic', 'name': 'M84 Extension Tube 75mm', 'type': 'type_adapter', 'optical_length': 75, 'mass': 60, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M84_Extension_Tube_100mm': {'brand': 'Generic', 'name': 'M84 Extension Tube 100mm', 'type': 'type_adapter', 'optical_length': 100, 'mass': 68, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M92_Extension_Tube_3mm': {'brand': 'Generic', 'name': 'M92 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 42, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M92_Extension_Tube_6mm': {'brand': 'Generic', 'name': 'M92 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 43, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M92_Extension_Tube_7mm': {'brand': 'Generic', 'name': 'M92 Extension Tube 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 44, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M92_Extension_Tube_8mm': {'brand': 'Generic', 'name': 'M92 Extension Tube 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 44, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M92_Extension_Tube_9mm': {'brand': 'Generic', 'name': 'M92 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 44, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M92_Extension_Tube_11mm': {'brand': 'Generic', 'name': 'M92 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 45, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M92_Extension_Tube_12mm': {'brand': 'Generic', 'name': 'M92 Extension Tube 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 45, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M92_Extension_Tube_13mm': {'brand': 'Generic', 'name': 'M92 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 45, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M92_Extension_Tube_14mm': {'brand': 'Generic', 'name': 'M92 Extension Tube 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 46, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M92_Extension_Tube_16mm': {'brand': 'Generic', 'name': 'M92 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 46, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M92_Extension_Tube_17mm': {'brand': 'Generic', 'name': 'M92 Extension Tube 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 47, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M92_Extension_Tube_18mm': {'brand': 'Generic', 'name': 'M92 Extension Tube 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 47, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M92_Extension_Tube_22mm': {'brand': 'Generic', 'name': 'M92 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 48, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M92_Extension_Tube_28mm': {'brand': 'Generic', 'name': 'M92 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 50, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M92_Extension_Tube_35mm': {'brand': 'Generic', 'name': 'M92 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 52, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M92_Extension_Tube_45mm': {'brand': 'Generic', 'name': 'M92 Extension Tube 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 55, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M92_Extension_Tube_55mm': {'brand': 'Generic', 'name': 'M92 Extension Tube 55mm', 'type': 'type_adapter', 'optical_length': 55, 'mass': 58, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M92_Extension_Tube_60mm': {'brand': 'Generic', 'name': 'M92 Extension Tube 60mm', 'type': 'type_adapter', 'optical_length': 60, 'mass': 60, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M92_Extension_Tube_75mm': {'brand': 'Generic', 'name': 'M92 Extension Tube 75mm', 'type': 'type_adapter', 'optical_length': 75, 'mass': 64, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M92_Extension_Tube_100mm': {'brand': 'Generic', 'name': 'M92 Extension Tube 100mm', 'type': 'type_adapter', 'optical_length': 100, 'mass': 72, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M56_Spacer_2_5mm': {'brand': 'Generic', 'name': 'M56 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 10, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M56_Spacer_3mm': {'brand': 'Generic', 'name': 'M56 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 10, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M56_Spacer_3_5mm': {'brand': 'Generic', 'name': 'M56 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 10, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M56_Spacer_4mm': {'brand': 'Generic', 'name': 'M56 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 11, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M56_Spacer_4_5mm': {'brand': 'Generic', 'name': 'M56 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 11, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M56_Spacer_5_5mm': {'brand': 'Generic', 'name': 'M56 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 12, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M56_Spacer_6mm': {'brand': 'Generic', 'name': 'M56 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 12, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M56_Spacer_6_5mm': {'brand': 'Generic', 'name': 'M56 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 13, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M56_Spacer_7mm': {'brand': 'Generic', 'name': 'M56 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 13, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M56_Spacer_7_5mm': {'brand': 'Generic', 'name': 'M56 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 14, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M56_Spacer_8mm': {'brand': 'Generic', 'name': 'M56 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 14, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M56_Spacer_8_5mm': {'brand': 'Generic', 'name': 'M56 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 14, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M56_Spacer_9mm': {'brand': 'Generic', 'name': 'M56 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 15, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M56_Spacer_9_5mm': {'brand': 'Generic', 'name': 'M56 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 15, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M56_Spacer_11mm': {'brand': 'Generic', 'name': 'M56 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 16, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M56_Spacer_12mm': {'brand': 'Generic', 'name': 'M56 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 17, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M56_Spacer_13mm': {'brand': 'Generic', 'name': 'M56 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 18, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M56_Spacer_14mm': {'brand': 'Generic', 'name': 'M56 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 19, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M56_Spacer_16mm': {'brand': 'Generic', 'name': 'M56 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 20, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M56_Spacer_17mm': {'brand': 'Generic', 'name': 'M56 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 21, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M56_Spacer_18mm': {'brand': 'Generic', 'name': 'M56 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 22, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M56_Spacer_22mm': {'brand': 'Generic', 'name': 'M56 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 25, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M56_Spacer_25mm': {'brand': 'Generic', 'name': 'M56 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 28, 'tside_thread': 'M56', 'tside_gender': 'Female', 'cside_thread': 'M56', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M63_Spacer_2_5mm': {'brand': 'Generic', 'name': 'M63 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 12, 'tside_thread': 'M63', 'tside_gender': 'Female', 'cside_thread': 'M63', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M63_Spacer_3mm': {'brand': 'Generic', 'name': 'M63 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 12, 'tside_thread': 'M63', 'tside_gender': 'Female', 'cside_thread': 'M63', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M63_Spacer_3_5mm': {'brand': 'Generic', 'name': 'M63 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 12, 'tside_thread': 'M63', 'tside_gender': 'Female', 'cside_thread': 'M63', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M63_Spacer_4mm': {'brand': 'Generic', 'name': 'M63 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 13, 'tside_thread': 'M63', 'tside_gender': 'Female', 'cside_thread': 'M63', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M63_Spacer_4_5mm': {'brand': 'Generic', 'name': 'M63 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 13, 'tside_thread': 'M63', 'tside_gender': 'Female', 'cside_thread': 'M63', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M63_Spacer_5_5mm': {'brand': 'Generic', 'name': 'M63 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 14, 'tside_thread': 'M63', 'tside_gender': 'Female', 'cside_thread': 'M63', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M63_Spacer_6mm': {'brand': 'Generic', 'name': 'M63 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 14, 'tside_thread': 'M63', 'tside_gender': 'Female', 'cside_thread': 'M63', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M63_Spacer_6_5mm': {'brand': 'Generic', 'name': 'M63 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 15, 'tside_thread': 'M63', 'tside_gender': 'Female', 'cside_thread': 'M63', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M63_Spacer_7mm': {'brand': 'Generic', 'name': 'M63 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 15, 'tside_thread': 'M63', 'tside_gender': 'Female', 'cside_thread': 'M63', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M63_Spacer_7_5mm': {'brand': 'Generic', 'name': 'M63 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 16, 'tside_thread': 'M63', 'tside_gender': 'Female', 'cside_thread': 'M63', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M63_Spacer_8mm': {'brand': 'Generic', 'name': 'M63 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 16, 'tside_thread': 'M63', 'tside_gender': 'Female', 'cside_thread': 'M63', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M63_Spacer_8_5mm': {'brand': 'Generic', 'name': 'M63 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 16, 'tside_thread': 'M63', 'tside_gender': 'Female', 'cside_thread': 'M63', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M63_Spacer_9mm': {'brand': 'Generic', 'name': 'M63 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 17, 'tside_thread': 'M63', 'tside_gender': 'Female', 'cside_thread': 'M63', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M63_Spacer_9_5mm': {'brand': 'Generic', 'name': 'M63 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 17, 'tside_thread': 'M63', 'tside_gender': 'Female', 'cside_thread': 'M63', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M63_Spacer_11mm': {'brand': 'Generic', 'name': 'M63 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 18, 'tside_thread': 'M63', 'tside_gender': 'Female', 'cside_thread': 'M63', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M63_Spacer_12mm': {'brand': 'Generic', 'name': 'M63 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 19, 'tside_thread': 'M63', 'tside_gender': 'Female', 'cside_thread': 'M63', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M63_Spacer_13mm': {'brand': 'Generic', 'name': 'M63 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 20, 'tside_thread': 'M63', 'tside_gender': 'Female', 'cside_thread': 'M63', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M63_Spacer_14mm': {'brand': 'Generic', 'name': 'M63 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 21, 'tside_thread': 'M63', 'tside_gender': 'Female', 'cside_thread': 'M63', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M63_Spacer_16mm': {'brand': 'Generic', 'name': 'M63 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 22, 'tside_thread': 'M63', 'tside_gender': 'Female', 'cside_thread': 'M63', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M63_Spacer_17mm': {'brand': 'Generic', 'name': 'M63 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 23, 'tside_thread': 'M63', 'tside_gender': 'Female', 'cside_thread': 'M63', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M63_Spacer_18mm': {'brand': 'Generic', 'name': 'M63 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 24, 'tside_thread': 'M63', 'tside_gender': 'Female', 'cside_thread': 'M63', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M63_Spacer_22mm': {'brand': 'Generic', 'name': 'M63 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 27, 'tside_thread': 'M63', 'tside_gender': 'Female', 'cside_thread': 'M63', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M63_Spacer_25mm': {'brand': 'Generic', 'name': 'M63 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 30, 'tside_thread': 'M63', 'tside_gender': 'Female', 'cside_thread': 'M63', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_SC_Schmidt_Cassegrain_Spacer_2_5mm': {'brand': 'Generic', 'name': 'SC (Schmidt-Cassegrain) Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 22, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_SC_Schmidt_Cassegrain_Spacer_3_5mm': {'brand': 'Generic', 'name': 'SC (Schmidt-Cassegrain) Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 22, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_SC_Schmidt_Cassegrain_Spacer_4_5mm': {'brand': 'Generic', 'name': 'SC (Schmidt-Cassegrain) Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 23, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_SC_Schmidt_Cassegrain_Spacer_5_5mm': {'brand': 'Generic', 'name': 'SC (Schmidt-Cassegrain) Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 24, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_SC_Schmidt_Cassegrain_Spacer_6mm': {'brand': 'Generic', 'name': 'SC (Schmidt-Cassegrain) Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 24, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_SC_Schmidt_Cassegrain_Spacer_6_5mm': {'brand': 'Generic', 'name': 'SC (Schmidt-Cassegrain) Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 25, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_SC_Schmidt_Cassegrain_Spacer_7_5mm': {'brand': 'Generic', 'name': 'SC (Schmidt-Cassegrain) Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 26, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_SC_Schmidt_Cassegrain_Spacer_8mm': {'brand': 'Generic', 'name': 'SC (Schmidt-Cassegrain) Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 26, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_SC_Schmidt_Cassegrain_Spacer_8_5mm': {'brand': 'Generic', 'name': 'SC (Schmidt-Cassegrain) Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 26, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_SC_Schmidt_Cassegrain_Spacer_9mm': {'brand': 'Generic', 'name': 'SC (Schmidt-Cassegrain) Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 27, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_SC_Schmidt_Cassegrain_Spacer_9_5mm': {'brand': 'Generic', 'name': 'SC (Schmidt-Cassegrain) Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 27, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_SC_Schmidt_Cassegrain_Spacer_11mm': {'brand': 'Generic', 'name': 'SC (Schmidt-Cassegrain) Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 28, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_SC_Schmidt_Cassegrain_Spacer_12mm': {'brand': 'Generic', 'name': 'SC (Schmidt-Cassegrain) Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 29, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_SC_Schmidt_Cassegrain_Spacer_13mm': {'brand': 'Generic', 'name': 'SC (Schmidt-Cassegrain) Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 30, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_SC_Schmidt_Cassegrain_Spacer_14mm': {'brand': 'Generic', 'name': 'SC (Schmidt-Cassegrain) Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 31, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_SC_Schmidt_Cassegrain_Spacer_16mm': {'brand': 'Generic', 'name': 'SC (Schmidt-Cassegrain) Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 32, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_SC_Schmidt_Cassegrain_Spacer_17mm': {'brand': 'Generic', 'name': 'SC (Schmidt-Cassegrain) Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 33, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_SC_Schmidt_Cassegrain_Spacer_18mm': {'brand': 'Generic', 'name': 'SC (Schmidt-Cassegrain) Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 34, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_SC_Schmidt_Cassegrain_Spacer_22mm': {'brand': 'Generic', 'name': 'SC (Schmidt-Cassegrain) Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 37, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_SC_Schmidt_Cassegrain_Spacer_28mm': {'brand': 'Generic', 'name': 'SC (Schmidt-Cassegrain) Spacer 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 42, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_SC_Schmidt_Cassegrain_Spacer_35mm': {'brand': 'Generic', 'name': 'SC (Schmidt-Cassegrain) Spacer 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 48, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_SC_Schmidt_Cassegrain_Spacer_45mm': {'brand': 'Generic', 'name': 'SC (Schmidt-Cassegrain) Spacer 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 56, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_SC_Schmidt_Cassegrain_Spacer_55mm': {'brand': 'Generic', 'name': 'SC (Schmidt-Cassegrain) Spacer 55mm', 'type': 'type_adapter', 'optical_length': 55, 'mass': 64, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_SC_Schmidt_Cassegrain_Spacer_60mm': {'brand': 'Generic', 'name': 'SC (Schmidt-Cassegrain) Spacer 60mm', 'type': 'type_adapter', 'optical_length': 60, 'mass': 68, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_1_25_Spacer_2_5mm': {'brand': 'Generic', 'name': '1.25" Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 5, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_1_25_Spacer_3mm': {'brand': 'Generic', 'name': '1.25" Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 5, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_1_25_Spacer_3_5mm': {'brand': 'Generic', 'name': '1.25" Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 5, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_1_25_Spacer_4mm': {'brand': 'Generic', 'name': '1.25" Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 6, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_1_25_Spacer_4_5mm': {'brand': 'Generic', 'name': '1.25" Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 6, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_1_25_Spacer_5_5mm': {'brand': 'Generic', 'name': '1.25" Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 7, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_1_25_Spacer_6mm': {'brand': 'Generic', 'name': '1.25" Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 7, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_1_25_Spacer_6_5mm': {'brand': 'Generic', 'name': '1.25" Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 8, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_1_25_Spacer_7mm': {'brand': 'Generic', 'name': '1.25" Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 8, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_1_25_Spacer_7_5mm': {'brand': 'Generic', 'name': '1.25" Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 9, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_1_25_Spacer_8mm': {'brand': 'Generic', 'name': '1.25" Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 9, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_1_25_Spacer_8_5mm': {'brand': 'Generic', 'name': '1.25" Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 9, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_1_25_Spacer_9mm': {'brand': 'Generic', 'name': '1.25" Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 10, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_1_25_Spacer_9_5mm': {'brand': 'Generic', 'name': '1.25" Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 10, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_1_25_Spacer_11mm': {'brand': 'Generic', 'name': '1.25" Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 11, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_1_25_Spacer_12mm': {'brand': 'Generic', 'name': '1.25" Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 12, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_1_25_Spacer_13mm': {'brand': 'Generic', 'name': '1.25" Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 13, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_1_25_Spacer_14mm': {'brand': 'Generic', 'name': '1.25" Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 14, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_1_25_Spacer_16mm': {'brand': 'Generic', 'name': '1.25" Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 15, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_1_25_Spacer_17mm': {'brand': 'Generic', 'name': '1.25" Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 16, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_1_25_Spacer_18mm': {'brand': 'Generic', 'name': '1.25" Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 17, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_1_25_Spacer_22mm': {'brand': 'Generic', 'name': '1.25" Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 20, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_2_Spacer_2_5mm': {'brand': 'Generic', 'name': '2" Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 10, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_2_Spacer_3mm': {'brand': 'Generic', 'name': '2" Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 10, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_2_Spacer_3_5mm': {'brand': 'Generic', 'name': '2" Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 10, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_2_Spacer_4mm': {'brand': 'Generic', 'name': '2" Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 11, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_2_Spacer_4_5mm': {'brand': 'Generic', 'name': '2" Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 11, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_2_Spacer_5_5mm': {'brand': 'Generic', 'name': '2" Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 12, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_2_Spacer_6mm': {'brand': 'Generic', 'name': '2" Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 12, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_2_Spacer_6_5mm': {'brand': 'Generic', 'name': '2" Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 13, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_2_Spacer_7mm': {'brand': 'Generic', 'name': '2" Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 13, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_2_Spacer_7_5mm': {'brand': 'Generic', 'name': '2" Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 14, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_2_Spacer_8mm': {'brand': 'Generic', 'name': '2" Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 14, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_2_Spacer_8_5mm': {'brand': 'Generic', 'name': '2" Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 14, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_2_Spacer_9mm': {'brand': 'Generic', 'name': '2" Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 15, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_2_Spacer_9_5mm': {'brand': 'Generic', 'name': '2" Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 15, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_2_Spacer_11mm': {'brand': 'Generic', 'name': '2" Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 16, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_2_Spacer_12mm': {'brand': 'Generic', 'name': '2" Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 17, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_2_Spacer_13mm': {'brand': 'Generic', 'name': '2" Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 18, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_2_Spacer_14mm': {'brand': 'Generic', 'name': '2" Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 19, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_2_Spacer_16mm': {'brand': 'Generic', 'name': '2" Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 20, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_2_Spacer_17mm': {'brand': 'Generic', 'name': '2" Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 21, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_2_Spacer_18mm': {'brand': 'Generic', 'name': '2" Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 22, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_2_Spacer_22mm': {'brand': 'Generic', 'name': '2" Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 25, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M82_Extension_Tube_5mm': {'brand': 'Generic', 'name': 'M82 Extension Tube 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 19, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M82_Extension_Tube_10mm': {'brand': 'Generic', 'name': 'M82 Extension Tube 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 21, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M82_Extension_Tube_15mm': {'brand': 'Generic', 'name': 'M82 Extension Tube 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 22, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M82_Extension_Tube_20mm': {'brand': 'Generic', 'name': 'M82 Extension Tube 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 24, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M82_Extension_Tube_25mm': {'brand': 'Generic', 'name': 'M82 Extension Tube 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 25, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M82_Extension_Tube_30mm': {'brand': 'Generic', 'name': 'M82 Extension Tube 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 27, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_SC_Extension_Tube_5mm': {'brand': 'Generic', 'name': 'SC Extension Tube 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 19, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_SC_Extension_Tube_10mm': {'brand': 'Generic', 'name': 'SC Extension Tube 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 21, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_SC_Extension_Tube_15mm': {'brand': 'Generic', 'name': 'SC Extension Tube 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 22, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_SC_Extension_Tube_20mm': {'brand': 'Generic', 'name': 'SC Extension Tube 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 24, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_SC_Extension_Tube_25mm': {'brand': 'Generic', 'name': 'SC Extension Tube 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 25, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_SC_Extension_Tube_30mm': {'brand': 'Generic', 'name': 'SC Extension Tube 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 27, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_SC_Extension_Tube_35mm': {'brand': 'Generic', 'name': 'SC Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 28, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_SC_Extension_Tube_40mm': {'brand': 'Generic', 'name': 'SC Extension Tube 40mm', 'type': 'type_adapter', 'optical_length': 40, 'mass': 30, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_SC_Extension_Tube_50mm': {'brand': 'Generic', 'name': 'SC Extension Tube 50mm', 'type': 'type_adapter', 'optical_length': 50, 'mass': 33, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_SC_Extension_Tube_60mm': {'brand': 'Generic', 'name': 'SC Extension Tube 60mm', 'type': 'type_adapter', 'optical_length': 60, 'mass': 36, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_SC_Extension_Tube_75mm': {'brand': 'Generic', 'name': 'SC Extension Tube 75mm', 'type': 'type_adapter', 'optical_length': 75, 'mass': 40, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Generic_M92_Spacer_2_5mm': {'brand': 'Generic', 'name': 'M92 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 18, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M92_Spacer_3_5mm': {'brand': 'Generic', 'name': 'M92 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 18, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M92_Spacer_4_5mm': {'brand': 'Generic', 'name': 'M92 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 19, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M92_Spacer_5_5mm': {'brand': 'Generic', 'name': 'M92 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 20, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M92_Spacer_6_5mm': {'brand': 'Generic', 'name': 'M92 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 21, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M92_Spacer_7_5mm': {'brand': 'Generic', 'name': 'M92 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 22, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M92_Spacer_8_5mm': {'brand': 'Generic', 'name': 'M92 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 22, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M92_Spacer_9_5mm': {'brand': 'Generic', 'name': 'M92 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 23, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M92_Spacer_11mm': {'brand': 'Generic', 'name': 'M92 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 24, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M92_Spacer_13mm': {'brand': 'Generic', 'name': 'M92 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 26, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M92_Spacer_14mm': {'brand': 'Generic', 'name': 'M92 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 27, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M92_Spacer_16mm': {'brand': 'Generic', 'name': 'M92 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 28, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M92_Spacer_17mm': {'brand': 'Generic', 'name': 'M92 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 29, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M92_Spacer_18mm': {'brand': 'Generic', 'name': 'M92 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 30, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M92_Spacer_22mm': {'brand': 'Generic', 'name': 'M92 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 33, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M92_Spacer_28mm': {'brand': 'Generic', 'name': 'M92 Spacer 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 38, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M92_Spacer_32mm': {'brand': 'Generic', 'name': 'M92 Spacer 32mm', 'type': 'type_adapter', 'optical_length': 32, 'mass': 41, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M92_Spacer_35mm': {'brand': 'Generic', 'name': 'M92 Spacer 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 44, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M117_Spacer_2_5mm': {'brand': 'Generic', 'name': 'M117 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 24, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M117_Spacer_3_5mm': {'brand': 'Generic', 'name': 'M117 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 24, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M117_Spacer_4_5mm': {'brand': 'Generic', 'name': 'M117 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 25, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M117_Spacer_5_5mm': {'brand': 'Generic', 'name': 'M117 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 26, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M117_Spacer_6_5mm': {'brand': 'Generic', 'name': 'M117 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 27, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M117_Spacer_7_5mm': {'brand': 'Generic', 'name': 'M117 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 28, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M117_Spacer_8_5mm': {'brand': 'Generic', 'name': 'M117 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 28, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M117_Spacer_9_5mm': {'brand': 'Generic', 'name': 'M117 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 29, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M117_Spacer_11mm': {'brand': 'Generic', 'name': 'M117 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 30, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M117_Spacer_13mm': {'brand': 'Generic', 'name': 'M117 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 32, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M117_Spacer_14mm': {'brand': 'Generic', 'name': 'M117 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 33, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M117_Spacer_16mm': {'brand': 'Generic', 'name': 'M117 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 34, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M117_Spacer_17mm': {'brand': 'Generic', 'name': 'M117 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 35, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M117_Spacer_18mm': {'brand': 'Generic', 'name': 'M117 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 36, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M117_Spacer_22mm': {'brand': 'Generic', 'name': 'M117 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 39, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M117_Spacer_28mm': {'brand': 'Generic', 'name': 'M117 Spacer 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 44, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M117_Spacer_32mm': {'brand': 'Generic', 'name': 'M117 Spacer 32mm', 'type': 'type_adapter', 'optical_length': 32, 'mass': 47, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M117_Spacer_35mm': {'brand': 'Generic', 'name': 'M117 Spacer 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 50, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M117_Spacer_45mm': {'brand': 'Generic', 'name': 'M117 Spacer 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 58, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M117_Spacer_50mm': {'brand': 'Generic', 'name': 'M117 Spacer 50mm', 'type': 'type_adapter', 'optical_length': 50, 'mass': 62, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M84_Spacer_2_5mm': {'brand': 'Generic', 'name': 'M84 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 16, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M84_Spacer_3_5mm': {'brand': 'Generic', 'name': 'M84 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 16, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M84_Spacer_4_5mm': {'brand': 'Generic', 'name': 'M84 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 17, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M84_Spacer_5_5mm': {'brand': 'Generic', 'name': 'M84 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 18, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M84_Spacer_6_5mm': {'brand': 'Generic', 'name': 'M84 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 19, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M84_Spacer_7_5mm': {'brand': 'Generic', 'name': 'M84 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 20, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M84_Spacer_8_5mm': {'brand': 'Generic', 'name': 'M84 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 20, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M84_Spacer_9mm': {'brand': 'Generic', 'name': 'M84 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 21, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M84_Spacer_9_5mm': {'brand': 'Generic', 'name': 'M84 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 21, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M84_Spacer_11mm': {'brand': 'Generic', 'name': 'M84 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 22, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M84_Spacer_13mm': {'brand': 'Generic', 'name': 'M84 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 24, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M84_Spacer_16mm': {'brand': 'Generic', 'name': 'M84 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 26, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M84_Spacer_18mm': {'brand': 'Generic', 'name': 'M84 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 28, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M84_Spacer_22mm': {'brand': 'Generic', 'name': 'M84 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 31, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M84_Spacer_28mm': {'brand': 'Generic', 'name': 'M84 Spacer 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 36, 'tside_thread': 'M84', 'tside_gender': 'Female', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}}

    @classmethod
    def Generic_M42_M48_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_M48_Adapter'])

    @classmethod
    def Generic_M48_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_M42_Adapter'])

    @classmethod
    def Generic_M42_M54_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_M54_Adapter'])

    @classmethod
    def Generic_M54_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_M42_Adapter'])

    @classmethod
    def Generic_M42_M68_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_M68_Adapter'])

    @classmethod
    def Generic_M68_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_M42_Adapter'])

    @classmethod
    def Generic_M48_M54_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_M54_Adapter'])

    @classmethod
    def Generic_M54_M48_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_M48_Adapter'])

    @classmethod
    def Generic_M48_M68_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_M68_Adapter'])

    @classmethod
    def Generic_M68_M48_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_M48_Adapter'])

    @classmethod
    def Generic_M48_M72_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_M72_Adapter'])

    @classmethod
    def Generic_M72_M48_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_M48_Adapter'])

    @classmethod
    def Generic_M54_M68_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_M68_Adapter'])

    @classmethod
    def Generic_M68_M54_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_M54_Adapter'])

    @classmethod
    def Generic_M54_M72_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_M72_Adapter'])

    @classmethod
    def Generic_M72_M54_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_M54_Adapter'])

    @classmethod
    def Generic_M54_M82_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_M82_Adapter'])

    @classmethod
    def Generic_M82_M54_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_M54_Adapter'])

    @classmethod
    def Generic_M68_M72_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_M72_Adapter'])

    @classmethod
    def Generic_M72_M68_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_M68_Adapter'])

    @classmethod
    def Generic_M68_M82_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_M82_Adapter'])

    @classmethod
    def Generic_M82_M68_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_M68_Adapter'])

    @classmethod
    def Generic_M68_M84_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_M84_Adapter'])

    @classmethod
    def Generic_M84_M68_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_M68_Adapter'])

    @classmethod
    def Generic_M72_M82_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_M82_Adapter'])

    @classmethod
    def Generic_M82_M72_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_M72_Adapter'])

    @classmethod
    def Generic_M72_M84_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_M84_Adapter'])

    @classmethod
    def Generic_M84_M72_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_M72_Adapter'])

    @classmethod
    def Generic_M82_M84_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_M84_Adapter'])

    @classmethod
    def Generic_M84_M82_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_M82_Adapter'])

    @classmethod
    def Generic_M82_M92_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_M92_Adapter'])

    @classmethod
    def Generic_M92_M82_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_M82_Adapter'])

    @classmethod
    def Generic_M84_M92_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_M92_Adapter'])

    @classmethod
    def Generic_M92_M84_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_M84_Adapter'])

    @classmethod
    def Generic_M92_M117_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_M117_Adapter'])

    @classmethod
    def Generic_M117_M92_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M117_M92_Adapter'])

    @classmethod
    def Generic_M84_M117_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_M117_Adapter'])

    @classmethod
    def Generic_M117_M84_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M117_M84_Adapter'])

    @classmethod
    def Generic_M68_M117_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_M117_Adapter'])

    @classmethod
    def Generic_M117_M68_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M117_M68_Adapter'])

    @classmethod
    def Generic_M82_M117_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_M117_Adapter'])

    @classmethod
    def Generic_M117_M82_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_M117_M82_Adapter'])

    @classmethod
    def Generic_M42_Extension_Tube_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Extension_Tube_5mm'])

    @classmethod
    def Generic_M42_Extension_Tube_10mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Extension_Tube_10mm'])

    @classmethod
    def Generic_M42_Extension_Tube_15mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Extension_Tube_15mm'])

    @classmethod
    def Generic_M42_Extension_Tube_20mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Extension_Tube_20mm'])

    @classmethod
    def Generic_M42_Extension_Tube_25mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Extension_Tube_25mm'])

    @classmethod
    def Generic_M42_Extension_Tube_30mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Extension_Tube_30mm'])

    @classmethod
    def Generic_M42_Extension_Tube_40mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Extension_Tube_40mm'])

    @classmethod
    def Generic_M42_Extension_Tube_50mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Extension_Tube_50mm'])

    @classmethod
    def Generic_M48_Extension_Tube_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Extension_Tube_5mm'])

    @classmethod
    def Generic_M48_Extension_Tube_10mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Extension_Tube_10mm'])

    @classmethod
    def Generic_M48_Extension_Tube_15mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Extension_Tube_15mm'])

    @classmethod
    def Generic_M48_Extension_Tube_20mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Extension_Tube_20mm'])

    @classmethod
    def Generic_M48_Extension_Tube_25mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Extension_Tube_25mm'])

    @classmethod
    def Generic_M48_Extension_Tube_30mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Extension_Tube_30mm'])

    @classmethod
    def Generic_M48_Extension_Tube_40mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Extension_Tube_40mm'])

    @classmethod
    def Generic_M48_Extension_Tube_50mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Extension_Tube_50mm'])

    @classmethod
    def Generic_M54_Extension_Tube_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Extension_Tube_5mm'])

    @classmethod
    def Generic_M54_Extension_Tube_10mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Extension_Tube_10mm'])

    @classmethod
    def Generic_M54_Extension_Tube_15mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Extension_Tube_15mm'])

    @classmethod
    def Generic_M54_Extension_Tube_20mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Extension_Tube_20mm'])

    @classmethod
    def Generic_M54_Extension_Tube_25mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Extension_Tube_25mm'])

    @classmethod
    def Generic_M54_Extension_Tube_30mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Extension_Tube_30mm'])

    @classmethod
    def Generic_M54_Extension_Tube_40mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Extension_Tube_40mm'])

    @classmethod
    def Generic_M54_Extension_Tube_50mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Extension_Tube_50mm'])

    @classmethod
    def Generic_M68_Extension_Tube_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Extension_Tube_5mm'])

    @classmethod
    def Generic_M68_Extension_Tube_10mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Extension_Tube_10mm'])

    @classmethod
    def Generic_M68_Extension_Tube_15mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Extension_Tube_15mm'])

    @classmethod
    def Generic_M68_Extension_Tube_20mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Extension_Tube_20mm'])

    @classmethod
    def Generic_M68_Extension_Tube_25mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Extension_Tube_25mm'])

    @classmethod
    def Generic_M68_Extension_Tube_30mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Extension_Tube_30mm'])

    @classmethod
    def Generic_M68_Extension_Tube_40mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Extension_Tube_40mm'])

    @classmethod
    def Generic_M68_Extension_Tube_50mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Extension_Tube_50mm'])

    @classmethod
    def Generic_M72_Extension_Tube_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Extension_Tube_5mm'])

    @classmethod
    def Generic_M72_Extension_Tube_10mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Extension_Tube_10mm'])

    @classmethod
    def Generic_M72_Extension_Tube_15mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Extension_Tube_15mm'])

    @classmethod
    def Generic_M72_Extension_Tube_20mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Extension_Tube_20mm'])

    @classmethod
    def Generic_M72_Extension_Tube_25mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Extension_Tube_25mm'])

    @classmethod
    def Generic_M72_Extension_Tube_30mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Extension_Tube_30mm'])

    @classmethod
    def Generic_M72_Extension_Tube_40mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Extension_Tube_40mm'])

    @classmethod
    def Generic_M72_Extension_Tube_50mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Extension_Tube_50mm'])

    @classmethod
    def Generic_T2_Ring_EOS(cls):
        return cls.from_database(cls._DATABASE['Generic_T2_Ring_EOS'])

    @classmethod
    def Generic_EOS_M48_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_EOS_M48_Adapter'])

    @classmethod
    def Generic_T2_Ring_Canon_RF(cls):
        return cls.from_database(cls._DATABASE['Generic_T2_Ring_Canon_RF'])

    @classmethod
    def Generic_Canon_RF_M48_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_Canon_RF_M48_Adapter'])

    @classmethod
    def Generic_T2_Ring_Nikon_F(cls):
        return cls.from_database(cls._DATABASE['Generic_T2_Ring_Nikon_F'])

    @classmethod
    def Generic_Nikon_F_M48_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_Nikon_F_M48_Adapter'])

    @classmethod
    def Generic_T2_Ring_Nikon_Z(cls):
        return cls.from_database(cls._DATABASE['Generic_T2_Ring_Nikon_Z'])

    @classmethod
    def Generic_Nikon_Z_M48_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_Nikon_Z_M48_Adapter'])

    @classmethod
    def Generic_T2_Ring_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Generic_T2_Ring_Sony_E'])

    @classmethod
    def Generic_Sony_E_M48_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_Sony_E_M48_Adapter'])

    @classmethod
    def Generic_T2_Ring_Fuji_X(cls):
        return cls.from_database(cls._DATABASE['Generic_T2_Ring_Fuji_X'])

    @classmethod
    def Generic_Fuji_X_M48_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_Fuji_X_M48_Adapter'])

    @classmethod
    def Generic_T2_Ring_MFT(cls):
        return cls.from_database(cls._DATABASE['Generic_T2_Ring_MFT'])

    @classmethod
    def Generic_MFT_M48_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_MFT_M48_Adapter'])

    @classmethod
    def Generic_T2_Ring_Pentax_K(cls):
        return cls.from_database(cls._DATABASE['Generic_T2_Ring_Pentax_K'])

    @classmethod
    def Generic_Pentax_K_M48_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_Pentax_K_M48_Adapter'])

    @classmethod
    def Generic_Canon_RF_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_Canon_RF_M42_Adapter'])

    @classmethod
    def Generic_Sony_E_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_Sony_E_M42_Adapter'])

    @classmethod
    def Generic_Nikon_Z_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_Nikon_Z_M42_Adapter'])

    @classmethod
    def Generic_Fuji_X_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_Fuji_X_M42_Adapter'])

    @classmethod
    def Generic_MFT_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_MFT_M42_Adapter'])

    @classmethod
    def Generic_Pentax_K_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_Pentax_K_M42_Adapter'])

    @classmethod
    def Generic_1_25_CS_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_1_25_CS_Adapter'])

    @classmethod
    def Generic_2_1_25_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_2_1_25_Adapter'])

    @classmethod
    def Generic_2_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_2_M42_Adapter'])

    @classmethod
    def Generic_2_M48_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_2_M48_Adapter'])

    @classmethod
    def Generic_2_M54_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_2_M54_Adapter'])

    @classmethod
    def Generic_1_25_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_1_25_M42_Adapter'])

    @classmethod
    def Generic_1_25_M48_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_1_25_M48_Adapter'])

    @classmethod
    def Generic_SC_M42_Adapter_short(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_M42_Adapter_short'])

    @classmethod
    def Generic_SC_M42_Adapter_long(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_M42_Adapter_long'])

    @classmethod
    def Generic_SC_M48_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_M48_Adapter'])

    @classmethod
    def Generic_SC_M54_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_M54_Adapter'])

    @classmethod
    def Generic_SC_M68_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_M68_Adapter'])

    @classmethod
    def Generic_SC_2_Adapter(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_2_Adapter'])

    @classmethod
    def Generic_M42_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_3mm'])

    @classmethod
    def Generic_M42_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_5mm'])

    @classmethod
    def Generic_M42_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_7mm'])

    @classmethod
    def Generic_M42_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_10mm'])

    @classmethod
    def Generic_M42_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_15mm'])

    @classmethod
    def Generic_M42_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_20mm'])

    @classmethod
    def Generic_M42_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_25mm'])

    @classmethod
    def Generic_M42_Spacer_30mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_30mm'])

    @classmethod
    def Generic_M48_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_3mm'])

    @classmethod
    def Generic_M48_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_5mm'])

    @classmethod
    def Generic_M48_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_7mm'])

    @classmethod
    def Generic_M48_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_10mm'])

    @classmethod
    def Generic_M48_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_15mm'])

    @classmethod
    def Generic_M48_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_20mm'])

    @classmethod
    def Generic_M48_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_25mm'])

    @classmethod
    def Generic_M48_Spacer_30mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_30mm'])

    @classmethod
    def Generic_M54_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_3mm'])

    @classmethod
    def Generic_M54_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_5mm'])

    @classmethod
    def Generic_M54_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_10mm'])

    @classmethod
    def Generic_M54_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_15mm'])

    @classmethod
    def Generic_M54_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_20mm'])

    @classmethod
    def Generic_M54_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_25mm'])

    @classmethod
    def Generic_M54_Spacer_30mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_30mm'])

    @classmethod
    def Generic_M68_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_3mm'])

    @classmethod
    def Generic_M68_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_5mm'])

    @classmethod
    def Generic_M68_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_10mm'])

    @classmethod
    def Generic_M68_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_15mm'])

    @classmethod
    def Generic_M68_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_20mm'])

    @classmethod
    def Generic_M68_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_25mm'])

    @classmethod
    def Generic_M68_Spacer_30mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_30mm'])

    @classmethod
    def Generic_M72_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Spacer_5mm'])

    @classmethod
    def Generic_M72_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Spacer_10mm'])

    @classmethod
    def Generic_M72_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Spacer_15mm'])

    @classmethod
    def Generic_M72_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Spacer_20mm'])

    @classmethod
    def Generic_M82_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Spacer_5mm'])

    @classmethod
    def Generic_M82_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Spacer_10mm'])

    @classmethod
    def Generic_M82_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Spacer_15mm'])

    @classmethod
    def Generic_M82_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Spacer_20mm'])

    @classmethod
    def Generic_M42_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_4mm'])

    @classmethod
    def Generic_M42_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_6mm'])

    @classmethod
    def Generic_M42_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_8mm'])

    @classmethod
    def Generic_M42_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_12mm'])

    @classmethod
    def Generic_M42_Spacer_35mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_35mm'])

    @classmethod
    def Generic_M42_Spacer_40mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_40mm'])

    @classmethod
    def Generic_M42_Spacer_50mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_50mm'])

    @classmethod
    def Generic_M48_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_4mm'])

    @classmethod
    def Generic_M48_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_6mm'])

    @classmethod
    def Generic_M48_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_8mm'])

    @classmethod
    def Generic_M48_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_12mm'])

    @classmethod
    def Generic_M48_Spacer_35mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_35mm'])

    @classmethod
    def Generic_M48_Spacer_40mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_40mm'])

    @classmethod
    def Generic_M48_Spacer_50mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_50mm'])

    @classmethod
    def Generic_M54_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_4mm'])

    @classmethod
    def Generic_M54_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_7mm'])

    @classmethod
    def Generic_M54_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_8mm'])

    @classmethod
    def Generic_M54_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_12mm'])

    @classmethod
    def Generic_M54_Spacer_35mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_35mm'])

    @classmethod
    def Generic_M54_Spacer_40mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_40mm'])

    @classmethod
    def Generic_M68_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_4mm'])

    @classmethod
    def Generic_M68_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_7mm'])

    @classmethod
    def Generic_M68_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_8mm'])

    @classmethod
    def Generic_M68_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_12mm'])

    @classmethod
    def Generic_M68_Spacer_35mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_35mm'])

    @classmethod
    def Generic_M68_Spacer_40mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_40mm'])

    @classmethod
    def Generic_M72_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Spacer_3mm'])

    @classmethod
    def Generic_M72_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Spacer_7mm'])

    @classmethod
    def Generic_M72_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Spacer_25mm'])

    @classmethod
    def Generic_M72_Spacer_30mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Spacer_30mm'])

    @classmethod
    def Generic_M42_Extension_Tube_2mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Extension_Tube_2mm'])

    @classmethod
    def Generic_M42_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Extension_Tube_3mm'])

    @classmethod
    def Generic_M42_Extension_Tube_7mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Extension_Tube_7mm'])

    @classmethod
    def Generic_M42_Extension_Tube_8mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Extension_Tube_8mm'])

    @classmethod
    def Generic_M42_Extension_Tube_12mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Extension_Tube_12mm'])

    @classmethod
    def Generic_M42_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Extension_Tube_35mm'])

    @classmethod
    def Generic_M42_Extension_Tube_45mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Extension_Tube_45mm'])

    @classmethod
    def Generic_M42_Extension_Tube_60mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Extension_Tube_60mm'])

    @classmethod
    def Generic_M48_Extension_Tube_2mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Extension_Tube_2mm'])

    @classmethod
    def Generic_M48_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Extension_Tube_3mm'])

    @classmethod
    def Generic_M48_Extension_Tube_7mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Extension_Tube_7mm'])

    @classmethod
    def Generic_M48_Extension_Tube_8mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Extension_Tube_8mm'])

    @classmethod
    def Generic_M48_Extension_Tube_12mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Extension_Tube_12mm'])

    @classmethod
    def Generic_M48_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Extension_Tube_35mm'])

    @classmethod
    def Generic_M48_Extension_Tube_45mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Extension_Tube_45mm'])

    @classmethod
    def Generic_M48_Extension_Tube_60mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Extension_Tube_60mm'])

    @classmethod
    def Generic_M54_Extension_Tube_2mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Extension_Tube_2mm'])

    @classmethod
    def Generic_M54_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Extension_Tube_3mm'])

    @classmethod
    def Generic_M54_Extension_Tube_7mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Extension_Tube_7mm'])

    @classmethod
    def Generic_M54_Extension_Tube_8mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Extension_Tube_8mm'])

    @classmethod
    def Generic_M54_Extension_Tube_12mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Extension_Tube_12mm'])

    @classmethod
    def Generic_M54_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Extension_Tube_35mm'])

    @classmethod
    def Generic_M54_Extension_Tube_45mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Extension_Tube_45mm'])

    @classmethod
    def Generic_M54_Extension_Tube_60mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Extension_Tube_60mm'])

    @classmethod
    def Generic_M68_Extension_Tube_2mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Extension_Tube_2mm'])

    @classmethod
    def Generic_M68_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Extension_Tube_3mm'])

    @classmethod
    def Generic_M68_Extension_Tube_7mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Extension_Tube_7mm'])

    @classmethod
    def Generic_M68_Extension_Tube_8mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Extension_Tube_8mm'])

    @classmethod
    def Generic_M68_Extension_Tube_12mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Extension_Tube_12mm'])

    @classmethod
    def Generic_M68_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Extension_Tube_35mm'])

    @classmethod
    def Generic_M68_Extension_Tube_45mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Extension_Tube_45mm'])

    @classmethod
    def Generic_M68_Extension_Tube_60mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Extension_Tube_60mm'])

    @classmethod
    def Generic_Eyepiece_Projection_Adapter_1_25(cls):
        return cls.from_database(cls._DATABASE['Generic_Eyepiece_Projection_Adapter_1_25'])

    @classmethod
    def Generic_Eyepiece_Projection_Adapter_2(cls):
        return cls.from_database(cls._DATABASE['Generic_Eyepiece_Projection_Adapter_2'])

    @classmethod
    def Generic_T_Thread_Extension_10mm(cls):
        return cls.from_database(cls._DATABASE['Generic_T_Thread_Extension_10mm'])

    @classmethod
    def Generic_T_Thread_Extension_30mm(cls):
        return cls.from_database(cls._DATABASE['Generic_T_Thread_Extension_30mm'])

    @classmethod
    def Generic_T_Thread_Extension_50mm(cls):
        return cls.from_database(cls._DATABASE['Generic_T_Thread_Extension_50mm'])

    @classmethod
    def Generic_M48_M54_Adapter_short_2mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_M54_Adapter_short_2mm'])

    @classmethod
    def Generic_M54_M68_Adapter_short_2mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_M68_Adapter_short_2mm'])

    @classmethod
    def Generic_M68_M72_Adapter_short_2mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_M72_Adapter_short_2mm'])

    @classmethod
    def Generic_M72_M82_Adapter_short_2mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_M82_Adapter_short_2mm'])

    @classmethod
    def Generic_M92_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Spacer_5mm'])

    @classmethod
    def Generic_M92_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Spacer_10mm'])

    @classmethod
    def Generic_M92_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Spacer_15mm'])

    @classmethod
    def Generic_M117_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M117_Spacer_5mm'])

    @classmethod
    def Generic_M117_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M117_Spacer_10mm'])

    @classmethod
    def Generic_M117_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M117_Spacer_20mm'])

    @classmethod
    def Generic_M117_Spacer_30mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M117_Spacer_30mm'])

    @classmethod
    def Generic_M42_Male_Male_Ring(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Male_Male_Ring'])

    @classmethod
    def Generic_M48_Male_Male_Ring(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Male_Male_Ring'])

    @classmethod
    def Generic_M54_Male_Male_Ring(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Male_Male_Ring'])

    @classmethod
    def Generic_M56_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M56_Spacer_5mm'])

    @classmethod
    def Generic_M56_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M56_Spacer_10mm'])

    @classmethod
    def Generic_M56_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M56_Spacer_15mm'])

    @classmethod
    def Generic_M56_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M56_Spacer_20mm'])

    @classmethod
    def Generic_M63_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M63_Spacer_5mm'])

    @classmethod
    def Generic_M63_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M63_Spacer_10mm'])

    @classmethod
    def Generic_M63_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M63_Spacer_15mm'])

    @classmethod
    def Generic_M63_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M63_Spacer_20mm'])

    @classmethod
    def Generic_M84_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Spacer_5mm'])

    @classmethod
    def Generic_M84_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Spacer_10mm'])

    @classmethod
    def Generic_M84_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Spacer_15mm'])

    @classmethod
    def Generic_M84_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Spacer_20mm'])

    @classmethod
    def Generic_SC_Schmidt_Cassegrain_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Schmidt_Cassegrain_Spacer_3mm'])

    @classmethod
    def Generic_SC_Schmidt_Cassegrain_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Schmidt_Cassegrain_Spacer_5mm'])

    @classmethod
    def Generic_SC_Schmidt_Cassegrain_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Schmidt_Cassegrain_Spacer_7mm'])

    @classmethod
    def Generic_SC_Schmidt_Cassegrain_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Schmidt_Cassegrain_Spacer_10mm'])

    @classmethod
    def Generic_SC_Schmidt_Cassegrain_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Schmidt_Cassegrain_Spacer_15mm'])

    @classmethod
    def Generic_SC_Schmidt_Cassegrain_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Schmidt_Cassegrain_Spacer_20mm'])

    @classmethod
    def Generic_SC_Schmidt_Cassegrain_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Schmidt_Cassegrain_Spacer_25mm'])

    @classmethod
    def Generic_SC_Schmidt_Cassegrain_Spacer_30mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Schmidt_Cassegrain_Spacer_30mm'])

    @classmethod
    def Generic_SC_Schmidt_Cassegrain_Spacer_40mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Schmidt_Cassegrain_Spacer_40mm'])

    @classmethod
    def Generic_SC_Schmidt_Cassegrain_Spacer_50mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Schmidt_Cassegrain_Spacer_50mm'])

    @classmethod
    def Generic_1_25_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_1_25_Spacer_5mm'])

    @classmethod
    def Generic_1_25_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Generic_1_25_Spacer_10mm'])

    @classmethod
    def Generic_1_25_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Generic_1_25_Spacer_15mm'])

    @classmethod
    def Generic_1_25_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Generic_1_25_Spacer_20mm'])

    @classmethod
    def Generic_1_25_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Generic_1_25_Spacer_25mm'])

    @classmethod
    def Generic_1_25_Spacer_30mm(cls):
        return cls.from_database(cls._DATABASE['Generic_1_25_Spacer_30mm'])

    @classmethod
    def Generic_2_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_2_Spacer_5mm'])

    @classmethod
    def Generic_2_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Generic_2_Spacer_10mm'])

    @classmethod
    def Generic_2_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Generic_2_Spacer_15mm'])

    @classmethod
    def Generic_2_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Generic_2_Spacer_20mm'])

    @classmethod
    def Generic_2_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Generic_2_Spacer_25mm'])

    @classmethod
    def Generic_2_Spacer_30mm(cls):
        return cls.from_database(cls._DATABASE['Generic_2_Spacer_30mm'])

    @classmethod
    def Generic_SC_Visual_Back_1_25(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Visual_Back_1_25'])

    @classmethod
    def Generic_SC_Visual_Back_2(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Visual_Back_2'])

    @classmethod
    def Generic_M42_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_9mm'])

    @classmethod
    def Generic_M42_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_14mm'])

    @classmethod
    def Generic_M42_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_17mm'])

    @classmethod
    def Generic_M42_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_22mm'])

    @classmethod
    def Generic_M42_Spacer_28mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_28mm'])

    @classmethod
    def Generic_M42_Spacer_45mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_45mm'])

    @classmethod
    def Generic_M48_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_9mm'])

    @classmethod
    def Generic_M48_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_14mm'])

    @classmethod
    def Generic_M48_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_17mm'])

    @classmethod
    def Generic_M48_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_22mm'])

    @classmethod
    def Generic_M48_Spacer_28mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_28mm'])

    @classmethod
    def Generic_M48_Spacer_45mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_45mm'])

    @classmethod
    def Generic_M54_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_6mm'])

    @classmethod
    def Generic_M54_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_9mm'])

    @classmethod
    def Generic_M54_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_14mm'])

    @classmethod
    def Generic_M54_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_17mm'])

    @classmethod
    def Generic_M54_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_22mm'])

    @classmethod
    def Generic_M54_Spacer_28mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_28mm'])

    @classmethod
    def Generic_M68_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_2_5mm'])

    @classmethod
    def Generic_M68_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_6mm'])

    @classmethod
    def Generic_M68_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_9mm'])

    @classmethod
    def Generic_M68_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_14mm'])

    @classmethod
    def Generic_M68_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_17mm'])

    @classmethod
    def Generic_M68_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_22mm'])

    @classmethod
    def Generic_M68_Spacer_28mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_28mm'])

    @classmethod
    def Generic_M72_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Spacer_2_5mm'])

    @classmethod
    def Generic_M72_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Spacer_4mm'])

    @classmethod
    def Generic_M72_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Spacer_6mm'])

    @classmethod
    def Generic_M72_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Spacer_8mm'])

    @classmethod
    def Generic_M72_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Spacer_12mm'])

    @classmethod
    def Generic_M72_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Spacer_17mm'])

    @classmethod
    def Generic_M82_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Spacer_2_5mm'])

    @classmethod
    def Generic_M82_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Spacer_3mm'])

    @classmethod
    def Generic_M82_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Spacer_4mm'])

    @classmethod
    def Generic_M82_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Spacer_6mm'])

    @classmethod
    def Generic_M82_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Spacer_7mm'])

    @classmethod
    def Generic_M82_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Spacer_8mm'])

    @classmethod
    def Generic_M82_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Spacer_12mm'])

    @classmethod
    def Generic_M82_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Spacer_17mm'])

    @classmethod
    def Generic_M82_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Spacer_25mm'])

    @classmethod
    def Generic_M82_Spacer_30mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Spacer_30mm'])

    @classmethod
    def Generic_M84_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Spacer_3mm'])

    @classmethod
    def Generic_M84_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Spacer_4mm'])

    @classmethod
    def Generic_M84_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Spacer_6mm'])

    @classmethod
    def Generic_M84_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Spacer_7mm'])

    @classmethod
    def Generic_M84_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Spacer_8mm'])

    @classmethod
    def Generic_M84_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Spacer_12mm'])

    @classmethod
    def Generic_M84_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Spacer_25mm'])

    @classmethod
    def Generic_M84_Spacer_30mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Spacer_30mm'])

    @classmethod
    def Generic_M92_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Spacer_3mm'])

    @classmethod
    def Generic_M92_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Spacer_4mm'])

    @classmethod
    def Generic_M92_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Spacer_6mm'])

    @classmethod
    def Generic_M92_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Spacer_7mm'])

    @classmethod
    def Generic_M92_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Spacer_8mm'])

    @classmethod
    def Generic_M92_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Spacer_12mm'])

    @classmethod
    def Generic_M92_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Spacer_20mm'])

    @classmethod
    def Generic_M92_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Spacer_25mm'])

    @classmethod
    def Generic_M92_Spacer_30mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Spacer_30mm'])

    @classmethod
    def Generic_M117_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M117_Spacer_3mm'])

    @classmethod
    def Generic_M117_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M117_Spacer_4mm'])

    @classmethod
    def Generic_M117_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M117_Spacer_7mm'])

    @classmethod
    def Generic_M117_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M117_Spacer_8mm'])

    @classmethod
    def Generic_M117_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M117_Spacer_12mm'])

    @classmethod
    def Generic_M117_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M117_Spacer_15mm'])

    @classmethod
    def Generic_M117_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M117_Spacer_25mm'])

    @classmethod
    def Generic_M117_Spacer_40mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M117_Spacer_40mm'])

    @classmethod
    def Generic_M42_Spacer_2_1mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_2_1mm'])

    @classmethod
    def Generic_M42_Spacer_2_3mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_2_3mm'])

    @classmethod
    def Generic_M42_Spacer_2_7mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_2_7mm'])

    @classmethod
    def Generic_M42_Spacer_3_2mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_3_2mm'])

    @classmethod
    def Generic_M42_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_3_5mm'])

    @classmethod
    def Generic_M42_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_4_5mm'])

    @classmethod
    def Generic_M42_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_5_5mm'])

    @classmethod
    def Generic_M42_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_6_5mm'])

    @classmethod
    def Generic_M42_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_8_5mm'])

    @classmethod
    def Generic_M42_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_9_5mm'])

    @classmethod
    def Generic_M42_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_11mm'])

    @classmethod
    def Generic_M42_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_13mm'])

    @classmethod
    def Generic_M42_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_16mm'])

    @classmethod
    def Generic_M42_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_18mm'])

    @classmethod
    def Generic_M42_Spacer_19mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_19mm'])

    @classmethod
    def Generic_M42_Spacer_21mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_21mm'])

    @classmethod
    def Generic_M42_Spacer_23mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_23mm'])

    @classmethod
    def Generic_M42_Spacer_24mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_24mm'])

    @classmethod
    def Generic_M42_Spacer_26mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_26mm'])

    @classmethod
    def Generic_M42_Spacer_27mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_27mm'])

    @classmethod
    def Generic_M42_Spacer_29mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_29mm'])

    @classmethod
    def Generic_M42_Spacer_32mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_32mm'])

    @classmethod
    def Generic_M42_Spacer_33mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_33mm'])

    @classmethod
    def Generic_M42_Spacer_36mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_36mm'])

    @classmethod
    def Generic_M42_Spacer_37mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_37mm'])

    @classmethod
    def Generic_M42_Spacer_38mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_38mm'])

    @classmethod
    def Generic_M42_Spacer_42mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_42mm'])

    @classmethod
    def Generic_M42_Spacer_44mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_44mm'])

    @classmethod
    def Generic_M42_Spacer_46mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_46mm'])

    @classmethod
    def Generic_M42_Spacer_48mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_48mm'])

    @classmethod
    def Generic_M48_Spacer_2_1mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_2_1mm'])

    @classmethod
    def Generic_M48_Spacer_2_3mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_2_3mm'])

    @classmethod
    def Generic_M48_Spacer_2_7mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_2_7mm'])

    @classmethod
    def Generic_M48_Spacer_3_2mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_3_2mm'])

    @classmethod
    def Generic_M48_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_3_5mm'])

    @classmethod
    def Generic_M48_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_4_5mm'])

    @classmethod
    def Generic_M48_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_5_5mm'])

    @classmethod
    def Generic_M48_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_6_5mm'])

    @classmethod
    def Generic_M48_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_8_5mm'])

    @classmethod
    def Generic_M48_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_9_5mm'])

    @classmethod
    def Generic_M48_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_11mm'])

    @classmethod
    def Generic_M48_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_13mm'])

    @classmethod
    def Generic_M48_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_16mm'])

    @classmethod
    def Generic_M48_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_18mm'])

    @classmethod
    def Generic_M48_Spacer_19mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_19mm'])

    @classmethod
    def Generic_M48_Spacer_21mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_21mm'])

    @classmethod
    def Generic_M48_Spacer_23mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_23mm'])

    @classmethod
    def Generic_M48_Spacer_24mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_24mm'])

    @classmethod
    def Generic_M48_Spacer_26mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_26mm'])

    @classmethod
    def Generic_M48_Spacer_27mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_27mm'])

    @classmethod
    def Generic_M48_Spacer_29mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_29mm'])

    @classmethod
    def Generic_M48_Spacer_32mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_32mm'])

    @classmethod
    def Generic_M48_Spacer_33mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_33mm'])

    @classmethod
    def Generic_M48_Spacer_36mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_36mm'])

    @classmethod
    def Generic_M48_Spacer_37mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_37mm'])

    @classmethod
    def Generic_M48_Spacer_38mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_38mm'])

    @classmethod
    def Generic_M48_Spacer_42mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_42mm'])

    @classmethod
    def Generic_M48_Spacer_44mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_44mm'])

    @classmethod
    def Generic_M48_Spacer_46mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_46mm'])

    @classmethod
    def Generic_M48_Spacer_48mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_48mm'])

    @classmethod
    def Generic_M54_Spacer_2_1mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_2_1mm'])

    @classmethod
    def Generic_M54_Spacer_2_3mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_2_3mm'])

    @classmethod
    def Generic_M54_Spacer_2_7mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_2_7mm'])

    @classmethod
    def Generic_M54_Spacer_3_2mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_3_2mm'])

    @classmethod
    def Generic_M54_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_3_5mm'])

    @classmethod
    def Generic_M54_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_4_5mm'])

    @classmethod
    def Generic_M54_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_5_5mm'])

    @classmethod
    def Generic_M54_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_6_5mm'])

    @classmethod
    def Generic_M54_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_7_5mm'])

    @classmethod
    def Generic_M54_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_8_5mm'])

    @classmethod
    def Generic_M54_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_9_5mm'])

    @classmethod
    def Generic_M54_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_11mm'])

    @classmethod
    def Generic_M54_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_13mm'])

    @classmethod
    def Generic_M54_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_16mm'])

    @classmethod
    def Generic_M54_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_18mm'])

    @classmethod
    def Generic_M54_Spacer_19mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_19mm'])

    @classmethod
    def Generic_M54_Spacer_21mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_21mm'])

    @classmethod
    def Generic_M54_Spacer_23mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_23mm'])

    @classmethod
    def Generic_M54_Spacer_24mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_24mm'])

    @classmethod
    def Generic_M54_Spacer_26mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_26mm'])

    @classmethod
    def Generic_M54_Spacer_27mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_27mm'])

    @classmethod
    def Generic_M68_Spacer_2_1mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_2_1mm'])

    @classmethod
    def Generic_M68_Spacer_2_3mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_2_3mm'])

    @classmethod
    def Generic_M68_Spacer_2_7mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_2_7mm'])

    @classmethod
    def Generic_M68_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_3_5mm'])

    @classmethod
    def Generic_M68_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_4_5mm'])

    @classmethod
    def Generic_M68_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_5_5mm'])

    @classmethod
    def Generic_M68_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_6_5mm'])

    @classmethod
    def Generic_M68_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_7_5mm'])

    @classmethod
    def Generic_M68_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_8_5mm'])

    @classmethod
    def Generic_M68_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_9_5mm'])

    @classmethod
    def Generic_M68_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_11mm'])

    @classmethod
    def Generic_M68_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_13mm'])

    @classmethod
    def Generic_M68_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_16mm'])

    @classmethod
    def Generic_M68_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_18mm'])

    @classmethod
    def Generic_M68_Spacer_19mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_19mm'])

    @classmethod
    def Generic_M68_Spacer_21mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_21mm'])

    @classmethod
    def Generic_M68_Spacer_23mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_23mm'])

    @classmethod
    def Generic_M68_Spacer_24mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_24mm'])

    @classmethod
    def Generic_M68_Spacer_26mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_26mm'])

    @classmethod
    def Generic_M68_Spacer_27mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_27mm'])

    @classmethod
    def Generic_M42_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Extension_Tube_6mm'])

    @classmethod
    def Generic_M42_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Extension_Tube_9mm'])

    @classmethod
    def Generic_M42_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Extension_Tube_11mm'])

    @classmethod
    def Generic_M42_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Extension_Tube_13mm'])

    @classmethod
    def Generic_M42_Extension_Tube_14mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Extension_Tube_14mm'])

    @classmethod
    def Generic_M42_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Extension_Tube_16mm'])

    @classmethod
    def Generic_M42_Extension_Tube_17mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Extension_Tube_17mm'])

    @classmethod
    def Generic_M42_Extension_Tube_18mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Extension_Tube_18mm'])

    @classmethod
    def Generic_M42_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Extension_Tube_22mm'])

    @classmethod
    def Generic_M42_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Extension_Tube_28mm'])

    @classmethod
    def Generic_M42_Extension_Tube_55mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Extension_Tube_55mm'])

    @classmethod
    def Generic_M42_Extension_Tube_75mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Extension_Tube_75mm'])

    @classmethod
    def Generic_M42_Extension_Tube_100mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Extension_Tube_100mm'])

    @classmethod
    def Generic_M48_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Extension_Tube_6mm'])

    @classmethod
    def Generic_M48_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Extension_Tube_9mm'])

    @classmethod
    def Generic_M48_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Extension_Tube_11mm'])

    @classmethod
    def Generic_M48_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Extension_Tube_13mm'])

    @classmethod
    def Generic_M48_Extension_Tube_14mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Extension_Tube_14mm'])

    @classmethod
    def Generic_M48_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Extension_Tube_16mm'])

    @classmethod
    def Generic_M48_Extension_Tube_17mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Extension_Tube_17mm'])

    @classmethod
    def Generic_M48_Extension_Tube_18mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Extension_Tube_18mm'])

    @classmethod
    def Generic_M48_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Extension_Tube_22mm'])

    @classmethod
    def Generic_M48_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Extension_Tube_28mm'])

    @classmethod
    def Generic_M48_Extension_Tube_55mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Extension_Tube_55mm'])

    @classmethod
    def Generic_M48_Extension_Tube_75mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Extension_Tube_75mm'])

    @classmethod
    def Generic_M48_Extension_Tube_100mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Extension_Tube_100mm'])

    @classmethod
    def Generic_M54_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Extension_Tube_6mm'])

    @classmethod
    def Generic_M54_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Extension_Tube_9mm'])

    @classmethod
    def Generic_M54_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Extension_Tube_11mm'])

    @classmethod
    def Generic_M54_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Extension_Tube_13mm'])

    @classmethod
    def Generic_M54_Extension_Tube_14mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Extension_Tube_14mm'])

    @classmethod
    def Generic_M54_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Extension_Tube_16mm'])

    @classmethod
    def Generic_M54_Extension_Tube_17mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Extension_Tube_17mm'])

    @classmethod
    def Generic_M54_Extension_Tube_18mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Extension_Tube_18mm'])

    @classmethod
    def Generic_M54_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Extension_Tube_22mm'])

    @classmethod
    def Generic_M54_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Extension_Tube_28mm'])

    @classmethod
    def Generic_M54_Extension_Tube_55mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Extension_Tube_55mm'])

    @classmethod
    def Generic_M54_Extension_Tube_75mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Extension_Tube_75mm'])

    @classmethod
    def Generic_M54_Extension_Tube_100mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Extension_Tube_100mm'])

    @classmethod
    def Generic_M68_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Extension_Tube_6mm'])

    @classmethod
    def Generic_M68_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Extension_Tube_9mm'])

    @classmethod
    def Generic_M68_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Extension_Tube_11mm'])

    @classmethod
    def Generic_M68_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Extension_Tube_13mm'])

    @classmethod
    def Generic_M68_Extension_Tube_14mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Extension_Tube_14mm'])

    @classmethod
    def Generic_M68_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Extension_Tube_16mm'])

    @classmethod
    def Generic_M68_Extension_Tube_17mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Extension_Tube_17mm'])

    @classmethod
    def Generic_M68_Extension_Tube_18mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Extension_Tube_18mm'])

    @classmethod
    def Generic_M68_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Extension_Tube_22mm'])

    @classmethod
    def Generic_M68_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Extension_Tube_28mm'])

    @classmethod
    def Generic_M68_Extension_Tube_55mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Extension_Tube_55mm'])

    @classmethod
    def Generic_M68_Extension_Tube_75mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Extension_Tube_75mm'])

    @classmethod
    def Generic_M68_Extension_Tube_100mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Extension_Tube_100mm'])

    @classmethod
    def Generic_M72_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Extension_Tube_3mm'])

    @classmethod
    def Generic_M72_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Extension_Tube_6mm'])

    @classmethod
    def Generic_M72_Extension_Tube_7mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Extension_Tube_7mm'])

    @classmethod
    def Generic_M72_Extension_Tube_8mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Extension_Tube_8mm'])

    @classmethod
    def Generic_M72_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Extension_Tube_9mm'])

    @classmethod
    def Generic_M72_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Extension_Tube_11mm'])

    @classmethod
    def Generic_M72_Extension_Tube_12mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Extension_Tube_12mm'])

    @classmethod
    def Generic_M72_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Extension_Tube_13mm'])

    @classmethod
    def Generic_M72_Extension_Tube_14mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Extension_Tube_14mm'])

    @classmethod
    def Generic_M72_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Extension_Tube_16mm'])

    @classmethod
    def Generic_M72_Extension_Tube_17mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Extension_Tube_17mm'])

    @classmethod
    def Generic_M72_Extension_Tube_18mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Extension_Tube_18mm'])

    @classmethod
    def Generic_M72_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Extension_Tube_22mm'])

    @classmethod
    def Generic_M72_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Extension_Tube_28mm'])

    @classmethod
    def Generic_M72_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Extension_Tube_35mm'])

    @classmethod
    def Generic_M72_Extension_Tube_45mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Extension_Tube_45mm'])

    @classmethod
    def Generic_M72_Extension_Tube_55mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Extension_Tube_55mm'])

    @classmethod
    def Generic_M72_Extension_Tube_60mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Extension_Tube_60mm'])

    @classmethod
    def Generic_M72_Extension_Tube_75mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Extension_Tube_75mm'])

    @classmethod
    def Generic_M72_Extension_Tube_100mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Extension_Tube_100mm'])

    @classmethod
    def Generic_M82_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Extension_Tube_3mm'])

    @classmethod
    def Generic_M82_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Extension_Tube_6mm'])

    @classmethod
    def Generic_M82_Extension_Tube_7mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Extension_Tube_7mm'])

    @classmethod
    def Generic_M82_Extension_Tube_8mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Extension_Tube_8mm'])

    @classmethod
    def Generic_M82_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Extension_Tube_9mm'])

    @classmethod
    def Generic_M82_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Extension_Tube_11mm'])

    @classmethod
    def Generic_M82_Extension_Tube_12mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Extension_Tube_12mm'])

    @classmethod
    def Generic_M82_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Extension_Tube_13mm'])

    @classmethod
    def Generic_M82_Extension_Tube_14mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Extension_Tube_14mm'])

    @classmethod
    def Generic_M82_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Extension_Tube_16mm'])

    @classmethod
    def Generic_M82_Extension_Tube_17mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Extension_Tube_17mm'])

    @classmethod
    def Generic_M82_Extension_Tube_18mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Extension_Tube_18mm'])

    @classmethod
    def Generic_M82_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Extension_Tube_22mm'])

    @classmethod
    def Generic_M82_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Extension_Tube_28mm'])

    @classmethod
    def Generic_M82_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Extension_Tube_35mm'])

    @classmethod
    def Generic_M82_Extension_Tube_45mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Extension_Tube_45mm'])

    @classmethod
    def Generic_M82_Extension_Tube_55mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Extension_Tube_55mm'])

    @classmethod
    def Generic_M82_Extension_Tube_60mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Extension_Tube_60mm'])

    @classmethod
    def Generic_M82_Extension_Tube_75mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Extension_Tube_75mm'])

    @classmethod
    def Generic_M82_Extension_Tube_100mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Extension_Tube_100mm'])

    @classmethod
    def Generic_M84_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Extension_Tube_3mm'])

    @classmethod
    def Generic_M84_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Extension_Tube_6mm'])

    @classmethod
    def Generic_M84_Extension_Tube_7mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Extension_Tube_7mm'])

    @classmethod
    def Generic_M84_Extension_Tube_8mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Extension_Tube_8mm'])

    @classmethod
    def Generic_M84_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Extension_Tube_9mm'])

    @classmethod
    def Generic_M84_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Extension_Tube_11mm'])

    @classmethod
    def Generic_M84_Extension_Tube_12mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Extension_Tube_12mm'])

    @classmethod
    def Generic_M84_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Extension_Tube_13mm'])

    @classmethod
    def Generic_M84_Extension_Tube_14mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Extension_Tube_14mm'])

    @classmethod
    def Generic_M84_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Extension_Tube_16mm'])

    @classmethod
    def Generic_M84_Extension_Tube_17mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Extension_Tube_17mm'])

    @classmethod
    def Generic_M84_Extension_Tube_18mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Extension_Tube_18mm'])

    @classmethod
    def Generic_M84_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Extension_Tube_22mm'])

    @classmethod
    def Generic_M84_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Extension_Tube_28mm'])

    @classmethod
    def Generic_M84_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Extension_Tube_35mm'])

    @classmethod
    def Generic_M84_Extension_Tube_45mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Extension_Tube_45mm'])

    @classmethod
    def Generic_M84_Extension_Tube_55mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Extension_Tube_55mm'])

    @classmethod
    def Generic_M84_Extension_Tube_60mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Extension_Tube_60mm'])

    @classmethod
    def Generic_M84_Extension_Tube_75mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Extension_Tube_75mm'])

    @classmethod
    def Generic_M84_Extension_Tube_100mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Extension_Tube_100mm'])

    @classmethod
    def Generic_M92_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Extension_Tube_3mm'])

    @classmethod
    def Generic_M92_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Extension_Tube_6mm'])

    @classmethod
    def Generic_M92_Extension_Tube_7mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Extension_Tube_7mm'])

    @classmethod
    def Generic_M92_Extension_Tube_8mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Extension_Tube_8mm'])

    @classmethod
    def Generic_M92_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Extension_Tube_9mm'])

    @classmethod
    def Generic_M92_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Extension_Tube_11mm'])

    @classmethod
    def Generic_M92_Extension_Tube_12mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Extension_Tube_12mm'])

    @classmethod
    def Generic_M92_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Extension_Tube_13mm'])

    @classmethod
    def Generic_M92_Extension_Tube_14mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Extension_Tube_14mm'])

    @classmethod
    def Generic_M92_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Extension_Tube_16mm'])

    @classmethod
    def Generic_M92_Extension_Tube_17mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Extension_Tube_17mm'])

    @classmethod
    def Generic_M92_Extension_Tube_18mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Extension_Tube_18mm'])

    @classmethod
    def Generic_M92_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Extension_Tube_22mm'])

    @classmethod
    def Generic_M92_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Extension_Tube_28mm'])

    @classmethod
    def Generic_M92_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Extension_Tube_35mm'])

    @classmethod
    def Generic_M92_Extension_Tube_45mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Extension_Tube_45mm'])

    @classmethod
    def Generic_M92_Extension_Tube_55mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Extension_Tube_55mm'])

    @classmethod
    def Generic_M92_Extension_Tube_60mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Extension_Tube_60mm'])

    @classmethod
    def Generic_M92_Extension_Tube_75mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Extension_Tube_75mm'])

    @classmethod
    def Generic_M92_Extension_Tube_100mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Extension_Tube_100mm'])

    @classmethod
    def Generic_M56_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M56_Spacer_2_5mm'])

    @classmethod
    def Generic_M56_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M56_Spacer_3mm'])

    @classmethod
    def Generic_M56_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M56_Spacer_3_5mm'])

    @classmethod
    def Generic_M56_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M56_Spacer_4mm'])

    @classmethod
    def Generic_M56_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M56_Spacer_4_5mm'])

    @classmethod
    def Generic_M56_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M56_Spacer_5_5mm'])

    @classmethod
    def Generic_M56_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M56_Spacer_6mm'])

    @classmethod
    def Generic_M56_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M56_Spacer_6_5mm'])

    @classmethod
    def Generic_M56_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M56_Spacer_7mm'])

    @classmethod
    def Generic_M56_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M56_Spacer_7_5mm'])

    @classmethod
    def Generic_M56_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M56_Spacer_8mm'])

    @classmethod
    def Generic_M56_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M56_Spacer_8_5mm'])

    @classmethod
    def Generic_M56_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M56_Spacer_9mm'])

    @classmethod
    def Generic_M56_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M56_Spacer_9_5mm'])

    @classmethod
    def Generic_M56_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M56_Spacer_11mm'])

    @classmethod
    def Generic_M56_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M56_Spacer_12mm'])

    @classmethod
    def Generic_M56_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M56_Spacer_13mm'])

    @classmethod
    def Generic_M56_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M56_Spacer_14mm'])

    @classmethod
    def Generic_M56_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M56_Spacer_16mm'])

    @classmethod
    def Generic_M56_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M56_Spacer_17mm'])

    @classmethod
    def Generic_M56_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M56_Spacer_18mm'])

    @classmethod
    def Generic_M56_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M56_Spacer_22mm'])

    @classmethod
    def Generic_M56_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M56_Spacer_25mm'])

    @classmethod
    def Generic_M63_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M63_Spacer_2_5mm'])

    @classmethod
    def Generic_M63_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M63_Spacer_3mm'])

    @classmethod
    def Generic_M63_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M63_Spacer_3_5mm'])

    @classmethod
    def Generic_M63_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M63_Spacer_4mm'])

    @classmethod
    def Generic_M63_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M63_Spacer_4_5mm'])

    @classmethod
    def Generic_M63_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M63_Spacer_5_5mm'])

    @classmethod
    def Generic_M63_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M63_Spacer_6mm'])

    @classmethod
    def Generic_M63_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M63_Spacer_6_5mm'])

    @classmethod
    def Generic_M63_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M63_Spacer_7mm'])

    @classmethod
    def Generic_M63_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M63_Spacer_7_5mm'])

    @classmethod
    def Generic_M63_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M63_Spacer_8mm'])

    @classmethod
    def Generic_M63_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M63_Spacer_8_5mm'])

    @classmethod
    def Generic_M63_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M63_Spacer_9mm'])

    @classmethod
    def Generic_M63_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M63_Spacer_9_5mm'])

    @classmethod
    def Generic_M63_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M63_Spacer_11mm'])

    @classmethod
    def Generic_M63_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M63_Spacer_12mm'])

    @classmethod
    def Generic_M63_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M63_Spacer_13mm'])

    @classmethod
    def Generic_M63_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M63_Spacer_14mm'])

    @classmethod
    def Generic_M63_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M63_Spacer_16mm'])

    @classmethod
    def Generic_M63_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M63_Spacer_17mm'])

    @classmethod
    def Generic_M63_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M63_Spacer_18mm'])

    @classmethod
    def Generic_M63_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M63_Spacer_22mm'])

    @classmethod
    def Generic_M63_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M63_Spacer_25mm'])

    @classmethod
    def Generic_SC_Schmidt_Cassegrain_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Schmidt_Cassegrain_Spacer_2_5mm'])

    @classmethod
    def Generic_SC_Schmidt_Cassegrain_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Schmidt_Cassegrain_Spacer_3_5mm'])

    @classmethod
    def Generic_SC_Schmidt_Cassegrain_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Schmidt_Cassegrain_Spacer_4_5mm'])

    @classmethod
    def Generic_SC_Schmidt_Cassegrain_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Schmidt_Cassegrain_Spacer_5_5mm'])

    @classmethod
    def Generic_SC_Schmidt_Cassegrain_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Schmidt_Cassegrain_Spacer_6mm'])

    @classmethod
    def Generic_SC_Schmidt_Cassegrain_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Schmidt_Cassegrain_Spacer_6_5mm'])

    @classmethod
    def Generic_SC_Schmidt_Cassegrain_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Schmidt_Cassegrain_Spacer_7_5mm'])

    @classmethod
    def Generic_SC_Schmidt_Cassegrain_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Schmidt_Cassegrain_Spacer_8mm'])

    @classmethod
    def Generic_SC_Schmidt_Cassegrain_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Schmidt_Cassegrain_Spacer_8_5mm'])

    @classmethod
    def Generic_SC_Schmidt_Cassegrain_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Schmidt_Cassegrain_Spacer_9mm'])

    @classmethod
    def Generic_SC_Schmidt_Cassegrain_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Schmidt_Cassegrain_Spacer_9_5mm'])

    @classmethod
    def Generic_SC_Schmidt_Cassegrain_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Schmidt_Cassegrain_Spacer_11mm'])

    @classmethod
    def Generic_SC_Schmidt_Cassegrain_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Schmidt_Cassegrain_Spacer_12mm'])

    @classmethod
    def Generic_SC_Schmidt_Cassegrain_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Schmidt_Cassegrain_Spacer_13mm'])

    @classmethod
    def Generic_SC_Schmidt_Cassegrain_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Schmidt_Cassegrain_Spacer_14mm'])

    @classmethod
    def Generic_SC_Schmidt_Cassegrain_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Schmidt_Cassegrain_Spacer_16mm'])

    @classmethod
    def Generic_SC_Schmidt_Cassegrain_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Schmidt_Cassegrain_Spacer_17mm'])

    @classmethod
    def Generic_SC_Schmidt_Cassegrain_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Schmidt_Cassegrain_Spacer_18mm'])

    @classmethod
    def Generic_SC_Schmidt_Cassegrain_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Schmidt_Cassegrain_Spacer_22mm'])

    @classmethod
    def Generic_SC_Schmidt_Cassegrain_Spacer_28mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Schmidt_Cassegrain_Spacer_28mm'])

    @classmethod
    def Generic_SC_Schmidt_Cassegrain_Spacer_35mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Schmidt_Cassegrain_Spacer_35mm'])

    @classmethod
    def Generic_SC_Schmidt_Cassegrain_Spacer_45mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Schmidt_Cassegrain_Spacer_45mm'])

    @classmethod
    def Generic_SC_Schmidt_Cassegrain_Spacer_55mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Schmidt_Cassegrain_Spacer_55mm'])

    @classmethod
    def Generic_SC_Schmidt_Cassegrain_Spacer_60mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Schmidt_Cassegrain_Spacer_60mm'])

    @classmethod
    def Generic_1_25_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_1_25_Spacer_2_5mm'])

    @classmethod
    def Generic_1_25_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Generic_1_25_Spacer_3mm'])

    @classmethod
    def Generic_1_25_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_1_25_Spacer_3_5mm'])

    @classmethod
    def Generic_1_25_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Generic_1_25_Spacer_4mm'])

    @classmethod
    def Generic_1_25_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_1_25_Spacer_4_5mm'])

    @classmethod
    def Generic_1_25_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_1_25_Spacer_5_5mm'])

    @classmethod
    def Generic_1_25_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Generic_1_25_Spacer_6mm'])

    @classmethod
    def Generic_1_25_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_1_25_Spacer_6_5mm'])

    @classmethod
    def Generic_1_25_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Generic_1_25_Spacer_7mm'])

    @classmethod
    def Generic_1_25_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_1_25_Spacer_7_5mm'])

    @classmethod
    def Generic_1_25_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Generic_1_25_Spacer_8mm'])

    @classmethod
    def Generic_1_25_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_1_25_Spacer_8_5mm'])

    @classmethod
    def Generic_1_25_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Generic_1_25_Spacer_9mm'])

    @classmethod
    def Generic_1_25_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_1_25_Spacer_9_5mm'])

    @classmethod
    def Generic_1_25_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Generic_1_25_Spacer_11mm'])

    @classmethod
    def Generic_1_25_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Generic_1_25_Spacer_12mm'])

    @classmethod
    def Generic_1_25_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Generic_1_25_Spacer_13mm'])

    @classmethod
    def Generic_1_25_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Generic_1_25_Spacer_14mm'])

    @classmethod
    def Generic_1_25_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Generic_1_25_Spacer_16mm'])

    @classmethod
    def Generic_1_25_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Generic_1_25_Spacer_17mm'])

    @classmethod
    def Generic_1_25_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Generic_1_25_Spacer_18mm'])

    @classmethod
    def Generic_1_25_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Generic_1_25_Spacer_22mm'])

    @classmethod
    def Generic_2_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_2_Spacer_2_5mm'])

    @classmethod
    def Generic_2_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Generic_2_Spacer_3mm'])

    @classmethod
    def Generic_2_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_2_Spacer_3_5mm'])

    @classmethod
    def Generic_2_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Generic_2_Spacer_4mm'])

    @classmethod
    def Generic_2_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_2_Spacer_4_5mm'])

    @classmethod
    def Generic_2_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_2_Spacer_5_5mm'])

    @classmethod
    def Generic_2_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Generic_2_Spacer_6mm'])

    @classmethod
    def Generic_2_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_2_Spacer_6_5mm'])

    @classmethod
    def Generic_2_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Generic_2_Spacer_7mm'])

    @classmethod
    def Generic_2_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_2_Spacer_7_5mm'])

    @classmethod
    def Generic_2_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Generic_2_Spacer_8mm'])

    @classmethod
    def Generic_2_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_2_Spacer_8_5mm'])

    @classmethod
    def Generic_2_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Generic_2_Spacer_9mm'])

    @classmethod
    def Generic_2_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_2_Spacer_9_5mm'])

    @classmethod
    def Generic_2_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Generic_2_Spacer_11mm'])

    @classmethod
    def Generic_2_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Generic_2_Spacer_12mm'])

    @classmethod
    def Generic_2_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Generic_2_Spacer_13mm'])

    @classmethod
    def Generic_2_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Generic_2_Spacer_14mm'])

    @classmethod
    def Generic_2_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Generic_2_Spacer_16mm'])

    @classmethod
    def Generic_2_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Generic_2_Spacer_17mm'])

    @classmethod
    def Generic_2_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Generic_2_Spacer_18mm'])

    @classmethod
    def Generic_2_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Generic_2_Spacer_22mm'])

    @classmethod
    def Generic_M82_Extension_Tube_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Extension_Tube_5mm'])

    @classmethod
    def Generic_M82_Extension_Tube_10mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Extension_Tube_10mm'])

    @classmethod
    def Generic_M82_Extension_Tube_15mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Extension_Tube_15mm'])

    @classmethod
    def Generic_M82_Extension_Tube_20mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Extension_Tube_20mm'])

    @classmethod
    def Generic_M82_Extension_Tube_25mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Extension_Tube_25mm'])

    @classmethod
    def Generic_M82_Extension_Tube_30mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Extension_Tube_30mm'])

    @classmethod
    def Generic_SC_Extension_Tube_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Extension_Tube_5mm'])

    @classmethod
    def Generic_SC_Extension_Tube_10mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Extension_Tube_10mm'])

    @classmethod
    def Generic_SC_Extension_Tube_15mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Extension_Tube_15mm'])

    @classmethod
    def Generic_SC_Extension_Tube_20mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Extension_Tube_20mm'])

    @classmethod
    def Generic_SC_Extension_Tube_25mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Extension_Tube_25mm'])

    @classmethod
    def Generic_SC_Extension_Tube_30mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Extension_Tube_30mm'])

    @classmethod
    def Generic_SC_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Extension_Tube_35mm'])

    @classmethod
    def Generic_SC_Extension_Tube_40mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Extension_Tube_40mm'])

    @classmethod
    def Generic_SC_Extension_Tube_50mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Extension_Tube_50mm'])

    @classmethod
    def Generic_SC_Extension_Tube_60mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Extension_Tube_60mm'])

    @classmethod
    def Generic_SC_Extension_Tube_75mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Extension_Tube_75mm'])

    @classmethod
    def Generic_M92_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Spacer_2_5mm'])

    @classmethod
    def Generic_M92_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Spacer_3_5mm'])

    @classmethod
    def Generic_M92_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Spacer_4_5mm'])

    @classmethod
    def Generic_M92_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Spacer_5_5mm'])

    @classmethod
    def Generic_M92_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Spacer_6_5mm'])

    @classmethod
    def Generic_M92_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Spacer_7_5mm'])

    @classmethod
    def Generic_M92_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Spacer_8_5mm'])

    @classmethod
    def Generic_M92_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Spacer_9_5mm'])

    @classmethod
    def Generic_M92_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Spacer_11mm'])

    @classmethod
    def Generic_M92_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Spacer_13mm'])

    @classmethod
    def Generic_M92_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Spacer_14mm'])

    @classmethod
    def Generic_M92_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Spacer_16mm'])

    @classmethod
    def Generic_M92_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Spacer_17mm'])

    @classmethod
    def Generic_M92_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Spacer_18mm'])

    @classmethod
    def Generic_M92_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Spacer_22mm'])

    @classmethod
    def Generic_M92_Spacer_28mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Spacer_28mm'])

    @classmethod
    def Generic_M92_Spacer_32mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Spacer_32mm'])

    @classmethod
    def Generic_M92_Spacer_35mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Spacer_35mm'])

    @classmethod
    def Generic_M117_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M117_Spacer_2_5mm'])

    @classmethod
    def Generic_M117_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M117_Spacer_3_5mm'])

    @classmethod
    def Generic_M117_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M117_Spacer_4_5mm'])

    @classmethod
    def Generic_M117_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M117_Spacer_5_5mm'])

    @classmethod
    def Generic_M117_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M117_Spacer_6_5mm'])

    @classmethod
    def Generic_M117_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M117_Spacer_7_5mm'])

    @classmethod
    def Generic_M117_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M117_Spacer_8_5mm'])

    @classmethod
    def Generic_M117_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M117_Spacer_9_5mm'])

    @classmethod
    def Generic_M117_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M117_Spacer_11mm'])

    @classmethod
    def Generic_M117_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M117_Spacer_13mm'])

    @classmethod
    def Generic_M117_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M117_Spacer_14mm'])

    @classmethod
    def Generic_M117_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M117_Spacer_16mm'])

    @classmethod
    def Generic_M117_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M117_Spacer_17mm'])

    @classmethod
    def Generic_M117_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M117_Spacer_18mm'])

    @classmethod
    def Generic_M117_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M117_Spacer_22mm'])

    @classmethod
    def Generic_M117_Spacer_28mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M117_Spacer_28mm'])

    @classmethod
    def Generic_M117_Spacer_32mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M117_Spacer_32mm'])

    @classmethod
    def Generic_M117_Spacer_35mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M117_Spacer_35mm'])

    @classmethod
    def Generic_M117_Spacer_45mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M117_Spacer_45mm'])

    @classmethod
    def Generic_M117_Spacer_50mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M117_Spacer_50mm'])

    @classmethod
    def Generic_M84_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Spacer_2_5mm'])

    @classmethod
    def Generic_M84_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Spacer_3_5mm'])

    @classmethod
    def Generic_M84_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Spacer_4_5mm'])

    @classmethod
    def Generic_M84_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Spacer_5_5mm'])

    @classmethod
    def Generic_M84_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Spacer_6_5mm'])

    @classmethod
    def Generic_M84_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Spacer_7_5mm'])

    @classmethod
    def Generic_M84_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Spacer_8_5mm'])

    @classmethod
    def Generic_M84_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Spacer_9mm'])

    @classmethod
    def Generic_M84_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Spacer_9_5mm'])

    @classmethod
    def Generic_M84_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Spacer_11mm'])

    @classmethod
    def Generic_M84_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Spacer_13mm'])

    @classmethod
    def Generic_M84_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Spacer_16mm'])

    @classmethod
    def Generic_M84_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Spacer_18mm'])

    @classmethod
    def Generic_M84_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Spacer_22mm'])

    @classmethod
    def Generic_M84_Spacer_28mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Spacer_28mm'])

class GenericSpacer(Spacer):
    _DATABASE = {'Generic_M42_Spacer_0_5mm': {'brand': 'Generic', 'name': 'M42 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_1mm': {'brand': 'Generic', 'name': 'M42 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_2mm': {'brand': 'Generic', 'name': 'M42 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_0_5mm': {'brand': 'Generic', 'name': 'M48 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_1mm': {'brand': 'Generic', 'name': 'M48 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_2mm': {'brand': 'Generic', 'name': 'M48 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_0_5mm': {'brand': 'Generic', 'name': 'M54 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_1mm': {'brand': 'Generic', 'name': 'M54 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_2mm': {'brand': 'Generic', 'name': 'M54 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_1mm': {'brand': 'Generic', 'name': 'M68 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_2mm': {'brand': 'Generic', 'name': 'M68 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M72_Spacer_1mm': {'brand': 'Generic', 'name': 'M72 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 13, 'tside_thread': 'M72', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M72_Spacer_2mm': {'brand': 'Generic', 'name': 'M72 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 13, 'tside_thread': 'M72', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M82_Spacer_2mm': {'brand': 'Generic', 'name': 'M82 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 16, 'tside_thread': 'M82', 'tside_gender': '', 'cside_thread': 'M82', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_0_3mm': {'brand': 'Generic', 'name': 'M42 Spacer 0.3mm', 'type': 'type_spacer', 'optical_length': 0.3, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_0_3mm': {'brand': 'Generic', 'name': 'M48 Spacer 0.3mm', 'type': 'type_spacer', 'optical_length': 0.3, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_0_3mm': {'brand': 'Generic', 'name': 'M54 Spacer 0.3mm', 'type': 'type_spacer', 'optical_length': 0.3, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_0_5mm': {'brand': 'Generic', 'name': 'M68 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M92_Spacer_2mm': {'brand': 'Generic', 'name': 'M92 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 19, 'tside_thread': 'M92', 'tside_gender': '', 'cside_thread': 'M92', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M56_Spacer_1mm': {'brand': 'Generic', 'name': 'M56 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 9, 'tside_thread': 'M56', 'tside_gender': '', 'cside_thread': 'M56', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M56_Spacer_2mm': {'brand': 'Generic', 'name': 'M56 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 9, 'tside_thread': 'M56', 'tside_gender': '', 'cside_thread': 'M56', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M63_Spacer_1mm': {'brand': 'Generic', 'name': 'M63 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 11, 'tside_thread': 'M63', 'tside_gender': '', 'cside_thread': 'M63', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M63_Spacer_2mm': {'brand': 'Generic', 'name': 'M63 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 11, 'tside_thread': 'M63', 'tside_gender': '', 'cside_thread': 'M63', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M84_Spacer_2mm': {'brand': 'Generic', 'name': 'M84 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 15, 'tside_thread': 'M84', 'tside_gender': '', 'cside_thread': 'M84', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_SC_Schmidt_Cassegrain_Spacer_1mm': {'brand': 'Generic', 'name': 'SC (Schmidt-Cassegrain) Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 21, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_SC_Schmidt_Cassegrain_Spacer_2mm': {'brand': 'Generic', 'name': 'SC (Schmidt-Cassegrain) Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 21, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_0_1mm': {'brand': 'Generic', 'name': 'M42 Spacer 0.1mm', 'type': 'type_spacer', 'optical_length': 0.1, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_0_15mm': {'brand': 'Generic', 'name': 'M42 Spacer 0.15mm', 'type': 'type_spacer', 'optical_length': 0.15, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_0_2mm': {'brand': 'Generic', 'name': 'M42 Spacer 0.2mm', 'type': 'type_spacer', 'optical_length': 0.2, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_0_25mm': {'brand': 'Generic', 'name': 'M42 Spacer 0.25mm', 'type': 'type_spacer', 'optical_length': 0.25, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_0_35mm': {'brand': 'Generic', 'name': 'M42 Spacer 0.35mm', 'type': 'type_spacer', 'optical_length': 0.35, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_0_6mm': {'brand': 'Generic', 'name': 'M42 Spacer 0.6mm', 'type': 'type_spacer', 'optical_length': 0.6, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_0_75mm': {'brand': 'Generic', 'name': 'M42 Spacer 0.75mm', 'type': 'type_spacer', 'optical_length': 0.75, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_0_8mm': {'brand': 'Generic', 'name': 'M42 Spacer 0.8mm', 'type': 'type_spacer', 'optical_length': 0.8, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_0_1mm': {'brand': 'Generic', 'name': 'M48 Spacer 0.1mm', 'type': 'type_spacer', 'optical_length': 0.1, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_0_15mm': {'brand': 'Generic', 'name': 'M48 Spacer 0.15mm', 'type': 'type_spacer', 'optical_length': 0.15, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_0_2mm': {'brand': 'Generic', 'name': 'M48 Spacer 0.2mm', 'type': 'type_spacer', 'optical_length': 0.2, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_0_25mm': {'brand': 'Generic', 'name': 'M48 Spacer 0.25mm', 'type': 'type_spacer', 'optical_length': 0.25, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_0_35mm': {'brand': 'Generic', 'name': 'M48 Spacer 0.35mm', 'type': 'type_spacer', 'optical_length': 0.35, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_0_6mm': {'brand': 'Generic', 'name': 'M48 Spacer 0.6mm', 'type': 'type_spacer', 'optical_length': 0.6, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_0_75mm': {'brand': 'Generic', 'name': 'M48 Spacer 0.75mm', 'type': 'type_spacer', 'optical_length': 0.75, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_0_8mm': {'brand': 'Generic', 'name': 'M48 Spacer 0.8mm', 'type': 'type_spacer', 'optical_length': 0.8, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_0_1mm': {'brand': 'Generic', 'name': 'M54 Spacer 0.1mm', 'type': 'type_spacer', 'optical_length': 0.1, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_0_15mm': {'brand': 'Generic', 'name': 'M54 Spacer 0.15mm', 'type': 'type_spacer', 'optical_length': 0.15, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_0_2mm': {'brand': 'Generic', 'name': 'M54 Spacer 0.2mm', 'type': 'type_spacer', 'optical_length': 0.2, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_0_25mm': {'brand': 'Generic', 'name': 'M54 Spacer 0.25mm', 'type': 'type_spacer', 'optical_length': 0.25, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_0_35mm': {'brand': 'Generic', 'name': 'M54 Spacer 0.35mm', 'type': 'type_spacer', 'optical_length': 0.35, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_0_6mm': {'brand': 'Generic', 'name': 'M54 Spacer 0.6mm', 'type': 'type_spacer', 'optical_length': 0.6, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_0_75mm': {'brand': 'Generic', 'name': 'M54 Spacer 0.75mm', 'type': 'type_spacer', 'optical_length': 0.75, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_0_8mm': {'brand': 'Generic', 'name': 'M54 Spacer 0.8mm', 'type': 'type_spacer', 'optical_length': 0.8, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_0_75mm': {'brand': 'Generic', 'name': 'M68 Spacer 0.75mm', 'type': 'type_spacer', 'optical_length': 0.75, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_1_5mm': {'brand': 'Generic', 'name': 'M68 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M72_Spacer_0_5mm': {'brand': 'Generic', 'name': 'M72 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 13, 'tside_thread': 'M72', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M72_Spacer_0_75mm': {'brand': 'Generic', 'name': 'M72 Spacer 0.75mm', 'type': 'type_spacer', 'optical_length': 0.75, 'mass': 13, 'tside_thread': 'M72', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M72_Spacer_1_5mm': {'brand': 'Generic', 'name': 'M72 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 13, 'tside_thread': 'M72', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M82_Spacer_0_5mm': {'brand': 'Generic', 'name': 'M82 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 16, 'tside_thread': 'M82', 'tside_gender': '', 'cside_thread': 'M82', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M82_Spacer_1mm': {'brand': 'Generic', 'name': 'M82 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 16, 'tside_thread': 'M82', 'tside_gender': '', 'cside_thread': 'M82', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M82_Spacer_1_5mm': {'brand': 'Generic', 'name': 'M82 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 16, 'tside_thread': 'M82', 'tside_gender': '', 'cside_thread': 'M82', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M84_Spacer_1mm': {'brand': 'Generic', 'name': 'M84 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 15, 'tside_thread': 'M84', 'tside_gender': '', 'cside_thread': 'M84', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M92_Spacer_1mm': {'brand': 'Generic', 'name': 'M92 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 17, 'tside_thread': 'M92', 'tside_gender': '', 'cside_thread': 'M92', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M117_Spacer_1mm': {'brand': 'Generic', 'name': 'M117 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 23, 'tside_thread': 'M117', 'tside_gender': '', 'cside_thread': 'M117', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M117_Spacer_2mm': {'brand': 'Generic', 'name': 'M117 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 23, 'tside_thread': 'M117', 'tside_gender': '', 'cside_thread': 'M117', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_1_1mm': {'brand': 'Generic', 'name': 'M42 Spacer 1.1mm', 'type': 'type_spacer', 'optical_length': 1.1, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_1_3mm': {'brand': 'Generic', 'name': 'M42 Spacer 1.3mm', 'type': 'type_spacer', 'optical_length': 1.3, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_1_7mm': {'brand': 'Generic', 'name': 'M42 Spacer 1.7mm', 'type': 'type_spacer', 'optical_length': 1.7, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M42_Spacer_1_9mm': {'brand': 'Generic', 'name': 'M42 Spacer 1.9mm', 'type': 'type_spacer', 'optical_length': 1.9, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_1_1mm': {'brand': 'Generic', 'name': 'M48 Spacer 1.1mm', 'type': 'type_spacer', 'optical_length': 1.1, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_1_3mm': {'brand': 'Generic', 'name': 'M48 Spacer 1.3mm', 'type': 'type_spacer', 'optical_length': 1.3, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_1_7mm': {'brand': 'Generic', 'name': 'M48 Spacer 1.7mm', 'type': 'type_spacer', 'optical_length': 1.7, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M48_Spacer_1_9mm': {'brand': 'Generic', 'name': 'M48 Spacer 1.9mm', 'type': 'type_spacer', 'optical_length': 1.9, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_1_1mm': {'brand': 'Generic', 'name': 'M54 Spacer 1.1mm', 'type': 'type_spacer', 'optical_length': 1.1, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_1_3mm': {'brand': 'Generic', 'name': 'M54 Spacer 1.3mm', 'type': 'type_spacer', 'optical_length': 1.3, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_1_7mm': {'brand': 'Generic', 'name': 'M54 Spacer 1.7mm', 'type': 'type_spacer', 'optical_length': 1.7, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M54_Spacer_1_9mm': {'brand': 'Generic', 'name': 'M54 Spacer 1.9mm', 'type': 'type_spacer', 'optical_length': 1.9, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_1_1mm': {'brand': 'Generic', 'name': 'M68 Spacer 1.1mm', 'type': 'type_spacer', 'optical_length': 1.1, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_1_3mm': {'brand': 'Generic', 'name': 'M68 Spacer 1.3mm', 'type': 'type_spacer', 'optical_length': 1.3, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_1_7mm': {'brand': 'Generic', 'name': 'M68 Spacer 1.7mm', 'type': 'type_spacer', 'optical_length': 1.7, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M68_Spacer_1_9mm': {'brand': 'Generic', 'name': 'M68 Spacer 1.9mm', 'type': 'type_spacer', 'optical_length': 1.9, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M56_Spacer_0_5mm': {'brand': 'Generic', 'name': 'M56 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 9, 'tside_thread': 'M56', 'tside_gender': '', 'cside_thread': 'M56', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M56_Spacer_0_7mm': {'brand': 'Generic', 'name': 'M56 Spacer 0.7mm', 'type': 'type_spacer', 'optical_length': 0.7, 'mass': 9, 'tside_thread': 'M56', 'tside_gender': '', 'cside_thread': 'M56', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M56_Spacer_1_5mm': {'brand': 'Generic', 'name': 'M56 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 9, 'tside_thread': 'M56', 'tside_gender': '', 'cside_thread': 'M56', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M63_Spacer_0_5mm': {'brand': 'Generic', 'name': 'M63 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 11, 'tside_thread': 'M63', 'tside_gender': '', 'cside_thread': 'M63', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M63_Spacer_0_7mm': {'brand': 'Generic', 'name': 'M63 Spacer 0.7mm', 'type': 'type_spacer', 'optical_length': 0.7, 'mass': 11, 'tside_thread': 'M63', 'tside_gender': '', 'cside_thread': 'M63', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M63_Spacer_1_5mm': {'brand': 'Generic', 'name': 'M63 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 11, 'tside_thread': 'M63', 'tside_gender': '', 'cside_thread': 'M63', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_SC_Schmidt_Cassegrain_Spacer_0_5mm': {'brand': 'Generic', 'name': 'SC (Schmidt-Cassegrain) Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 21, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_SC_Schmidt_Cassegrain_Spacer_1_5mm': {'brand': 'Generic', 'name': 'SC (Schmidt-Cassegrain) Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 21, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_1_25_Spacer_0_5mm': {'brand': 'Generic', 'name': '1.25" Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 4, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_1_25_Spacer_1mm': {'brand': 'Generic', 'name': '1.25" Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 4, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_1_25_Spacer_1_5mm': {'brand': 'Generic', 'name': '1.25" Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 4, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_1_25_Spacer_2mm': {'brand': 'Generic', 'name': '1.25" Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 4, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_2_Spacer_0_5mm': {'brand': 'Generic', 'name': '2" Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 9, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_2_Spacer_1mm': {'brand': 'Generic', 'name': '2" Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 9, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_2_Spacer_1_5mm': {'brand': 'Generic', 'name': '2" Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 9, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_2_Spacer_2mm': {'brand': 'Generic', 'name': '2" Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 9, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Generic_M92_Spacer_0_5mm': {'brand': 'Generic', 'name': 'M92 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 17, 'tside_thread': 'M92', 'tside_gender': '', 'cside_thread': 'M92', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M92_Spacer_1_5mm': {'brand': 'Generic', 'name': 'M92 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 17, 'tside_thread': 'M92', 'tside_gender': '', 'cside_thread': 'M92', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M117_Spacer_0_5mm': {'brand': 'Generic', 'name': 'M117 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 23, 'tside_thread': 'M117', 'tside_gender': '', 'cside_thread': 'M117', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M117_Spacer_1_5mm': {'brand': 'Generic', 'name': 'M117 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 23, 'tside_thread': 'M117', 'tside_gender': '', 'cside_thread': 'M117', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M84_Spacer_0_5mm': {'brand': 'Generic', 'name': 'M84 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 15, 'tside_thread': 'M84', 'tside_gender': '', 'cside_thread': 'M84', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Generic_M84_Spacer_1_5mm': {'brand': 'Generic', 'name': 'M84 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 15, 'tside_thread': 'M84', 'tside_gender': '', 'cside_thread': 'M84', 'cside_gender': '', 'reversible': True, 'bf_role': ''}}

    @classmethod
    def Generic_M42_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_0_5mm'])

    @classmethod
    def Generic_M42_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_1mm'])

    @classmethod
    def Generic_M42_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_2mm'])

    @classmethod
    def Generic_M48_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_0_5mm'])

    @classmethod
    def Generic_M48_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_1mm'])

    @classmethod
    def Generic_M48_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_2mm'])

    @classmethod
    def Generic_M54_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_0_5mm'])

    @classmethod
    def Generic_M54_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_1mm'])

    @classmethod
    def Generic_M54_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_2mm'])

    @classmethod
    def Generic_M68_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_1mm'])

    @classmethod
    def Generic_M68_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_2mm'])

    @classmethod
    def Generic_M72_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Spacer_1mm'])

    @classmethod
    def Generic_M72_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Spacer_2mm'])

    @classmethod
    def Generic_M82_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Spacer_2mm'])

    @classmethod
    def Generic_M42_Spacer_0_3mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_0_3mm'])

    @classmethod
    def Generic_M48_Spacer_0_3mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_0_3mm'])

    @classmethod
    def Generic_M54_Spacer_0_3mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_0_3mm'])

    @classmethod
    def Generic_M68_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_0_5mm'])

    @classmethod
    def Generic_M92_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Spacer_2mm'])

    @classmethod
    def Generic_M56_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M56_Spacer_1mm'])

    @classmethod
    def Generic_M56_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M56_Spacer_2mm'])

    @classmethod
    def Generic_M63_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M63_Spacer_1mm'])

    @classmethod
    def Generic_M63_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M63_Spacer_2mm'])

    @classmethod
    def Generic_M84_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Spacer_2mm'])

    @classmethod
    def Generic_SC_Schmidt_Cassegrain_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Schmidt_Cassegrain_Spacer_1mm'])

    @classmethod
    def Generic_SC_Schmidt_Cassegrain_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Schmidt_Cassegrain_Spacer_2mm'])

    @classmethod
    def Generic_M42_Spacer_0_1mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_0_1mm'])

    @classmethod
    def Generic_M42_Spacer_0_15mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_0_15mm'])

    @classmethod
    def Generic_M42_Spacer_0_2mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_0_2mm'])

    @classmethod
    def Generic_M42_Spacer_0_25mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_0_25mm'])

    @classmethod
    def Generic_M42_Spacer_0_35mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_0_35mm'])

    @classmethod
    def Generic_M42_Spacer_0_6mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_0_6mm'])

    @classmethod
    def Generic_M42_Spacer_0_75mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_0_75mm'])

    @classmethod
    def Generic_M42_Spacer_0_8mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_0_8mm'])

    @classmethod
    def Generic_M48_Spacer_0_1mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_0_1mm'])

    @classmethod
    def Generic_M48_Spacer_0_15mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_0_15mm'])

    @classmethod
    def Generic_M48_Spacer_0_2mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_0_2mm'])

    @classmethod
    def Generic_M48_Spacer_0_25mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_0_25mm'])

    @classmethod
    def Generic_M48_Spacer_0_35mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_0_35mm'])

    @classmethod
    def Generic_M48_Spacer_0_6mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_0_6mm'])

    @classmethod
    def Generic_M48_Spacer_0_75mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_0_75mm'])

    @classmethod
    def Generic_M48_Spacer_0_8mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_0_8mm'])

    @classmethod
    def Generic_M54_Spacer_0_1mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_0_1mm'])

    @classmethod
    def Generic_M54_Spacer_0_15mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_0_15mm'])

    @classmethod
    def Generic_M54_Spacer_0_2mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_0_2mm'])

    @classmethod
    def Generic_M54_Spacer_0_25mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_0_25mm'])

    @classmethod
    def Generic_M54_Spacer_0_35mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_0_35mm'])

    @classmethod
    def Generic_M54_Spacer_0_6mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_0_6mm'])

    @classmethod
    def Generic_M54_Spacer_0_75mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_0_75mm'])

    @classmethod
    def Generic_M54_Spacer_0_8mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_0_8mm'])

    @classmethod
    def Generic_M68_Spacer_0_75mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_0_75mm'])

    @classmethod
    def Generic_M68_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_1_5mm'])

    @classmethod
    def Generic_M72_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Spacer_0_5mm'])

    @classmethod
    def Generic_M72_Spacer_0_75mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Spacer_0_75mm'])

    @classmethod
    def Generic_M72_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M72_Spacer_1_5mm'])

    @classmethod
    def Generic_M82_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Spacer_0_5mm'])

    @classmethod
    def Generic_M82_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Spacer_1mm'])

    @classmethod
    def Generic_M82_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M82_Spacer_1_5mm'])

    @classmethod
    def Generic_M84_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Spacer_1mm'])

    @classmethod
    def Generic_M92_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Spacer_1mm'])

    @classmethod
    def Generic_M117_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M117_Spacer_1mm'])

    @classmethod
    def Generic_M117_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M117_Spacer_2mm'])

    @classmethod
    def Generic_M42_Spacer_1_1mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_1_1mm'])

    @classmethod
    def Generic_M42_Spacer_1_3mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_1_3mm'])

    @classmethod
    def Generic_M42_Spacer_1_7mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_1_7mm'])

    @classmethod
    def Generic_M42_Spacer_1_9mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M42_Spacer_1_9mm'])

    @classmethod
    def Generic_M48_Spacer_1_1mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_1_1mm'])

    @classmethod
    def Generic_M48_Spacer_1_3mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_1_3mm'])

    @classmethod
    def Generic_M48_Spacer_1_7mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_1_7mm'])

    @classmethod
    def Generic_M48_Spacer_1_9mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M48_Spacer_1_9mm'])

    @classmethod
    def Generic_M54_Spacer_1_1mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_1_1mm'])

    @classmethod
    def Generic_M54_Spacer_1_3mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_1_3mm'])

    @classmethod
    def Generic_M54_Spacer_1_7mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_1_7mm'])

    @classmethod
    def Generic_M54_Spacer_1_9mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M54_Spacer_1_9mm'])

    @classmethod
    def Generic_M68_Spacer_1_1mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_1_1mm'])

    @classmethod
    def Generic_M68_Spacer_1_3mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_1_3mm'])

    @classmethod
    def Generic_M68_Spacer_1_7mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_1_7mm'])

    @classmethod
    def Generic_M68_Spacer_1_9mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M68_Spacer_1_9mm'])

    @classmethod
    def Generic_M56_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M56_Spacer_0_5mm'])

    @classmethod
    def Generic_M56_Spacer_0_7mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M56_Spacer_0_7mm'])

    @classmethod
    def Generic_M56_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M56_Spacer_1_5mm'])

    @classmethod
    def Generic_M63_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M63_Spacer_0_5mm'])

    @classmethod
    def Generic_M63_Spacer_0_7mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M63_Spacer_0_7mm'])

    @classmethod
    def Generic_M63_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M63_Spacer_1_5mm'])

    @classmethod
    def Generic_SC_Schmidt_Cassegrain_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Schmidt_Cassegrain_Spacer_0_5mm'])

    @classmethod
    def Generic_SC_Schmidt_Cassegrain_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_SC_Schmidt_Cassegrain_Spacer_1_5mm'])

    @classmethod
    def Generic_1_25_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_1_25_Spacer_0_5mm'])

    @classmethod
    def Generic_1_25_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Generic_1_25_Spacer_1mm'])

    @classmethod
    def Generic_1_25_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_1_25_Spacer_1_5mm'])

    @classmethod
    def Generic_1_25_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Generic_1_25_Spacer_2mm'])

    @classmethod
    def Generic_2_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_2_Spacer_0_5mm'])

    @classmethod
    def Generic_2_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Generic_2_Spacer_1mm'])

    @classmethod
    def Generic_2_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_2_Spacer_1_5mm'])

    @classmethod
    def Generic_2_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Generic_2_Spacer_2mm'])

    @classmethod
    def Generic_M92_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Spacer_0_5mm'])

    @classmethod
    def Generic_M92_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M92_Spacer_1_5mm'])

    @classmethod
    def Generic_M117_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M117_Spacer_0_5mm'])

    @classmethod
    def Generic_M117_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M117_Spacer_1_5mm'])

    @classmethod
    def Generic_M84_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Spacer_0_5mm'])

    @classmethod
    def Generic_M84_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Generic_M84_Spacer_1_5mm'])