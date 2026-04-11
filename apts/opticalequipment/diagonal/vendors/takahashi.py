from ..base import Diagonal

class TakahashiDiagonal(Diagonal):
    _DATABASE = {
        "Takahashi_Diagonal_1_25": {
            "brand": "Takahashi",
            "name": 'Diagonal (1.25")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_Diagonal_2": {
            "brand": "Takahashi",
            "name": 'Diagonal (2")',
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
        "Takahashi_Star_Diagonal_1_25": {
            "brand": "Takahashi",
            "name": 'Star Diagonal (1.25")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Takahashi_Star_Diagonal_2": {
            "brand": "Takahashi",
            "name": 'Star Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 550,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": '2"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Takahashi_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Diagonal_1_25"])

    @classmethod
    def Takahashi_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Diagonal_2"])

    @classmethod
    def Takahashi_Star_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Star_Diagonal_1_25"])

    @classmethod
    def Takahashi_Star_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Star_Diagonal_2"])
