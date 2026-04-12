from ..base import GuideScope


class VixenGuideScope(GuideScope):
    _DATABASE = {
        "Vixen_Guide_Scope_50mm": {
            "brand": "Vixen",
            "name": "Guide Scope 50mm",
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
        "Vixen_Guide_Scope_60mm": {
            "brand": "Vixen",
            "name": "Guide Scope 60mm",
            "type": "type_guide_scope",
            "optical_length": 0,
            "mass": 330,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Vixen_Guide_Scope_50mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_Guide_Scope_50mm"])

    @classmethod
    def Vixen_Guide_Scope_60mm(cls):
        return cls.from_database(cls._DATABASE["Vixen_Guide_Scope_60mm"])
