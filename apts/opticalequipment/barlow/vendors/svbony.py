from ..base import Barlow

class SVBonyBarlow(Barlow):
    _DATABASE = {
        "SVBony_SV137_2x_Barlow": {
            "brand": "SVBony",
            "name": "SV137 2x Barlow",
            "type": "type_barlow",
            "optical_length": 0,
            "mass": 90,
            "tside_thread": '1.25"',
            "tside_gender": "Male",
            "cside_thread": '1.25"',
            "cside_gender": "Female",
            "reversible": False,
            "bf_role": "start",
        },
    }

    @classmethod
    def SVBony_SV137_2x_Barlow(cls):
        return cls.from_database(cls._DATABASE["SVBony_SV137_2x_Barlow"])
