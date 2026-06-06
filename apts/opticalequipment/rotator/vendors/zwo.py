from ..base import Rotator


class ZwoRotator(Rotator):
    _DATABASE = {
        "ZWO_EAF_Rotator_M42": {
            "brand": "ZWO",
            "name": "EAF + Rotator (M42)",
            "type": "type_rotator",
            "optical_length": 12,
            "mass": 250,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "ZWO_EAF_Rotator_M54": {
            "brand": "ZWO",
            "name": "EAF + Rotator (M54)",
            "type": "type_rotator",
            "optical_length": 12,
            "mass": 280,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def ZWO_EAF_Rotator_M42(cls):
        return cls.from_database(cls._DATABASE['ZWO_EAF_Rotator_M42'])

    @classmethod
    def ZWO_EAF_Rotator_M54(cls):
        return cls.from_database(cls._DATABASE['ZWO_EAF_Rotator_M54'])
