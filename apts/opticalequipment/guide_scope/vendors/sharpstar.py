from ..base import GuideScope


class SharpstarGuideScope(GuideScope):
    _DATABASE = {
        "Sharpstar_30mm_Guide_Scope": {
            "brand": "Sharpstar",
            "name": "30mm Guide Scope",
            "type": "type_guide_scope",
            "optical_length": 0,
            "mass": 120,
            "tside_thread": "",
            "tside_gender": "Male",
            "cside_thread": "CS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sharpstar_50mm_Guide_Scope": {
            "brand": "Sharpstar",
            "name": "50mm Guide Scope",
            "type": "type_guide_scope",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": "",
            "tside_gender": "Male",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sharpstar_60mm_Guide_Scope": {
            "brand": "Sharpstar",
            "name": "60mm Guide Scope",
            "type": "type_guide_scope",
            "optical_length": 0,
            "mass": 300,
            "tside_thread": "",
            "tside_gender": "Male",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Sharpstar_30mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_30mm_Guide_Scope'])

    @classmethod
    def Sharpstar_50mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_50mm_Guide_Scope'])

    @classmethod
    def Sharpstar_60mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_60mm_Guide_Scope'])
