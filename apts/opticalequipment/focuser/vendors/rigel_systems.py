from ..base import Focuser


class RigelSystemsFocuser(Focuser):
    _DATABASE = {
        "Rigel_Systems_nFocus": {'brand': 'Rigel Systems', 'name': 'nFocus', 'type': 'type_focuser', 'optical_length': 0, 'mass': 120, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
    }

    @classmethod
    def Rigel_Systems_nFocus(cls):
        return cls.from_database(cls._DATABASE["Rigel_Systems_nFocus"])
