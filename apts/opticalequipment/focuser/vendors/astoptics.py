from ..base import Focuser


class ASTopticsFocuser(Focuser):
    _DATABASE = {
        "ASToptics_Electronic_Focuser": {
            "brand": "ASToptics",
            "name": "Electronic Focuser",
            "type": "type_focuser",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": "",
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def ASToptics_Electronic_Focuser(cls):
        return cls.from_database(cls._DATABASE['ASToptics_Electronic_Focuser'])
