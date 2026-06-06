from ..base import Diagonal

class SaxonDiagonal(Diagonal):
    _DATABASE = {
        "Saxon_Mirror_Diagonal_1_25": {
            "brand": "Saxon",
            "name": "Mirror Diagonal (1.25\")",
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 90,
            "tside_thread": "1.25\"",
            "tside_gender": "Male",
            "cside_thread": "1.25\"",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Saxon_Dielectric_Diagonal_2": {
            "brand": "Saxon",
            "name": "Dielectric Diagonal (2\")",
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 350,
            "tside_thread": "2\"",
            "tside_gender": "Male",
            "cside_thread": "2\"",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Saxon_Mirror_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["Saxon_Mirror_Diagonal_1_25"])

    @classmethod
    def Saxon_Dielectric_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Saxon_Dielectric_Diagonal_2"])
