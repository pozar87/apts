from ..base import OAG


class PegasusOAG(OAG):
    _DATABASE = {
        "Pegasus_OAG_M42": {
            "brand": "Pegasus",
            "name": "OAG (M42)",
            "type": "type_oag",
            "optical_length": 16,
            "mass": 175,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Pegasus_OAG_M54": {
            "brand": "Pegasus",
            "name": "OAG (M54)",
            "type": "type_oag",
            "optical_length": 19,
            "mass": 280,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Pegasus_OAG_M42(cls):
        return cls.from_database(cls._DATABASE['Pegasus_OAG_M42'])

    @classmethod
    def Pegasus_OAG_M54(cls):
        return cls.from_database(cls._DATABASE['Pegasus_OAG_M54'])
