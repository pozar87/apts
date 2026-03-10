from ..base import Barlow

class GSOBarlow(Barlow):
    _DATABASE = {
        "GSO_2x_Barlow_1_25": {
            "brand": "GSO",
            "name": '2x Barlow (1.25")',
            "type": "type_barlow",
            "optical_length": 0,
            "mass": 80,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
        "GSO_2x_Barlow_2": {
            "brand": "GSO",
            "name": '2x Barlow (2")',
            "type": "type_barlow",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": '2"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
    }

    @classmethod
    def GSO_2x_Barlow_1_25(cls):
        return cls.from_database(cls._DATABASE["GSO_2x_Barlow_1_25"])

    @classmethod
    def GSO_2x_Barlow_2(cls):
        return cls.from_database(cls._DATABASE["GSO_2x_Barlow_2"])
