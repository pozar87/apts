from ..base import Telescope

class SkyvisionTelescope(Telescope):
    _DATABASE = {'SkyVision_SkyVision_T500_20': {'brand': 'SkyVision', 'name': 'SkyVision T500 (20")', 'type': 'type_telescope', 'optical_length': 0, 'mass': 35000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'SkyVision_SkyVision_T600_24': {'brand': 'SkyVision', 'name': 'SkyVision T600 (24")', 'type': 'type_telescope', 'optical_length': 0, 'mass': 50000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'SkyVision_SkyVision_T700_28': {'brand': 'SkyVision', 'name': 'SkyVision T700 (28")', 'type': 'type_telescope', 'optical_length': 0, 'mass': 65000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'SkyVision_SkyVision_T400_16': {'brand': 'SkyVision', 'name': 'SkyVision T400 (16")', 'type': 'type_telescope', 'optical_length': 0, 'mass': 22000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def SkyVision_SkyVision_T500_20(cls):
        return cls.from_database(cls._DATABASE['SkyVision_SkyVision_T500_20'])

    @classmethod
    def SkyVision_SkyVision_T600_24(cls):
        return cls.from_database(cls._DATABASE['SkyVision_SkyVision_T600_24'])

    @classmethod
    def SkyVision_SkyVision_T700_28(cls):
        return cls.from_database(cls._DATABASE['SkyVision_SkyVision_T700_28'])

    @classmethod
    def SkyVision_SkyVision_T400_16(cls):
        return cls.from_database(cls._DATABASE['SkyVision_SkyVision_T400_16'])