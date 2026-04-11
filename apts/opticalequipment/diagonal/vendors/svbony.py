from ..base import Diagonal

class SvbonyDiagonal(Diagonal):
    _DATABASE = {
        "SVBony_SV188P_Diagonal_1_25": {
            "brand": "SVBony",
            "name": 'SV188P Diagonal (1.25")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV199P_Diagonal_2": {
            "brand": "SVBony",
            "name": 'SV199P Diagonal (2")',
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
        "SVBony_Mirror_Diagonal_1_25": {
            "brand": "SVBony",
            "name": 'Mirror Diagonal (1.25")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 80,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_Mirror_Diagonal_2": {
            "brand": "SVBony",
            "name": 'Mirror Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": '2"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def SVBony_SV188P_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV188P_Diagonal_1_25"])

    @classmethod
    def SVBony_SV199P_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV199P_Diagonal_2"])

    @classmethod
    def SVBony_Mirror_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["SVBony_Mirror_Diagonal_1_25"])

    @classmethod
    def SVBony_Mirror_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["SVBony_Mirror_Diagonal_2"])
