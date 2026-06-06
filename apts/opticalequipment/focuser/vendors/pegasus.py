from ..base import Focuser


class PegasusFocuser(Focuser):
    _DATABASE = {'Pegasus_FocusCube_3': {'brand': 'Pegasus', 'name':
        'FocusCube 3', 'type': 'type_focuser', 'optical_length': 0, 'mass':
        115, 'tside_thread': '', 'tside_gender': 'Male', 'cside_thread': '',
        'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Pegasus_FocusCube_2': {'brand': 'Pegasus', 'name': 'FocusCube 2',
        'type': 'type_focuser', 'optical_length': 0, 'mass': 100,
        'tside_thread': '', 'tside_gender': 'Male', 'cside_thread': '',
        'cside_gender': 'Female', 'reversible': False, 'bf_role': ''},
        'Pegasus_NYX_Focuser': {'brand': 'Pegasus', 'name': 'NYX Focuser',
        'type': 'type_focuser', 'optical_length': 0, 'mass': 300,
        'tside_thread': '', 'tside_gender': 'Male', 'cside_thread': '',
        'cside_gender': 'Female', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Pegasus_FocusCube_3(cls):
        return cls.from_database(cls._DATABASE['Pegasus_FocusCube_3'])

    @classmethod
    def Pegasus_FocusCube_2(cls):
        return cls.from_database(cls._DATABASE['Pegasus_FocusCube_2'])

    @classmethod
    def Pegasus_NYX_Focuser(cls):
        return cls.from_database(cls._DATABASE['Pegasus_NYX_Focuser'])
