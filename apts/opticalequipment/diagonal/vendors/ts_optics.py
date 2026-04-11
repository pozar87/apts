from ..base import Diagonal

class TsOpticsDiagonal(Diagonal):
    _DATABASE = {
        "TS_Optics_Dielectric_Diagonal_2": {
            "brand": "TS-Optics",
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
        "TS_Optics_Dielectric_Diagonal_1_25": {
            "brand": "TS-Optics",
            "name": 'Dielectric Diagonal (1.25")',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 170,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_Dielectric_Diagonal_1_25_v2": {
            "brand": "TS-Optics",
            "name": 'Dielectric Diagonal (1.25") (v2)',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 125,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "TS_Optics_Dielectric_Diagonal_2_v2": {
            "brand": "TS-Optics",
            "name": 'Dielectric Diagonal (2") (v2)',
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 355,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": '2"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def TS_Optics_Dielectric_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Dielectric_Diagonal_2"])

    @classmethod
    def TS_Optics_Dielectric_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Dielectric_Diagonal_1_25"])

    @classmethod
    def TS_Optics_Dielectric_Diagonal_1_25_v2(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Dielectric_Diagonal_1_25_v2"])

    @classmethod
    def TS_Optics_Dielectric_Diagonal_2_v2(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Dielectric_Diagonal_2_v2"])
