from ..base import Barlow

class APMBarlow(Barlow):
    _DATABASE = {
        "APM_Comacorr_2x_Barlow_M48": {
            "brand": "APM",
            "name": "Comacorr 2x Barlow (M48)",
            "type": "type_barlow",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": "M48",
            "tside_gender": "Male",
            "cside_thread": "M48",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
        "APM_2x_ED_Barlow_1_25": {
            "brand": "APM",
            "name": '2x ED Barlow (1.25")',
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
        "APM_ED_Barlow_1_5x_1_25": {
            "brand": "APM",
            "name": 'ED Barlow 1.5x (1.25")',
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
        "APM_ED_Barlow_2x_1_25": {
            "brand": "APM",
            "name": 'ED Barlow 2x (1.25")',
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
        "APM_ED_Barlow_2_5x_1_25": {
            "brand": "APM",
            "name": 'ED Barlow 2.5x (1.25")',
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
        "APM_ED_Barlow_3x_1_25": {
            "brand": "APM",
            "name": 'ED Barlow 3x (1.25")',
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
        "APM_ED_Barlow_2x_2": {
            "brand": "APM",
            "name": 'ED Barlow 2x (2")',
            "type": "type_barlow",
            "optical_length": 0,
            "mass": 260,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": '2"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
    }

    @classmethod
    def APM_Comacorr_2x_Barlow_M48(cls):
        return cls.from_database(cls._DATABASE["APM_Comacorr_2x_Barlow_M48"])

    @classmethod
    def APM_2x_ED_Barlow_1_25(cls):
        return cls.from_database(cls._DATABASE["APM_2x_ED_Barlow_1_25"])

    @classmethod
    def APM_ED_Barlow_1_5x_1_25(cls):
        return cls.from_database(cls._DATABASE["APM_ED_Barlow_1_5x_1_25"])

    @classmethod
    def APM_ED_Barlow_2x_1_25(cls):
        return cls.from_database(cls._DATABASE["APM_ED_Barlow_2x_1_25"])

    @classmethod
    def APM_ED_Barlow_2_5x_1_25(cls):
        return cls.from_database(cls._DATABASE["APM_ED_Barlow_2_5x_1_25"])

    @classmethod
    def APM_ED_Barlow_3x_1_25(cls):
        return cls.from_database(cls._DATABASE["APM_ED_Barlow_3x_1_25"])

    @classmethod
    def APM_ED_Barlow_2x_2(cls):
        return cls.from_database(cls._DATABASE["APM_ED_Barlow_2x_2"])
