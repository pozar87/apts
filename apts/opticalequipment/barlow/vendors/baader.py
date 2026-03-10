from ..base import Barlow

class BaaderBarlow(Barlow):
    _DATABASE = {
        "Baader_VIP_Barlow_2_25x": {
            "brand": "Baader",
            "name": "VIP Barlow 2.25x",
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
        "Baader_1_3x_GPC_M48": {
            "brand": "Baader",
            "name": "1.3x GPC (M48)",
            "type": "type_barlow",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": "M48",
            "tside_gender": "Male",
            "cside_thread": "M48",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
        "Baader_Q_Barlow_2_25x_1_25": {
            "brand": "Baader",
            "name": 'Q-Barlow 2.25x (1.25")',
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
        "Baader_Mark_III_2x_Shorty_Barlow": {
            "brand": "Baader",
            "name": "Mark III 2x Shorty Barlow",
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
        "Baader_2x_Barlow_M48": {
            "brand": "Baader",
            "name": "2x Barlow (M48)",
            "type": "type_barlow",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": "M48",
            "tside_gender": "Male",
            "cside_thread": "M48",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
    }

    @classmethod
    def Baader_VIP_Barlow_2_25x(cls):
        return cls.from_database(cls._DATABASE["Baader_VIP_Barlow_2_25x"])

    @classmethod
    def Baader_1_3x_GPC_M48(cls):
        return cls.from_database(cls._DATABASE["Baader_1_3x_GPC_M48"])

    @classmethod
    def Baader_Q_Barlow_2_25x_1_25(cls):
        return cls.from_database(cls._DATABASE["Baader_Q_Barlow_2_25x_1_25"])

    @classmethod
    def Baader_Mark_III_2x_Shorty_Barlow(cls):
        return cls.from_database(cls._DATABASE["Baader_Mark_III_2x_Shorty_Barlow"])

    @classmethod
    def Baader_2x_Barlow_M48(cls):
        return cls.from_database(cls._DATABASE["Baader_2x_Barlow_M48"])
