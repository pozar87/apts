from ..base import FilterWheel


class AskarFilterWheel(FilterWheel):
    _DATABASE = {
        "Askar_Filter_Wheel_5x_M42": {
            "brand": "Askar",
            "name": "Filter Wheel 5x (M42)",
            "type": "type_filter_wheel",
            "optical_length": 19,
            "mass": 310,
            "tside_thread": "M42",
            "tside_gender": "Male",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_Filter_Wheel_7x_M48": {
            "brand": "Askar",
            "name": "Filter Wheel 7x (M48)",
            "type": "type_filter_wheel",
            "optical_length": 20,
            "mass": 450,
            "tside_thread": "M48",
            "tside_gender": "Male",
            "cside_thread": "M48",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Askar_Filter_Wheel_7x_M54": {
            "brand": "Askar",
            "name": "Filter Wheel 7x (M54)",
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
    def Askar_Filter_Wheel_5x_M42(cls):
        return cls.from_database(cls._DATABASE["Askar_Filter_Wheel_5x_M42"])

    @classmethod
    def Askar_Filter_Wheel_7x_M48(cls):
        return cls.from_database(cls._DATABASE["Askar_Filter_Wheel_7x_M48"])

    @classmethod
    def Askar_Filter_Wheel_7x_M54(cls):
        return cls.from_database(cls._DATABASE["Askar_Filter_Wheel_7x_M54"])
