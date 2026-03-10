from ..base import Barlow

class StellarvueBarlow(Barlow):
    _DATABASE = {
        "Stellarvue_Barlow_2x_1_25": {
            "brand": "Stellarvue",
            "name": 'Barlow 2x (1.25")',
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
        "Stellarvue_Barlow_2x_2": {
            "brand": "Stellarvue",
            "name": 'Barlow 2x (2")',
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
    def Stellarvue_Barlow_2x_1_25(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_Barlow_2x_1_25"])

    @classmethod
    def Stellarvue_Barlow_2x_2(cls):
        return cls.from_database(cls._DATABASE["Stellarvue_Barlow_2x_2"])
