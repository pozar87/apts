from ..base import Focuser


class PlayerOneFocuser(Focuser):
    _DATABASE = {'Player_One_Electronic_Focuser': {'brand': 'Player One',
        'name': 'Electronic Focuser', 'type': 'type_focuser',
        'optical_length': 0, 'mass': 130, 'tside_thread': '',
        'tside_gender': 'Male', 'cside_thread': '', 'cside_gender':
        'Female', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Player_One_Electronic_Focuser(cls):
        return cls.from_database(cls._DATABASE['Player_One_Electronic_Focuser']
            )
