from ..base import FlipMirror


class TSOpticsFlipMirror(FlipMirror):
    _DATABASE = {
        "TS_Optics_Flip_Mirror": {
            "brand": "TS-Optics",
            "name": "Flip Mirror",
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
    def TS_Optics_Flip_Mirror(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Flip_Mirror"])
