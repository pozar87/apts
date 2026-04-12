from ..base import OAG


class OmegonOAG(OAG):
    _DATABASE = {
        "Omegon_OAG_M42": {
            "brand": "Omegon",
            "name": "OAG (M42)",
            "type": "type_oag",
            "optical_length": 15,
            "mass": 165,
            "tside_thread": "M42",
            "tside_gender": "Male",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Omegon_OAG_M48": {
            "brand": "Omegon",
            "name": "OAG (M48)",
            "type": "type_oag",
            "optical_length": 17,
            "mass": 190,
            "tside_thread": "M48",
            "tside_gender": "Male",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Omegon_OAG_M42(cls):
        return cls.from_database(cls._DATABASE["Omegon_OAG_M42"])

    @classmethod
    def Omegon_OAG_M48(cls):
        return cls.from_database(cls._DATABASE["Omegon_OAG_M48"])
