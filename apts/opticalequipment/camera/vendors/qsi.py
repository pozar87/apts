from ..base import Camera

class QsiCamera(Camera):
    _DATABASE = {
        'QSI_690ws': {
            'brand': 'QSI',
            'name': '690ws',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 800,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 12.48,
            'sensor_height_mm': 9.98,
            'width': 3388,
            'height': 2712,
            'pixel_size_um': 3.69,
            'quantum_efficiency_pct': 77,
            'read_noise_e': 4.0,
            'full_well_e': 18000
        },
        'QSI_690wsg': {
            'brand': 'QSI',
            'name': '690wsg',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 850,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 12.48,
            'sensor_height_mm': 9.98,
            'width': 3388,
            'height': 2712,
            'pixel_size_um': 3.69,
            'quantum_efficiency_pct': 77,
            'read_noise_e': 4.0,
            'full_well_e': 18000
        },
        'QSI_660ws': {
            'brand': 'QSI',
            'name': '660ws',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 700,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 12.48,
            'sensor_height_mm': 9.98,
            'width': 2750,
            'height': 2200,
            'pixel_size_um': 4.54,
            'quantum_efficiency_pct': 77,
            'read_noise_e': 4.0,
            'full_well_e': 18000
        },
        'QSI_660wsg': {
            'brand': 'QSI',
            'name': '660wsg',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 750,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 12.48,
            'sensor_height_mm': 9.98,
            'width': 2750,
            'height': 2200,
            'pixel_size_um': 4.54,
            'quantum_efficiency_pct': 77,
            'read_noise_e': 4.0,
            'full_well_e': 18000
        },
        'QSI_583ws': {
            'brand': 'QSI',
            'name': '583ws',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 600,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 17.96,
            'sensor_height_mm': 13.52,
            'width': 3326,
            'height': 2504,
            'pixel_size_um': 5.4,
            'quantum_efficiency_pct': 56,
            'read_noise_e': 8.0,
            'full_well_e': 25500
        },
        'QSI_583wsg': {
            'brand': 'QSI',
            'name': '583wsg',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 650,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 17.96,
            'sensor_height_mm': 13.52,
            'width': 3326,
            'height': 2504,
            'pixel_size_um': 5.4,
            'quantum_efficiency_pct': 56,
            'read_noise_e': 8.0,
            'full_well_e': 25500
        },
        'QSI_616ws': {
            'brand': 'QSI',
            'name': '616ws',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 700,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 13.8,
            'sensor_height_mm': 9.2,
            'width': 1536,
            'height': 1024,
            'pixel_size_um': 9.0,
            'quantum_efficiency_pct': 60,
            'read_noise_e': 10.0,
            'full_well_e': 100000
        }
    }

    @classmethod
    def QSI_690ws(cls):
        return cls.from_database(cls._DATABASE['QSI_690ws'])

    @classmethod
    def QSI_690wsg(cls):
        return cls.from_database(cls._DATABASE['QSI_690wsg'])

    @classmethod
    def QSI_660ws(cls):
        return cls.from_database(cls._DATABASE['QSI_660ws'])

    @classmethod
    def QSI_660wsg(cls):
        return cls.from_database(cls._DATABASE['QSI_660wsg'])

    @classmethod
    def QSI_583ws(cls):
        return cls.from_database(cls._DATABASE['QSI_583ws'])

    @classmethod
    def QSI_583wsg(cls):
        return cls.from_database(cls._DATABASE['QSI_583wsg'])

    @classmethod
    def QSI_616ws(cls):
        return cls.from_database(cls._DATABASE['QSI_616ws'])