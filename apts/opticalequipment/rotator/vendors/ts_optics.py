from ..base import Rotator


class TsOpticsRotator(Rotator):
    _DATABASE = {
        "TS_Optics_TSRot2_M54": {
            "brand": "TS-Optics",
            "name": "TSRot2 (M54)",
            "type": "type_rotator",
            "optical_length": 12,
            "mass": 320,
            "tside_thread": "M54",
            "tside_gender": "Male",
            "cside_thread": "M54",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def TS_Optics_TSRot2_M54(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_TSRot2_M54"])
