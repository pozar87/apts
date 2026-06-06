from ..base import Diagonal

class NationalGeographicDiagonal(Diagonal):
    _DATABASE = {
        "National_Geographic_Mirror_Diagonal_1_25": {
            "brand": "National Geographic",
            "name": "Mirror Diagonal (1.25\")",
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 80,
            "tside_thread": "1.25\"",
            "tside_gender": "Male",
            "cside_thread": "1.25\"",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def National_Geographic_Mirror_Diagonal_1_25(cls):
        return cls.from_database(
            cls._DATABASE["National_Geographic_Mirror_Diagonal_1_25"]
        )
