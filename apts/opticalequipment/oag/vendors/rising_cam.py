from ..base import OAG


class Rising_camOAG(OAG):
    _DATABASE = {
        "Rising_Cam_OAG_M42": {
            "brand": "Rising Cam",
            "name": "OAG (M42)",
            "type": "type_oag",
            "optical_length": 15,
            "mass": 160,
            "tside_thread": "M42",
            "tside_gender": "Male",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Rising_Cam_OAG_M42(cls):
        return cls.from_database(cls._DATABASE["Rising_Cam_OAG_M42"])
