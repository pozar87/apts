from ..base import GuideScope


class OrionGuideScope(GuideScope):
    _DATABASE = {
        "Orion_50mm_Guide_Scope": {
            "brand": "Orion",
            "name": "50mm Guide Scope",
            "type": "type_guide_scope",
            "optical_length": 0,
            "mass": 280,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_60mm_Guide_Scope": {
            "brand": "Orion",
            "name": "60mm Guide Scope",
            "type": "type_guide_scope",
            "optical_length": 0,
            "mass": 340,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Mini_50mm_Guide_Scope": {
            "brand": "Orion",
            "name": "Mini 50mm Guide Scope",
            "type": "type_guide_scope",
            "optical_length": 0,
            "mass": 260,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Deluxe_60mm_Guide_Scope": {
            "brand": "Orion",
            "name": "Deluxe 60mm Guide Scope",
            "type": "type_guide_scope",
            "optical_length": 0,
            "mass": 350,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Orion_50mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE["Orion_50mm_Guide_Scope"])

    @classmethod
    def Orion_60mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE["Orion_60mm_Guide_Scope"])

    @classmethod
    def Orion_Mini_50mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE["Orion_Mini_50mm_Guide_Scope"])

    @classmethod
    def Orion_Deluxe_60mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE["Orion_Deluxe_60mm_Guide_Scope"])
