from ..base import Telescope

class GsoTelescope(Telescope):
    _DATABASE = {'GSO_RC_6': {'brand': 'GSO', 'name': 'RC 6"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 5000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'GSO_RC_8': {'brand': 'GSO', 'name': 'RC 8"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 8500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'GSO_RC_10': {'brand': 'GSO', 'name': 'RC 10"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 12000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'GSO_RC_12': {'brand': 'GSO', 'name': 'RC 12"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 16000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'GSO_RC_14': {'brand': 'GSO', 'name': 'RC 14"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 20000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'GSO_RC_16': {'brand': 'GSO', 'name': 'RC 16"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 28000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'GSO_Newton_6_f_5': {'brand': 'GSO', 'name': 'Newton 6" f/5', 'type': 'type_telescope', 'optical_length': 0, 'mass': 4500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'GSO_Newton_8_f_4': {'brand': 'GSO', 'name': 'Newton 8" f/4', 'type': 'type_telescope', 'optical_length': 0, 'mass': 7500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'GSO_Newton_8_f_5': {'brand': 'GSO', 'name': 'Newton 8" f/5', 'type': 'type_telescope', 'optical_length': 0, 'mass': 8000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'GSO_Newton_10_f_5': {'brand': 'GSO', 'name': 'Newton 10" f/5', 'type': 'type_telescope', 'optical_length': 0, 'mass': 11000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'GSO_Newton_12_f_5': {'brand': 'GSO', 'name': 'Newton 12" f/5', 'type': 'type_telescope', 'optical_length': 0, 'mass': 15000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'GSO_Newton_16_f_4_5': {'brand': 'GSO', 'name': 'Newton 16" f/4.5', 'type': 'type_telescope', 'optical_length': 0, 'mass': 26000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'GSO_Newton_6_f_8_Dob': {'brand': 'GSO', 'name': 'Newton 6" f/8 Dob', 'type': 'type_telescope', 'optical_length': 0, 'mass': 5500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'GSO_Newton_8_f_6_Dob': {'brand': 'GSO', 'name': 'Newton 8" f/6 Dob', 'type': 'type_telescope', 'optical_length': 0, 'mass': 8000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'GSO_Newton_10_f_6_Dob': {'brand': 'GSO', 'name': 'Newton 10" f/6 Dob', 'type': 'type_telescope', 'optical_length': 0, 'mass': 11500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'GSO_Newton_12_f_5_Dob': {'brand': 'GSO', 'name': 'Newton 12" f/5 Dob', 'type': 'type_telescope', 'optical_length': 0, 'mass': 15000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'GSO_GSO_80ED': {'brand': 'GSO', 'name': 'GSO 80ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2400, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'GSO_GSO_102ED': {'brand': 'GSO', 'name': 'GSO 102ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'GSO_Dobson_6': {'brand': 'GSO', 'name': 'Dobson 6"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 5000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'GSO_Dobson_8': {'brand': 'GSO', 'name': 'Dobson 8"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 7000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'GSO_Dobson_10': {'brand': 'GSO', 'name': 'Dobson 10"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 9500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'GSO_Dobson_12': {'brand': 'GSO', 'name': 'Dobson 12"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 13000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'GSO_Dobson_14': {'brand': 'GSO', 'name': 'Dobson 14"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 18000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'GSO_Dobson_16': {'brand': 'GSO', 'name': 'Dobson 16"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 25000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def GSO_RC_6(cls):
        return cls.from_database(cls._DATABASE['GSO_RC_6'])

    @classmethod
    def GSO_RC_8(cls):
        return cls.from_database(cls._DATABASE['GSO_RC_8'])

    @classmethod
    def GSO_RC_10(cls):
        return cls.from_database(cls._DATABASE['GSO_RC_10'])

    @classmethod
    def GSO_RC_12(cls):
        return cls.from_database(cls._DATABASE['GSO_RC_12'])

    @classmethod
    def GSO_RC_14(cls):
        return cls.from_database(cls._DATABASE['GSO_RC_14'])

    @classmethod
    def GSO_RC_16(cls):
        return cls.from_database(cls._DATABASE['GSO_RC_16'])

    @classmethod
    def GSO_Newton_6_f_5(cls):
        return cls.from_database(cls._DATABASE['GSO_Newton_6_f_5'])

    @classmethod
    def GSO_Newton_8_f_4(cls):
        return cls.from_database(cls._DATABASE['GSO_Newton_8_f_4'])

    @classmethod
    def GSO_Newton_8_f_5(cls):
        return cls.from_database(cls._DATABASE['GSO_Newton_8_f_5'])

    @classmethod
    def GSO_Newton_10_f_5(cls):
        return cls.from_database(cls._DATABASE['GSO_Newton_10_f_5'])

    @classmethod
    def GSO_Newton_12_f_5(cls):
        return cls.from_database(cls._DATABASE['GSO_Newton_12_f_5'])

    @classmethod
    def GSO_Newton_16_f_4_5(cls):
        return cls.from_database(cls._DATABASE['GSO_Newton_16_f_4_5'])

    @classmethod
    def GSO_Newton_6_f_8_Dob(cls):
        return cls.from_database(cls._DATABASE['GSO_Newton_6_f_8_Dob'])

    @classmethod
    def GSO_Newton_8_f_6_Dob(cls):
        return cls.from_database(cls._DATABASE['GSO_Newton_8_f_6_Dob'])

    @classmethod
    def GSO_Newton_10_f_6_Dob(cls):
        return cls.from_database(cls._DATABASE['GSO_Newton_10_f_6_Dob'])

    @classmethod
    def GSO_Newton_12_f_5_Dob(cls):
        return cls.from_database(cls._DATABASE['GSO_Newton_12_f_5_Dob'])

    @classmethod
    def GSO_GSO_80ED(cls):
        return cls.from_database(cls._DATABASE['GSO_GSO_80ED'])

    @classmethod
    def GSO_GSO_102ED(cls):
        return cls.from_database(cls._DATABASE['GSO_GSO_102ED'])

    @classmethod
    def GSO_Dobson_6(cls):
        return cls.from_database(cls._DATABASE['GSO_Dobson_6'])

    @classmethod
    def GSO_Dobson_8(cls):
        return cls.from_database(cls._DATABASE['GSO_Dobson_8'])

    @classmethod
    def GSO_Dobson_10(cls):
        return cls.from_database(cls._DATABASE['GSO_Dobson_10'])

    @classmethod
    def GSO_Dobson_12(cls):
        return cls.from_database(cls._DATABASE['GSO_Dobson_12'])

    @classmethod
    def GSO_Dobson_14(cls):
        return cls.from_database(cls._DATABASE['GSO_Dobson_14'])

    @classmethod
    def GSO_Dobson_16(cls):
        return cls.from_database(cls._DATABASE['GSO_Dobson_16'])