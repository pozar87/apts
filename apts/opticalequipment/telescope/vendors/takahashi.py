from ..base import Telescope

class TakahashiTelescope(Telescope):
    _DATABASE = {
        'Takahashi_FSQ_85EDP': {'brand': 'Takahashi', 'name': 'FSQ-85EDP', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3600, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 85, 'focal_length_mm': 450}, # Verified via Takahashi specs
        'Takahashi_FSQ_106ED': {'brand': 'Takahashi', 'name': 'FSQ-106ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 7000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 106, 'focal_length_mm': 530}, # Verified via Takahashi specs
        'Takahashi_FSQ_130ED': {'brand': 'Takahashi', 'name': 'FSQ-130ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 12100, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M82', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 130, 'focal_length_mm': 650},
        'Takahashi_FC_76DCU': {'brand': 'Takahashi', 'name': 'FC-76DCU', 'type': 'type_refractor', 'optical_length': 0, 'mass': 1900, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 76, 'focal_length_mm': 570},
        'Takahashi_FC_100DZ': {'brand': 'Takahashi', 'name': 'FC-100DZ', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3900, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 100, 'focal_length_mm': 800},
        'Takahashi_FS_60CB': {'brand': 'Takahashi', 'name': 'FS-60CB', 'type': 'type_refractor', 'optical_length': 0, 'mass': 1300, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 60, 'focal_length_mm': 355},
        'Takahashi_TSA_120': {'brand': 'Takahashi', 'name': 'TSA-120', 'type': 'type_refractor', 'optical_length': 0, 'mass': 6700, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 120, 'focal_length_mm': 900},
        'Takahashi_TOA_130NFB': {'brand': 'Takahashi', 'name': 'TOA-130NFB', 'type': 'type_refractor', 'optical_length': 0, 'mass': 12300, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M92', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 130, 'focal_length_mm': 1000},
        'Takahashi_Epsilon_130D': {'brand': 'Takahashi', 'name': 'Epsilon-130D', 'type': 'newtonian_reflector', 'optical_length': 0, 'mass': 4900, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 130, 'focal_length_mm': 430, 'central_obstruction_mm': 65}, # Hyperbolic Newtonian
        'Takahashi_Epsilon_160ED': {'brand': 'Takahashi', 'name': 'Epsilon-160ED', 'type': 'newtonian_reflector', 'optical_length': 0, 'mass': 6900, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 160, 'focal_length_mm': 530, 'central_obstruction_mm': 80},
        'Takahashi_Epsilon_180ED': {'brand': 'Takahashi', 'name': 'Epsilon-180ED', 'type': 'newtonian_reflector', 'optical_length': 0, 'mass': 10000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 180, 'focal_length_mm': 500, 'central_obstruction_mm': 90},
        'Takahashi_Mewlon_180C': {'brand': 'Takahashi', 'name': 'Mewlon-180C', 'type': 'catadioptric', 'optical_length': 0, 'mass': 6200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 180, 'focal_length_mm': 2160, 'central_obstruction_mm': 54},
        'Takahashi_Mewlon_210': {'brand': 'Takahashi', 'name': 'Mewlon-210', 'type': 'catadioptric', 'optical_length': 0, 'mass': 8100, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 210, 'focal_length_mm': 2415, 'central_obstruction_mm': 63},
    }

    @classmethod
    def Takahashi_FSQ_85EDP(cls):
        return cls.from_database(cls._DATABASE['Takahashi_FSQ_85EDP'])

    @classmethod
    def Takahashi_FSQ_106ED(cls):
        return cls.from_database(cls._DATABASE['Takahashi_FSQ_106ED'])

    @classmethod
    def Takahashi_FSQ_130ED(cls):
        return cls.from_database(cls._DATABASE['Takahashi_FSQ_130ED'])

    @classmethod
    def Takahashi_FC_76DCU(cls):
        return cls.from_database(cls._DATABASE['Takahashi_FC_76DCU'])

    @classmethod
    def Takahashi_FC_100DZ(cls):
        return cls.from_database(cls._DATABASE['Takahashi_FC_100DZ'])

    @classmethod
    def Takahashi_FS_60CB(cls):
        return cls.from_database(cls._DATABASE['Takahashi_FS_60CB'])

    @classmethod
    def Takahashi_TSA_120(cls):
        return cls.from_database(cls._DATABASE['Takahashi_TSA_120'])

    @classmethod
    def Takahashi_TOA_130NFB(cls):
        return cls.from_database(cls._DATABASE['Takahashi_TOA_130NFB'])

    @classmethod
    def Takahashi_Epsilon_130D(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Epsilon_130D'])

    @classmethod
    def Takahashi_Epsilon_160ED(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Epsilon_160ED'])

    @classmethod
    def Takahashi_Epsilon_180ED(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Epsilon_180ED'])

    @classmethod
    def Takahashi_Mewlon_180C(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Mewlon_180C'])

    @classmethod
    def Takahashi_Mewlon_210(cls):
        return cls.from_database(cls._DATABASE['Takahashi_Mewlon_210'])
