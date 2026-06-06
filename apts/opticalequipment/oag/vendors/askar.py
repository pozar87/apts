from ..base import OAG


class AskarOAG(OAG):
    _DATABASE = {
        "Askar_OAG_M48": {
            "brand": "Askar",
            "name": "OAG (M48)",
            "type": "type_oag",
            "optical_length": 17,
            "mass": 195,
            "tside_thread": "M48",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_OAG_M54": {
            "brand": "Askar",
            "name": "OAG (M54)",
            "type": "type_oag",
            "optical_length": 20,
            "mass": 290,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Askar_OAG_M48(cls):
        return cls.from_database(cls._DATABASE['Askar_OAG_M48'])

    @classmethod
    def Askar_OAG_M54(cls):
        return cls.from_database(cls._DATABASE['Askar_OAG_M54'])
