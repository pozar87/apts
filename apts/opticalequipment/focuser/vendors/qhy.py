from ..base import Focuser


class QHYFocuser(Focuser):
    _DATABASE = {
        "QHY_Q_Focuser": {
            "brand": "QHY",
            "name": "Q-Focuser",
            "type": "type_focuser",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": "",
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def QHY_Q_Focuser(cls):
        return cls.from_database(cls._DATABASE['QHY_Q_Focuser'])
