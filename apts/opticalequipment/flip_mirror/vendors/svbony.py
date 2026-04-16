from ..base import FlipMirror


class SVBonyFlipMirror(FlipMirror):
    _DATABASE = {
        "SVBony_SV211_Flip_Mirror": {
            "brand": "SVBony",
            "name": "SV211 Flip Mirror",
            "type": "type_flip_mirror",
            "optical_length": 0,
            "mass": 460,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "SVBony_SV123_Flipmirror": {
            "brand": "SVBony",
            "name": "SV123 Flipmirror",
            "type": "type_flip_mirror",
            "optical_length": 0,
            "mass": 400,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def SVBony_SV211_Flip_Mirror(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV211_Flip_Mirror"])

    @classmethod
    def SVBony_SV123_Flipmirror(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV123_Flipmirror"])
