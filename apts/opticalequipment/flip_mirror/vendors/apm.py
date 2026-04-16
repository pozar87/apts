from ..base import FlipMirror


class APMFlipMirror(FlipMirror):
    _DATABASE = {
        "APM_Flipmirror": {
            "brand": "APM",
            "name": "Flipmirror",
            "type": "type_flip_mirror",
            "optical_length": 0,
            "mass": 510,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def APM_Flipmirror(cls):
        return cls.from_database(cls._DATABASE["APM_Flipmirror"])
