from ..base import Telescope

class BorgTelescope(Telescope):
    _DATABASE = {'Borg_55FL': {'brand': 'Borg', 'name': '55FL', 'type': 'type_refractor', 'optical_length': 0, 'mass': 800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Borg_71FL': {'brand': 'Borg', 'name': '71FL', 'type': 'type_refractor', 'optical_length': 0, 'mass': 1200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Borg_89ED': {'brand': 'Borg', 'name': '89ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Borg_107FL': {'brand': 'Borg', 'name': '107FL', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Borg_90FL': {'brand': 'Borg', 'name': '90FL', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Borg_77EDII': {'brand': 'Borg', 'name': '77EDII', 'type': 'type_refractor', 'optical_length': 0, 'mass': 1800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Borg_55FL(cls):
        return cls.from_database(cls._DATABASE['Borg_55FL'])

    @classmethod
    def Borg_71FL(cls):
        return cls.from_database(cls._DATABASE['Borg_71FL'])

    @classmethod
    def Borg_89ED(cls):
        return cls.from_database(cls._DATABASE['Borg_89ED'])

    @classmethod
    def Borg_107FL(cls):
        return cls.from_database(cls._DATABASE['Borg_107FL'])

    @classmethod
    def Borg_90FL(cls):
        return cls.from_database(cls._DATABASE['Borg_90FL'])

    @classmethod
    def Borg_77EDII(cls):
        return cls.from_database(cls._DATABASE['Borg_77EDII'])