from ..base import Adapter, Spacer

class Player_oneAdapter(Adapter):
    _DATABASE = {'Player_One_M42_M54_Adapter_11mm': {'brand': 'Player One', 'name': 'M42→M54 Adapter (11mm)', 'type': 'type_adapter', 'optical_length': 11, 'mass': 30, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Player_One_M42_M48_Adapter_5mm': {'brand': 'Player One', 'name': 'M42→M48 Adapter (5mm)', 'type': 'type_adapter', 'optical_length': 5, 'mass': 20, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Player_One_EOS_M42_Adapter': {'brand': 'Player One', 'name': 'EOS→M42 Adapter', 'type': 'type_adapter', 'optical_length': 11, 'mass': 30, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Player_One_M42_CS_Adapter': {'brand': 'Player One', 'name': 'M42→CS Adapter', 'type': 'type_adapter', 'optical_length': 5, 'mass': 10, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'CS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Player_One_M42_Spacer_5mm': {'brand': 'Player One', 'name': 'M42 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 8, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M42_Spacer_10mm': {'brand': 'Player One', 'name': 'M42 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 12, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M48_Spacer_5mm': {'brand': 'Player One', 'name': 'M48 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 10, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M48_Spacer_10mm': {'brand': 'Player One', 'name': 'M48 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 14, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M54_Spacer_5mm': {'brand': 'Player One', 'name': 'M54 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 12, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M54_Spacer_10mm': {'brand': 'Player One', 'name': 'M54 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 16, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M54_Spacer_15mm': {'brand': 'Player One', 'name': 'M54 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 20, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M42_Spacer_2_5mm': {'brand': 'Player One', 'name': 'M42 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M42_Spacer_3mm': {'brand': 'Player One', 'name': 'M42 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M42_Spacer_3_5mm': {'brand': 'Player One', 'name': 'M42 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M42_Spacer_4mm': {'brand': 'Player One', 'name': 'M42 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 7, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M42_Spacer_4_5mm': {'brand': 'Player One', 'name': 'M42 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 7, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M42_Spacer_5_5mm': {'brand': 'Player One', 'name': 'M42 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 8, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M42_Spacer_6mm': {'brand': 'Player One', 'name': 'M42 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 8, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M42_Spacer_6_5mm': {'brand': 'Player One', 'name': 'M42 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 9, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M42_Spacer_7mm': {'brand': 'Player One', 'name': 'M42 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 9, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M42_Spacer_7_5mm': {'brand': 'Player One', 'name': 'M42 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 10, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M42_Spacer_8mm': {'brand': 'Player One', 'name': 'M42 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 10, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M42_Spacer_8_5mm': {'brand': 'Player One', 'name': 'M42 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 10, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M42_Spacer_9mm': {'brand': 'Player One', 'name': 'M42 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 11, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M42_Spacer_9_5mm': {'brand': 'Player One', 'name': 'M42 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 11, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M42_Spacer_11mm': {'brand': 'Player One', 'name': 'M42 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 12, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M42_Spacer_12mm': {'brand': 'Player One', 'name': 'M42 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 13, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M42_Spacer_13mm': {'brand': 'Player One', 'name': 'M42 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 14, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M42_Spacer_14mm': {'brand': 'Player One', 'name': 'M42 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 15, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M42_Spacer_16mm': {'brand': 'Player One', 'name': 'M42 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M42_Spacer_17mm': {'brand': 'Player One', 'name': 'M42 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 17, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M42_Spacer_18mm': {'brand': 'Player One', 'name': 'M42 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 18, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M42_Spacer_22mm': {'brand': 'Player One', 'name': 'M42 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 21, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M42_Spacer_25mm': {'brand': 'Player One', 'name': 'M42 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 24, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M48_Spacer_2_5mm': {'brand': 'Player One', 'name': 'M48 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M48_Spacer_3mm': {'brand': 'Player One', 'name': 'M48 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M48_Spacer_3_5mm': {'brand': 'Player One', 'name': 'M48 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M48_Spacer_4mm': {'brand': 'Player One', 'name': 'M48 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 9, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M48_Spacer_4_5mm': {'brand': 'Player One', 'name': 'M48 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 9, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M48_Spacer_5_5mm': {'brand': 'Player One', 'name': 'M48 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 10, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M48_Spacer_6mm': {'brand': 'Player One', 'name': 'M48 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 10, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M48_Spacer_6_5mm': {'brand': 'Player One', 'name': 'M48 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 11, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M48_Spacer_7mm': {'brand': 'Player One', 'name': 'M48 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 11, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M48_Spacer_7_5mm': {'brand': 'Player One', 'name': 'M48 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 12, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M48_Spacer_8mm': {'brand': 'Player One', 'name': 'M48 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 12, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M48_Spacer_8_5mm': {'brand': 'Player One', 'name': 'M48 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 12, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M48_Spacer_9mm': {'brand': 'Player One', 'name': 'M48 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 13, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M48_Spacer_9_5mm': {'brand': 'Player One', 'name': 'M48 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 13, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M48_Spacer_11mm': {'brand': 'Player One', 'name': 'M48 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 14, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M48_Spacer_12mm': {'brand': 'Player One', 'name': 'M48 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 15, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M48_Spacer_13mm': {'brand': 'Player One', 'name': 'M48 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 16, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M48_Spacer_14mm': {'brand': 'Player One', 'name': 'M48 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 17, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M48_Spacer_16mm': {'brand': 'Player One', 'name': 'M48 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M48_Spacer_17mm': {'brand': 'Player One', 'name': 'M48 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 19, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M48_Spacer_18mm': {'brand': 'Player One', 'name': 'M48 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 20, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M48_Spacer_22mm': {'brand': 'Player One', 'name': 'M48 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 23, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M48_Spacer_25mm': {'brand': 'Player One', 'name': 'M48 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 26, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M54_Spacer_2_5mm': {'brand': 'Player One', 'name': 'M54 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 10, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M54_Spacer_3mm': {'brand': 'Player One', 'name': 'M54 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 10, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M54_Spacer_3_5mm': {'brand': 'Player One', 'name': 'M54 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 10, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M54_Spacer_4mm': {'brand': 'Player One', 'name': 'M54 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 11, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M54_Spacer_4_5mm': {'brand': 'Player One', 'name': 'M54 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 11, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M54_Spacer_5_5mm': {'brand': 'Player One', 'name': 'M54 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 12, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M54_Spacer_6mm': {'brand': 'Player One', 'name': 'M54 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 12, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M54_Spacer_6_5mm': {'brand': 'Player One', 'name': 'M54 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 13, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M54_Spacer_7mm': {'brand': 'Player One', 'name': 'M54 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 13, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M54_Spacer_7_5mm': {'brand': 'Player One', 'name': 'M54 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 14, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M54_Spacer_8mm': {'brand': 'Player One', 'name': 'M54 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 14, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M54_Spacer_8_5mm': {'brand': 'Player One', 'name': 'M54 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 14, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M54_Spacer_9mm': {'brand': 'Player One', 'name': 'M54 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 15, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M54_Spacer_9_5mm': {'brand': 'Player One', 'name': 'M54 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 15, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M54_Spacer_11mm': {'brand': 'Player One', 'name': 'M54 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 16, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M54_Spacer_12mm': {'brand': 'Player One', 'name': 'M54 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 17, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M54_Spacer_13mm': {'brand': 'Player One', 'name': 'M54 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 18, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M54_Spacer_14mm': {'brand': 'Player One', 'name': 'M54 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 19, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M54_Spacer_16mm': {'brand': 'Player One', 'name': 'M54 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 20, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M54_Spacer_17mm': {'brand': 'Player One', 'name': 'M54 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 21, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M54_Spacer_18mm': {'brand': 'Player One', 'name': 'M54 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 22, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M54_Spacer_22mm': {'brand': 'Player One', 'name': 'M54 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 25, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M54_Spacer_25mm': {'brand': 'Player One', 'name': 'M54 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 28, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Player_One_M42_Extension_Tube_3mm': {'brand': 'Player One', 'name': 'M42 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 10, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Player_One_M42_Extension_Tube_6mm': {'brand': 'Player One', 'name': 'M42 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 11, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Player_One_M42_Extension_Tube_9mm': {'brand': 'Player One', 'name': 'M42 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 12, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Player_One_M42_Extension_Tube_11mm': {'brand': 'Player One', 'name': 'M42 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 13, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Player_One_M42_Extension_Tube_13mm': {'brand': 'Player One', 'name': 'M42 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 13, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Player_One_M42_Extension_Tube_16mm': {'brand': 'Player One', 'name': 'M42 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 14, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Player_One_M42_Extension_Tube_22mm': {'brand': 'Player One', 'name': 'M42 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Player_One_M42_Extension_Tube_28mm': {'brand': 'Player One', 'name': 'M42 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 18, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Player_One_M42_Extension_Tube_35mm': {'brand': 'Player One', 'name': 'M42 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 20, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Player_One_M42_Extension_Tube_45mm': {'brand': 'Player One', 'name': 'M42 Extension Tube 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 23, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Player_One_M48_Extension_Tube_3mm': {'brand': 'Player One', 'name': 'M48 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 14, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Player_One_M48_Extension_Tube_6mm': {'brand': 'Player One', 'name': 'M48 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 15, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Player_One_M48_Extension_Tube_9mm': {'brand': 'Player One', 'name': 'M48 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 16, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Player_One_M48_Extension_Tube_11mm': {'brand': 'Player One', 'name': 'M48 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 17, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Player_One_M48_Extension_Tube_13mm': {'brand': 'Player One', 'name': 'M48 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 17, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Player_One_M48_Extension_Tube_16mm': {'brand': 'Player One', 'name': 'M48 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Player_One_M48_Extension_Tube_22mm': {'brand': 'Player One', 'name': 'M48 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 20, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Player_One_M48_Extension_Tube_28mm': {'brand': 'Player One', 'name': 'M48 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 22, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Player_One_M48_Extension_Tube_35mm': {'brand': 'Player One', 'name': 'M48 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 24, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Player_One_M48_Extension_Tube_45mm': {'brand': 'Player One', 'name': 'M48 Extension Tube 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 27, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Player_One_M54_Extension_Tube_3mm': {'brand': 'Player One', 'name': 'M54 Extension Tube 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 18, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Player_One_M54_Extension_Tube_6mm': {'brand': 'Player One', 'name': 'M54 Extension Tube 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 19, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Player_One_M54_Extension_Tube_9mm': {'brand': 'Player One', 'name': 'M54 Extension Tube 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 20, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Player_One_M54_Extension_Tube_11mm': {'brand': 'Player One', 'name': 'M54 Extension Tube 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 21, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Player_One_M54_Extension_Tube_13mm': {'brand': 'Player One', 'name': 'M54 Extension Tube 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 21, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Player_One_M54_Extension_Tube_16mm': {'brand': 'Player One', 'name': 'M54 Extension Tube 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 22, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Player_One_M54_Extension_Tube_22mm': {'brand': 'Player One', 'name': 'M54 Extension Tube 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 24, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Player_One_M54_Extension_Tube_28mm': {'brand': 'Player One', 'name': 'M54 Extension Tube 28mm', 'type': 'type_adapter', 'optical_length': 28, 'mass': 26, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Player_One_M54_Extension_Tube_35mm': {'brand': 'Player One', 'name': 'M54 Extension Tube 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 28, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Player_One_M54_Extension_Tube_45mm': {'brand': 'Player One', 'name': 'M54 Extension Tube 45mm', 'type': 'type_adapter', 'optical_length': 45, 'mass': 31, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Player_One_M42_M54_Adapter_11mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_M54_Adapter_11mm'])

    @classmethod
    def Player_One_M42_M48_Adapter_5mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_M48_Adapter_5mm'])

    @classmethod
    def Player_One_EOS_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['Player_One_EOS_M42_Adapter'])

    @classmethod
    def Player_One_M42_CS_Adapter(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_CS_Adapter'])

    @classmethod
    def Player_One_M42_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_Spacer_5mm'])

    @classmethod
    def Player_One_M42_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_Spacer_10mm'])

    @classmethod
    def Player_One_M48_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M48_Spacer_5mm'])

    @classmethod
    def Player_One_M48_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M48_Spacer_10mm'])

    @classmethod
    def Player_One_M54_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M54_Spacer_5mm'])

    @classmethod
    def Player_One_M54_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M54_Spacer_10mm'])

    @classmethod
    def Player_One_M54_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M54_Spacer_15mm'])

    @classmethod
    def Player_One_M42_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_Spacer_2_5mm'])

    @classmethod
    def Player_One_M42_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_Spacer_3mm'])

    @classmethod
    def Player_One_M42_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_Spacer_3_5mm'])

    @classmethod
    def Player_One_M42_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_Spacer_4mm'])

    @classmethod
    def Player_One_M42_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_Spacer_4_5mm'])

    @classmethod
    def Player_One_M42_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_Spacer_5_5mm'])

    @classmethod
    def Player_One_M42_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_Spacer_6mm'])

    @classmethod
    def Player_One_M42_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_Spacer_6_5mm'])

    @classmethod
    def Player_One_M42_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_Spacer_7mm'])

    @classmethod
    def Player_One_M42_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_Spacer_7_5mm'])

    @classmethod
    def Player_One_M42_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_Spacer_8mm'])

    @classmethod
    def Player_One_M42_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_Spacer_8_5mm'])

    @classmethod
    def Player_One_M42_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_Spacer_9mm'])

    @classmethod
    def Player_One_M42_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_Spacer_9_5mm'])

    @classmethod
    def Player_One_M42_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_Spacer_11mm'])

    @classmethod
    def Player_One_M42_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_Spacer_12mm'])

    @classmethod
    def Player_One_M42_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_Spacer_13mm'])

    @classmethod
    def Player_One_M42_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_Spacer_14mm'])

    @classmethod
    def Player_One_M42_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_Spacer_16mm'])

    @classmethod
    def Player_One_M42_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_Spacer_17mm'])

    @classmethod
    def Player_One_M42_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_Spacer_18mm'])

    @classmethod
    def Player_One_M42_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_Spacer_22mm'])

    @classmethod
    def Player_One_M42_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_Spacer_25mm'])

    @classmethod
    def Player_One_M48_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M48_Spacer_2_5mm'])

    @classmethod
    def Player_One_M48_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M48_Spacer_3mm'])

    @classmethod
    def Player_One_M48_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M48_Spacer_3_5mm'])

    @classmethod
    def Player_One_M48_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M48_Spacer_4mm'])

    @classmethod
    def Player_One_M48_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M48_Spacer_4_5mm'])

    @classmethod
    def Player_One_M48_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M48_Spacer_5_5mm'])

    @classmethod
    def Player_One_M48_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M48_Spacer_6mm'])

    @classmethod
    def Player_One_M48_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M48_Spacer_6_5mm'])

    @classmethod
    def Player_One_M48_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M48_Spacer_7mm'])

    @classmethod
    def Player_One_M48_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M48_Spacer_7_5mm'])

    @classmethod
    def Player_One_M48_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M48_Spacer_8mm'])

    @classmethod
    def Player_One_M48_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M48_Spacer_8_5mm'])

    @classmethod
    def Player_One_M48_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M48_Spacer_9mm'])

    @classmethod
    def Player_One_M48_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M48_Spacer_9_5mm'])

    @classmethod
    def Player_One_M48_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M48_Spacer_11mm'])

    @classmethod
    def Player_One_M48_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M48_Spacer_12mm'])

    @classmethod
    def Player_One_M48_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M48_Spacer_13mm'])

    @classmethod
    def Player_One_M48_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M48_Spacer_14mm'])

    @classmethod
    def Player_One_M48_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M48_Spacer_16mm'])

    @classmethod
    def Player_One_M48_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M48_Spacer_17mm'])

    @classmethod
    def Player_One_M48_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M48_Spacer_18mm'])

    @classmethod
    def Player_One_M48_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M48_Spacer_22mm'])

    @classmethod
    def Player_One_M48_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M48_Spacer_25mm'])

    @classmethod
    def Player_One_M54_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M54_Spacer_2_5mm'])

    @classmethod
    def Player_One_M54_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M54_Spacer_3mm'])

    @classmethod
    def Player_One_M54_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M54_Spacer_3_5mm'])

    @classmethod
    def Player_One_M54_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M54_Spacer_4mm'])

    @classmethod
    def Player_One_M54_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M54_Spacer_4_5mm'])

    @classmethod
    def Player_One_M54_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M54_Spacer_5_5mm'])

    @classmethod
    def Player_One_M54_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M54_Spacer_6mm'])

    @classmethod
    def Player_One_M54_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M54_Spacer_6_5mm'])

    @classmethod
    def Player_One_M54_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M54_Spacer_7mm'])

    @classmethod
    def Player_One_M54_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M54_Spacer_7_5mm'])

    @classmethod
    def Player_One_M54_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M54_Spacer_8mm'])

    @classmethod
    def Player_One_M54_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M54_Spacer_8_5mm'])

    @classmethod
    def Player_One_M54_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M54_Spacer_9mm'])

    @classmethod
    def Player_One_M54_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M54_Spacer_9_5mm'])

    @classmethod
    def Player_One_M54_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M54_Spacer_11mm'])

    @classmethod
    def Player_One_M54_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M54_Spacer_12mm'])

    @classmethod
    def Player_One_M54_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M54_Spacer_13mm'])

    @classmethod
    def Player_One_M54_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M54_Spacer_14mm'])

    @classmethod
    def Player_One_M54_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M54_Spacer_16mm'])

    @classmethod
    def Player_One_M54_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M54_Spacer_17mm'])

    @classmethod
    def Player_One_M54_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M54_Spacer_18mm'])

    @classmethod
    def Player_One_M54_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M54_Spacer_22mm'])

    @classmethod
    def Player_One_M54_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M54_Spacer_25mm'])

    @classmethod
    def Player_One_M42_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_Extension_Tube_3mm'])

    @classmethod
    def Player_One_M42_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_Extension_Tube_6mm'])

    @classmethod
    def Player_One_M42_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_Extension_Tube_9mm'])

    @classmethod
    def Player_One_M42_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_Extension_Tube_11mm'])

    @classmethod
    def Player_One_M42_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_Extension_Tube_13mm'])

    @classmethod
    def Player_One_M42_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_Extension_Tube_16mm'])

    @classmethod
    def Player_One_M42_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_Extension_Tube_22mm'])

    @classmethod
    def Player_One_M42_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_Extension_Tube_28mm'])

    @classmethod
    def Player_One_M42_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_Extension_Tube_35mm'])

    @classmethod
    def Player_One_M42_Extension_Tube_45mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_Extension_Tube_45mm'])

    @classmethod
    def Player_One_M48_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M48_Extension_Tube_3mm'])

    @classmethod
    def Player_One_M48_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M48_Extension_Tube_6mm'])

    @classmethod
    def Player_One_M48_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M48_Extension_Tube_9mm'])

    @classmethod
    def Player_One_M48_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M48_Extension_Tube_11mm'])

    @classmethod
    def Player_One_M48_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M48_Extension_Tube_13mm'])

    @classmethod
    def Player_One_M48_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M48_Extension_Tube_16mm'])

    @classmethod
    def Player_One_M48_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M48_Extension_Tube_22mm'])

    @classmethod
    def Player_One_M48_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M48_Extension_Tube_28mm'])

    @classmethod
    def Player_One_M48_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M48_Extension_Tube_35mm'])

    @classmethod
    def Player_One_M48_Extension_Tube_45mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M48_Extension_Tube_45mm'])

    @classmethod
    def Player_One_M54_Extension_Tube_3mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M54_Extension_Tube_3mm'])

    @classmethod
    def Player_One_M54_Extension_Tube_6mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M54_Extension_Tube_6mm'])

    @classmethod
    def Player_One_M54_Extension_Tube_9mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M54_Extension_Tube_9mm'])

    @classmethod
    def Player_One_M54_Extension_Tube_11mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M54_Extension_Tube_11mm'])

    @classmethod
    def Player_One_M54_Extension_Tube_13mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M54_Extension_Tube_13mm'])

    @classmethod
    def Player_One_M54_Extension_Tube_16mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M54_Extension_Tube_16mm'])

    @classmethod
    def Player_One_M54_Extension_Tube_22mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M54_Extension_Tube_22mm'])

    @classmethod
    def Player_One_M54_Extension_Tube_28mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M54_Extension_Tube_28mm'])

    @classmethod
    def Player_One_M54_Extension_Tube_35mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M54_Extension_Tube_35mm'])

    @classmethod
    def Player_One_M54_Extension_Tube_45mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M54_Extension_Tube_45mm'])

class Player_oneSpacer(Spacer):
    _DATABASE = {'Player_One_M42_Spacer_1mm': {'brand': 'Player One', 'name': 'M42 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Player_One_M42_Spacer_2mm': {'brand': 'Player One', 'name': 'M42 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Player_One_M48_Spacer_1mm': {'brand': 'Player One', 'name': 'M48 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Player_One_M48_Spacer_2mm': {'brand': 'Player One', 'name': 'M48 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Player_One_M54_Spacer_1mm': {'brand': 'Player One', 'name': 'M54 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Player_One_M54_Spacer_2mm': {'brand': 'Player One', 'name': 'M54 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Player_One_M42_Spacer_0_5mm': {'brand': 'Player One', 'name': 'M42 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Player_One_M42_Spacer_0_7mm': {'brand': 'Player One', 'name': 'M42 Spacer 0.7mm', 'type': 'type_spacer', 'optical_length': 0.7, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Player_One_M42_Spacer_1_5mm': {'brand': 'Player One', 'name': 'M42 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Player_One_M48_Spacer_0_5mm': {'brand': 'Player One', 'name': 'M48 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Player_One_M48_Spacer_0_7mm': {'brand': 'Player One', 'name': 'M48 Spacer 0.7mm', 'type': 'type_spacer', 'optical_length': 0.7, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Player_One_M48_Spacer_1_5mm': {'brand': 'Player One', 'name': 'M48 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Player_One_M54_Spacer_0_5mm': {'brand': 'Player One', 'name': 'M54 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Player_One_M54_Spacer_0_7mm': {'brand': 'Player One', 'name': 'M54 Spacer 0.7mm', 'type': 'type_spacer', 'optical_length': 0.7, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Player_One_M54_Spacer_1_5mm': {'brand': 'Player One', 'name': 'M54 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}}

    @classmethod
    def Player_One_M42_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_Spacer_1mm'])

    @classmethod
    def Player_One_M42_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_Spacer_2mm'])

    @classmethod
    def Player_One_M48_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M48_Spacer_1mm'])

    @classmethod
    def Player_One_M48_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M48_Spacer_2mm'])

    @classmethod
    def Player_One_M54_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M54_Spacer_1mm'])

    @classmethod
    def Player_One_M54_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M54_Spacer_2mm'])

    @classmethod
    def Player_One_M42_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_Spacer_0_5mm'])

    @classmethod
    def Player_One_M42_Spacer_0_7mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_Spacer_0_7mm'])

    @classmethod
    def Player_One_M42_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M42_Spacer_1_5mm'])

    @classmethod
    def Player_One_M48_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M48_Spacer_0_5mm'])

    @classmethod
    def Player_One_M48_Spacer_0_7mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M48_Spacer_0_7mm'])

    @classmethod
    def Player_One_M48_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M48_Spacer_1_5mm'])

    @classmethod
    def Player_One_M54_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M54_Spacer_0_5mm'])

    @classmethod
    def Player_One_M54_Spacer_0_7mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M54_Spacer_0_7mm'])

    @classmethod
    def Player_One_M54_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_M54_Spacer_1_5mm'])