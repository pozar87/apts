from ..base import Barlow

class SaxonBarlow(Barlow):
    _DATABASE = {
        "Saxon_2x_Barlow_1_25": {
            "brand": "Saxon",
            "name": '2x Barlow (1.25")',
            "type": "type_barlow",
            "optical_length": 0,
            "mass": 80,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
    }

    @classmethod
    def Saxon_2x_Barlow_1_25(cls):
        return cls.from_database(cls._DATABASE["Saxon_2x_Barlow_1_25"])
