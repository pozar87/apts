from ..base import Telescope

class LacertaTelescope(Telescope):
    _DATABASE = {'Lacerta_Newton_200_800': {'brand': 'Lacerta', 'name': 'Newton 200/800', 'type': 'type_telescope', 'optical_length': 0, 'mass': 7500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Lacerta_Newton_250_1000': {'brand': 'Lacerta', 'name': 'Newton 250/1000', 'type': 'type_telescope', 'optical_length': 0, 'mass': 11500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Lacerta_Newton_200_1000': {'brand': 'Lacerta', 'name': 'Newton 200/1000', 'type': 'type_telescope', 'optical_length': 0, 'mass': 7800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Lacerta_Newton_300_1200': {'brand': 'Lacerta', 'name': 'Newton 300/1200', 'type': 'type_telescope', 'optical_length': 0, 'mass': 16000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Lacerta_72_432_APO': {'brand': 'Lacerta', 'name': '72/432 APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Lacerta_80_480_APO': {'brand': 'Lacerta', 'name': '80/480 APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Lacerta_102_714_APO': {'brand': 'Lacerta', 'name': '102/714 APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Lacerta_130_910_APO': {'brand': 'Lacerta', 'name': '130/910 APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 6500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

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