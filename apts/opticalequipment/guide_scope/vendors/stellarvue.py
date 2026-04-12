from ..base import GuideScope


class StellarvueGuideScope(GuideScope):
    _DATABASE = {
        "Stellarvue_SV50_Guide_Scope": {
            "brand": "Stellarvue",
            "name": "SV50 Guide Scope",
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
    def Stellarvue_SV50_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_SV50_Guide_Scope"])
