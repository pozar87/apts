from ..base import AntiTilt


class ExploreScientificAntiTilt(AntiTilt):
    _DATABASE = {
        "Explore_Scientific_Tilt_Adjuster_M48": {
            "brand": "Explore Scientific",
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
    }

    @classmethod
    def Explore_Scientific_Tilt_Adjuster_M48(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_Tilt_Adjuster_M48"])
