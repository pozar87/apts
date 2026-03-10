from ..base import Barlow

class AntaresBarlow(Barlow):
    _DATABASE = {
        "Antares_Barlow_1_5x_1_25": {
            "brand": "Antares",
            "name": 'Barlow 1.5x (1.25")',
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
        "Antares_Barlow_2x_1_25": {
            "brand": "Antares",
            "name": 'Barlow 2x (1.25")',
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
        "Antares_Barlow_3x_1_25": {
            "brand": "Antares",
            "name": 'Barlow 3x (1.25")',
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
        "Antares_Barlow_5x_1_25": {
            "brand": "Antares",
            "name": 'Barlow 5x (1.25")',
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
    }

    @classmethod
    def Antares_Barlow_1_5x_1_25(cls):
        return cls.from_database(cls._DATABASE["Antares_Barlow_1_5x_1_25"])

    @classmethod
    def Antares_Barlow_2x_1_25(cls):
        return cls.from_database(cls._DATABASE["Antares_Barlow_2x_1_25"])

    @classmethod
    def Antares_Barlow_3x_1_25(cls):
        return cls.from_database(cls._DATABASE["Antares_Barlow_3x_1_25"])

    @classmethod
    def Antares_Barlow_5x_1_25(cls):
        return cls.from_database(cls._DATABASE["Antares_Barlow_5x_1_25"])
