from ..base import GuideScope


class BresserGuideScope(GuideScope):
    _DATABASE = {
        "Bresser_50mm_Guide_Scope": {
            "brand": "Bresser",
            "name": "50mm Guide Scope",
            "type": "type_guide_scope",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Guide_Scope_50mm": {
            "brand": "Bresser",
            "name": "Guide Scope 50mm",
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
        "Bresser_60mm_Guide_Scope": {
            "brand": "Bresser",
            "name": "60mm Guide Scope",
            "type": "type_guide_scope",
            "optical_length": 0,
            "mass": 310,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Bresser_50mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE["Bresser_50mm_Guide_Scope"])

    @classmethod
    def Bresser_Guide_Scope_50mm(cls):
        return cls.from_database(cls._DATABASE["Bresser_Guide_Scope_50mm"])

    @classmethod
    def Bresser_60mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE["Bresser_60mm_Guide_Scope"])
