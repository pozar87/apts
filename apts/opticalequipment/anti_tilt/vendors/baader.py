from ..base import AntiTilt


class BaaderAntiTilt(AntiTilt):
    _DATABASE = {
        "Baader_Anti_tilt_Adapter_M42": {
            "brand": "Baader",
            "name": "Anti-tilt Adapter (M42)",
            "type": "type_anti_tilt",
            "optical_length": 5,
            "mass": 60,
            "tside_thread": "M42",
            "tside_gender": "Male",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Anti_tilt_Adapter_M48": {
            "brand": "Baader",
            "name": "Anti-tilt Adapter (M48)",
            "type": "type_anti_tilt",
            "optical_length": 5,
            "mass": 70,
            "tside_thread": "M48",
            "tside_gender": "Male",
            "cside_thread": "M48",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Anti_tilt_Adapter_M54": {
            "brand": "Baader",
            "name": "Anti-tilt Adapter (M54)",
            "type": "type_anti_tilt",
            "optical_length": 5,
            "mass": 80,
            "tside_thread": "M54",
            "tside_gender": "Male",
            "cside_thread": "M54",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Anti_tilt_Adapter_M68": {
            "brand": "Baader",
            "name": "Anti-tilt Adapter (M68)",
            "type": "type_anti_tilt",
            "optical_length": 5,
            "mass": 100,
            "tside_thread": "M68",
            "tside_gender": "Male",
            "cside_thread": "M68",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Baader_Anti_tilt_Adapter_M42(cls):
        return cls.from_database(cls._DATABASE["Baader_Anti_tilt_Adapter_M42"])

    @classmethod
    def Baader_Anti_tilt_Adapter_M48(cls):
        return cls.from_database(cls._DATABASE["Baader_Anti_tilt_Adapter_M48"])

    @classmethod
    def Baader_Anti_tilt_Adapter_M54(cls):
        return cls.from_database(cls._DATABASE["Baader_Anti_tilt_Adapter_M54"])

    @classmethod
    def Baader_Anti_tilt_Adapter_M68(cls):
        return cls.from_database(cls._DATABASE["Baader_Anti_tilt_Adapter_M68"])
