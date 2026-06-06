from ..base import Diagonal

class ApmDiagonal(Diagonal):
    _DATABASE = {
        "APM_Dielectric_Diagonal_1_25": {
            "brand": "APM",
            "name": "Dielectric Diagonal (1.25\")",
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": "1.25\"",
            "tside_gender": "Male",
            "cside_thread": "1.25\"",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "APM_Dielectric_Diagonal_2": {
            "brand": "APM",
            "name": "Dielectric Diagonal (2\")",
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 360,
            "tside_thread": "2\"",
            "tside_gender": "Male",
            "cside_thread": "2\"",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def APM_Dielectric_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["APM_Dielectric_Diagonal_1_25"])

    @classmethod
    def APM_Dielectric_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["APM_Dielectric_Diagonal_2"])
