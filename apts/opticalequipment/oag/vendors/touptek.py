from ..base import OAG


class TouptekOAG(OAG):
    _DATABASE = {
        "ToupTek_OAG_M42": {
            "brand": "ToupTek",
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
    }

    @classmethod
    def ToupTek_OAG_M42(cls):
        return cls.from_database(cls._DATABASE["ToupTek_OAG_M42"])
