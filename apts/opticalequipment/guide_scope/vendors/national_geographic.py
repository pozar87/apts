from ..base import GuideScope


class NationalGeographicGuideScope(GuideScope):
    _DATABASE = {
        "National_Geographic_Guide_Scope_50mm": {
            "brand": "National Geographic",
            "name": "Guide Scope 50mm",
            "type": "type_guide_scope",
            "optical_length": 0,
            "mass": 240,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def National_Geographic_Guide_Scope_50mm(cls):
        return cls.from_database(cls._DATABASE["National_Geographic_Guide_Scope_50mm"])
