from ..base import Rotator


class AskarRotator(Rotator):
    _DATABASE = {
        "Askar_Rotator_M48": {
            "brand": "Askar",
            "name": "Rotator (M48)",
            "type": "type_rotator",
            "optical_length": 11,
            "mass": 280,
            "tside_thread": "M48",
            "tside_gender": "Female",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_Rotator_M54": {
            "brand": "Askar",
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
    def Askar_Rotator_M48(cls):
        return cls.from_database(cls._DATABASE['Askar_Rotator_M48'])

    @classmethod
    def Askar_Rotator_M54(cls):
        return cls.from_database(cls._DATABASE['Askar_Rotator_M54'])
