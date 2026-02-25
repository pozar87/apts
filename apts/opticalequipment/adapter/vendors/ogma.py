from ..base import Adapter, Spacer

class OgmaAdapter(Adapter):
    _DATABASE = {'OGMA_M42_Spacer_5mm': {'brand': 'OGMA', 'name': 'M42 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 8, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'OGMA_M42_Spacer_10mm': {'brand': 'OGMA', 'name': 'M42 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 12, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'OGMA_M42_Spacer_15mm': {'brand': 'OGMA', 'name': 'M42 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'OGMA_M48_Spacer_5mm': {'brand': 'OGMA', 'name': 'M48 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 10, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'OGMA_M48_Spacer_10mm': {'brand': 'OGMA', 'name': 'M48 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 14, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'OGMA_M48_Spacer_15mm': {'brand': 'OGMA', 'name': 'M48 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'OGMA_M42_Spacer_2_5mm': {'brand': 'OGMA', 'name': 'M42 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'OGMA_M42_Spacer_3_5mm': {'brand': 'OGMA', 'name': 'M42 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 6, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'OGMA_M42_Spacer_4_5mm': {'brand': 'OGMA', 'name': 'M42 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 7, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'OGMA_M42_Spacer_5_5mm': {'brand': 'OGMA', 'name': 'M42 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 8, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'OGMA_M42_Spacer_6_5mm': {'brand': 'OGMA', 'name': 'M42 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 9, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'OGMA_M42_Spacer_7_5mm': {'brand': 'OGMA', 'name': 'M42 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 10, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'OGMA_M42_Spacer_8_5mm': {'brand': 'OGMA', 'name': 'M42 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 10, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'OGMA_M42_Spacer_9_5mm': {'brand': 'OGMA', 'name': 'M42 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 11, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'OGMA_M42_Spacer_11mm': {'brand': 'OGMA', 'name': 'M42 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 12, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'OGMA_M42_Spacer_12mm': {'brand': 'OGMA', 'name': 'M42 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 13, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'OGMA_M42_Spacer_13mm': {'brand': 'OGMA', 'name': 'M42 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 14, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'OGMA_M42_Spacer_14mm': {'brand': 'OGMA', 'name': 'M42 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 15, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'OGMA_M42_Spacer_16mm': {'brand': 'OGMA', 'name': 'M42 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 16, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'OGMA_M42_Spacer_17mm': {'brand': 'OGMA', 'name': 'M42 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 17, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'OGMA_M42_Spacer_18mm': {'brand': 'OGMA', 'name': 'M42 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 18, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'OGMA_M42_Spacer_22mm': {'brand': 'OGMA', 'name': 'M42 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 21, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'OGMA_M42_Spacer_25mm': {'brand': 'OGMA', 'name': 'M42 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 24, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'OGMA_M48_Spacer_2_5mm': {'brand': 'OGMA', 'name': 'M48 Spacer 2.5mm', 'type': 'type_adapter', 'optical_length': 2.5, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'OGMA_M48_Spacer_3_5mm': {'brand': 'OGMA', 'name': 'M48 Spacer 3.5mm', 'type': 'type_adapter', 'optical_length': 3.5, 'mass': 8, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'OGMA_M48_Spacer_4_5mm': {'brand': 'OGMA', 'name': 'M48 Spacer 4.5mm', 'type': 'type_adapter', 'optical_length': 4.5, 'mass': 9, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'OGMA_M48_Spacer_5_5mm': {'brand': 'OGMA', 'name': 'M48 Spacer 5.5mm', 'type': 'type_adapter', 'optical_length': 5.5, 'mass': 10, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'OGMA_M48_Spacer_6_5mm': {'brand': 'OGMA', 'name': 'M48 Spacer 6.5mm', 'type': 'type_adapter', 'optical_length': 6.5, 'mass': 11, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'OGMA_M48_Spacer_7_5mm': {'brand': 'OGMA', 'name': 'M48 Spacer 7.5mm', 'type': 'type_adapter', 'optical_length': 7.5, 'mass': 12, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'OGMA_M48_Spacer_8_5mm': {'brand': 'OGMA', 'name': 'M48 Spacer 8.5mm', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 12, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'OGMA_M48_Spacer_9_5mm': {'brand': 'OGMA', 'name': 'M48 Spacer 9.5mm', 'type': 'type_adapter', 'optical_length': 9.5, 'mass': 13, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'OGMA_M48_Spacer_11mm': {'brand': 'OGMA', 'name': 'M48 Spacer 11mm', 'type': 'type_adapter', 'optical_length': 11, 'mass': 14, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'OGMA_M48_Spacer_12mm': {'brand': 'OGMA', 'name': 'M48 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 15, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'OGMA_M48_Spacer_13mm': {'brand': 'OGMA', 'name': 'M48 Spacer 13mm', 'type': 'type_adapter', 'optical_length': 13, 'mass': 16, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'OGMA_M48_Spacer_14mm': {'brand': 'OGMA', 'name': 'M48 Spacer 14mm', 'type': 'type_adapter', 'optical_length': 14, 'mass': 17, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'OGMA_M48_Spacer_16mm': {'brand': 'OGMA', 'name': 'M48 Spacer 16mm', 'type': 'type_adapter', 'optical_length': 16, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'OGMA_M48_Spacer_17mm': {'brand': 'OGMA', 'name': 'M48 Spacer 17mm', 'type': 'type_adapter', 'optical_length': 17, 'mass': 19, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'OGMA_M48_Spacer_18mm': {'brand': 'OGMA', 'name': 'M48 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 20, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'OGMA_M48_Spacer_22mm': {'brand': 'OGMA', 'name': 'M48 Spacer 22mm', 'type': 'type_adapter', 'optical_length': 22, 'mass': 23, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'OGMA_M48_Spacer_25mm': {'brand': 'OGMA', 'name': 'M48 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 26, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}}

    @classmethod
    def OGMA_M42_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M42_Spacer_5mm'])

    @classmethod
    def OGMA_M42_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M42_Spacer_10mm'])

    @classmethod
    def OGMA_M42_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M42_Spacer_15mm'])

    @classmethod
    def OGMA_M48_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M48_Spacer_5mm'])

    @classmethod
    def OGMA_M48_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M48_Spacer_10mm'])

    @classmethod
    def OGMA_M48_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M48_Spacer_15mm'])

    @classmethod
    def OGMA_M42_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M42_Spacer_2_5mm'])

    @classmethod
    def OGMA_M42_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M42_Spacer_3_5mm'])

    @classmethod
    def OGMA_M42_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M42_Spacer_4_5mm'])

    @classmethod
    def OGMA_M42_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M42_Spacer_5_5mm'])

    @classmethod
    def OGMA_M42_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M42_Spacer_6_5mm'])

    @classmethod
    def OGMA_M42_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M42_Spacer_7_5mm'])

    @classmethod
    def OGMA_M42_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M42_Spacer_8_5mm'])

    @classmethod
    def OGMA_M42_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M42_Spacer_9_5mm'])

    @classmethod
    def OGMA_M42_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M42_Spacer_11mm'])

    @classmethod
    def OGMA_M42_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M42_Spacer_12mm'])

    @classmethod
    def OGMA_M42_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M42_Spacer_13mm'])

    @classmethod
    def OGMA_M42_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M42_Spacer_14mm'])

    @classmethod
    def OGMA_M42_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M42_Spacer_16mm'])

    @classmethod
    def OGMA_M42_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M42_Spacer_17mm'])

    @classmethod
    def OGMA_M42_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M42_Spacer_18mm'])

    @classmethod
    def OGMA_M42_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M42_Spacer_22mm'])

    @classmethod
    def OGMA_M42_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M42_Spacer_25mm'])

    @classmethod
    def OGMA_M48_Spacer_2_5mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M48_Spacer_2_5mm'])

    @classmethod
    def OGMA_M48_Spacer_3_5mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M48_Spacer_3_5mm'])

    @classmethod
    def OGMA_M48_Spacer_4_5mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M48_Spacer_4_5mm'])

    @classmethod
    def OGMA_M48_Spacer_5_5mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M48_Spacer_5_5mm'])

    @classmethod
    def OGMA_M48_Spacer_6_5mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M48_Spacer_6_5mm'])

    @classmethod
    def OGMA_M48_Spacer_7_5mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M48_Spacer_7_5mm'])

    @classmethod
    def OGMA_M48_Spacer_8_5mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M48_Spacer_8_5mm'])

    @classmethod
    def OGMA_M48_Spacer_9_5mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M48_Spacer_9_5mm'])

    @classmethod
    def OGMA_M48_Spacer_11mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M48_Spacer_11mm'])

    @classmethod
    def OGMA_M48_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M48_Spacer_12mm'])

    @classmethod
    def OGMA_M48_Spacer_13mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M48_Spacer_13mm'])

    @classmethod
    def OGMA_M48_Spacer_14mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M48_Spacer_14mm'])

    @classmethod
    def OGMA_M48_Spacer_16mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M48_Spacer_16mm'])

    @classmethod
    def OGMA_M48_Spacer_17mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M48_Spacer_17mm'])

    @classmethod
    def OGMA_M48_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M48_Spacer_18mm'])

    @classmethod
    def OGMA_M48_Spacer_22mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M48_Spacer_22mm'])

    @classmethod
    def OGMA_M48_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M48_Spacer_25mm'])

class OgmaSpacer(Spacer):
    _DATABASE = {'OGMA_M42_Spacer_1mm': {'brand': 'OGMA', 'name': 'M42 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'OGMA_M42_Spacer_2mm': {'brand': 'OGMA', 'name': 'M42 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'OGMA_M48_Spacer_1mm': {'brand': 'OGMA', 'name': 'M48 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'OGMA_M48_Spacer_2mm': {'brand': 'OGMA', 'name': 'M48 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'OGMA_M42_Spacer_0_5mm': {'brand': 'OGMA', 'name': 'M42 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'OGMA_M42_Spacer_1_5mm': {'brand': 'OGMA', 'name': 'M42 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 5, 'tside_thread': 'M42', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'OGMA_M48_Spacer_0_5mm': {'brand': 'OGMA', 'name': 'M48 Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'OGMA_M48_Spacer_1_5mm': {'brand': 'OGMA', 'name': 'M48 Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}}

    @classmethod
    def OGMA_M42_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M42_Spacer_1mm'])

    @classmethod
    def OGMA_M42_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M42_Spacer_2mm'])

    @classmethod
    def OGMA_M48_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M48_Spacer_1mm'])

    @classmethod
    def OGMA_M48_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M48_Spacer_2mm'])

    @classmethod
    def OGMA_M42_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M42_Spacer_0_5mm'])

    @classmethod
    def OGMA_M42_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M42_Spacer_1_5mm'])

    @classmethod
    def OGMA_M48_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M48_Spacer_0_5mm'])

    @classmethod
    def OGMA_M48_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['OGMA_M48_Spacer_1_5mm'])