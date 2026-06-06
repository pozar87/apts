from ..base import FilterWheel, FilterHolder


class PlayerOneFilterWheel(FilterWheel):
    _DATABASE = {
        "Player_One_Xena_M_M42": {
            "brand": "Player One",
            "name": "Xena-M (M42)",
            "type": "type_filter_wheel",
            "optical_length": 20,
            "mass": 350,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Player_One_Xena_L_M54": {
            "brand": "Player One",
            "name": "Xena-L (M54)",
            "type": "type_filter_wheel",
            "optical_length": 21,
            "mass": 600,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Player_One_Xena_XL_M68": {
            "brand": "Player One",
            "name": "Xena-XL (M68)",
            "type": "type_filter_wheel",
            "optical_length": 22,
            "mass": 800,
            "tside_thread": "M68",
            "tside_gender": "Female",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Player_One_Xena_S_M42": {
            "brand": "Player One",
            "name": "Xena-S (M42)",
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
    def Player_One_Xena_M_M42(cls):
        return cls.from_database(cls._DATABASE['Player_One_Xena_M_M42'])

    @classmethod
    def Player_One_Xena_L_M54(cls):
        return cls.from_database(cls._DATABASE['Player_One_Xena_L_M54'])

    @classmethod
    def Player_One_Xena_XL_M68(cls):
        return cls.from_database(cls._DATABASE['Player_One_Xena_XL_M68'])

    @classmethod
    def Player_One_Xena_S_M42(cls):
        return cls.from_database(cls._DATABASE['Player_One_Xena_S_M42'])


class PlayerOneFilterHolder(FilterHolder):
    _DATABASE = {
        "Player_One_Filter_Drawer_M48": {
            "brand": "Player One",
            "name": "Filter Drawer (M48)",
            "type": "type_filter_holder",
            "optical_length": 25,
            "mass": 190,
            "tside_thread": "M48",
            "tside_gender": "Female",
            "cside_thread": "M48",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Player_One_Filter_Drawer_M54": {
            "brand": "Player One",
            "name": "Filter Drawer (M54)",
            "type": "type_filter_holder",
            "optical_length": 25,
            "mass": 220,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Player_One_Filter_Drawer_M48(cls):
        return cls.from_database(cls._DATABASE['Player_One_Filter_Drawer_M48'])

    @classmethod
    def Player_One_Filter_Drawer_M54(cls):
        return cls.from_database(cls._DATABASE['Player_One_Filter_Drawer_M54'])
    _DATABASE = {
        "Player_One_Xena_M_M42": {
            "brand": "Player One",
            "name": "Xena-M (M42)",
            "type": "type_filter_wheel",
            "optical_length": 20,
            "mass": 350,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Player_One_Xena_L_M54": {
            "brand": "Player One",
            "name": "Xena-L (M54)",
            "type": "type_filter_wheel",
            "optical_length": 21,
            "mass": 600,
            "tside_thread": "M54",
            "tside_gender": "Female",
            "cside_thread": "M54",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Player_One_Xena_XL_M68": {
            "brand": "Player One",
            "name": "Xena-XL (M68)",
            "type": "type_filter_wheel",
            "optical_length": 22,
            "mass": 800,
            "tside_thread": "M68",
            "tside_gender": "Female",
            "cside_thread": "M68",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Player_One_Xena_S_M42": {
            "brand": "Player One",
            "name": "Xena-S (M42)",
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
