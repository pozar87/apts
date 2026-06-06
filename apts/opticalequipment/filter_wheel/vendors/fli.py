from ..base import FilterWheel


class FliFilterWheel(FilterWheel):
    _DATABASE = {
        "FLI_CFW_2_7_M54": {
            "brand": "FLI",
            "name": "CFW-2-7 (M54)",
            "type": "type_filter_wheel",
            "optical_length": 20,
            "mass": 600,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "FLI_CFW_3_10_M68": {
            "brand": "FLI",
            "name": "CFW-3-10 (M68)",
            "type": "type_filter_wheel",
            "optical_length": 22,
            "mass": 800,
            "tside_thread": "M68",
            "tside_gender": "Female",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "FLI_Atlas_M54": {
            "brand": "FLI",
            "name": "Atlas (M54)",
            "type": "type_filter_wheel",
            "optical_length": 20,
            "mass": 700,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "FLI_CenterLine_M42": {
            "brand": "FLI",
            "name": "CenterLine (M42)",
            "type": "type_filter_wheel",
            "optical_length": 18,
            "mass": 400,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "FLI_CenterLine_M68": {
            "brand": "FLI",
            "name": "CenterLine (M68)",
            "type": "type_filter_wheel",
            "optical_length": 22,
            "mass": 750,
            "tside_thread": "M68",
            "tside_gender": "Female",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def FLI_CFW_2_7_M54(cls):
        return cls.from_database(cls._DATABASE['FLI_CFW_2_7_M54'])

    @classmethod
    def FLI_CFW_3_10_M68(cls):
        return cls.from_database(cls._DATABASE['FLI_CFW_3_10_M68'])

    @classmethod
    def FLI_Atlas_M54(cls):
        return cls.from_database(cls._DATABASE['FLI_Atlas_M54'])

    @classmethod
    def FLI_CenterLine_M42(cls):
        return cls.from_database(cls._DATABASE['FLI_CenterLine_M42'])

    @classmethod
    def FLI_CenterLine_M68(cls):
        return cls.from_database(cls._DATABASE['FLI_CenterLine_M68'])
