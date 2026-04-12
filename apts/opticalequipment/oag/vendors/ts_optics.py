from ..base import OAG


class Ts_opticsOAG(OAG):
    _DATABASE = {
        "TS_Optics_OAG_M48": {
            "brand": "TS-Optics",
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
        "TS_Optics_OAG_M54": {
            "brand": "TS-Optics",
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
    def TS_Optics_OAG_M48(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_OAG_M48"])

    @classmethod
    def TS_Optics_OAG_M54(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_OAG_M54"])
