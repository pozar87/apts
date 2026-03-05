from ..base import Camera

class MicrosoftCamera(Camera):
    _DATABASE = {
        'Microsoft_LifeCam_HD_3000_afocal': {
            'brand': 'Microsoft',
            'name': 'LifeCam HD-3000 (afocal)',
            'type': 'type_camera',
            'optical_length': 0,
            'mass': 110,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 3.6,
            'sensor_height_mm': 2.0,
            'width': 1280,
            'height': 720,
            'pixel_size_um': 2.8
        }
    }

    @classmethod
    def Microsoft_LifeCam_HD_3000_afocal(cls):
        return cls.from_database(cls._DATABASE['Microsoft_LifeCam_HD_3000_afocal'])
