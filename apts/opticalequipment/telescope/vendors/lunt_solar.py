from ..base import Telescope

class Lunt_solarTelescope(Telescope):
    _DATABASE = {
        'Lunt_Solar_LS50THa_50mm_H_alpha': {'brand': 'Lunt Solar', 'name': 'LS50THa 50mm H-alpha', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2100, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 50, 'focal_length_mm': 350}, # Verified via Lunt specs
        'Lunt_Solar_LS60THa_60mm_H_alpha': {'brand': 'Lunt Solar', 'name': 'LS60THa 60mm H-alpha', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2900, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 60, 'focal_length_mm': 500}, # Verified via Lunt specs
        'Lunt_Solar_LS80THa_80mm_H_alpha': {'brand': 'Lunt Solar', 'name': 'LS80THa 80mm H-alpha', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 80, 'focal_length_mm': 560}, # Verified via Lunt specs
        'Lunt_Solar_LS100THa_100mm_H_alpha': {'brand': 'Lunt Solar', 'name': 'LS100THa 100mm H-alpha', 'type': 'type_refractor', 'optical_length': 0, 'mass': 7200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 100, 'focal_length_mm': 714},
        'Lunt_Solar_LS130THa_130mm_H_alpha': {'brand': 'Lunt Solar', 'name': 'LS130THa 130mm H-alpha', 'type': 'type_refractor', 'optical_length': 0, 'mass': 12500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 130, 'focal_length_mm': 910},
        'Lunt_Solar_LS60MT': {'brand': 'Lunt Solar', 'name': 'LS60MT', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3100, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 60, 'focal_length_mm': 420},
        'Lunt_Solar_LS80MT': {'brand': 'Lunt Solar', 'name': 'LS80MT', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 80, 'focal_length_mm': 560},
    }

    @classmethod
    def Lunt_Solar_LS50THa_50mm_H_alpha(cls):
        return cls.from_database(cls._DATABASE['Lunt_Solar_LS50THa_50mm_H_alpha'])

    @classmethod
    def Lunt_Solar_LS60THa_60mm_H_alpha(cls):
        return cls.from_database(cls._DATABASE['Lunt_Solar_LS60THa_60mm_H_alpha'])

    @classmethod
    def Lunt_Solar_LS80THa_80mm_H_alpha(cls):
        return cls.from_database(cls._DATABASE['Lunt_Solar_LS80THa_80mm_H_alpha'])

    @classmethod
    def Lunt_Solar_LS100THa_100mm_H_alpha(cls):
        return cls.from_database(cls._DATABASE['Lunt_Solar_LS100THa_100mm_H_alpha'])

    @classmethod
    def Lunt_Solar_LS130THa_130mm_H_alpha(cls):
        return cls.from_database(cls._DATABASE['Lunt_Solar_LS130THa_130mm_H_alpha'])

    @classmethod
    def Lunt_Solar_LS60MT(cls):
        return cls.from_database(cls._DATABASE['Lunt_Solar_LS60MT'])

    @classmethod
    def Lunt_Solar_LS80MT(cls):
        return cls.from_database(cls._DATABASE['Lunt_Solar_LS80MT'])
