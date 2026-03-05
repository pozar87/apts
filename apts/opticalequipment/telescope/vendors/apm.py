from ..base import Telescope

class ApmTelescope(Telescope):
    _DATABASE = {
        'APM_LZOS_115_805': {'brand': 'APM', 'name': 'LZOS 115/805', 'type': 'type_refractor', 'optical_length': 0, 'mass': 6200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 115, 'focal_length_mm': 805}, # Verified via APM specs
        'APM_LZOS_130_780': {'brand': 'APM', 'name': 'LZOS 130/780', 'type': 'type_refractor', 'optical_length': 0, 'mass': 8800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 130, 'focal_length_mm': 780}, # Verified via APM specs
        'APM_LZOS_152_1200': {'brand': 'APM', 'name': 'LZOS 152/1200', 'type': 'type_refractor', 'optical_length': 0, 'mass': 13500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 152, 'focal_length_mm': 1200}, # Verified via APM specs
        'APM_LZOS_175_1400': {'brand': 'APM', 'name': 'LZOS 175/1400', 'type': 'type_refractor', 'optical_length': 0, 'mass': 19000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 175, 'focal_length_mm': 1400}, # Verified via APM specs
        'APM_TMB_80_480': {'brand': 'APM', 'name': 'TMB 80/480', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 80, 'focal_length_mm': 480},
        'APM_TMB_105_650': {'brand': 'APM', 'name': 'TMB 105/650', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 105, 'focal_length_mm': 650},
        'APM_TMB_130_780': {'brand': 'APM', 'name': 'TMB 130/780', 'type': 'type_refractor', 'optical_length': 0, 'mass': 8000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 130, 'focal_length_mm': 780},
    }

    @classmethod
    def APM_LZOS_115_805(cls):
        return cls.from_database(cls._DATABASE['APM_LZOS_115_805'])

    @classmethod
    def APM_LZOS_130_780(cls):
        return cls.from_database(cls._DATABASE['APM_LZOS_130_780'])

    @classmethod
    def APM_LZOS_152_1200(cls):
        return cls.from_database(cls._DATABASE['APM_LZOS_152_1200'])

    @classmethod
    def APM_LZOS_175_1400(cls):
        return cls.from_database(cls._DATABASE['APM_LZOS_175_1400'])

    @classmethod
    def APM_TMB_80_480(cls):
        return cls.from_database(cls._DATABASE['APM_TMB_80_480'])

    @classmethod
    def APM_TMB_105_650(cls):
        return cls.from_database(cls._DATABASE['APM_TMB_105_650'])

    @classmethod
    def APM_TMB_130_780(cls):
        return cls.from_database(cls._DATABASE['APM_TMB_130_780'])
