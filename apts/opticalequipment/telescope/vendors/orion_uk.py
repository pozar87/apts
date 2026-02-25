from ..base import Telescope

class Orion_ukTelescope(Telescope):
    _DATABASE = {'Orion_UK_VX6_6_Newt': {'brand': 'Orion UK', 'name': 'VX6 (6" Newt)', 'type': 'type_telescope', 'optical_length': 0, 'mass': 5200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Orion_UK_VX8_8_Newt': {'brand': 'Orion UK', 'name': 'VX8 (8" Newt)', 'type': 'type_telescope', 'optical_length': 0, 'mass': 8500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Orion_UK_VX10_10_Newt': {'brand': 'Orion UK', 'name': 'VX10 (10" Newt)', 'type': 'type_telescope', 'optical_length': 0, 'mass': 12000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Orion_UK_VX12_12_Newt': {'brand': 'Orion UK', 'name': 'VX12 (12" Newt)', 'type': 'type_telescope', 'optical_length': 0, 'mass': 16000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Orion_UK_Europa_200_f_4': {'brand': 'Orion UK', 'name': 'Europa 200 f/4', 'type': 'type_telescope', 'optical_length': 0, 'mass': 7800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Orion_UK_ODK_10': {'brand': 'Orion UK', 'name': 'ODK 10"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 11000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Orion_UK_ODK_12': {'brand': 'Orion UK', 'name': 'ODK 12"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 15000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Orion_UK_ODK_14': {'brand': 'Orion UK', 'name': 'ODK 14"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 20000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M68', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Orion_UK_ODK_16': {'brand': 'Orion UK', 'name': 'ODK 16"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 26000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Orion_UK_AG12_12_AG': {'brand': 'Orion UK', 'name': 'AG12 (12" AG)', 'type': 'type_telescope', 'optical_length': 0, 'mass': 14000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M84', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Orion_UK_VX6_6_Newt(cls):
        return cls.from_database(cls._DATABASE['Orion_UK_VX6_6_Newt'])

    @classmethod
    def Orion_UK_VX8_8_Newt(cls):
        return cls.from_database(cls._DATABASE['Orion_UK_VX8_8_Newt'])

    @classmethod
    def Orion_UK_VX10_10_Newt(cls):
        return cls.from_database(cls._DATABASE['Orion_UK_VX10_10_Newt'])

    @classmethod
    def Orion_UK_VX12_12_Newt(cls):
        return cls.from_database(cls._DATABASE['Orion_UK_VX12_12_Newt'])

    @classmethod
    def Orion_UK_Europa_200_f_4(cls):
        return cls.from_database(cls._DATABASE['Orion_UK_Europa_200_f_4'])

    @classmethod
    def Orion_UK_ODK_10(cls):
        return cls.from_database(cls._DATABASE['Orion_UK_ODK_10'])

    @classmethod
    def Orion_UK_ODK_12(cls):
        return cls.from_database(cls._DATABASE['Orion_UK_ODK_12'])

    @classmethod
    def Orion_UK_ODK_14(cls):
        return cls.from_database(cls._DATABASE['Orion_UK_ODK_14'])

    @classmethod
    def Orion_UK_ODK_16(cls):
        return cls.from_database(cls._DATABASE['Orion_UK_ODK_16'])

    @classmethod
    def Orion_UK_AG12_12_AG(cls):
        return cls.from_database(cls._DATABASE['Orion_UK_AG12_12_AG'])