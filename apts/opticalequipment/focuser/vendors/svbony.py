from ..base import Focuser


class SVBonyFocuser(Focuser):
    _DATABASE = {'SVBony_SV231_Electronic_Focuser': {'brand': 'SVBony',
        'name': 'SV231 Electronic Focuser', 'type': 'type_focuser',
        'optical_length': 0, 'mass': 120, 'tside_thread': '',
        'tside_gender': 'Male', 'cside_thread': '', 'cside_gender':
        'Female', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def SVBony_SV231_Electronic_Focuser(cls):
        return cls.from_database(cls._DATABASE[
            'SVBony_SV231_Electronic_Focuser'])
