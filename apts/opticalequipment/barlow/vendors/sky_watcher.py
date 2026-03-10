from ..base import Barlow

class SkyWatcherBarlow(Barlow):
    _DATABASE = {
        "Sky_Watcher_2x_Deluxe_Barlow_1_25": {
            "brand": "Sky-Watcher",
            "name": '2x Deluxe Barlow (1.25")',
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
        "Sky_Watcher_2x_Deluxe_Barlow_2": {
            "brand": "Sky-Watcher",
            "name": '2x Deluxe Barlow (2")',
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
        "Sky_Watcher_2x_ED_Extender": {
            "brand": "Sky-Watcher",
            "name": "2x ED Extender",
            "type": "type_extender",
            "optical_length": 0,
            "mass": 160,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
    }

    @classmethod
    def Sky_Watcher_2x_Deluxe_Barlow_1_25(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_2x_Deluxe_Barlow_1_25"])

    @classmethod
    def Sky_Watcher_2x_Deluxe_Barlow_2(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_2x_Deluxe_Barlow_2"])

    @classmethod
    def Sky_Watcher_2x_ED_Extender(cls):
        return cls.from_database(cls._DATABASE["Sky_Watcher_2x_ED_Extender"])
