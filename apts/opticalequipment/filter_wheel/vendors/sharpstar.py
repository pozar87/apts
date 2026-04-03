from ..base import FilterWheel


class SharpstarFilterWheel(FilterWheel):
    _DATABASE = {
        "Sharpstar_Filter_Wheel_5x_M42": {
            "brand": "Sharpstar",
            "name": "Filter Wheel 5x (M42)",
            "type": "type_filter_wheel",
            "optical_length": 18,
            "mass": 290,
            "tside_thread": "M42",
            "tside_gender": "Male",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Sharpstar_Filter_Wheel_7x_M48": {
            "brand": "Sharpstar",
            "name": "Filter Wheel 7x (M48)",
            "type": "type_filter_wheel",
            "optical_length": 20,
            "mass": 440,
            "tside_thread": "M48",
            "tside_gender": "Male",
            "cside_thread": "M48",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Sharpstar_Filter_Wheel_5x_M42(cls):
        return cls.from_database(cls._DATABASE["Sharpstar_Filter_Wheel_5x_M42"])

    @classmethod
    def Sharpstar_Filter_Wheel_7x_M48(cls):
        return cls.from_database(cls._DATABASE["Sharpstar_Filter_Wheel_7x_M48"])
