from ..base import Focuser


class SkyWatcherFocuser(Focuser):
    _DATABASE = {'Sky_Watcher_2_Crayford_Focuser': {'brand': 'Sky-Watcher',
        'name': '2" Crayford Focuser', 'type': 'type_focuser',
        'optical_length': 0, 'mass': 550, 'tside_thread': '',
        'tside_gender': 'Male', 'cside_thread': '', 'cside_gender':
        'Female', 'reversible': False, 'bf_role': ''},
        'Sky_Watcher_2_Dual_Speed_Focuser': {'brand': 'Sky-Watcher', 'name':
        '2" Dual-Speed Focuser', 'type': 'type_focuser', 'optical_length': 
        0, 'mass': 620, 'tside_thread': '', 'tside_gender': 'Male',
        'cside_thread': '', 'cside_gender': 'Female', 'reversible': False,
        'bf_role': ''}}

    @classmethod
    def Sky_Watcher_2_Crayford_Focuser(cls):
        return cls.from_database(cls._DATABASE[
            'Sky_Watcher_2_Crayford_Focuser'])

    @classmethod
    def Sky_Watcher_2_Dual_Speed_Focuser(cls):
        return cls.from_database(cls._DATABASE[
            'Sky_Watcher_2_Dual_Speed_Focuser'])
