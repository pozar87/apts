from ..base import AntiTilt


class ZWOAntiTilt(AntiTilt):
    _DATABASE = {
        "ZWO_M54_Tilt_Adjuster": {
            "brand": "ZWO",
            "name": "M54 Tilt Adjuster",
            "type": "type_anti_tilt",
            "optical_length": 11,
            "mass": 50,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "ZWO_Anti_tilt_Plate_6_bolt_5mm": {
            "brand": "ZWO",
            "name": "Anti-tilt Plate (6-bolt, 5mm)",
            "type": "type_anti_tilt",
            "optical_length": 5,
            "mass": 30,
            "tside_thread": "ZWO 6-bolt",
            "tside_gender": "Female",
            "cside_thread": "ZWO 6-bolt",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def ZWO_M54_Tilt_Adjuster(cls):
        return cls.from_database(cls._DATABASE['ZWO_M54_Tilt_Adjuster'])

    @classmethod
    def ZWO_Anti_tilt_Plate_6_bolt_5mm(cls):
        return cls.from_database(cls._DATABASE[
            'ZWO_Anti_tilt_Plate_6_bolt_5mm'])
