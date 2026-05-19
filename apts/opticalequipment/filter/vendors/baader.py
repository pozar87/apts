from ..base import Filter


class BaaderFilter(Filter):
    _DATABASE = {
        "Baader_UHC_S_2": {
            "brand": "Baader",
            "name": 'UHC-S (2")',
            "type": "type_filter",
            "optical_length": 0,
            "mass": 60,
            "tside_thread": '2"',
            "transmission": 0.95,
        },
        "Baader_UHC_S_1_25": {
            "brand": "Baader",
            "name": 'UHC-S (1.25")',
            "type": "type_filter",
            "optical_length": 0,
            "mass": 40,
            "tside_thread": '1.25"',
            "transmission": 0.95,
        },
    }

    @classmethod
    def Baader_UHC_S_2(cls):
        return cls.from_database(cls._DATABASE["Baader_UHC_S_2"])

    @classmethod
    def Baader_UHC_S_1_25(cls):
        return cls.from_database(cls._DATABASE["Baader_UHC_S_1_25"])
