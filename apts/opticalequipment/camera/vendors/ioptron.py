from ..base import Camera

class IoptronCamera(Camera):
    _DATABASE = {
        'iOptron_iGuider_174M': {
            'brand': 'iOptron',
            'name': 'iGuider 174M',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 60,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 4.8,
            'sensor_height_mm': 3.6,
            'width': 1280,
            'height': 960,
            'pixel_size_um': 3.75,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 4.0,
            'full_well_e': 13000
        }
    }

    @classmethod
    def iOptron_iGuider_174M(cls):
        return cls.from_database(cls._DATABASE['iOptron_iGuider_174M'])
