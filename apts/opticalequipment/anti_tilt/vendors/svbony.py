from ..base import AntiTilt


class SVBonyAntiTilt(AntiTilt):
    _DATABASE = {
        "SVBony_Tilt_Adjuster_M42": {
            "brand": "SVBony",
            "name": "Tilt Adjuster (M42)",
            "type": "type_anti_tilt",
            "optical_length": 5,
            "mass": 35,
            "tside_thread": "M42",
            "tside_gender": "Male",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def SVBony_Tilt_Adjuster_M42(cls):
        return cls.from_database(cls._DATABASE["SVBony_Tilt_Adjuster_M42"])
