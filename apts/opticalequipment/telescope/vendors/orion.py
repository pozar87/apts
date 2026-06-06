from ..base import Telescope


class OrionTelescope(Telescope):
    _DATABASE = {'Orion_EON_130mm_ED': {'brand': 'Orion', 'name':
        'EON 130mm ED', 'type': 'type_refractor', 'optical_length': 0,
        'mass': 10210, 'tside_thread': '', 'tside_gender': '',
        'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False,
        'bf_role': '', 'aperture_mm': 130, 'focal_length_mm': 910,
        'central_obstruction_mm': 0}, 'Orion_8_f_3_9_Astrograph': {'brand':
        'Orion', 'name': '8" f/3.9 Astrograph', 'type':
        'newtonian_reflector', 'optical_length': 0, 'mass': 7940,
        'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48',
        'cside_gender': 'Male', 'reversible': False, 'bf_role': '',
        'aperture_mm': 203, 'focal_length_mm': 800,
        'central_obstruction_mm': 70}, 'Orion_EON_110mm_ED': {'brand':
        'Orion', 'name': 'EON 110mm ED', 'type': 'type_refractor',
        'optical_length': 0, 'mass': 5220, 'tside_thread': '',
        'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male',
        'reversible': False, 'bf_role': '', 'aperture_mm': 110,
        'focal_length_mm': 660, 'central_obstruction_mm': 0},
        'Orion_EON_80mm_ED': {'brand': 'Orion', 'name': 'EON 80mm ED',
        'type': 'type_refractor', 'optical_length': 0, 'mass': 2950,
        'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48',
        'cside_gender': 'Male', 'reversible': False, 'bf_role': '',
        'aperture_mm': 80, 'focal_length_mm': 500, 'central_obstruction_mm':
        0}, 'Orion_XT8_Classic_Dob': {'brand': 'Orion', 'name':
        'XT8 Classic Dob', 'type': 'newtonian_reflector', 'optical_length':
        0, 'mass': 9210, 'tside_thread': '', 'tside_gender': '',
        'cside_thread': '2"', 'cside_gender': 'Female', 'reversible': False,
        'bf_role': '', 'aperture_mm': 203, 'focal_length_mm': 1200,
        'central_obstruction_mm': 47}, 'Orion_XT10_Classic_Dob': {'brand':
        'Orion', 'name': 'XT10 Classic Dob', 'type': 'newtonian_reflector',
        'optical_length': 0, 'mass': 13110, 'tside_thread': '',
        'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Female',
        'reversible': False, 'bf_role': '', 'aperture_mm': 254,
        'focal_length_mm': 1200, 'central_obstruction_mm': 63},
        'Orion_XT12_Classic_Dob': {'brand': 'Orion', 'name':
        'XT12 Classic Dob', 'type': 'newtonian_reflector', 'optical_length':
        0, 'mass': 22680, 'tside_thread': '', 'tside_gender': '',
        'cside_thread': '2"', 'cside_gender': 'Female', 'reversible': False,
        'bf_role': '', 'aperture_mm': 305, 'focal_length_mm': 1500,
        'central_obstruction_mm': 70}, 'Orion_SpaceProbe_130ST': {'brand':
        'Orion', 'name': 'SpaceProbe 130ST', 'type': 'newtonian_reflector',
        'optical_length': 0, 'mass': 2810, 'tside_thread': '',
        'tside_gender': '', 'cside_thread': '1.25"', 'cside_gender':
        'Female', 'reversible': False, 'bf_role': '', 'aperture_mm': 130,
        'focal_length_mm': 650, 'central_obstruction_mm': 36.4}}

    @classmethod
    def Orion_EON_130mm_ED(cls):
        return cls.from_database(cls._DATABASE['Orion_EON_130mm_ED'])

    @classmethod
    def Orion_8_f_3_9_Astrograph(cls):
        return cls.from_database(cls._DATABASE['Orion_8_f_3_9_Astrograph'])

    @classmethod
    def Orion_EON_110mm_ED(cls):
        return cls.from_database(cls._DATABASE['Orion_EON_110mm_ED'])

    @classmethod
    def Orion_EON_80mm_ED(cls):
        return cls.from_database(cls._DATABASE['Orion_EON_80mm_ED'])

    @classmethod
    def Orion_XT8_Classic_Dob(cls):
        return cls.from_database(cls._DATABASE['Orion_XT8_Classic_Dob'])

    @classmethod
    def Orion_XT10_Classic_Dob(cls):
        return cls.from_database(cls._DATABASE['Orion_XT10_Classic_Dob'])

    @classmethod
    def Orion_XT12_Classic_Dob(cls):
        return cls.from_database(cls._DATABASE['Orion_XT12_Classic_Dob'])

    @classmethod
    def Orion_SpaceProbe_130ST(cls):
        return cls.from_database(cls._DATABASE['Orion_SpaceProbe_130ST'])
