from ..base import Rotator


class WandererAstroRotator(Rotator):
    _DATABASE = {
        "Wanderer_Astro_Field_Rotator_M42": {
            "brand": "Wanderer Astro",
            "name": "Field Rotator (M42)",
            "type": "type_rotator",
            "optical_length": 10,
            "mass": 250,
            "tside_thread": "M42",
            "tside_gender": "Male",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Wanderer_Astro_Field_Rotator_M48": {
            "brand": "Wanderer Astro",
            "name": "Field Rotator (M48)",
            "type": "type_rotator",
            "optical_length": 11,
            "mass": 300,
            "tside_thread": "M48",
            "tside_gender": "Male",
            "cside_thread": "M48",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Wanderer_Astro_Field_Rotator_M54": {
            "brand": "Wanderer Astro",
            "name": "Field Rotator (M54)",
            "type": "type_rotator",
            "optical_length": 11,
            "mass": 320,
            "tside_thread": "M54",
            "tside_gender": "Male",
            "cside_thread": "M54",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Wanderer_Astro_Rotator_Mini_V2_M54": {
            "brand": "Wanderer Astro",
            "name": "Rotator Mini V2 (M54)",
            "type": "type_rotator",
            "optical_length": 10,
            "mass": 420,
            "tside_thread": "M54",
            "tside_gender": "Male",
            "cside_thread": "M54",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Wanderer_Astro_Rotator_Lite_V2_M68": {
            "brand": "Wanderer Astro",
            "name": "Rotator Lite V2 (M68)",
            "type": "type_rotator",
            "optical_length": 12,
            "mass": 550,
            "tside_thread": "M68",
            "tside_gender": "Male",
            "cside_thread": "M68",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Wanderer_Astro_Rotator_Pro_V2_M92": {
            "brand": "Wanderer Astro",
            "name": "Rotator Pro V2 (M92)",
            "type": "type_rotator",
            "optical_length": 16,
            "mass": 900,
            "tside_thread": "M92",
            "tside_gender": "Male",
            "cside_thread": "M92",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Wanderer_Astro_Field_Rotator_M42(cls):
        return cls.from_database(cls._DATABASE["Wanderer_Astro_Field_Rotator_M42"])

    @classmethod
    def Wanderer_Astro_Field_Rotator_M48(cls):
        return cls.from_database(cls._DATABASE["Wanderer_Astro_Field_Rotator_M48"])

    @classmethod
    def Wanderer_Astro_Field_Rotator_M54(cls):
        return cls.from_database(cls._DATABASE["Wanderer_Astro_Field_Rotator_M54"])

    @classmethod
    def Wanderer_Astro_Rotator_Mini_V2_M54(cls):
        return cls.from_database(cls._DATABASE["Wanderer_Astro_Rotator_Mini_V2_M54"])

    @classmethod
    def Wanderer_Astro_Rotator_Lite_V2_M68(cls):
        return cls.from_database(cls._DATABASE["Wanderer_Astro_Rotator_Lite_V2_M68"])

    @classmethod
    def Wanderer_Astro_Rotator_Pro_V2_M92(cls):
        return cls.from_database(cls._DATABASE["Wanderer_Astro_Rotator_Pro_V2_M92"])
