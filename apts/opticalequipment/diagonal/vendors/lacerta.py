from ..base import Diagonal

class LacertaDiagonal(Diagonal):
    _DATABASE = {
        "Lacerta_Dielectric_Diagonal_2": {
            "brand": "Lacerta",
            "name": "Dielectric Diagonal (2\")",
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 420,
            "tside_thread": "2\"",
            "tside_gender": "Male",
            "cside_thread": "2\"",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Lacerta_Dielectric_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Lacerta_Dielectric_Diagonal_2"])
