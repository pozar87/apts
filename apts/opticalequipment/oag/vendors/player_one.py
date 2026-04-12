from ..base import OAG


class Player_oneOAG(OAG):
    _DATABASE = {
        "Player_One_OAG_M42": {
            "brand": "Player One",
            "name": "OAG (M42)",
            "type": "type_oag",
            "optical_length": 16.5,
            "mass": 180,
            "tside_thread": "M42",
            "tside_gender": "Male",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Player_One_OAG_L_M54": {
            "brand": "Player One",
            "name": "OAG-L (M54)",
            "type": "type_oag",
            "optical_length": 20,
            "mass": 300,
            "tside_thread": "M54",
            "tside_gender": "Male",
            "cside_thread": "M54",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Player_One_OAG_M42(cls):
        return cls.from_database(cls._DATABASE["Player_One_OAG_M42"])

    @classmethod
    def Player_One_OAG_L_M54(cls):
        return cls.from_database(cls._DATABASE["Player_One_OAG_L_M54"])
