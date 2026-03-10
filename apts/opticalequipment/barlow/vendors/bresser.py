from ..base import Barlow

class BresserBarlow(Barlow):
    _DATABASE = {
        "Bresser_2x_Barlow_1_25": {
            "brand": "Bresser",
            "name": '2x Barlow (1.25")',
            "type": "type_barlow",
            "optical_length": 0,
            "mass": 90,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
        "Bresser_3x_Barlow_1_25": {
            "brand": "Bresser",
            "name": '3x Barlow (1.25")',
            "type": "type_barlow",
            "optical_length": 0,
            "mass": 95,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
    }

    @classmethod
    def Bresser_2x_Barlow_1_25(cls):
        return cls.from_database(cls._DATABASE["Bresser_2x_Barlow_1_25"])

    @classmethod
    def Bresser_3x_Barlow_1_25(cls):
        return cls.from_database(cls._DATABASE["Bresser_3x_Barlow_1_25"])
