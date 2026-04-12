from ..base import GuideScope


class OGMAGuideScope(GuideScope):
    _DATABASE = {
        "OGMA_Guide_Scope_30mm": {
            "brand": "OGMA",
            "name": "Guide Scope 30mm",
            "type": "type_guide_scope",
            "optical_length": 0,
            "mass": 120,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "CS",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "OGMA_Guide_Scope_60mm": {
            "brand": "OGMA",
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
    def OGMA_Guide_Scope_30mm(cls):
        return cls.from_database(cls._DATABASE["OGMA_Guide_Scope_30mm"])

    @classmethod
    def OGMA_Guide_Scope_60mm(cls):
        return cls.from_database(cls._DATABASE["OGMA_Guide_Scope_60mm"])
