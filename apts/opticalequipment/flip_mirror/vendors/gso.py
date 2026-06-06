from ..base import FlipMirror


class GSOFlipMirror(FlipMirror):
    _DATABASE = {
        "GSO_Flip_Mirror": {
            "brand": "GSO",
            "name": "Flip Mirror",
            "type": "type_flip_mirror",
            "optical_length": 0,
            "mass": 500,
            "tside_thread": "2\"",
            "tside_gender": "Male",
            "cside_thread": "1.25\"",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def GSO_Flip_Mirror(cls):
        return cls.from_database(cls._DATABASE["GSO_Flip_Mirror"])
