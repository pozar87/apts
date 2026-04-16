from ..base import FlipMirror


class OmegonFlipMirror(FlipMirror):
    _DATABASE = {
        "Omegon_Flip_Mirror": {
            "brand": "Omegon",
            "name": "Flip Mirror",
            "type": "type_flip_mirror",
            "optical_length": 0,
            "mass": 490,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Omegon_Flip_Mirror(cls):
        return cls.from_database(cls._DATABASE["Omegon_Flip_Mirror"])
