from ..base import OAG


class BresserOAG(OAG):
    _DATABASE = {
        "Bresser_OAG_M42": {
            "brand": "Bresser",
            "name": "OAG (M42)",
            "type": "type_oag",
            "optical_length": 15,
            "mass": 160,
            "tside_thread": "M42",
            "tside_gender": "Male",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Bresser_OAG_M42(cls):
        return cls.from_database(cls._DATABASE["Bresser_OAG_M42"])
