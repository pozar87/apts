from ..base import FilterWheel


class QhyFilterWheel(FilterWheel):
    _DATABASE = {
        "QHY_CFW3S_Small": {
            "brand": "QHY",
            "name": "CFW3S Small",
            "type": "type_filter_wheel",
            "optical_length": 20,
            "mass": 450,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "QHY_CFW3M_Medium": {
            "brand": "QHY",
            "name": "CFW3M Medium",
            "type": "type_filter_wheel",
            "optical_length": 20,
            "mass": 600,
            "tside_thread": "M48",
            "tside_gender": "Female",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "QHY_CFW3L_Large": {
            "brand": "QHY",
            "name": "CFW3L Large",
            "type": "type_filter_wheel",
            "optical_length": 20,
            "mass": 850,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "QHY_CFW3XL_Extra_Large": {
            "brand": "QHY",
            "name": "CFW3XL Extra Large",
            "type": "type_filter_wheel",
            "optical_length": 22,
            "mass": 1000,
            "tside_thread": "M68",
            "tside_gender": "Female",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "QHY_CFW3S_US_Ultra_Slim": {
            "brand": "QHY",
            "name": "CFW3S-US Ultra Slim",
            "type": "type_filter_wheel",
            "optical_length": 14,
            "mass": 350,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def QHY_CFW3S_Small(cls):
        return cls.from_database(cls._DATABASE['QHY_CFW3S_Small'])

    @classmethod
    def QHY_CFW3M_Medium(cls):
        return cls.from_database(cls._DATABASE['QHY_CFW3M_Medium'])

    @classmethod
    def QHY_CFW3L_Large(cls):
        return cls.from_database(cls._DATABASE['QHY_CFW3L_Large'])

    @classmethod
    def QHY_CFW3XL_Extra_Large(cls):
        return cls.from_database(cls._DATABASE['QHY_CFW3XL_Extra_Large'])

    @classmethod
    def QHY_CFW3S_US_Ultra_Slim(cls):
        return cls.from_database(cls._DATABASE['QHY_CFW3S_US_Ultra_Slim'])
