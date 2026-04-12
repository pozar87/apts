from ..base import AntiTilt


class GerdNeumannAntiTilt(AntiTilt):
    _DATABASE = {
        "Gerd_Neumann_Tilt_Plate_M48": {
            "brand": "Gerd Neumann",
            "name": "Tilt Plate (M48)",
            "type": "type_anti_tilt",
            "optical_length": 4,
            "mass": 45,
            "tside_thread": "M48",
            "tside_gender": "Male",
            "cside_thread": "M48",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Gerd_Neumann_Tilt_Plate_M54": {
            "brand": "Gerd Neumann",
            "name": "Tilt Plate (M54)",
            "type": "type_anti_tilt",
            "optical_length": 4,
            "mass": 55,
            "tside_thread": "M54",
            "tside_gender": "Male",
            "cside_thread": "M54",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Gerd_Neumann_Tilt_Plate_M68": {
            "brand": "Gerd Neumann",
            "name": "Tilt Plate (M68)",
            "type": "type_anti_tilt",
            "optical_length": 4,
            "mass": 70,
            "tside_thread": "M68",
            "tside_gender": "Male",
            "cside_thread": "M68",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Gerd_Neumann_Tilt_Plate_M48(cls):
        return cls.from_database(cls._DATABASE["Gerd_Neumann_Tilt_Plate_M48"])

    @classmethod
    def Gerd_Neumann_Tilt_Plate_M54(cls):
        return cls.from_database(cls._DATABASE["Gerd_Neumann_Tilt_Plate_M54"])

    @classmethod
    def Gerd_Neumann_Tilt_Plate_M68(cls):
        return cls.from_database(cls._DATABASE["Gerd_Neumann_Tilt_Plate_M68"])
