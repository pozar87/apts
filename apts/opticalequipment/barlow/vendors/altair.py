from ..base import Barlow

class AltairBarlow(Barlow):
    _DATABASE = {
        "Altair_ED_Barlow_2x_1_25": {
            "brand": "Altair",
            "name": 'ED Barlow 2x (1.25")',
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
        "Altair_ED_Barlow_2x_2": {
            "brand": "Altair",
            "name": 'ED Barlow 2x (2")',
            "type": "type_barlow",
            "optical_length": 0,
            "mass": 240,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": '2"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
        "Altair_Barlow_3x_1_25": {
            "brand": "Altair",
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
    }

    @classmethod
    def Altair_ED_Barlow_2x_1_25(cls):
        return cls.from_database(cls._DATABASE["Altair_ED_Barlow_2x_1_25"])

    @classmethod
    def Altair_ED_Barlow_2x_2(cls):
        return cls.from_database(cls._DATABASE["Altair_ED_Barlow_2x_2"])

    @classmethod
    def Altair_Barlow_3x_1_25(cls):
        return cls.from_database(cls._DATABASE["Altair_Barlow_3x_1_25"])
