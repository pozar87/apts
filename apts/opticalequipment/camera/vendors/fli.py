from ..base import Camera

class FliCamera(Camera):
    _DATABASE = {
        'FLI_ML16200': {
            'brand': 'FLI',
            'name': 'ML16200',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 1500,
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
        'FLI_Kepler_KL400': {
            'brand': 'FLI',
            'name': 'Kepler KL400',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 1200,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 22.5,
            'sensor_height_mm': 22.5,
            'width': 2048,
            'height': 2048,
            'pixel_size_um': 11.0,
            'quantum_efficiency_pct': 95,
            'read_noise_e': 1.5,
            'full_well_e': 100000
        },
        'FLI_ProLine_16803': {
            'brand': 'FLI',
            'name': 'ProLine 16803',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 1800,
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
            'quantum_efficiency_pct': 60,
            'read_noise_e': 8.0,
            'full_well_e': 100000
        },
        'FLI_ML50100': {
            'brand': 'FLI',
            'name': 'ML50100',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 2000,
            'tside_thread': 'M68',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 49.1,
            'sensor_height_mm': 36.8,
            'width': 8176,
            'height': 6132,
            'pixel_size_um': 6.0,
            'quantum_efficiency_pct': 65,
            'read_noise_e': 7.0,
            'full_well_e': 40000
        },
        'FLI_Kepler_KL4040': {
            'brand': 'FLI',
            'name': 'Kepler KL4040',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 1500,
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
        'FLI_ML8300': {
            'brand': 'FLI',
            'name': 'ML8300',
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
            'read_noise_e': 7.0,
            'full_well_e': 25500
        },
        'FLI_ProLine_PL09000': {
            'brand': 'FLI',
            'name': 'ProLine PL09000',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 1500,
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
        'FLI_ProLine_PL4710': {
            'brand': 'FLI',
            'name': 'ProLine PL4710',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 1000,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 13.3,
            'sensor_height_mm': 13.3,
            'width': 1024,
            'height': 1024,
            'pixel_size_um': 13.0,
            'quantum_efficiency_pct': 95,
            'read_noise_e': 3.0,
            'full_well_e': 100000
        },
        'FLI_ProLine_PL11002': {
            'brand': 'FLI',
            'name': 'ProLine PL11002',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 1500,
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
        'FLI_Kepler_KL4040M': {
            'brand': 'FLI',
            'name': 'Kepler KL4040M',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 1500,
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
        'FLI_Kepler_KL16070': {
            'brand': 'FLI',
            'name': 'Kepler KL16070',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 1500,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 27.7,
            'sensor_height_mm': 18.5,
            'width': 4864,
            'height': 3232,
            'pixel_size_um': 5.7,
            'quantum_efficiency_pct': 50,
            'read_noise_e': 10.0,
            'full_well_e': 40000
        },
        'FLI_MicroLine_ML4710': {
            'brand': 'FLI',
            'name': 'MicroLine ML4710',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 1000,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 13.3,
            'sensor_height_mm': 13.3,
            'width': 1024,
            'height': 1024,
            'pixel_size_um': 13.0,
            'quantum_efficiency_pct': 95,
            'read_noise_e': 3.0,
            'full_well_e': 100000
        },
        'FLI_MicroLine_ML1109': {
            'brand': 'FLI',
            'name': 'MicroLine ML1109',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 1000,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 12.3,
            'sensor_height_mm': 12.3,
            'width': 1024,
            'height': 1024,
            'pixel_size_um': 12.0,
            'quantum_efficiency_pct': 65,
            'read_noise_e': 8.0,
            'full_well_e': 100000
        },
        'FLI_MicroLine_ML29050': {
            'brand': 'FLI',
            'name': 'MicroLine ML29050',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 1200,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 36.17,
            'sensor_height_mm': 24.11,
            'width': 6576,
            'height': 4384,
            'pixel_size_um': 5.5,
            'quantum_efficiency_pct': 50,
            'read_noise_e': 10.0,
            'full_well_e': 20000
        },
        'FLI_ML16070': {
            'brand': 'FLI',
            'name': 'ML16070',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 1200,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 27.7,
            'sensor_height_mm': 18.5,
            'width': 4864,
            'height': 3232,
            'pixel_size_um': 5.7,
            'quantum_efficiency_pct': 50,
            'read_noise_e': 10.0,
            'full_well_e': 40000
        },
        'FLI_ML8050': {
            'brand': 'FLI',
            'name': 'ML8050',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 1000,
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
        'FLI_ML4710': {
            'brand': 'FLI',
            'name': 'ML4710',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 1000,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 13.3,
            'sensor_height_mm': 13.3,
            'width': 1024,
            'height': 1024,
            'pixel_size_um': 13.0,
            'quantum_efficiency_pct': 95,
            'read_noise_e': 3.0,
            'full_well_e': 100000
        },
        'FLI_ProLine_PL16803': {
            'brand': 'FLI',
            'name': 'ProLine PL16803',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 1800,
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
            'quantum_efficiency_pct': 60,
            'read_noise_e': 8.0,
            'full_well_e': 100000
        },
        'FLI_Kepler_KL4040_FG': {
            'brand': 'FLI',
            'name': 'Kepler KL4040 FG',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 1500,
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
        }
    }

    @classmethod
    def FLI_ML16200(cls):
        return cls.from_database(cls._DATABASE['FLI_ML16200'])

    @classmethod
    def FLI_Kepler_KL400(cls):
        return cls.from_database(cls._DATABASE['FLI_Kepler_KL400'])

    @classmethod
    def FLI_ProLine_16803(cls):
        return cls.from_database(cls._DATABASE['FLI_ProLine_16803'])

    @classmethod
    def FLI_ML50100(cls):
        return cls.from_database(cls._DATABASE['FLI_ML50100'])

    @classmethod
    def FLI_Kepler_KL4040(cls):
        return cls.from_database(cls._DATABASE['FLI_Kepler_KL4040'])

    @classmethod
    def FLI_ML8300(cls):
        return cls.from_database(cls._DATABASE['FLI_ML8300'])

    @classmethod
    def FLI_ProLine_PL09000(cls):
        return cls.from_database(cls._DATABASE['FLI_ProLine_PL09000'])

    @classmethod
    def FLI_ProLine_PL4710(cls):
        return cls.from_database(cls._DATABASE['FLI_ProLine_PL4710'])

    @classmethod
    def FLI_ProLine_PL11002(cls):
        return cls.from_database(cls._DATABASE['FLI_ProLine_PL11002'])

    @classmethod
    def FLI_Kepler_KL4040M(cls):
        return cls.from_database(cls._DATABASE['FLI_Kepler_KL4040M'])

    @classmethod
    def FLI_Kepler_KL16070(cls):
        return cls.from_database(cls._DATABASE['FLI_Kepler_KL16070'])

    @classmethod
    def FLI_MicroLine_ML4710(cls):
        return cls.from_database(cls._DATABASE['FLI_MicroLine_ML4710'])

    @classmethod
    def FLI_MicroLine_ML1109(cls):
        return cls.from_database(cls._DATABASE['FLI_MicroLine_ML1109'])

    @classmethod
    def FLI_MicroLine_ML29050(cls):
        return cls.from_database(cls._DATABASE['FLI_MicroLine_ML29050'])

    @classmethod
    def FLI_ML16070(cls):
        return cls.from_database(cls._DATABASE['FLI_ML16070'])

    @classmethod
    def FLI_ML8050(cls):
        return cls.from_database(cls._DATABASE['FLI_ML8050'])

    @classmethod
    def FLI_ML4710(cls):
        return cls.from_database(cls._DATABASE['FLI_ML4710'])

    @classmethod
    def FLI_ProLine_PL16803(cls):
        return cls.from_database(cls._DATABASE['FLI_ProLine_PL16803'])

    @classmethod
    def FLI_Kepler_KL4040_FG(cls):
        return cls.from_database(cls._DATABASE['FLI_Kepler_KL4040_FG'])
