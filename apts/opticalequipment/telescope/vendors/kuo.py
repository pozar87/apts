from ..base import Telescope

class KuoTelescope(Telescope):
    _DATABASE = {'KUO_KUO_80_480_APO': {'brand': 'KUO', 'name': 'KUO 80/480 APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2300, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'KUO_KUO_102_714_APO': {'brand': 'KUO', 'name': 'KUO 102/714 APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'KUO_KUO_130_910_APO': {'brand': 'KUO', 'name': 'KUO 130/910 APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 6200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'KUO_KUO_152_1200_APO': {'brand': 'KUO', 'name': 'KUO 152/1200 APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 9000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def KUO_KUO_80_480_APO(cls):
        return cls.from_database(cls._DATABASE['KUO_KUO_80_480_APO'])

    @classmethod
    def KUO_KUO_102_714_APO(cls):
        return cls.from_database(cls._DATABASE['KUO_KUO_102_714_APO'])

    @classmethod
    def KUO_KUO_130_910_APO(cls):
        return cls.from_database(cls._DATABASE['KUO_KUO_130_910_APO'])

    @classmethod
    def KUO_KUO_152_1200_APO(cls):
        return cls.from_database(cls._DATABASE['KUO_KUO_152_1200_APO'])