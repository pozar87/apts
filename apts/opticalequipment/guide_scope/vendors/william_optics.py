from ..base import GuideScope


class WilliamOpticsGuideScope(GuideScope):
    _DATABASE = {
        "William_Optics_UniGuide_50mm": {
            "brand": "William Optics",
            "name": "UniGuide 50mm",
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
        "William_Optics_UniGuide_32mm": {
            "brand": "William Optics",
            "name": "UniGuide 32mm",
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
    def William_Optics_UniGuide_50mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_UniGuide_50mm'])

    @classmethod
    def William_Optics_UniGuide_32mm(cls):
        return cls.from_database(cls._DATABASE['William_Optics_UniGuide_32mm'])
