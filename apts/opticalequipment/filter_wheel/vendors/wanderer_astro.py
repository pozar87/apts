from ..base import FilterWheel


class WandererAstroFilterWheel(FilterWheel):
    _DATABASE = {
        "Wanderer_Astro_FilterWheel_M42": {
            "brand": "Wanderer Astro",
            "name": "FilterWheel (M42)",
            "type": "type_filter_wheel",
            "optical_length": 19,
            "mass": 300,
            "tside_thread": "M42",
            "tside_gender": "Male",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Wanderer_Astro_FilterWheel_M48": {
            "brand": "Wanderer Astro",
            "name": "FilterWheel (M48)",
            "type": "type_filter_wheel",
            "optical_length": 19,
            "mass": 380,
            "tside_thread": "M48",
            "tside_gender": "Male",
            "cside_thread": "M48",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Wanderer_Astro_FilterWheel_M54": {
            "brand": "Wanderer Astro",
            "name": "FilterWheel (M54)",
            "type": "type_filter_wheel",
            "optical_length": 20,
            "mass": 500,
            "tside_thread": "M54",
            "tside_gender": "Male",
            "cside_thread": "M54",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Wanderer_Astro_FilterWheel_M68": {
            "brand": "Wanderer Astro",
            "name": "FilterWheel (M68)",
            "type": "type_filter_wheel",
            "optical_length": 21,
            "mass": 600,
            "tside_thread": "M68",
            "tside_gender": "Male",
            "cside_thread": "M68",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Wanderer_Astro_FilterWheel_M42(cls):
        return cls.from_database(cls._DATABASE["Wanderer_Astro_FilterWheel_M42"])

    @classmethod
    def Wanderer_Astro_FilterWheel_M48(cls):
        return cls.from_database(cls._DATABASE["Wanderer_Astro_FilterWheel_M48"])

    @classmethod
    def Wanderer_Astro_FilterWheel_M54(cls):
        return cls.from_database(cls._DATABASE["Wanderer_Astro_FilterWheel_M54"])

    @classmethod
    def Wanderer_Astro_FilterWheel_M68(cls):
        return cls.from_database(cls._DATABASE["Wanderer_Astro_FilterWheel_M68"])
