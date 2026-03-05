from ..base import Telescope

class Officina_stellareTelescope(Telescope):
    _DATABASE = {
        'Officina_Stellare_RH200': {'brand': 'Officina Stellare', 'name': 'RH200', 'type': 'catadioptric', 'optical_length': 0, 'mass': 12000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 200, 'focal_length_mm': 600, 'central_obstruction_mm': 110}, # Verified via specs
        'Officina_Stellare_RH300': {'brand': 'Officina Stellare', 'name': 'RH300', 'type': 'catadioptric', 'optical_length': 0, 'mass': 25000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 300, 'focal_length_mm': 900, 'central_obstruction_mm': 160},
        'Officina_Stellare_RiDK_250': {'brand': 'Officina Stellare', 'name': 'RiDK 250', 'type': 'catadioptric', 'optical_length': 0, 'mass': 15000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 250, 'focal_length_mm': 1750, 'central_obstruction_mm': 110},
        'Officina_Stellare_RiDK_300': {'brand': 'Officina Stellare', 'name': 'RiDK 300', 'type': 'catadioptric', 'optical_length': 0, 'mass': 22000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 300, 'focal_length_mm': 2100, 'central_obstruction_mm': 130},
        'Officina_Stellare_Ultra_CRC_250': {'brand': 'Officina Stellare', 'name': 'Ultra CRC 250', 'type': 'catadioptric', 'optical_length': 0, 'mass': 16000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 250, 'focal_length_mm': 1250, 'central_obstruction_mm': 110},
    }

    @classmethod
    def Officina_Stellare_RH200(cls):
        return cls.from_database(cls._DATABASE['Officina_Stellare_RH200'])

    @classmethod
    def Officina_Stellare_RH300(cls):
        return cls.from_database(cls._DATABASE['Officina_Stellare_RH300'])

    @classmethod
    def Officina_Stellare_RiDK_250(cls):
        return cls.from_database(cls._DATABASE['Officina_Stellare_RiDK_250'])

    @classmethod
    def Officina_Stellare_RiDK_300(cls):
        return cls.from_database(cls._DATABASE['Officina_Stellare_RiDK_300'])

    @classmethod
    def Officina_Stellare_Ultra_CRC_250(cls):
        return cls.from_database(cls._DATABASE['Officina_Stellare_Ultra_CRC_250'])
