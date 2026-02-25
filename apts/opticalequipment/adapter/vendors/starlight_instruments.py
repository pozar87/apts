from ..base import Adapter, Spacer

class Starlight_instrumentsAdapter(Adapter):
    _DATABASE = {'Starlight_Instruments_M42_Spacer_3mm': {'brand': 'Starlight Instruments', 'name': 'M42 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M42_Spacer_5mm': {'brand': 'Starlight Instruments', 'name': 'M42 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 8, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M42_Spacer_10mm': {'brand': 'Starlight Instruments', 'name': 'M42 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 12, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M42_Spacer_15mm': {'brand': 'Starlight Instruments', 'name': 'M42 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M48_Spacer_3mm': {'brand': 'Starlight Instruments', 'name': 'M48 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M48_Spacer_5mm': {'brand': 'Starlight Instruments', 'name': 'M48 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 10, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M48_Spacer_10mm': {'brand': 'Starlight Instruments', 'name': 'M48 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 14, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M48_Spacer_15mm': {'brand': 'Starlight Instruments', 'name': 'M48 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M42_Spacer_2_5mm': {'brand': 'Starlight Instruments', 'name': 'M42 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M42_Spacer_3_5mm': {'brand': 'Starlight Instruments', 'name': 'M42 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M42_Spacer_4mm': {'brand': 'Starlight Instruments', 'name': 'M42 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 7, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M42_Spacer_4_5mm': {'brand': 'Starlight Instruments', 'name': 'M42 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 7, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M42_Spacer_5_5mm': {'brand': 'Starlight Instruments', 'name': 'M42 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 8, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M42_Spacer_6mm': {'brand': 'Starlight Instruments', 'name': 'M42 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 8, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M42_Spacer_6_5mm': {'brand': 'Starlight Instruments', 'name': 'M42 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 9, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M42_Spacer_7mm': {'brand': 'Starlight Instruments', 'name': 'M42 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 9, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M42_Spacer_7_5mm': {'brand': 'Starlight Instruments', 'name': 'M42 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 10, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M42_Spacer_8mm': {'brand': 'Starlight Instruments', 'name': 'M42 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 10, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M42_Spacer_8_5mm': {'brand': 'Starlight Instruments', 'name': 'M42 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 10, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M42_Spacer_9mm': {'brand': 'Starlight Instruments', 'name': 'M42 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 11, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M42_Spacer_9_5mm': {'brand': 'Starlight Instruments', 'name': 'M42 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 11, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M42_Spacer_11mm': {'brand': 'Starlight Instruments', 'name': 'M42 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 12, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M42_Spacer_12mm': {'brand': 'Starlight Instruments', 'name': 'M42 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 13, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M42_Spacer_13mm': {'brand': 'Starlight Instruments', 'name': 'M42 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 14, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M42_Spacer_14mm': {'brand': 'Starlight Instruments', 'name': 'M42 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 15, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M42_Spacer_16mm': {'brand': 'Starlight Instruments', 'name': 'M42 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M42_Spacer_17mm': {'brand': 'Starlight Instruments', 'name': 'M42 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 17, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M42_Spacer_18mm': {'brand': 'Starlight Instruments', 'name': 'M42 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 18, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M42_Spacer_22mm': {'brand': 'Starlight Instruments', 'name': 'M42 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 21, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M42_Spacer_25mm': {'brand': 'Starlight Instruments', 'name': 'M42 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 24, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M48_Spacer_2_5mm': {'brand': 'Starlight Instruments', 'name': 'M48 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M48_Spacer_3_5mm': {'brand': 'Starlight Instruments', 'name': 'M48 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M48_Spacer_4mm': {'brand': 'Starlight Instruments', 'name': 'M48 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 9, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M48_Spacer_4_5mm': {'brand': 'Starlight Instruments', 'name': 'M48 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 9, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M48_Spacer_5_5mm': {'brand': 'Starlight Instruments', 'name': 'M48 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 10, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M48_Spacer_6mm': {'brand': 'Starlight Instruments', 'name': 'M48 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 10, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M48_Spacer_6_5mm': {'brand': 'Starlight Instruments', 'name': 'M48 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 11, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M48_Spacer_7mm': {'brand': 'Starlight Instruments', 'name': 'M48 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 11, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M48_Spacer_7_5mm': {'brand': 'Starlight Instruments', 'name': 'M48 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 12, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M48_Spacer_8mm': {'brand': 'Starlight Instruments', 'name': 'M48 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 12, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M48_Spacer_8_5mm': {'brand': 'Starlight Instruments', 'name': 'M48 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 12, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M48_Spacer_9mm': {'brand': 'Starlight Instruments', 'name': 'M48 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 13, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M48_Spacer_9_5mm': {'brand': 'Starlight Instruments', 'name': 'M48 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 13, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M48_Spacer_11mm': {'brand': 'Starlight Instruments', 'name': 'M48 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 14, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M48_Spacer_12mm': {'brand': 'Starlight Instruments', 'name': 'M48 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 15, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M48_Spacer_13mm': {'brand': 'Starlight Instruments', 'name': 'M48 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 16, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M48_Spacer_14mm': {'brand': 'Starlight Instruments', 'name': 'M48 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 17, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M48_Spacer_16mm': {'brand': 'Starlight Instruments', 'name': 'M48 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M48_Spacer_17mm': {'brand': 'Starlight Instruments', 'name': 'M48 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 19, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M48_Spacer_18mm': {'brand': 'Starlight Instruments', 'name': 'M48 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 20, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M48_Spacer_22mm': {'brand': 'Starlight Instruments', 'name': 'M48 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 23, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M48_Spacer_25mm': {'brand': 'Starlight Instruments', 'name': 'M48 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 26, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M42_Extension_Tube_3mm': {'brand': 'Starlight Instruments', 'name': 'M42 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 14, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Starlight_Instruments_M42_Extension_Tube_6mm': {'brand': 'Starlight Instruments', 'name': 'M42 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 15, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Starlight_Instruments_M42_Extension_Tube_9mm': {'brand': 'Starlight Instruments', 'name': 'M42 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Starlight_Instruments_M42_Extension_Tube_11mm': {'brand': 'Starlight Instruments', 'name': 'M42 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 17, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Starlight_Instruments_M42_Extension_Tube_13mm': {'brand': 'Starlight Instruments', 'name': 'M42 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 17, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Starlight_Instruments_M42_Extension_Tube_16mm': {'brand': 'Starlight Instruments', 'name': 'M42 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 18, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Starlight_Instruments_M42_Extension_Tube_22mm': {'brand': 'Starlight Instruments', 'name': 'M42 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 20, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Starlight_Instruments_M42_Extension_Tube_28mm': {'brand': 'Starlight Instruments', 'name': 'M42 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 22, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Starlight_Instruments_M42_Extension_Tube_35mm': {'brand': 'Starlight Instruments', 'name': 'M42 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 24, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Starlight_Instruments_M42_Extension_Tube_45mm': {'brand': 'Starlight Instruments', 'name': 'M42 Extension Tube 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 27, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Starlight_Instruments_M48_Extension_Tube_3mm': {'brand': 'Starlight Instruments', 'name': 'M48 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Starlight_Instruments_M48_Extension_Tube_6mm': {'brand': 'Starlight Instruments', 'name': 'M48 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 19, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Starlight_Instruments_M48_Extension_Tube_9mm': {'brand': 'Starlight Instruments', 'name': 'M48 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 20, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Starlight_Instruments_M48_Extension_Tube_11mm': {'brand': 'Starlight Instruments', 'name': 'M48 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 21, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Starlight_Instruments_M48_Extension_Tube_13mm': {'brand': 'Starlight Instruments', 'name': 'M48 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 21, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Starlight_Instruments_M48_Extension_Tube_16mm': {'brand': 'Starlight Instruments', 'name': 'M48 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 22, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Starlight_Instruments_M48_Extension_Tube_22mm': {'brand': 'Starlight Instruments', 'name': 'M48 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 24, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Starlight_Instruments_M48_Extension_Tube_28mm': {'brand': 'Starlight Instruments', 'name': 'M48 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 26, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Starlight_Instruments_M48_Extension_Tube_35mm': {'brand': 'Starlight Instruments', 'name': 'M48 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 28, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Starlight_Instruments_M48_Extension_Tube_45mm': {'brand': 'Starlight Instruments', 'name': 'M48 Extension Tube 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 31, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Starlight_Instruments_M54_Extension_Tube_3mm': {'brand': 'Starlight Instruments', 'name': 'M54 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 22, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Starlight_Instruments_M54_Extension_Tube_6mm': {'brand': 'Starlight Instruments', 'name': 'M54 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 23, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Starlight_Instruments_M54_Extension_Tube_9mm': {'brand': 'Starlight Instruments', 'name': 'M54 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 24, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Starlight_Instruments_M54_Extension_Tube_11mm': {'brand': 'Starlight Instruments', 'name': 'M54 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 25, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Starlight_Instruments_M54_Extension_Tube_13mm': {'brand': 'Starlight Instruments', 'name': 'M54 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 25, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Starlight_Instruments_M54_Extension_Tube_16mm': {'brand': 'Starlight Instruments', 'name': 'M54 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 26, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Starlight_Instruments_M54_Extension_Tube_22mm': {'brand': 'Starlight Instruments', 'name': 'M54 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 28, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Starlight_Instruments_M54_Extension_Tube_28mm': {'brand': 'Starlight Instruments', 'name': 'M54 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 30, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Starlight_Instruments_M54_Extension_Tube_35mm': {'brand': 'Starlight Instruments', 'name': 'M54 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 32, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Starlight_Instruments_M54_Extension_Tube_45mm': {'brand': 'Starlight Instruments', 'name': 'M54 Extension Tube 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 35, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Starlight_Instruments_M42_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Spacer_3mm'])

    @classmethod
    def Starlight_Instruments_M42_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Spacer_5mm'])

    @classmethod
    def Starlight_Instruments_M42_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Spacer_10mm'])

    @classmethod
    def Starlight_Instruments_M42_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Spacer_15mm'])

    @classmethod
    def Starlight_Instruments_M48_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Spacer_3mm'])

    @classmethod
    def Starlight_Instruments_M48_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Spacer_5mm'])

    @classmethod
    def Starlight_Instruments_M48_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Spacer_10mm'])

    @classmethod
    def Starlight_Instruments_M48_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Spacer_15mm'])

    @classmethod
    def Starlight_Instruments_M42_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Spacer_2_5mm'])

    @classmethod
    def Starlight_Instruments_M42_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Spacer_3_5mm'])

    @classmethod
    def Starlight_Instruments_M42_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Spacer_4mm'])

    @classmethod
    def Starlight_Instruments_M42_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Spacer_4_5mm'])

    @classmethod
    def Starlight_Instruments_M42_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Spacer_5_5mm'])

    @classmethod
    def Starlight_Instruments_M42_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Spacer_6mm'])

    @classmethod
    def Starlight_Instruments_M42_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Spacer_6_5mm'])

    @classmethod
    def Starlight_Instruments_M42_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Spacer_7mm'])

    @classmethod
    def Starlight_Instruments_M42_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Spacer_7_5mm'])

    @classmethod
    def Starlight_Instruments_M42_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Spacer_8mm'])

    @classmethod
    def Starlight_Instruments_M42_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Spacer_8_5mm'])

    @classmethod
    def Starlight_Instruments_M42_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Spacer_9mm'])

    @classmethod
    def Starlight_Instruments_M42_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Spacer_9_5mm'])

    @classmethod
    def Starlight_Instruments_M42_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Spacer_11mm'])

    @classmethod
    def Starlight_Instruments_M42_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Spacer_12mm'])

    @classmethod
    def Starlight_Instruments_M42_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Spacer_13mm'])

    @classmethod
    def Starlight_Instruments_M42_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Spacer_14mm'])

    @classmethod
    def Starlight_Instruments_M42_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Spacer_16mm'])

    @classmethod
    def Starlight_Instruments_M42_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Spacer_17mm'])

    @classmethod
    def Starlight_Instruments_M42_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Spacer_18mm'])

    @classmethod
    def Starlight_Instruments_M42_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Spacer_22mm'])

    @classmethod
    def Starlight_Instruments_M42_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Spacer_25mm'])

    @classmethod
    def Starlight_Instruments_M48_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Spacer_2_5mm'])

    @classmethod
    def Starlight_Instruments_M48_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Spacer_3_5mm'])

    @classmethod
    def Starlight_Instruments_M48_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Spacer_4mm'])

    @classmethod
    def Starlight_Instruments_M48_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Spacer_4_5mm'])

    @classmethod
    def Starlight_Instruments_M48_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Spacer_5_5mm'])

    @classmethod
    def Starlight_Instruments_M48_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Spacer_6mm'])

    @classmethod
    def Starlight_Instruments_M48_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Spacer_6_5mm'])

    @classmethod
    def Starlight_Instruments_M48_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Spacer_7mm'])

    @classmethod
    def Starlight_Instruments_M48_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Spacer_7_5mm'])

    @classmethod
    def Starlight_Instruments_M48_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Spacer_8mm'])

    @classmethod
    def Starlight_Instruments_M48_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Spacer_8_5mm'])

    @classmethod
    def Starlight_Instruments_M48_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Spacer_9mm'])

    @classmethod
    def Starlight_Instruments_M48_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Spacer_9_5mm'])

    @classmethod
    def Starlight_Instruments_M48_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Spacer_11mm'])

    @classmethod
    def Starlight_Instruments_M48_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Spacer_12mm'])

    @classmethod
    def Starlight_Instruments_M48_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Spacer_13mm'])

    @classmethod
    def Starlight_Instruments_M48_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Spacer_14mm'])

    @classmethod
    def Starlight_Instruments_M48_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Spacer_16mm'])

    @classmethod
    def Starlight_Instruments_M48_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Spacer_17mm'])

    @classmethod
    def Starlight_Instruments_M48_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Spacer_18mm'])

    @classmethod
    def Starlight_Instruments_M48_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Spacer_22mm'])

    @classmethod
    def Starlight_Instruments_M48_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Spacer_25mm'])

    @classmethod
    def Starlight_Instruments_M42_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Extension_Tube_3mm'])

    @classmethod
    def Starlight_Instruments_M42_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Extension_Tube_6mm'])

    @classmethod
    def Starlight_Instruments_M42_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Extension_Tube_9mm'])

    @classmethod
    def Starlight_Instruments_M42_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Extension_Tube_11mm'])

    @classmethod
    def Starlight_Instruments_M42_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Extension_Tube_13mm'])

    @classmethod
    def Starlight_Instruments_M42_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Extension_Tube_16mm'])

    @classmethod
    def Starlight_Instruments_M42_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Extension_Tube_22mm'])

    @classmethod
    def Starlight_Instruments_M42_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Extension_Tube_28mm'])

    @classmethod
    def Starlight_Instruments_M42_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Extension_Tube_35mm'])

    @classmethod
    def Starlight_Instruments_M42_Extension_Tube_45mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Extension_Tube_45mm'])

    @classmethod
    def Starlight_Instruments_M48_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Extension_Tube_3mm'])

    @classmethod
    def Starlight_Instruments_M48_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Extension_Tube_6mm'])

    @classmethod
    def Starlight_Instruments_M48_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Extension_Tube_9mm'])

    @classmethod
    def Starlight_Instruments_M48_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Extension_Tube_11mm'])

    @classmethod
    def Starlight_Instruments_M48_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Extension_Tube_13mm'])

    @classmethod
    def Starlight_Instruments_M48_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Extension_Tube_16mm'])

    @classmethod
    def Starlight_Instruments_M48_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Extension_Tube_22mm'])

    @classmethod
    def Starlight_Instruments_M48_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Extension_Tube_28mm'])

    @classmethod
    def Starlight_Instruments_M48_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Extension_Tube_35mm'])

    @classmethod
    def Starlight_Instruments_M48_Extension_Tube_45mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Extension_Tube_45mm'])

    @classmethod
    def Starlight_Instruments_M54_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M54_Extension_Tube_3mm'])

    @classmethod
    def Starlight_Instruments_M54_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M54_Extension_Tube_6mm'])

    @classmethod
    def Starlight_Instruments_M54_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M54_Extension_Tube_9mm'])

    @classmethod
    def Starlight_Instruments_M54_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M54_Extension_Tube_11mm'])

    @classmethod
    def Starlight_Instruments_M54_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M54_Extension_Tube_13mm'])

    @classmethod
    def Starlight_Instruments_M54_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M54_Extension_Tube_16mm'])

    @classmethod
    def Starlight_Instruments_M54_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M54_Extension_Tube_22mm'])

    @classmethod
    def Starlight_Instruments_M54_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M54_Extension_Tube_28mm'])

    @classmethod
    def Starlight_Instruments_M54_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M54_Extension_Tube_35mm'])

    @classmethod
    def Starlight_Instruments_M54_Extension_Tube_45mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M54_Extension_Tube_45mm'])

class Starlight_instrumentsSpacer(Spacer):
    _DATABASE = {'Starlight_Instruments_M42_Spacer_0_5mm': {'brand': 'Starlight Instruments', 'name': 'M42 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M42_Spacer_1mm': {'brand': 'Starlight Instruments', 'name': 'M42 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M42_Spacer_2mm': {'brand': 'Starlight Instruments', 'name': 'M42 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M48_Spacer_0_5mm': {'brand': 'Starlight Instruments', 'name': 'M48 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M48_Spacer_1mm': {'brand': 'Starlight Instruments', 'name': 'M48 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M48_Spacer_2mm': {'brand': 'Starlight Instruments', 'name': 'M48 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M42_Spacer_0_25mm': {'brand': 'Starlight Instruments', 'name': 'M42 Spacer 0.25mm', 'type': 'type_spacer', 'optical_length': 0.25, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M42_Spacer_0_75mm': {'brand': 'Starlight Instruments', 'name': 'M42 Spacer 0.75mm', 'type': 'type_spacer', 'optical_length': 0.75, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M42_Spacer_1_5mm': {'brand': 'Starlight Instruments', 'name': 'M42 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M48_Spacer_0_25mm': {'brand': 'Starlight Instruments', 'name': 'M48 Spacer 0.25mm', 'type': 'type_spacer', 'optical_length': 0.25, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M48_Spacer_0_75mm': {'brand': 'Starlight Instruments', 'name': 'M48 Spacer 0.75mm', 'type': 'type_spacer', 'optical_length': 0.75, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Starlight_Instruments_M48_Spacer_1_5mm': {'brand': 'Starlight Instruments', 'name': 'M48 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}}

    @classmethod
    def Starlight_Instruments_M42_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Spacer_0_5mm'])

    @classmethod
    def Starlight_Instruments_M42_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Spacer_1mm'])

    @classmethod
    def Starlight_Instruments_M42_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Spacer_2mm'])

    @classmethod
    def Starlight_Instruments_M48_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Spacer_0_5mm'])

    @classmethod
    def Starlight_Instruments_M48_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Spacer_1mm'])

    @classmethod
    def Starlight_Instruments_M48_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Spacer_2mm'])

    @classmethod
    def Starlight_Instruments_M42_Spacer_0_25mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Spacer_0_25mm'])

    @classmethod
    def Starlight_Instruments_M42_Spacer_0_75mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Spacer_0_75mm'])

    @classmethod
    def Starlight_Instruments_M42_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M42_Spacer_1_5mm'])

    @classmethod
    def Starlight_Instruments_M48_Spacer_0_25mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Spacer_0_25mm'])

    @classmethod
    def Starlight_Instruments_M48_Spacer_0_75mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Spacer_0_75mm'])

    @classmethod
    def Starlight_Instruments_M48_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Starlight_Instruments_M48_Spacer_1_5mm'])