from ..base import FlipMirror


class CelestronFlipMirror(FlipMirror):
    _DATABASE = {
        "Celestron_Flip_Mirror": {
            "brand": "Celestron",
            "name": "Flip Mirror",
            "type": "type_flip_mirror",
            "optical_length": 0,
            "mass": 480,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Celestron_Flip_Mirror(cls):
        return cls.from_database(cls._DATABASE["Celestron_Flip_Mirror"])
