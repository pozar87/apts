from ..base import OAG


class SharpstarOAG(OAG):
    _DATABASE = {
        "Sharpstar_OAG_M48": {
            "brand": "Sharpstar",
            "name": "OAG (M48)",
            "type": "type_oag",
            "optical_length": 17,
            "mass": 185,
            "tside_thread": "M48",
            "tside_gender": "Male",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Sharpstar_OAG_M54": {
            "brand": "Sharpstar",
            "name": "OAG (M54)",
            "type": "type_oag",
            "optical_length": 20,
            "mass": 280,
            "tside_thread": "M54",
            "tside_gender": "Male",
            "cside_thread": "M54",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Sharpstar_OAG_M48(cls):
        return cls.from_database(cls._DATABASE["Sharpstar_OAG_M48"])

    @classmethod
    def Sharpstar_OAG_M54(cls):
        return cls.from_database(cls._DATABASE["Sharpstar_OAG_M54"])
