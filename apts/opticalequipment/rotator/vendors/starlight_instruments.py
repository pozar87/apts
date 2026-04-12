from ..base import Rotator


class StarlightInstrumentsRotator(Rotator):
    _DATABASE = {
        "Starlight_Instruments_Rotator_M42": {
            "brand": "Starlight Instruments",
            "name": "Rotator (M42)",
            "type": "type_rotator",
            "optical_length": 10,
            "mass": 200,
            "tside_thread": "M42",
            "tside_gender": "Male",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Starlight_Instruments_Rotator_M48": {
            "brand": "Starlight Instruments",
            "name": "Rotator (M48)",
            "type": "type_rotator",
            "optical_length": 11,
            "mass": 250,
            "tside_thread": "M48",
            "tside_gender": "Male",
            "cside_thread": "M48",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Starlight_Instruments_Rotator_M54": {
            "brand": "Starlight Instruments",
            "name": "Rotator (M54)",
            "type": "type_rotator",
            "optical_length": 12,
            "mass": 300,
            "tside_thread": "M54",
            "tside_gender": "Male",
            "cside_thread": "M54",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Starlight_Instruments_Rotator_M42(cls):
        return cls.from_database(cls._DATABASE["Starlight_Instruments_Rotator_M42"])

    @classmethod
    def Starlight_Instruments_Rotator_M48(cls):
        return cls.from_database(cls._DATABASE["Starlight_Instruments_Rotator_M48"])

    @classmethod
    def Starlight_Instruments_Rotator_M54(cls):
        return cls.from_database(cls._DATABASE["Starlight_Instruments_Rotator_M54"])
