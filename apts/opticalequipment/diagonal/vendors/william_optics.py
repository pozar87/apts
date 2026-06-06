from ..base import Diagonal

class WilliamOpticsDiagonal(Diagonal):
    _DATABASE = {
        "William_Optics_Dielectric_Diagonal_2": {
            "brand": "William Optics",
            "name": "Dielectric Diagonal (2\")",
            "type": "type_diagonal",
            "optical_length": 105,
            "mass": 431,
            "tside_thread": "2\"",
            "tside_gender": "Male",
            "cside_thread": "2\"",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "William_Optics_Dielectric_Diagonal_1_25": {
            "brand": "William Optics",
            "name": "Dielectric Diagonal (1.25\")",
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": "1.25\"",
            "tside_gender": "Male",
            "cside_thread": "1.25\"",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def William_Optics_Dielectric_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["William_Optics_Dielectric_Diagonal_2"])

    @classmethod
    def William_Optics_Dielectric_Diagonal_1_25(cls):
        return cls.from_database(
            cls._DATABASE["William_Optics_Dielectric_Diagonal_1_25"]
        )
