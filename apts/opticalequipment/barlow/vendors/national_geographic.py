from ..base import Barlow

class NationalGeographicBarlow(Barlow):
    _DATABASE = {
        "National_Geographic_2x_Barlow_1_25": {
            "brand": "National Geographic",
            "name": '2x Barlow (1.25")',
            "type": "type_barlow",
            "optical_length": 0,
            "mass": 70,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
    }

    @classmethod
    def National_Geographic_2x_Barlow_1_25(cls):
        return cls.from_database(cls._DATABASE["National_Geographic_2x_Barlow_1_25"])
