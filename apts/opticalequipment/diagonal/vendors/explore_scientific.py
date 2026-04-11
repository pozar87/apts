from ..base import Diagonal

class ExploreScientificDiagonal(Diagonal):
    _DATABASE = {
        "Explore_Scientific_Diagonal_1_25": {
            "brand": "Explore Scientific",
            "name": 'Diagonal (1.25")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_Diagonal_2": {
            "brand": "Explore Scientific",
            "name": 'Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 380,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": '2"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Explore_Scientific_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_Diagonal_1_25"])

    @classmethod
    def Explore_Scientific_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Explore_Scientific_Diagonal_2"])
