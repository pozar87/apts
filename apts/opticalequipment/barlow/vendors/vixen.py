from ..base import Barlow

class VixenBarlow(Barlow):
    _DATABASE = {
        "Vixen_2x_Barlow_1_25": {
            "brand": "Vixen",
            "name": '2x Barlow (1.25")',
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
        "Vixen_2x_Barlow_2": {
            "brand": "Vixen",
            "name": '2x Barlow (2")',
            "type": "type_barlow",
            "optical_length": 0,
            "mass": 220,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": '2"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
        "Vixen_Barlow_2x_1_25": {
            "brand": "Vixen",
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
        "Vixen_Barlow_2_5x_1_25": {
            "brand": "Vixen",
            "name": 'Barlow 2.5x (1.25")',
            "type": "type_barlow",
            "optical_length": 0,
            "mass": 130,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
    }

    @classmethod
    def Vixen_2x_Barlow_1_25(cls):
        return cls.from_database(cls._DATABASE["Vixen_2x_Barlow_1_25"])

    @classmethod
    def Vixen_2x_Barlow_2(cls):
        return cls.from_database(cls._DATABASE["Vixen_2x_Barlow_2"])

    @classmethod
    def Vixen_Barlow_2x_1_25(cls):
        return cls.from_database(cls._DATABASE["Vixen_Barlow_2x_1_25"])

    @classmethod
    def Vixen_Barlow_2_5x_1_25(cls):
        return cls.from_database(cls._DATABASE["Vixen_Barlow_2_5x_1_25"])
