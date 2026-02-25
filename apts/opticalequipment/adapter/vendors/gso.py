from ...abstract import IntermediateOpticalEquipment
from ....constants import OpticalType
from ..base import Adapter, Spacer

class GsoAdapter(Adapter):
    _DATABASE = {'GSO_SC_M42_T_Adapter': {'brand': 'GSO', 'name': 'SC→M42 T-Adapter', 'type': 'type_adapter', 'optical_length': 30, 'mass': 55, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'GSO_SC_2_Visual_Back': {'brand': 'GSO', 'name': 'SC→2" Visual Back', 'type': 'type_adapter', 'optical_length': 35, 'mass': 60, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'GSO_SC_1_25_Visual_Back': {'brand': 'GSO', 'name': 'SC→1.25" Visual Back', 'type': 'type_adapter', 'optical_length': 30, 'mass': 40, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'GSO_SC_Schmidt_Cassegrain_Spacer_5mm': {'brand': 'GSO', 'name': 'SC (Schmidt-Cassegrain) Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 24, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'GSO_SC_Schmidt_Cassegrain_Spacer_10mm': {'brand': 'GSO', 'name': 'SC (Schmidt-Cassegrain) Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 28, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'GSO_SC_Schmidt_Cassegrain_Spacer_20mm': {'brand': 'GSO', 'name': 'SC (Schmidt-Cassegrain) Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 36, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'GSO_SC_Schmidt_Cassegrain_Spacer_30mm': {'brand': 'GSO', 'name': 'SC (Schmidt-Cassegrain) Spacer 30mm', 'type': 'type_adapter', 'optical_length': 30, 'mass': 44, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'GSO_SC_Schmidt_Cassegrain_Spacer_40mm': {'brand': 'GSO', 'name': 'SC (Schmidt-Cassegrain) Spacer 40mm', 'type': 'type_adapter', 'optical_length': 40, 'mass': 52, 'tside_thread': 'SC (Schmidt-Cassegrain)', 'tside_gender': 'Female', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'GSO_2_1_25_Adapter': {'brand': 'GSO', 'name': '2"→1.25" Adapter', 'type': 'type_adapter', 'optical_length': 0, 'mass': 10, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'GSO_M42_M48_Adapter': {'brand': 'GSO', 'name': 'M42→M48 Adapter', 'type': 'type_adapter', 'optical_length': 5, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'GSO_M48_M54_Adapter': {'brand': 'GSO', 'name': 'M48→M54 Adapter', 'type': 'type_adapter', 'optical_length': 7, 'mass': 22, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'GSO_M42_M54_Adapter': {'brand': 'GSO', 'name': 'M42→M54 Adapter', 'type': 'type_adapter', 'optical_length': 10, 'mass': 22, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'GSO_M54_M68_Adapter': {'brand': 'GSO', 'name': 'M54→M68 Adapter', 'type': 'type_adapter', 'optical_length': 8, 'mass': 28, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'GSO_M48_M42_Adapter': {'brand': 'GSO', 'name': 'M48→M42 Adapter', 'type': 'type_adapter', 'optical_length': 5, 'mass': 18, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'GSO_M72_M68_Adapter': {'brand': 'GSO', 'name': 'M72→M68 Adapter', 'type': 'type_adapter', 'optical_length': 5, 'mass': 32, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'GSO_M72_M54_Adapter': {'brand': 'GSO', 'name': 'M72→M54 Adapter', 'type': 'type_adapter', 'optical_length': 8, 'mass': 30, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'GSO_M72_M42_Adapter': {'brand': 'GSO', 'name': 'M72→M42 Adapter', 'type': 'type_adapter', 'optical_length': 12, 'mass': 28, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'GSO_EOS_M42_T_Ring': {'brand': 'GSO', 'name': 'EOS→M42 T-Ring', 'type': 'type_adapter', 'optical_length': 10.5, 'mass': 28, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'GSO_Nikon_F_M42_T_Ring': {'brand': 'GSO', 'name': 'Nikon F→M42 T-Ring', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 28, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'GSO_Sony_E_M42_Adapter': {'brand': 'GSO', 'name': 'Sony E→M42 Adapter', 'type': 'type_adapter', 'optical_length': 7, 'mass': 22, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'GSO_1_25_Spacer_3mm': {'brand': 'GSO', 'name': '1.25" Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 5, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'GSO_1_25_Spacer_4mm': {'brand': 'GSO', 'name': '1.25" Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 6, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'GSO_1_25_Spacer_5mm': {'brand': 'GSO', 'name': '1.25" Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 7, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'GSO_1_25_Spacer_6mm': {'brand': 'GSO', 'name': '1.25" Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 7, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'GSO_1_25_Spacer_7mm': {'brand': 'GSO', 'name': '1.25" Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 8, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'GSO_1_25_Spacer_8mm': {'brand': 'GSO', 'name': '1.25" Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 9, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'GSO_1_25_Spacer_9mm': {'brand': 'GSO', 'name': '1.25" Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 10, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'GSO_1_25_Spacer_10mm': {'brand': 'GSO', 'name': '1.25" Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 11, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'GSO_1_25_Spacer_12mm': {'brand': 'GSO', 'name': '1.25" Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 12, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'GSO_1_25_Spacer_15mm': {'brand': 'GSO', 'name': '1.25" Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 15, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'GSO_1_25_Spacer_18mm': {'brand': 'GSO', 'name': '1.25" Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 17, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'GSO_1_25_Spacer_20mm': {'brand': 'GSO', 'name': '1.25" Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 19, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'GSO_1_25_Spacer_25mm': {'brand': 'GSO', 'name': '1.25" Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 23, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'GSO_2_Spacer_3mm': {'brand': 'GSO', 'name': '2" Spacer 3mm', 'type': 'type_adapter', 'optical_length': 3, 'mass': 10, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'GSO_2_Spacer_4mm': {'brand': 'GSO', 'name': '2" Spacer 4mm', 'type': 'type_adapter', 'optical_length': 4, 'mass': 11, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'GSO_2_Spacer_5mm': {'brand': 'GSO', 'name': '2" Spacer 5mm', 'type': 'type_adapter', 'optical_length': 5, 'mass': 12, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'GSO_2_Spacer_6mm': {'brand': 'GSO', 'name': '2" Spacer 6mm', 'type': 'type_adapter', 'optical_length': 6, 'mass': 12, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'GSO_2_Spacer_7mm': {'brand': 'GSO', 'name': '2" Spacer 7mm', 'type': 'type_adapter', 'optical_length': 7, 'mass': 13, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'GSO_2_Spacer_8mm': {'brand': 'GSO', 'name': '2" Spacer 8mm', 'type': 'type_adapter', 'optical_length': 8, 'mass': 14, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'GSO_2_Spacer_9mm': {'brand': 'GSO', 'name': '2" Spacer 9mm', 'type': 'type_adapter', 'optical_length': 9, 'mass': 15, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'GSO_2_Spacer_10mm': {'brand': 'GSO', 'name': '2" Spacer 10mm', 'type': 'type_adapter', 'optical_length': 10, 'mass': 16, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'GSO_2_Spacer_12mm': {'brand': 'GSO', 'name': '2" Spacer 12mm', 'type': 'type_adapter', 'optical_length': 12, 'mass': 17, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'GSO_2_Spacer_15mm': {'brand': 'GSO', 'name': '2" Spacer 15mm', 'type': 'type_adapter', 'optical_length': 15, 'mass': 20, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'GSO_2_Spacer_18mm': {'brand': 'GSO', 'name': '2" Spacer 18mm', 'type': 'type_adapter', 'optical_length': 18, 'mass': 22, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'GSO_2_Spacer_20mm': {'brand': 'GSO', 'name': '2" Spacer 20mm', 'type': 'type_adapter', 'optical_length': 20, 'mass': 24, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'GSO_2_Spacer_25mm': {'brand': 'GSO', 'name': '2" Spacer 25mm', 'type': 'type_adapter', 'optical_length': 25, 'mass': 28, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}}

    @classmethod
    def GSO_SC_M42_T_Adapter(cls):
        return cls.from_database(cls._DATABASE['GSO_SC_M42_T_Adapter'])

    @classmethod
    def GSO_SC_2_Visual_Back(cls):
        return cls.from_database(cls._DATABASE['GSO_SC_2_Visual_Back'])

    @classmethod
    def GSO_SC_1_25_Visual_Back(cls):
        return cls.from_database(cls._DATABASE['GSO_SC_1_25_Visual_Back'])

    @classmethod
    def GSO_SC_Schmidt_Cassegrain_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['GSO_SC_Schmidt_Cassegrain_Spacer_5mm'])

    @classmethod
    def GSO_SC_Schmidt_Cassegrain_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['GSO_SC_Schmidt_Cassegrain_Spacer_10mm'])

    @classmethod
    def GSO_SC_Schmidt_Cassegrain_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['GSO_SC_Schmidt_Cassegrain_Spacer_20mm'])

    @classmethod
    def GSO_SC_Schmidt_Cassegrain_Spacer_30mm(cls):
        return cls.from_database(cls._DATABASE['GSO_SC_Schmidt_Cassegrain_Spacer_30mm'])

    @classmethod
    def GSO_SC_Schmidt_Cassegrain_Spacer_40mm(cls):
        return cls.from_database(cls._DATABASE['GSO_SC_Schmidt_Cassegrain_Spacer_40mm'])

    @classmethod
    def GSO_2_1_25_Adapter(cls):
        return cls.from_database(cls._DATABASE['GSO_2_1_25_Adapter'])

    @classmethod
    def GSO_M42_M48_Adapter(cls):
        return cls.from_database(cls._DATABASE['GSO_M42_M48_Adapter'])

    @classmethod
    def GSO_M48_M54_Adapter(cls):
        return cls.from_database(cls._DATABASE['GSO_M48_M54_Adapter'])

    @classmethod
    def GSO_M42_M54_Adapter(cls):
        return cls.from_database(cls._DATABASE['GSO_M42_M54_Adapter'])

    @classmethod
    def GSO_M54_M68_Adapter(cls):
        return cls.from_database(cls._DATABASE['GSO_M54_M68_Adapter'])

    @classmethod
    def GSO_M48_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['GSO_M48_M42_Adapter'])

    @classmethod
    def GSO_M72_M68_Adapter(cls):
        return cls.from_database(cls._DATABASE['GSO_M72_M68_Adapter'])

    @classmethod
    def GSO_M72_M54_Adapter(cls):
        return cls.from_database(cls._DATABASE['GSO_M72_M54_Adapter'])

    @classmethod
    def GSO_M72_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['GSO_M72_M42_Adapter'])

    @classmethod
    def GSO_EOS_M42_T_Ring(cls):
        return cls.from_database(cls._DATABASE['GSO_EOS_M42_T_Ring'])

    @classmethod
    def GSO_Nikon_F_M42_T_Ring(cls):
        return cls.from_database(cls._DATABASE['GSO_Nikon_F_M42_T_Ring'])

    @classmethod
    def GSO_Sony_E_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['GSO_Sony_E_M42_Adapter'])

    @classmethod
    def GSO_1_25_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['GSO_1_25_Spacer_3mm'])

    @classmethod
    def GSO_1_25_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['GSO_1_25_Spacer_4mm'])

    @classmethod
    def GSO_1_25_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['GSO_1_25_Spacer_5mm'])

    @classmethod
    def GSO_1_25_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['GSO_1_25_Spacer_6mm'])

    @classmethod
    def GSO_1_25_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['GSO_1_25_Spacer_7mm'])

    @classmethod
    def GSO_1_25_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['GSO_1_25_Spacer_8mm'])

    @classmethod
    def GSO_1_25_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['GSO_1_25_Spacer_9mm'])

    @classmethod
    def GSO_1_25_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['GSO_1_25_Spacer_10mm'])

    @classmethod
    def GSO_1_25_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['GSO_1_25_Spacer_12mm'])

    @classmethod
    def GSO_1_25_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['GSO_1_25_Spacer_15mm'])

    @classmethod
    def GSO_1_25_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['GSO_1_25_Spacer_18mm'])

    @classmethod
    def GSO_1_25_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['GSO_1_25_Spacer_20mm'])

    @classmethod
    def GSO_1_25_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['GSO_1_25_Spacer_25mm'])

    @classmethod
    def GSO_2_Spacer_3mm(cls):
        return cls.from_database(cls._DATABASE['GSO_2_Spacer_3mm'])

    @classmethod
    def GSO_2_Spacer_4mm(cls):
        return cls.from_database(cls._DATABASE['GSO_2_Spacer_4mm'])

    @classmethod
    def GSO_2_Spacer_5mm(cls):
        return cls.from_database(cls._DATABASE['GSO_2_Spacer_5mm'])

    @classmethod
    def GSO_2_Spacer_6mm(cls):
        return cls.from_database(cls._DATABASE['GSO_2_Spacer_6mm'])

    @classmethod
    def GSO_2_Spacer_7mm(cls):
        return cls.from_database(cls._DATABASE['GSO_2_Spacer_7mm'])

    @classmethod
    def GSO_2_Spacer_8mm(cls):
        return cls.from_database(cls._DATABASE['GSO_2_Spacer_8mm'])

    @classmethod
    def GSO_2_Spacer_9mm(cls):
        return cls.from_database(cls._DATABASE['GSO_2_Spacer_9mm'])

    @classmethod
    def GSO_2_Spacer_10mm(cls):
        return cls.from_database(cls._DATABASE['GSO_2_Spacer_10mm'])

    @classmethod
    def GSO_2_Spacer_12mm(cls):
        return cls.from_database(cls._DATABASE['GSO_2_Spacer_12mm'])

    @classmethod
    def GSO_2_Spacer_15mm(cls):
        return cls.from_database(cls._DATABASE['GSO_2_Spacer_15mm'])

    @classmethod
    def GSO_2_Spacer_18mm(cls):
        return cls.from_database(cls._DATABASE['GSO_2_Spacer_18mm'])

    @classmethod
    def GSO_2_Spacer_20mm(cls):
        return cls.from_database(cls._DATABASE['GSO_2_Spacer_20mm'])

    @classmethod
    def GSO_2_Spacer_25mm(cls):
        return cls.from_database(cls._DATABASE['GSO_2_Spacer_25mm'])

class GsoSpacer(Spacer):
    _DATABASE = {'GSO_1_25_Spacer_0_5mm': {'brand': 'GSO', 'name': '1.25" Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 4, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'GSO_1_25_Spacer_1mm': {'brand': 'GSO', 'name': '1.25" Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 4, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'GSO_1_25_Spacer_1_5mm': {'brand': 'GSO', 'name': '1.25" Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 4, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'GSO_1_25_Spacer_2mm': {'brand': 'GSO', 'name': '1.25" Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 4, 'tside_thread': '1.25"', 'tside_gender': 'Female', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'GSO_2_Spacer_0_5mm': {'brand': 'GSO', 'name': '2" Spacer 0.5mm', 'type': 'type_spacer', 'optical_length': 0.5, 'mass': 9, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'GSO_2_Spacer_1mm': {'brand': 'GSO', 'name': '2" Spacer 1mm', 'type': 'type_spacer', 'optical_length': 1, 'mass': 9, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'GSO_2_Spacer_1_5mm': {'brand': 'GSO', 'name': '2" Spacer 1.5mm', 'type': 'type_spacer', 'optical_length': 1.5, 'mass': 9, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}, 'GSO_2_Spacer_2mm': {'brand': 'GSO', 'name': '2" Spacer 2mm', 'type': 'type_spacer', 'optical_length': 2, 'mass': 9, 'tside_thread': '2"', 'tside_gender': 'Female', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': True, 'bf_role': ''}}

    @classmethod
    def GSO_1_25_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['GSO_1_25_Spacer_0_5mm'])

    @classmethod
    def GSO_1_25_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['GSO_1_25_Spacer_1mm'])

    @classmethod
    def GSO_1_25_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['GSO_1_25_Spacer_1_5mm'])

    @classmethod
    def GSO_1_25_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['GSO_1_25_Spacer_2mm'])

    @classmethod
    def GSO_2_Spacer_0_5mm(cls):
        return cls.from_database(cls._DATABASE['GSO_2_Spacer_0_5mm'])

    @classmethod
    def GSO_2_Spacer_1mm(cls):
        return cls.from_database(cls._DATABASE['GSO_2_Spacer_1mm'])

    @classmethod
    def GSO_2_Spacer_1_5mm(cls):
        return cls.from_database(cls._DATABASE['GSO_2_Spacer_1_5mm'])

    @classmethod
    def GSO_2_Spacer_2mm(cls):
        return cls.from_database(cls._DATABASE['GSO_2_Spacer_2mm'])