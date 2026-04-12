from ..base import AntiTilt


class QHYAntiTilt(AntiTilt):
    _DATABASE = {
        "QHY_Tilt_Adjuster_M54": {
            "brand": "QHY",
            "name": "Tilt Adjuster (M54)",
            "type": "type_anti_tilt",
            "optical_length": 10,
            "mass": 70,
            "tside_thread": "M54",
            "tside_gender": "Male",
            "cside_thread": "M54",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def QHY_Tilt_Adjuster_M54(cls):
        return cls.from_database(cls._DATABASE["QHY_Tilt_Adjuster_M54"])
