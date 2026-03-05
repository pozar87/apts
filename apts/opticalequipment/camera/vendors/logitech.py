from ..base import Camera

class LogitechCamera(Camera):
    _DATABASE = {
        'Logitech_C920_Webcam_afocal': {
            'brand': 'Logitech',
            'name': 'C920 Webcam (afocal)',
            'type': 'type_camera',
            'optical_length': 0,
            'mass': 162,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 4.8,
            'sensor_height_mm': 3.6,
            'width': 1920,
            'height': 1080,
            'pixel_size_um': 3.0
        },
        'Logitech_C930e_Webcam_afocal': {
            'brand': 'Logitech',
            'name': 'C930e Webcam (afocal)',
            'type': 'type_camera',
            'optical_length': 0,
            'mass': 175,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 4.8,
            'sensor_height_mm': 3.6,
            'width': 1920,
            'height': 1080,
            'pixel_size_um': 3.0
        }
    }

    @classmethod
    def Logitech_C920_Webcam_afocal(cls):
        return cls.from_database(cls._DATABASE['Logitech_C920_Webcam_afocal'])

    @classmethod
    def Logitech_C930e_Webcam_afocal(cls):
        return cls.from_database(cls._DATABASE['Logitech_C930e_Webcam_afocal'])
