from ..base import Camera

class MeadeCamera(Camera):
    _DATABASE = {
        'Meade_LPI_G_Color': {
            'brand': 'Meade',
            'name': 'LPI-G (Color)',
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
        'Meade_LPI_G_Mono': {
            'brand': 'Meade',
            'name': 'LPI-G (Mono)',
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
        'Meade_LPI_G_Advanced_Color': {
            'brand': 'Meade',
            'name': 'LPI-G Advanced (Color)',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 120,
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
        'Meade_Deep_Sky_Imager_IV_Color': {
            'brand': 'Meade',
            'name': 'Deep Sky Imager IV (Color)',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 250,
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
        'Meade_Deep_Sky_Imager_IV_Mono': {
            'brand': 'Meade',
            'name': 'Deep Sky Imager IV (Mono)',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 250,
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
        'Meade_Deep_Sky_Imager_Pro': {
            'brand': 'Meade',
            'name': 'Deep Sky Imager Pro',
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
            'width': 510,
            'height': 492,
            'pixel_size_um': 9.6,
            'quantum_efficiency_pct': 50,
            'read_noise_e': 15.0,
            'full_well_e': 30000
        }
    }

    @classmethod
    def Meade_LPI_G_Color(cls):
        return cls.from_database(cls._DATABASE['Meade_LPI_G_Color'])

    @classmethod
    def Meade_LPI_G_Mono(cls):
        return cls.from_database(cls._DATABASE['Meade_LPI_G_Mono'])

    @classmethod
    def Meade_LPI_G_Advanced_Color(cls):
        return cls.from_database(cls._DATABASE['Meade_LPI_G_Advanced_Color'])

    @classmethod
    def Meade_Deep_Sky_Imager_IV_Color(cls):
        return cls.from_database(cls._DATABASE['Meade_Deep_Sky_Imager_IV_Color'])

    @classmethod
    def Meade_Deep_Sky_Imager_IV_Mono(cls):
        return cls.from_database(cls._DATABASE['Meade_Deep_Sky_Imager_IV_Mono'])

    @classmethod
    def Meade_Deep_Sky_Imager_Pro(cls):
        return cls.from_database(cls._DATABASE['Meade_Deep_Sky_Imager_Pro'])
