from ..base import Camera

class OrionCamera(Camera):
    _DATABASE = {
        'Orion_StarShoot_G21': {
            'brand': 'Orion',
            'name': 'StarShoot G21',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 350,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 17.3,
            'sensor_height_mm': 13.0,
            'width': 5280,
            'height': 3956,
            'pixel_size_um': 3.3,
            'quantum_efficiency_pct': 84,
            'read_noise_e': 1.0,
            'full_well_e': 14000
        },
        'Orion_StarShoot_G26_Deep_Space': {
            'brand': 'Orion',
            'name': 'StarShoot G26 Deep Space',
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
            'width': 6224,
            'height': 4168,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 81,
            'read_noise_e': 1.1,
            'full_well_e': 51000
        },
        'Orion_StarShoot_Solar_System_V': {
            'brand': 'Orion',
            'name': 'StarShoot Solar System V',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 150,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 6.5,
            'sensor_height_mm': 4.9,
            'width': 2040,
            'height': 1528,
            'pixel_size_um': 3.2,
            'quantum_efficiency_pct': 50,
            'read_noise_e': 10.0,
            'full_well_e': 10000
        },
        'Orion_StarShoot_Autoguider': {
            'brand': 'Orion',
            'name': 'StarShoot Autoguider',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 100,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 6.66,
            'sensor_height_mm': 5.32,
            'width': 1280,
            'height': 1024,
            'pixel_size_um': 5.2,
            'quantum_efficiency_pct': 50,
            'read_noise_e': 15.0,
            'full_well_e': 40000
        },
        'Orion_StarShoot_Deep_Space_3': {
            'brand': 'Orion',
            'name': 'StarShoot Deep Space 3',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 400,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 8.5,
            'sensor_height_mm': 6.8,
            'width': 1392,
            'height': 1040,
            'pixel_size_um': 6.45,
            'quantum_efficiency_pct': 60,
            'read_noise_e': 6.0,
            'full_well_e': 25000
        },
        'Orion_StarShoot_Mini': {
            'brand': 'Orion',
            'name': 'StarShoot Mini',
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
        }
    }

    @classmethod
    def Orion_StarShoot_G21(cls):
        return cls.from_database(cls._DATABASE['Orion_StarShoot_G21'])

    @classmethod
    def Orion_StarShoot_G26_Deep_Space(cls):
        return cls.from_database(cls._DATABASE['Orion_StarShoot_G26_Deep_Space'])

    @classmethod
    def Orion_StarShoot_Solar_System_V(cls):
        return cls.from_database(cls._DATABASE['Orion_StarShoot_Solar_System_V'])

    @classmethod
    def Orion_StarShoot_Autoguider(cls):
        return cls.from_database(cls._DATABASE['Orion_StarShoot_Autoguider'])

    @classmethod
    def Orion_StarShoot_Deep_Space_3(cls):
        return cls.from_database(cls._DATABASE['Orion_StarShoot_Deep_Space_3'])

    @classmethod
    def Orion_StarShoot_Mini(cls):
        return cls.from_database(cls._DATABASE['Orion_StarShoot_Mini'])
