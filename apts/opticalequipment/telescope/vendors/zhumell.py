from ..base import Telescope

class ZhumellTelescope(Telescope):
    _DATABASE = {'Zhumell_Z6_Dobsonian': {'brand': 'Zhumell', 'name': 'Z6 Dobsonian', 'type': 'type_telescope', 'optical_length': 0, 'mass': 5000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Zhumell_Z8_Dobsonian': {'brand': 'Zhumell', 'name': 'Z8 Dobsonian', 'type': 'type_telescope', 'optical_length': 0, 'mass': 7500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Zhumell_Z10_Dobsonian': {'brand': 'Zhumell', 'name': 'Z10 Dobsonian', 'type': 'type_telescope', 'optical_length': 0, 'mass': 10000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Zhumell_Z12_Dobsonian': {'brand': 'Zhumell', 'name': 'Z12 Dobsonian', 'type': 'type_telescope', 'optical_length': 0, 'mass': 14000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Zhumell_Z14_Dobsonian': {'brand': 'Zhumell', 'name': 'Z14 Dobsonian', 'type': 'type_telescope', 'optical_length': 0, 'mass': 19000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Zhumell_Z16_Dobsonian': {'brand': 'Zhumell', 'name': 'Z16 Dobsonian', 'type': 'type_telescope', 'optical_length': 0, 'mass': 27000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Zhumell_Z6_Dobsonian(cls):
        return cls.from_database(cls._DATABASE['Zhumell_Z6_Dobsonian'])

    @classmethod
    def Zhumell_Z8_Dobsonian(cls):
        return cls.from_database(cls._DATABASE['Zhumell_Z8_Dobsonian'])

    @classmethod
    def Zhumell_Z10_Dobsonian(cls):
        return cls.from_database(cls._DATABASE['Zhumell_Z10_Dobsonian'])

    @classmethod
    def Zhumell_Z12_Dobsonian(cls):
        return cls.from_database(cls._DATABASE['Zhumell_Z12_Dobsonian'])

    @classmethod
    def Zhumell_Z14_Dobsonian(cls):
        return cls.from_database(cls._DATABASE['Zhumell_Z14_Dobsonian'])

    @classmethod
    def Zhumell_Z16_Dobsonian(cls):
        return cls.from_database(cls._DATABASE['Zhumell_Z16_Dobsonian'])