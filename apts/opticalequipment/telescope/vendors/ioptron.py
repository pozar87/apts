from ..base import Telescope

class IoptronTelescope(Telescope):
    _DATABASE = {'iOptron_iOptron_RC_6': {'brand': 'iOptron', 'name': 'iOptron RC 6"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 5200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'iOptron_iOptron_RC_8': {'brand': 'iOptron', 'name': 'iOptron RC 8"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 8800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M72', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'iOptron_iOptron_80mm_APO': {'brand': 'iOptron', 'name': 'iOptron 80mm APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'iOptron_iOptron_102mm_APO': {'brand': 'iOptron', 'name': 'iOptron 102mm APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def iOptron_iOptron_RC_6(cls):
        return cls.from_database(cls._DATABASE['iOptron_iOptron_RC_6'])

    @classmethod
    def iOptron_iOptron_RC_8(cls):
        return cls.from_database(cls._DATABASE['iOptron_iOptron_RC_8'])

    @classmethod
    def iOptron_iOptron_80mm_APO(cls):
        return cls.from_database(cls._DATABASE['iOptron_iOptron_80mm_APO'])

    @classmethod
    def iOptron_iOptron_102mm_APO(cls):
        return cls.from_database(cls._DATABASE['iOptron_iOptron_102mm_APO'])