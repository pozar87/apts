from ..base import Focuser


class RigelSystemsFocuser(Focuser):
    _DATABASE = {'Rigel_Systems_nFocus': {'brand': 'Rigel Systems', 'name':
        'nFocus', 'type': 'type_focuser', 'optical_length': 0, 'mass': 120,
        'tside_thread': '', 'tside_gender': 'Male', 'cside_thread': '',
        'cside_gender': 'Female', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Rigel_Systems_nFocus(cls):
        return cls.from_database(cls._DATABASE['Rigel_Systems_nFocus'])
