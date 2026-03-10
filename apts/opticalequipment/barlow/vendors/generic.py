from ..base import Barlow

class GenericBarlow(Barlow):
    _DATABASE = {
        "Generic_Barlow_2x_1_25": {
            "brand": "Generic",
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
        "Generic_Barlow_3x_1_25": {
            "brand": "Generic",
            "name": 'Barlow 3x (1.25")',
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
        "Generic_Barlow_5x_1_25": {
            "brand": "Generic",
            "name": 'Barlow 5x (1.25")',
            "type": "type_barlow",
            "optical_length": 0,
            "mass": 150,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
        "Generic_Barlow_2x_2": {
            "brand": "Generic",
            "name": 'Barlow 2x (2")',
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
    def Generic_Barlow_2x_1_25(cls):
        return cls.from_database(cls._DATABASE["Generic_Barlow_2x_1_25"])

    @classmethod
    def Generic_Barlow_3x_1_25(cls):
        return cls.from_database(cls._DATABASE["Generic_Barlow_3x_1_25"])

    @classmethod
    def Generic_Barlow_5x_1_25(cls):
        return cls.from_database(cls._DATABASE["Generic_Barlow_5x_1_25"])

    @classmethod
    def Generic_Barlow_2x_2(cls):
        return cls.from_database(cls._DATABASE["Generic_Barlow_2x_2"])
