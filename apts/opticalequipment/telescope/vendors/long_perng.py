from ..base import Telescope

class Long_perngTelescope(Telescope):
    _DATABASE = {
        'Long_Perng_LP_66_400_APO': {'brand': 'Long Perng', 'name': 'LP 66/400 APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 1800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 66, 'focal_length_mm': 400}, # Verified via specs
        'Long_Perng_LP_80_480_APO': {'brand': 'Long Perng', 'name': 'LP 80/480 APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 80, 'focal_length_mm': 480}, # Verified via specs
        'Long_Perng_LP_90_500_APO': {'brand': 'Long Perng', 'name': 'LP 90/500 APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 90, 'focal_length_mm': 500},
        'Long_Perng_LP_110_660_APO': {'brand': 'Long Perng', 'name': 'LP 110/660 APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 5500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 110, 'focal_length_mm': 660},
        'Long_Perng_LP_127_952_APO': {'brand': 'Long Perng', 'name': 'LP 127/952 APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 8200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 127, 'focal_length_mm': 952},
    }

    @classmethod
    def Long_Perng_LP_66_400_APO(cls):
        return cls.from_database(cls._DATABASE['Long_Perng_LP_66_400_APO'])

    @classmethod
    def Long_Perng_LP_80_480_APO(cls):
        return cls.from_database(cls._DATABASE['Long_Perng_LP_80_480_APO'])

    @classmethod
    def Long_Perng_LP_90_500_APO(cls):
        return cls.from_database(cls._DATABASE['Long_Perng_LP_90_500_APO'])

    @classmethod
    def Long_Perng_LP_110_660_APO(cls):
        return cls.from_database(cls._DATABASE['Long_Perng_LP_110_660_APO'])

    @classmethod
    def Long_Perng_LP_127_952_APO(cls):
        return cls.from_database(cls._DATABASE['Long_Perng_LP_127_952_APO'])
