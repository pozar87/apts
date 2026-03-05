from ..base import Camera


class OmegonCamera(Camera):
    _DATABASE = {
        "Omegon_veTEC_571C": {
            "brand": "Omegon",
            "name": "veTEC 571C",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 600,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
            "sensor_width_mm": 23.5,
            "sensor_height_mm": 15.7,
            "width": 6224,
            "height": 4168,
            "pixel_size_um": 3.76,
            "quantum_efficiency_pct": 81,
            "read_noise_e": 1.1,
            "full_well_e": 51000,
        },
        "Omegon_veTEC_533C": {
            "brand": "Omegon",
            "name": "veTEC 533C",
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
        "Omegon_veTEC_294C": {
            "brand": "Omegon",
            "name": "veTEC 294C",
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
        "Omegon_veTEC_183C": {
            "brand": "Omegon",
            "name": "veTEC 183C",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 400,
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
        "Omegon_veTEC_26000C_Pro": {
            "brand": "Omegon",
            "name": "veTEC 26000C Pro",
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
            "width": 6224,
            "height": 4168,
            "pixel_size_um": 3.76,
            "quantum_efficiency_pct": 81,
            "read_noise_e": 1.1,
            "full_well_e": 51000,
        },
        "Omegon_veTEC_2600MC": {
            "brand": "Omegon",
            "name": "veTEC 2600MC",
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
            "width": 6224,
            "height": 4168,
            "pixel_size_um": 3.76,
            "quantum_efficiency_pct": 81,
            "read_noise_e": 1.1,
            "full_well_e": 51000,
        },
        "Omegon_veTEC_571M": {
            "brand": "Omegon",
            "name": "veTEC 571M",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 620,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
            "sensor_width_mm": 23.5,
            "sensor_height_mm": 15.7,
            "width": 6224,
            "height": 4168,
            "pixel_size_um": 3.76,
            "quantum_efficiency_pct": 91,
            "read_noise_e": 1.1,
            "full_well_e": 51000,
        },
        "Omegon_veTEC_16000C": {
            "brand": "Omegon",
            "name": "veTEC 16000C",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 550,
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
        "Omegon_veTEC_585C": {
            "brand": "Omegon",
            "name": "veTEC 585C",
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
        "Omegon_veTEC_462C": {
            "brand": "Omegon",
            "name": "veTEC 462C",
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
        "Omegon_veTEC_178M": {
            "brand": "Omegon",
            "name": "veTEC 178M",
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
        "Omegon_veTEC_290M": {
            "brand": "Omegon",
            "name": "veTEC 290M",
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
        "Omegon_vePROBE_462C": {
            "brand": "Omegon",
            "name": "vePROBE 462C",
            "type": "type_camera",
            "optical_length": 12.5,
            "mass": 80,
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
        "Omegon_vePROBE_290MC": {
            "brand": "Omegon",
            "name": "vePROBE 290MC",
            "type": "type_camera",
            "optical_length": 12.5,
            "mass": 80,
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
    }

    @classmethod
    def Omegon_veTEC_571C(cls):
        return cls.from_database(cls._DATABASE['Omegon_veTEC_571C'])

    @classmethod
    def Omegon_veTEC_533C(cls):
        return cls.from_database(cls._DATABASE['Omegon_veTEC_533C'])

    @classmethod
    def Omegon_veTEC_294C(cls):
        return cls.from_database(cls._DATABASE['Omegon_veTEC_294C'])

    @classmethod
    def Omegon_veTEC_183C(cls):
        return cls.from_database(cls._DATABASE['Omegon_veTEC_183C'])

    @classmethod
    def Omegon_veTEC_26000C_Pro(cls):
        return cls.from_database(cls._DATABASE['Omegon_veTEC_26000C_Pro'])

    @classmethod
    def Omegon_veTEC_2600MC(cls):
        return cls.from_database(cls._DATABASE['Omegon_veTEC_2600MC'])

    @classmethod
    def Omegon_veTEC_571M(cls):
        return cls.from_database(cls._DATABASE['Omegon_veTEC_571M'])

    @classmethod
    def Omegon_veTEC_16000C(cls):
        return cls.from_database(cls._DATABASE['Omegon_veTEC_16000C'])

    @classmethod
    def Omegon_veTEC_585C(cls):
        return cls.from_database(cls._DATABASE['Omegon_veTEC_585C'])

    @classmethod
    def Omegon_veTEC_462C(cls):
        return cls.from_database(cls._DATABASE['Omegon_veTEC_462C'])

    @classmethod
    def Omegon_veTEC_178M(cls):
        return cls.from_database(cls._DATABASE['Omegon_veTEC_178M'])

    @classmethod
    def Omegon_veTEC_290M(cls):
        return cls.from_database(cls._DATABASE['Omegon_veTEC_290M'])

    @classmethod
    def Omegon_vePROBE_462C(cls):
        return cls.from_database(cls._DATABASE['Omegon_vePROBE_462C'])

    @classmethod
    def Omegon_vePROBE_290MC(cls):
        return cls.from_database(cls._DATABASE['Omegon_vePROBE_290MC'])