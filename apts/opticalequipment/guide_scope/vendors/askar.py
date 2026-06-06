from ..base import GuideScope


class AskarGuideScope(GuideScope):
    _DATABASE = {
        "Askar_FMA135_Guide_Scope": {
            "brand": "Askar",
            "name": "FMA135 Guide Scope",
            "type": "type_guide_scope",
            "optical_length": 0,
            "mass": 600,
            "tside_thread": "",
            "tside_gender": "Male",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_40mm_Guide_Scope": {
            "brand": "Askar",
            "name": "40mm Guide Scope",
            "type": "type_guide_scope",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": "",
            "tside_gender": "Male",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_32mm_Guide_Scope": {
            "brand": "Askar",
            "name": "32mm Guide Scope",
            "type": "type_guide_scope",
            "optical_length": 0,
            "mass": 150,
            "tside_thread": "",
            "tside_gender": "Male",
            "cside_thread": "CS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Askar_FMA135_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Askar_FMA135_Guide_Scope'])

    @classmethod
    def Askar_40mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Askar_40mm_Guide_Scope'])

    @classmethod
    def Askar_32mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Askar_32mm_Guide_Scope'])
