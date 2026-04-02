from ..base import Telescope

class IoptronTelescope(Telescope):
    _DATABASE = {
        'iOptron_iOptron_RC_6': {'brand': 'iOptron', 'name': 'iOptron RC 6"', 'type': 'catadioptric', 'optical_length': 0, 'mass': 5400, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M90', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 152, 'focal_length_mm': 1370, 'central_obstruction_mm': 61},
        'iOptron_iOptron_RC_8': {'brand': 'iOptron', 'name': 'iOptron RC 8"', 'type': 'catadioptric', 'optical_length': 0, 'mass': 7500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M90', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 203, 'focal_length_mm': 1624, 'central_obstruction_mm': 85},
        'iOptron_iOptron_80mm_APO': {'brand': 'iOptron', 'name': 'iOptron 80mm APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3100, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 80, 'focal_length_mm': 480},
        'iOptron_iOptron_102mm_APO': {'brand': 'iOptron', 'name': 'iOptron 102mm APO', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 102, 'focal_length_mm': 714},
    }

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
