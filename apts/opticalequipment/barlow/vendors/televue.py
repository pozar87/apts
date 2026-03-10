from ..base import Barlow

class TeleVueBarlow(Barlow):
    _DATABASE = {
        "TeleVue_Powermate_2x_1_25": {
            "brand": "TeleVue",
            "name": 'Powermate 2x (1.25")',
            "type": "type_barlow",
            "optical_length": 0,
            "mass": 170,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
        "TeleVue_Powermate_2_5x_1_25": {
            "brand": "TeleVue",
            "name": 'Powermate 2.5x (1.25")',
            "type": "type_barlow",
            "optical_length": 0,
            "mass": 170,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
        "TeleVue_Powermate_4x_1_25": {
            "brand": "TeleVue",
            "name": 'Powermate 4x (1.25")',
            "type": "type_barlow",
            "optical_length": 0,
            "mass": 170,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
        "TeleVue_Powermate_5x_1_25": {
            "brand": "TeleVue",
            "name": 'Powermate 5x (1.25")',
            "type": "type_barlow",
            "optical_length": 0,
            "mass": 170,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
        "TeleVue_Big_Barlow_2x_2": {
            "brand": "TeleVue",
            "name": 'Big Barlow 2x (2")',
            "type": "type_barlow",
            "optical_length": 0,
            "mass": 310,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": '2"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
        "TeleVue_Powermate_2x_2": {
            "brand": "TeleVue",
            "name": 'Powermate 2x (2")',
            "type": "type_barlow",
            "optical_length": 0,
            "mass": 310,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": '2"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
        "TeleVue_Powermate_4x_2": {
            "brand": "TeleVue",
            "name": 'Powermate 4x (2")',
            "type": "type_barlow",
            "optical_length": 0,
            "mass": 310,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": '2"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
        "TeleVue_2x_Extender_1_25": {
            "brand": "TeleVue",
            "name": '2x Extender (1.25")',
            "type": "type_extender",
            "optical_length": 0,
            "mass": 170,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
        "TeleVue_2x_Extender_2": {
            "brand": "TeleVue",
            "name": '2x Extender (2")',
            "type": "type_extender",
            "optical_length": 0,
            "mass": 310,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": '2"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
    }

    @classmethod
    def TeleVue_Powermate_2x_1_25(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Powermate_2x_1_25"])

    @classmethod
    def TeleVue_Powermate_2_5x_1_25(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Powermate_2_5x_1_25"])

    @classmethod
    def TeleVue_Powermate_4x_1_25(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Powermate_4x_1_25"])

    @classmethod
    def TeleVue_Powermate_5x_1_25(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Powermate_5x_1_25"])

    @classmethod
    def TeleVue_Big_Barlow_2x_2(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Big_Barlow_2x_2"])

    @classmethod
    def TeleVue_Powermate_2x_2(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Powermate_2x_2"])

    @classmethod
    def TeleVue_Powermate_4x_2(cls):
        return cls.from_database(cls._DATABASE["TeleVue_Powermate_4x_2"])

    @classmethod
    def TeleVue_2x_Extender_1_25(cls):
        return cls.from_database(cls._DATABASE["TeleVue_2x_Extender_1_25"])

    @classmethod
    def TeleVue_2x_Extender_2(cls):
        return cls.from_database(cls._DATABASE["TeleVue_2x_Extender_2"])
