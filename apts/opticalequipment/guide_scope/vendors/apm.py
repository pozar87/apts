from ..base import GuideScope


class APMGuideScope(GuideScope):
    _DATABASE = {
        "APM_Guide_Scope_50mm": {
            "brand": "APM",
            "name": "Guide Scope 50mm",
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
        "APM_Guide_Scope_60mm": {
            "brand": "APM",
            "name": "Guide Scope 60mm",
            "type": "type_guide_scope",
            "optical_length": 0,
            "mass": 300,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def APM_Guide_Scope_50mm(cls):
        return cls.from_database(cls._DATABASE["APM_Guide_Scope_50mm"])

    @classmethod
    def APM_Guide_Scope_60mm(cls):
        return cls.from_database(cls._DATABASE["APM_Guide_Scope_60mm"])
