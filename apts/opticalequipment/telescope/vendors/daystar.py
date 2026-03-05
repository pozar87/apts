from ..base import Telescope

class DaystarTelescope(Telescope):
    _DATABASE = {
        'DayStar_Solar_Scout_60mm': {'brand': 'DayStar', 'name': 'Solar Scout 60mm', 'type': 'type_refractor', 'optical_length': 0, 'mass': 1400, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 60, 'focal_length_mm': 930}, # Verified via DayStar specs
        'DayStar_Solar_Scout_80mm': {'brand': 'DayStar', 'name': 'Solar Scout 80mm', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 80, 'focal_length_mm': 1200}, # Verified via DayStar specs
        'DayStar_SOLO_60_SE': {'brand': 'DayStar', 'name': 'SOLO 60 SE', 'type': 'type_refractor', 'optical_length': 0, 'mass': 1800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 60, 'focal_length_mm': 1200},
        'DayStar_SOLO_80_SE': {'brand': 'DayStar', 'name': 'SOLO 80 SE', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 80, 'focal_length_mm': 1600},
        'DayStar_SolaREDi_66': {'brand': 'DayStar', 'name': 'SolaREDi 66', 'type': 'type_refractor', 'optical_length': 0, 'mass': 1500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 66, 'focal_length_mm': 943},
        'DayStar_SolaREDi_127': {'brand': 'DayStar', 'name': 'SolaREDi 127', 'type': 'type_refractor', 'optical_length': 0, 'mass': 5500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 127, 'focal_length_mm': 2667},
    }

    @classmethod
    def DayStar_Solar_Scout_60mm(cls):
        return cls.from_database(cls._DATABASE['DayStar_Solar_Scout_60mm'])

    @classmethod
    def DayStar_Solar_Scout_80mm(cls):
        return cls.from_database(cls._DATABASE['DayStar_Solar_Scout_80mm'])

    @classmethod
    def DayStar_SOLO_60_SE(cls):
        return cls.from_database(cls._DATABASE['DayStar_SOLO_60_SE'])

    @classmethod
    def DayStar_SOLO_80_SE(cls):
        return cls.from_database(cls._DATABASE['DayStar_SOLO_80_SE'])

    @classmethod
    def DayStar_SolaREDi_66(cls):
        return cls.from_database(cls._DATABASE['DayStar_SolaREDi_66'])

    @classmethod
    def DayStar_SolaREDi_127(cls):
        return cls.from_database(cls._DATABASE['DayStar_SolaREDi_127'])
