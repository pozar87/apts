from ..base import FlipMirror


class SaxonFlipMirror(FlipMirror):
    _DATABASE = {
        "Saxon_Flip_Mirror": {
            "brand": "Saxon",
            "name": "Flip Mirror",
            "type": "type_flip_mirror",
            "optical_length": 0,
            "mass": 450,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Saxon_Flip_Mirror(cls):
        return cls.from_database(cls._DATABASE["Saxon_Flip_Mirror"])
