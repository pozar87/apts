from ..base import FlipMirror


class OrionFlipMirror(FlipMirror):
    _DATABASE = {
        "Orion_Flip_Mirror": {
            "brand": "Orion",
            "name": "Flip Mirror",
            "type": "type_flip_mirror",
            "optical_length": 0,
            "mass": 520,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Orion_Flip_Mirror(cls):
        return cls.from_database(cls._DATABASE["Orion_Flip_Mirror"])
