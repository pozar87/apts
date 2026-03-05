from ..base import Camera

class MoravianCamera(Camera):
    _DATABASE = {
        'Moravian_C3_61000_Pro': {
            'brand': 'Moravian',
            'name': 'C3-61000 Pro',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 1200,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 36.0,
            'sensor_height_mm': 24.0,
            'width': 9576,
            'height': 6388,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 1.2,
            'full_well_e': 51000
        },
        'Moravian_C1_12000': {
            'brand': 'Moravian',
            'name': 'C1-12000',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 600,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 14.2,
            'sensor_height_mm': 10.4,
            'width': 4112,
            'height': 3008,
            'pixel_size_um': 3.45,
            'quantum_efficiency_pct': 70,
            'read_noise_e': 2.2,
            'full_well_e': 10500
        },
        'Moravian_C4_16000': {
            'brand': 'Moravian',
            'name': 'C4-16000',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 900,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 36.86,
            'sensor_height_mm': 36.86,
            'width': 4096,
            'height': 4096,
            'pixel_size_um': 9.0,
            'quantum_efficiency_pct': 74,
            'read_noise_e': 3.7,
            'full_well_e': 70000
        },
        'Moravian_C3_26000_Pro': {
            'brand': 'Moravian',
            'name': 'C3-26000 Pro',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 1000,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 23.5,
            'sensor_height_mm': 15.7,
            'width': 6248,
            'height': 4176,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 81,
            'read_noise_e': 1.1,
            'full_well_e': 51000
        },
        'Moravian_C1_5000': {
            'brand': 'Moravian',
            'name': 'C1-5000',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 500,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 8.4,
            'sensor_height_mm': 7.1,
            'width': 2448,
            'height': 2048,
            'pixel_size_um': 3.45,
            'quantum_efficiency_pct': 70,
            'read_noise_e': 2.2,
            'full_well_e': 10500
        },
        'Moravian_C5_100000': {
            'brand': 'Moravian',
            'name': 'C5-100000',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 1500,
            'tside_thread': 'M68',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 54.0,
            'sensor_height_mm': 40.0,
            'width': 11656,
            'height': 8742,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 1.5,
            'full_well_e': 50000
        },
        'Moravian_C3_12000_Pro': {
            'brand': 'Moravian',
            'name': 'C3-12000 Pro',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 800,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 14.1,
            'sensor_height_mm': 10.3,
            'width': 4096,
            'height': 3000,
            'pixel_size_um': 3.45,
            'quantum_efficiency_pct': 78,
            'read_noise_e': 3.0,
            'full_well_e': 30000
        },
        'Moravian_C2_3000': {
            'brand': 'Moravian',
            'name': 'C2-3000',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 400,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 7.1,
            'sensor_height_mm': 5.4,
            'width': 2048,
            'height': 1536,
            'pixel_size_um': 3.45,
            'quantum_efficiency_pct': 75,
            'read_noise_e': 2.0,
            'full_well_e': 15000
        },
        'Moravian_C3_16000_Pro': {
            'brand': 'Moravian',
            'name': 'C3-16000 Pro',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 1000,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 17.7,
            'sensor_height_mm': 13.4,
            'width': 4656,
            'height': 3520,
            'pixel_size_um': 3.8,
            'quantum_efficiency_pct': 60,
            'read_noise_e': 1.2,
            'full_well_e': 20000
        },
        'Moravian_C4_9000': {
            'brand': 'Moravian',
            'name': 'C4-9000',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 1200,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 36.67,
            'sensor_height_mm': 36.67,
            'width': 3056,
            'height': 3056,
            'pixel_size_um': 12.0,
            'quantum_efficiency_pct': 65,
            'read_noise_e': 10.0,
            'full_well_e': 110000
        },
        'Moravian_C1_3000': {
            'brand': 'Moravian',
            'name': 'C1-3000',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 500,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 7.1,
            'sensor_height_mm': 5.4,
            'width': 2048,
            'height': 1536,
            'pixel_size_um': 3.45,
            'quantum_efficiency_pct': 75,
            'read_noise_e': 2.0,
            'full_well_e': 15000
        },
        'Moravian_C1x_61000': {
            'brand': 'Moravian',
            'name': 'C1x-61000',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 800,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 36.0,
            'sensor_height_mm': 24.0,
            'width': 9576,
            'height': 6388,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 1.2,
            'full_well_e': 51000
        },
        'Moravian_C1x_26000': {
            'brand': 'Moravian',
            'name': 'C1x-26000',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 700,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 23.5,
            'sensor_height_mm': 15.7,
            'width': 6248,
            'height': 4176,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 81,
            'read_noise_e': 1.1,
            'full_well_e': 51000
        },
        'Moravian_C1_5500': {
            'brand': 'Moravian',
            'name': 'C1-5500',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 500,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 12.5,
            'sensor_height_mm': 10.0,
            'width': 2750,
            'height': 2200,
            'pixel_size_um': 4.54,
            'quantum_efficiency_pct': 77,
            'read_noise_e': 5.0,
            'full_well_e': 18000
        },
        'Moravian_C2_7000': {
            'brand': 'Moravian',
            'name': 'C2-7000',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 600,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 13.3,
            'sensor_height_mm': 13.3,
            'width': 3008,
            'height': 3008,
            'pixel_size_um': 4.5,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 3.0,
            'full_well_e': 50000
        },
        'Moravian_C3_61000_Pro_v2': {
            'brand': 'Moravian',
            'name': 'C3-61000 Pro v2',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 1200,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 36.0,
            'sensor_height_mm': 24.0,
            'width': 9576,
            'height': 6388,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 1.2,
            'full_well_e': 51000
        },
        'Moravian_C4_20000': {
            'brand': 'Moravian',
            'name': 'C4-20000',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 1300,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 36.0,
            'sensor_height_mm': 24.0,
            'width': 5472,
            'height': 3648,
            'pixel_size_um': 6.5,
            'quantum_efficiency_pct': 60,
            'read_noise_e': 8.0,
            'full_well_e': 40000
        },
        'Moravian_C5_100000_v2': {
            'brand': 'Moravian',
            'name': 'C5-100000 v2',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 1500,
            'tside_thread': 'M68',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 54.0,
            'sensor_height_mm': 40.0,
            'width': 11656,
            'height': 8742,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 1.5,
            'full_well_e': 50000
        }
    }

    @classmethod
    def Moravian_C3_61000_Pro(cls):
        return cls.from_database(cls._DATABASE['Moravian_C3_61000_Pro'])

    @classmethod
    def Moravian_C1_12000(cls):
        return cls.from_database(cls._DATABASE['Moravian_C1_12000'])

    @classmethod
    def Moravian_C4_16000(cls):
        return cls.from_database(cls._DATABASE['Moravian_C4_16000'])

    @classmethod
    def Moravian_C3_26000_Pro(cls):
        return cls.from_database(cls._DATABASE['Moravian_C3_26000_Pro'])

    @classmethod
    def Moravian_C1_5000(cls):
        return cls.from_database(cls._DATABASE['Moravian_C1_5000'])

    @classmethod
    def Moravian_C5_100000(cls):
        return cls.from_database(cls._DATABASE['Moravian_C5_100000'])

    @classmethod
    def Moravian_C3_12000_Pro(cls):
        return cls.from_database(cls._DATABASE['Moravian_C3_12000_Pro'])

    @classmethod
    def Moravian_C2_3000(cls):
        return cls.from_database(cls._DATABASE['Moravian_C2_3000'])

    @classmethod
    def Moravian_C3_16000_Pro(cls):
        return cls.from_database(cls._DATABASE['Moravian_C3_16000_Pro'])

    @classmethod
    def Moravian_C4_9000(cls):
        return cls.from_database(cls._DATABASE['Moravian_C4_9000'])

    @classmethod
    def Moravian_C1_3000(cls):
        return cls.from_database(cls._DATABASE['Moravian_C1_3000'])

    @classmethod
    def Moravian_C1x_61000(cls):
        return cls.from_database(cls._DATABASE['Moravian_C1x_61000'])

    @classmethod
    def Moravian_C1x_26000(cls):
        return cls.from_database(cls._DATABASE['Moravian_C1x_26000'])

    @classmethod
    def Moravian_C1_5500(cls):
        return cls.from_database(cls._DATABASE['Moravian_C1_5500'])

    @classmethod
    def Moravian_C2_7000(cls):
        return cls.from_database(cls._DATABASE['Moravian_C2_7000'])

    @classmethod
    def Moravian_C3_61000_Pro_v2(cls):
        return cls.from_database(cls._DATABASE['Moravian_C3_61000_Pro_v2'])

    @classmethod
    def Moravian_C4_20000(cls):
        return cls.from_database(cls._DATABASE['Moravian_C4_20000'])

    @classmethod
    def Moravian_C5_100000_v2(cls):
        return cls.from_database(cls._DATABASE['Moravian_C5_100000_v2'])
