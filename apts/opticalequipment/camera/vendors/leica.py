from ..base import Camera

class LeicaCamera(Camera):
    _DATABASE = {
        'Leica_SL2': {
            'brand': 'Leica',
            'name': 'SL2',
            'type': 'type_dslr',
            'optical_length': 20,
            'mass': 835,
            'tside_thread': 'Sony E',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 36.0,
            'sensor_height_mm': 24.0,
            'width': 8368,
            'height': 5584,
            'pixel_size_um': 4.3
        },
        'Leica_SL2_S': {
            'brand': 'Leica',
            'name': 'SL2-S',
            'type': 'type_dslr',
            'optical_length': 20,
            'mass': 850,
            'tside_thread': 'Sony E',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 36.0,
            'sensor_height_mm': 24.0,
            'width': 6072,
            'height': 4056,
            'pixel_size_um': 5.94
        },
        'Leica_M11': {
            'brand': 'Leica',
            'name': 'M11',
            'type': 'type_dslr',
            'optical_length': 20,
            'mass': 530,
            'tside_thread': 'Sony E',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 36.0,
            'sensor_height_mm': 24.0,
            'width': 9528,
            'height': 6328,
            'pixel_size_um': 3.76
        },
        'Leica_Q2': {
            'brand': 'Leica',
            'name': 'Q2',
            'type': 'type_dslr',
            'optical_length': 20,
            'mass': 718,
            'tside_thread': 'Sony E',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 36.0,
            'sensor_height_mm': 24.0,
            'width': 8368,
            'height': 5584,
            'pixel_size_um': 4.3
        },
        'Leica_CL': {
            'brand': 'Leica',
            'name': 'CL',
            'type': 'type_dslr',
            'optical_length': 20,
            'mass': 390,
            'tside_thread': 'Sony E',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 23.6,
            'sensor_height_mm': 15.7,
            'width': 6000,
            'height': 4000,
            'pixel_size_um': 3.92
        }
    }

    @classmethod
    def Leica_SL2(cls):
        return cls.from_database(cls._DATABASE['Leica_SL2'])

    @classmethod
    def Leica_SL2_S(cls):
        return cls.from_database(cls._DATABASE['Leica_SL2_S'])

    @classmethod
    def Leica_M11(cls):
        return cls.from_database(cls._DATABASE['Leica_M11'])

    @classmethod
    def Leica_Q2(cls):
        return cls.from_database(cls._DATABASE['Leica_Q2'])

    @classmethod
    def Leica_CL(cls):
        return cls.from_database(cls._DATABASE['Leica_CL'])
