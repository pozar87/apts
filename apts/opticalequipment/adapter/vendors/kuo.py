from ...abstract import IntermediateOpticalEquipment
from ....constants import OpticalType
from ..base import Adapter, Spacer

class KuoAdapter(Adapter):
    _DATABASE = {'KUO_M42_M48_Adapter': {'brand': 'KUO', 'name': 'M42→M48 Adapter', 'type': 'type_adapter', 'optical_length': 5, 'mass': 18, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'KUO_M48_M54_Adapter': {'brand': 'KUO', 'name': 'M48→M54 Adapter', 'type': 'type_adapter', 'optical_length': 7, 'mass': 22, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'KUO_M54_M68_Adapter': {'brand': 'KUO', 'name': 'M54→M68 Adapter', 'type': 'type_adapter', 'optical_length': 8, 'mass': 28, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def KUO_M42_M48_Adapter(cls):
        return cls.from_database(cls._DATABASE['KUO_M42_M48_Adapter'])

    @classmethod
    def KUO_M48_M54_Adapter(cls):
        return cls.from_database(cls._DATABASE['KUO_M48_M54_Adapter'])

    @classmethod
    def KUO_M54_M68_Adapter(cls):
        return cls.from_database(cls._DATABASE['KUO_M54_M68_Adapter'])