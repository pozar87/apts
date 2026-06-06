from ..base import Focuser


class StarlightInstrumentsFocuser(Focuser):
    _DATABASE = {
        "Starlight_Instruments_Feather_Touch_2": {
            "brand": "Starlight Instruments",
            "name": "Feather Touch 2\"",
            "type": "type_focuser",
            "optical_length": 0,
            "mass": 700,
            "tside_thread": "",
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Starlight_Instruments_Feather_Touch_2_5": {
            "brand": "Starlight Instruments",
            "name": "Feather Touch 2.5\"",
            "type": "type_focuser",
            "optical_length": 0,
            "mass": 900,
            "tside_thread": "",
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Starlight_Instruments_Feather_Touch_3": {
            "brand": "Starlight Instruments",
            "name": "Feather Touch 3\"",
            "type": "type_focuser",
            "optical_length": 0,
            "mass": 1200,
            "tside_thread": "",
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Starlight_Instruments_Feather_Touch_3_5": {
            "brand": "Starlight Instruments",
            "name": "Feather Touch 3.5\"",
            "type": "type_focuser",
            "optical_length": 0,
            "mass": 1500,
            "tside_thread": "",
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Starlight_Instruments_Feather_Touch_4": {
            "brand": "Starlight Instruments",
            "name": "Feather Touch 4\"",
            "type": "type_focuser",
            "optical_length": 0,
            "mass": 1800,
            "tside_thread": "",
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Starlight_Instruments_Feather_Touch_2(cls):
        return cls.from_database(cls._DATABASE[
            'Starlight_Instruments_Feather_Touch_2'])

    @classmethod
    def Starlight_Instruments_Feather_Touch_2_5(cls):
        return cls.from_database(cls._DATABASE[
            'Starlight_Instruments_Feather_Touch_2_5'])

    @classmethod
    def Starlight_Instruments_Feather_Touch_3(cls):
        return cls.from_database(cls._DATABASE[
            'Starlight_Instruments_Feather_Touch_3'])

    @classmethod
    def Starlight_Instruments_Feather_Touch_3_5(cls):
        return cls.from_database(cls._DATABASE[
            'Starlight_Instruments_Feather_Touch_3_5'])

    @classmethod
    def Starlight_Instruments_Feather_Touch_4(cls):
        return cls.from_database(cls._DATABASE[
            'Starlight_Instruments_Feather_Touch_4'])
