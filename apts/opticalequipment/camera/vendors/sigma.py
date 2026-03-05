from ..base import Camera

class SigmaCamera(Camera):
    _DATABASE = {
        'Sigma_fp': {
            'brand': 'Sigma',
            'name': 'fp',
            'type': 'type_dslr',
            'optical_length': 20,
            'mass': 427,
            'tside_thread': 'Sony E',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 35.9,
            'sensor_height_mm': 23.9,
            'width': 6000,
            'height': 4000,
            'pixel_size_um': 5.97
        },
        'Sigma_fp_L': {
            'brand': 'Sigma',
            'name': 'fp L',
            'type': 'type_dslr',
            'optical_length': 20,
            'mass': 427,
            'tside_thread': 'Sony E',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 36.0,
            'sensor_height_mm': 24.0,
            'width': 9520,
            'height': 6328,
            'pixel_size_um': 3.76
        },
        'Sigma_sd_Quattro': {
            'brand': 'Sigma',
            'name': 'sd Quattro',
            'type': 'type_dslr',
            'optical_length': 20,
            'mass': 625,
            'tside_thread': 'Sony E',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 23.4,
            'sensor_height_mm': 15.5,
            'width': 5424,
            'height': 3616,
            'pixel_size_um': 4.31
        },
        'Sigma_sd_Quattro_H': {
            'brand': 'Sigma',
            'name': 'sd Quattro H',
            'type': 'type_dslr',
            'optical_length': 20,
            'mass': 625,
            'tside_thread': 'Sony E',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 26.7,
            'sensor_height_mm': 17.9,
            'width': 6200,
            'height': 4152,
            'pixel_size_um': 4.31
        }
    }

    @classmethod
    def Sigma_fp(cls):
        return cls.from_database(cls._DATABASE['Sigma_fp'])

    @classmethod
    def Sigma_fp_L(cls):
        return cls.from_database(cls._DATABASE['Sigma_fp_L'])

    @classmethod
    def Sigma_sd_Quattro(cls):
        return cls.from_database(cls._DATABASE['Sigma_sd_Quattro'])

    @classmethod
    def Sigma_sd_Quattro_H(cls):
        return cls.from_database(cls._DATABASE['Sigma_sd_Quattro_H'])