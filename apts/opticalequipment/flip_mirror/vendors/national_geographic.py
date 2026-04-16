from ..base import FlipMirror


class NationalGeographicFlipMirror(FlipMirror):
    _DATABASE = {
        "National_Geographic_Flip_Mirror": {
            "brand": "National Geographic",
            "name": "Flip Mirror",
            "type": "type_flip_mirror",
            "optical_length": 0,
            "mass": 420,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def National_Geographic_Flip_Mirror(cls):
        return cls.from_database(cls._DATABASE["National_Geographic_Flip_Mirror"])
