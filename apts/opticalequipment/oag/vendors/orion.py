from ..base import OAG


class OrionOAG(OAG):
    _DATABASE = {
        "Orion_Thin_OAG_M48": {
            "brand": "Orion",
            "name": "Thin OAG (M48)",
            "type": "type_oag",
            "optical_length": 12,
            "mass": 170,
            "tside_thread": "M48",
            "tside_gender": "Male",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Orion_Thin_OAG_M48(cls):
        return cls.from_database(cls._DATABASE["Orion_Thin_OAG_M48"])
