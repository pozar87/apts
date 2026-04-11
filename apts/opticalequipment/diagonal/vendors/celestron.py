from ..base import Diagonal

class CelestronDiagonal(Diagonal):
    _DATABASE = {
        "Celestron_Dielectric_Diagonal_1_25": {
            "brand": "Celestron",
            "name": 'Dielectric Diagonal (1.25")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 150,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Dielectric_Diagonal_2": {
            "brand": "Celestron",
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
        "Celestron_XLT_Diagonal_1_25": {
            "brand": "Celestron",
            "name": 'XLT Diagonal (1.25")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_XLT_Diagonal_2": {
            "brand": "Celestron",
            "name": 'XLT Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 420,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": '2"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Mirror_Diagonal_1_25": {
            "brand": "Celestron",
            "name": 'Mirror Diagonal (1.25")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 120,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Mirror_Diagonal_2": {
            "brand": "Celestron",
            "name": 'Mirror Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 350,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": '2"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Celestron_Dielectric_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["Celestron_Dielectric_Diagonal_1_25"])

    @classmethod
    def Celestron_Dielectric_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Celestron_Dielectric_Diagonal_2"])

    @classmethod
    def Celestron_XLT_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["Celestron_XLT_Diagonal_1_25"])

    @classmethod
    def Celestron_XLT_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Celestron_XLT_Diagonal_2"])

    @classmethod
    def Celestron_Mirror_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["Celestron_Mirror_Diagonal_1_25"])

    @classmethod
    def Celestron_Mirror_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Celestron_Mirror_Diagonal_2"])
