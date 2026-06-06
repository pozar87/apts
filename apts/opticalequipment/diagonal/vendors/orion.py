from ..base import Diagonal

class OrionDiagonal(Diagonal):
    _DATABASE = {
        "Orion_Quartz_Mirror_Diagonal_1_25": {
            "brand": "Orion",
            "name": "Quartz Mirror Diagonal (1.25\")",
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": "1.25\"",
            "tside_gender": "Male",
            "cside_thread": "1.25\"",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Quartz_Mirror_Diagonal_2": {
            "brand": "Orion",
            "name": "Quartz Mirror Diagonal (2\")",
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 430,
            "tside_thread": "2\"",
            "tside_gender": "Male",
            "cside_thread": "2\"",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Dielectric_Diagonal_1_25": {
            "brand": "Orion",
            "name": "Dielectric Diagonal (1.25\")",
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": "1.25\"",
            "tside_gender": "Male",
            "cside_thread": "1.25\"",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Dielectric_Diagonal_2": {
            "brand": "Orion",
            "name": "Dielectric Diagonal (2\")",
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 400,
            "tside_thread": "2\"",
            "tside_gender": "Male",
            "cside_thread": "2\"",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Mirror_Diagonal_1_25": {
            "brand": "Orion",
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
        "Orion_Mirror_Diagonal_2": {
            "brand": "Orion",
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
    def Orion_Quartz_Mirror_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["Orion_Quartz_Mirror_Diagonal_1_25"])

    @classmethod
    def Orion_Quartz_Mirror_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Orion_Quartz_Mirror_Diagonal_2"])

    @classmethod
    def Orion_Dielectric_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["Orion_Dielectric_Diagonal_1_25"])

    @classmethod
    def Orion_Dielectric_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Orion_Dielectric_Diagonal_2"])

    @classmethod
    def Orion_Mirror_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["Orion_Mirror_Diagonal_1_25"])

    @classmethod
    def Orion_Mirror_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Orion_Mirror_Diagonal_2"])
