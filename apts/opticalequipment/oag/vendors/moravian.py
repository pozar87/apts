from ..base import OAG


class MoravianOAG(OAG):
    _DATABASE = {
        "Moravian_OAG_M54": {
            "brand": "Moravian",
            "name": "OAG (M54)",
            "type": "type_oag",
            "optical_length": 18,
            "mass": 260,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Moravian_OAG_M54(cls):
        return cls.from_database(cls._DATABASE['Moravian_OAG_M54'])
