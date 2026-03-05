from ..base import Camera

class PentaxCamera(Camera):
    _DATABASE = {
        'Pentax_K_1_II': {
            'brand': 'Pentax',
            'name': 'K-1 II',
            'type': 'type_dslr',
            'optical_length': 45.5,
            'mass': 1010,
            'tside_thread': 'Pentax K',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 35.9,
            'sensor_height_mm': 24.0,
            'width': 7360,
            'height': 4912,
            'pixel_size_um': 4.88
        },
        'Pentax_K_1': {
            'brand': 'Pentax',
            'name': 'K-1',
            'type': 'type_dslr',
            'optical_length': 45.5,
            'mass': 1010,
            'tside_thread': 'Pentax K',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 35.9,
            'sensor_height_mm': 24.0,
            'width': 7360,
            'height': 4912,
            'pixel_size_um': 4.88
        },
        'Pentax_K_3_III': {
            'brand': 'Pentax',
            'name': 'K-3 III',
            'type': 'type_dslr',
            'optical_length': 45.5,
            'mass': 820,
            'tside_thread': 'Pentax K',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 23.3,
            'sensor_height_mm': 15.5,
            'width': 6192,
            'height': 4128,
            'pixel_size_um': 3.76
        },
        'Pentax_KP': {
            'brand': 'Pentax',
            'name': 'KP',
            'type': 'type_dslr',
            'optical_length': 45.5,
            'mass': 703,
            'tside_thread': 'Pentax K',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 23.5,
            'sensor_height_mm': 15.6,
            'width': 6016,
            'height': 4016,
            'pixel_size_um': 3.91
        },
        'Pentax_K_70': {
            'brand': 'Pentax',
            'name': 'K-70',
            'type': 'type_dslr',
            'optical_length': 45.5,
            'mass': 688,
            'tside_thread': 'Pentax K',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 23.5,
            'sensor_height_mm': 15.6,
            'width': 6000,
            'height': 4000,
            'pixel_size_um': 3.92
        }
    }

    @classmethod
    def Pentax_K_1_II(cls):
        return cls.from_database(cls._DATABASE['Pentax_K_1_II'])

    @classmethod
    def Pentax_K_1(cls):
        return cls.from_database(cls._DATABASE['Pentax_K_1'])

    @classmethod
    def Pentax_K_3_III(cls):
        return cls.from_database(cls._DATABASE['Pentax_K_3_III'])

    @classmethod
    def Pentax_KP(cls):
        return cls.from_database(cls._DATABASE['Pentax_KP'])

    @classmethod
    def Pentax_K_70(cls):
        return cls.from_database(cls._DATABASE['Pentax_K_70'])
