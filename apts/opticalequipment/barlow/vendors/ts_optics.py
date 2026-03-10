from ..base import Barlow

class TSOpticsBarlow(Barlow):
    _DATABASE = {
        "TS_Optics_2_5x_ED_Barlow_1_25": {
            "brand": "TS-Optics",
            "name": '2.5x ED Barlow (1.25")',
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
        "TS_Optics_2x_Barlow_2": {
            "brand": "TS-Optics",
            "name": '2x Barlow (2")',
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
        "TS_Optics_Barlow_2x_1_25": {
            "brand": "TS-Optics",
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
        "TS_Optics_Barlow_2_5x_1_25": {
            "brand": "TS-Optics",
            "name": 'Barlow 2.5x (1.25")',
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
        "TS_Optics_Barlow_3x_1_25": {
            "brand": "TS-Optics",
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
        "TS_Optics_Barlow_5x_1_25": {
            "brand": "TS-Optics",
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
        "TS_Optics_Barlow_2x_2": {
            "brand": "TS-Optics",
            "name": 'Barlow 2x (2")',
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
    def TS_Optics_2_5x_ED_Barlow_1_25(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_2_5x_ED_Barlow_1_25"])

    @classmethod
    def TS_Optics_2x_Barlow_2(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_2x_Barlow_2"])

    @classmethod
    def TS_Optics_Barlow_2x_1_25(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Barlow_2x_1_25"])

    @classmethod
    def TS_Optics_Barlow_2_5x_1_25(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Barlow_2_5x_1_25"])

    @classmethod
    def TS_Optics_Barlow_3x_1_25(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Barlow_3x_1_25"])

    @classmethod
    def TS_Optics_Barlow_5x_1_25(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Barlow_5x_1_25"])

    @classmethod
    def TS_Optics_Barlow_2x_2(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_Barlow_2x_2"])
