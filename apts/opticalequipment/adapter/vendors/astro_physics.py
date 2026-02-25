from ...abstract import IntermediateOpticalEquipment
from ....constants import OpticalType
from ..base import Adapter, Spacer

class Astro_physicsAdapter(Adapter):
    _DATABASE = {'Astro_Physics_M68_M42_Adapter': {'brand': 'Astro-Physics', 'name': 'M68→M42 Adapter', 'type': 'type_adapter', 'optical_length': 10, 'mass': 35, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Astro_Physics_M68_M48_Adapter': {'brand': 'Astro-Physics', 'name': 'M68→M48 Adapter', 'type': 'type_adapter', 'optical_length': 8, 'mass': 35, 'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Astro_Physics_M68_EOS_Adapter': {'brand': 'Astro-Physics', 'name': 'M68→EOS Adapter', 'type': 'type_adapter', 'optical_length': 10, 'mass': 40, 'tside_thread': 'EOS', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Astro_Physics_M68_Nikon_F_Adapter': {'brand': 'Astro-Physics', 'name': 'M68→Nikon F Adapter', 'type': 'type_adapter', 'optical_length': 10, 'mass': 40, 'tside_thread': 'Nikon F', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Astro_Physics_M68_Sony_E_Adapter': {'brand': 'Astro-Physics', 'name': 'M68→Sony E Adapter', 'type': 'type_adapter', 'optical_length': 10, 'mass': 38, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Astro_Physics_M68_Canon_RF_Adapter': {'brand': 'Astro-Physics', 'name': 'M68→Canon RF Adapter', 'type': 'type_adapter', 'optical_length': 10, 'mass': 38, 'tside_thread': 'Canon RF', 'tside_gender': 'Female', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Astro_Physics_M68_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['Astro_Physics_M68_M42_Adapter'])

    @classmethod
    def Astro_Physics_M68_M48_Adapter(cls):
        return cls.from_database(cls._DATABASE['Astro_Physics_M68_M48_Adapter'])

    @classmethod
    def Astro_Physics_M68_EOS_Adapter(cls):
        return cls.from_database(cls._DATABASE['Astro_Physics_M68_EOS_Adapter'])

    @classmethod
    def Astro_Physics_M68_Nikon_F_Adapter(cls):
        return cls.from_database(cls._DATABASE['Astro_Physics_M68_Nikon_F_Adapter'])

    @classmethod
    def Astro_Physics_M68_Sony_E_Adapter(cls):
        return cls.from_database(cls._DATABASE['Astro_Physics_M68_Sony_E_Adapter'])

    @classmethod
    def Astro_Physics_M68_Canon_RF_Adapter(cls):
        return cls.from_database(cls._DATABASE['Astro_Physics_M68_Canon_RF_Adapter'])