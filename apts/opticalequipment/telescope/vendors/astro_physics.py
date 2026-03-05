from ..base import Telescope

class Astro_physicsTelescope(Telescope):
    _DATABASE = {
        'Astro_Physics_130GTX': {'brand': 'Astro-Physics', 'name': '130GTX', 'type': 'type_refractor', 'optical_length': 0, 'mass': 8200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 130, 'focal_length_mm': 819}, # Verified via AP specs
        'Astro_Physics_Stowaway_92mm': {'brand': 'Astro-Physics', 'name': 'Stowaway 92mm', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 92, 'focal_length_mm': 612}, # Verified via AP specs
        'Astro_Physics_Traveler_105mm': {'brand': 'Astro-Physics', 'name': 'Traveler 105mm', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4100, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 105, 'focal_length_mm': 610},
        'Astro_Physics_StarFire_130_EDF': {'brand': 'Astro-Physics', 'name': 'StarFire 130 EDF', 'type': 'type_refractor', 'optical_length': 0, 'mass': 6800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 130, 'focal_length_mm': 780},
        'Astro_Physics_StarFire_155_EDF': {'brand': 'Astro-Physics', 'name': 'StarFire 155 EDF', 'type': 'type_refractor', 'optical_length': 0, 'mass': 10400, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 155, 'focal_length_mm': 1085},
        'Astro_Physics_StarFire_175_EDF': {'brand': 'Astro-Physics', 'name': 'StarFire 175 EDF', 'type': 'type_refractor', 'optical_length': 0, 'mass': 13600, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 175, 'focal_length_mm': 1400},
        'Astro_Physics_AP_92': {'brand': 'Astro-Physics', 'name': 'AP 92', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 92, 'focal_length_mm': 612},
    }

    @classmethod
    def Astro_Physics_130GTX(cls):
        return cls.from_database(cls._DATABASE['Astro_Physics_130GTX'])

    @classmethod
    def Astro_Physics_Stowaway_92mm(cls):
        return cls.from_database(cls._DATABASE['Astro_Physics_Stowaway_92mm'])

    @classmethod
    def Astro_Physics_Traveler_105mm(cls):
        return cls.from_database(cls._DATABASE['Astro_Physics_Traveler_105mm'])

    @classmethod
    def Astro_Physics_StarFire_130_EDF(cls):
        return cls.from_database(cls._DATABASE['Astro_Physics_StarFire_130_EDF'])

    @classmethod
    def Astro_Physics_StarFire_155_EDF(cls):
        return cls.from_database(cls._DATABASE['Astro_Physics_StarFire_155_EDF'])

    @classmethod
    def Astro_Physics_StarFire_175_EDF(cls):
        return cls.from_database(cls._DATABASE['Astro_Physics_StarFire_175_EDF'])

    @classmethod
    def Astro_Physics_AP_92(cls):
        return cls.from_database(cls._DATABASE['Astro_Physics_AP_92'])
