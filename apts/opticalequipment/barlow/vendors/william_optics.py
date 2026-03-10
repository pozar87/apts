from ..base import Barlow

class WilliamOpticsBarlow(Barlow):
    _DATABASE = {
        "William_Optics_Barlow_2x_1_25": {
            "brand": "William Optics",
            "name": 'Barlow 2x (1.25")',
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
    }

    @classmethod
    def William_Optics_Barlow_2x_1_25(cls):
        return cls.from_database(cls._DATABASE["William_Optics_Barlow_2x_1_25"])
