from ..base import Camera

class CelestronCamera(Camera):
    _DATABASE = {
        "Celestron_NexImage_10": {
            "brand": "Celestron",
            "name": "NexImage 10",
            "type": "type_camera",
            "optical_length": 12.5,
            "mass": 120,
            "tside_thread": "CS",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
            "sensor_width_mm": 6.4,
            "sensor_height_mm": 4.6,
            "width": 3856,
            "height": 2764,
            "pixel_size_um": 1.67,
            "quantum_efficiency_pct": 60,
            "read_noise_e": 2.0,
            "full_well_e": 5000,
        },
        "Celestron_NexImage_Burst": {
            "brand": "Celestron",
            "name": "NexImage Burst",
            "type": "type_camera",
            "optical_length": 10.6, # Verified via official Celestron documentation: 10.6mm (0.41") without nosepiece
            "mass": 57, # Verified via official Celestron documentation: 2.0 oz (57 g)
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
        "Celestron_NexImage_5": {
            "brand": "Celestron",
            "name": "NexImage 5",
            "type": "type_camera",
            "optical_length": 10.6, # Verified via official Celestron documentation: 10.6mm (0.41") without nosepiece
            "mass": 57, # Verified via official Celestron documentation: 2.0 oz (57 g)
            "tside_thread": "CS",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
            "sensor_width_mm": 5.7,
            "sensor_height_mm": 4.28, # Verified via official Celestron documentation: 5.7mm x 4.28mm
            "width": 2592,
            "height": 1944,
            "pixel_size_um": 2.2,
            "quantum_efficiency_pct": 60,
            "read_noise_e": 2.5,
            "full_well_e": 7000,
        },
        "Celestron_Skyris_132M": {
            "brand": "Celestron",
            "name": "Skyris 132M",
            "type": "type_camera",
            "optical_length": 17.5, # Verified via official Celestron documentation: 17.5mm (0.68") with C-mount / without nosepiece
            "mass": 102, # Verified via official Celestron documentation: 3.6 oz (102 g)
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
        "Celestron_Skyris_236M": {
            "brand": "Celestron",
            "name": "Skyris 236M",
            "type": "type_camera",
            "optical_length": 17.5, # Verified via official Celestron documentation: 17.5mm (0.68") with C-mount / without nosepiece
            "mass": 102, # Verified via official Celestron documentation: 3.6 oz (102 g)
            "tside_thread": "CS",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
            "sensor_width_mm": 5.4,
            "sensor_height_mm": 3.4,
            "width": 1920,
            "height": 1200,
            "pixel_size_um": 2.8,
            "quantum_efficiency_pct": 80,
            "read_noise_e": 1.0,
            "full_well_e": 15000,
        },
        "Celestron_Skyris_618M": {
            "brand": "Celestron",
            "name": "Skyris 618M",
            "type": "type_camera",
            "optical_length": 17.5, # Verified via official Celestron documentation: 17.5mm (0.68") with C-mount / without nosepiece
            "mass": 102, # Verified via official Celestron / TIS documentation: 3.6 oz (102 g)
            "tside_thread": "CS",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
            "sensor_width_mm": 3.6,
            "sensor_height_mm": 2.7,
            "width": 640,
            "height": 480,
            "pixel_size_um": 5.6,
            "quantum_efficiency_pct": 65,
            "read_noise_e": 5.0,
            "full_well_e": 20000,
        },
        "Celestron_Skyris_445M": {
            "brand": "Celestron",
            "name": "Skyris 445M",
            "type": "type_camera",
            "optical_length": 17.5, # Verified via official Celestron documentation: 17.5mm (0.68") with C-mount / without nosepiece
            "mass": 102, # Verified via official Celestron / TIS documentation: 3.6 oz (102 g)
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
            "quantum_efficiency_pct": 70,
            "read_noise_e": 4.0,
            "full_well_e": 15000,
        },
        "Celestron_Skyris_274M": {
            "brand": "Celestron",
            "name": "Skyris 274M",
            "type": "type_camera",
            "optical_length": 17.5, # Verified via official Celestron documentation: 17.5mm (0.68") with C-mount / without nosepiece
            "mass": 102, # Verified via official Celestron / TIS documentation: 3.6 oz (102 g)
            "tside_thread": "CS",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
            "sensor_width_mm": 8.5, # Verified via official Celestron documentation: Sony ICX274 sensor size is 8.50mm x 6.80mm
            "sensor_height_mm": 6.8, # Verified via official Celestron documentation: Sony ICX274 sensor size is 8.50mm x 6.80mm
            "width": 1600,
            "height": 1200,
            "pixel_size_um": 4.4,
            "quantum_efficiency_pct": 55,
            "read_noise_e": 5.0,
            "full_well_e": 40000,
        },
    }

    @classmethod
    def Celestron_NexImage_10(cls):
        return cls.from_database(cls._DATABASE['Celestron_NexImage_10'])

    @classmethod
    def Celestron_NexImage_Burst(cls):
        return cls.from_database(cls._DATABASE['Celestron_NexImage_Burst'])

    @classmethod
    def Celestron_NexImage_5(cls):
        return cls.from_database(cls._DATABASE['Celestron_NexImage_5'])

    @classmethod
    def Celestron_Skyris_132M(cls):
        return cls.from_database(cls._DATABASE['Celestron_Skyris_132M'])

    @classmethod
    def Celestron_Skyris_236M(cls):
        return cls.from_database(cls._DATABASE['Celestron_Skyris_236M'])

    @classmethod
    def Celestron_Skyris_618M(cls):
        return cls.from_database(cls._DATABASE['Celestron_Skyris_618M'])

    @classmethod
    def Celestron_Skyris_445M(cls):
        return cls.from_database(cls._DATABASE['Celestron_Skyris_445M'])

    @classmethod
    def Celestron_Skyris_274M(cls):
        return cls.from_database(cls._DATABASE['Celestron_Skyris_274M'])
