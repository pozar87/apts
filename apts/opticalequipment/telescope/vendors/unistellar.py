from ..base import Telescope


class UnistellarTelescope(Telescope):
    _DATABASE = {
        "Unistellar_eVscope": {
            "brand": "Unistellar",
            "name": "eVscope",
            "type": "type_smart_telescope",
            "aperture": 114,
            "focal_length": 450,
            "sensor_width": 4.8,
            "sensor_height": 3.6,
            "width": 1280,
            "height": 960,
            "pixel_size_um": 3.75,
            "read_noise_e": 1.0,
            "quantum_efficiency_pct": 80,
            "full_well_e": 13000,
            "mass": 7000,
        },
        "Unistellar_eQuinox": {
            "brand": "Unistellar",
            "name": "eQuinox",
            "type": "type_smart_telescope",
            "aperture": 114,
            "focal_length": 450,
            "sensor_width": 4.8,
            "sensor_height": 3.6,
            "width": 1280,
            "height": 960,
            "pixel_size_um": 3.75,
            "read_noise_e": 1.0,
            "quantum_efficiency_pct": 80,
            "full_well_e": 13000,
            "mass": 7000,
        },
        "Unistellar_eVscope_2": {
            "brand": "Unistellar",
            "name": "eVscope 2",
            "type": "type_smart_telescope",
            "aperture": 114,
            "focal_length": 450,
            "sensor_width": 9.28,
            "sensor_height": 6.96,
            "width": 3200,
            "height": 2400,
            "pixel_size_um": 2.9,
            "read_noise_e": 0.8,
            "quantum_efficiency_pct": 91,
            "full_well_e": 40000,
            "mass": 7000,
        },
        "Unistellar_eQuinox_2": {
            "brand": "Unistellar",
            "name": "eQuinox 2",
            "type": "type_smart_telescope",
            "aperture": 114,
            "focal_length": 450,
            "sensor_width": 8.91,
            "sensor_height": 5.94,
            "width": 3072,
            "height": 2048,
            "pixel_size_um": 2.9,
            "read_noise_e": 0.8,
            "quantum_efficiency_pct": 91,
            "full_well_e": 40000,
            "mass": 7000,
        },
        "Unistellar_Odyssey": {
            "brand": "Unistellar",
            "name": "Odyssey",
            "type": "type_smart_telescope",
            "aperture": 85,
            "focal_length": 320,
            "sensor_width": 4.48,
            "sensor_height": 3.0,
            "width": 3088,
            "height": 2072,
            "pixel_size_um": 1.45,
            "read_noise_e": 0.5,
            "quantum_efficiency_pct": 80,
            "full_well_e": 12000,
            "mass": 4000,
        },
        "Unistellar_Odyssey_Pro": {
            "brand": "Unistellar",
            "name": "Odyssey Pro",
            "type": "type_smart_telescope",
            "aperture": 85,
            "focal_length": 320,
            "sensor_width": 4.48,
            "sensor_height": 3.0,
            "width": 3088,
            "height": 2072,
            "pixel_size_um": 1.45,
            "read_noise_e": 0.5,
            "quantum_efficiency_pct": 80,
            "full_well_e": 12000,
            "mass": 4000,
        },
    }

    @classmethod
    def Unistellar_eVscope(cls):
        from ...smart_telescope import SmartTelescope

        return SmartTelescope.from_database(cls._DATABASE["Unistellar_eVscope"])

    @classmethod
    def Unistellar_eQuinox(cls):
        from ...smart_telescope import SmartTelescope

        return SmartTelescope.from_database(cls._DATABASE["Unistellar_eQuinox"])

    @classmethod
    def Unistellar_eVscope_2(cls):
        from ...smart_telescope import SmartTelescope

        return SmartTelescope.from_database(cls._DATABASE["Unistellar_eVscope_2"])

    @classmethod
    def Unistellar_eQuinox_2(cls):
        from ...smart_telescope import SmartTelescope

        return SmartTelescope.from_database(cls._DATABASE["Unistellar_eQuinox_2"])

    @classmethod
    def Unistellar_Odyssey(cls):
        from ...smart_telescope import SmartTelescope

        return SmartTelescope.from_database(cls._DATABASE["Unistellar_Odyssey"])

    @classmethod
    def Unistellar_Odyssey_Pro(cls):
        from ...smart_telescope import SmartTelescope

        return SmartTelescope.from_database(cls._DATABASE["Unistellar_Odyssey_Pro"])
