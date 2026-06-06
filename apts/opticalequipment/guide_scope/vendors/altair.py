from ..base import GuideScope


class AltairGuideScope(GuideScope):
    _DATABASE = {
        "Altair_60mm_Guide_Scope": {
            "brand": "Altair",
            "name": "60mm Guide Scope",
            "type": "type_guide_scope",
            "optical_length": 0,
            "mass": 330,
            "tside_thread": "",
            "tside_gender": "Male",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Altair_30mm_Guide_Scope": {
            "brand": "Altair",
            "name": "30mm Guide Scope",
            "type": "type_guide_scope",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": "",
            "tside_gender": "Male",
            "cside_thread": "CS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Altair_60mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Altair_60mm_Guide_Scope'])

    @classmethod
    def Altair_30mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Altair_30mm_Guide_Scope'])
