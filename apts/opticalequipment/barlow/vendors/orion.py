from ..base import Barlow

class OrionBarlow(Barlow):
    _DATABASE = {
        "Orion_Shorty_2x_Barlow": {
            "brand": "Orion",
            "name": "Shorty 2x Barlow",
            "type": "type_barlow",
            "optical_length": 0,
            "mass": 100,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
        "Orion_2x_Shorty_Plus_Barlow_2": {
            "brand": "Orion",
            "name": '2x Shorty Plus Barlow (2")',
            "type": "type_barlow",
            "optical_length": 0,
            "mass": 230,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": '2"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
    }

    @classmethod
    def Orion_Shorty_2x_Barlow(cls):
        return cls.from_database(cls._DATABASE["Orion_Shorty_2x_Barlow"])

    @classmethod
    def Orion_2x_Shorty_Plus_Barlow_2(cls):
        return cls.from_database(cls._DATABASE["Orion_2x_Shorty_Plus_Barlow_2"])
