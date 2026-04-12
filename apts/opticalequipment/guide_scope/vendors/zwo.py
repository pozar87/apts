from ..base import GuideScope


class ZWOGuideScope(GuideScope):
    _DATABASE = {
        "ZWO_30mm_Mini_Guide_Scope": {
            "brand": "ZWO",
            "name": "30mm Mini Guide Scope",
            "type": "type_guide_scope",
            "optical_length": 0,
            "mass": 150,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "CS",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "ZWO_60mm_Guide_Scope": {
            "brand": "ZWO",
            "name": "60mm Guide Scope",
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
        "ZWO_120mm_Guide_Scope": {
            "brand": "ZWO",
            "name": "120mm Guide Scope",
            "type": "type_guide_scope",
            "optical_length": 0,
            "mass": 500,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def ZWO_30mm_Mini_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE["ZWO_30mm_Mini_Guide_Scope"])

    @classmethod
    def ZWO_60mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE["ZWO_60mm_Guide_Scope"])

    @classmethod
    def ZWO_120mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE["ZWO_120mm_Guide_Scope"])
