from ..base import FilterWheel


class VixenFilterWheel(FilterWheel):
    _DATABASE = {
        "Vixen_Filter_Wheel_5x_M42": {
            "brand": "Vixen",
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
    }

    @classmethod
    def Vixen_Filter_Wheel_5x_M42(cls):
        return cls.from_database(cls._DATABASE['Vixen_Filter_Wheel_5x_M42'])
