from ..base import Focuser


class MoonliteFocuser(Focuser):
    _DATABASE = {'Moonlite_CS_2_Focuser': {'brand': 'Moonlite', 'name':
        'CS 2" Focuser', 'type': 'type_focuser', 'optical_length': 0,
        'mass': 800, 'tside_thread': '', 'tside_gender': 'Male',
        'cside_thread': '', 'cside_gender': 'Female', 'reversible': False,
        'bf_role': ''}, 'Moonlite_CSL_2_5_Focuser': {'brand': 'Moonlite',
        'name': 'CSL 2.5" Focuser', 'type': 'type_focuser',
        'optical_length': 0, 'mass': 1100, 'tside_thread': '',
        'tside_gender': 'Male', 'cside_thread': '', 'cside_gender':
        'Female', 'reversible': False, 'bf_role': ''},
        'Moonlite_NightCrawler_3_Focuser': {'brand': 'Moonlite', 'name':
        'NightCrawler 3" Focuser', 'type': 'type_focuser', 'optical_length':
        0, 'mass': 1500, 'tside_thread': '', 'tside_gender': 'Male',
        'cside_thread': '', 'cside_gender': 'Female', 'reversible': False,
        'bf_role': ''}, 'Moonlite_CR2_Focuser_2': {'brand': 'Moonlite',
        'name': 'CR2 Focuser (2")', 'type': 'type_focuser',
        'optical_length': 0, 'mass': 750, 'tside_thread': '',
        'tside_gender': 'Male', 'cside_thread': '', 'cside_gender':
        'Female', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Moonlite_CS_2_Focuser(cls):
        return cls.from_database(cls._DATABASE['Moonlite_CS_2_Focuser'])

    @classmethod
    def Moonlite_CSL_2_5_Focuser(cls):
        return cls.from_database(cls._DATABASE['Moonlite_CSL_2_5_Focuser'])

    @classmethod
    def Moonlite_NightCrawler_3_Focuser(cls):
        return cls.from_database(cls._DATABASE[
            'Moonlite_NightCrawler_3_Focuser'])

    @classmethod
    def Moonlite_CR2_Focuser_2(cls):
        return cls.from_database(cls._DATABASE['Moonlite_CR2_Focuser_2'])
