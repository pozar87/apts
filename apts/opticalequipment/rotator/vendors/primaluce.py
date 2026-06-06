from ..base import Rotator


class PrimaLuceRotator(Rotator):
    _DATABASE = {
        "PrimaLuce_EAGLE_Rotator_M48": {
            "brand": "PrimaLuce",
            "name": "EAGLE Rotator (M48)",
            "type": "type_rotator",
            "optical_length": 12,
            "mass": 350,
            "tside_thread": "M48",
            "tside_gender": "Female",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "PrimaLuce_EAGLE_Rotator_M54": {
            "brand": "PrimaLuce",
            "name": "EAGLE Rotator (M54)",
            "type": "type_rotator",
            "optical_length": 12,
            "mass": 380,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "PrimaLuce_EAGLE_Rotator_M68": {
            "brand": "PrimaLuce",
            "name": "EAGLE Rotator (M68)",
            "type": "type_rotator",
            "optical_length": 12,
            "mass": 420,
            "tside_thread": "M68",
            "tside_gender": "Female",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def PrimaLuce_EAGLE_Rotator_M48(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_EAGLE_Rotator_M48'])

    @classmethod
    def PrimaLuce_EAGLE_Rotator_M54(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_EAGLE_Rotator_M54'])

    @classmethod
    def PrimaLuce_EAGLE_Rotator_M68(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_EAGLE_Rotator_M68'])
