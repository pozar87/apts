from ..base import OAG


class BaaderOAG(OAG):
    _DATABASE = {
        "Baader_FlipMirror_OAG": {
            "brand": "Baader",
            "name": "FlipMirror OAG",
            "type": "type_oag",
            "optical_length": 20,
            "mass": 300,
            "tside_thread": "M48",
            "tside_gender": "Male",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Baader_FlipMirror_OAG(cls):
        return cls.from_database(cls._DATABASE["Baader_FlipMirror_OAG"])
