from ..base import Telescope

class OmegonTelescope(Telescope):
    _DATABASE = {'Omegon_ProED_80': {'brand': 'Omegon', 'name': 'ProED 80', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Omegon_ProED_100': {'brand': 'Omegon', 'name': 'ProED 100', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Omegon_ProED_110': {'brand': 'Omegon', 'name': 'ProED 110', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Omegon_N_200_800': {'brand': 'Omegon', 'name': 'N 200/800', 'type': 'type_telescope', 'optical_length': 0, 'mass': 7000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Omegon_N_250_1000': {'brand': 'Omegon', 'name': 'N 250/1000', 'type': 'type_telescope', 'optical_length': 0, 'mass': 11000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Omegon_Pro_APO_94': {'brand': 'Omegon', 'name': 'Pro APO 94', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Omegon_Pro_APO_121': {'brand': 'Omegon', 'name': 'Pro APO 121', 'type': 'type_refractor', 'optical_length': 0, 'mass': 5500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Omegon_Pro_APO_152': {'brand': 'Omegon', 'name': 'Pro APO 152', 'type': 'type_refractor', 'optical_length': 0, 'mass': 9000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Omegon_Pro_APO_72_400': {'brand': 'Omegon', 'name': 'Pro APO 72/400', 'type': 'type_refractor', 'optical_length': 0, 'mass': 1800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Omegon_Pro_APO_80_500': {'brand': 'Omegon', 'name': 'Pro APO 80/500', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2600, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Omegon_Pro_APO_100_580': {'brand': 'Omegon', 'name': 'Pro APO 100/580', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Omegon_Pro_APO_110_660': {'brand': 'Omegon', 'name': 'Pro APO 110/660', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Omegon_Pro_APO_127_793': {'brand': 'Omegon', 'name': 'Pro APO 127/793', 'type': 'type_refractor', 'optical_length': 0, 'mass': 6500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Omegon_Pro_APO_152_988': {'brand': 'Omegon', 'name': 'Pro APO 152/988', 'type': 'type_refractor', 'optical_length': 0, 'mass': 9500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Omegon_Pro_Newton_200_800_OTA': {'brand': 'Omegon', 'name': 'Pro Newton 200/800 OTA', 'type': 'type_telescope', 'optical_length': 0, 'mass': 7200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Omegon_Pro_Newton_250_1000_OTA': {'brand': 'Omegon', 'name': 'Pro Newton 250/1000 OTA', 'type': 'type_telescope', 'optical_length': 0, 'mass': 11200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Omegon_Pro_RC_154_1370': {'brand': 'Omegon', 'name': 'Pro RC 154/1370', 'type': 'type_telescope', 'optical_length': 0, 'mass': 6000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Omegon_Pro_RC_203_1624': {'brand': 'Omegon', 'name': 'Pro RC 203/1624', 'type': 'type_telescope', 'optical_length': 0, 'mass': 9500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Omegon_Pro_RC_254_2000': {'brand': 'Omegon', 'name': 'Pro RC 254/2000', 'type': 'type_telescope', 'optical_length': 0, 'mass': 13000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Omegon_Pro_RC_304_2432': {'brand': 'Omegon', 'name': 'Pro RC 304/2432', 'type': 'type_telescope', 'optical_length': 0, 'mass': 17000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Omegon_Pro_RC_355_2845': {'brand': 'Omegon', 'name': 'Pro RC 355/2845', 'type': 'type_telescope', 'optical_length': 0, 'mass': 22000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Omegon_ProED_80(cls):
        return cls.from_database(cls._DATABASE['Omegon_ProED_80'])

    @classmethod
    def Omegon_ProED_100(cls):
        return cls.from_database(cls._DATABASE['Omegon_ProED_100'])

    @classmethod
    def Omegon_ProED_110(cls):
        return cls.from_database(cls._DATABASE['Omegon_ProED_110'])

    @classmethod
    def Omegon_N_200_800(cls):
        return cls.from_database(cls._DATABASE['Omegon_N_200_800'])

    @classmethod
    def Omegon_N_250_1000(cls):
        return cls.from_database(cls._DATABASE['Omegon_N_250_1000'])

    @classmethod
    def Omegon_Pro_APO_94(cls):
        return cls.from_database(cls._DATABASE['Omegon_Pro_APO_94'])

    @classmethod
    def Omegon_Pro_APO_121(cls):
        return cls.from_database(cls._DATABASE['Omegon_Pro_APO_121'])

    @classmethod
    def Omegon_Pro_APO_152(cls):
        return cls.from_database(cls._DATABASE['Omegon_Pro_APO_152'])

    @classmethod
    def Omegon_Pro_APO_72_400(cls):
        return cls.from_database(cls._DATABASE['Omegon_Pro_APO_72_400'])

    @classmethod
    def Omegon_Pro_APO_80_500(cls):
        return cls.from_database(cls._DATABASE['Omegon_Pro_APO_80_500'])

    @classmethod
    def Omegon_Pro_APO_100_580(cls):
        return cls.from_database(cls._DATABASE['Omegon_Pro_APO_100_580'])

    @classmethod
    def Omegon_Pro_APO_110_660(cls):
        return cls.from_database(cls._DATABASE['Omegon_Pro_APO_110_660'])

    @classmethod
    def Omegon_Pro_APO_127_793(cls):
        return cls.from_database(cls._DATABASE['Omegon_Pro_APO_127_793'])

    @classmethod
    def Omegon_Pro_APO_152_988(cls):
        return cls.from_database(cls._DATABASE['Omegon_Pro_APO_152_988'])

    @classmethod
    def Omegon_Pro_Newton_200_800_OTA(cls):
        return cls.from_database(cls._DATABASE['Omegon_Pro_Newton_200_800_OTA'])

    @classmethod
    def Omegon_Pro_Newton_250_1000_OTA(cls):
        return cls.from_database(cls._DATABASE['Omegon_Pro_Newton_250_1000_OTA'])

    @classmethod
    def Omegon_Pro_RC_154_1370(cls):
        return cls.from_database(cls._DATABASE['Omegon_Pro_RC_154_1370'])

    @classmethod
    def Omegon_Pro_RC_203_1624(cls):
        return cls.from_database(cls._DATABASE['Omegon_Pro_RC_203_1624'])

    @classmethod
    def Omegon_Pro_RC_254_2000(cls):
        return cls.from_database(cls._DATABASE['Omegon_Pro_RC_254_2000'])

    @classmethod
    def Omegon_Pro_RC_304_2432(cls):
        return cls.from_database(cls._DATABASE['Omegon_Pro_RC_304_2432'])

    @classmethod
    def Omegon_Pro_RC_355_2845(cls):
        return cls.from_database(cls._DATABASE['Omegon_Pro_RC_355_2845'])