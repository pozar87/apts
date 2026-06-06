from ..base import Diagonal

class BresserDiagonal(Diagonal):
    _DATABASE = {
        "Bresser_Dielectric_Diagonal_2": {
            "brand": "Bresser",
            "name": "Dielectric Diagonal (2\")",
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 380,
            "tside_thread": "2\"",
            "tside_gender": "Male",
            "cside_thread": "2\"",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Mirror_Diagonal_1_25": {
            "brand": "Bresser",
            "name": "Mirror Diagonal (1.25\")",
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 100,
            "tside_thread": "1.25\"",
            "tside_gender": "Male",
            "cside_thread": "1.25\"",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Bresser_Mirror_Diagonal_2": {
            "brand": "Bresser",
            "name": "Mirror Diagonal (2\")",
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 280,
            "tside_thread": "2\"",
            "tside_gender": "Male",
            "cside_thread": "2\"",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Bresser_Dielectric_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Bresser_Dielectric_Diagonal_2"])

    @classmethod
    def Bresser_Mirror_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["Bresser_Mirror_Diagonal_1_25"])

    @classmethod
    def Bresser_Mirror_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Bresser_Mirror_Diagonal_2"])
