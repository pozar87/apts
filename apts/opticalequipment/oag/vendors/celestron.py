from ..base import OAG


class CelestronOAG(OAG):
    _DATABASE = {
        "Celestron_OAG_SCT": {
            "brand": "Celestron",
            "name": "OAG (SCT)",
            "type": "type_oag",
            "optical_length": 19,
            "mass": 200,
            "tside_thread": "SC (Schmidt-Cassegrain)",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Celestron_OAG_SCT(cls):
        return cls.from_database(cls._DATABASE['Celestron_OAG_SCT'])
