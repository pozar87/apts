from ..base import Camera

class AtikCamera(Camera):
    _DATABASE = {
        'Atik_Horizon': {
            'brand': 'Atik',
            'name': 'Horizon',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 600,
            'tside_thread': 'M42',
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
        'Atik_383L': {
            'brand': 'Atik',
            'name': '383L+',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 550,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 17.96,
            'sensor_height_mm': 13.52,
            'width': 3362,
            'height': 2504,
            'pixel_size_um': 5.4,
            'quantum_efficiency_pct': 56,
            'read_noise_e': 7.0,
            'full_well_e': 25500
        },
        'Atik_460EX': {
            'brand': 'Atik',
            'name': '460EX',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 450,
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
            'read_noise_e': 5.0,
            'full_well_e': 18000
        },
        'Atik_ONE_6_0': {
            'brand': 'Atik',
            'name': 'ONE 6.0',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 800,
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
            'read_noise_e': 5.0,
            'full_well_e': 18000
        },
        'Atik_Infinity': {
            'brand': 'Atik',
            'name': 'Infinity',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 300,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 8.98,
            'sensor_height_mm': 6.71,
            'width': 1392,
            'height': 1040,
            'pixel_size_um': 6.45,
            'quantum_efficiency_pct': 77,
            'read_noise_e': 6.0,
            'full_well_e': 20000
        },
        'Atik_414EX': {
            'brand': 'Atik',
            'name': '414EX',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 400,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 8.98,
            'sensor_height_mm': 6.71,
            'width': 1392,
            'height': 1040,
            'pixel_size_um': 6.45,
            'quantum_efficiency_pct': 77,
            'read_noise_e': 6.0,
            'full_well_e': 20000
        },
        'Atik_490EX': {
            'brand': 'Atik',
            'name': '490EX',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 500,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 12.49,
            'sensor_height_mm': 9.99,
            'width': 3380,
            'height': 2704,
            'pixel_size_um': 3.69,
            'quantum_efficiency_pct': 77,
            'read_noise_e': 5.0,
            'full_well_e': 12000
        },
        'Atik_ONE_9_0': {
            'brand': 'Atik',
            'name': 'ONE 9.0',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 1000,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '', 'reversible': False, 'bf_role': 'end',
            'sensor_width_mm': 12.49,
            'sensor_height_mm': 9.99,
            'width': 3380,
            'height': 2704,
            'pixel_size_um': 3.69,
            'quantum_efficiency_pct': 77,
            'read_noise_e': 5.0,
            'full_well_e': 12000
        },
        'Atik_16200': {
            'brand': 'Atik',
            'name': '16200',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 1300,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 27.2,
            'sensor_height_mm': 21.8,
            'width': 4499,
            'height': 3599,
            'pixel_size_um': 6.0,
            'quantum_efficiency_pct': 60,
            'read_noise_e': 9.0,
            'full_well_e': 40000
        },
        'Atik_Horizon_II': {
            'brand': 'Atik',
            'name': 'Horizon II',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 600,
            'tside_thread': 'M42',
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
        'Atik_414EX_Mono': {
            'brand': 'Atik',
            'name': '414EX Mono',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 400,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 8.98,
            'sensor_height_mm': 6.71,
            'width': 1392,
            'height': 1040,
            'pixel_size_um': 6.45,
            'quantum_efficiency_pct': 77,
            'read_noise_e': 6.0,
            'full_well_e': 20000
        },
        'Atik_428EX': {
            'brand': 'Atik',
            'name': '428EX',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 400,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 6.7,
            'sensor_height_mm': 5.4,
            'width': 1940,
            'height': 1460,
            'pixel_size_um': 4.54,
            'quantum_efficiency_pct': 77,
            'read_noise_e': 5.0,
            'full_well_e': 18000
        },
        'Atik_450EX': {
            'brand': 'Atik',
            'name': '450EX',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 400,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 6.7,
            'sensor_height_mm': 5.4,
            'width': 2448,
            'height': 2050,
            'pixel_size_um': 3.45,
            'quantum_efficiency_pct': 77,
            'read_noise_e': 5.0,
            'full_well_e': 18000
        },
        'Atik_ONE_2_0': {
            'brand': 'Atik',
            'name': 'ONE 2.0',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 800,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 7.1,
            'sensor_height_mm': 5.4,
            'width': 1600,
            'height': 1200,
            'pixel_size_um': 4.4,
            'quantum_efficiency_pct': 55,
            'read_noise_e': 5.0,
            'full_well_e': 40000
        },
        'Atik_ACIS_7_1': {
            'brand': 'Atik',
            'name': 'ACIS 7.1',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 530,
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
        'Atik_ACIS_12_1': {
            'brand': 'Atik',
            'name': 'ACIS 12.3',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 530,
            'tside_thread': 'M42',
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
        'Atik_11000': {
            'brand': 'Atik',
            'name': '11000',
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
            'width': 4008,
            'height': 2672,
            'pixel_size_um': 9.0,
            'quantum_efficiency_pct': 50,
            'read_noise_e': 13.0,
            'full_well_e': 60000
        },
        'Atik_16HR': {
            'brand': 'Atik',
            'name': '16HR',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 450,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 8.98,
            'sensor_height_mm': 6.71,
            'width': 1392,
            'height': 1040,
            'pixel_size_um': 6.45,
            'quantum_efficiency_pct': 65,
            'read_noise_e': 4.0,
            'full_well_e': 20000
        },
        'Atik_320E': {
            'brand': 'Atik',
            'name': '320E',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 350,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 7.1,
            'sensor_height_mm': 5.4,
            'width': 1620,
            'height': 1220,
            'pixel_size_um': 4.4,
            'quantum_efficiency_pct': 55,
            'read_noise_e': 4.0,
            'full_well_e': 40000
        },
        'Atik_4000': {
            'brand': 'Atik',
            'name': '4000',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 1300,
            'tside_thread': 'M54',
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
        'Atik_Titan_Mono': {
            'brand': 'Atik',
            'name': 'Titan Mono',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 350,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 4.9,
            'sensor_height_mm': 3.6,
            'width': 659,
            'height': 494,
            'pixel_size_um': 7.4,
            'quantum_efficiency_pct': 65,
            'read_noise_e': 5.0,
            'full_well_e': 20000
        },
        'Atik_GP_CAM3_290M': {
            'brand': 'Atik',
            'name': 'GP-CAM3 290M',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 150,
            'tside_thread': 'M42',
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
        'Atik_GP_CAM2_290M': {
            'brand': 'Atik',
            'name': 'GP-CAM2 290M',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 150,
            'tside_thread': 'M42',
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
        'Atik_VS14': {
            'brand': 'Atik',
            'name': 'VS14',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 1300,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 13.1,
            'sensor_height_mm': 8.8,
            'width': 1392,
            'height': 1040,
            'pixel_size_um': 6.45,
            'quantum_efficiency_pct': 77,
            'read_noise_e': 6.0,
            'full_well_e': 20000
        },
        'Atik_Apx60': {
            'brand': 'Atik',
            'name': 'Apx60',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 1100,
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
        }
    }

    @classmethod
    def Atik_Horizon(cls):
        return cls.from_database(cls._DATABASE['Atik_Horizon'])

    @classmethod
    def Atik_383L(cls):
        return cls.from_database(cls._DATABASE['Atik_383L'])

    @classmethod
    def Atik_460EX(cls):
        return cls.from_database(cls._DATABASE['Atik_460EX'])

    @classmethod
    def Atik_ONE_6_0(cls):
        return cls.from_database(cls._DATABASE['Atik_ONE_6_0'])

    @classmethod
    def Atik_Infinity(cls):
        return cls.from_database(cls._DATABASE['Atik_Infinity'])

    @classmethod
    def Atik_414EX(cls):
        return cls.from_database(cls._DATABASE['Atik_414EX'])

    @classmethod
    def Atik_490EX(cls):
        return cls.from_database(cls._DATABASE['Atik_490EX'])

    @classmethod
    def Atik_ONE_9_0(cls):
        return cls.from_database(cls._DATABASE['Atik_ONE_9_0'])

    @classmethod
    def Atik_16200(cls):
        return cls.from_database(cls._DATABASE['Atik_16200'])

    @classmethod
    def Atik_Horizon_II(cls):
        return cls.from_database(cls._DATABASE['Atik_Horizon_II'])

    @classmethod
    def Atik_414EX_Mono(cls):
        return cls.from_database(cls._DATABASE['Atik_414EX_Mono'])

    @classmethod
    def Atik_428EX(cls):
        return cls.from_database(cls._DATABASE['Atik_428EX'])

    @classmethod
    def Atik_450EX(cls):
        return cls.from_database(cls._DATABASE['Atik_450EX'])

    @classmethod
    def Atik_ONE_2_0(cls):
        return cls.from_database(cls._DATABASE['Atik_ONE_2_0'])

    @classmethod
    def Atik_ACIS_7_1(cls):
        return cls.from_database(cls._DATABASE['Atik_ACIS_7_1'])

    @classmethod
    def Atik_ACIS_12_1(cls):
        return cls.from_database(cls._DATABASE['Atik_ACIS_12_1'])

    @classmethod
    def Atik_11000(cls):
        return cls.from_database(cls._DATABASE['Atik_11000'])

    @classmethod
    def Atik_16HR(cls):
        return cls.from_database(cls._DATABASE['Atik_16HR'])

    @classmethod
    def Atik_320E(cls):
        return cls.from_database(cls._DATABASE['Atik_320E'])

    @classmethod
    def Atik_4000(cls):
        return cls.from_database(cls._DATABASE['Atik_4000'])

    @classmethod
    def Atik_Titan_Mono(cls):
        return cls.from_database(cls._DATABASE['Atik_Titan_Mono'])

    @classmethod
    def Atik_GP_CAM3_290M(cls):
        return cls.from_database(cls._DATABASE['Atik_GP_CAM3_290M'])

    @classmethod
    def Atik_GP_CAM2_290M(cls):
        return cls.from_database(cls._DATABASE['Atik_GP_CAM2_290M'])

    @classmethod
    def Atik_VS14(cls):
        return cls.from_database(cls._DATABASE['Atik_VS14'])

    @classmethod
    def Atik_Apx60(cls):
        return cls.from_database(cls._DATABASE['Atik_Apx60'])
