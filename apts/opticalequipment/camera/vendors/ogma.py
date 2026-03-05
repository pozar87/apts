from ..base import Camera


class OgmaCamera(Camera):
    _DATABASE = {
        "OGMA_OGC_533C_Pro": {
            "brand": "OGMA",
            "name": "OGC-533C Pro",
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
        "OGMA_OGC_294C_Pro": {
            "brand": "OGMA",
            "name": "OGC-294C Pro",
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
        "OGMA_OGC_571C_Pro": {
            "brand": "OGMA",
            "name": "OGC-571C Pro",
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
        "OGMA_OGC_183C_Pro": {
            "brand": "OGMA",
            "name": "OGC-183C Pro",
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
        "OGMA_OGC_585C": {
            "brand": "OGMA",
            "name": "OGC-585C",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 180,
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
        "OGMA_OGC_462C": {
            "brand": "OGMA",
            "name": "OGC-462C",
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
        "OGMA_OGC_678C": {
            "brand": "OGMA",
            "name": "OGC-678C",
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
        "OGMA_OGC_178C": {
            "brand": "OGMA",
            "name": "OGC-178C",
            "type": "type_camera",
            "optical_length": 12.5,
            "mass": 80,
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
        "OGMA_OGC_533M_Pro": {
            "brand": "OGMA",
            "name": "OGC-533M Pro",
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
        "OGMA_OGC_2600C_Pro": {
            "brand": "OGMA",
            "name": "OGC-2600C Pro",
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
        "OGMA_OGC_2600M_Pro": {
            "brand": "OGMA",
            "name": "OGC-2600M Pro",
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
        "OGMA_OGC_290MC": {
            "brand": "OGMA",
            "name": "OGC-290MC",
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
        "OGMA_OGC_178MM": {
            "brand": "OGMA",
            "name": "OGC-178MM",
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
        "OGMA_OGC_571M_Pro": {
            "brand": "OGMA",
            "name": "OGC-571M Pro",
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
        "OGMA_OGC_2600C": {
            "brand": "OGMA",
            "name": "OGC-2600C",
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
        "OGMA_OGC_2600M": {
            "brand": "OGMA",
            "name": "OGC-2600M",
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
        "OGMA_OGC_571C": {
            "brand": "OGMA",
            "name": "OGC-571C",
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
        "OGMA_OGC_183M_Pro": {
            "brand": "OGMA",
            "name": "OGC-183M Pro",
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
    }

    @classmethod
    def OGMA_OGC_533C_Pro(cls):
        return cls.from_database(cls._DATABASE['OGMA_OGC_533C_Pro'])

    @classmethod
    def OGMA_OGC_294C_Pro(cls):
        return cls.from_database(cls._DATABASE['OGMA_OGC_294C_Pro'])

    @classmethod
    def OGMA_OGC_571C_Pro(cls):
        return cls.from_database(cls._DATABASE['OGMA_OGC_571C_Pro'])

    @classmethod
    def OGMA_OGC_183C_Pro(cls):
        return cls.from_database(cls._DATABASE['OGMA_OGC_183C_Pro'])

    @classmethod
    def OGMA_OGC_585C(cls):
        return cls.from_database(cls._DATABASE['OGMA_OGC_585C'])

    @classmethod
    def OGMA_OGC_462C(cls):
        return cls.from_database(cls._DATABASE['OGMA_OGC_462C'])

    @classmethod
    def OGMA_OGC_678C(cls):
        return cls.from_database(cls._DATABASE['OGMA_OGC_678C'])

    @classmethod
    def OGMA_OGC_178C(cls):
        return cls.from_database(cls._DATABASE['OGMA_OGC_178C'])

    @classmethod
    def OGMA_OGC_533M_Pro(cls):
        return cls.from_database(cls._DATABASE['OGMA_OGC_533M_Pro'])

    @classmethod
    def OGMA_OGC_2600C_Pro(cls):
        return cls.from_database(cls._DATABASE['OGMA_OGC_2600C_Pro'])

    @classmethod
    def OGMA_OGC_2600M_Pro(cls):
        return cls.from_database(cls._DATABASE['OGMA_OGC_2600M_Pro'])

    @classmethod
    def OGMA_OGC_290MC(cls):
        return cls.from_database(cls._DATABASE['OGMA_OGC_290MC'])

    @classmethod
    def OGMA_OGC_178MM(cls):
        return cls.from_database(cls._DATABASE['OGMA_OGC_178MM'])

    @classmethod
    def OGMA_OGC_571M_Pro(cls):
        return cls.from_database(cls._DATABASE['OGMA_OGC_571M_Pro'])

    @classmethod
    def OGMA_OGC_2600C(cls):
        return cls.from_database(cls._DATABASE['OGMA_OGC_2600C'])

    @classmethod
    def OGMA_OGC_2600M(cls):
        return cls.from_database(cls._DATABASE['OGMA_OGC_2600M'])

    def OGMA_OGC_571C(cls):
        return cls.from_database(cls._DATABASE["OGMA_OGC_571C"])

    @classmethod
    def OGMA_OGC_183M_Pro(cls):
        return cls.from_database(cls._DATABASE["OGMA_OGC_183M_Pro"])
