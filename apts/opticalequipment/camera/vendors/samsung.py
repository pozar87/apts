from ..base import Camera

class SamsungCamera(Camera):
    _DATABASE = {
        'Samsung_NX1': {
            'brand': 'Samsung',
            'name': 'NX1',
            'type': 'type_dslr',
            'optical_length': 25.5,
            'mass': 550,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 23.5,
            'sensor_height_mm': 15.7,
            'width': 6480,
            'height': 4320,
            'pixel_size_um': 3.63
        },
        'Samsung_NX500': {
            'brand': 'Samsung',
            'name': 'NX500',
            'type': 'type_dslr',
            'optical_length': 25.5,
            'mass': 292,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 23.5,
            'sensor_height_mm': 15.7,
            'width': 6480,
            'height': 4320,
            'pixel_size_um': 3.63
        },
        'Samsung_NX300': {
            'brand': 'Samsung',
            'name': 'NX300',
            'type': 'type_dslr',
            'optical_length': 25.5,
            'mass': 284,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 23.5,
            'sensor_height_mm': 15.7,
            'width': 5472,
            'height': 3648,
            'pixel_size_um': 4.3
        },
        'Samsung_NX3000': {
            'brand': 'Samsung',
            'name': 'NX3000',
            'type': 'type_dslr',
            'optical_length': 25.5,
            'mass': 250,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 23.5,
            'sensor_height_mm': 15.7,
            'width': 5472,
            'height': 3648,
            'pixel_size_um': 4.3
        }
    }

    @classmethod
    def Samsung_NX1(cls):
        return cls.from_database(cls._DATABASE['Samsung_NX1'])

    @classmethod
    def Samsung_NX500(cls):
        return cls.from_database(cls._DATABASE['Samsung_NX500'])

    @classmethod
    def Samsung_NX300(cls):
        return cls.from_database(cls._DATABASE['Samsung_NX300'])

    @classmethod
    def Samsung_NX3000(cls):
        return cls.from_database(cls._DATABASE['Samsung_NX3000'])
