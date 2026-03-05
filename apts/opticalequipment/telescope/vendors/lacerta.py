from ..base import Telescope

class LacertaTelescope(Telescope):
    _DATABASE = {
        'Lacerta_Newton_200_800': {'brand': 'Lacerta', 'name': 'Newton 200/800', 'type': 'newtonian_reflector', 'optical_length': 0, 'mass': 8200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 200, 'focal_length_mm': 800, 'central_obstruction_mm': 70}, # Verified via Lacerta specs
        'Lacerta_Newton_250_1000': {'brand': 'Lacerta', 'name': 'Newton 250/1000', 'type': 'newtonian_reflector', 'optical_length': 0, 'mass': 12500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 250, 'focal_length_mm': 1000, 'central_obstruction_mm': 80}, # Verified via Lacerta specs
        'Lacerta_Newton_200_1000': {'brand': 'Lacerta', 'name': 'Newton 200/1000', 'type': 'newtonian_reflector', 'optical_length': 0, 'mass': 8500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 200, 'focal_length_mm': 1000, 'central_obstruction_mm': 63},
        'Lacerta_Newton_300_1200': {'brand': 'Lacerta', 'name': 'Newton 300/1200', 'type': 'newtonian_reflector', 'optical_length': 0, 'mass': 18500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 300, 'focal_length_mm': 1200, 'central_obstruction_mm': 88},
        'Lacerta_72_432_APO': {'brand': 'Lacerta', 'name': '72/432 APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 72, 'focal_length_mm': 432},
        'Lacerta_80_480_APO': {'brand': 'Lacerta', 'name': '80/480 APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3100, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 80, 'focal_length_mm': 480},
        'Lacerta_102_714_APO': {'brand': 'Lacerta', 'name': '102/714 APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 102, 'focal_length_mm': 714},
        'Lacerta_130_910_APO': {'brand': 'Lacerta', 'name': '130/910 APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 7200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 130, 'focal_length_mm': 910},
    }

    @classmethod
    def Lacerta_Newton_200_800(cls):
        return cls.from_database(cls._DATABASE['Lacerta_Newton_200_800'])

    @classmethod
    def Lacerta_Newton_250_1000(cls):
        return cls.from_database(cls._DATABASE['Lacerta_Newton_250_1000'])

    @classmethod
    def Lacerta_Newton_200_1000(cls):
        return cls.from_database(cls._DATABASE['Lacerta_Newton_200_1000'])

    @classmethod
    def Lacerta_Newton_300_1200(cls):
        return cls.from_database(cls._DATABASE['Lacerta_Newton_300_1200'])

    @classmethod
    def Lacerta_72_432_APO(cls):
        return cls.from_database(cls._DATABASE['Lacerta_72_432_APO'])

    @classmethod
    def Lacerta_80_480_APO(cls):
        return cls.from_database(cls._DATABASE['Lacerta_80_480_APO'])

    @classmethod
    def Lacerta_102_714_APO(cls):
        return cls.from_database(cls._DATABASE['Lacerta_102_714_APO'])

    @classmethod
    def Lacerta_130_910_APO(cls):
        return cls.from_database(cls._DATABASE['Lacerta_130_910_APO'])
