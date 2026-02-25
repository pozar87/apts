from ..base import Adapter, Spacer

class PlanewaveAdapter(Adapter):
    _DATABASE = {'PlaneWave_M117_M68_Adapter': {'brand': 'PlaneWave', 'name': 'M117→M68 Adapter', 'type': 'type_adapter', 'optical_length': 15, 'mass': 60, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'PlaneWave_M117_M54_Adapter': {'brand': 'PlaneWave', 'name': 'M117→M54 Adapter', 'type': 'type_adapter', 'optical_length': 20, 'mass': 55, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'PlaneWave_M117_M42_Adapter': {'brand': 'PlaneWave', 'name': 'M117→M42 Adapter', 'type': 'type_adapter', 'optical_length': 25, 'mass': 50, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'PlaneWave_M117_M82_Adapter': {'brand': 'PlaneWave', 'name': 'M117→M82 Adapter', 'type': 'type_adapter', 'optical_length': 12, 'mass': 55, 'tside_thread': 'M82', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'PlaneWave_M117_EOS_Adapter': {'brand': 'PlaneWave', 'name': 'M117→EOS Adapter', 'type': 'type_adapter', 'optical_length': 20, 'mass': 55, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'PlaneWave_M117_Nikon_F_Adapter': {'brand': 'PlaneWave', 'name': 'M117→Nikon F Adapter', 'type': 'type_adapter', 'optical_length': 18, 'mass': 52, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'PlaneWave_M117_Sony_E_Adapter': {'brand': 'PlaneWave', 'name': 'M117→Sony E Adapter', 'type': 'type_adapter', 'optical_length': 18, 'mass': 50, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'PlaneWave_M117_Canon_RF_Adapter': {'brand': 'PlaneWave', 'name': 'M117→Canon RF Adapter', 'type': 'type_adapter', 'optical_length': 18, 'mass': 50, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'PlaneWave_M117_M92_Adapter': {'brand': 'PlaneWave', 'name': 'M117→M92 Adapter', 'type': 'type_adapter', 'optical_length': 8, 'mass': 48, 'tside_thread': 'M92', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'PlaneWave_M117_M72_Adapter': {'brand': 'PlaneWave', 'name': 'M117→M72 Adapter', 'type': 'type_adapter', 'optical_length': 10, 'mass': 50, 'tside_thread': 'M72', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'PlaneWave_M117_Spacer_3mm': {'brand': 'PlaneWave', 'name': 'M117 Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 24, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PlaneWave_M117_Spacer_4mm': {'brand': 'PlaneWave', 'name': 'M117 Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 25, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PlaneWave_M117_Spacer_5mm': {'brand': 'PlaneWave', 'name': 'M117 Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 26, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PlaneWave_M117_Spacer_6mm': {'brand': 'PlaneWave', 'name': 'M117 Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 26, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PlaneWave_M117_Spacer_7mm': {'brand': 'PlaneWave', 'name': 'M117 Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 27, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PlaneWave_M117_Spacer_8mm': {'brand': 'PlaneWave', 'name': 'M117 Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 28, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PlaneWave_M117_Spacer_9mm': {'brand': 'PlaneWave', 'name': 'M117 Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 29, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PlaneWave_M117_Spacer_10mm': {'brand': 'PlaneWave', 'name': 'M117 Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 30, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PlaneWave_M117_Spacer_12mm': {'brand': 'PlaneWave', 'name': 'M117 Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 31, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PlaneWave_M117_Spacer_15mm': {'brand': 'PlaneWave', 'name': 'M117 Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 34, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PlaneWave_M117_Spacer_18mm': {'brand': 'PlaneWave', 'name': 'M117 Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 36, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PlaneWave_M117_Spacer_20mm': {'brand': 'PlaneWave', 'name': 'M117 Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 38, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PlaneWave_M117_Spacer_25mm': {'brand': 'PlaneWave', 'name': 'M117 Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 42, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PlaneWave_M117_Spacer_30mm': {'brand': 'PlaneWave', 'name': 'M117 Spacer 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 46, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PlaneWave_M117_Spacer_35mm': {'brand': 'PlaneWave', 'name': 'M117 Spacer 35mm', 'type': 'type_adapter', 'optical_length': 35, 'mass': 50, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'PlaneWave_M117_Spacer_40mm': {'brand': 'PlaneWave', 'name': 'M117 Spacer 40mm', 'type': 'type_adapter', 'optical_length': 40, 'mass': 54, 'tside_thread': 'M117', 'tside_gender': 'Female', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}}

    @classmethod
    def PlaneWave_M117_M68_Adapter(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_M117_M68_Adapter'])

    @classmethod
    def PlaneWave_M117_M54_Adapter(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_M117_M54_Adapter'])

    @classmethod
    def PlaneWave_M117_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_M117_M42_Adapter'])

    @classmethod
    def PlaneWave_M117_M82_Adapter(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_M117_M82_Adapter'])

    @classmethod
    def PlaneWave_M117_EOS_Adapter(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_M117_EOS_Adapter'])

    @classmethod
    def PlaneWave_M117_Nikon_F_Adapter(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_M117_Nikon_F_Adapter'])

    @classmethod
    def PlaneWave_M117_Sony_E_Adapter(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_M117_Sony_E_Adapter'])

    @classmethod
    def PlaneWave_M117_Canon_RF_Adapter(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_M117_Canon_RF_Adapter'])

    @classmethod
    def PlaneWave_M117_M92_Adapter(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_M117_M92_Adapter'])

    @classmethod
    def PlaneWave_M117_M72_Adapter(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_M117_M72_Adapter'])

    @classmethod
    def PlaneWave_M117_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_M117_Spacer_3mm'])

    @classmethod
    def PlaneWave_M117_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_M117_Spacer_4mm'])

    @classmethod
    def PlaneWave_M117_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_M117_Spacer_5mm'])

    @classmethod
    def PlaneWave_M117_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_M117_Spacer_6mm'])

    @classmethod
    def PlaneWave_M117_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_M117_Spacer_7mm'])

    @classmethod
    def PlaneWave_M117_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_M117_Spacer_8mm'])

    @classmethod
    def PlaneWave_M117_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_M117_Spacer_9mm'])

    @classmethod
    def PlaneWave_M117_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_M117_Spacer_10mm'])

    @classmethod
    def PlaneWave_M117_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_M117_Spacer_12mm'])

    @classmethod
    def PlaneWave_M117_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_M117_Spacer_15mm'])

    @classmethod
    def PlaneWave_M117_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_M117_Spacer_18mm'])

    @classmethod
    def PlaneWave_M117_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_M117_Spacer_20mm'])

    @classmethod
    def PlaneWave_M117_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_M117_Spacer_25mm'])

    @classmethod
    def PlaneWave_M117_Spacer_30mm(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_M117_Spacer_30mm'])

    @classmethod
    def PlaneWave_M117_Spacer_35mm(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_M117_Spacer_35mm'])

    @classmethod
    def PlaneWave_M117_Spacer_40mm(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_M117_Spacer_40mm'])

class PlanewaveSpacer(Spacer):
    _DATABASE = {'PlaneWave_M117_Spacer_1mm': {'brand': 'PlaneWave', 'name': 'M117 Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 23, 'tside_thread': 'M117', 'tside_gender': '', 'cside_thread': 'M117', 'cside_gender': '', 'reversible': True, 'bf_role': ''}, 'PlaneWave_M117_Spacer_2mm': {'brand': 'PlaneWave', 'name': 'M117 Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 23, 'tside_thread': 'M117', 'tside_gender': '', 'cside_thread': 'M117', 'cside_gender': '', 'reversible': True, 'bf_role': ''}}

    @classmethod
    def PlaneWave_M117_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_M117_Spacer_1mm'])

    @classmethod
    def PlaneWave_M117_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['PlaneWave_M117_Spacer_2mm'])