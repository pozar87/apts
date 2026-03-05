from ..base import Camera

class SbigCamera(Camera):
    _DATABASE = {
        'SBIG_STF_8300M': {
            'brand': 'SBIG',
            'name': 'STF-8300M',
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
            'read_noise_e': 9.3,
            'full_well_e': 25500
        },
        'SBIG_STT_8300M': {
            'brand': 'SBIG',
            'name': 'STT-8300M',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 800,
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
            'read_noise_e': 9.0,
            'full_well_e': 25500
        },
        'SBIG_STX_16803': {
            'brand': 'SBIG',
            'name': 'STX-16803',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 1200,
            'tside_thread': 'M42',
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
            'quantum_efficiency_pct': 60,
            'read_noise_e': 8.0,
            'full_well_e': 100000
        },
        'SBIG_STXL_11002': {
            'brand': 'SBIG',
            'name': 'STXL-11002',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 1400,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 36.0,
            'sensor_height_mm': 24.0,
            'width': 4008,
            'height': 2672,
            'pixel_size_um': 9.0,
            'quantum_efficiency_pct': 50,
            'read_noise_e': 13.0,
            'full_well_e': 60000
        },
        'SBIG_STF_8050M': {
            'brand': 'SBIG',
            'name': 'STF-8050M',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 650,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 18.1,
            'sensor_height_mm': 13.6,
            'width': 3296,
            'height': 2472,
            'pixel_size_um': 5.5,
            'quantum_efficiency_pct': 50,
            'read_noise_e': 10.0,
            'full_well_e': 20000
        },
        'SBIG_STT_1603M': {
            'brand': 'SBIG',
            'name': 'STT-1603M',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 500,
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
            'quantum_efficiency_pct': 77,
            'read_noise_e': 15.0,
            'full_well_e': 100000
        },
        'SBIG_Aluma_AC694': {
            'brand': 'SBIG',
            'name': 'Aluma AC694',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 400,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 12.49,
            'sensor_height_mm': 9.99,
            'width': 2750,
            'height': 2200,
            'pixel_size_um': 4.54,
            'quantum_efficiency_pct': 77,
            'read_noise_e': 4.5,
            'full_well_e': 18000
        },
        'SBIG_STT_1603ME': {
            'brand': 'SBIG',
            'name': 'STT-1603ME',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 550,
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
            'quantum_efficiency_pct': 77,
            'read_noise_e': 15.0,
            'full_well_e': 100000
        },
        'SBIG_STT_3200ME': {
            'brand': 'SBIG',
            'name': 'STT-3200ME',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 550,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 14.7,
            'sensor_height_mm': 10.2,
            'width': 2184,
            'height': 1472,
            'pixel_size_um': 6.8,
            'quantum_efficiency_pct': 85,
            'read_noise_e': 10.0,
            'full_well_e': 55000
        },
        'SBIG_ST_i': {
            'brand': 'SBIG',
            'name': 'ST-i',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 150,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 4.8,
            'sensor_height_mm': 3.6,
            'width': 648,
            'height': 484,
            'pixel_size_um': 7.4,
            'quantum_efficiency_pct': 55,
            'read_noise_e': 12.0,
            'full_well_e': 40000
        },
        'SBIG_ST_402ME': {
            'brand': 'SBIG',
            'name': 'ST-402ME',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 450,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 6.9,
            'sensor_height_mm': 4.6,
            'width': 765,
            'height': 510,
            'pixel_size_um': 9.0,
            'quantum_efficiency_pct': 85,
            'read_noise_e': 15.0,
            'full_well_e': 100000
        },
        'SBIG_ST_8300M': {
            'brand': 'SBIG',
            'name': 'ST-8300M',
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
            'read_noise_e': 9.3,
            'full_well_e': 25500
        },
        'SBIG_STF_4070M': {
            'brand': 'SBIG',
            'name': 'STF-4070M',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 650,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 15.15,
            'sensor_height_mm': 15.15,
            'width': 2048,
            'height': 2048,
            'pixel_size_um': 7.4,
            'quantum_efficiency_pct': 55,
            'read_noise_e': 11.0,
            'full_well_e': 40000
        },
        'SBIG_Aluma_AC4040': {
            'brand': 'SBIG',
            'name': 'Aluma AC4040',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 1200,
            'tside_thread': 'M42',
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
        'SBIG_Aluma_AC2020': {
            'brand': 'SBIG',
            'name': 'Aluma AC2020',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 1100,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 13.3,
            'sensor_height_mm': 13.3,
            'width': 2048,
            'height': 2048,
            'pixel_size_um': 6.5,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 2.0,
            'full_well_e': 50000
        },
        'SBIG_STF_8050': {
            'brand': 'SBIG',
            'name': 'STF-8050',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 650,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 18.1,
            'sensor_height_mm': 13.6,
            'width': 3296,
            'height': 2472,
            'pixel_size_um': 5.5,
            'quantum_efficiency_pct': 50,
            'read_noise_e': 10.0,
            'full_well_e': 20000
        },
        'SBIG_ST_10XME': {
            'brand': 'SBIG',
            'name': 'ST-10XME',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 800,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 14.9,
            'sensor_height_mm': 10.0,
            'width': 2184,
            'height': 1472,
            'pixel_size_um': 6.8,
            'quantum_efficiency_pct': 85,
            'read_noise_e': 10.0,
            'full_well_e': 77000
        },
        'SBIG_ST_8XME': {
            'brand': 'SBIG',
            'name': 'ST-8XME',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 800,
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
            'quantum_efficiency_pct': 85,
            'read_noise_e': 15.0,
            'full_well_e': 100000
        },
        'SBIG_ST_7XME': {
            'brand': 'SBIG',
            'name': 'ST-7XME',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 800,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 6.9,
            'sensor_height_mm': 4.6,
            'width': 765,
            'height': 510,
            'pixel_size_um': 9.0,
            'quantum_efficiency_pct': 85,
            'read_noise_e': 15.0,
            'full_well_e': 100000
        }
    }

    @classmethod
    def SBIG_STF_8300M(cls):
        return cls.from_database(cls._DATABASE['SBIG_STF_8300M'])

    @classmethod
    def SBIG_STT_8300M(cls):
        return cls.from_database(cls._DATABASE['SBIG_STT_8300M'])

    @classmethod
    def SBIG_STX_16803(cls):
        return cls.from_database(cls._DATABASE['SBIG_STX_16803'])

    @classmethod
    def SBIG_STXL_11002(cls):
        return cls.from_database(cls._DATABASE['SBIG_STXL_11002'])

    @classmethod
    def SBIG_STF_8050M(cls):
        return cls.from_database(cls._DATABASE['SBIG_STF_8050M'])

    @classmethod
    def SBIG_STT_1603M(cls):
        return cls.from_database(cls._DATABASE['SBIG_STT_1603M'])

    @classmethod
    def SBIG_Aluma_AC694(cls):
        return cls.from_database(cls._DATABASE['SBIG_Aluma_AC694'])

    @classmethod
    def SBIG_STT_1603ME(cls):
        return cls.from_database(cls._DATABASE['SBIG_STT_1603ME'])

    @classmethod
    def SBIG_STT_3200ME(cls):
        return cls.from_database(cls._DATABASE['SBIG_STT_3200ME'])

    @classmethod
    def SBIG_ST_i(cls):
        return cls.from_database(cls._DATABASE['SBIG_ST_i'])

    @classmethod
    def SBIG_ST_402ME(cls):
        return cls.from_database(cls._DATABASE['SBIG_ST_402ME'])

    @classmethod
    def SBIG_ST_8300M(cls):
        return cls.from_database(cls._DATABASE['SBIG_ST_8300M'])

    @classmethod
    def SBIG_STF_4070M(cls):
        return cls.from_database(cls._DATABASE['SBIG_STF_4070M'])

    @classmethod
    def SBIG_Aluma_AC4040(cls):
        return cls.from_database(cls._DATABASE['SBIG_Aluma_AC4040'])

    @classmethod
    def SBIG_Aluma_AC2020(cls):
        return cls.from_database(cls._DATABASE['SBIG_Aluma_AC2020'])

    @classmethod
    def SBIG_STF_8050(cls):
        return cls.from_database(cls._DATABASE['SBIG_STF_8050'])

    @classmethod
    def SBIG_ST_10XME(cls):
        return cls.from_database(cls._DATABASE['SBIG_ST_10XME'])

    @classmethod
    def SBIG_ST_8XME(cls):
        return cls.from_database(cls._DATABASE['SBIG_ST_8XME'])

    @classmethod
    def SBIG_ST_7XME(cls):
        return cls.from_database(cls._DATABASE['SBIG_ST_7XME'])