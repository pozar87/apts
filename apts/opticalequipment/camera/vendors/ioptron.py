from ..base import Camera

class IoptronCamera(Camera):
    _DATABASE = {'iOptron_iGuider_174M': {'brand': 'iOptron', 'name': 'iGuider 174M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}}

    @classmethod
    def iOptron_iGuider_174M(cls):
        return cls.from_database(cls._DATABASE['iOptron_iGuider_174M'])