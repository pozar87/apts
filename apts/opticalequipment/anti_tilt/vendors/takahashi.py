from ..base import AntiTilt


class TakahashiAntiTilt(AntiTilt):
    _DATABASE = {
        "Takahashi_Tilt_Adjuster_M54": {
            "brand": "Takahashi",
            "name": "Tilt Adjuster (M54)",
            "type": "type_anti_tilt",
            "optical_length": 8,
            "mass": 55,
            "tside_thread": "M54",
            "tside_gender": "Male",
            "cside_thread": "M54",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_Tilt_Adjuster_M82": {
            "brand": "Takahashi",
            "name": "Tilt Adjuster (M82)",
            "type": "type_anti_tilt",
            "optical_length": 8,
            "mass": 70,
            "tside_thread": "M82",
            "tside_gender": "Male",
            "cside_thread": "M82",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Takahashi_Tilt_Adjuster_M54(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Tilt_Adjuster_M54"])

    @classmethod
    def Takahashi_Tilt_Adjuster_M82(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Tilt_Adjuster_M82"])
