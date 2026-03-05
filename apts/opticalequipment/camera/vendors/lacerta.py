from ..base import Camera


class LacertaCamera(Camera):
    _DATABASE = {
        "Lacerta_DeepSkyPro_2600C": {
            "brand": "Lacerta",
            "name": "DeepSkyPro 2600C",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 700,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
            "sensor_width_mm": 23.5,
            "sensor_height_mm": 15.7,
            "width": 6248,
            "height": 4176,
            "pixel_size_um": 3.76,
            "quantum_efficiency_pct": 81,
            "read_noise_e": 1.1,
            "full_well_e": 51000,
        },
        "Lacerta_DeepSkyPro_533C": {
            "brand": "Lacerta",
            "name": "DeepSkyPro 533C",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 450,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
            "sensor_width_mm": 11.31,
            "sensor_height_mm": 11.31,
            "width": 3008,
            "height": 3008,
            "pixel_size_um": 3.76,
            "quantum_efficiency_pct": 80,
            "read_noise_e": 1.0,
            "full_well_e": 50000,
        },
        "Lacerta_DeepSkyPro_294C": {
            "brand": "Lacerta",
            "name": "DeepSkyPro 294C",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 500,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
            "sensor_width_mm": 19.1,
            "sensor_height_mm": 13.0,
            "width": 4144,
            "height": 2822,
            "pixel_size_um": 4.63,
            "quantum_efficiency_pct": 75,
            "read_noise_e": 1.2,
            "full_well_e": 63700,
        },
        "Lacerta_DeepSkyPro_571C": {
            "brand": "Lacerta",
            "name": "DeepSkyPro 571C",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 580,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
            "sensor_width_mm": 23.5,
            "sensor_height_mm": 15.7,
            "width": 6248,
            "height": 4176,
            "pixel_size_um": 3.76,
            "quantum_efficiency_pct": 81,
            "read_noise_e": 1.1,
            "full_well_e": 51000,
        },
        "Lacerta_DeepSkyPro_2600M": {
            "brand": "Lacerta",
            "name": "DeepSkyPro 2600M",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 720,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
            "sensor_width_mm": 23.5,
            "sensor_height_mm": 15.7,
            "width": 6248,
            "height": 4176,
            "pixel_size_um": 3.76,
            "quantum_efficiency_pct": 91,
            "read_noise_e": 1.1,
            "full_well_e": 51000,
        },
        "Lacerta_DeepSkyPro_183C": {
            "brand": "Lacerta",
            "name": "DeepSkyPro 183C",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 420,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
            "sensor_width_mm": 13.2,
            "sensor_height_mm": 8.8,
            "width": 5496,
            "height": 3672,
            "pixel_size_um": 2.4,
            "quantum_efficiency_pct": 84,
            "read_noise_e": 1.6,
            "full_well_e": 15000,
        },
        "Lacerta_DeepSkyPro_183M": {
            "brand": "Lacerta",
            "name": "DeepSkyPro 183M",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 430,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
            "sensor_width_mm": 13.2,
            "sensor_height_mm": 8.8,
            "width": 5496,
            "height": 3672,
            "pixel_size_um": 2.4,
            "quantum_efficiency_pct": 84,
            "read_noise_e": 1.6,
            "full_well_e": 15000,
        },
        "Lacerta_DeepSkyPro_585C": {
            "brand": "Lacerta",
            "name": "DeepSkyPro 585C",
            "type": "type_camera",
            "optical_length": 12.5,
            "mass": 180,
            "tside_thread": "CS",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
            "sensor_width_mm": 11.13,
            "sensor_height_mm": 6.26,
            "width": 3840,
            "height": 2160,
            "pixel_size_um": 2.9,
            "quantum_efficiency_pct": 91,
            "read_noise_e": 0.6,
            "full_well_e": 40000,
        },
        "Lacerta_DeepSkyPro_462C": {
            "brand": "Lacerta",
            "name": "DeepSkyPro 462C",
            "type": "type_camera",
            "optical_length": 12.5,
            "mass": 150,
            "tside_thread": "CS",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
            "sensor_width_mm": 5.6,
            "sensor_height_mm": 3.2,
            "width": 1920,
            "height": 1080,
            "pixel_size_um": 2.9,
            "quantum_efficiency_pct": 91,
            "read_noise_e": 0.5,
            "full_well_e": 12000,
        },
        "Lacerta_DeepSkyPro_290MC": {
            "brand": "Lacerta",
            "name": "DeepSkyPro 290MC",
            "type": "type_camera",
            "optical_length": 12.5,
            "mass": 150,
            "tside_thread": "CS",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
            "sensor_width_mm": 5.6,
            "sensor_height_mm": 3.2,
            "width": 1936,
            "height": 1096,
            "pixel_size_um": 2.9,
            "quantum_efficiency_pct": 80,
            "read_noise_e": 1.0,
            "full_well_e": 14600,
        },
        "Lacerta_DeepSkyPro_178MM": {
            "brand": "Lacerta",
            "name": "DeepSkyPro 178MM",
            "type": "type_camera",
            "optical_length": 12.5,
            "mass": 150,
            "tside_thread": "CS",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
            "sensor_width_mm": 7.4,
            "sensor_height_mm": 5.0,
            "width": 3072,
            "height": 2048,
            "pixel_size_um": 2.4,
            "quantum_efficiency_pct": 78,
            "read_noise_e": 1.4,
            "full_well_e": 15000,
        },
    }

    @classmethod
    def Lacerta_DeepSkyPro_2600C(cls):
        return cls.from_database(cls._DATABASE['Lacerta_DeepSkyPro_2600C'])

    @classmethod
    def Lacerta_DeepSkyPro_533C(cls):
        return cls.from_database(cls._DATABASE['Lacerta_DeepSkyPro_533C'])

    @classmethod
    def Lacerta_DeepSkyPro_294C(cls):
        return cls.from_database(cls._DATABASE['Lacerta_DeepSkyPro_294C'])

    @classmethod
    def Lacerta_DeepSkyPro_571C(cls):
        return cls.from_database(cls._DATABASE['Lacerta_DeepSkyPro_571C'])

    @classmethod
    def Lacerta_DeepSkyPro_2600M(cls):
        return cls.from_database(cls._DATABASE['Lacerta_DeepSkyPro_2600M'])

    @classmethod
    def Lacerta_DeepSkyPro_183C(cls):
        return cls.from_database(cls._DATABASE['Lacerta_DeepSkyPro_183C'])

    @classmethod
    def Lacerta_DeepSkyPro_183M(cls):
        return cls.from_database(cls._DATABASE['Lacerta_DeepSkyPro_183M'])

    @classmethod
    def Lacerta_DeepSkyPro_585C(cls):
        return cls.from_database(cls._DATABASE['Lacerta_DeepSkyPro_585C'])

    @classmethod
    def Lacerta_DeepSkyPro_462C(cls):
        return cls.from_database(cls._DATABASE['Lacerta_DeepSkyPro_462C'])

    @classmethod
    def Lacerta_DeepSkyPro_290MC(cls):
        return cls.from_database(cls._DATABASE['Lacerta_DeepSkyPro_290MC'])

    @classmethod
    def Lacerta_DeepSkyPro_178MM(cls):
        return cls.from_database(cls._DATABASE['Lacerta_DeepSkyPro_178MM'])