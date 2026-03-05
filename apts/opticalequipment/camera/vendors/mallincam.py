from ..base import Camera

class MallincamCamera(Camera):
    _DATABASE = {
        'Mallincam_SkyRaider_DS26000C': {
            'brand': 'Mallincam',
            'name': 'SkyRaider DS26000C',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 700,
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
        'Mallincam_SkyRaider_DS16000C': {
            'brand': 'Mallincam',
            'name': 'SkyRaider DS16000C',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 500,
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
        'Mallincam_SkyRaider_DS2100C': {
            'brand': 'Mallincam',
            'name': 'SkyRaider DS2100C',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 350,
            'tside_thread': 'M42',
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
        'Mallincam_SkyRaider_DS287C': {
            'brand': 'Mallincam',
            'name': 'SkyRaider DS287C',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 250,
            'tside_thread': 'M42',
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
        },
        'Mallincam_Xtreme_Solar_System_Imager': {
            'brand': 'Mallincam',
            'name': 'Xtreme Solar System Imager',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 120,
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
        'Mallincam_SkyRaider_DS26C': {
            'brand': 'Mallincam',
            'name': 'SkyRaider DS26C',
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
        'Mallincam_SkyRaider_DS10C': {
            'brand': 'Mallincam',
            'name': 'SkyRaider DS10C',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 300,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 13.0,
            'sensor_height_mm': 8.0,
            'width': 3840,
            'height': 2160,
            'pixel_size_um': 3.3,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 1.5,
            'full_well_e': 15000
        },
        'Mallincam_Xtreme': {
            'brand': 'Mallincam',
            'name': 'Xtreme',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 600,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 6.4,
            'sensor_height_mm': 4.8,
            'width': 752,
            'height': 582,
            'pixel_size_um': 8.6,
            'quantum_efficiency_pct': 60,
            'read_noise_e': 10.0,
            'full_well_e': 25000
        },
        'Mallincam_Universe': {
            'brand': 'Mallincam',
            'name': 'Universe',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 800,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 23.4,
            'sensor_height_mm': 15.6,
            'width': 3032,
            'height': 2016,
            'pixel_size_um': 7.8,
            'quantum_efficiency_pct': 50,
            'read_noise_e': 12.0,
            'full_well_e': 40000
        },
        'Mallincam_Micro': {
            'brand': 'Mallincam',
            'name': 'Micro',
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
            'width': 752,
            'height': 582,
            'pixel_size_um': 6.35,
            'quantum_efficiency_pct': 55,
            'read_noise_e': 15.0,
            'full_well_e': 20000
        }
    }

    @classmethod
    def Mallincam_SkyRaider_DS26000C(cls):
        return cls.from_database(cls._DATABASE['Mallincam_SkyRaider_DS26000C'])

    @classmethod
    def Mallincam_SkyRaider_DS16000C(cls):
        return cls.from_database(cls._DATABASE['Mallincam_SkyRaider_DS16000C'])

    @classmethod
    def Mallincam_SkyRaider_DS2100C(cls):
        return cls.from_database(cls._DATABASE['Mallincam_SkyRaider_DS2100C'])

    @classmethod
    def Mallincam_SkyRaider_DS287C(cls):
        return cls.from_database(cls._DATABASE['Mallincam_SkyRaider_DS287C'])

    @classmethod
    def Mallincam_Xtreme_Solar_System_Imager(cls):
        return cls.from_database(cls._DATABASE['Mallincam_Xtreme_Solar_System_Imager'])

    @classmethod
    def Mallincam_SkyRaider_DS26C(cls):
        return cls.from_database(cls._DATABASE['Mallincam_SkyRaider_DS26C'])

    @classmethod
    def Mallincam_SkyRaider_DS10C(cls):
        return cls.from_database(cls._DATABASE['Mallincam_SkyRaider_DS10C'])

    @classmethod
    def Mallincam_Xtreme(cls):
        return cls.from_database(cls._DATABASE['Mallincam_Xtreme'])

    @classmethod
    def Mallincam_Universe(cls):
        return cls.from_database(cls._DATABASE['Mallincam_Universe'])

    @classmethod
    def Mallincam_Micro(cls):
        return cls.from_database(cls._DATABASE['Mallincam_Micro'])
