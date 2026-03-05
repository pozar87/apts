from ..base import Camera

class BresserCamera(Camera):
    _DATABASE = {
        'Bresser_MikroCamII_5MP': {
            'brand': 'Bresser',
            'name': 'MikroCamII 5MP',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 100,
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
        'Bresser_MikroCamII_10MP': {
            'brand': 'Bresser',
            'name': 'MikroCamII 10MP',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 120,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 6.4,
            'sensor_height_mm': 4.6,
            'width': 3584,
            'height': 2746,
            'pixel_size_um': 1.67,
            'quantum_efficiency_pct': 60,
            'read_noise_e': 2.0,
            'full_well_e': 5000
        },
        'Bresser_Full_HD_Deep_Sky': {
            'brand': 'Bresser',
            'name': 'Full HD Deep Sky',
            'type': 'type_camera',
            'optical_length': 6.5,
            'mass': 300,
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
        'Bresser_Astro_2MP_Guide': {
            'brand': 'Bresser',
            'name': 'Astro 2MP Guide',
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
        }
    }

    @classmethod
    def Bresser_MikroCamII_5MP(cls):
        return cls.from_database(cls._DATABASE['Bresser_MikroCamII_5MP'])

    @classmethod
    def Bresser_MikroCamII_10MP(cls):
        return cls.from_database(cls._DATABASE['Bresser_MikroCamII_10MP'])

    @classmethod
    def Bresser_Full_HD_Deep_Sky(cls):
        return cls.from_database(cls._DATABASE['Bresser_Full_HD_Deep_Sky'])

    @classmethod
    def Bresser_Astro_2MP_Guide(cls):
        return cls.from_database(cls._DATABASE['Bresser_Astro_2MP_Guide'])
