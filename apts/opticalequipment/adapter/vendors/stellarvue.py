from ..base import Adapter, Spacer

class StellarvueAdapter(Adapter):
    _DATABASE = {'Stellarvue_M48_Spacer_5mm': {'brand': 'Stellarvue', 'name': 'M48 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 10, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Stellarvue_M48_Spacer_10mm': {'brand': 'Stellarvue', 'name': 'M48 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 14, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Stellarvue_M48_Spacer_15mm': {'brand': 'Stellarvue', 'name': 'M48 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Stellarvue_M48_Spacer_20mm': {'brand': 'Stellarvue', 'name': 'M48 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 22, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Stellarvue_M54_Spacer_5mm': {'brand': 'Stellarvue', 'name': 'M54 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 12, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Stellarvue_M54_Spacer_10mm': {'brand': 'Stellarvue', 'name': 'M54 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 16, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Stellarvue_M54_Spacer_15mm': {'brand': 'Stellarvue', 'name': 'M54 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 20, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'Stellarvue_M54_Spacer_20mm': {'brand': 'Stellarvue', 'name': 'M54 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 24, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}}

    @classmethod
    def Stellarvue_M48_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_M48_Spacer_5mm'])

    @classmethod
    def Stellarvue_M48_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_M48_Spacer_10mm'])

    @classmethod
    def Stellarvue_M48_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_M48_Spacer_15mm'])

    @classmethod
    def Stellarvue_M48_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_M48_Spacer_20mm'])

    @classmethod
    def Stellarvue_M54_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_M54_Spacer_5mm'])

    @classmethod
    def Stellarvue_M54_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_M54_Spacer_10mm'])

    @classmethod
    def Stellarvue_M54_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_M54_Spacer_15mm'])

    @classmethod
    def Stellarvue_M54_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_M54_Spacer_20mm'])

class StellarvueSpacer(Spacer):
    _DATABASE = {'Stellarvue_M48_Spacer_1mm': {'brand': 'Stellarvue', 'name': 'M48 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Stellarvue_M48_Spacer_2mm': {'brand': 'Stellarvue', 'name': 'M48 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Stellarvue_M54_Spacer_1mm': {'brand': 'Stellarvue', 'name': 'M54 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'Stellarvue_M54_Spacer_2mm': {'brand': 'Stellarvue', 'name': 'M54 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}}

    @classmethod
    def Stellarvue_M48_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_M48_Spacer_1mm'])

    @classmethod
    def Stellarvue_M48_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_M48_Spacer_2mm'])

    @classmethod
    def Stellarvue_M54_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_M54_Spacer_1mm'])

    @classmethod
    def Stellarvue_M54_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_M54_Spacer_2mm'])