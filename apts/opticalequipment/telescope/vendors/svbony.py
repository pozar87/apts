from ..base import Telescope

class SvbonyTelescope(Telescope):
    _DATABASE = {'SVBony_SV503_70ED': {'brand': 'SVBony', 'name': 'SV503 70ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 1800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'SVBony_SV503_80ED': {'brand': 'SVBony', 'name': 'SV503 80ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'SVBony_SV503_102ED': {'brand': 'SVBony', 'name': 'SV503 102ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'SVBony_SV550_80ED': {'brand': 'SVBony', 'name': 'SV550 80ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2700, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'SVBony_SV550_122ED': {'brand': 'SVBony', 'name': 'SV550 122ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 6000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'SVBony_SV48': {'brand': 'SVBony', 'name': 'SV48', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'SVBony_SV503_80': {'brand': 'SVBony', 'name': 'SV503 80', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def SVBony_SV503_70ED(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV503_70ED'])

    @classmethod
    def SVBony_SV503_80ED(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV503_80ED'])

    @classmethod
    def SVBony_SV503_102ED(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV503_102ED'])

    @classmethod
    def SVBony_SV550_80ED(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV550_80ED'])

    @classmethod
    def SVBony_SV550_122ED(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV550_122ED'])

    @classmethod
    def SVBony_SV48(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV48'])

    @classmethod
    def SVBony_SV503_80(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV503_80'])