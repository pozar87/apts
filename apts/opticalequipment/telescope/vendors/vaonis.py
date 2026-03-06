from ..base import Telescope

class VaonisTelescope(Telescope):
    _DATABASE = {
        "Vaonis_Stellina": {
            "brand": "Vaonis",
            "name": "Stellina",
            "type": "type_smart_telescope",
            "aperture": 80,
            "focal_length": 400,
            "sensor_width": 7.43,
            "sensor_height": 4.99,
            "width": 3096,
            "height": 2080,
            "mass": 11200,
            "pixel_size_um": 2.4,
            "quantum_efficiency_pct": 80,
            "read_noise_e": 1.4,
            "full_well_e": 15000,
        },
        "Vaonis_Vespera": {
            "brand": "Vaonis",
            "name": "Vespera",
            "type": "type_smart_telescope",
            "aperture": 50,
            "focal_length": 200,
            "sensor_width": 5.57,
            "sensor_height": 3.13,
            "width": 1920,
            "height": 1080,
            "mass": 5000,
            "pixel_size_um": 2.9,
            "quantum_efficiency_pct": 80,
            "read_noise_e": 0.5,
            "full_well_e": 12000,
        },
        "Vaonis_Vespera_II": {
            "brand": "Vaonis",
            "name": "Vespera II",
            "type": "type_smart_telescope",
            "aperture": 50,
            "focal_length": 250,
            "sensor_width": 11.14,
            "sensor_height": 6.26,
            "width": 3840,
            "height": 2160,
            "mass": 5000,
            "pixel_size_um": 2.9,
            "quantum_efficiency_pct": 91,
            "read_noise_e": 0.6,
            "full_well_e": 40000,
        },
        "Vaonis_Vespera_Pro": {
            "brand": "Vaonis",
            "name": "Vespera Pro",
            "type": "type_smart_telescope",
            "aperture": 50,
            "focal_length": 250,
            "sensor_width": 7.07,
            "sensor_height": 7.07,
            "width": 3536,
            "height": 3536,
            "mass": 5000,
            "pixel_size_um": 2.0,
            "quantum_efficiency_pct": 83,
            "read_noise_e": 0.6,
            "full_well_e": 10550,
        },
        "Vaonis_Hyperia": {
            "brand": "Vaonis",
            "name": "Hyperia",
            "type": "type_smart_telescope",
            "aperture": 150,
            "focal_length": 1050,
            "sensor_width": 36.0,
            "sensor_height": 24.0,
            "width": 9576,
            "height": 6388,
            "mass": 75000,
            "pixel_size_um": 3.76,
            "quantum_efficiency_pct": 91,
            "read_noise_e": 1.2,
            "full_well_e": 51000,
        },
    }

    @classmethod
    def Vaonis_Stellina(cls):
        from ...smart_telescope import SmartTelescope

        return SmartTelescope.from_database(cls._DATABASE["Vaonis_Stellina"])

    @classmethod
    def Vaonis_Vespera(cls):
        from ...smart_telescope import SmartTelescope

        return SmartTelescope.from_database(cls._DATABASE["Vaonis_Vespera"])

    @classmethod
    def Vaonis_Vespera_II(cls):
        from ...smart_telescope import SmartTelescope

        return SmartTelescope.from_database(cls._DATABASE["Vaonis_Vespera_II"])

    @classmethod
    def Vaonis_Vespera_Pro(cls):
        from ...smart_telescope import SmartTelescope

        return SmartTelescope.from_database(cls._DATABASE["Vaonis_Vespera_Pro"])

    @classmethod
    def Vaonis_Hyperia(cls):
        from ...smart_telescope import SmartTelescope

        return SmartTelescope.from_database(cls._DATABASE["Vaonis_Hyperia"])