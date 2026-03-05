from ..base import Telescope

class Explore_scientificTelescope(Telescope):
    _DATABASE = {
        'Explore_Scientific_ED80_FCD100': {'brand': 'Explore Scientific', 'name': 'ED80 FCD100', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3400, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 80, 'focal_length_mm': 480}, # Verified via specs
        'Explore_Scientific_ED102_FCD100': {'brand': 'Explore Scientific', 'name': 'ED102 FCD100', 'type': 'type_refractor', 'optical_length': 0, 'mass': 5000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 102, 'focal_length_mm': 714}, # Verified via specs
        'Explore_Scientific_ED127_FCD100': {'brand': 'Explore Scientific', 'name': 'ED127 FCD100', 'type': 'type_refractor', 'optical_length': 0, 'mass': 8200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 127, 'focal_length_mm': 952}, # Verified via specs
        'Explore_Scientific_ED152_FCD100': {'brand': 'Explore Scientific', 'name': 'ED152 FCD100', 'type': 'type_refractor', 'optical_length': 0, 'mass': 11300, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 152, 'focal_length_mm': 1216}, # Verified via specs
        'Explore_Scientific_ED80_Essential': {'brand': 'Explore Scientific', 'name': 'ED80 Essential', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2600, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 80, 'focal_length_mm': 480},
        'Explore_Scientific_ED102_Essential': {'brand': 'Explore Scientific', 'name': 'ED102 Essential', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 102, 'focal_length_mm': 714},
        'Explore_Scientific_ED127_Essential': {'brand': 'Explore Scientific', 'name': 'ED127 Essential', 'type': 'type_refractor', 'optical_length': 0, 'mass': 7000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 127, 'focal_length_mm': 952},
        'Explore_Scientific_AR102_Air_Spaced_Doublet': {'brand': 'Explore Scientific', 'name': 'AR102 Air-Spaced Doublet', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 102, 'focal_length_mm': 663},
        'Explore_Scientific_AR127_Air_Spaced': {'brand': 'Explore Scientific', 'name': 'AR127 Air-Spaced', 'type': 'type_refractor', 'optical_length': 0, 'mass': 6800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 127, 'focal_length_mm': 825},
        'Explore_Scientific_AR152_Air_Spaced': {'brand': 'Explore Scientific', 'name': 'AR152 Air-Spaced', 'type': 'type_refractor', 'optical_length': 0, 'mass': 10000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 152, 'focal_length_mm': 988},
        'Explore_Scientific_FirstLight_130mm_Newtonian': {'brand': 'Explore Scientific', 'name': 'FirstLight 130mm Newtonian', 'type': 'newtonian_reflector', 'optical_length': 0, 'mass': 3500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 130, 'focal_length_mm': 600},
        'Explore_Scientific_Truss_Dob_10': {'brand': 'Explore Scientific', 'name': 'Truss Dob 10"', 'type': 'newtonian_reflector', 'optical_length': 0, 'mass': 26400, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 254, 'focal_length_mm': 1270},
        'Explore_Scientific_Truss_Dob_12': {'brand': 'Explore Scientific', 'name': 'Truss Dob 12"', 'type': 'newtonian_reflector', 'optical_length': 0, 'mass': 30000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 305, 'focal_length_mm': 1525},
        'Explore_Scientific_Truss_Dob_16': {'brand': 'Explore Scientific', 'name': 'Truss Dob 16"', 'type': 'newtonian_reflector', 'optical_length': 0, 'mass': 40000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 406, 'focal_length_mm': 1826},
    }

    @classmethod
    def Explore_Scientific_ED80_FCD100(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_ED80_FCD100'])

    @classmethod
    def Explore_Scientific_ED102_FCD100(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_ED102_FCD100'])

    @classmethod
    def Explore_Scientific_ED127_FCD100(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_ED127_FCD100'])

    @classmethod
    def Explore_Scientific_ED152_FCD100(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_ED152_FCD100'])

    @classmethod
    def Explore_Scientific_ED80_Essential(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_ED80_Essential'])

    @classmethod
    def Explore_Scientific_ED102_Essential(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_ED102_Essential'])

    @classmethod
    def Explore_Scientific_ED127_Essential(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_ED127_Essential'])

    @classmethod
    def Explore_Scientific_AR102_Air_Spaced_Doublet(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_AR102_Air_Spaced_Doublet'])

    @classmethod
    def Explore_Scientific_AR127_Air_Spaced(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_AR127_Air_Spaced'])

    @classmethod
    def Explore_Scientific_AR152_Air_Spaced(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_AR152_Air_Spaced'])

    @classmethod
    def Explore_Scientific_FirstLight_130mm_Newtonian(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_FirstLight_130mm_Newtonian'])

    @classmethod
    def Explore_Scientific_Truss_Dob_10(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_Truss_Dob_10'])

    @classmethod
    def Explore_Scientific_Truss_Dob_12(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_Truss_Dob_12'])

    @classmethod
    def Explore_Scientific_Truss_Dob_16(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_Truss_Dob_16'])
