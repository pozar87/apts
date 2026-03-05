from ..base import Camera

class Flir_point_greyCamera(Camera):
    _DATABASE = {
        'FLIR_Point_Grey_Chameleon3_USB3': {
            'brand': 'FLIR/Point Grey',
            'name': 'Chameleon3 USB3',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 200,
            'tside_thread': 'CS',
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
        'FLIR_Point_Grey_Grasshopper3_USB3': {
            'brand': 'FLIR/Point Grey',
            'name': 'Grasshopper3 USB3',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 350,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 11.3,
            'sensor_height_mm': 7.1,
            'width': 1920,
            'height': 1200,
            'pixel_size_um': 5.86,
            'quantum_efficiency_pct': 77,
            'read_noise_e': 6.0,
            'full_well_e': 32000
        },
        'FLIR_Point_Grey_Blackfly_S_IMX290': {
            'brand': 'FLIR/Point Grey',
            'name': 'Blackfly S (IMX290)',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 250,
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
        'FLIR_Point_Grey_Blackfly_S_IMX178': {
            'brand': 'FLIR/Point Grey',
            'name': 'Blackfly S (IMX178)',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 220,
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
        'FLIR_Point_Grey_Firefly_S': {
            'brand': 'FLIR/Point Grey',
            'name': 'Firefly S',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 180,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 4.97,
            'sensor_height_mm': 3.73,
            'width': 720,
            'height': 540,
            'pixel_size_um': 6.9,
            'quantum_efficiency_pct': 65,
            'read_noise_e': 2.0,
            'full_well_e': 20000
        }
    }

    @classmethod
    def FLIR_Point_Grey_Chameleon3_USB3(cls):
        return cls.from_database(cls._DATABASE['FLIR_Point_Grey_Chameleon3_USB3'])

    @classmethod
    def FLIR_Point_Grey_Grasshopper3_USB3(cls):
        return cls.from_database(cls._DATABASE['FLIR_Point_Grey_Grasshopper3_USB3'])

    @classmethod
    def FLIR_Point_Grey_Blackfly_S_IMX290(cls):
        return cls.from_database(cls._DATABASE['FLIR_Point_Grey_Blackfly_S_IMX290'])

    @classmethod
    def FLIR_Point_Grey_Blackfly_S_IMX178(cls):
        return cls.from_database(cls._DATABASE['FLIR_Point_Grey_Blackfly_S_IMX178'])

    @classmethod
    def FLIR_Point_Grey_Firefly_S(cls):
        return cls.from_database(cls._DATABASE['FLIR_Point_Grey_Firefly_S'])
