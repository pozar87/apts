from ..base import AntiTilt


class MoonliteAntiTilt(AntiTilt):
    _DATABASE = {
        "Moonlite_Tilt_Adjuster_M42": {
            "brand": "Moonlite",
            "name": "Tilt Adjuster (M42)",
            "type": "type_anti_tilt",
            "optical_length": 5,
            "mass": 40,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Moonlite_Tilt_Adjuster_M48": {
            "brand": "Moonlite",
            "name": "Tilt Adjuster (M48)",
            "type": "type_anti_tilt",
            "optical_length": 6,
            "mass": 50,
            "tside_thread": "M48",
            "tside_gender": "Female",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Moonlite_Tilt_Adjuster_M42(cls):
        return cls.from_database(cls._DATABASE['Moonlite_Tilt_Adjuster_M42'])

    @classmethod
    def Moonlite_Tilt_Adjuster_M48(cls):
        return cls.from_database(cls._DATABASE['Moonlite_Tilt_Adjuster_M48'])
