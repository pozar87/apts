from ..base import Focuser


class LacertaFocuser(Focuser):
    _DATABASE = {
        "Lacerta_MFOC_Focuser": {
            "brand": "Lacerta",
            "name": "MFOC Focuser",
            "type": "type_focuser",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": "",
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_2_Micro_Focuser": {
            "brand": "Lacerta",
            "name": "2\" Micro Focuser",
            "type": "type_focuser",
            "optical_length": 0,
            "mass": 500,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Lacerta_2_5_Micro_Focuser": {
            "brand": "Lacerta",
            "name": "2.5\" Micro Focuser",
            "type": "type_focuser",
            "optical_length": 0,
            "mass": 700,
            "tside_thread": "M68",
            "tside_gender": "Female",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Lacerta_MFOC_Focuser(cls):
        return cls.from_database(cls._DATABASE['Lacerta_MFOC_Focuser'])

    @classmethod
    def Lacerta_2_Micro_Focuser(cls):
        return cls.from_database(cls._DATABASE['Lacerta_2_Micro_Focuser'])

    @classmethod
    def Lacerta_2_5_Micro_Focuser(cls):
        return cls.from_database(cls._DATABASE['Lacerta_2_5_Micro_Focuser'])
