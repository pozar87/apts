from ..base import Diagonal

class OmegonDiagonal(Diagonal):
    _DATABASE = {
        "Omegon_Dielectric_Diagonal_2": {
            "brand": "Omegon",
            "name": 'Dielectric Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 400,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": '2"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Mirror_Diagonal_1_25": {
            "brand": "Omegon",
            "name": 'Mirror Diagonal (1.25")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 100,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Dielectric_Diagonal_1_25_v2": {
            "brand": "Omegon",
            "name": 'Dielectric Diagonal (1.25") (v2)',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 155,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_Dielectric_Diagonal_2_v2": {
            "brand": "Omegon",
            "name": 'Dielectric Diagonal (2") (v2)',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 405,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": '2"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Omegon_Dielectric_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Omegon_Dielectric_Diagonal_2"])

    @classmethod
    def Omegon_Mirror_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["Omegon_Mirror_Diagonal_1_25"])

    @classmethod
    def Omegon_Dielectric_Diagonal_1_25_v2(cls):
        return cls.from_database(cls._DATABASE["Omegon_Dielectric_Diagonal_1_25_v2"])

    @classmethod
    def Omegon_Dielectric_Diagonal_2_v2(cls):
        return cls.from_database(cls._DATABASE["Omegon_Dielectric_Diagonal_2_v2"])
