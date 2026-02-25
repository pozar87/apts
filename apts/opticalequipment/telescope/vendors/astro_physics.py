from ..base import Telescope

class Astro_physicsTelescope(Telescope):
    _DATABASE = {'Astro_Physics_130GTX': {'brand': 'Astro-Physics', 'name': '130GTX', 'type': 'type_refractor', 'optical_length': 0, 'mass': 7500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Astro_Physics_Stowaway_92mm': {'brand': 'Astro-Physics', 'name': 'Stowaway 92mm', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Astro_Physics_Traveler_105mm': {'brand': 'Astro-Physics', 'name': 'Traveler 105mm', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Astro_Physics_StarFire_130_EDF': {'brand': 'Astro-Physics', 'name': 'StarFire 130 EDF', 'type': 'type_refractor', 'optical_length': 0, 'mass': 6500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Astro_Physics_StarFire_155_EDF': {'brand': 'Astro-Physics', 'name': 'StarFire 155 EDF', 'type': 'type_refractor', 'optical_length': 0, 'mass': 10000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Astro_Physics_StarFire_175_EDF': {'brand': 'Astro-Physics', 'name': 'StarFire 175 EDF', 'type': 'type_refractor', 'optical_length': 0, 'mass': 13000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Astro_Physics_AP_92': {'brand': 'Astro-Physics', 'name': 'AP 92', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

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