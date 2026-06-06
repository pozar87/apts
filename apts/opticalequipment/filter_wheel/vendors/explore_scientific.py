from ..base import FilterWheel


class ExploreScientificFilterWheel(FilterWheel):
    _DATABASE = {
        "Explore_Scientific_Filter_Wheel_5x_M42": {
            "brand": "Explore Scientific",
            "name": "Filter Wheel 5x (M42)",
            "type": "type_filter_wheel",
            "optical_length": 18,
            "mass": 290,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Explore_Scientific_Filter_Wheel_7x_M48": {
            "brand": "Explore Scientific",
            "name": "Filter Wheel 7x (M48)",
            "type": "type_filter_wheel",
            "optical_length": 20,
            "mass": 450,
            "tside_thread": "M48",
            "tside_gender": "Female",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Explore_Scientific_Filter_Wheel_5x_M42(cls):
        return cls.from_database(cls._DATABASE[
            'Explore_Scientific_Filter_Wheel_5x_M42'])

    @classmethod
    def Explore_Scientific_Filter_Wheel_7x_M48(cls):
        return cls.from_database(cls._DATABASE[
            'Explore_Scientific_Filter_Wheel_7x_M48'])
