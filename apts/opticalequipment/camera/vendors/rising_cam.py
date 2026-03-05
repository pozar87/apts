from ..base import Camera

class Rising_camCamera(Camera):
    _DATABASE = {
        'Rising_Cam_IMX571_ATR': {
            'brand': 'Rising Cam',
            'name': 'IMX571 (ATR)',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 600,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 23.5,
            'sensor_height_mm': 15.7,
            'width': 6224,
            'height': 4168,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 81,
            'read_noise_e': 1.1,
            'full_well_e': 51000
        },
        'Rising_Cam_IMX533_ATR': {
            'brand': 'Rising Cam',
            'name': 'IMX533 (ATR)',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 400,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 11.31,
            'sensor_height_mm': 11.31,
            'width': 3008,
            'height': 3008,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 1.0,
            'full_well_e': 50000
        },
        'Rising_Cam_IMX294_ATR': {
            'brand': 'Rising Cam',
            'name': 'IMX294 (ATR)',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 500,
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
        'Rising_Cam_IMX585_ATR': {
            'brand': 'Rising Cam',
            'name': 'IMX585 (ATR)',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 200,
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
        'Rising_Cam_IMX_678C': {
            'brand': 'Rising Cam',
            'name': 'IMX 678C',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 200,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 7.68,
            'sensor_height_mm': 4.32,
            'width': 3840,
            'height': 2160,
            'pixel_size_um': 2.0,
            'quantum_efficiency_pct': 83,
            'read_noise_e': 0.6,
            'full_well_e': 10000
        },
        'Rising_Cam_IMX_462MC': {
            'brand': 'Rising Cam',
            'name': 'IMX 462MC',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 150,
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
        'Rising_Cam_IMX_174MM': {
            'brand': 'Rising Cam',
            'name': 'IMX 174MM',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 180,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 11.3,
            'sensor_height_mm': 7.1,
            'width': 1936,
            'height': 1216,
            'pixel_size_um': 5.86,
            'quantum_efficiency_pct': 77,
            'read_noise_e': 6.0,
            'full_well_e': 32000
        },
        'Rising_Cam_IMX_290MM': {
            'brand': 'Rising Cam',
            'name': 'IMX 290MM',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 170,
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
        'Rising_Cam_IMX_290MC': {
            'brand': 'Rising Cam',
            'name': 'IMX 290MC',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 170,
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
        'Rising_Cam_IMX_120MM': {
            'brand': 'Rising Cam',
            'name': 'IMX 120MM',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 150,
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
        'Rising_Cam_IMX_482MC': {
            'brand': 'Rising Cam',
            'name': 'IMX 482MC',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 150,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 11.13,
            'sensor_height_mm': 6.26,
            'width': 1920,
            'height': 1080,
            'pixel_size_um': 5.8,
            'quantum_efficiency_pct': 85,
            'read_noise_e': 1.5,
            'full_well_e': 50000
        },
        'Rising_Cam_IMX_385MC': {
            'brand': 'Rising Cam',
            'name': 'IMX 385MC',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 150,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 7.3,
            'sensor_height_mm': 4.1,
            'width': 1936,
            'height': 1096,
            'pixel_size_um': 3.75,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 0.7,
            'full_well_e': 18700
        },
        'Rising_Cam_IMX_224MC': {
            'brand': 'Rising Cam',
            'name': 'IMX 224MC',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 150,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 4.8,
            'sensor_height_mm': 3.6,
            'width': 1304,
            'height': 976,
            'pixel_size_um': 3.75,
            'quantum_efficiency_pct': 75,
            'read_noise_e': 0.75,
            'full_well_e': 19000
        },
        'Rising_Cam_IMX_178MM': {
            'brand': 'Rising Cam',
            'name': 'IMX 178MM',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 150,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 7.4,
            'sensor_height_mm': 5.0,
            'width': 3072,
            'height': 2048,
            'pixel_size_um': 2.4,
            'quantum_efficiency_pct': 78,
            'read_noise_e': 1.4,
            'full_well_e': 15000
        },
        'Rising_Cam_IMX_178MC': {
            'brand': 'Rising Cam',
            'name': 'IMX 178MC',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 150,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 7.4,
            'sensor_height_mm': 5.0,
            'width': 3072,
            'height': 2048,
            'pixel_size_um': 2.4,
            'quantum_efficiency_pct': 78,
            'read_noise_e': 1.4,
            'full_well_e': 15000
        }
    }

    @classmethod
    def Rising_Cam_IMX571_ATR(cls):
        return cls.from_database(cls._DATABASE['Rising_Cam_IMX571_ATR'])

    @classmethod
    def Rising_Cam_IMX533_ATR(cls):
        return cls.from_database(cls._DATABASE['Rising_Cam_IMX533_ATR'])

    @classmethod
    def Rising_Cam_IMX294_ATR(cls):
        return cls.from_database(cls._DATABASE['Rising_Cam_IMX294_ATR'])

    @classmethod
    def Rising_Cam_IMX585_ATR(cls):
        return cls.from_database(cls._DATABASE['Rising_Cam_IMX585_ATR'])

    @classmethod
    def Rising_Cam_IMX_678C(cls):
        return cls.from_database(cls._DATABASE['Rising_Cam_IMX_678C'])

    @classmethod
    def Rising_Cam_IMX_462MC(cls):
        return cls.from_database(cls._DATABASE['Rising_Cam_IMX_462MC'])

    @classmethod
    def Rising_Cam_IMX_174MM(cls):
        return cls.from_database(cls._DATABASE['Rising_Cam_IMX_174MM'])

    @classmethod
    def Rising_Cam_IMX_290MM(cls):
        return cls.from_database(cls._DATABASE['Rising_Cam_IMX_290MM'])

    @classmethod
    def Rising_Cam_IMX_290MC(cls):
        return cls.from_database(cls._DATABASE['Rising_Cam_IMX_290MC'])

    @classmethod
    def Rising_Cam_IMX_120MM(cls):
        return cls.from_database(cls._DATABASE['Rising_Cam_IMX_120MM'])

    @classmethod
    def Rising_Cam_IMX_482MC(cls):
        return cls.from_database(cls._DATABASE['Rising_Cam_IMX_482MC'])

    @classmethod
    def Rising_Cam_IMX_385MC(cls):
        return cls.from_database(cls._DATABASE['Rising_Cam_IMX_385MC'])

    @classmethod
    def Rising_Cam_IMX_224MC(cls):
        return cls.from_database(cls._DATABASE['Rising_Cam_IMX_224MC'])

    @classmethod
    def Rising_Cam_IMX_178MM(cls):
        return cls.from_database(cls._DATABASE['Rising_Cam_IMX_178MM'])

    @classmethod
    def Rising_Cam_IMX_178MC(cls):
        return cls.from_database(cls._DATABASE['Rising_Cam_IMX_178MC'])