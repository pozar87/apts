from ..base import Barlow

class MeadeBarlow(Barlow):
    _DATABASE = {
        "Meade_126_2x_Barlow": {
            "brand": "Meade",
            "name": "#126 2x Barlow",
            "type": "type_barlow",
            "optical_length": 0,
            "mass": 120,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
        "Meade_140_2x_Barlow_2": {
            "brand": "Meade",
            "name": '#140 2x Barlow (2")',
            "type": "type_barlow",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": '2"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
    }

    @classmethod
    def Meade_126_2x_Barlow(cls):
        return cls.from_database(cls._DATABASE["Meade_126_2x_Barlow"])

    @classmethod
    def Meade_140_2x_Barlow_2(cls):
        return cls.from_database(cls._DATABASE["Meade_140_2x_Barlow_2"])
