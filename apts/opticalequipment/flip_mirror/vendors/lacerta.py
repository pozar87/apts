from ..base import FlipMirror


class LacertaFlipMirror(FlipMirror):
    _DATABASE = {
        "Lacerta_Flip_Mirror": {
            "brand": "Lacerta",
            "name": "Flip Mirror",
            "type": "type_flip_mirror",
            "optical_length": 0,
            "mass": 500,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_Flipmirror": {
            "brand": "Lacerta",
            "name": "Flipmirror",
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
    def Lacerta_Flip_Mirror(cls):
        return cls.from_database(cls._DATABASE["Lacerta_Flip_Mirror"])

    @classmethod
    def Lacerta_Flipmirror(cls):
        return cls.from_database(cls._DATABASE["Lacerta_Flipmirror"])
