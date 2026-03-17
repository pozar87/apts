from ..base import Telescope


class MeadeTelescope(Telescope):
    _DATABASE = {
        "Meade_LX85_ACF_6": {
            "brand": "Meade",
            "name": 'LX85 ACF 6"',
            "type": "catadioptric",
            "optical_length": 0,
            "mass": 4490,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
            "aperture_mm": 152.4,
            "focal_length_mm": 1524,
            "central_obstruction_mm": 56,
        },  # Verified via OPT/Meade specs (9.9 lbs OTA)
        "Meade_LX85_ACF_8": {
            "brand": "Meade",
            "name": 'LX85 ACF 8"',
            "type": "catadioptric",
            "optical_length": 0,
            "mass": 5760,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
            "aperture_mm": 203.2,
            "focal_length_mm": 2032,
            "central_obstruction_mm": 76,
        },  # Verified via Levenhuk/Meade specs (12.7 lbs OTA)
        "Meade_LX200_ACF_8": {
            "brand": "Meade",
            "name": 'LX200 ACF 8"',
            "type": "catadioptric",
            "optical_length": 0,
            "mass": 6350,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
            "aperture_mm": 203.2,
            "focal_length_mm": 2032,
            "central_obstruction_mm": 76,
        },  # Verified via Agena/Meade specs (14 lbs OTA)
        "Meade_LX200_ACF_10": {
            "brand": "Meade",
            "name": 'LX200 ACF 10"',
            "type": "catadioptric",
            "optical_length": 0,
            "mass": 11790,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
            "aperture_mm": 254.0,
            "focal_length_mm": 2540,
            "central_obstruction_mm": 94,
        },  # Verified via Meade specs (26 lbs OTA)
        "Meade_LX200_ACF_12": {
            "brand": "Meade",
            "name": 'LX200 ACF 12"',
            "type": "catadioptric",
            "optical_length": 0,
            "mass": 16330,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
            "aperture_mm": 304.8,
            "focal_length_mm": 3048,
            "central_obstruction_mm": 102,
        },  # Verified via Meade specs (36 lbs OTA)
        "Meade_LX200_ACF_14": {
            "brand": "Meade",
            "name": 'LX200 ACF 14"',
            "type": "catadioptric",
            "optical_length": 0,
            "mass": 22680,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
            "aperture_mm": 355.6,
            "focal_length_mm": 3556,
            "central_obstruction_mm": 117,
        },  # Verified via Meade specs (50 lbs OTA)
        "Meade_LX200_ACF_16": {
            "brand": "Meade",
            "name": 'LX200 ACF 16"',
            "type": "catadioptric",
            "optical_length": 0,
            "mass": 30390,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
            "aperture_mm": 406.4,
            "focal_length_mm": 4064,
            "central_obstruction_mm": 127,
        },  # Verified via Meade specs (67 lbs OTA)
        "Meade_LX600_ACF_10": {
            "brand": "Meade",
            "name": 'LX600 ACF 10"',
            "type": "catadioptric",
            "optical_length": 0,
            "mass": 12250,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
            "aperture_mm": 254.0,
            "focal_length_mm": 2032,
            "central_obstruction_mm": 121,
        },  # Verified via Space Arcade/Meade (f/8, 121mm CO, ~27 lbs OTA)
        "Meade_LX600_ACF_12": {
            "brand": "Meade",
            "name": 'LX600 ACF 12"',
            "type": "catadioptric",
            "optical_length": 0,
            "mass": 16780,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
            "aperture_mm": 304.8,
            "focal_length_mm": 2438,
            "central_obstruction_mm": 146,
        },  # Verified via Meade (f/8, 48% CO by diameter, ~37 lbs OTA)
        "Meade_LX600_ACF_14": {
            "brand": "Meade",
            "name": 'LX600 ACF 14"',
            "type": "catadioptric",
            "optical_length": 0,
            "mass": 23130,
            "tside_thread": "",
            "tside_gender": "",
            "cside_thread": "SC (Schmidt-Cassegrain)",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
            "aperture_mm": 355.6,
            "focal_length_mm": 2845,
            "central_obstruction_mm": 171,
        },  # Verified via Meade (f/8, 48% CO by diameter, ~51 lbs OTA)
    }

    @classmethod
    def Meade_LX85_ACF_6(cls):
        return cls.from_database(cls._DATABASE["Meade_LX85_ACF_6"])

    @classmethod
    def Meade_LX85_ACF_8(cls):
        return cls.from_database(cls._DATABASE["Meade_LX85_ACF_8"])

    @classmethod
    def Meade_LX200_ACF_8(cls):
        return cls.from_database(cls._DATABASE["Meade_LX200_ACF_8"])

    @classmethod
    def Meade_LX200_ACF_10(cls):
        return cls.from_database(cls._DATABASE["Meade_LX200_ACF_10"])

    @classmethod
    def Meade_LX200_ACF_12(cls):
        return cls.from_database(cls._DATABASE["Meade_LX200_ACF_12"])

    @classmethod
    def Meade_LX200_ACF_14(cls):
        return cls.from_database(cls._DATABASE["Meade_LX200_ACF_14"])

    @classmethod
    def Meade_LX200_ACF_16(cls):
        return cls.from_database(cls._DATABASE["Meade_LX200_ACF_16"])

    @classmethod
    def Meade_LX600_ACF_10(cls):
        return cls.from_database(cls._DATABASE["Meade_LX600_ACF_10"])

    @classmethod
    def Meade_LX600_ACF_12(cls):
        return cls.from_database(cls._DATABASE["Meade_LX600_ACF_12"])

    @classmethod
    def Meade_LX600_ACF_14(cls):
        return cls.from_database(cls._DATABASE["Meade_LX600_ACF_14"])
