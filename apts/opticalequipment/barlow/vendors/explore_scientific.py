from ..base import Barlow

class ExploreScientificBarlow(Barlow):
    _DATABASE = {
        "Explore_Scientific_Focal_Extender_2x_1_25": {
            "brand": "Explore Scientific",
            "name": 'Focal Extender 2x (1.25")',
            "type": "type_barlow",
            "optical_length": 0,
            "mass": 155,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
        "Explore_Scientific_Focal_Extender_3x_1_25": {
            "brand": "Explore Scientific",
            "name": 'Focal Extender 3x (1.25")',
            "type": "type_barlow",
            "optical_length": 0,
            "mass": 155,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
        "Explore_Scientific_Focal_Extender_5x_1_25": {
            "brand": "Explore Scientific",
            "name": 'Focal Extender 5x (1.25")',
            "type": "type_barlow",
            "optical_length": 0,
            "mass": 155,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
        "Explore_Scientific_2x_Focal_Extender_2": {
            "brand": "Explore Scientific",
            "name": '2x Focal Extender (2")',
            "type": "type_barlow",
            "optical_length": 0,
            "mass": 300,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": '2"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
    }

    @classmethod
    def Explore_Scientific_Focal_Extender_2x_1_25(cls):
        return cls.from_database(
            cls._DATABASE["Explore_Scientific_Focal_Extender_2x_1_25"]
        )

    @classmethod
    def Explore_Scientific_Focal_Extender_3x_1_25(cls):
        return cls.from_database(
            cls._DATABASE["Explore_Scientific_Focal_Extender_3x_1_25"]
        )

    @classmethod
    def Explore_Scientific_Focal_Extender_5x_1_25(cls):
        return cls.from_database(
            cls._DATABASE["Explore_Scientific_Focal_Extender_5x_1_25"]
        )

    @classmethod
    def Explore_Scientific_2x_Focal_Extender_2(cls):
        return cls.from_database(
            cls._DATABASE["Explore_Scientific_2x_Focal_Extender_2"]
        )
