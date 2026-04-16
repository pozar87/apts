from ..base import FlipMirror


class BresserFlipMirror(FlipMirror):
    _DATABASE = {
        "Bresser_Flip_Mirror": {
            "brand": "Bresser",
            "name": "Flip Mirror",
            "type": "type_flip_mirror",
            "optical_length": 0,
            "mass": 470,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Bresser_Flip_Mirror(cls):
        return cls.from_database(cls._DATABASE["Bresser_Flip_Mirror"])
