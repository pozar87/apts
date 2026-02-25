from ...abstract import IntermediateOpticalEquipment
from ....constants import OpticalType
from ..base import Adapter, Spacer

class AntliaAdapter(Adapter):
    _DATABASE = {'Antlia_M42_Spacer_2_5mm': {'brand': 'Antlia', 'name': 'M42 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M42_Spacer_3mm': {'brand': 'Antlia', 'name': 'M42 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M42_Spacer_3_5mm': {'brand': 'Antlia', 'name': 'M42 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M42_Spacer_4mm': {'brand': 'Antlia', 'name': 'M42 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 7, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M42_Spacer_5mm': {'brand': 'Antlia', 'name': 'M42 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 8, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M42_Spacer_6mm': {'brand': 'Antlia', 'name': 'M42 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 8, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M42_Spacer_7mm': {'brand': 'Antlia', 'name': 'M42 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 9, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M42_Spacer_8mm': {'brand': 'Antlia', 'name': 'M42 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 10, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M42_Spacer_9mm': {'brand': 'Antlia', 'name': 'M42 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 11, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M42_Spacer_10mm': {'brand': 'Antlia', 'name': 'M42 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 12, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M42_Spacer_11mm': {'brand': 'Antlia', 'name': 'M42 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 12, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M42_Spacer_12mm': {'brand': 'Antlia', 'name': 'M42 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 13, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M42_Spacer_13mm': {'brand': 'Antlia', 'name': 'M42 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 14, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M42_Spacer_14mm': {'brand': 'Antlia', 'name': 'M42 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 15, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M42_Spacer_15mm': {'brand': 'Antlia', 'name': 'M42 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M42_Spacer_16mm': {'brand': 'Antlia', 'name': 'M42 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M42_Spacer_17mm': {'brand': 'Antlia', 'name': 'M42 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 17, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M42_Spacer_18mm': {'brand': 'Antlia', 'name': 'M42 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 18, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M42_Spacer_20mm': {'brand': 'Antlia', 'name': 'M42 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 20, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M42_Spacer_22mm': {'brand': 'Antlia', 'name': 'M42 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 21, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M42_Spacer_25mm': {'brand': 'Antlia', 'name': 'M42 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 24, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M48_Spacer_2_5mm': {'brand': 'Antlia', 'name': 'M48 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M48_Spacer_3mm': {'brand': 'Antlia', 'name': 'M48 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M48_Spacer_3_5mm': {'brand': 'Antlia', 'name': 'M48 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M48_Spacer_4mm': {'brand': 'Antlia', 'name': 'M48 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 9, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M48_Spacer_5mm': {'brand': 'Antlia', 'name': 'M48 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 10, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M48_Spacer_6mm': {'brand': 'Antlia', 'name': 'M48 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 10, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M48_Spacer_7mm': {'brand': 'Antlia', 'name': 'M48 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 11, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M48_Spacer_8mm': {'brand': 'Antlia', 'name': 'M48 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 12, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M48_Spacer_9mm': {'brand': 'Antlia', 'name': 'M48 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 13, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M48_Spacer_10mm': {'brand': 'Antlia', 'name': 'M48 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 14, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M48_Spacer_11mm': {'brand': 'Antlia', 'name': 'M48 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 14, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M48_Spacer_12mm': {'brand': 'Antlia', 'name': 'M48 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 15, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M48_Spacer_13mm': {'brand': 'Antlia', 'name': 'M48 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 16, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M48_Spacer_14mm': {'brand': 'Antlia', 'name': 'M48 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 17, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M48_Spacer_15mm': {'brand': 'Antlia', 'name': 'M48 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M48_Spacer_16mm': {'brand': 'Antlia', 'name': 'M48 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M48_Spacer_17mm': {'brand': 'Antlia', 'name': 'M48 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 19, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M48_Spacer_18mm': {'brand': 'Antlia', 'name': 'M48 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 20, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M48_Spacer_20mm': {'brand': 'Antlia', 'name': 'M48 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 22, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M48_Spacer_22mm': {'brand': 'Antlia', 'name': 'M48 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 23, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M48_Spacer_25mm': {'brand': 'Antlia', 'name': 'M48 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 26, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M54_Spacer_3mm': {'brand': 'Antlia', 'name': 'M54 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 10, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M54_Spacer_4mm': {'brand': 'Antlia', 'name': 'M54 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 11, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M54_Spacer_5mm': {'brand': 'Antlia', 'name': 'M54 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 12, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M54_Spacer_6mm': {'brand': 'Antlia', 'name': 'M54 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 12, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M54_Spacer_7mm': {'brand': 'Antlia', 'name': 'M54 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 13, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M54_Spacer_8mm': {'brand': 'Antlia', 'name': 'M54 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 14, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M54_Spacer_9mm': {'brand': 'Antlia', 'name': 'M54 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 15, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M54_Spacer_10mm': {'brand': 'Antlia', 'name': 'M54 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 16, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M54_Spacer_11mm': {'brand': 'Antlia', 'name': 'M54 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 16, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M54_Spacer_12mm': {'brand': 'Antlia', 'name': 'M54 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 17, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M54_Spacer_13mm': {'brand': 'Antlia', 'name': 'M54 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 18, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M54_Spacer_14mm': {'brand': 'Antlia', 'name': 'M54 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 19, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M54_Spacer_15mm': {'brand': 'Antlia', 'name': 'M54 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 20, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M54_Spacer_16mm': {'brand': 'Antlia', 'name': 'M54 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 20, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M54_Spacer_17mm': {'brand': 'Antlia', 'name': 'M54 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 21, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M54_Spacer_18mm': {'brand': 'Antlia', 'name': 'M54 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 22, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M54_Spacer_20mm': {'brand': 'Antlia', 'name': 'M54 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 24, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M54_Spacer_22mm': {'brand': 'Antlia', 'name': 'M54 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 25, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Antlia_M54_Spacer_25mm': {'brand': 'Antlia', 'name': 'M54 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 28, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}}

    @classmethod
    def Antlia_M42_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M42_Spacer_2_5mm'])

    @classmethod
    def Antlia_M42_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M42_Spacer_3mm'])

    @classmethod
    def Antlia_M42_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M42_Spacer_3_5mm'])

    @classmethod
    def Antlia_M42_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M42_Spacer_4mm'])

    @classmethod
    def Antlia_M42_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M42_Spacer_5mm'])

    @classmethod
    def Antlia_M42_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M42_Spacer_6mm'])

    @classmethod
    def Antlia_M42_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M42_Spacer_7mm'])

    @classmethod
    def Antlia_M42_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M42_Spacer_8mm'])

    @classmethod
    def Antlia_M42_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M42_Spacer_9mm'])

    @classmethod
    def Antlia_M42_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M42_Spacer_10mm'])

    @classmethod
    def Antlia_M42_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M42_Spacer_11mm'])

    @classmethod
    def Antlia_M42_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M42_Spacer_12mm'])

    @classmethod
    def Antlia_M42_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M42_Spacer_13mm'])

    @classmethod
    def Antlia_M42_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M42_Spacer_14mm'])

    @classmethod
    def Antlia_M42_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M42_Spacer_15mm'])

    @classmethod
    def Antlia_M42_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M42_Spacer_16mm'])

    @classmethod
    def Antlia_M42_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M42_Spacer_17mm'])

    @classmethod
    def Antlia_M42_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M42_Spacer_18mm'])

    @classmethod
    def Antlia_M42_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M42_Spacer_20mm'])

    @classmethod
    def Antlia_M42_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M42_Spacer_22mm'])

    @classmethod
    def Antlia_M42_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M42_Spacer_25mm'])

    @classmethod
    def Antlia_M48_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M48_Spacer_2_5mm'])

    @classmethod
    def Antlia_M48_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M48_Spacer_3mm'])

    @classmethod
    def Antlia_M48_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M48_Spacer_3_5mm'])

    @classmethod
    def Antlia_M48_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M48_Spacer_4mm'])

    @classmethod
    def Antlia_M48_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M48_Spacer_5mm'])

    @classmethod
    def Antlia_M48_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M48_Spacer_6mm'])

    @classmethod
    def Antlia_M48_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M48_Spacer_7mm'])

    @classmethod
    def Antlia_M48_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M48_Spacer_8mm'])

    @classmethod
    def Antlia_M48_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M48_Spacer_9mm'])

    @classmethod
    def Antlia_M48_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M48_Spacer_10mm'])

    @classmethod
    def Antlia_M48_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M48_Spacer_11mm'])

    @classmethod
    def Antlia_M48_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M48_Spacer_12mm'])

    @classmethod
    def Antlia_M48_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M48_Spacer_13mm'])

    @classmethod
    def Antlia_M48_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M48_Spacer_14mm'])

    @classmethod
    def Antlia_M48_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M48_Spacer_15mm'])

    @classmethod
    def Antlia_M48_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M48_Spacer_16mm'])

    @classmethod
    def Antlia_M48_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M48_Spacer_17mm'])

    @classmethod
    def Antlia_M48_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M48_Spacer_18mm'])

    @classmethod
    def Antlia_M48_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M48_Spacer_20mm'])

    @classmethod
    def Antlia_M48_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M48_Spacer_22mm'])

    @classmethod
    def Antlia_M48_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M48_Spacer_25mm'])

    @classmethod
    def Antlia_M54_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M54_Spacer_3mm'])

    @classmethod
    def Antlia_M54_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M54_Spacer_4mm'])

    @classmethod
    def Antlia_M54_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M54_Spacer_5mm'])

    @classmethod
    def Antlia_M54_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M54_Spacer_6mm'])

    @classmethod
    def Antlia_M54_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M54_Spacer_7mm'])

    @classmethod
    def Antlia_M54_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M54_Spacer_8mm'])

    @classmethod
    def Antlia_M54_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M54_Spacer_9mm'])

    @classmethod
    def Antlia_M54_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M54_Spacer_10mm'])

    @classmethod
    def Antlia_M54_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M54_Spacer_11mm'])

    @classmethod
    def Antlia_M54_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M54_Spacer_12mm'])

    @classmethod
    def Antlia_M54_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M54_Spacer_13mm'])

    @classmethod
    def Antlia_M54_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M54_Spacer_14mm'])

    @classmethod
    def Antlia_M54_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M54_Spacer_15mm'])

    @classmethod
    def Antlia_M54_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M54_Spacer_16mm'])

    @classmethod
    def Antlia_M54_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M54_Spacer_17mm'])

    @classmethod
    def Antlia_M54_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M54_Spacer_18mm'])

    @classmethod
    def Antlia_M54_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M54_Spacer_20mm'])

    @classmethod
    def Antlia_M54_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M54_Spacer_22mm'])

    @classmethod
    def Antlia_M54_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M54_Spacer_25mm'])

class AntliaSpacer(Spacer):
    _DATABASE = {'Antlia_M42_Spacer_0_5mm': {'brand': 'Antlia', 'name': 'M42 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Antlia_M42_Spacer_1mm': {'brand': 'Antlia', 'name': 'M42 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Antlia_M42_Spacer_1_5mm': {'brand': 'Antlia', 'name': 'M42 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Antlia_M42_Spacer_2mm': {'brand': 'Antlia', 'name': 'M42 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Antlia_M48_Spacer_0_5mm': {'brand': 'Antlia', 'name': 'M48 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Antlia_M48_Spacer_1mm': {'brand': 'Antlia', 'name': 'M48 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Antlia_M48_Spacer_1_5mm': {'brand': 'Antlia', 'name': 'M48 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Antlia_M48_Spacer_2mm': {'brand': 'Antlia', 'name': 'M48 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Antlia_M54_Spacer_0_5mm': {'brand': 'Antlia', 'name': 'M54 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Antlia_M54_Spacer_1mm': {'brand': 'Antlia', 'name': 'M54 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Antlia_M54_Spacer_1_5mm': {'brand': 'Antlia', 'name': 'M54 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Antlia_M54_Spacer_2mm': {'brand': 'Antlia', 'name': 'M54 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}}

    @classmethod
    def Antlia_M42_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M42_Spacer_0_5mm'])

    @classmethod
    def Antlia_M42_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M42_Spacer_1mm'])

    @classmethod
    def Antlia_M42_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M42_Spacer_1_5mm'])

    @classmethod
    def Antlia_M42_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M42_Spacer_2mm'])

    @classmethod
    def Antlia_M48_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M48_Spacer_0_5mm'])

    @classmethod
    def Antlia_M48_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M48_Spacer_1mm'])

    @classmethod
    def Antlia_M48_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M48_Spacer_1_5mm'])

    @classmethod
    def Antlia_M48_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M48_Spacer_2mm'])

    @classmethod
    def Antlia_M54_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M54_Spacer_0_5mm'])

    @classmethod
    def Antlia_M54_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M54_Spacer_1mm'])

    @classmethod
    def Antlia_M54_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M54_Spacer_1_5mm'])

    @classmethod
    def Antlia_M54_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Antlia_M54_Spacer_2mm'])