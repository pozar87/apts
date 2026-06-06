from ..base import Focuser


class PrimaLuceFocuser(Focuser):
    _DATABASE = {
        "PrimaLuce_ESATTO_2": {
            "brand": "PrimaLuce",
            "name": "ESATTO 2\"",
            "type": "type_focuser",
            "optical_length": 50,
            "mass": 670,
            "tside_thread": "M56",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "PrimaLuce_ESATTO_3": {
            "brand": "PrimaLuce",
            "name": "ESATTO 3\"",
            "type": "type_focuser",
            "optical_length": 58,
            "mass": 1300,
            "tside_thread": "SC (Schmidt-Cassegrain)",
            "tside_gender": "Female",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "PrimaLuce_SESTO_SENSO_2": {
            "brand": "PrimaLuce",
            "name": "SESTO SENSO 2",
            "type": "type_focuser",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": "",
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "PrimaLuce_GIOTTO": {
            "brand": "PrimaLuce",
            "name": "GIOTTO",
            "type": "type_focuser",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": "",
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def PrimaLuce_ESATTO_2(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_ESATTO_2'])

    @classmethod
    def PrimaLuce_ESATTO_3(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_ESATTO_3'])

    @classmethod
    def PrimaLuce_SESTO_SENSO_2(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_SESTO_SENSO_2'])

    @classmethod
    def PrimaLuce_GIOTTO(cls):
        return cls.from_database(cls._DATABASE['PrimaLuce_GIOTTO'])
