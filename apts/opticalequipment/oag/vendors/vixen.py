from ..base import OAG


class VixenOAG(OAG):
    _DATABASE = {
        "Vixen_OAG_M42": {
            "brand": "Vixen",
            "name": "OAG (M42)",
            "type": "type_oag",
            "optical_length": 16,
            "mass": 180,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Vixen_OAG_M42(cls):
        return cls.from_database(cls._DATABASE['Vixen_OAG_M42'])
