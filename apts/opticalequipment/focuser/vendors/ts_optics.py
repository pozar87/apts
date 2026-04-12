from ..base import Focuser


class TSOpticsFocuser(Focuser):
    _DATABASE = {
        "TS_Optics_2_Crayford_Focuser": {'brand': 'TS-Optics', 'name': '2" Crayford Focuser', 'type': 'type_focuser', 'optical_length': 0, 'mass': 580, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
        "TS_Optics_3_Rack_Pinion_Focuser": {'brand': 'TS-Optics', 'name': '3" Rack & Pinion Focuser', 'type': 'type_focuser', 'optical_length': 0, 'mass': 1000, 'tside_thread': 'M68', 'tside_gender': 'Male', 'cside_thread': 'M68', 'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
    }

    @classmethod
    def TS_Optics_2_Crayford_Focuser(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_2_Crayford_Focuser"])

    @classmethod
    def TS_Optics_3_Rack_Pinion_Focuser(cls):
        return cls.from_database(cls._DATABASE["TS_Optics_3_Rack_Pinion_Focuser"])
