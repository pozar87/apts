from ..base import GuideScope


class PegasusGuideScope(GuideScope):
    _DATABASE = {
        "Pegasus_50mm_Guide_Scope": {
            "brand": "Pegasus",
            "name": "50mm Guide Scope",
            "type": "type_guide_scope",
            "optical_length": 0,
            "mass": 260,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Pegasus_50mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE["Pegasus_50mm_Guide_Scope"])
