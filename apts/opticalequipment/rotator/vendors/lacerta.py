from ..base import Rotator


class LacertaRotator(Rotator):
    _DATABASE = {
        "Lacerta_Rotator_M42": {
            "brand": "Lacerta",
            "name": "Rotator (M42)",
            "type": "type_rotator",
            "optical_length": 11,
            "mass": 200,
            "tside_thread": "M42",
            "tside_gender": "Male",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_Rotator_M48": {
            "brand": "Lacerta",
            "name": "Rotator (M48)",
            "type": "type_rotator",
            "optical_length": 12,
            "mass": 280,
            "tside_thread": "M48",
            "tside_gender": "Male",
            "cside_thread": "M48",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Lacerta_Rotator_M42(cls):
        return cls.from_database(cls._DATABASE["Lacerta_Rotator_M42"])

    @classmethod
    def Lacerta_Rotator_M48(cls):
        return cls.from_database(cls._DATABASE["Lacerta_Rotator_M48"])
