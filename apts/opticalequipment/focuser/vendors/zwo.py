from ..base import Focuser


class ZWOFocuser(Focuser):
    _DATABASE = {
        "ZWO_EAF": {
            "brand": "ZWO",
            "name": "EAF",
            "type": "type_focuser",
            "optical_length": 0,
            "mass": 115,
            "tside_thread": "",
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "ZWO_EAF_v2": {
            "brand": "ZWO",
            "name": "EAF v2",
            "type": "type_focuser",
            "optical_length": 0,
            "mass": 120,
            "tside_thread": "",
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def ZWO_EAF(cls):
        return cls.from_database(cls._DATABASE['ZWO_EAF'])

    @classmethod
    def ZWO_EAF_v2(cls):
        return cls.from_database(cls._DATABASE['ZWO_EAF_v2'])
