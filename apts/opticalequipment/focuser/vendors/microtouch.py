from ..base import Focuser


class MicroTouchFocuser(Focuser):
    _DATABASE = {
        "MicroTouch_WR35_Focuser": {'brand': 'MicroTouch', 'name': 'WR35 Focuser', 'type': 'type_focuser', 'optical_length': 0, 'mass': 200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
    }

    @classmethod
    def MicroTouch_WR35_Focuser(cls):
        return cls.from_database(cls._DATABASE["MicroTouch_WR35_Focuser"])
