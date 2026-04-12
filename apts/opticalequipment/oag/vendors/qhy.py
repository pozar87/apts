from ..base import OAG


class QhyOAG(OAG):
    _DATABASE = {
        "QHY_OAG_M_M48_M42": {
            "brand": "QHY",
            "name": "OAG-M (M48→M42)",
            "type": "type_oag",
            "optical_length": 18,
            "mass": 250,
            "tside_thread": "M48",
            "tside_gender": "Male",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "QHY_OAG_S_M42": {
            "brand": "QHY",
            "name": "OAG-S (M42)",
            "type": "type_oag",
            "optical_length": 14,
            "mass": 180,
            "tside_thread": "M42",
            "tside_gender": "Male",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "QHY_OAG_L_M54": {
            "brand": "QHY",
            "name": "OAG-L (M54)",
            "type": "type_oag",
            "optical_length": 21,
            "mass": 350,
            "tside_thread": "M54",
            "tside_gender": "Male",
            "cside_thread": "M54",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def QHY_OAG_M_M48_M42(cls):
        return cls.from_database(cls._DATABASE["QHY_OAG_M_M48_M42"])

    @classmethod
    def QHY_OAG_S_M42(cls):
        return cls.from_database(cls._DATABASE["QHY_OAG_S_M42"])

    @classmethod
    def QHY_OAG_L_M54(cls):
        return cls.from_database(cls._DATABASE["QHY_OAG_L_M54"])
