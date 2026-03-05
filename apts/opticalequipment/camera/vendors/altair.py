from ..base import Camera


class AltairCamera(Camera):
    _DATABASE = {
        "Altair_Hypercam_269C_Pro": {
            "brand": "Altair",
            "name": "Hypercam 269C Pro",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 700,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
            "sensor_width_mm": 17.3,
            "sensor_height_mm": 13.0,
            "width": 5280,
            "height": 3956,
            "pixel_size_um": 3.3,
            "quantum_efficiency_pct": 84,
            "read_noise_e": 1.0,
            "full_well_e": 14000,
        },
        "Altair_Hypercam_183M_Pro": {
            "brand": "Altair",
            "name": "Hypercam 183M Pro",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 500,
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
        "Altair_Hypercam_533C_Pro": {
            "brand": "Altair",
            "name": "Hypercam 533C Pro",
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
        "Altair_Hypercam_294C_Pro": {
            "brand": "Altair",
            "name": "Hypercam 294C Pro",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 680,
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
        "Altair_Hypercam_571C_Pro": {
            "brand": "Altair",
            "name": "Hypercam 571C Pro",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 650,
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
        "Altair_Hypercam_26000C_Pro": {
            "brand": "Altair",
            "name": "Hypercam 26000C Pro",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 750,
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
        "Altair_Hypercam_585C": {
            "brand": "Altair",
            "name": "Hypercam 585C",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 150,
            "tside_thread": "M42",
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
        "Altair_Hypercam_462C": {
            "brand": "Altair",
            "name": "Hypercam 462C",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 150,
            "tside_thread": "M42",
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
        "Altair_Hypercam_678C": {
            "brand": "Altair",
            "name": "Hypercam 678C",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 170,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
            "sensor_width_mm": 7.68,
            "sensor_height_mm": 4.32,
            "width": 3840,
            "height": 2160,
            "pixel_size_um": 2.0,
            "quantum_efficiency_pct": 83,
            "read_noise_e": 0.6,
            "full_well_e": 10000,
        },
        "Altair_Hypercam_174M": {
            "brand": "Altair",
            "name": "Hypercam 174M",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 180,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
            "sensor_width_mm": 11.3,
            "sensor_height_mm": 7.1,
            "width": 1936,
            "height": 1216,
            "pixel_size_um": 5.86,
            "quantum_efficiency_pct": 77,
            "read_noise_e": 6.0,
            "full_well_e": 32000,
        },
        "Altair_Hypercam_290M": {
            "brand": "Altair",
            "name": "Hypercam 290M",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 150,
            "tside_thread": "M42",
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
        "Altair_Hypercam_290C": {
            "brand": "Altair",
            "name": "Hypercam 290C",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 150,
            "tside_thread": "M42",
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
        "Altair_Hypercam_178M": {
            "brand": "Altair",
            "name": "Hypercam 178M",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 150,
            "tside_thread": "M42",
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
        "Altair_Hypercam_178C": {
            "brand": "Altair",
            "name": "Hypercam 178C",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 150,
            "tside_thread": "M42",
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
        "Altair_Hypercam_224C": {
            "brand": "Altair",
            "name": "Hypercam 224C",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 150,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
            "sensor_width_mm": 4.8,
            "sensor_height_mm": 3.6,
            "width": 1304,
            "height": 976,
            "pixel_size_um": 3.75,
            "quantum_efficiency_pct": 75,
            "read_noise_e": 0.75,
            "full_well_e": 19000,
        },
        "Altair_Hypercam_120M": {
            "brand": "Altair",
            "name": "Hypercam 120M",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 150,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
            "sensor_width_mm": 4.8,
            "sensor_height_mm": 3.6,
            "width": 1280,
            "height": 960,
            "pixel_size_um": 3.75,
            "quantum_efficiency_pct": 80,
            "read_noise_e": 4.0,
            "full_well_e": 13000,
        },
        "Altair_Hypercam_385C": {
            "brand": "Altair",
            "name": "Hypercam 385C",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 150,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
            "sensor_width_mm": 7.3,
            "sensor_height_mm": 4.1,
            "width": 1936,
            "height": 1096,
            "pixel_size_um": 3.75,
            "quantum_efficiency_pct": 80,
            "read_noise_e": 0.7,
            "full_well_e": 18700,
        },
        "Altair_Hypercam_174C": {
            "brand": "Altair",
            "name": "Hypercam 174C",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 180,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
            "sensor_width_mm": 11.3,
            "sensor_height_mm": 7.1,
            "width": 1936,
            "height": 1216,
            "pixel_size_um": 5.86,
            "quantum_efficiency_pct": 77,
            "read_noise_e": 6.0,
            "full_well_e": 32000,
        },
        "Altair_Hypercam_2600C_Pro": {
            "brand": "Altair",
            "name": "Hypercam 2600C Pro",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 750,
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
        "Altair_Hypercam_16000M_Pro": {
            "brand": "Altair",
            "name": "Hypercam 16000M Pro",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 500,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
            "sensor_width_mm": 17.7,
            "sensor_height_mm": 13.4,
            "width": 4656,
            "height": 3520,
            "pixel_size_um": 3.8,
            "quantum_efficiency_pct": 60,
            "read_noise_e": 1.2,
            "full_well_e": 20000,
        },
        "Altair_GPCAM3_290M": {
            "brand": "Altair",
            "name": "GPCAM3 290M",
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
        "Altair_GPCAM3_178M": {
            "brand": "Altair",
            "name": "GPCAM3 178M",
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
        "Altair_GPCAM3_462C": {
            "brand": "Altair",
            "name": "GPCAM3 462C",
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
        "Altair_GPCAM3_385C": {
            "brand": "Altair",
            "name": "GPCAM3 385C",
            "type": "type_camera",
            "optical_length": 12.5,
            "mass": 150,
            "tside_thread": "CS",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
            "sensor_width_mm": 7.3,
            "sensor_height_mm": 4.1,
            "width": 1936,
            "height": 1096,
            "pixel_size_um": 3.75,
            "quantum_efficiency_pct": 80,
            "read_noise_e": 0.7,
            "full_well_e": 18700,
        },
        "Altair_Hypercam_26000M_Pro": {
            "brand": "Altair",
            "name": "Hypercam 26000M Pro",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 750,
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
        "Altair_Hypercam_571M_Pro": {
            "brand": "Altair",
            "name": "Hypercam 571M Pro",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 650,
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
        "Altair_Hypercam_533M_Pro": {
            "brand": "Altair",
            "name": "Hypercam 533M Pro",
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
            "quantum_efficiency_pct": 91,
            "read_noise_e": 1.0,
            "full_well_e": 50000,
        },
        "Altair_Hypercam_294M_Pro": {
            "brand": "Altair",
            "name": "Hypercam 294M Pro",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 680,
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
            "quantum_efficiency_pct": 90,
            "read_noise_e": 1.2,
            "full_well_e": 66000,
        },
        "Altair_Hypercam_183M_Pro_v2": {
            "brand": "Altair",
            "name": "Hypercam 183M Pro v2",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 500,
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
        "Altair_Hypercam_2600M_Pro": {
            "brand": "Altair",
            "name": "Hypercam 2600M Pro",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 750,
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
    }

    @classmethod
    def Altair_Hypercam_269C_Pro(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_269C_Pro'])

    @classmethod
    def Altair_Hypercam_183M_Pro(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_183M_Pro'])

    @classmethod
    def Altair_Hypercam_533C_Pro(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_533C_Pro'])

    @classmethod
    def Altair_Hypercam_294C_Pro(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_294C_Pro'])

    @classmethod
    def Altair_Hypercam_571C_Pro(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_571C_Pro'])

    @classmethod
    def Altair_Hypercam_26000C_Pro(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_26000C_Pro'])

    @classmethod
    def Altair_Hypercam_585C(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_585C'])

    @classmethod
    def Altair_Hypercam_462C(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_462C'])

    @classmethod
    def Altair_Hypercam_678C(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_678C'])

    @classmethod
    def Altair_Hypercam_174M(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_174M'])

    @classmethod
    def Altair_Hypercam_290M(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_290M'])

    @classmethod
    def Altair_Hypercam_290C(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_290C'])

    @classmethod
    def Altair_Hypercam_178M(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_178M'])

    @classmethod
    def Altair_Hypercam_178C(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_178C'])

    @classmethod
    def Altair_Hypercam_224C(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_224C'])

    @classmethod
    def Altair_Hypercam_120M(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_120M'])

    @classmethod
    def Altair_Hypercam_385C(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_385C'])

    @classmethod
    def Altair_Hypercam_174C(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_174C'])

    @classmethod
    def Altair_Hypercam_2600C_Pro(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_2600C_Pro'])

    @classmethod
    def Altair_Hypercam_16000M_Pro(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_16000M_Pro'])

    @classmethod
    def Altair_GPCAM3_290M(cls):
        return cls.from_database(cls._DATABASE['Altair_GPCAM3_290M'])

    @classmethod
    def Altair_GPCAM3_178M(cls):
        return cls.from_database(cls._DATABASE['Altair_GPCAM3_178M'])

    @classmethod
    def Altair_GPCAM3_462C(cls):
        return cls.from_database(cls._DATABASE['Altair_GPCAM3_462C'])

    @classmethod
    def Altair_GPCAM3_385C(cls):
        return cls.from_database(cls._DATABASE['Altair_GPCAM3_385C'])

    @classmethod
    def Altair_Hypercam_26000M_Pro(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_26000M_Pro'])

    @classmethod
    def Altair_Hypercam_571M_Pro(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_571M_Pro'])

    @classmethod
    def Altair_Hypercam_533M_Pro(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_533M_Pro'])

    @classmethod
    def Altair_Hypercam_294M_Pro(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_294M_Pro'])

    @classmethod
    def Altair_Hypercam_183M_Pro_v2(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_183M_Pro_v2'])

    @classmethod
    def Altair_Hypercam_2600M_Pro(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_2600M_Pro'])
