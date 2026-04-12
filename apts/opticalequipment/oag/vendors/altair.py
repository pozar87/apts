from ..base import OAG


class AltairOAG(OAG):
    _DATABASE = {
        "Altair_OAG_M42": {
            "brand": "Altair",
            "name": "OAG (M42)",
            "type": "type_oag",
            "optical_length": 16,
            "mass": 170,
            "tside_thread": "M42",
            "tside_gender": "Male",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Altair_OAG_M54": {
            "brand": "Altair",
            "name": "OAG (M54)",
            "type": "type_oag",
            "optical_length": 19,
            "mass": 280,
            "tside_thread": "M54",
            "tside_gender": "Male",
            "cside_thread": "M54",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Altair_Deluxe_OAG_M48": {
            "brand": "Altair",
            "name": "Deluxe OAG (M48)",
            "type": "type_oag",
            "optical_length": 17,
            "mass": 200,
            "tside_thread": "M48",
            "tside_gender": "Male",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Altair_Deluxe_OAG_M54": {
            "brand": "Altair",
            "name": "Deluxe OAG (M54)",
            "type": "type_oag",
            "optical_length": 20,
            "mass": 290,
            "tside_thread": "M54",
            "tside_gender": "Male",
            "cside_thread": "M54",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Altair_OAG_M42(cls):
        return cls.from_database(cls._DATABASE["Altair_OAG_M42"])

    @classmethod
    def Altair_OAG_M54(cls):
        return cls.from_database(cls._DATABASE["Altair_OAG_M54"])

    @classmethod
    def Altair_Deluxe_OAG_M48(cls):
        return cls.from_database(cls._DATABASE["Altair_Deluxe_OAG_M48"])

    @classmethod
    def Altair_Deluxe_OAG_M54(cls):
        return cls.from_database(cls._DATABASE["Altair_Deluxe_OAG_M54"])
