from ..base import FlipMirror


class ExploreScientificFlipMirror(FlipMirror):
    _DATABASE = {
        "Explore_Scientific_Flip_Mirror": {
            "brand": "Explore Scientific",
            "name": "Flip Mirror",
            "type": "type_flip_mirror",
            "optical_length": 0,
            "mass": 500,
            "tside_thread": "2\"",
            "tside_gender": "Male",
            "cside_thread": "1.25\"",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_Flipmirror": {
            "brand": "Explore Scientific",
            "name": "Flipmirror",
            "type": "type_flip_mirror",
            "optical_length": 0,
            "mass": 500,
            "tside_thread": "2\"",
            "tside_gender": "Male",
            "cside_thread": "1.25\"",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Explore_Scientific_Flip_Mirror(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_Flip_Mirror"])

    @classmethod
    def Explore_Scientific_Flipmirror(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_Flipmirror"])
