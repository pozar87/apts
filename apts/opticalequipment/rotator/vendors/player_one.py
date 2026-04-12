from ..base import Rotator


class PlayerOneRotator(Rotator):
    _DATABASE = {
        "Player_One_Ares_Rotator_M54": {
            "brand": "Player One",
            "name": "Ares Rotator (M54)",
            "type": "type_rotator",
            "optical_length": 11,
            "mass": 250,
            "tside_thread": "M54",
            "tside_gender": "Male",
            "cside_thread": "M54",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Player_One_Ares_Rotator_M54(cls):
        return cls.from_database(cls._DATABASE["Player_One_Ares_Rotator_M54"])
