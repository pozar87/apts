from ..base import Camera

class SvbonyCamera(Camera):
    _DATABASE = {
        'SVBony_SV305': {
            'brand': 'SVBony',
            'name': 'SV305',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 80,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 5.6,
            'sensor_height_mm': 3.2,
            'width': 1936,
            'height': 1096,
            'pixel_size_um': 2.9,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 1.0,
            'full_well_e': 14600
        },
        'SVBony_SV305M_Pro': {
            'brand': 'SVBony',
            'name': 'SV305M Pro',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 80,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 5.6,
            'sensor_height_mm': 3.2,
            'width': 1936,
            'height': 1096,
            'pixel_size_um': 2.9,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 1.0,
            'full_well_e': 14600
        },
        'SVBony_SV305C_Pro': {
            'brand': 'SVBony',
            'name': 'SV305C Pro',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 80,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 5.6,
            'sensor_height_mm': 3.2,
            'width': 1936,
            'height': 1096,
            'pixel_size_um': 2.9,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 1.0,
            'full_well_e': 14600
        },
        'SVBony_SV205': {
            'brand': 'SVBony',
            'name': 'SV205',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 70,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 5.7,
            'sensor_height_mm': 4.3,
            'width': 3264,
            'height': 2448,
            'pixel_size_um': 1.4,
            'quantum_efficiency_pct': 50,
            'read_noise_e': 2.0,
            'full_well_e': 5000
        },
        'SVBony_SV405CC': {
            'brand': 'SVBony',
            'name': 'SV405CC',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 400,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 19.1,
            'sensor_height_mm': 13.0,
            'width': 4144,
            'height': 2822,
            'pixel_size_um': 4.63,
            'quantum_efficiency_pct': 75,
            'read_noise_e': 1.2,
            'full_well_e': 63700
        },
        'SVBony_SV505C': {
            'brand': 'SVBony',
            'name': 'SV505C',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 300,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 11.13,
            'sensor_height_mm': 6.26,
            'width': 3840,
            'height': 2160,
            'pixel_size_um': 2.9,
            'quantum_efficiency_pct': 91,
            'read_noise_e': 0.6,
            'full_well_e': 40000
        },
        'SVBony_SV605CC': {
            'brand': 'SVBony',
            'name': 'SV605CC',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 500,
            'tside_thread': 'M42',
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
        'SVBony_SV705C': {
            'brand': 'SVBony',
            'name': 'SV705C',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 450,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 11.13,
            'sensor_height_mm': 6.26,
            'width': 3840,
            'height': 2160,
            'pixel_size_um': 2.9,
            'quantum_efficiency_pct': 91,
            'read_noise_e': 0.6,
            'full_well_e': 40000
        },
        'SVBony_SV905C': {
            'brand': 'SVBony',
            'name': 'SV905C',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 80,
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
        },
        'SVBony_SV305_Pro': {
            'brand': 'SVBony',
            'name': 'SV305 Pro',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 80,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 5.6,
            'sensor_height_mm': 3.2,
            'width': 1936,
            'height': 1096,
            'pixel_size_um': 2.9,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 1.0,
            'full_well_e': 14600
        },
        'SVBony_SV105': {
            'brand': 'SVBony',
            'name': 'SV105',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 70,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 4.5,
            'sensor_height_mm': 3.4,
            'width': 1920,
            'height': 1080,
            'pixel_size_um': 2.8,
            'quantum_efficiency_pct': 50,
            'read_noise_e': 5.0,
            'full_well_e': 10000
        },
        'SVBony_SV205C': {
            'brand': 'SVBony',
            'name': 'SV205C',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 70,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 5.7,
            'sensor_height_mm': 4.3,
            'width': 3264,
            'height': 2448,
            'pixel_size_um': 1.4,
            'quantum_efficiency_pct': 50,
            'read_noise_e': 2.0,
            'full_well_e': 5000
        },
        'SVBony_SV305M_II': {
            'brand': 'SVBony',
            'name': 'SV305M II',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 80,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 5.6,
            'sensor_height_mm': 3.2,
            'width': 1936,
            'height': 1096,
            'pixel_size_um': 2.9,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 1.0,
            'full_well_e': 14600
        },
        'SVBony_SV405CC_Pro': {
            'brand': 'SVBony',
            'name': 'SV405CC Pro',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 450,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 19.1,
            'sensor_height_mm': 13.0,
            'width': 4144,
            'height': 2822,
            'pixel_size_um': 4.63,
            'quantum_efficiency_pct': 75,
            'read_noise_e': 1.2,
            'full_well_e': 63700
        },
        'SVBony_SV505C_Pro': {
            'brand': 'SVBony',
            'name': 'SV505C Pro',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 350,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 11.13,
            'sensor_height_mm': 6.26,
            'width': 3840,
            'height': 2160,
            'pixel_size_um': 2.9,
            'quantum_efficiency_pct': 91,
            'read_noise_e': 0.6,
            'full_well_e': 40000
        },
        'SVBony_SV605CC_Pro': {
            'brand': 'SVBony',
            'name': 'SV605CC Pro',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 550,
            'tside_thread': 'M42',
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
        'SVBony_SV805C': {
            'brand': 'SVBony',
            'name': 'SV805C',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 100,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 5.6,
            'sensor_height_mm': 3.2,
            'width': 1920,
            'height': 1080,
            'pixel_size_um': 2.9,
            'quantum_efficiency_pct': 91,
            'read_noise_e': 0.5,
            'full_well_e': 12000
        },
        'SVBony_SV130': {
            'brand': 'SVBony',
            'name': 'SV130',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 100,
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
            'quantum_efficiency_pct': 50,
            'read_noise_e': 5.0,
            'full_well_e': 13000
        },
        'SVBony_SV135M': {
            'brand': 'SVBony',
            'name': 'SV135M',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 100,
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
            'quantum_efficiency_pct': 50,
            'read_noise_e': 5.0,
            'full_well_e': 13000
        },
        'SVBony_SV305_II': {
            'brand': 'SVBony',
            'name': 'SV305 II',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 80,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 5.6,
            'sensor_height_mm': 3.2,
            'width': 1936,
            'height': 1096,
            'pixel_size_um': 2.9,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 1.0,
            'full_well_e': 14600
        },
        'SVBony_SV505M': {
            'brand': 'SVBony',
            'name': 'SV505M',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 300,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 11.13,
            'sensor_height_mm': 6.26,
            'width': 3840,
            'height': 2160,
            'pixel_size_um': 2.9,
            'quantum_efficiency_pct': 91,
            'read_noise_e': 0.6,
            'full_well_e': 40000
        },
        'SVBony_SV905M': {
            'brand': 'SVBony',
            'name': 'SV905M',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 80,
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
        },
        'SVBony_SV705M': {
            'brand': 'SVBony',
            'name': 'SV705M',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 450,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 11.13,
            'sensor_height_mm': 6.26,
            'width': 3840,
            'height': 2160,
            'pixel_size_um': 2.9,
            'quantum_efficiency_pct': 91,
            'read_noise_e': 0.6,
            'full_well_e': 40000
        },
        'SVBony_SV805M': {
            'brand': 'SVBony',
            'name': 'SV805M',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 100,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 5.6,
            'sensor_height_mm': 3.2,
            'width': 1920,
            'height': 1080,
            'pixel_size_um': 2.9,
            'quantum_efficiency_pct': 91,
            'read_noise_e': 0.5,
            'full_well_e': 12000
        },
        'SVBony_SV905CC': {
            'brand': 'SVBony',
            'name': 'SV905CC',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 450,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 11.13,
            'sensor_height_mm': 6.26,
            'width': 3840,
            'height': 2160,
            'pixel_size_um': 2.9,
            'quantum_efficiency_pct': 91,
            'read_noise_e': 0.6,
            'full_well_e': 40000
        },
        'SVBony_SV405CC_v2': {
            'brand': 'SVBony',
            'name': 'SV405CC v2',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 400,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 19.1,
            'sensor_height_mm': 13.0,
            'width': 4144,
            'height': 2822,
            'pixel_size_um': 4.63,
            'quantum_efficiency_pct': 75,
            'read_noise_e': 1.2,
            'full_well_e': 63700
        },
        'SVBony_SV505M_Pro': {
            'brand': 'SVBony',
            'name': 'SV505M Pro',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 350,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 11.13,
            'sensor_height_mm': 6.26,
            'width': 3840,
            'height': 2160,
            'pixel_size_um': 2.9,
            'quantum_efficiency_pct': 91,
            'read_noise_e': 0.6,
            'full_well_e': 40000
        },
        'SVBony_SV605CC_v2': {
            'brand': 'SVBony',
            'name': 'SV605CC v2',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 500,
            'tside_thread': 'M42',
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
        'SVBony_SV205M': {
            'brand': 'SVBony',
            'name': 'SV205M',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 70,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 5.7,
            'sensor_height_mm': 4.3,
            'width': 3264,
            'height': 2448,
            'pixel_size_um': 1.4,
            'quantum_efficiency_pct': 50,
            'read_noise_e': 2.0,
            'full_well_e': 5000
        },
        'SVBony_SV305M_Pro_v2': {
            'brand': 'SVBony',
            'name': 'SV305M Pro v2',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 80,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 5.6,
            'sensor_height_mm': 3.2,
            'width': 1936,
            'height': 1096,
            'pixel_size_um': 2.9,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 1.0,
            'full_well_e': 14600
        }
    }

    @classmethod
    def SVBony_SV305(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV305'])

    @classmethod
    def SVBony_SV305M_Pro(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV305M_Pro'])

    @classmethod
    def SVBony_SV305C_Pro(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV305C_Pro'])

    @classmethod
    def SVBony_SV205(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV205'])

    @classmethod
    def SVBony_SV405CC(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV405CC'])

    @classmethod
    def SVBony_SV505C(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV505C'])

    @classmethod
    def SVBony_SV605CC(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV605CC'])

    @classmethod
    def SVBony_SV705C(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV705C'])

    @classmethod
    def SVBony_SV905C(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV905C'])

    @classmethod
    def SVBony_SV305_Pro(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV305_Pro'])

    @classmethod
    def SVBony_SV105(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV105'])

    @classmethod
    def SVBony_SV205C(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV205C'])

    @classmethod
    def SVBony_SV305M_II(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV305M_II'])

    @classmethod
    def SVBony_SV405CC_Pro(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV405CC_Pro'])

    @classmethod
    def SVBony_SV505C_Pro(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV505C_Pro'])

    @classmethod
    def SVBony_SV605CC_Pro(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV605CC_Pro'])

    @classmethod
    def SVBony_SV805C(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV805C'])

    @classmethod
    def SVBony_SV130(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV130'])

    @classmethod
    def SVBony_SV135M(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV135M'])

    @classmethod
    def SVBony_SV305_II(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV305_II'])

    @classmethod
    def SVBony_SV505M(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV505M'])

    @classmethod
    def SVBony_SV905M(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV905M'])

    @classmethod
    def SVBony_SV705M(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV705M'])

    @classmethod
    def SVBony_SV805M(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV805M'])

    @classmethod
    def SVBony_SV905CC(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV905CC'])

    @classmethod
    def SVBony_SV405CC_v2(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV405CC_v2'])

    @classmethod
    def SVBony_SV505M_Pro(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV505M_Pro'])

    @classmethod
    def SVBony_SV605CC_v2(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV605CC_v2'])

    @classmethod
    def SVBony_SV205M(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV205M'])

    @classmethod
    def SVBony_SV305M_Pro_v2(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV305M_Pro_v2'])
