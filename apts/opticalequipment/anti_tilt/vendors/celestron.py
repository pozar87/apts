from ..base import AntiTilt


class CelestronAntiTilt(AntiTilt):
    _DATABASE = {
        "Celestron_Tilt_Adjuster_SC": {
            "brand": "Celestron",
            "name": "Tilt Adjuster (SC)",
            "type": "type_anti_tilt",
            "optical_length": 8,
            "mass": 70,
            "tside_thread": "SC (Schmidt-Cassegrain)",
            "tside_gender": "Male",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Celestron_Tilt_Adjuster_SC(cls):
        return cls.from_database(cls._DATABASE["Celestron_Tilt_Adjuster_SC"])
