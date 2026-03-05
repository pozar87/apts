from ..base import Camera

class InovaCamera(Camera):
    _DATABASE = {
        'iNova_PLB_Cx2_178C': {
            'brand': 'iNova',
            'name': 'PLB-Cx2 178C',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 80,
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
        'iNova_PLB_Cx2_290C': {
            'brand': 'iNova',
            'name': 'PLB-Cx2 290C',
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
        'iNova_PLB_Cx2_462C': {
            'brand': 'iNova',
            'name': 'PLB-Cx2 462C',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 85,
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
        'iNova_PLB_Cx2_585C': {
            'brand': 'iNova',
            'name': 'PLB-Cx2 585C',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 90,
            'tside_thread': 'CS',
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
        'iNova_PLB_Mx2_IMX290': {
            'brand': 'iNova',
            'name': 'PLB-Mx2 (IMX290)',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 180,
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
        'iNova_PLB_Cx2_IMX290': {
            'brand': 'iNova',
            'name': 'PLB-Cx2 (IMX290)',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 180,
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
        'iNova_PLB_Mx2_IMX178': {
            'brand': 'iNova',
            'name': 'PLB-Mx2 (IMX178)',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 160,
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
        'iNova_PLB_Cx2_IMX178': {
            'brand': 'iNova',
            'name': 'PLB-Cx2 (IMX178)',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 160,
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
    def iNova_PLB_Cx2_178C(cls):
        return cls.from_database(cls._DATABASE['iNova_PLB_Cx2_178C'])

    @classmethod
    def iNova_PLB_Cx2_290C(cls):
        return cls.from_database(cls._DATABASE['iNova_PLB_Cx2_290C'])

    @classmethod
    def iNova_PLB_Cx2_462C(cls):
        return cls.from_database(cls._DATABASE['iNova_PLB_Cx2_462C'])

    @classmethod
    def iNova_PLB_Cx2_585C(cls):
        return cls.from_database(cls._DATABASE['iNova_PLB_Cx2_585C'])

    @classmethod
    def iNova_PLB_Mx2_IMX290(cls):
        return cls.from_database(cls._DATABASE['iNova_PLB_Mx2_IMX290'])

    @classmethod
    def iNova_PLB_Cx2_IMX290(cls):
        return cls.from_database(cls._DATABASE['iNova_PLB_Cx2_IMX290'])

    @classmethod
    def iNova_PLB_Mx2_IMX178(cls):
        return cls.from_database(cls._DATABASE['iNova_PLB_Mx2_IMX178'])

    @classmethod
    def iNova_PLB_Cx2_IMX178(cls):
        return cls.from_database(cls._DATABASE['iNova_PLB_Cx2_IMX178'])
