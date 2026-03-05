from ..base import Camera

class Explore_scientificCamera(Camera):
    _DATABASE = {
        'Explore_Scientific_5MP_Guide_Camera': {
            'brand': 'Explore Scientific',
            'name': '5MP Guide Camera',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 80,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 5.18,
            'sensor_height_mm': 3.89,
            'width': 2592,
            'height': 1944,
            'pixel_size_um': 2.0,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 1.5,
            'full_well_e': 10000
        },
        'Explore_Scientific_3MP_USB3_Planetary': {
            'brand': 'Explore Scientific',
            'name': '3MP USB3 Planetary',
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
            'width': 2048,
            'height': 1536,
            'pixel_size_um': 3.75,
            'quantum_efficiency_pct': 75,
            'read_noise_e': 1.0,
            'full_well_e': 19000
        },
        'Explore_Scientific_Starlight_571C': {
            'brand': 'Explore Scientific',
            'name': 'Starlight 571C',
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
            'width': 6248,
            'height': 4176,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 81,
            'read_noise_e': 1.1,
            'full_well_e': 51000
        },
        'Explore_Scientific_Starlight_533C': {
            'brand': 'Explore Scientific',
            'name': 'Starlight 533C',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 450,
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
        'Explore_Scientific_Starlight_585C': {
            'brand': 'Explore Scientific',
            'name': 'Starlight 585C',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 160,
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
        }
    }

    @classmethod
    def Explore_Scientific_5MP_Guide_Camera(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_5MP_Guide_Camera'])

    @classmethod
    def Explore_Scientific_3MP_USB3_Planetary(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_3MP_USB3_Planetary'])

    @classmethod
    def Explore_Scientific_Starlight_571C(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_Starlight_571C'])

    @classmethod
    def Explore_Scientific_Starlight_533C(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_Starlight_533C'])

    @classmethod
    def Explore_Scientific_Starlight_585C(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_Starlight_585C'])
