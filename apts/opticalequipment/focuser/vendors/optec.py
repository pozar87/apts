from ..base import Focuser


class OptecFocuser(Focuser):
    _DATABASE = {
        "Optec_TCF_S": {
            "brand": "Optec",
            "name": "TCF-S",
            "type": "type_focuser",
            "optical_length": 0,
            "mass": 200,
            "tside_thread": "",
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Optec_TCF_S3": {
            "brand": "Optec",
            "name": "TCF-S3",
            "type": "type_focuser",
            "optical_length": 0,
            "mass": 250,
            "tside_thread": "",
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Optec_Leo_Focuser": {
            "brand": "Optec",
            "name": "Leo Focuser",
            "type": "type_focuser",
            "optical_length": 0,
            "mass": 350,
            "tside_thread": "",
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
        "Optec_FastFocus_FSQ": {
            "brand": "Optec",
            "name": "FastFocus FSQ",
            "type": "type_focuser",
            "optical_length": 0,
            "mass": 150,
            "tside_thread": "",
            "tside_gender": "Male",
            "cside_thread": "",
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "",
        },
    }

    @classmethod
    def Optec_TCF_S(cls):
        return cls.from_database(cls._DATABASE['Optec_TCF_S'])

    @classmethod
    def Optec_TCF_S3(cls):
        return cls.from_database(cls._DATABASE['Optec_TCF_S3'])

    @classmethod
    def Optec_Leo_Focuser(cls):
        return cls.from_database(cls._DATABASE['Optec_Leo_Focuser'])

    @classmethod
    def Optec_FastFocus_FSQ(cls):
        return cls.from_database(cls._DATABASE['Optec_FastFocus_FSQ'])
