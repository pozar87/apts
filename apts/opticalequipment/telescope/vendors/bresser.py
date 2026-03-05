from ..base import Telescope

class BresserTelescope(Telescope):
    _DATABASE = {
        'Bresser_Messier_AR_102xs': {'brand': 'Bresser', 'name': 'Messier AR-102xs', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 102, 'focal_length_mm': 460}, # Verified via specs
        'Bresser_Messier_AR_127L': {'brand': 'Bresser', 'name': 'Messier AR-127L', 'type': 'type_refractor', 'optical_length': 0, 'mass': 7900, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 127, 'focal_length_mm': 1200}, # Verified via specs
        'Bresser_Messier_AR_152L': {'brand': 'Bresser', 'name': 'Messier AR-152L', 'type': 'type_refractor', 'optical_length': 0, 'mass': 10600, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 152, 'focal_length_mm': 1200}, # Verified via specs
        'Bresser_Messier_MC_127': {'brand': 'Bresser', 'name': 'Messier MC-127', 'type': 'catadioptric', 'optical_length': 0, 'mass': 3400, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 127, 'focal_length_mm': 1900},
        'Bresser_Messier_MC_152': {'brand': 'Bresser', 'name': 'Messier MC-152', 'type': 'catadioptric', 'optical_length': 0, 'mass': 6500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 152, 'focal_length_mm': 1900},
        'Bresser_Messier_NT_150L_6': {'brand': 'Bresser', 'name': 'Messier NT-150L (6")', 'type': 'newtonian_reflector', 'optical_length': 0, 'mass': 6500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 150, 'focal_length_mm': 1200},
        'Bresser_Messier_NT_203_8': {'brand': 'Bresser', 'name': 'Messier NT-203 (8")', 'type': 'newtonian_reflector', 'optical_length': 0, 'mass': 11500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 203, 'focal_length_mm': 1000},
        'Bresser_Messier_NT_254_10': {'brand': 'Bresser', 'name': 'Messier NT-254 (10")', 'type': 'newtonian_reflector', 'optical_length': 0, 'mass': 14000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 254, 'focal_length_mm': 1270},
    }

    @classmethod
    def Bresser_Messier_AR_102xs(cls):
        return cls.from_database(cls._DATABASE['Bresser_Messier_AR_102xs'])

    @classmethod
    def Bresser_Messier_AR_127L(cls):
        return cls.from_database(cls._DATABASE['Bresser_Messier_AR_127L'])

    @classmethod
    def Bresser_Messier_AR_152L(cls):
        return cls.from_database(cls._DATABASE['Bresser_Messier_AR_152L'])

    @classmethod
    def Bresser_Messier_MC_127(cls):
        return cls.from_database(cls._DATABASE['Bresser_Messier_MC_127'])

    @classmethod
    def Bresser_Messier_MC_152(cls):
        return cls.from_database(cls._DATABASE['Bresser_Messier_MC_152'])

    @classmethod
    def Bresser_Messier_NT_150L_6(cls):
        return cls.from_database(cls._DATABASE['Bresser_Messier_NT_150L_6'])

    @classmethod
    def Bresser_Messier_NT_203_8(cls):
        return cls.from_database(cls._DATABASE['Bresser_Messier_NT_203_8'])

    @classmethod
    def Bresser_Messier_NT_254_10(cls):
        return cls.from_database(cls._DATABASE['Bresser_Messier_NT_254_10'])
