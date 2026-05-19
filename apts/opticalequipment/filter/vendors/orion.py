from ..base import Filter


class OrionFilter(Filter):
    _DATABASE = {
        "Orion_SkyGlow_Broadband_Filter": {
            "brand": "Orion",
            "name": "SkyGlow Broadband Filter",
            "type": "type_filter",
            "optical_length": 0,
            "mass": 50,
            "tside_thread": '2"',
            "transmission": 0.95,
        }
    }

    @classmethod
    def Orion_SkyGlow_Broadband_Filter(cls):
        return cls.from_database(cls._DATABASE["Orion_SkyGlow_Broadband_Filter"])
