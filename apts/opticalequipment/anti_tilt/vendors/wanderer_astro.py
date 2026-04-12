from ..base import AntiTilt


class WandererAstroAntiTilt(AntiTilt):
    _DATABASE = {
        "Wanderer_Astro_ETA_Electronic_Tilt_Adjuster_M54": {
            "brand": "Wanderer Astro",
            "name": "ETA Electronic Tilt Adjuster (M54)",
            "type": "type_anti_tilt",
            "optical_length": 11,
            "mass": 150,
            "tside_thread": "M54",
            "tside_gender": "Male",
            "cside_thread": "M54",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Wanderer_Astro_ETA_Electronic_Tilt_Adjuster_M48": {
            "brand": "Wanderer Astro",
            "name": "ETA Electronic Tilt Adjuster (M48)",
            "type": "type_anti_tilt",
            "optical_length": 11,
            "mass": 140,
            "tside_thread": "M48",
            "tside_gender": "Male",
            "cside_thread": "M48",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Wanderer_Astro_ETA_Electronic_Tilt_Adjuster_M68": {
            "brand": "Wanderer Astro",
            "name": "ETA Electronic Tilt Adjuster (M68)",
            "type": "type_anti_tilt",
            "optical_length": 11,
            "mass": 170,
            "tside_thread": "M68",
            "tside_gender": "Male",
            "cside_thread": "M68",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Wanderer_Astro_ETA_Electronic_Tilt_Adjuster_M54(cls):
        return cls.from_database(
            cls._DATABASE["Wanderer_Astro_ETA_Electronic_Tilt_Adjuster_M54"]
        )

    @classmethod
    def Wanderer_Astro_ETA_Electronic_Tilt_Adjuster_M48(cls):
        return cls.from_database(
            cls._DATABASE["Wanderer_Astro_ETA_Electronic_Tilt_Adjuster_M48"]
        )

    @classmethod
    def Wanderer_Astro_ETA_Electronic_Tilt_Adjuster_M68(cls):
        return cls.from_database(
            cls._DATABASE["Wanderer_Astro_ETA_Electronic_Tilt_Adjuster_M68"]
        )
