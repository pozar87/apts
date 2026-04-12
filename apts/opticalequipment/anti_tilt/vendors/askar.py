from ..base import AntiTilt


class AskarAntiTilt(AntiTilt):
    _DATABASE = {
        "Askar_Tilt_Adjuster_M48": {
            "brand": "Askar",
            "name": "Tilt Adjuster (M48)",
            "type": "type_anti_tilt",
            "optical_length": 6,
            "mass": 50,
            "tside_thread": "M48",
            "tside_gender": "Male",
            "cside_thread": "M48",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_Tilt_Adjuster_M54": {
            "brand": "Askar",
            "name": "Tilt Adjuster (M54)",
            "type": "type_anti_tilt",
            "optical_length": 8,
            "mass": 60,
            "tside_thread": "M54",
            "tside_gender": "Male",
            "cside_thread": "M54",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Askar_Tilt_Adjuster_M48(cls):
        return cls.from_database(cls._DATABASE["Askar_Tilt_Adjuster_M48"])

    @classmethod
    def Askar_Tilt_Adjuster_M54(cls):
        return cls.from_database(cls._DATABASE["Askar_Tilt_Adjuster_M54"])
