from ..base import FilterWheel, FilterHolder


class CelestronFilterWheel(FilterWheel):
    _DATABASE = {
        "Celestron_Filter_Wheel_5x_M42": {
            "brand": "Celestron",
            "name": "Filter Wheel 5x (M42)",
            "type": "type_filter_wheel",
            "optical_length": 18,
            "mass": 280,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Filter_Wheel_7x_M48": {
            "brand": "Celestron",
            "name": "Filter Wheel 7x (M48)",
            "type": "type_filter_wheel",
            "optical_length": 20,
            "mass": 440,
            "tside_thread": "M48",
            "tside_gender": "Female",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Celestron_Filter_Wheel_5x_M42(cls):
        return cls.from_database(cls._DATABASE['Celestron_Filter_Wheel_5x_M42']
            )

    @classmethod
    def Celestron_Filter_Wheel_7x_M48(cls):
        return cls.from_database(cls._DATABASE['Celestron_Filter_Wheel_7x_M48']
            )


class CelestronFilterHolder(FilterHolder):
    _DATABASE = {
        "Celestron_Filter_Slide_1_25": {
            "brand": "Celestron",
            "name": "Filter Slide 1.25\"",
            "type": "type_filter_holder",
            "optical_length": 8,
            "mass": 100,
            "tside_thread": "1.25\"",
            "tside_gender": "Male",
            "cside_thread": "1.25\"",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Celestron_Filter_Slide_1_25(cls):
        return cls.from_database(cls._DATABASE['Celestron_Filter_Slide_1_25'])
    _DATABASE = {
        "Celestron_Filter_Wheel_5x_M42": {
            "brand": "Celestron",
            "name": "Filter Wheel 5x (M42)",
            "type": "type_filter_wheel",
            "optical_length": 18,
            "mass": 280,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Celestron_Filter_Wheel_7x_M48": {
            "brand": "Celestron",
            "name": "Filter Wheel 7x (M48)",
            "type": "type_filter_wheel",
            "optical_length": 20,
            "mass": 440,
            "tside_thread": "M48",
            "tside_gender": "Female",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
    }
