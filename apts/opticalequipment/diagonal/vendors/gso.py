from ..base import Diagonal

class GsoDiagonal(Diagonal):
    _DATABASE = {
        "GSO_Erecting_Prism_1_25": {
            "brand": "GSO",
            "name": "Erecting Prism (1.25\")",
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 120,
            "tside_thread": "1.25\"",
            "tside_gender": "Male",
            "cside_thread": "1.25\"",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "GSO_Mirror_Diagonal_2": {
            "brand": "GSO",
            "name": "Mirror Diagonal (2\")",
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
    def GSO_Erecting_Prism_1_25(cls):
        return cls.from_database(cls._DATABASE["GSO_Erecting_Prism_1_25"])

    @classmethod
    def GSO_Mirror_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["GSO_Mirror_Diagonal_2"])
