from ..base import AntiTilt


class StellarvueAntiTilt(AntiTilt):
    _DATABASE = {
        "Stellarvue_Tilt_Plate_M48": {
            "brand": "Stellarvue",
            "name": "Tilt Plate (M48)",
            "type": "type_anti_tilt",
            "optical_length": 5,
            "mass": 45,
            "tside_thread": "M48",
            "tside_gender": "Female",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Stellarvue_Tilt_Plate_M68": {
            "brand": "Stellarvue",
            "name": "Tilt Plate (M68)",
            "type": "type_anti_tilt",
            "optical_length": 5,
            "mass": 60,
            "tside_thread": "M68",
            "tside_gender": "Female",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Stellarvue_Tilt_Plate_M48(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_Tilt_Plate_M48'])

    @classmethod
    def Stellarvue_Tilt_Plate_M68(cls):
        return cls.from_database(cls._DATABASE['Stellarvue_Tilt_Plate_M68'])
