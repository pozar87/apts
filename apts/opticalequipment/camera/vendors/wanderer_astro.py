from ..base import Camera


class Wanderer_astroCamera(Camera):
    _DATABASE = {
        "Wanderer_Astro_WanderCam_585C": {
            "brand": "Wanderer Astro",
            "name": "WanderCam 585C",
            "type": "type_camera",
            "optical_length": 6.5,
            "mass": 160,
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
        }
    }

    @classmethod
    def Wanderer_Astro_WanderCam_585C(cls):
        return cls.from_database(cls._DATABASE["Wanderer_Astro_WanderCam_585C"])
