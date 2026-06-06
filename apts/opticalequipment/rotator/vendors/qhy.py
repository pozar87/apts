from ..base import Rotator


class QhyRotator(Rotator):
    _DATABASE = {
        "QHY_Camera_Rotator_M42": {
            "brand": "QHY",
            "name": "Camera Rotator (M42)",
            "type": "type_rotator",
            "optical_length": 10,
            "mass": 200,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "QHY_Camera_Rotator_M54": {
            "brand": "QHY",
            "name": "Camera Rotator (M54)",
            "type": "type_rotator",
            "optical_length": 12,
            "mass": 280,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def QHY_Camera_Rotator_M42(cls):
        return cls.from_database(cls._DATABASE['QHY_Camera_Rotator_M42'])

    @classmethod
    def QHY_Camera_Rotator_M54(cls):
        return cls.from_database(cls._DATABASE['QHY_Camera_Rotator_M54'])
