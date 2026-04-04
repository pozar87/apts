from ..base import FilterWheel


class OgmaFilterWheel(FilterWheel):
    _DATABASE = {
        "OGMA_OGC_FW7_M42": {
            "brand": "OGMA",
            "name": "OGC-FW7 (M42)",
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
        "OGMA_OGC_FW5_M48": {
            "brand": "OGMA",
            "name": "OGC-FW5 (M48)",
            "type": "type_filter_wheel",
            "optical_length": 20,
            "mass": 420,
            "tside_thread": "M48",
            "tside_gender": "Male",
            "cside_thread": "M48",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "OGMA_OGC_FW9_M54": {
            "brand": "OGMA",
            "name": "OGC-FW9 (M54)",
            "type": "type_filter_wheel",
            "optical_length": 21,
            "mass": 600,
            "tside_thread": "M54",
            "tside_gender": "Male",
            "cside_thread": "M54",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def OGMA_OGC_FW7_M42(cls):
        return cls.from_database(cls._DATABASE["OGMA_OGC_FW7_M42"])

    @classmethod
    def OGMA_OGC_FW5_M48(cls):
        return cls.from_database(cls._DATABASE["OGMA_OGC_FW5_M48"])

    @classmethod
    def OGMA_OGC_FW9_M54(cls):
        return cls.from_database(cls._DATABASE["OGMA_OGC_FW9_M54"])
