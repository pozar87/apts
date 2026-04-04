from ..base import FilterWheel, FilterHolder


class AltairFilterWheel(FilterWheel):
    _DATABASE = {
        "Altair_Filter_Wheel_5x1_25_M42": {
            "brand": "Altair",
            "name": 'Filter Wheel 5x1.25" (M42)',
            "type": "type_filter_wheel",
            "optical_length": 18,
            "mass": 320,
            "tside_thread": "M42",
            "tside_gender": "Male",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Altair_Filter_Wheel_7x2_M54": {
            "brand": "Altair",
            "name": 'Filter Wheel 7x2" (M54)',
            "type": "type_filter_wheel",
            "optical_length": 20,
            "mass": 600,
            "tside_thread": "M54",
            "tside_gender": "Male",
            "cside_thread": "M54",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Altair_Filter_Wheel_5x_M42": {
            "brand": "Altair",
            "name": "Filter Wheel 5x (M42)",
            "type": "type_filter_wheel",
            "optical_length": 19,
            "mass": 300,
            "tside_thread": "M42",
            "tside_gender": "Male",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Altair_Filter_Wheel_7x_M48": {
            "brand": "Altair",
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
        "Altair_Filter_Wheel_7x_M54": {
            "brand": "Altair",
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
    def Altair_Filter_Wheel_5x1_25_M42(cls):
        return cls.from_database(cls._DATABASE["Altair_Filter_Wheel_5x1_25_M42"])

    @classmethod
    def Altair_Filter_Wheel_7x2_M54(cls):
        return cls.from_database(cls._DATABASE["Altair_Filter_Wheel_7x2_M54"])

    @classmethod
    def Altair_Filter_Wheel_5x_M42(cls):
        return cls.from_database(cls._DATABASE["Altair_Filter_Wheel_5x_M42"])

    @classmethod
    def Altair_Filter_Wheel_7x_M48(cls):
        return cls.from_database(cls._DATABASE["Altair_Filter_Wheel_7x_M48"])

    @classmethod
    def Altair_Filter_Wheel_7x_M54(cls):
        return cls.from_database(cls._DATABASE["Altair_Filter_Wheel_7x_M54"])


class AltairFilterHolder(FilterHolder):
    _DATABASE = {
        "Altair_Filter_Drawer_M48": {
            "brand": "Altair",
            "name": "Filter Drawer (M48)",
            "type": "type_filter_holder",
            "optical_length": 25,
            "mass": 200,
            "tside_thread": "M48",
            "tside_gender": "Male",
            "cside_thread": "M48",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Altair_Filter_Drawer_M54": {
            "brand": "Altair",
            "name": "Filter Drawer (M54)",
            "type": "type_filter_holder",
            "optical_length": 25,
            "mass": 230,
            "tside_thread": "M54",
            "tside_gender": "Male",
            "cside_thread": "M54",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Altair_Filter_Drawer_M48(cls):
        return cls.from_database(cls._DATABASE["Altair_Filter_Drawer_M48"])

    @classmethod
    def Altair_Filter_Drawer_M54(cls):
        return cls.from_database(cls._DATABASE["Altair_Filter_Drawer_M54"])
