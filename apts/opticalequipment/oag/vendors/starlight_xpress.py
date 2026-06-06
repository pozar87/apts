from ..base import OAG


class Starlight_xpressOAG(OAG):
    _DATABASE = {
        "Starlight_Xpress_Lodestar_OAG": {
            "brand": "Starlight Xpress",
            "name": "Lodestar OAG",
            "type": "type_oag",
            "optical_length": 15,
            "mass": 160,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Starlight_Xpress_Lodestar_OAG(cls):
        return cls.from_database(cls._DATABASE['Starlight_Xpress_Lodestar_OAG']
            )
