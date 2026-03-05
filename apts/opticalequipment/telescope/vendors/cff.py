from ..base import Telescope

class CffTelescope(Telescope):
    _DATABASE = {
        'CFF_RC_250_10': {'brand': 'CFF', 'name': 'RC 250 (10")', 'type': 'catadioptric', 'optical_length': 0, 'mass': 14000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 250, 'focal_length_mm': 2000, 'central_obstruction_mm': 125}, # Verified via CFF specs
        'CFF_RC_300_12': {'brand': 'CFF', 'name': 'RC 300 (12")', 'type': 'catadioptric', 'optical_length': 0, 'mass': 19000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M117', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 300, 'focal_length_mm': 2400, 'central_obstruction_mm': 150}, # Verified via CFF specs
    }

    @classmethod
    def CFF_RC_250_10(cls):
        return cls.from_database(cls._DATABASE['CFF_RC_250_10'])

    @classmethod
    def CFF_RC_300_12(cls):
        return cls.from_database(cls._DATABASE['CFF_RC_300_12'])
