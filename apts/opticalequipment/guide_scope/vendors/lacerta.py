from ..base import GuideScope


class LacertaGuideScope(GuideScope):
    _DATABASE = {
        "Lacerta_Micro_Guide_Scope_30mm": {
            "brand": "Lacerta",
            "name": "Micro Guide Scope 30mm",
            "type": "type_guide_scope",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "CS",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_Guide_Scope_50mm": {
            "brand": "Lacerta",
            "name": "Guide Scope 50mm",
            "type": "type_guide_scope",
            "optical_length": 0,
            "mass": 270,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Lacerta_Micro_Guide_Scope_30mm(cls):
        return cls.from_database(cls._DATABASE["Lacerta_Micro_Guide_Scope_30mm"])

    @classmethod
    def Lacerta_Guide_Scope_50mm(cls):
        return cls.from_database(cls._DATABASE["Lacerta_Guide_Scope_50mm"])
