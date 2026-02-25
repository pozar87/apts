from ..base import Adapter

class SaxonAdapter(Adapter):
    _DATABASE = {'Saxon_M42_M48_Adapter': {'brand': 'Saxon', 'name': 'M42→M48 Adapter', 'type': 'type_adapter', 'optical_length': 5, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Saxon_M48_M42_Adapter': {'brand': 'Saxon', 'name': 'M48→M42 Adapter', 'type': 'type_adapter', 'optical_length': 5, 'mass': 18, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Saxon_EOS_M42_T_Ring': {'brand': 'Saxon', 'name': 'EOS→M42 T-Ring', 'type': 'type_adapter', 'optical_length': 10.5, 'mass': 28, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Saxon_Nikon_F_M42_T_Ring': {'brand': 'Saxon', 'name': 'Nikon F→M42 T-Ring', 'type': 'type_adapter', 'optical_length': 8.5, 'mass': 28, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Saxon_M42_M48_Adapter(cls):
        return cls.from_database(cls._DATABASE['Saxon_M42_M48_Adapter'])

    @classmethod
    def Saxon_M48_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['Saxon_M48_M42_Adapter'])

    @classmethod
    def Saxon_EOS_M42_T_Ring(cls):
        return cls.from_database(cls._DATABASE['Saxon_EOS_M42_T_Ring'])

    @classmethod
    def Saxon_Nikon_F_M42_T_Ring(cls):
        return cls.from_database(cls._DATABASE['Saxon_Nikon_F_M42_T_Ring'])