from ..base import FilterWheel


class SbigFilterWheel(FilterWheel):
    _DATABASE = {
        "SBIG_FW5_8300_M42": {
            "brand": "SBIG",
            "name": "FW5-8300 (M42)",
            "type": "type_filter_wheel",
            "optical_length": 18,
            "mass": 350,
            "tside_thread": "M42",
            "tside_gender": "Male",
            "cside_thread": "M42",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "SBIG_FW8_STT_M54": {
            "brand": "SBIG",
            "name": "FW8-STT (M54)",
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
        "SBIG_FW7_STX_M68": {
            "brand": "SBIG",
            "name": "FW7-STX (M68)",
            "type": "type_filter_wheel",
            "optical_length": 22,
            "mass": 800,
            "tside_thread": "M68",
            "tside_gender": "Male",
            "cside_thread": "M68",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def SBIG_FW5_8300_M42(cls):
        return cls.from_database(cls._DATABASE["SBIG_FW5_8300_M42"])

    @classmethod
    def SBIG_FW8_STT_M54(cls):
        return cls.from_database(cls._DATABASE["SBIG_FW8_STT_M54"])

    @classmethod
    def SBIG_FW7_STX_M68(cls):
        return cls.from_database(cls._DATABASE["SBIG_FW7_STX_M68"])
