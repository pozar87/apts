from ..base import Telescope


class ZhumellTelescope(Telescope):
    _DATABASE = {
        "Zhumell_Z6_Dobsonian": {
            "brand": "Zhumell",
            "name": "Z6 Dobsonian",
            "type": "newtonian_reflector",
            "optical_length": 0,
            "mass": 8255,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "2\"",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
            "aperture_mm": 152.4,  # Verified via GSO OEM / High Point Scientific (6" = 152.4mm)
            "focal_length_mm": 1200,
            "central_obstruction_mm": 31,  # Verified via GSO OEM mirror set specs (31mm secondary minor axis)
        },
        "Zhumell_Z8_Dobsonian": {
            "brand": "Zhumell",
            "name": "Z8 Dobsonian",
            "type": "newtonian_reflector",
            "optical_length": 0,
            "mass": 11113,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "2\"",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
            "aperture_mm": 203.2,  # Verified via GSO OEM / High Point Scientific (8" = 203.2mm)
            "focal_length_mm": 1200,
            "central_obstruction_mm": 50,  # Verified via GSO OEM mirror set specs (50mm secondary minor axis)
        },
        "Zhumell_Z10_Dobsonian": {
            "brand": "Zhumell",
            "name": "Z10 Dobsonian",
            "type": "newtonian_reflector",
            "optical_length": 0,
            "mass": 15785,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "2\"",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
            "aperture_mm": 254,  # Verified via GSO OEM (10" = 254mm)
            "focal_length_mm": 1250,
            "central_obstruction_mm": 63,  # Verified via GSO OEM mirror set specs (63mm / 2.48" secondary minor axis)
        },
        "Zhumell_Z12_Dobsonian": {
            "brand": "Zhumell",
            "name": "Z12 Dobsonian",
            "type": "newtonian_reflector",
            "optical_length": 0,
            "mass": 21682,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "2\"",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
            "aperture_mm": 304.8,  # Verified via GSO OEM (12" = 304.8mm)
            "focal_length_mm": 1520,
            "central_obstruction_mm": 70,  # Verified via GSO OEM mirror set specs (70mm / 2.76" secondary minor axis)
        },
        "Zhumell_Z16_Dobsonian": {
            "brand": "Zhumell",
            "name": "Z16 Dobsonian",
            "type": "newtonian_reflector",
            "optical_length": 0,
            "mass": 34246,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "2\"",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
            "aperture_mm": 406.4,  # Verified via GSO OEM (16" = 406.4mm)
            "focal_length_mm": 1800,
            "central_obstruction_mm": 88,  # Verified via GSO OEM mirror set specs (88mm secondary minor axis)
        },
    }

    @classmethod
    def Zhumell_Z6_Dobsonian(cls):
        return cls.from_database(cls._DATABASE['Zhumell_Z6_Dobsonian'])

    @classmethod
    def Zhumell_Z8_Dobsonian(cls):
        return cls.from_database(cls._DATABASE['Zhumell_Z8_Dobsonian'])

    @classmethod
    def Zhumell_Z10_Dobsonian(cls):
        return cls.from_database(cls._DATABASE['Zhumell_Z10_Dobsonian'])

    @classmethod
    def Zhumell_Z12_Dobsonian(cls):
        return cls.from_database(cls._DATABASE['Zhumell_Z12_Dobsonian'])

    @classmethod
    def Zhumell_Z14_Dobsonian(cls):
        return cls.from_database(cls._DATABASE['Zhumell_Z14_Dobsonian'])

    @classmethod
    def Zhumell_Z16_Dobsonian(cls):
        return cls.from_database(cls._DATABASE['Zhumell_Z16_Dobsonian'])
