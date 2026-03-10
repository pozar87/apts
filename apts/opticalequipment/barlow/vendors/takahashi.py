from ..base import Barlow

class TakahashiBarlow(Barlow):
    _DATABASE = {
        "Takahashi_Extender_Q_1_6x": {
            "brand": "Takahashi",
            "name": "Extender-Q 1.6x",
            "type": "type_extender",
            "optical_length": 0,
            "mass": 300,
            "tside_thread": "M82",
            "tside_gender": "Male",
            "cside_thread": "M54",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
        "Takahashi_Extender_CQ_1_7x": {
            "brand": "Takahashi",
            "name": "Extender-CQ 1.7x",
            "type": "type_extender",
            "optical_length": 0,
            "mass": 350,
            "tside_thread": "M82",
            "tside_gender": "Male",
            "cside_thread": "M54",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
        "Takahashi_2x_Extender_Q_1_25": {
            "brand": "Takahashi",
            "name": '2x Extender-Q (1.25")',
            "type": "type_barlow",
            "optical_length": 0,
            "mass": 180,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
        "Takahashi_Extender_C_2_27x": {
            "brand": "Takahashi",
            "name": "Extender C 2.27x",
            "type": "type_extender",
            "optical_length": 0,
            "mass": 400,
            "tside_thread": "M82",
            "tside_gender": "Male",
            "cside_thread": "M54",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
        "Takahashi_Extender_EX_1_5x": {
            "brand": "Takahashi",
            "name": "Extender EX 1.5x",
            "type": "type_extender",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": "M54",
            "tside_gender": "Male",
            "cside_thread": "M54",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
        "Takahashi_Barlow_2x_1_25": {
            "brand": "Takahashi",
            "name": 'Barlow 2x (1.25")',
            "type": "type_barlow",
            "optical_length": 0,
            "mass": 140,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
        "Takahashi_Barlow_1_6x_M42": {
            "brand": "Takahashi",
            "name": "Barlow 1.6x (M42)",
            "type": "type_barlow",
            "optical_length": 0,
            "mass": 150,
            "tside_thread": "M42",
            "tside_gender": "Male",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
    }

    @classmethod
    def Takahashi_Extender_Q_1_6x(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Extender_Q_1_6x"])

    @classmethod
    def Takahashi_Extender_CQ_1_7x(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Extender_CQ_1_7x"])

    @classmethod
    def Takahashi_2x_Extender_Q_1_25(cls):
        return cls.from_database(cls._DATABASE["Takahashi_2x_Extender_Q_1_25"])

    @classmethod
    def Takahashi_Extender_C_2_27x(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Extender_C_2_27x"])

    @classmethod
    def Takahashi_Extender_EX_1_5x(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Extender_EX_1_5x"])

    @classmethod
    def Takahashi_Barlow_2x_1_25(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Barlow_2x_1_25"])

    @classmethod
    def Takahashi_Barlow_1_6x_M42(cls):
        return cls.from_database(cls._DATABASE["Takahashi_Barlow_1_6x_M42"])
