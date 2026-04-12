from ..base import Rotator


class ArcoRotator(Rotator):
    _DATABASE = {
        "ARCO_2_Camera_Rotator_M48": {
            "brand": "ARCO",
            "name": '2" Camera Rotator (M48)',
            "type": "type_rotator",
            "optical_length": 12,
            "mass": 400,
            "tside_thread": "M48",
            "tside_gender": "Male",
            "cside_thread": "M48",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "ARCO_2_Camera_Rotator_M54": {
            "brand": "ARCO",
            "name": '2" Camera Rotator (M54)',
            "type": "type_rotator",
            "optical_length": 12,
            "mass": 420,
            "tside_thread": "M54",
            "tside_gender": "Male",
            "cside_thread": "M54",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "ARCO_2_Camera_Rotator_M68": {
            "brand": "ARCO",
            "name": '2" Camera Rotator (M68)',
            "type": "type_rotator",
            "optical_length": 12,
            "mass": 450,
            "tside_thread": "M68",
            "tside_gender": "Male",
            "cside_thread": "M68",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def ARCO_2_Camera_Rotator_M48(cls):
        return cls.from_database(cls._DATABASE["ARCO_2_Camera_Rotator_M48"])

    @classmethod
    def ARCO_2_Camera_Rotator_M54(cls):
        return cls.from_database(cls._DATABASE["ARCO_2_Camera_Rotator_M54"])

    @classmethod
    def ARCO_2_Camera_Rotator_M68(cls):
        return cls.from_database(cls._DATABASE["ARCO_2_Camera_Rotator_M68"])
