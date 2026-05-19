from ..base import Filter


class OptolongFilter(Filter):
    _DATABASE = {
        "Optolong_L_Pro_2": {
            "brand": "Optolong",
            "name": 'L-Pro (2")',
            "type": "type_filter",
            "optical_length": 0,
            "mass": 50,
            "tside_thread": '2"',
            "transmission": 0.9,
        },
        "Optolong_L_Pro_1_25": {
            "brand": "Optolong",
            "name": 'L-Pro (1.25")',
            "type": "type_filter",
            "optical_length": 0,
            "mass": 30,
            "tside_thread": '1.25"',
            "transmission": 0.9,
        },
    }

    @classmethod
    def Optolong_L_Pro_2(cls):
        return cls.from_database(cls._DATABASE["Optolong_L_Pro_2"])

    @classmethod
    def Optolong_L_Pro_1_25(cls):
        return cls.from_database(cls._DATABASE["Optolong_L_Pro_1_25"])
