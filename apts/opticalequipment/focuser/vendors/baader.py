from ..base import Focuser


class BaaderFocuser(Focuser):
    _DATABASE = {
        "Baader_Steeldrive_II": {
            "brand": "Baader",
            "name": "Steeldrive II",
            "type": "type_focuser",
            "optical_length": 0,
            "mass": 350,
            "tside_thread": "",
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Baader_Diamond_Steeltrack": {
            "brand": "Baader",
            "name": "Diamond Steeltrack",
            "type": "type_focuser",
            "optical_length": 0,
            "mass": 600,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Baader_Steeldrive_II(cls):
        return cls.from_database(cls._DATABASE['Baader_Steeldrive_II'])

    @classmethod
    def Baader_Diamond_Steeltrack(cls):
        return cls.from_database(cls._DATABASE['Baader_Diamond_Steeltrack'])
