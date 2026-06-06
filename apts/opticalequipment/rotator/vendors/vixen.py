from ..base import Rotator


class VixenRotator(Rotator):
    _DATABASE = {
        "Vixen_Rotator_M42": {
            "brand": "Vixen",
            "name": "Rotator (M42)",
            "type": "type_rotator",
            "optical_length": 10,
            "mass": 220,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Vixen_Rotator_M54": {
            "brand": "Vixen",
            "name": "Rotator (M54)",
            "type": "type_rotator",
            "optical_length": 12,
            "mass": 310,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Vixen_Rotator_M42(cls):
        return cls.from_database(cls._DATABASE['Vixen_Rotator_M42'])

    @classmethod
    def Vixen_Rotator_M54(cls):
        return cls.from_database(cls._DATABASE['Vixen_Rotator_M54'])
