from ..base import FilterWheel


class ToupTekFilterWheel(FilterWheel):
    _DATABASE = {
        "ToupTek_Filter_Wheel_5x1_25_M42": {
            "brand": "ToupTek",
            "name": "Filter Wheel 5x1.25\" (M42)",
            "type": "type_filter_wheel",
            "optical_length": 18,
            "mass": 300,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "ToupTek_Filter_Wheel_7x2_M54": {
            "brand": "ToupTek",
            "name": "Filter Wheel 7x2\" (M54)",
            "type": "type_filter_wheel",
            "optical_length": 20,
            "mass": 550,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def ToupTek_Filter_Wheel_5x1_25_M42(cls):
        return cls.from_database(cls._DATABASE[
            'ToupTek_Filter_Wheel_5x1_25_M42'])

    @classmethod
    def ToupTek_Filter_Wheel_7x2_M54(cls):
        return cls.from_database(cls._DATABASE['ToupTek_Filter_Wheel_7x2_M54'])
