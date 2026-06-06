from ..base import FilterWheel


class OrionFilterWheel(FilterWheel):
    _DATABASE = {
        "Orion_Nautilus_5x_M42": {
            "brand": "Orion",
            "name": "Nautilus 5x (M42)",
            "type": "type_filter_wheel",
            "optical_length": 19,
            "mass": 300,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "M42",
            "cside_gender": "Male",
            "reversible": False,
            "bf_role": "",
        },
        "Orion_Nautilus_7x_M48": {
            "brand": "Orion",
            "name": "Nautilus 7x (M48)",
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
    def Orion_Nautilus_5x_M42(cls):
        return cls.from_database(cls._DATABASE['Orion_Nautilus_5x_M42'])

    @classmethod
    def Orion_Nautilus_7x_M48(cls):
        return cls.from_database(cls._DATABASE['Orion_Nautilus_7x_M48'])
