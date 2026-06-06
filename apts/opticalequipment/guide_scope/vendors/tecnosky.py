from ..base import GuideScope


class TecnoskyGuideScope(GuideScope):
    _DATABASE = {
        "Tecnosky_30mm_Guide_Scope": {
            "brand": "Tecnosky",
            "name": "30mm Guide Scope",
            "type": "type_guide_scope",
            "optical_length": 0,
            "mass": 110,
            "tside_thread": "",
            "tside_gender": "Male",
            "cside_thread": "CS",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Tecnosky_60mm_Guide_Scope": {
            "brand": "Tecnosky",
            "name": "60mm Guide Scope",
            "type": "type_guide_scope",
            "optical_length": 0,
            "mass": 310,
            "tside_thread": "",
            "tside_gender": "Male",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Tecnosky_30mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Tecnosky_30mm_Guide_Scope'])

    @classmethod
    def Tecnosky_60mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Tecnosky_60mm_Guide_Scope'])
