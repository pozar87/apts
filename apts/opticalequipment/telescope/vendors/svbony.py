from ..base import Telescope

class SvbonyTelescope(Telescope):
    _DATABASE = {
        'SVBony_SV503_70ED': {'brand': 'SVBony', 'name': 'SV503 70ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2220, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 70, 'focal_length_mm': 420}, # Verified via specs
        'SVBony_SV503_80ED': {'brand': 'SVBony', 'name': 'SV503 80ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2900, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 80, 'focal_length_mm': 560}, # Verified via specs
        'SVBony_SV503_102ED': {'brand': 'SVBony', 'name': 'SV503 102ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 102, 'focal_length_mm': 714}, # Verified via specs
        'SVBony_SV550_80ED': {'brand': 'SVBony', 'name': 'SV550 80ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2450, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 80, 'focal_length_mm': 480}, # Triplet APO
        'SVBony_SV550_122ED': {'brand': 'SVBony', 'name': 'SV550 122ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 6440, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 122, 'focal_length_mm': 854},
        'SVBony_SV48': {'brand': 'SVBony', 'name': 'SV48', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2410, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 90, 'focal_length_mm': 500},
        'SVBony_SV503_80': {'brand': 'SVBony', 'name': 'SV503 80', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2900, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 80, 'focal_length_mm': 560},
    }

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