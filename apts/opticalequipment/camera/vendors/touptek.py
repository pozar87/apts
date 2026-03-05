from ..base import Camera


class TouptekCamera(Camera):
    _DATABASE = {
        "ToupTek_ATR3CMOS26000KPA": {
            "brand": "ToupTek",
            "name": "ATR3CMOS26000KPA",
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
            "width": 6224,
            "height": 4168,
            "pixel_size_um": 3.76,
            "quantum_efficiency_pct": 81,
            "read_noise_e": 1.1,
            "full_well_e": 51000,
        },
        "ToupTek_ATR3CMOS16000KPA": {
            "brand": "ToupTek",
            "name": "ATR3CMOS16000KPA",
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
        "ToupTek_ATR3CMOS02000KMA": {
            "brand": "ToupTek",
            "name": "ATR3CMOS02000KMA",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 350,
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
        "ToupTek_ATR3CMOS06300KPA": {
            "brand": "ToupTek",
            "name": "ATR3CMOS06300KPA",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 450,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
            "sensor_width_mm": 12.48,
            "sensor_height_mm": 9.98,
            "width": 3072,
            "height": 2048,
            "pixel_size_um": 4.54,
            "quantum_efficiency_pct": 77,
            "read_noise_e": 4.0,
            "full_well_e": 18000,
        },
        "ToupTek_ATR3CMOS26000KMA": {
            "brand": "ToupTek",
            "name": "ATR3CMOS26000KMA",
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
            "width": 6224,
            "height": 4168,
            "pixel_size_um": 3.76,
            "quantum_efficiency_pct": 91,
            "read_noise_e": 1.1,
            "full_well_e": 51000,
        },
        "ToupTek_ATR3CMOS07100KPA": {
            "brand": "ToupTek",
            "name": "ATR3CMOS07100KPA",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 480,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
            "sensor_width_mm": 23.6,
            "sensor_height_mm": 15.6,
            "width": 4944,
            "height": 3284,
            "pixel_size_um": 4.78,
            "quantum_efficiency_pct": 50,
            "read_noise_e": 2.3,
            "full_well_e": 46000,
        },
        "ToupTek_ATR3CMOS21000KPA": {
            "brand": "ToupTek",
            "name": "ATR3CMOS21000KPA",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 600,
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
        "ToupTek_GP_CMOS02000KMA": {
            "brand": "ToupTek",
            "name": "GP-CMOS02000KMA",
            "type": "type_camera",
            "optical_length": 12.5,
            "mass": 100,
            "tside_thread": "CS",
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
        "ToupTek_GP_CMOS02900KPA": {
            "brand": "ToupTek",
            "name": "GP-CMOS02900KPA",
            "type": "type_camera",
            "optical_length": 12.5,
            "mass": 100,
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
        "ToupTek_GP_CMOS04600KPA": {
            "brand": "ToupTek",
            "name": "GP-CMOS04600KPA",
            "type": "type_camera",
            "optical_length": 12.5,
            "mass": 100,
            "tside_thread": "CS",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
            "sensor_width_mm": 6.7,
            "sensor_height_mm": 5.4,
            "width": 2448,
            "height": 2050,
            "pixel_size_um": 3.45,
            "quantum_efficiency_pct": 77,
            "read_noise_e": 5.0,
            "full_well_e": 18000,
        },
        "ToupTek_ATR3CMOS09440KPA": {
            "brand": "ToupTek",
            "name": "ATR3CMOS09440KPA",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 800,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
            "sensor_width_mm": 24.0,
            "sensor_height_mm": 36.0,
            "width": 7376,
            "height": 4928,
            "pixel_size_um": 4.88,
            "quantum_efficiency_pct": 56,
            "read_noise_e": 2.1,
            "full_well_e": 52000,
        },
        "ToupTek_ATR3CMOS04600KPA": {
            "brand": "ToupTek",
            "name": "ATR3CMOS04600KPA",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 550,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
            "sensor_width_mm": 6.7,
            "sensor_height_mm": 5.4,
            "width": 2448,
            "height": 2050,
            "pixel_size_um": 3.45,
            "quantum_efficiency_pct": 77,
            "read_noise_e": 5.0,
            "full_well_e": 18000,
        },
        "ToupTek_ATR3CMOS12000KPA": {
            "brand": "ToupTek",
            "name": "ATR3CMOS12000KPA",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 600,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
            "sensor_width_mm": 14.1,
            "sensor_height_mm": 10.3,
            "width": 4096,
            "height": 3000,
            "pixel_size_um": 3.45,
            "quantum_efficiency_pct": 78,
            "read_noise_e": 3.0,
            "full_well_e": 30000,
        },
        "ToupTek_ATR3CMOS09120KPA": {
            "brand": "ToupTek",
            "name": "ATR3CMOS09120KPA",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 500,
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
        "ToupTek_ATR3CMOS02100KPA": {
            "brand": "ToupTek",
            "name": "ATR3CMOS02100KPA",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 450,
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
        "ToupTek_ATR3CMOS08000KPA": {
            "brand": "ToupTek",
            "name": "ATR3CMOS08000KPA",
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
            "width": 3326,
            "height": 2504,
            "pixel_size_um": 3.9,
            "quantum_efficiency_pct": 84,
            "read_noise_e": 1.6,
            "full_well_e": 15000,
        },
        "ToupTek_GCMOS01200KPA": {
            "brand": "ToupTek",
            "name": "GCMOS01200KPA",
            "type": "type_camera",
            "optical_length": 12.5,
            "mass": 100,
            "tside_thread": "CS",
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
        "ToupTek_GCMOS01200KMA": {
            "brand": "ToupTek",
            "name": "GCMOS01200KMA",
            "type": "type_camera",
            "optical_length": 12.5,
            "mass": 100,
            "tside_thread": "CS",
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
        "ToupTek_ATR3CMOS16000KMA": {
            "brand": "ToupTek",
            "name": "ATR3CMOS16000KMA",
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
        "ToupTek_ATR3CMOS02900KPA": {
            "brand": "ToupTek",
            "name": "ATR3CMOS02900KPA",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 400,
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
        "ToupTek_ATR3CMOS04600KMA": {
            "brand": "ToupTek",
            "name": "ATR3CMOS04600KMA",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 550,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
            "sensor_width_mm": 6.7,
            "sensor_height_mm": 5.4,
            "width": 2448,
            "height": 2050,
            "pixel_size_um": 3.45,
            "quantum_efficiency_pct": 77,
            "read_noise_e": 5.0,
            "full_well_e": 18000,
        },
        "ToupTek_ATR3CMOS09440KMA": {
            "brand": "ToupTek",
            "name": "ATR3CMOS09440KMA",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 800,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
            "sensor_width_mm": 24.0,
            "sensor_height_mm": 36.0,
            "width": 7376,
            "height": 4928,
            "pixel_size_um": 4.88,
            "quantum_efficiency_pct": 91,
            "read_noise_e": 2.1,
            "full_well_e": 52000,
        },
        "ToupTek_ATR3CMOS12000KMA": {
            "brand": "ToupTek",
            "name": "ATR3CMOS12000KMA",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 600,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
            "sensor_width_mm": 14.1,
            "sensor_height_mm": 10.3,
            "width": 4096,
            "height": 3000,
            "pixel_size_um": 3.45,
            "quantum_efficiency_pct": 78,
            "read_noise_e": 3.0,
            "full_well_e": 30000,
        },
        "ToupTek_ATR3CMOS09120KMA": {
            "brand": "ToupTek",
            "name": "ATR3CMOS09120KMA",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 500,
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
        "ToupTek_ATR3CMOS02100KMA": {
            "brand": "ToupTek",
            "name": "ATR3CMOS02100KMA",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 450,
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
        "ToupTek_ATR3CMOS08000KMA": {
            "brand": "ToupTek",
            "name": "ATR3CMOS08000KMA",
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
            "width": 3326,
            "height": 2504,
            "pixel_size_um": 3.9,
            "quantum_efficiency_pct": 84,
            "read_noise_e": 1.6,
            "full_well_e": 15000,
        },
        "ToupTek_GP_CMOS01200KPA": {
            "brand": "ToupTek",
            "name": "GP-CMOS01200KPA",
            "type": "type_camera",
            "optical_length": 12.5,
            "mass": 100,
            "tside_thread": "CS",
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
        "ToupTek_GP_CMOS01200KMA": {
            "brand": "ToupTek",
            "name": "GP-CMOS01200KMA",
            "type": "type_camera",
            "optical_length": 12.5,
            "mass": 100,
            "tside_thread": "CS",
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
        "ToupTek_GP_CMOS05780KPA": {
            "brand": "ToupTek",
            "name": "GP-CMOS05780KPA",
            "type": "type_camera",
            "optical_length": 12.5,
            "mass": 100,
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
        "ToupTek_GP_CMOS05780KMA": {
            "brand": "ToupTek",
            "name": "GP-CMOS05780KMA",
            "type": "type_camera",
            "optical_length": 12.5,
            "mass": 100,
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
    def ToupTek_ATR3CMOS26000KPA(cls):
        return cls.from_database(cls._DATABASE["ToupTek_ATR3CMOS26000KPA"])

    @classmethod
    def ToupTek_ATR3CMOS16000KPA(cls):
        return cls.from_database(cls._DATABASE["ToupTek_ATR3CMOS16000KPA"])

    @classmethod
    def ToupTek_ATR3CMOS02000KMA(cls):
        return cls.from_database(cls._DATABASE["ToupTek_ATR3CMOS02000KMA"])

    @classmethod
    def ToupTek_ATR3CMOS06300KPA(cls):
        return cls.from_database(cls._DATABASE["ToupTek_ATR3CMOS06300KPA"])

    @classmethod
    def ToupTek_ATR3CMOS26000KMA(cls):
        return cls.from_database(cls._DATABASE["ToupTek_ATR3CMOS26000KMA"])

    @classmethod
    def ToupTek_ATR3CMOS07100KPA(cls):
        return cls.from_database(cls._DATABASE["ToupTek_ATR3CMOS07100KPA"])

    @classmethod
    def ToupTek_ATR3CMOS21000KPA(cls):
        return cls.from_database(cls._DATABASE["ToupTek_ATR3CMOS21000KPA"])

    @classmethod
    def ToupTek_GP_CMOS02000KMA(cls):
        return cls.from_database(cls._DATABASE["ToupTek_GP_CMOS02000KMA"])

    @classmethod
    def ToupTek_GP_CMOS02900KPA(cls):
        return cls.from_database(cls._DATABASE["ToupTek_GP_CMOS02900KPA"])

    @classmethod
    def ToupTek_GP_CMOS04600KPA(cls):
        return cls.from_database(cls._DATABASE["ToupTek_GP_CMOS04600KPA"])

    @classmethod
    def ToupTek_ATR3CMOS09440KPA(cls):
        return cls.from_database(cls._DATABASE["ToupTek_ATR3CMOS09440KPA"])

    @classmethod
    def ToupTek_ATR3CMOS04600KPA(cls):
        return cls.from_database(cls._DATABASE["ToupTek_ATR3CMOS04600KPA"])

    @classmethod
    def ToupTek_ATR3CMOS12000KPA(cls):
        return cls.from_database(cls._DATABASE["ToupTek_ATR3CMOS12000KPA"])

    @classmethod
    def ToupTek_ATR3CMOS09120KPA(cls):
        return cls.from_database(cls._DATABASE["ToupTek_ATR3CMOS09120KPA"])

    @classmethod
    def ToupTek_ATR3CMOS02100KPA(cls):
        return cls.from_database(cls._DATABASE["ToupTek_ATR3CMOS02100KPA"])

    @classmethod
    def ToupTek_ATR3CMOS08000KPA(cls):
        return cls.from_database(cls._DATABASE["ToupTek_ATR3CMOS08000KPA"])

    @classmethod
    def ToupTek_GCMOS01200KPA(cls):
        return cls.from_database(cls._DATABASE["ToupTek_GCMOS01200KPA"])

    @classmethod
    def ToupTek_GCMOS01200KMA(cls):
        return cls.from_database(cls._DATABASE["ToupTek_GCMOS01200KMA"])

    @classmethod
    def ToupTek_ATR3CMOS16000KMA(cls):
        return cls.from_database(cls._DATABASE["ToupTek_ATR3CMOS16000KMA"])

    @classmethod
    def ToupTek_ATR3CMOS02900KPA(cls):
        return cls.from_database(cls._DATABASE["ToupTek_ATR3CMOS02900KPA"])

    @classmethod
    def ToupTek_ATR3CMOS04600KMA(cls):
        return cls.from_database(cls._DATABASE["ToupTek_ATR3CMOS04600KMA"])

    @classmethod
    def ToupTek_ATR3CMOS09440KMA(cls):
        return cls.from_database(cls._DATABASE["ToupTek_ATR3CMOS09440KMA"])

    @classmethod
    def ToupTek_ATR3CMOS12000KMA(cls):
        return cls.from_database(cls._DATABASE["ToupTek_ATR3CMOS12000KMA"])

    @classmethod
    def ToupTek_ATR3CMOS09120KMA(cls):
        return cls.from_database(cls._DATABASE["ToupTek_ATR3CMOS09120KMA"])

    @classmethod
    def ToupTek_ATR3CMOS02100KMA(cls):
        return cls.from_database(cls._DATABASE["ToupTek_ATR3CMOS02100KMA"])

    @classmethod
    def ToupTek_ATR3CMOS08000KMA(cls):
        return cls.from_database(cls._DATABASE["ToupTek_ATR3CMOS08000KMA"])

    @classmethod
    def ToupTek_GP_CMOS01200KPA(cls):
        return cls.from_database(cls._DATABASE["ToupTek_GP_CMOS01200KPA"])

    @classmethod
    def ToupTek_GP_CMOS01200KMA(cls):
        return cls.from_database(cls._DATABASE["ToupTek_GP_CMOS01200KMA"])

    @classmethod
    def ToupTek_GP_CMOS05780KPA(cls):
        return cls.from_database(cls._DATABASE["ToupTek_GP_CMOS05780KPA"])

    @classmethod
    def ToupTek_GP_CMOS05780KMA(cls):
        return cls.from_database(cls._DATABASE["ToupTek_GP_CMOS05780KMA"])
