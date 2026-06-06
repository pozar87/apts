from ..base import Diagonal

class StellarvueDiagonal(Diagonal):
    _DATABASE = {
        "Stellarvue_Dielectric_Diagonal_1_25": {
            "brand": "Stellarvue",
            "name": "Dielectric Diagonal (1.25\")",
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": "1.25\"",
            "tside_gender": "Male",
            "cside_thread": "1.25\"",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_Dielectric_Diagonal_2": {
            "brand": "Stellarvue",
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
    }

    @classmethod
    def Stellarvue_Dielectric_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_Dielectric_Diagonal_1_25"])

    @classmethod
    def Stellarvue_Dielectric_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_Dielectric_Diagonal_2"])
