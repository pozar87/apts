from ..base import AntiTilt


class OmegonAntiTilt(AntiTilt):
    _DATABASE = {
        "Omegon_Tilt_Adjuster_M42": {
            "brand": "Omegon",
            "name": "Tilt Adjuster (M42)",
            "type": "type_anti_tilt",
            "optical_length": 5,
            "mass": 38,
            "tside_thread": "M42",
            "tside_gender": "Male",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Tilt_Adjuster_M48": {
            "brand": "Omegon",
            "name": "Tilt Adjuster (M48)",
            "type": "type_anti_tilt",
            "optical_length": 6,
            "mass": 48,
            "tside_thread": "M48",
            "tside_gender": "Male",
            "cside_thread": "M48",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Omegon_Tilt_Adjuster_M42(cls):
        return cls.from_database(cls._DATABASE["Omegon_Tilt_Adjuster_M42"])

    @classmethod
    def Omegon_Tilt_Adjuster_M48(cls):
        return cls.from_database(cls._DATABASE["Omegon_Tilt_Adjuster_M48"])
