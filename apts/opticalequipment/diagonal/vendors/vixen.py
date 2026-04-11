from ..base import Diagonal

class VixenDiagonal(Diagonal):
    _DATABASE = {
        "Vixen_Dielectric_Diagonal_1_25": {
            "brand": "Vixen",
            "name": 'Dielectric Diagonal (1.25")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_Dielectric_Diagonal_2": {
            "brand": "Vixen",
            "name": 'Dielectric Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 480,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": '2"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_SSW_Diagonal_2": {
            "brand": "Vixen",
            "name": 'SSW Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 520,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": '2"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_Enhanced_Aluminum_Diagonal_1_25": {
            "brand": "Vixen",
            "name": 'Enhanced Aluminum Diagonal (1.25")',
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
        "Vixen_Enhanced_Aluminum_Diagonal_2": {
            "brand": "Vixen",
            "name": 'Enhanced Aluminum Diagonal (2")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 300,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": '2"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_Dielectric_Diagonal_1_25_v2": {
            "brand": "Vixen",
            "name": 'Dielectric Diagonal (1.25")(v2)',
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
        "Vixen_Dielectric_Diagonal_2_v2": {
            "brand": "Vixen",
            "name": 'Dielectric Diagonal (2")(v2)',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 430,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": '2"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Vixen_Dielectric_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["Vixen_Dielectric_Diagonal_1_25"])

    @classmethod
    def Vixen_Dielectric_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Vixen_Dielectric_Diagonal_2"])

    @classmethod
    def Vixen_SSW_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Vixen_SSW_Diagonal_2"])

    @classmethod
    def Vixen_Enhanced_Aluminum_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["Vixen_Enhanced_Aluminum_Diagonal_1_25"])

    @classmethod
    def Vixen_Enhanced_Aluminum_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["Vixen_Enhanced_Aluminum_Diagonal_2"])

    @classmethod
    def Vixen_Dielectric_Diagonal_1_25_v2(cls):
        return cls.from_database(cls._DATABASE["Vixen_Dielectric_Diagonal_1_25_v2"])

    @classmethod
    def Vixen_Dielectric_Diagonal_2_v2(cls):
        return cls.from_database(cls._DATABASE["Vixen_Dielectric_Diagonal_2_v2"])
