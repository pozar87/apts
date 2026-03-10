from ..base import Barlow

class LacertaBarlow(Barlow):
    _DATABASE = {
        "Lacerta_2x_ED_Barlow_1_25": {
            "brand": "Lacerta",
            "name": '2x ED Barlow (1.25")',
            "type": "type_barlow",
            "optical_length": 0,
            "mass": 110,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
        "Lacerta_Barlow_2x_1_25": {
            "brand": "Lacerta",
            "name": 'Barlow 2x (1.25")',
            "type": "type_barlow",
            "optical_length": 0,
            "mass": 110,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
        "Lacerta_Barlow_2_5x_1_25": {
            "brand": "Lacerta",
            "name": 'Barlow 2.5x (1.25")',
            "type": "type_barlow",
            "optical_length": 0,
            "mass": 110,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
        "Lacerta_Barlow_3x_1_25": {
            "brand": "Lacerta",
            "name": 'Barlow 3x (1.25")',
            "type": "type_barlow",
            "optical_length": 0,
            "mass": 110,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
        "Lacerta_Barlow_5x_1_25": {
            "brand": "Lacerta",
            "name": 'Barlow 5x (1.25")',
            "type": "type_barlow",
            "optical_length": 0,
            "mass": 110,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
        "Lacerta_Barlow_2x_2": {
            "brand": "Lacerta",
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
    def Lacerta_2x_ED_Barlow_1_25(cls):
        return cls.from_database(cls._DATABASE["Lacerta_2x_ED_Barlow_1_25"])

    @classmethod
    def Lacerta_Barlow_2x_1_25(cls):
        return cls.from_database(cls._DATABASE["Lacerta_Barlow_2x_1_25"])

    @classmethod
    def Lacerta_Barlow_2_5x_1_25(cls):
        return cls.from_database(cls._DATABASE["Lacerta_Barlow_2_5x_1_25"])

    @classmethod
    def Lacerta_Barlow_3x_1_25(cls):
        return cls.from_database(cls._DATABASE["Lacerta_Barlow_3x_1_25"])

    @classmethod
    def Lacerta_Barlow_5x_1_25(cls):
        return cls.from_database(cls._DATABASE["Lacerta_Barlow_5x_1_25"])

    @classmethod
    def Lacerta_Barlow_2x_2(cls):
        return cls.from_database(cls._DATABASE["Lacerta_Barlow_2x_2"])
