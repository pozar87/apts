from ..base import FlipMirror


class BaaderFlipMirror(FlipMirror):
    _DATABASE = {
        "Baader_Flipmirror_II": {
            "brand": "Baader",
            "name": "Flipmirror II",
            "type": "type_flip_mirror",
            "optical_length": 0,
            "mass": 600,
            "tside_thread": "2\"",
            "tside_gender": "Male",
            "cside_thread": "1.25\"",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Baader_Flipmirror_II(cls):
        return cls.from_database(cls._DATABASE["Baader_Flipmirror_II"])
