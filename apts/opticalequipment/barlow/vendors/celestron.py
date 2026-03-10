from ..base import Barlow

class CelestronBarlow(Barlow):
    _DATABASE = {
        "Celestron_Ultima_Barlow_2x_1_25": {
            "brand": "Celestron",
            "name": 'Ultima Barlow 2x (1.25")',
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
        "Celestron_Ultima_Barlow_3x_1_25": {
            "brand": "Celestron",
            "name": 'Ultima Barlow 3x (1.25")',
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
        "Celestron_Ultima_Barlow_5x_1_25": {
            "brand": "Celestron",
            "name": 'Ultima Barlow 5x (1.25")',
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
        "Celestron_Ultima_Barlow_2x_2": {
            "brand": "Celestron",
            "name": 'Ultima Barlow 2x (2")',
            "type": "type_barlow",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": '2"',
            "tside_gender": "Male",
            "cside_thread": '2"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
        "Celestron_X_Cel_LX_2x_Barlow": {
            "brand": "Celestron",
            "name": "X-Cel LX 2x Barlow",
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
        "Celestron_X_Cel_LX_3x_Barlow": {
            "brand": "Celestron",
            "name": "X-Cel LX 3x Barlow",
            "type": "type_barlow",
            "optical_length": 0,
            "mass": 150,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
        "Celestron_2x_Extender": {
            "brand": "Celestron",
            "name": "2x Extender",
            "type": "type_extender",
            "optical_length": 0,
            "mass": 150,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
    }

    @classmethod
    def Celestron_Ultima_Barlow_2x_1_25(cls):
        return cls.from_database(cls._DATABASE["Celestron_Ultima_Barlow_2x_1_25"])

    @classmethod
    def Celestron_Ultima_Barlow_3x_1_25(cls):
        return cls.from_database(cls._DATABASE["Celestron_Ultima_Barlow_3x_1_25"])

    @classmethod
    def Celestron_Ultima_Barlow_5x_1_25(cls):
        return cls.from_database(cls._DATABASE["Celestron_Ultima_Barlow_5x_1_25"])

    @classmethod
    def Celestron_Ultima_Barlow_2x_2(cls):
        return cls.from_database(cls._DATABASE["Celestron_Ultima_Barlow_2x_2"])

    @classmethod
    def Celestron_X_Cel_LX_2x_Barlow(cls):
        return cls.from_database(cls._DATABASE["Celestron_X_Cel_LX_2x_Barlow"])

    @classmethod
    def Celestron_X_Cel_LX_3x_Barlow(cls):
        return cls.from_database(cls._DATABASE["Celestron_X_Cel_LX_3x_Barlow"])

    @classmethod
    def Celestron_2x_Extender(cls):
        return cls.from_database(cls._DATABASE["Celestron_2x_Extender"])
