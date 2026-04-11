from ..base import Diagonal

class BaaderDiagonal(Diagonal):
    _DATABASE = {
        "Baader_T_2_Star_Diagonal_1_25": {
            "brand": "Baader",
            "name": 'T-2 Star Diagonal (1.25")',
            "type": "type_diagonal",
            "optical_length": 64,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Clicklock_Diagonal_2": {
            "brand": "Baader",
            "name": 'Clicklock Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 500,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": '2"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Prism_Diagonal_2": {
            "brand": "Baader",
            "name": 'Prism Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 600,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": '2"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Zeiss_Prism_Diagonal_1_25": {
            "brand": "Baader",
            "name": 'Zeiss Prism Diagonal (1.25")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 300,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Zeiss_Prism_Diagonal_2": {
            "brand": "Baader",
            "name": 'Zeiss Prism Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 700,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": '2"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Baader_T_2_Star_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["Baader_T_2_Star_Diagonal_1_25"])

    @classmethod
    def Baader_Clicklock_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Baader_Clicklock_Diagonal_2"])

    @classmethod
    def Baader_Prism_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Baader_Prism_Diagonal_2"])

    @classmethod
    def Baader_Zeiss_Prism_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["Baader_Zeiss_Prism_Diagonal_1_25"])

    @classmethod
    def Baader_Zeiss_Prism_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Baader_Zeiss_Prism_Diagonal_2"])
