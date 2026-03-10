from ..base import Barlow

class OmegonBarlow(Barlow):
    _DATABASE = {
        "Omegon_2x_ED_Barlow_1_25": {
            "brand": "Omegon",
            "name": '2x ED Barlow (1.25")',
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
        "Omegon_3x_Barlow_1_25": {
            "brand": "Omegon",
            "name": '3x Barlow (1.25")',
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
        "Omegon_Barlow_2x_1_25": {
            "brand": "Omegon",
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
        "Omegon_Barlow_3x_1_25": {
            "brand": "Omegon",
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
        "Omegon_Barlow_5x_1_25": {
            "brand": "Omegon",
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
        "Omegon_Barlow_2x_2": {
            "brand": "Omegon",
            "name": 'Barlow 2x (2")',
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
    }

    @classmethod
    def Omegon_2x_ED_Barlow_1_25(cls):
        return cls.from_database(cls._DATABASE["Omegon_2x_ED_Barlow_1_25"])

    @classmethod
    def Omegon_3x_Barlow_1_25(cls):
        return cls.from_database(cls._DATABASE["Omegon_3x_Barlow_1_25"])

    @classmethod
    def Omegon_Barlow_2x_1_25(cls):
        return cls.from_database(cls._DATABASE["Omegon_Barlow_2x_1_25"])

    @classmethod
    def Omegon_Barlow_3x_1_25(cls):
        return cls.from_database(cls._DATABASE["Omegon_Barlow_3x_1_25"])

    @classmethod
    def Omegon_Barlow_5x_1_25(cls):
        return cls.from_database(cls._DATABASE["Omegon_Barlow_5x_1_25"])

    @classmethod
    def Omegon_Barlow_2x_2(cls):
        return cls.from_database(cls._DATABASE["Omegon_Barlow_2x_2"])
