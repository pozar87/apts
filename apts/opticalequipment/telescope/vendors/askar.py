from ..base import Telescope

class AskarTelescope(Telescope):
    _DATABASE = {'Askar_FRA300_Pro': {'brand': 'Askar', 'name': 'FRA300 Pro', 'type': 'type_refractor', 'optical_length': 0, 'mass': 1800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Askar_FRA400': {'brand': 'Askar', 'name': 'FRA400', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Askar_FRA500': {'brand': 'Askar', 'name': 'FRA500', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Askar_FRA600': {'brand': 'Askar', 'name': 'FRA600', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Askar_103APO': {'brand': 'Askar', 'name': '103APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Askar_80PHQ': {'brand': 'Askar', 'name': '80PHQ', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Askar_65PHQ': {'brand': 'Askar', 'name': '65PHQ', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Askar_107PHQ': {'brand': 'Askar', 'name': '107PHQ', 'type': 'type_refractor', 'optical_length': 0, 'mass': 5000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Askar_130PHQ': {'brand': 'Askar', 'name': '130PHQ', 'type': 'type_refractor', 'optical_length': 0, 'mass': 6000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Askar_151PHQ': {'brand': 'Askar', 'name': '151PHQ', 'type': 'type_refractor', 'optical_length': 0, 'mass': 8500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Askar_185APO': {'brand': 'Askar', 'name': '185APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 12000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Askar_V_60Q': {'brand': 'Askar', 'name': 'V 60Q', 'type': 'type_refractor', 'optical_length': 0, 'mass': 1600, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Askar_V_80Q': {'brand': 'Askar', 'name': 'V 80Q', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Askar_FMA_135': {'brand': 'Askar', 'name': 'FMA 135', 'type': 'type_refractor', 'optical_length': 0, 'mass': 600, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Askar_FMA_180_Pro': {'brand': 'Askar', 'name': 'FMA 180 Pro', 'type': 'type_refractor', 'optical_length': 0, 'mass': 800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Askar_FMA_230': {'brand': 'Askar', 'name': 'FMA 230', 'type': 'type_refractor', 'optical_length': 0, 'mass': 1000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Askar_200APO': {'brand': 'Askar', 'name': '200APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 14000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Askar_140APO': {'brand': 'Askar', 'name': '140APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 5500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Askar_120APO': {'brand': 'Askar', 'name': '120APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Askar_ACL200': {'brand': 'Askar', 'name': 'ACL200', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 2400, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Askar_FMA_80': {'brand': 'Askar', 'name': 'FMA 80', 'type': 'type_refractor', 'optical_length': 0, 'mass': 1100, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Askar_FMA_107APO': {'brand': 'Askar', 'name': 'FMA 107APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Askar_ACL130': {'brand': 'Askar', 'name': 'ACL130', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Askar_V_40Q': {'brand': 'Askar', 'name': 'V 40Q', 'type': 'type_refractor', 'optical_length': 0, 'mass': 1200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Askar_72Q': {'brand': 'Askar', 'name': '72Q', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2400, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Askar_FRA300_Pro_v2': {'brand': 'Askar', 'name': 'FRA300 Pro v2', 'type': 'type_refractor', 'optical_length': 0, 'mass': 1900, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Askar_FRA400_v2': {'brand': 'Askar', 'name': 'FRA400 v2', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2300, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Askar_FRA500_v2': {'brand': 'Askar', 'name': 'FRA500 v2', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3100, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Askar_FRA600_v2': {'brand': 'Askar', 'name': 'FRA600 v2', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3600, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Askar_65PHQ_v2': {'brand': 'Askar', 'name': '65PHQ v2', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2300, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Askar_80PHQ_v2': {'brand': 'Askar', 'name': '80PHQ v2', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3600, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Askar_107PHQ_v2': {'brand': 'Askar', 'name': '107PHQ v2', 'type': 'type_refractor', 'optical_length': 0, 'mass': 5100, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Askar_130PHQ_v2': {'brand': 'Askar', 'name': '130PHQ v2', 'type': 'type_refractor', 'optical_length': 0, 'mass': 6100, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Askar_151PHQ_v2': {'brand': 'Askar', 'name': '151PHQ v2', 'type': 'type_refractor', 'optical_length': 0, 'mass': 8600, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Askar_V_60Q_v2': {'brand': 'Askar', 'name': 'V 60Q v2', 'type': 'type_refractor', 'optical_length': 0, 'mass': 1700, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Askar_V_80Q_v2': {'brand': 'Askar', 'name': 'V 80Q v2', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2300, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Askar_FMA_230_v2': {'brand': 'Askar', 'name': 'FMA 230 v2', 'type': 'type_refractor', 'optical_length': 0, 'mass': 1100, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Askar_200APO_v2': {'brand': 'Askar', 'name': '200APO v2', 'type': 'type_refractor', 'optical_length': 0, 'mass': 14200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Askar_71Q': {'brand': 'Askar', 'name': '71Q', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2400, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Askar_55Q': {'brand': 'Askar', 'name': '55Q', 'type': 'type_refractor', 'optical_length': 0, 'mass': 1500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Askar_FRA300_Pro(cls):
        return cls.from_database(cls._DATABASE['Askar_FRA300_Pro'])

    @classmethod
    def Askar_FRA400(cls):
        return cls.from_database(cls._DATABASE['Askar_FRA400'])

    @classmethod
    def Askar_FRA500(cls):
        return cls.from_database(cls._DATABASE['Askar_FRA500'])

    @classmethod
    def Askar_FRA600(cls):
        return cls.from_database(cls._DATABASE['Askar_FRA600'])

    @classmethod
    def Askar_103APO(cls):
        return cls.from_database(cls._DATABASE['Askar_103APO'])

    @classmethod
    def Askar_80PHQ(cls):
        return cls.from_database(cls._DATABASE['Askar_80PHQ'])

    @classmethod
    def Askar_65PHQ(cls):
        return cls.from_database(cls._DATABASE['Askar_65PHQ'])

    @classmethod
    def Askar_107PHQ(cls):
        return cls.from_database(cls._DATABASE['Askar_107PHQ'])

    @classmethod
    def Askar_130PHQ(cls):
        return cls.from_database(cls._DATABASE['Askar_130PHQ'])

    @classmethod
    def Askar_151PHQ(cls):
        return cls.from_database(cls._DATABASE['Askar_151PHQ'])

    @classmethod
    def Askar_185APO(cls):
        return cls.from_database(cls._DATABASE['Askar_185APO'])

    @classmethod
    def Askar_V_60Q(cls):
        return cls.from_database(cls._DATABASE['Askar_V_60Q'])

    @classmethod
    def Askar_V_80Q(cls):
        return cls.from_database(cls._DATABASE['Askar_V_80Q'])

    @classmethod
    def Askar_FMA_135(cls):
        return cls.from_database(cls._DATABASE['Askar_FMA_135'])

    @classmethod
    def Askar_FMA_180_Pro(cls):
        return cls.from_database(cls._DATABASE['Askar_FMA_180_Pro'])

    @classmethod
    def Askar_FMA_230(cls):
        return cls.from_database(cls._DATABASE['Askar_FMA_230'])

    @classmethod
    def Askar_200APO(cls):
        return cls.from_database(cls._DATABASE['Askar_200APO'])

    @classmethod
    def Askar_140APO(cls):
        return cls.from_database(cls._DATABASE['Askar_140APO'])

    @classmethod
    def Askar_120APO(cls):
        return cls.from_database(cls._DATABASE['Askar_120APO'])

    @classmethod
    def Askar_ACL200(cls):
        return cls.from_database(cls._DATABASE['Askar_ACL200'])

    @classmethod
    def Askar_FMA_80(cls):
        return cls.from_database(cls._DATABASE['Askar_FMA_80'])

    @classmethod
    def Askar_FMA_107APO(cls):
        return cls.from_database(cls._DATABASE['Askar_FMA_107APO'])

    @classmethod
    def Askar_ACL130(cls):
        return cls.from_database(cls._DATABASE['Askar_ACL130'])

    @classmethod
    def Askar_V_40Q(cls):
        return cls.from_database(cls._DATABASE['Askar_V_40Q'])

    @classmethod
    def Askar_72Q(cls):
        return cls.from_database(cls._DATABASE['Askar_72Q'])

    @classmethod
    def Askar_FRA300_Pro_v2(cls):
        return cls.from_database(cls._DATABASE['Askar_FRA300_Pro_v2'])

    @classmethod
    def Askar_FRA400_v2(cls):
        return cls.from_database(cls._DATABASE['Askar_FRA400_v2'])

    @classmethod
    def Askar_FRA500_v2(cls):
        return cls.from_database(cls._DATABASE['Askar_FRA500_v2'])

    @classmethod
    def Askar_FRA600_v2(cls):
        return cls.from_database(cls._DATABASE['Askar_FRA600_v2'])

    @classmethod
    def Askar_65PHQ_v2(cls):
        return cls.from_database(cls._DATABASE['Askar_65PHQ_v2'])

    @classmethod
    def Askar_80PHQ_v2(cls):
        return cls.from_database(cls._DATABASE['Askar_80PHQ_v2'])

    @classmethod
    def Askar_107PHQ_v2(cls):
        return cls.from_database(cls._DATABASE['Askar_107PHQ_v2'])

    @classmethod
    def Askar_130PHQ_v2(cls):
        return cls.from_database(cls._DATABASE['Askar_130PHQ_v2'])

    @classmethod
    def Askar_151PHQ_v2(cls):
        return cls.from_database(cls._DATABASE['Askar_151PHQ_v2'])

    @classmethod
    def Askar_V_60Q_v2(cls):
        return cls.from_database(cls._DATABASE['Askar_V_60Q_v2'])

    @classmethod
    def Askar_V_80Q_v2(cls):
        return cls.from_database(cls._DATABASE['Askar_V_80Q_v2'])

    @classmethod
    def Askar_FMA_230_v2(cls):
        return cls.from_database(cls._DATABASE['Askar_FMA_230_v2'])

    @classmethod
    def Askar_200APO_v2(cls):
        return cls.from_database(cls._DATABASE['Askar_200APO_v2'])

    @classmethod
    def Askar_71Q(cls):
        return cls.from_database(cls._DATABASE['Askar_71Q'])

    @classmethod
    def Askar_55Q(cls):
        return cls.from_database(cls._DATABASE['Askar_55Q'])