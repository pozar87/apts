from ..base import Diagonal

class SkyWatcherDiagonal(Diagonal):
    _DATABASE = {
        "Sky_Watcher_Silver_Diamond_Diagonal_1_25": {
            "brand": "Sky-Watcher",
            "name": "Silver Diamond Diagonal (1.25\")",
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": "1.25\"",
            "tside_gender": "Male",
            "cside_thread": "1.25\"",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Silver_Diamond_Diagonal_2": {
            "brand": "Sky-Watcher",
            "name": "Silver Diamond Diagonal (2\")",
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 450,
            "tside_thread": "2\"",
            "tside_gender": "Male",
            "cside_thread": "2\"",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Sky_Watcher_Ultra_HD_Diagonal_2": {
            "brand": "Sky-Watcher",
            "name": "Ultra HD Diagonal (2\")",
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 600,
            "tside_thread": "2\"",
            "tside_gender": "Male",
            "cside_thread": "2\"",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Sky_Watcher_Silver_Diamond_Diagonal_1_25(cls):
        return cls.from_database(
            cls._DATABASE["Sky_Watcher_Silver_Diamond_Diagonal_1_25"]
        )

    @classmethod
    def Sky_Watcher_Silver_Diamond_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Silver_Diamond_Diagonal_2"])

    @classmethod
    def Sky_Watcher_Ultra_HD_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_Ultra_HD_Diagonal_2"])
