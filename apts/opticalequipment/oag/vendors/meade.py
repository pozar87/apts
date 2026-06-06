from ..base import OAG


class MeadeOAG(OAG):
    _DATABASE = {
        "Meade_OAG_SCT": {
            "brand": "Meade",
            "name": "OAG (SCT)",
            "type": "type_oag",
            "optical_length": 19,
            "mass": 210,
            "tside_thread": "SC (Schmidt-Cassegrain)",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Meade_OAG_SCT(cls):
        return cls.from_database(cls._DATABASE['Meade_OAG_SCT'])
