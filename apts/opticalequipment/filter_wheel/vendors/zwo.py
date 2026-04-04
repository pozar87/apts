from ..base import FilterWheel, FilterHolder


class ZwoFilterWheel(FilterWheel):
    _DATABASE = {
        "ZWO_EFW_Mini_5x1_25": {
            "brand": "ZWO",
            "name": 'EFW Mini 5x1.25"',
            "type": "type_filter_wheel",
            "optical_length": 20,
            "mass": 265,
            "tside_thread": "M42",
            "tside_gender": "Male",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "ZWO_EFW_8x1_25": {
            "brand": "ZWO",
            "name": 'EFW 8x1.25"',
            "type": "type_filter_wheel",
            "optical_length": 20,
            "mass": 380,
            "tside_thread": "M42",
            "tside_gender": "Male",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "ZWO_EFW_7x36mm": {
            "brand": "ZWO",
            "name": "EFW 7x36mm",
            "type": "type_filter_wheel",
            "optical_length": 20,
            "mass": 400,
            "tside_thread": "M42",
            "tside_gender": "Male",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "ZWO_EFW_5x2_M48": {
            "brand": "ZWO",
            "name": 'EFW 5x2" (M48)',
            "type": "type_filter_wheel",
            "optical_length": 20,
            "mass": 550,
            "tside_thread": "M48",
            "tside_gender": "Male",
            "cside_thread": "M48",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "ZWO_EFW_5x2_M54": {
            "brand": "ZWO",
            "name": 'EFW 5x2" (M54)',
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
        "ZWO_EFW_7x2_M54": {
            "brand": "ZWO",
            "name": 'EFW 7x2" (M54)',
            "type": "type_filter_wheel",
            "optical_length": 20,
            "mass": 700,
            "tside_thread": "M54",
            "tside_gender": "Male",
            "cside_thread": "M54",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "ZWO_EFW_7x50mm_M54": {
            "brand": "ZWO",
            "name": "EFW 7x50mm (M54)",
            "type": "type_filter_wheel",
            "optical_length": 20,
            "mass": 700,
            "tside_thread": "M54",
            "tside_gender": "Male",
            "cside_thread": "M54",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def ZWO_EFW_Mini_5x1_25(cls):
        return cls.from_database(cls._DATABASE["ZWO_EFW_Mini_5x1_25"])

    @classmethod
    def ZWO_EFW_8x1_25(cls):
        return cls.from_database(cls._DATABASE["ZWO_EFW_8x1_25"])

    @classmethod
    def ZWO_EFW_7x36mm(cls):
        return cls.from_database(cls._DATABASE["ZWO_EFW_7x36mm"])

    @classmethod
    def ZWO_EFW_5x2_M48(cls):
        return cls.from_database(cls._DATABASE["ZWO_EFW_5x2_M48"])

    @classmethod
    def ZWO_EFW_5x2_M54(cls):
        return cls.from_database(cls._DATABASE["ZWO_EFW_5x2_M54"])

    @classmethod
    def ZWO_EFW_7x2_M54(cls):
        return cls.from_database(cls._DATABASE["ZWO_EFW_7x2_M54"])

    @classmethod
    def ZWO_EFW_7x50mm_M54(cls):
        return cls.from_database(cls._DATABASE["ZWO_EFW_7x50mm_M54"])


class ZwoFilterHolder(FilterHolder):
    _DATABASE = {
        "ZWO_Filter_Drawer_M48": {
            "brand": "ZWO",
            "name": "Filter Drawer (M48)",
            "type": "type_filter_holder",
            "optical_length": 26.5,
            "mass": 220,
            "tside_thread": "M48",
            "tside_gender": "Male",
            "cside_thread": "M48",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "ZWO_Filter_Drawer_M54": {
            "brand": "ZWO",
            "name": "Filter Drawer (M54)",
            "type": "type_filter_holder",
            "optical_length": 26.5,
            "mass": 250,
            "tside_thread": "M54",
            "tside_gender": "Male",
            "cside_thread": "M54",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "ZWO_Filter_Drawer_EOS_EF": {
            "brand": "ZWO",
            "name": "Filter Drawer EOS-EF",
            "type": "type_filter_holder",
            "optical_length": 26.5,
            "mass": 230,
            "tside_thread": "EOS",
            "tside_gender": "Male",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def ZWO_Filter_Drawer_M48(cls):
        return cls.from_database(cls._DATABASE["ZWO_Filter_Drawer_M48"])

    @classmethod
    def ZWO_Filter_Drawer_M54(cls):
        return cls.from_database(cls._DATABASE["ZWO_Filter_Drawer_M54"])

    @classmethod
    def ZWO_Filter_Drawer_EOS_EF(cls):
        return cls.from_database(cls._DATABASE["ZWO_Filter_Drawer_EOS_EF"])
