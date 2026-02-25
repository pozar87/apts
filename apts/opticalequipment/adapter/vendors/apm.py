from ..base import Adapter, Spacer

class ApmAdapter(Adapter):
    _DATABASE = {'APM_M48_Spacer_5mm': {'brand': 'APM', 'name': 'M48 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 10, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'APM_M48_Spacer_10mm': {'brand': 'APM', 'name': 'M48 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 14, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'APM_M48_Spacer_15mm': {'brand': 'APM', 'name': 'M48 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'APM_M48_Spacer_20mm': {'brand': 'APM', 'name': 'M48 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 22, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'APM_M54_Spacer_5mm': {'brand': 'APM', 'name': 'M54 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 12, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'APM_M54_Spacer_10mm': {'brand': 'APM', 'name': 'M54 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 16, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'APM_M54_Spacer_15mm': {'brand': 'APM', 'name': 'M54 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 20, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'APM_M54_Spacer_20mm': {'brand': 'APM', 'name': 'M54 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 24, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'APM_M68_Spacer_5mm': {'brand': 'APM', 'name': 'M68 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 14, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'APM_M68_Spacer_10mm': {'brand': 'APM', 'name': 'M68 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 18, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'APM_M68_Spacer_15mm': {'brand': 'APM', 'name': 'M68 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 22, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'APM_M68_Spacer_20mm': {'brand': 'APM', 'name': 'M68 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 26, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}}

    @classmethod
    def APM_M48_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['APM_M48_Spacer_5mm'])

    @classmethod
    def APM_M48_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['APM_M48_Spacer_10mm'])

    @classmethod
    def APM_M48_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['APM_M48_Spacer_15mm'])

    @classmethod
    def APM_M48_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['APM_M48_Spacer_20mm'])

    @classmethod
    def APM_M54_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['APM_M54_Spacer_5mm'])

    @classmethod
    def APM_M54_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['APM_M54_Spacer_10mm'])

    @classmethod
    def APM_M54_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['APM_M54_Spacer_15mm'])

    @classmethod
    def APM_M54_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['APM_M54_Spacer_20mm'])

    @classmethod
    def APM_M68_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['APM_M68_Spacer_5mm'])

    @classmethod
    def APM_M68_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['APM_M68_Spacer_10mm'])

    @classmethod
    def APM_M68_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['APM_M68_Spacer_15mm'])

    @classmethod
    def APM_M68_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['APM_M68_Spacer_20mm'])

class ApmSpacer(Spacer):
    _DATABASE = {'APM_M48_Spacer_1mm': {'brand': 'APM', 'name': 'M48 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'APM_M48_Spacer_2mm': {'brand': 'APM', 'name': 'M48 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 7, 'tside_thread': 'M48', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'APM_M54_Spacer_1mm': {'brand': 'APM', 'name': 'M54 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'APM_M54_Spacer_2mm': {'brand': 'APM', 'name': 'M54 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 9, 'tside_thread': 'M54', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'APM_M68_Spacer_2mm': {'brand': 'APM', 'name': 'M68 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 11, 'tside_thread': 'M68', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': '', 'reversible': True, 'bf_role': ''}}

    @classmethod
    def APM_M48_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['APM_M48_Spacer_1mm'])

    @classmethod
    def APM_M48_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['APM_M48_Spacer_2mm'])

    @classmethod
    def APM_M54_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['APM_M54_Spacer_1mm'])

    @classmethod
    def APM_M54_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['APM_M54_Spacer_2mm'])

    @classmethod
    def APM_M68_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['APM_M68_Spacer_2mm'])