from ..base import Telescope

class William_opticsTelescope(Telescope):
    _DATABASE = {
        'William_Optics_GT71': {'brand': 'William Optics', 'name': 'GT71', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2300, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 71, 'focal_length_mm': 420}, # Verified via specs
        'William_Optics_GT81': {'brand': 'William Optics', 'name': 'GT81', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3300, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 81, 'focal_length_mm': 478}, # Verified via specs
        'William_Optics_GT102': {'brand': 'William Optics', 'name': 'GT102', 'type': 'type_refractor', 'optical_length': 0, 'mass': 5000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 102, 'focal_length_mm': 703}, # Verified via specs
        'William_Optics_GT153': {'brand': 'William Optics', 'name': 'GT153', 'type': 'type_refractor', 'optical_length': 0, 'mass': 8400, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 153, 'focal_length_mm': 1056},
        'William_Optics_RedCat_51': {'brand': 'William Optics', 'name': 'RedCat 51', 'type': 'type_refractor', 'optical_length': 0, 'mass': 1800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 51, 'focal_length_mm': 250}, # Petzval
        'William_Optics_SpaceCat_51': {'brand': 'William Optics', 'name': 'SpaceCat 51', 'type': 'type_refractor', 'optical_length': 0, 'mass': 1800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 51, 'focal_length_mm': 250},
        'William_Optics_WhiteCat_51': {'brand': 'William Optics', 'name': 'WhiteCat 51', 'type': 'type_refractor', 'optical_length': 0, 'mass': 1800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 51, 'focal_length_mm': 250},
        'William_Optics_FluoroStar_91': {'brand': 'William Optics', 'name': 'FluoroStar 91', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 91, 'focal_length_mm': 540},
        'William_Optics_FluoroStar_132': {'brand': 'William Optics', 'name': 'FluoroStar 132', 'type': 'type_refractor', 'optical_length': 0, 'mass': 9000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 132, 'focal_length_mm': 925},
        'William_Optics_ZenithStar_61_II': {'brand': 'William Optics', 'name': 'ZenithStar 61 II', 'type': 'type_refractor', 'optical_length': 0, 'mass': 1450, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 61, 'focal_length_mm': 360},
        'William_Optics_ZenithStar_73': {'brand': 'William Optics', 'name': 'ZenithStar 73', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 73, 'focal_length_mm': 430},
        'William_Optics_ZenithStar_81': {'brand': 'William Optics', 'name': 'ZenithStar 81', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 81, 'focal_length_mm': 559},
        'William_Optics_ZenithStar_103': {'brand': 'William Optics', 'name': 'ZenithStar 103', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4360, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 103, 'focal_length_mm': 710},
        'William_Optics_Redcat_71': {'brand': 'William Optics', 'name': 'Redcat 71', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 71, 'focal_length_mm': 350},
        'William_Optics_Pleiades_68': {'brand': 'William Optics', 'name': 'Pleiades 68', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 68, 'focal_length_mm': 260},
    }

    @classmethod
    def William_Optics_GT71(cls):
        return cls.from_database(cls._DATABASE['William_Optics_GT71'])

    @classmethod
    def William_Optics_GT81(cls):
        return cls.from_database(cls._DATABASE['William_Optics_GT81'])

    @classmethod
    def William_Optics_GT102(cls):
        return cls.from_database(cls._DATABASE['William_Optics_GT102'])

    @classmethod
    def William_Optics_GT153(cls):
        return cls.from_database(cls._DATABASE['William_Optics_GT153'])

    @classmethod
    def William_Optics_RedCat_51(cls):
        return cls.from_database(cls._DATABASE['William_Optics_RedCat_51'])

    @classmethod
    def William_Optics_SpaceCat_51(cls):
        return cls.from_database(cls._DATABASE['William_Optics_SpaceCat_51'])

    @classmethod
    def William_Optics_WhiteCat_51(cls):
        return cls.from_database(cls._DATABASE['William_Optics_WhiteCat_51'])

    @classmethod
    def William_Optics_FluoroStar_91(cls):
        return cls.from_database(cls._DATABASE['William_Optics_FluoroStar_91'])

    @classmethod
    def William_Optics_FluoroStar_132(cls):
        return cls.from_database(cls._DATABASE['William_Optics_FluoroStar_132'])

    @classmethod
    def William_Optics_ZenithStar_61_II(cls):
        return cls.from_database(cls._DATABASE['William_Optics_ZenithStar_61_II'])

    @classmethod
    def William_Optics_ZenithStar_73(cls):
        return cls.from_database(cls._DATABASE['William_Optics_ZenithStar_73'])

    @classmethod
    def William_Optics_ZenithStar_81(cls):
        return cls.from_database(cls._DATABASE['William_Optics_ZenithStar_81'])

    @classmethod
    def William_Optics_ZenithStar_103(cls):
        return cls.from_database(cls._DATABASE['William_Optics_ZenithStar_103'])

    @classmethod
    def William_Optics_Redcat_71(cls):
        return cls.from_database(cls._DATABASE['William_Optics_Redcat_71'])

    @classmethod
    def William_Optics_Pleiades_68(cls):
        return cls.from_database(cls._DATABASE['William_Optics_Pleiades_68'])
