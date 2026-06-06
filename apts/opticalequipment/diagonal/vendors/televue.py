from ..base import Diagonal

class TeleVueDiagonal(Diagonal):
    _DATABASE = {
        "TeleVue_Everbrite_Diagonal_1_25": {
            "brand": "TeleVue",
            "name": "Everbrite Diagonal (1.25\")",
            "type": "type_diagonal",
            "optical_length": 75,
            "mass": 227,
            "tside_thread": "1.25\"",
            "tside_gender": "Male",
            "cside_thread": "1.25\"",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Everbrite_Diagonal_2": {
            "brand": "TeleVue",
            "name": "Everbrite Diagonal (2\")",
            "type": "type_diagonal",
            "optical_length": 100,
            "mass": 470,
            "tside_thread": "2\"",
            "tside_gender": "Male",
            "cside_thread": "2\"",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "TeleVue_Star_Diagonal_2": {
            "brand": "TeleVue",
            "name": "Star Diagonal (2\")",
            "type": "type_diagonal",
            "optical_length": 0,
            "mass": 500,
            "tside_thread": "2\"",
            "tside_gender": "Male",
            "cside_thread": "2\"",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def TeleVue_Everbrite_Diagonal_1_25(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Everbrite_Diagonal_1_25"])

    @classmethod
    def TeleVue_Everbrite_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Everbrite_Diagonal_2"])

    @classmethod
    def TeleVue_Star_Diagonal_2(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Star_Diagonal_2"])
