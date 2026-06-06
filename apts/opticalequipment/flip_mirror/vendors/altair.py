from ..base import FlipMirror


class AltairFlipMirror(FlipMirror):
    _DATABASE = {
        "Altair_Flipmirror": {
            "brand": "Altair",
            "name": "Flipmirror",
            "type": "type_flip_mirror",
            "optical_length": 0,
            "mass": 480,
            "tside_thread": "2\"",
            "tside_gender": "Male",
            "cside_thread": "1.25\"",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Altair_Flipmirror(cls):
        return cls.from_database(cls._DATABASE["Altair_Flipmirror"])
