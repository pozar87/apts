from ..base import Barlow

class DatysonBarlow(Barlow):
    _DATABASE = {
        "Datyson_Barlow_2x_1_25": {
            "brand": "Datyson",
            "name": 'Barlow 2x (1.25")',
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
        "Datyson_Barlow_3x_1_25": {
            "brand": "Datyson",
            "name": 'Barlow 3x (1.25")',
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
        "Datyson_Barlow_5x_1_25": {
            "brand": "Datyson",
            "name": 'Barlow 5x (1.25")',
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
    }

    @classmethod
    def Datyson_Barlow_2x_1_25(cls):
        return cls.from_database(cls._DATABASE["Datyson_Barlow_2x_1_25"])

    @classmethod
    def Datyson_Barlow_3x_1_25(cls):
        return cls.from_database(cls._DATABASE["Datyson_Barlow_3x_1_25"])

    @classmethod
    def Datyson_Barlow_5x_1_25(cls):
        return cls.from_database(cls._DATABASE["Datyson_Barlow_5x_1_25"])
