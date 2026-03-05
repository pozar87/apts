from ..base import Telescope

class AskarTelescope(Telescope):
    _DATABASE = {
        'Askar_FRA300_Pro': {'brand': 'Askar', 'name': 'FRA300 Pro', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2260, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 60, 'focal_length_mm': 300}, # Verified via specs
        'Askar_FRA400': {'brand': 'Askar', 'name': 'FRA400', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2560, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 72, 'focal_length_mm': 400}, # Verified via specs
        'Askar_FRA500': {'brand': 'Askar', 'name': 'FRA500', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4100, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 90, 'focal_length_mm': 500}, # Verified via specs
        'Askar_FRA600': {'brand': 'Askar', 'name': 'FRA600', 'type': 'type_refractor', 'optical_length': 0, 'mass': 6500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 108, 'focal_length_mm': 600}, # Verified via specs
        'Askar_103APO': {'brand': 'Askar', 'name': '103APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 5500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 103, 'focal_length_mm': 700.4},
        'Askar_80PHQ': {'brand': 'Askar', 'name': '80PHQ', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4700, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 80, 'focal_length_mm': 600},
        'Askar_65PHQ': {'brand': 'Askar', 'name': '65PHQ', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 65, 'focal_length_mm': 416},
        'Askar_107PHQ': {'brand': 'Askar', 'name': '107PHQ', 'type': 'type_refractor', 'optical_length': 0, 'mass': 6400, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 107, 'focal_length_mm': 749},
        'Askar_130PHQ': {'brand': 'Askar', 'name': '130PHQ', 'type': 'type_refractor', 'optical_length': 0, 'mass': 10200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 130, 'focal_length_mm': 1000},
        'Askar_151PHQ': {'brand': 'Askar', 'name': '151PHQ', 'type': 'type_refractor', 'optical_length': 0, 'mass': 11000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 151, 'focal_length_mm': 1057},
        'Askar_185APO': {'brand': 'Askar', 'name': '185APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 14000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 185, 'focal_length_mm': 1295},
        'Askar_V_60Q': {'brand': 'Askar', 'name': 'V 60Q', 'type': 'type_refractor', 'optical_length': 0, 'mass': 1600, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 60, 'focal_length_mm': 300},
        'Askar_V_80Q': {'brand': 'Askar', 'name': 'V 80Q', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 80, 'focal_length_mm': 400},
        'Askar_FMA_135': {'brand': 'Askar', 'name': 'FMA 135', 'type': 'type_refractor', 'optical_length': 0, 'mass': 600, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 30, 'focal_length_mm': 135},
        'Askar_FMA_180_Pro': {'brand': 'Askar', 'name': 'FMA 180 Pro', 'type': 'type_refractor', 'optical_length': 0, 'mass': 800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 40, 'focal_length_mm': 180},
        'Askar_FMA_230': {'brand': 'Askar', 'name': 'FMA 230', 'type': 'type_refractor', 'optical_length': 0, 'mass': 1000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 50, 'focal_length_mm': 230},
        'Askar_200APO': {'brand': 'Askar', 'name': '200APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 14000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 200, 'focal_length_mm': 1400},
        'Askar_140APO': {'brand': 'Askar', 'name': '140APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 10000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 140, 'focal_length_mm': 980},
        'Askar_120APO': {'brand': 'Askar', 'name': '120APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 6500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 120, 'focal_length_mm': 840},
        'Askar_ACL200': {'brand': 'Askar', 'name': 'ACL200', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 1800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 50, 'focal_length_mm': 200},
    }

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
