from ..base import Adapter, Spacer

class Gerd_neumannAdapter(Adapter):
    _DATABASE = {'Gerd_Neumann_M42_M48_Precision_Adapter': {'brand': 'Gerd Neumann', 'name': 'M42→M48 Precision Adapter', 'type': 'type_adapter', 'optical_length': 5, 'mass': 20, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M48_M54_Precision_Adapter': {'brand': 'Gerd Neumann', 'name': 'M48→M54 Precision Adapter', 'type': 'type_adapter', 'optical_length': 7, 'mass': 25, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M54_M68_Precision_Adapter': {'brand': 'Gerd Neumann', 'name': 'M54→M68 Precision Adapter', 'type': 'type_adapter', 'optical_length': 8, 'mass': 30, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M42_M68_Precision_Adapter': {'brand': 'Gerd Neumann', 'name': 'M42→M68 Precision Adapter', 'type': 'type_adapter', 'optical_length': 15, 'mass': 30, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M48_M68_Precision_Adapter': {'brand': 'Gerd Neumann', 'name': 'M48→M68 Precision Adapter', 'type': 'type_adapter', 'optical_length': 10, 'mass': 28, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_3mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_5mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 8, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_7mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 9, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_10mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 12, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_15mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_20mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 20, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_3mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_5mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 10, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_7mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 11, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_10mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 14, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_15mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_20mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 22, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_3mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 10, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_5mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 12, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_10mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 16, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_15mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 20, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_20mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 24, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_3mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 12, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_5mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 14, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_10mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 18, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_15mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 22, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_20mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 26, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Fine_Adj_Adapter_15_20mm': {'brand': 'Gerd Neumann', 'name': 'M42 Fine Adj. Adapter (15-20mm)', 'type': 'type_adapter', 'optical_length': 17.5, 'mass': 65, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M48_Fine_Adj_Adapter_15_20mm': {'brand': 'Gerd Neumann', 'name': 'M48 Fine Adj. Adapter (15-20mm)', 'type': 'type_adapter', 'optical_length': 17.5, 'mass': 75, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M54_Fine_Adj_Adapter_15_20mm': {'brand': 'Gerd Neumann', 'name': 'M54 Fine Adj. Adapter (15-20mm)', 'type': 'type_adapter', 'optical_length': 17.5, 'mass': 85, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M68_Fine_Adj_Adapter_15_20mm': {'brand': 'Gerd Neumann', 'name': 'M68 Fine Adj. Adapter (15-20mm)', 'type': 'type_adapter', 'optical_length': 17.5, 'mass': 95, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M42_Coupling_Ring_F_F': {'brand': 'Gerd Neumann', 'name': 'M42 Coupling Ring (F-F)', 'type': 'type_adapter', 'optical_length': 2, 'mass': 15, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Female', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Coupling_Ring_F_F': {'brand': 'Gerd Neumann', 'name': 'M48 Coupling Ring (F-F)', 'type': 'type_adapter', 'optical_length': 2, 'mass': 20, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Female', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Coupling_Ring_F_F': {'brand': 'Gerd Neumann', 'name': 'M54 Coupling Ring (F-F)', 'type': 'type_adapter', 'optical_length': 2, 'mass': 25, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Female', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Coupling_Ring_F_F': {'brand': 'Gerd Neumann', 'name': 'M68 Coupling Ring (F-F)', 'type': 'type_adapter', 'optical_length': 2, 'mass': 30, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_2_5mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_4mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 7, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_6mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 8, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_8mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 10, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_9mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 11, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_12mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 13, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_14mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 15, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_17mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 17, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_22mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 21, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_25mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 24, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_2_5mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_4mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 9, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_6mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 10, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_8mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 12, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_9mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 13, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_12mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 15, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_14mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 17, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_17mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 19, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_22mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 23, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_25mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 26, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_2_5mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 10, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_4mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 11, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_6mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 12, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_8mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 14, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_9mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 15, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_12mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 17, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_14mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 19, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_17mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 21, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_22mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 25, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_25mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 28, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_2_5mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 12, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_4mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 13, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_6mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 14, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_7mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 15, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_8mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 16, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_9mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 17, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_12mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 19, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_14mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 21, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_17mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 23, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_22mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 27, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_25mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 30, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M72_Spacer_2_5mm': {'brand': 'Gerd Neumann', 'name': 'M72 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 14, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M72_Spacer_3mm': {'brand': 'Gerd Neumann', 'name': 'M72 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 14, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M72_Spacer_4mm': {'brand': 'Gerd Neumann', 'name': 'M72 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 15, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M72_Spacer_6mm': {'brand': 'Gerd Neumann', 'name': 'M72 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 16, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M72_Spacer_7mm': {'brand': 'Gerd Neumann', 'name': 'M72 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 17, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M72_Spacer_8mm': {'brand': 'Gerd Neumann', 'name': 'M72 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 18, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M72_Spacer_12mm': {'brand': 'Gerd Neumann', 'name': 'M72 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 21, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M72_Spacer_15mm': {'brand': 'Gerd Neumann', 'name': 'M72 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 24, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M72_Spacer_17mm': {'brand': 'Gerd Neumann', 'name': 'M72 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 25, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M72_Spacer_20mm': {'brand': 'Gerd Neumann', 'name': 'M72 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 28, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M72_Spacer_25mm': {'brand': 'Gerd Neumann', 'name': 'M72 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 32, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_2_1mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 2.1mm', 'type': 'type_adapter', 'optical_length': 2.1, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_2_3mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 2.3mm', 'type': 'type_adapter', 'optical_length': 2.3, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_2_7mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 2.7mm', 'type': 'type_adapter', 'optical_length': 2.7, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_3_2mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 3.2mm', 'type': 'type_adapter', 'optical_length': 3.2, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_3_5mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_4_5mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 7, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_5_5mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 8, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_6_5mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 9, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_8_5mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 10, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_9_5mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 11, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_11mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 12, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_13mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 14, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_16mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_18mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 18, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_19mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 19mm', 'type': 'type_adapter', 'optical_length': 19, 'mass': 19, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_21mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 21mm', 'type': 'type_adapter', 'optical_length': 21, 'mass': 20, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_23mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 23mm', 'type': 'type_adapter', 'optical_length': 23, 'mass': 22, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_24mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 24mm', 'type': 'type_adapter', 'optical_length': 24, 'mass': 23, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_26mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 26mm', 'type': 'type_adapter', 'optical_length': 26, 'mass': 24, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_2_1mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 2.1mm', 'type': 'type_adapter', 'optical_length': 2.1, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_2_3mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 2.3mm', 'type': 'type_adapter', 'optical_length': 2.3, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_2_7mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 2.7mm', 'type': 'type_adapter', 'optical_length': 2.7, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_3_2mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 3.2mm', 'type': 'type_adapter', 'optical_length': 3.2, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_3_5mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_4_5mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 9, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_5_5mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 10, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_6_5mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 11, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_8_5mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 12, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_9_5mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 13, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_11mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 14, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_13mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 16, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_16mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_18mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 20, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_19mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 19mm', 'type': 'type_adapter', 'optical_length': 19, 'mass': 21, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_21mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 21mm', 'type': 'type_adapter', 'optical_length': 21, 'mass': 22, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_23mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 23mm', 'type': 'type_adapter', 'optical_length': 23, 'mass': 24, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_24mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 24mm', 'type': 'type_adapter', 'optical_length': 24, 'mass': 25, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_26mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 26mm', 'type': 'type_adapter', 'optical_length': 26, 'mass': 26, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_2_1mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 2.1mm', 'type': 'type_adapter', 'optical_length': 2.1, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_2_3mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 2.3mm', 'type': 'type_adapter', 'optical_length': 2.3, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_2_7mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 2.7mm', 'type': 'type_adapter', 'optical_length': 2.7, 'mass': 10, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_3_2mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 3.2mm', 'type': 'type_adapter', 'optical_length': 3.2, 'mass': 10, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_3_5mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 10, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_4_5mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 11, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_5_5mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 12, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_6_5mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 13, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_8_5mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 14, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_9_5mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 15, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_11mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 16, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_13mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 18, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_16mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 20, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_18mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 22, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_19mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 19mm', 'type': 'type_adapter', 'optical_length': 19, 'mass': 23, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_21mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 21mm', 'type': 'type_adapter', 'optical_length': 21, 'mass': 24, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_23mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 23mm', 'type': 'type_adapter', 'optical_length': 23, 'mass': 26, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_24mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 24mm', 'type': 'type_adapter', 'optical_length': 24, 'mass': 27, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_26mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 26mm', 'type': 'type_adapter', 'optical_length': 26, 'mass': 28, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_2_1mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 2.1mm', 'type': 'type_adapter', 'optical_length': 2.1, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_2_3mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 2.3mm', 'type': 'type_adapter', 'optical_length': 2.3, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_2_7mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 2.7mm', 'type': 'type_adapter', 'optical_length': 2.7, 'mass': 12, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_3_5mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 12, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_4_5mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 13, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_5_5mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 14, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_6_5mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 15, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_7_5mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 16, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_8_5mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 16, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_9_5mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 17, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_11mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 18, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_13mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 20, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_16mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 22, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_18mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 24, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_19mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 19mm', 'type': 'type_adapter', 'optical_length': 19, 'mass': 25, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_21mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 21mm', 'type': 'type_adapter', 'optical_length': 21, 'mass': 26, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_23mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 23mm', 'type': 'type_adapter', 'optical_length': 23, 'mass': 28, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_24mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 24mm', 'type': 'type_adapter', 'optical_length': 24, 'mass': 29, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M82_Spacer_2_5mm': {'brand': 'Gerd Neumann', 'name': 'M82 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 17, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M82_Spacer_3mm': {'brand': 'Gerd Neumann', 'name': 'M82 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 17, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M82_Spacer_3_5mm': {'brand': 'Gerd Neumann', 'name': 'M82 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 17, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M82_Spacer_4mm': {'brand': 'Gerd Neumann', 'name': 'M82 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 18, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M82_Spacer_4_5mm': {'brand': 'Gerd Neumann', 'name': 'M82 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 18, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M82_Spacer_5mm': {'brand': 'Gerd Neumann', 'name': 'M82 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 19, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M82_Spacer_5_5mm': {'brand': 'Gerd Neumann', 'name': 'M82 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 19, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M82_Spacer_6mm': {'brand': 'Gerd Neumann', 'name': 'M82 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 19, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M82_Spacer_6_5mm': {'brand': 'Gerd Neumann', 'name': 'M82 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 20, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M82_Spacer_7mm': {'brand': 'Gerd Neumann', 'name': 'M82 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 20, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M82_Spacer_7_5mm': {'brand': 'Gerd Neumann', 'name': 'M82 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 21, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M82_Spacer_8mm': {'brand': 'Gerd Neumann', 'name': 'M82 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 21, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M82_Spacer_8_5mm': {'brand': 'Gerd Neumann', 'name': 'M82 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 21, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M82_Spacer_9mm': {'brand': 'Gerd Neumann', 'name': 'M82 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 22, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M82_Spacer_9_5mm': {'brand': 'Gerd Neumann', 'name': 'M82 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 22, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M82_Spacer_11mm': {'brand': 'Gerd Neumann', 'name': 'M82 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 23, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M82_Spacer_12mm': {'brand': 'Gerd Neumann', 'name': 'M82 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 24, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M82_Spacer_13mm': {'brand': 'Gerd Neumann', 'name': 'M82 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 25, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M82_Spacer_14mm': {'brand': 'Gerd Neumann', 'name': 'M82 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 26, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M82_Spacer_16mm': {'brand': 'Gerd Neumann', 'name': 'M82 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 27, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M82_Spacer_17mm': {'brand': 'Gerd Neumann', 'name': 'M82 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 28, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M82_Spacer_18mm': {'brand': 'Gerd Neumann', 'name': 'M82 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 29, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M82_Spacer_22mm': {'brand': 'Gerd Neumann', 'name': 'M82 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 32, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M82_Spacer_25mm': {'brand': 'Gerd Neumann', 'name': 'M82 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 35, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M92_Spacer_3mm': {'brand': 'Gerd Neumann', 'name': 'M92 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 18, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M92_Spacer_4mm': {'brand': 'Gerd Neumann', 'name': 'M92 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 19, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M92_Spacer_5mm': {'brand': 'Gerd Neumann', 'name': 'M92 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 20, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M92_Spacer_6mm': {'brand': 'Gerd Neumann', 'name': 'M92 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 20, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M92_Spacer_7mm': {'brand': 'Gerd Neumann', 'name': 'M92 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 21, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M92_Spacer_8mm': {'brand': 'Gerd Neumann', 'name': 'M92 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 22, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M92_Spacer_9mm': {'brand': 'Gerd Neumann', 'name': 'M92 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 23, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M92_Spacer_10mm': {'brand': 'Gerd Neumann', 'name': 'M92 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 24, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M92_Spacer_12mm': {'brand': 'Gerd Neumann', 'name': 'M92 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 25, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M92_Spacer_15mm': {'brand': 'Gerd Neumann', 'name': 'M92 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 28, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M92_Spacer_17mm': {'brand': 'Gerd Neumann', 'name': 'M92 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 29, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M92_Spacer_20mm': {'brand': 'Gerd Neumann', 'name': 'M92 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 32, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M92_Spacer_25mm': {'brand': 'Gerd Neumann', 'name': 'M92 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 36, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Extension_Tube_3mm': {'brand': 'Gerd Neumann', 'name': 'M42 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 14, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M42_Extension_Tube_6mm': {'brand': 'Gerd Neumann', 'name': 'M42 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 15, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M42_Extension_Tube_9mm': {'brand': 'Gerd Neumann', 'name': 'M42 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M42_Extension_Tube_11mm': {'brand': 'Gerd Neumann', 'name': 'M42 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 17, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M42_Extension_Tube_13mm': {'brand': 'Gerd Neumann', 'name': 'M42 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 17, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M42_Extension_Tube_16mm': {'brand': 'Gerd Neumann', 'name': 'M42 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 18, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M42_Extension_Tube_22mm': {'brand': 'Gerd Neumann', 'name': 'M42 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 20, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M42_Extension_Tube_28mm': {'brand': 'Gerd Neumann', 'name': 'M42 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 22, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M42_Extension_Tube_35mm': {'brand': 'Gerd Neumann', 'name': 'M42 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 24, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M42_Extension_Tube_45mm': {'brand': 'Gerd Neumann', 'name': 'M42 Extension Tube 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 27, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M48_Extension_Tube_3mm': {'brand': 'Gerd Neumann', 'name': 'M48 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M48_Extension_Tube_6mm': {'brand': 'Gerd Neumann', 'name': 'M48 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 19, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M48_Extension_Tube_9mm': {'brand': 'Gerd Neumann', 'name': 'M48 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 20, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M48_Extension_Tube_11mm': {'brand': 'Gerd Neumann', 'name': 'M48 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 21, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M48_Extension_Tube_13mm': {'brand': 'Gerd Neumann', 'name': 'M48 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 21, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M48_Extension_Tube_16mm': {'brand': 'Gerd Neumann', 'name': 'M48 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 22, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M48_Extension_Tube_22mm': {'brand': 'Gerd Neumann', 'name': 'M48 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 24, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M48_Extension_Tube_28mm': {'brand': 'Gerd Neumann', 'name': 'M48 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 26, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M48_Extension_Tube_35mm': {'brand': 'Gerd Neumann', 'name': 'M48 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 28, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M48_Extension_Tube_45mm': {'brand': 'Gerd Neumann', 'name': 'M48 Extension Tube 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 31, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M54_Extension_Tube_3mm': {'brand': 'Gerd Neumann', 'name': 'M54 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 22, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M54_Extension_Tube_6mm': {'brand': 'Gerd Neumann', 'name': 'M54 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 23, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M54_Extension_Tube_9mm': {'brand': 'Gerd Neumann', 'name': 'M54 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 24, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M54_Extension_Tube_11mm': {'brand': 'Gerd Neumann', 'name': 'M54 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 25, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M54_Extension_Tube_13mm': {'brand': 'Gerd Neumann', 'name': 'M54 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 25, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M54_Extension_Tube_16mm': {'brand': 'Gerd Neumann', 'name': 'M54 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 26, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M54_Extension_Tube_22mm': {'brand': 'Gerd Neumann', 'name': 'M54 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 28, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M54_Extension_Tube_28mm': {'brand': 'Gerd Neumann', 'name': 'M54 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 30, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M54_Extension_Tube_35mm': {'brand': 'Gerd Neumann', 'name': 'M54 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 32, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M54_Extension_Tube_45mm': {'brand': 'Gerd Neumann', 'name': 'M54 Extension Tube 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 35, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M68_Extension_Tube_3mm': {'brand': 'Gerd Neumann', 'name': 'M68 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 18, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M68_Extension_Tube_5mm': {'brand': 'Gerd Neumann', 'name': 'M68 Extension Tube 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 19, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M68_Extension_Tube_6mm': {'brand': 'Gerd Neumann', 'name': 'M68 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 19, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M68_Extension_Tube_8mm': {'brand': 'Gerd Neumann', 'name': 'M68 Extension Tube 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 20, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M68_Extension_Tube_9mm': {'brand': 'Gerd Neumann', 'name': 'M68 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 20, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M68_Extension_Tube_11mm': {'brand': 'Gerd Neumann', 'name': 'M68 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 21, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M68_Extension_Tube_13mm': {'brand': 'Gerd Neumann', 'name': 'M68 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 21, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M68_Extension_Tube_14mm': {'brand': 'Gerd Neumann', 'name': 'M68 Extension Tube 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 22, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M68_Extension_Tube_16mm': {'brand': 'Gerd Neumann', 'name': 'M68 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 22, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M68_Extension_Tube_18mm': {'brand': 'Gerd Neumann', 'name': 'M68 Extension Tube 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 23, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M68_Extension_Tube_22mm': {'brand': 'Gerd Neumann', 'name': 'M68 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 24, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M68_Extension_Tube_25mm': {'brand': 'Gerd Neumann', 'name': 'M68 Extension Tube 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 25, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M68_Extension_Tube_28mm': {'brand': 'Gerd Neumann', 'name': 'M68 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 26, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M68_Extension_Tube_30mm': {'brand': 'Gerd Neumann', 'name': 'M68 Extension Tube 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 27, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M68_Extension_Tube_35mm': {'brand': 'Gerd Neumann', 'name': 'M68 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 28, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M72_Extension_Tube_3mm': {'brand': 'Gerd Neumann', 'name': 'M72 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 20, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M72_Extension_Tube_5mm': {'brand': 'Gerd Neumann', 'name': 'M72 Extension Tube 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 21, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M72_Extension_Tube_8mm': {'brand': 'Gerd Neumann', 'name': 'M72 Extension Tube 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 22, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M72_Extension_Tube_10mm': {'brand': 'Gerd Neumann', 'name': 'M72 Extension Tube 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 23, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M72_Extension_Tube_12mm': {'brand': 'Gerd Neumann', 'name': 'M72 Extension Tube 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 23, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M72_Extension_Tube_15mm': {'brand': 'Gerd Neumann', 'name': 'M72 Extension Tube 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 24, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M72_Extension_Tube_18mm': {'brand': 'Gerd Neumann', 'name': 'M72 Extension Tube 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 25, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M72_Extension_Tube_20mm': {'brand': 'Gerd Neumann', 'name': 'M72 Extension Tube 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 26, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M72_Extension_Tube_25mm': {'brand': 'Gerd Neumann', 'name': 'M72 Extension Tube 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 27, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M72_Extension_Tube_30mm': {'brand': 'Gerd Neumann', 'name': 'M72 Extension Tube 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 29, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M82_Extension_Tube_3mm': {'brand': 'Gerd Neumann', 'name': 'M82 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 22, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M82_Extension_Tube_5mm': {'brand': 'Gerd Neumann', 'name': 'M82 Extension Tube 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 23, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M82_Extension_Tube_8mm': {'brand': 'Gerd Neumann', 'name': 'M82 Extension Tube 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 24, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M82_Extension_Tube_10mm': {'brand': 'Gerd Neumann', 'name': 'M82 Extension Tube 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 25, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M82_Extension_Tube_12mm': {'brand': 'Gerd Neumann', 'name': 'M82 Extension Tube 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 25, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M82_Extension_Tube_15mm': {'brand': 'Gerd Neumann', 'name': 'M82 Extension Tube 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 26, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M82_Extension_Tube_18mm': {'brand': 'Gerd Neumann', 'name': 'M82 Extension Tube 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 27, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M82_Extension_Tube_20mm': {'brand': 'Gerd Neumann', 'name': 'M82 Extension Tube 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 28, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M82_Extension_Tube_25mm': {'brand': 'Gerd Neumann', 'name': 'M82 Extension Tube 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 29, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M82_Extension_Tube_30mm': {'brand': 'Gerd Neumann', 'name': 'M82 Extension Tube 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 31, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Gerd_Neumann_M92_Spacer_2_5mm': {'brand': 'Gerd Neumann', 'name': 'M92 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 18, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M92_Spacer_3_5mm': {'brand': 'Gerd Neumann', 'name': 'M92 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 18, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M92_Spacer_4_5mm': {'brand': 'Gerd Neumann', 'name': 'M92 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 19, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M92_Spacer_5_5mm': {'brand': 'Gerd Neumann', 'name': 'M92 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 20, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M92_Spacer_6_5mm': {'brand': 'Gerd Neumann', 'name': 'M92 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 21, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M92_Spacer_7_5mm': {'brand': 'Gerd Neumann', 'name': 'M92 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 22, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M92_Spacer_8_5mm': {'brand': 'Gerd Neumann', 'name': 'M92 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 22, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M92_Spacer_9_5mm': {'brand': 'Gerd Neumann', 'name': 'M92 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 23, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M92_Spacer_11mm': {'brand': 'Gerd Neumann', 'name': 'M92 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 24, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M92_Spacer_13mm': {'brand': 'Gerd Neumann', 'name': 'M92 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 26, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M92_Spacer_14mm': {'brand': 'Gerd Neumann', 'name': 'M92 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 27, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M92_Spacer_16mm': {'brand': 'Gerd Neumann', 'name': 'M92 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 28, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M92_Spacer_18mm': {'brand': 'Gerd Neumann', 'name': 'M92 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 30, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M92_Spacer_22mm': {'brand': 'Gerd Neumann', 'name': 'M92 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 33, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M92_Spacer_28mm': {'brand': 'Gerd Neumann', 'name': 'M92 Spacer 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 38, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}}

    @classmethod
    def Gerd_Neumann_M42_M48_Precision_Adapter(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_M48_Precision_Adapter'])

    @classmethod
    def Gerd_Neumann_M48_M54_Precision_Adapter(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_M54_Precision_Adapter'])

    @classmethod
    def Gerd_Neumann_M54_M68_Precision_Adapter(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_M68_Precision_Adapter'])

    @classmethod
    def Gerd_Neumann_M42_M68_Precision_Adapter(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_M68_Precision_Adapter'])

    @classmethod
    def Gerd_Neumann_M48_M68_Precision_Adapter(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_M68_Precision_Adapter'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_3mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_5mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_7mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_10mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_15mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_20mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_3mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_5mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_7mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_10mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_15mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_20mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_3mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_5mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_10mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_15mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_20mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_3mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_5mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_10mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_15mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_20mm'])

    @classmethod
    def Gerd_Neumann_M42_Fine_Adj_Adapter_15_20mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Fine_Adj_Adapter_15_20mm'])

    @classmethod
    def Gerd_Neumann_M48_Fine_Adj_Adapter_15_20mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Fine_Adj_Adapter_15_20mm'])

    @classmethod
    def Gerd_Neumann_M54_Fine_Adj_Adapter_15_20mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Fine_Adj_Adapter_15_20mm'])

    @classmethod
    def Gerd_Neumann_M68_Fine_Adj_Adapter_15_20mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Fine_Adj_Adapter_15_20mm'])

    @classmethod
    def Gerd_Neumann_M42_Coupling_Ring_F_F(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Coupling_Ring_F_F'])

    @classmethod
    def Gerd_Neumann_M48_Coupling_Ring_F_F(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Coupling_Ring_F_F'])

    @classmethod
    def Gerd_Neumann_M54_Coupling_Ring_F_F(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Coupling_Ring_F_F'])

    @classmethod
    def Gerd_Neumann_M68_Coupling_Ring_F_F(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Coupling_Ring_F_F'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_2_5mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_4mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_6mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_8mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_9mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_12mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_14mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_17mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_22mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_25mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_2_5mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_4mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_6mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_8mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_9mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_12mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_14mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_17mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_22mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_25mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_2_5mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_4mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_6mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_8mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_9mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_12mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_14mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_17mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_22mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_25mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_2_5mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_4mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_6mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_7mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_8mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_9mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_12mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_14mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_17mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_22mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_25mm'])

    @classmethod
    def Gerd_Neumann_M72_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M72_Spacer_2_5mm'])

    @classmethod
    def Gerd_Neumann_M72_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M72_Spacer_3mm'])

    @classmethod
    def Gerd_Neumann_M72_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M72_Spacer_4mm'])

    @classmethod
    def Gerd_Neumann_M72_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M72_Spacer_6mm'])

    @classmethod
    def Gerd_Neumann_M72_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M72_Spacer_7mm'])

    @classmethod
    def Gerd_Neumann_M72_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M72_Spacer_8mm'])

    @classmethod
    def Gerd_Neumann_M72_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M72_Spacer_12mm'])

    @classmethod
    def Gerd_Neumann_M72_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M72_Spacer_15mm'])

    @classmethod
    def Gerd_Neumann_M72_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M72_Spacer_17mm'])

    @classmethod
    def Gerd_Neumann_M72_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M72_Spacer_20mm'])

    @classmethod
    def Gerd_Neumann_M72_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M72_Spacer_25mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_2_1mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_2_1mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_2_3mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_2_3mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_2_7mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_2_7mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_3_2mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_3_2mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_3_5mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_4_5mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_5_5mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_6_5mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_8_5mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_9_5mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_11mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_13mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_16mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_18mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_19mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_19mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_21mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_21mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_23mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_23mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_24mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_24mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_26mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_26mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_2_1mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_2_1mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_2_3mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_2_3mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_2_7mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_2_7mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_3_2mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_3_2mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_3_5mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_4_5mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_5_5mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_6_5mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_8_5mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_9_5mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_11mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_13mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_16mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_18mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_19mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_19mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_21mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_21mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_23mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_23mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_24mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_24mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_26mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_26mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_2_1mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_2_1mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_2_3mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_2_3mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_2_7mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_2_7mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_3_2mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_3_2mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_3_5mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_4_5mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_5_5mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_6_5mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_8_5mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_9_5mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_11mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_13mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_16mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_18mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_19mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_19mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_21mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_21mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_23mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_23mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_24mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_24mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_26mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_26mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_2_1mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_2_1mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_2_3mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_2_3mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_2_7mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_2_7mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_3_5mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_4_5mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_5_5mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_6_5mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_7_5mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_8_5mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_9_5mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_11mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_13mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_16mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_18mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_19mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_19mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_21mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_21mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_23mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_23mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_24mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_24mm'])

    @classmethod
    def Gerd_Neumann_M82_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M82_Spacer_2_5mm'])

    @classmethod
    def Gerd_Neumann_M82_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M82_Spacer_3mm'])

    @classmethod
    def Gerd_Neumann_M82_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M82_Spacer_3_5mm'])

    @classmethod
    def Gerd_Neumann_M82_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M82_Spacer_4mm'])

    @classmethod
    def Gerd_Neumann_M82_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M82_Spacer_4_5mm'])

    @classmethod
    def Gerd_Neumann_M82_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M82_Spacer_5mm'])

    @classmethod
    def Gerd_Neumann_M82_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M82_Spacer_5_5mm'])

    @classmethod
    def Gerd_Neumann_M82_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M82_Spacer_6mm'])

    @classmethod
    def Gerd_Neumann_M82_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M82_Spacer_6_5mm'])

    @classmethod
    def Gerd_Neumann_M82_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M82_Spacer_7mm'])

    @classmethod
    def Gerd_Neumann_M82_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M82_Spacer_7_5mm'])

    @classmethod
    def Gerd_Neumann_M82_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M82_Spacer_8mm'])

    @classmethod
    def Gerd_Neumann_M82_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M82_Spacer_8_5mm'])

    @classmethod
    def Gerd_Neumann_M82_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M82_Spacer_9mm'])

    @classmethod
    def Gerd_Neumann_M82_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M82_Spacer_9_5mm'])

    @classmethod
    def Gerd_Neumann_M82_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M82_Spacer_11mm'])

    @classmethod
    def Gerd_Neumann_M82_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M82_Spacer_12mm'])

    @classmethod
    def Gerd_Neumann_M82_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M82_Spacer_13mm'])

    @classmethod
    def Gerd_Neumann_M82_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M82_Spacer_14mm'])

    @classmethod
    def Gerd_Neumann_M82_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M82_Spacer_16mm'])

    @classmethod
    def Gerd_Neumann_M82_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M82_Spacer_17mm'])

    @classmethod
    def Gerd_Neumann_M82_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M82_Spacer_18mm'])

    @classmethod
    def Gerd_Neumann_M82_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M82_Spacer_22mm'])

    @classmethod
    def Gerd_Neumann_M82_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M82_Spacer_25mm'])

    @classmethod
    def Gerd_Neumann_M92_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M92_Spacer_3mm'])

    @classmethod
    def Gerd_Neumann_M92_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M92_Spacer_4mm'])

    @classmethod
    def Gerd_Neumann_M92_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M92_Spacer_5mm'])

    @classmethod
    def Gerd_Neumann_M92_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M92_Spacer_6mm'])

    @classmethod
    def Gerd_Neumann_M92_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M92_Spacer_7mm'])

    @classmethod
    def Gerd_Neumann_M92_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M92_Spacer_8mm'])

    @classmethod
    def Gerd_Neumann_M92_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M92_Spacer_9mm'])

    @classmethod
    def Gerd_Neumann_M92_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M92_Spacer_10mm'])

    @classmethod
    def Gerd_Neumann_M92_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M92_Spacer_12mm'])

    @classmethod
    def Gerd_Neumann_M92_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M92_Spacer_15mm'])

    @classmethod
    def Gerd_Neumann_M92_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M92_Spacer_17mm'])

    @classmethod
    def Gerd_Neumann_M92_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M92_Spacer_20mm'])

    @classmethod
    def Gerd_Neumann_M92_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M92_Spacer_25mm'])

    @classmethod
    def Gerd_Neumann_M42_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Extension_Tube_3mm'])

    @classmethod
    def Gerd_Neumann_M42_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Extension_Tube_6mm'])

    @classmethod
    def Gerd_Neumann_M42_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Extension_Tube_9mm'])

    @classmethod
    def Gerd_Neumann_M42_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Extension_Tube_11mm'])

    @classmethod
    def Gerd_Neumann_M42_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Extension_Tube_13mm'])

    @classmethod
    def Gerd_Neumann_M42_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Extension_Tube_16mm'])

    @classmethod
    def Gerd_Neumann_M42_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Extension_Tube_22mm'])

    @classmethod
    def Gerd_Neumann_M42_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Extension_Tube_28mm'])

    @classmethod
    def Gerd_Neumann_M42_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Extension_Tube_35mm'])

    @classmethod
    def Gerd_Neumann_M42_Extension_Tube_45mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Extension_Tube_45mm'])

    @classmethod
    def Gerd_Neumann_M48_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Extension_Tube_3mm'])

    @classmethod
    def Gerd_Neumann_M48_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Extension_Tube_6mm'])

    @classmethod
    def Gerd_Neumann_M48_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Extension_Tube_9mm'])

    @classmethod
    def Gerd_Neumann_M48_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Extension_Tube_11mm'])

    @classmethod
    def Gerd_Neumann_M48_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Extension_Tube_13mm'])

    @classmethod
    def Gerd_Neumann_M48_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Extension_Tube_16mm'])

    @classmethod
    def Gerd_Neumann_M48_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Extension_Tube_22mm'])

    @classmethod
    def Gerd_Neumann_M48_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Extension_Tube_28mm'])

    @classmethod
    def Gerd_Neumann_M48_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Extension_Tube_35mm'])

    @classmethod
    def Gerd_Neumann_M48_Extension_Tube_45mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Extension_Tube_45mm'])

    @classmethod
    def Gerd_Neumann_M54_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Extension_Tube_3mm'])

    @classmethod
    def Gerd_Neumann_M54_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Extension_Tube_6mm'])

    @classmethod
    def Gerd_Neumann_M54_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Extension_Tube_9mm'])

    @classmethod
    def Gerd_Neumann_M54_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Extension_Tube_11mm'])

    @classmethod
    def Gerd_Neumann_M54_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Extension_Tube_13mm'])

    @classmethod
    def Gerd_Neumann_M54_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Extension_Tube_16mm'])

    @classmethod
    def Gerd_Neumann_M54_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Extension_Tube_22mm'])

    @classmethod
    def Gerd_Neumann_M54_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Extension_Tube_28mm'])

    @classmethod
    def Gerd_Neumann_M54_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Extension_Tube_35mm'])

    @classmethod
    def Gerd_Neumann_M54_Extension_Tube_45mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Extension_Tube_45mm'])

    @classmethod
    def Gerd_Neumann_M68_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Extension_Tube_3mm'])

    @classmethod
    def Gerd_Neumann_M68_Extension_Tube_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Extension_Tube_5mm'])

    @classmethod
    def Gerd_Neumann_M68_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Extension_Tube_6mm'])

    @classmethod
    def Gerd_Neumann_M68_Extension_Tube_8mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Extension_Tube_8mm'])

    @classmethod
    def Gerd_Neumann_M68_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Extension_Tube_9mm'])

    @classmethod
    def Gerd_Neumann_M68_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Extension_Tube_11mm'])

    @classmethod
    def Gerd_Neumann_M68_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Extension_Tube_13mm'])

    @classmethod
    def Gerd_Neumann_M68_Extension_Tube_14mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Extension_Tube_14mm'])

    @classmethod
    def Gerd_Neumann_M68_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Extension_Tube_16mm'])

    @classmethod
    def Gerd_Neumann_M68_Extension_Tube_18mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Extension_Tube_18mm'])

    @classmethod
    def Gerd_Neumann_M68_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Extension_Tube_22mm'])

    @classmethod
    def Gerd_Neumann_M68_Extension_Tube_25mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Extension_Tube_25mm'])

    @classmethod
    def Gerd_Neumann_M68_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Extension_Tube_28mm'])

    @classmethod
    def Gerd_Neumann_M68_Extension_Tube_30mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Extension_Tube_30mm'])

    @classmethod
    def Gerd_Neumann_M68_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Extension_Tube_35mm'])

    @classmethod
    def Gerd_Neumann_M72_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M72_Extension_Tube_3mm'])

    @classmethod
    def Gerd_Neumann_M72_Extension_Tube_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M72_Extension_Tube_5mm'])

    @classmethod
    def Gerd_Neumann_M72_Extension_Tube_8mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M72_Extension_Tube_8mm'])

    @classmethod
    def Gerd_Neumann_M72_Extension_Tube_10mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M72_Extension_Tube_10mm'])

    @classmethod
    def Gerd_Neumann_M72_Extension_Tube_12mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M72_Extension_Tube_12mm'])

    @classmethod
    def Gerd_Neumann_M72_Extension_Tube_15mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M72_Extension_Tube_15mm'])

    @classmethod
    def Gerd_Neumann_M72_Extension_Tube_18mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M72_Extension_Tube_18mm'])

    @classmethod
    def Gerd_Neumann_M72_Extension_Tube_20mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M72_Extension_Tube_20mm'])

    @classmethod
    def Gerd_Neumann_M72_Extension_Tube_25mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M72_Extension_Tube_25mm'])

    @classmethod
    def Gerd_Neumann_M72_Extension_Tube_30mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M72_Extension_Tube_30mm'])

    @classmethod
    def Gerd_Neumann_M82_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M82_Extension_Tube_3mm'])

    @classmethod
    def Gerd_Neumann_M82_Extension_Tube_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M82_Extension_Tube_5mm'])

    @classmethod
    def Gerd_Neumann_M82_Extension_Tube_8mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M82_Extension_Tube_8mm'])

    @classmethod
    def Gerd_Neumann_M82_Extension_Tube_10mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M82_Extension_Tube_10mm'])

    @classmethod
    def Gerd_Neumann_M82_Extension_Tube_12mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M82_Extension_Tube_12mm'])

    @classmethod
    def Gerd_Neumann_M82_Extension_Tube_15mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M82_Extension_Tube_15mm'])

    @classmethod
    def Gerd_Neumann_M82_Extension_Tube_18mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M82_Extension_Tube_18mm'])

    @classmethod
    def Gerd_Neumann_M82_Extension_Tube_20mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M82_Extension_Tube_20mm'])

    @classmethod
    def Gerd_Neumann_M82_Extension_Tube_25mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M82_Extension_Tube_25mm'])

    @classmethod
    def Gerd_Neumann_M82_Extension_Tube_30mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M82_Extension_Tube_30mm'])

    @classmethod
    def Gerd_Neumann_M92_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M92_Spacer_2_5mm'])

    @classmethod
    def Gerd_Neumann_M92_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M92_Spacer_3_5mm'])

    @classmethod
    def Gerd_Neumann_M92_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M92_Spacer_4_5mm'])

    @classmethod
    def Gerd_Neumann_M92_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M92_Spacer_5_5mm'])

    @classmethod
    def Gerd_Neumann_M92_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M92_Spacer_6_5mm'])

    @classmethod
    def Gerd_Neumann_M92_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M92_Spacer_7_5mm'])

    @classmethod
    def Gerd_Neumann_M92_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M92_Spacer_8_5mm'])

    @classmethod
    def Gerd_Neumann_M92_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M92_Spacer_9_5mm'])

    @classmethod
    def Gerd_Neumann_M92_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M92_Spacer_11mm'])

    @classmethod
    def Gerd_Neumann_M92_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M92_Spacer_13mm'])

    @classmethod
    def Gerd_Neumann_M92_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M92_Spacer_14mm'])

    @classmethod
    def Gerd_Neumann_M92_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M92_Spacer_16mm'])

    @classmethod
    def Gerd_Neumann_M92_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M92_Spacer_18mm'])

    @classmethod
    def Gerd_Neumann_M92_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M92_Spacer_22mm'])

    @classmethod
    def Gerd_Neumann_M92_Spacer_28mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M92_Spacer_28mm'])

class Gerd_neumannSpacer(Spacer):
    _DATABASE = {'Gerd_Neumann_M42_Spacer_0_3mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 0.3mm', 'type': 'type_spacer', 'optical_length': 0.3, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_0_5mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_1mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_2mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_0_3mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 0.3mm', 'type': 'type_spacer', 'optical_length': 0.3, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_0_5mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_1mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_2mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_0_5mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_1mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_2mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_0_5mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_1mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_2mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_0_15mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 0.15mm', 'type': 'type_spacer', 'optical_length': 0.15, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_0_25mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 0.25mm', 'type': 'type_spacer', 'optical_length': 0.25, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_0_6mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 0.6mm', 'type': 'type_spacer', 'optical_length': 0.6, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_0_75mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 0.75mm', 'type': 'type_spacer', 'optical_length': 0.75, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_0_8mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 0.8mm', 'type': 'type_spacer', 'optical_length': 0.8, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_1_5mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_0_15mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 0.15mm', 'type': 'type_spacer', 'optical_length': 0.15, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_0_25mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 0.25mm', 'type': 'type_spacer', 'optical_length': 0.25, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_0_6mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 0.6mm', 'type': 'type_spacer', 'optical_length': 0.6, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_0_75mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 0.75mm', 'type': 'type_spacer', 'optical_length': 0.75, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_0_8mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 0.8mm', 'type': 'type_spacer', 'optical_length': 0.8, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_1_5mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_0_15mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 0.15mm', 'type': 'type_spacer', 'optical_length': 0.15, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_0_25mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 0.25mm', 'type': 'type_spacer', 'optical_length': 0.25, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_0_6mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 0.6mm', 'type': 'type_spacer', 'optical_length': 0.6, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_0_75mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 0.75mm', 'type': 'type_spacer', 'optical_length': 0.75, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_0_8mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 0.8mm', 'type': 'type_spacer', 'optical_length': 0.8, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_1_5mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_0_25mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 0.25mm', 'type': 'type_spacer', 'optical_length': 0.25, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_0_6mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 0.6mm', 'type': 'type_spacer', 'optical_length': 0.6, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_0_75mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 0.75mm', 'type': 'type_spacer', 'optical_length': 0.75, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_1_5mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M72_Spacer_0_5mm': {'brand': 'Gerd Neumann', 'name': 'M72 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 13, 'tside_thread': 'M72', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M72_Spacer_1mm': {'brand': 'Gerd Neumann', 'name': 'M72 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 13, 'tside_thread': 'M72', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M72_Spacer_1_5mm': {'brand': 'Gerd Neumann', 'name': 'M72 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 13, 'tside_thread': 'M72', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_1_1mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 1.1mm', 'type': 'type_spacer', 'optical_length': 1.1, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_1_3mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 1.3mm', 'type': 'type_spacer', 'optical_length': 1.3, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M42_Spacer_1_7mm': {'brand': 'Gerd Neumann', 'name': 'M42 Spacer 1.7mm', 'type': 'type_spacer', 'optical_length': 1.7, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_1_1mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 1.1mm', 'type': 'type_spacer', 'optical_length': 1.1, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_1_3mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 1.3mm', 'type': 'type_spacer', 'optical_length': 1.3, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M48_Spacer_1_7mm': {'brand': 'Gerd Neumann', 'name': 'M48 Spacer 1.7mm', 'type': 'type_spacer', 'optical_length': 1.7, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_1_1mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 1.1mm', 'type': 'type_spacer', 'optical_length': 1.1, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_1_3mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 1.3mm', 'type': 'type_spacer', 'optical_length': 1.3, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M54_Spacer_1_7mm': {'brand': 'Gerd Neumann', 'name': 'M54 Spacer 1.7mm', 'type': 'type_spacer', 'optical_length': 1.7, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_1_1mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 1.1mm', 'type': 'type_spacer', 'optical_length': 1.1, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_1_3mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 1.3mm', 'type': 'type_spacer', 'optical_length': 1.3, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M68_Spacer_1_7mm': {'brand': 'Gerd Neumann', 'name': 'M68 Spacer 1.7mm', 'type': 'type_spacer', 'optical_length': 1.7, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M82_Spacer_0_5mm': {'brand': 'Gerd Neumann', 'name': 'M82 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 16, 'tside_thread': 'M82', 'tside_gender': '', 'cside_thread': 'M82', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M82_Spacer_1mm': {'brand': 'Gerd Neumann', 'name': 'M82 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 16, 'tside_thread': 'M82', 'tside_gender': '', 'cside_thread': 'M82', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M82_Spacer_1_5mm': {'brand': 'Gerd Neumann', 'name': 'M82 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 16, 'tside_thread': 'M82', 'tside_gender': '', 'cside_thread': 'M82', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M82_Spacer_2mm': {'brand': 'Gerd Neumann', 'name': 'M82 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 16, 'tside_thread': 'M82', 'tside_gender': '', 'cside_thread': 'M82', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M92_Spacer_1mm': {'brand': 'Gerd Neumann', 'name': 'M92 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 17, 'tside_thread': 'M92', 'tside_gender': '', 'cside_thread': 'M92', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M92_Spacer_2mm': {'brand': 'Gerd Neumann', 'name': 'M92 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 17, 'tside_thread': 'M92', 'tside_gender': '', 'cside_thread': 'M92', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M92_Spacer_0_5mm': {'brand': 'Gerd Neumann', 'name': 'M92 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 17, 'tside_thread': 'M92', 'tside_gender': '', 'cside_thread': 'M92', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Gerd_Neumann_M92_Spacer_1_5mm': {'brand': 'Gerd Neumann', 'name': 'M92 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 17, 'tside_thread': 'M92', 'tside_gender': '', 'cside_thread': 'M92', 'cside_gender': '', 'reversible': True, 'bf_role': ''}}

    @classmethod
    def Gerd_Neumann_M42_Spacer_0_3mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_0_3mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_0_5mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_1mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_2mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_0_3mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_0_3mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_0_5mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_1mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_2mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_0_5mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_1mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_2mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_0_5mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_1mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_2mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_0_15mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_0_15mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_0_25mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_0_25mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_0_6mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_0_6mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_0_75mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_0_75mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_0_8mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_0_8mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_1_5mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_0_15mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_0_15mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_0_25mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_0_25mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_0_6mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_0_6mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_0_75mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_0_75mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_0_8mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_0_8mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_1_5mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_0_15mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_0_15mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_0_25mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_0_25mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_0_6mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_0_6mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_0_75mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_0_75mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_0_8mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_0_8mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_1_5mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_0_25mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_0_25mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_0_6mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_0_6mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_0_75mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_0_75mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_1_5mm'])

    @classmethod
    def Gerd_Neumann_M72_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M72_Spacer_0_5mm'])

    @classmethod
    def Gerd_Neumann_M72_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M72_Spacer_1mm'])

    @classmethod
    def Gerd_Neumann_M72_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M72_Spacer_1_5mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_1_1mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_1_1mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_1_3mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_1_3mm'])

    @classmethod
    def Gerd_Neumann_M42_Spacer_1_7mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M42_Spacer_1_7mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_1_1mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_1_1mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_1_3mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_1_3mm'])

    @classmethod
    def Gerd_Neumann_M48_Spacer_1_7mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M48_Spacer_1_7mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_1_1mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_1_1mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_1_3mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_1_3mm'])

    @classmethod
    def Gerd_Neumann_M54_Spacer_1_7mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M54_Spacer_1_7mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_1_1mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_1_1mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_1_3mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_1_3mm'])

    @classmethod
    def Gerd_Neumann_M68_Spacer_1_7mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M68_Spacer_1_7mm'])

    @classmethod
    def Gerd_Neumann_M82_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M82_Spacer_0_5mm'])

    @classmethod
    def Gerd_Neumann_M82_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M82_Spacer_1mm'])

    @classmethod
    def Gerd_Neumann_M82_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M82_Spacer_1_5mm'])

    @classmethod
    def Gerd_Neumann_M82_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M82_Spacer_2mm'])

    @classmethod
    def Gerd_Neumann_M92_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M92_Spacer_1mm'])

    @classmethod
    def Gerd_Neumann_M92_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M92_Spacer_2mm'])

    @classmethod
    def Gerd_Neumann_M92_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M92_Spacer_0_5mm'])

    @classmethod
    def Gerd_Neumann_M92_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Gerd_Neumann_M92_Spacer_1_5mm'])