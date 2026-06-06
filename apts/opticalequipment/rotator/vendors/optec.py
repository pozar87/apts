from ..base import Rotator


class OptecRotator(Rotator):
    _DATABASE = {
        "Optec_Gemini_Rotator_M68": {
            "brand": "Optec",
            "name": "Gemini Rotator (M68)",
            "type": "type_rotator",
            "optical_length": 12,
            "mass": 500,
            "tside_thread": "M68",
            "tside_gender": "Female",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Optec_Gemini_Rotator_M54": {
            "brand": "Optec",
            "name": "Gemini Rotator (M54)",
            "type": "type_rotator",
            "optical_length": 12,
            "mass": 450,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Optec_Gemini_Rotator_M68(cls):
        return cls.from_database(cls._DATABASE['Optec_Gemini_Rotator_M68'])

    @classmethod
    def Optec_Gemini_Rotator_M54(cls):
        return cls.from_database(cls._DATABASE['Optec_Gemini_Rotator_M54'])
