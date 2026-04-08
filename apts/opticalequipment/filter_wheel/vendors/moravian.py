from ..base import FilterWheel


class MoravianFilterWheel(FilterWheel):
    _DATABASE = {
        "Moravian_IFW_Internal_FW": {
            "brand": "Moravian",
            "name": "IFW (Internal FW)",
            "type": "type_filter_wheel",
            "optical_length": 0,
            "mass": 300,
            "tside_thread": "M54",
            "tside_gender": "Male",
            "cside_thread": "M54",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Moravian_EFW_2H_M42": {
            "brand": "Moravian",
            "name": "EFW-2H (M42)",
            "type": "type_filter_wheel",
            "optical_length": 18,
            "mass": 350,
            "tside_thread": "M42",
            "tside_gender": "Male",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Moravian_EFW_3H_M54": {
            "brand": "Moravian",
            "name": "EFW-3H (M54)",
            "type": "type_filter_wheel",
            "optical_length": 20,
            "mass": 550,
            "tside_thread": "M54",
            "tside_gender": "Male",
            "cside_thread": "M54",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Moravian_IFW_Internal_FW(cls):
        return cls.from_database(cls._DATABASE["Moravian_IFW_Internal_FW"])

    @classmethod
    def Moravian_EFW_2H_M42(cls):
        return cls.from_database(cls._DATABASE["Moravian_EFW_2H_M42"])

    @classmethod
    def Moravian_EFW_3H_M54(cls):
        return cls.from_database(cls._DATABASE["Moravian_EFW_3H_M54"])
