from ..base import Focuser


class AltairFocuser(Focuser):
    _DATABASE = {
        "Altair_Starwave_Auto_Focuser": {'brand': 'Altair', 'name': 'Starwave Auto Focuser', 'type': 'type_focuser', 'optical_length': 0, 'mass': 170, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
    }

    @classmethod
    def Altair_Starwave_Auto_Focuser(cls):
        return cls.from_database(cls._DATABASE["Altair_Starwave_Auto_Focuser"])
