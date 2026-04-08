from ..base import FilterWheel


class AtikFilterWheel(FilterWheel):
    _DATABASE = {
        "Atik_EFW2_M42": {
            "brand": "Atik",
            "name": "EFW2 (M42)",
            "type": "type_filter_wheel",
            "optical_length": 20,
            "mass": 350,
            "tside_thread": "M42",
            "tside_gender": "Male",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Atik_EFW3_M54": {
            "brand": "Atik",
            "name": "EFW3 (M54)",
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
    def Atik_EFW2_M42(cls):
        return cls.from_database(cls._DATABASE["Atik_EFW2_M42"])

    @classmethod
    def Atik_EFW3_M54(cls):
        return cls.from_database(cls._DATABASE["Atik_EFW3_M54"])
