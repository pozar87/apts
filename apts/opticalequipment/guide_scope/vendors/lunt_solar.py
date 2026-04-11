from ..base import GuideScope


class LuntSolarGuideScope(GuideScope):
    _DATABASE = {
        "Lunt_Solar_Guide_Scope_50mm": {
            "brand": "Lunt Solar",
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
        "Lunt_Solar_Guide_Scope_50mm_Solar": {
            "brand": "Lunt Solar",
            "name": "Guide Scope 50mm Solar",
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
    }

    @classmethod
    def Lunt_Solar_Guide_Scope_50mm(cls):
        return cls.from_database(cls._DATABASE["Lunt_Solar_Guide_Scope_50mm"])

    @classmethod
    def Lunt_Solar_Guide_Scope_50mm_Solar(cls):
        return cls.from_database(cls._DATABASE["Lunt_Solar_Guide_Scope_50mm_Solar"])
