from ..base import FlipMirror


class WilliamOpticsFlipMirror(FlipMirror):
    _DATABASE = {
        "William_Optics_Flip_Mirror": {
            "brand": "William Optics",
            "name": "Flip Mirror",
            "type": "type_flip_mirror",
            "optical_length": 0,
            "mass": 550,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def William_Optics_Flip_Mirror(cls):
        return cls.from_database(cls._DATABASE["William_Optics_Flip_Mirror"])
