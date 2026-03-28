from ..base import Telescope

class SvbonyTelescope(Telescope):
    _DATABASE = {
        'SVBony_SV503_70ED': {'brand': 'SVBony', 'name': 'SV503 70ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2220, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 70, 'focal_length_mm': 420, 'central_obstruction_mm': 0}, # Doublet version (Source: Svbony Official)
        'SVBony_SV503_70ED_Quad': {'brand': 'SVBony', 'name': 'SV503 70ED Quadruplet', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2685, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 70, 'focal_length_mm': 474, 'central_obstruction_mm': 0}, # Quad version with built-in flattener (Source: Svbony Blog)
        'SVBony_SV503_80ED': {'brand': 'SVBony', 'name': 'SV503 80ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 80, 'focal_length_mm': 560, 'central_obstruction_mm': 0}, # Mass with rings/caps, ~3.0kg (Source: Svbony Review/User Data)
        'SVBony_SV503_102ED': {'brand': 'SVBony', 'name': 'SV503 102ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 102, 'focal_length_mm': 714, 'central_obstruction_mm': 0}, # OTA net mass, ~4.0kg (Source: Stargazers Lounge / User Data)
        'SVBony_SV550_80ED': {'brand': 'SVBony', 'name': 'SV550 80ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2450, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 80, 'focal_length_mm': 480, 'central_obstruction_mm': 0}, # Triplet APO
        'SVBony_SV550_122ED': {'brand': 'SVBony', 'name': 'SV550 122ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 6440, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 122, 'focal_length_mm': 854, 'central_obstruction_mm': 0}, # Verified via specs
        'SVBony_SV550_60': {'brand': 'SVBony', 'name': 'SV550 60', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2030, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 60, 'focal_length_mm': 300, 'central_obstruction_mm': 0}, # Triplet APO
        'SVBony_SV48': {'brand': 'SVBony', 'name': 'SV48P 90', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2730, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 90, 'focal_length_mm': 500, 'central_obstruction_mm': 0}, # Corrected name and mass (Source: Svbony Official)
        'SVBony_SV48P_102': {'brand': 'SVBony', 'name': 'SV48P 102', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3400, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 102, 'focal_length_mm': 663, 'central_obstruction_mm': 0}, # Added (Source: Svbony Official)
        'SVBony_SV503_80': {'brand': 'SVBony', 'name': 'SV503 80ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 80, 'focal_length_mm': 560, 'central_obstruction_mm': 0}, # Redundant alias
    }

    @classmethod
    def SVBony_SV503_70ED(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV503_70ED'])

    @classmethod
    def SVBony_SV503_70ED_Quad(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV503_70ED_Quad'])

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
    def SVBony_SV550_60(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV550_60'])

    @classmethod
    def SVBony_SV48(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV48'])

    @classmethod
    def SVBony_SV48P_102(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV48P_102'])

    @classmethod
    def SVBony_SV503_80(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV503_80'])
