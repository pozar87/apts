from ..base import Rotator


class SharpstarRotator(Rotator):
    _DATABASE = {
        "Sharpstar_Rotator_M48": {
            "brand": "Sharpstar",
            "name": "Rotator (M48)",
            "type": "type_rotator",
            "optical_length": 11,
            "mass": 270,
            "tside_thread": "M48",
            "tside_gender": "Female",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Sharpstar_Rotator_M54": {
            "brand": "Sharpstar",
            "name": "Rotator (M54)",
            "type": "type_rotator",
            "optical_length": 12,
            "mass": 300,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Sharpstar_Rotator_M48(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_Rotator_M48'])

    @classmethod
    def Sharpstar_Rotator_M54(cls):
        return cls.from_database(cls._DATABASE['Sharpstar_Rotator_M54'])
