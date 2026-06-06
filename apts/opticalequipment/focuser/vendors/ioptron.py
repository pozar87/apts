from ..base import Focuser


class iOptronFocuser(Focuser):
    _DATABASE = {
        "iOptron_iEAF_Electronic_Focuser": {
            "brand": "iOptron",
            "name": "iEAF Electronic Focuser",
            "type": "type_focuser",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": "",
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def iOptron_iEAF_Electronic_Focuser(cls):
        return cls.from_database(cls._DATABASE[
            'iOptron_iEAF_Electronic_Focuser'])
