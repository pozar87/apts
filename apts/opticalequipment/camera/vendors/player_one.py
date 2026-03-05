from ..base import Camera


class Player_oneCamera(Camera):
    _DATABASE = {
        "Player_One_Poseidon_C_Pro": {
            "brand": "Player One",
            "name": "Poseidon-C Pro",
            "type": "type_camera",
            "sensor_width_mm": 23.5,
            "sensor_height_mm": 15.7,
            "width": 6252,
            "height": 4176,
            "pixel_size_um": 3.76,
            "full_well_e": 71700,
            "read_noise_e": 1.0,
            "quantum_efficiency_pct": 81,
            "optical_length": 17.5,
            "mass": 650,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Poseidon_M_Pro": {
            "brand": "Player One",
            "name": "Poseidon-M Pro",
            "type": "type_camera",
            "sensor_width_mm": 23.5,
            "sensor_height_mm": 15.7,
            "width": 6252,
            "height": 4176,
            "pixel_size_um": 3.76,
            "full_well_e": 71700,
            "read_noise_e": 1.0,
            "quantum_efficiency_pct": 91,
            "optical_length": 17.5,
            "mass": 650,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Artemis_C_Pro": {
            "brand": "Player One",
            "name": "Artemis-C Pro",
            "type": "type_camera",
            "sensor_width_mm": 19.1,
            "sensor_height_mm": 13.0,
            "width": 4144,
            "height": 2822,
            "pixel_size_um": 4.63,
            "full_well_e": 63700,
            "read_noise_e": 1.2,
            "quantum_efficiency_pct": 75,
            "optical_length": 17.5,
            "mass": 750,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Artemis_M_Pro": {
            "brand": "Player One",
            "name": "Artemis-M Pro",
            "type": "type_camera",
            "sensor_width_mm": 19.1,
            "sensor_height_mm": 13.0,
            "width": 4144,
            "height": 2822,
            "pixel_size_um": 4.63,
            "full_well_e": 66000,
            "read_noise_e": 1.2,
            "quantum_efficiency_pct": 90,
            "optical_length": 17.5,
            "mass": 750,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Ares_C_Pro": {
            "brand": "Player One",
            "name": "Ares-C Pro",
            "type": "type_camera",
            "sensor_width_mm": 11.31,
            "sensor_height_mm": 11.31,
            "width": 3008,
            "height": 3008,
            "pixel_size_um": 3.76,
            "full_well_e": 50000,
            "read_noise_e": 1.0,
            "quantum_efficiency_pct": 80,
            "optical_length": 17.5,
            "mass": 800,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Ares_M_Pro": {
            "brand": "Player One",
            "name": "Ares-M Pro",
            "type": "type_camera",
            "sensor_width_mm": 11.31,
            "sensor_height_mm": 11.31,
            "width": 3008,
            "height": 3008,
            "pixel_size_um": 3.76,
            "full_well_e": 50000,
            "read_noise_e": 1.0,
            "quantum_efficiency_pct": 91,
            "optical_length": 17.5,
            "mass": 800,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Apollo_MAX_C_Pro": {
            "brand": "Player One",
            "name": "Apollo-MAX-C Pro",
            "type": "type_camera",
            "sensor_width_mm": 14.5,
            "sensor_height_mm": 9.9,
            "width": 1608,
            "height": 1104,
            "pixel_size_um": 9.0,
            "full_well_e": 100000,
            "read_noise_e": 2.4,
            "quantum_efficiency_pct": 79,
            "optical_length": 17.5,
            "mass": 1000,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Apollo_MAX_M_Pro": {
            "brand": "Player One",
            "name": "Apollo-MAX-M Pro",
            "type": "type_camera",
            "sensor_width_mm": 14.5,
            "sensor_height_mm": 9.9,
            "width": 1608,
            "height": 1104,
            "pixel_size_um": 9.0,
            "full_well_e": 100000,
            "read_noise_e": 2.4,
            "quantum_efficiency_pct": 79,
            "optical_length": 17.5,
            "mass": 1000,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Zeus_C_Pro": {
            "brand": "Player One",
            "name": "Zeus-C Pro",
            "type": "type_camera",
            "sensor_width_mm": 36.0,
            "sensor_height_mm": 24.0,
            "width": 9576,
            "height": 6388,
            "pixel_size_um": 3.76,
            "full_well_e": 51000,
            "read_noise_e": 1.2,
            "quantum_efficiency_pct": 80,
            "optical_length": 17.5,
            "mass": 500,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Zeus_M_Pro": {
            "brand": "Player One",
            "name": "Zeus-M Pro",
            "type": "type_camera",
            "sensor_width_mm": 36.0,
            "sensor_height_mm": 24.0,
            "width": 9576,
            "height": 6388,
            "pixel_size_um": 3.76,
            "full_well_e": 51000,
            "read_noise_e": 1.2,
            "quantum_efficiency_pct": 91,
            "optical_length": 17.5,
            "mass": 500,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Hades_C_Pro": {
            "brand": "Player One",
            "name": "Hades-C Pro",
            "type": "type_camera",
            "sensor_width_mm": 14.7,
            "sensor_height_mm": 10.2,
            "width": 1944,
            "height": 1472,
            "pixel_size_um": 7.12,
            "full_well_e": 100000,
            "read_noise_e": 3.5,
            "quantum_efficiency_pct": 77,
            "optical_length": 17.5,
            "mass": 470,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Hades_M_Pro": {
            "brand": "Player One",
            "name": "Hades-M Pro",
            "type": "type_camera",
            "sensor_width_mm": 14.7,
            "sensor_height_mm": 10.2,
            "width": 1944,
            "height": 1472,
            "pixel_size_um": 7.12,
            "full_well_e": 100000,
            "read_noise_e": 3.5,
            "quantum_efficiency_pct": 77,
            "optical_length": 17.5,
            "mass": 470,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Athena_C_Pro": {
            "brand": "Player One",
            "name": "Athena-C Pro",
            "type": "type_camera",
            "sensor_width_mm": 5.6,
            "sensor_height_mm": 3.2,
            "width": 1920,
            "height": 1080,
            "pixel_size_um": 2.9,
            "full_well_e": 12000,
            "read_noise_e": 0.5,
            "quantum_efficiency_pct": 91,
            "optical_length": 17.5,
            "mass": 430,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Athena_M_Pro": {
            "brand": "Player One",
            "name": "Athena-M Pro",
            "type": "type_camera",
            "sensor_width_mm": 5.6,
            "sensor_height_mm": 3.2,
            "width": 1920,
            "height": 1080,
            "pixel_size_um": 2.9,
            "full_well_e": 12000,
            "read_noise_e": 0.5,
            "quantum_efficiency_pct": 91,
            "optical_length": 17.5,
            "mass": 430,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Ceres_C_Pro": {
            "brand": "Player One",
            "name": "Ceres-C Pro",
            "type": "type_camera",
            "sensor_width_mm": 4.8,
            "sensor_height_mm": 3.6,
            "width": 1304,
            "height": 976,
            "pixel_size_um": 3.75,
            "full_well_e": 19000,
            "read_noise_e": 0.75,
            "quantum_efficiency_pct": 75,
            "optical_length": 17.5,
            "mass": 350,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Ceres_M_Pro": {
            "brand": "Player One",
            "name": "Ceres-M Pro",
            "type": "type_camera",
            "sensor_width_mm": 5.6,
            "sensor_height_mm": 3.2,
            "width": 1936,
            "height": 1096,
            "pixel_size_um": 2.9,
            "full_well_e": 14600,
            "read_noise_e": 1.0,
            "quantum_efficiency_pct": 80,
            "optical_length": 17.5,
            "mass": 350,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Ceres_C": {
            "brand": "Player One",
            "name": "Ceres-C",
            "type": "type_camera",
            "sensor_width_mm": 4.8,
            "sensor_height_mm": 3.6,
            "width": 1304,
            "height": 976,
            "pixel_size_um": 3.75,
            "full_well_e": 19000,
            "read_noise_e": 0.75,
            "quantum_efficiency_pct": 75,
            "optical_length": 6.5,
            "mass": 150,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Ceres_M": {
            "brand": "Player One",
            "name": "Ceres-M",
            "type": "type_camera",
            "sensor_width_mm": 5.6,
            "sensor_height_mm": 3.2,
            "width": 1936,
            "height": 1096,
            "pixel_size_um": 2.9,
            "full_well_e": 14600,
            "read_noise_e": 1.0,
            "quantum_efficiency_pct": 80,
            "optical_length": 6.5,
            "mass": 150,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Neptune_II_C": {
            "brand": "Player One",
            "name": "Neptune-II-C",
            "type": "type_camera",
            "sensor_width_mm": 7.9,
            "sensor_height_mm": 4.5,
            "width": 2712,
            "height": 1538,
            "pixel_size_um": 2.9,
            "full_well_e": 12000,
            "read_noise_e": 0.7,
            "quantum_efficiency_pct": 80,
            "optical_length": 6.5,
            "mass": 120,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Neptune_II_M": {
            "brand": "Player One",
            "name": "Neptune-II-M",
            "type": "type_camera",
            "sensor_width_mm": 7.9,
            "sensor_height_mm": 4.5,
            "width": 2712,
            "height": 1538,
            "pixel_size_um": 2.9,
            "full_well_e": 12000,
            "read_noise_e": 0.7,
            "quantum_efficiency_pct": 80,
            "optical_length": 6.5,
            "mass": 120,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Saturn_C": {
            "brand": "Player One",
            "name": "Saturn-C",
            "type": "type_camera",
            "sensor_width_mm": 11.31,
            "sensor_height_mm": 11.31,
            "width": 3008,
            "height": 3008,
            "pixel_size_um": 3.76,
            "full_well_e": 50000,
            "read_noise_e": 1.0,
            "quantum_efficiency_pct": 80,
            "optical_length": 6.5,
            "mass": 130,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Saturn_M": {
            "brand": "Player One",
            "name": "Saturn-M",
            "type": "type_camera",
            "sensor_width_mm": 11.31,
            "sensor_height_mm": 11.31,
            "width": 3008,
            "height": 3008,
            "pixel_size_um": 3.76,
            "full_well_e": 50000,
            "read_noise_e": 1.0,
            "quantum_efficiency_pct": 91,
            "optical_length": 6.5,
            "mass": 130,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Uranus_C": {
            "brand": "Player One",
            "name": "Uranus-C",
            "type": "type_camera",
            "sensor_width_mm": 11.13,
            "sensor_height_mm": 6.26,
            "width": 3840,
            "height": 2160,
            "pixel_size_um": 2.9,
            "full_well_e": 40000,
            "read_noise_e": 0.6,
            "quantum_efficiency_pct": 91,
            "optical_length": 6.5,
            "mass": 140,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Uranus_M": {
            "brand": "Player One",
            "name": "Uranus-M",
            "type": "type_camera",
            "sensor_width_mm": 11.13,
            "sensor_height_mm": 6.26,
            "width": 3840,
            "height": 2160,
            "pixel_size_um": 2.9,
            "full_well_e": 40000,
            "read_noise_e": 0.6,
            "quantum_efficiency_pct": 91,
            "optical_length": 6.5,
            "mass": 140,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Mars_II_C": {
            "brand": "Player One",
            "name": "Mars-II-C",
            "type": "type_camera",
            "sensor_width_mm": 5.6,
            "sensor_height_mm": 3.2,
            "width": 1920,
            "height": 1080,
            "pixel_size_um": 2.9,
            "full_well_e": 12000,
            "read_noise_e": 0.5,
            "quantum_efficiency_pct": 91,
            "optical_length": 12.5,
            "mass": 60,
            "tside_thread": "CS",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Mars_II_M": {
            "brand": "Player One",
            "name": "Mars-II-M",
            "type": "type_camera",
            "sensor_width_mm": 5.6,
            "sensor_height_mm": 3.2,
            "width": 1920,
            "height": 1080,
            "pixel_size_um": 2.9,
            "full_well_e": 12000,
            "read_noise_e": 0.5,
            "quantum_efficiency_pct": 91,
            "optical_length": 12.5,
            "mass": 60,
            "tside_thread": "CS",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Mercury_C": {
            "brand": "Player One",
            "name": "Mercury-C",
            "type": "type_camera",
            "sensor_width_mm": 7.68,
            "sensor_height_mm": 4.32,
            "width": 3840,
            "height": 2160,
            "pixel_size_um": 2.0,
            "full_well_e": 10000,
            "read_noise_e": 0.6,
            "quantum_efficiency_pct": 80,
            "optical_length": 12.5,
            "mass": 55,
            "tside_thread": "CS",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Mercury_M": {
            "brand": "Player One",
            "name": "Mercury-M",
            "type": "type_camera",
            "sensor_width_mm": 7.68,
            "sensor_height_mm": 4.32,
            "width": 3840,
            "height": 2160,
            "pixel_size_um": 2.0,
            "full_well_e": 10000,
            "read_noise_e": 0.6,
            "quantum_efficiency_pct": 80,
            "optical_length": 12.5,
            "mass": 55,
            "tside_thread": "CS",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Jupiter_C": {
            "brand": "Player One",
            "name": "Jupiter-C",
            "type": "type_camera",
            "sensor_width_mm": 11.13,
            "sensor_height_mm": 6.26,
            "width": 3840,
            "height": 2160,
            "pixel_size_um": 2.9,
            "full_well_e": 13000,
            "read_noise_e": 1.0,
            "quantum_efficiency_pct": 85,
            "optical_length": 12.5,
            "mass": 120,
            "tside_thread": "CS",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Jupiter_M": {
            "brand": "Player One",
            "name": "Jupiter-M",
            "type": "type_camera",
            "sensor_width_mm": 11.13,
            "sensor_height_mm": 6.26,
            "width": 3840,
            "height": 2160,
            "pixel_size_um": 2.9,
            "full_well_e": 13000,
            "read_noise_e": 1.0,
            "quantum_efficiency_pct": 85,
            "optical_length": 12.5,
            "mass": 120,
            "tside_thread": "CS",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Luna_C": {
            "brand": "Player One",
            "name": "Luna-C",
            "type": "type_camera",
            "sensor_width_mm": 5.6,
            "sensor_height_mm": 3.2,
            "width": 1920,
            "height": 1080,
            "pixel_size_um": 2.9,
            "full_well_e": 12000,
            "read_noise_e": 0.5,
            "quantum_efficiency_pct": 91,
            "optical_length": 12.5,
            "mass": 100,
            "tside_thread": "CS",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Luna_M": {
            "brand": "Player One",
            "name": "Luna-M",
            "type": "type_camera",
            "sensor_width_mm": 5.6,
            "sensor_height_mm": 3.2,
            "width": 1920,
            "height": 1080,
            "pixel_size_um": 2.9,
            "full_well_e": 12000,
            "read_noise_e": 0.5,
            "quantum_efficiency_pct": 91,
            "optical_length": 12.5,
            "mass": 100,
            "tside_thread": "CS",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Pluto_C": {
            "brand": "Player One",
            "name": "Pluto-C",
            "type": "type_camera",
            "sensor_width_mm": 14.5,
            "sensor_height_mm": 9.9,
            "width": 1608,
            "height": 1104,
            "pixel_size_um": 9.0,
            "full_well_e": 100000,
            "read_noise_e": 2.4,
            "quantum_efficiency_pct": 79,
            "optical_length": 12.5,
            "mass": 80,
            "tside_thread": "CS",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Pluto_M": {
            "brand": "Player One",
            "name": "Pluto-M",
            "type": "type_camera",
            "sensor_width_mm": 14.5,
            "sensor_height_mm": 9.9,
            "width": 1608,
            "height": 1104,
            "pixel_size_um": 9.0,
            "full_well_e": 100000,
            "read_noise_e": 2.4,
            "quantum_efficiency_pct": 79,
            "optical_length": 12.5,
            "mass": 80,
            "tside_thread": "CS",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Callisto_C": {
            "brand": "Player One",
            "name": "Callisto-C",
            "type": "type_camera",
            "sensor_width_mm": 14.7,
            "sensor_height_mm": 10.2,
            "width": 1944,
            "height": 1472,
            "pixel_size_um": 7.12,
            "full_well_e": 100000,
            "read_noise_e": 3.5,
            "quantum_efficiency_pct": 77,
            "optical_length": 12.5,
            "mass": 130,
            "tside_thread": "CS",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Callisto_M": {
            "brand": "Player One",
            "name": "Callisto-M",
            "type": "type_camera",
            "sensor_width_mm": 14.7,
            "sensor_height_mm": 10.2,
            "width": 1944,
            "height": 1472,
            "pixel_size_um": 7.12,
            "full_well_e": 100000,
            "read_noise_e": 3.5,
            "quantum_efficiency_pct": 77,
            "optical_length": 12.5,
            "mass": 130,
            "tside_thread": "CS",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Io_C": {
            "brand": "Player One",
            "name": "Io-C",
            "type": "type_camera",
            "sensor_width_mm": 5.6,
            "sensor_height_mm": 3.2,
            "width": 1920,
            "height": 1080,
            "pixel_size_um": 2.9,
            "full_well_e": 12000,
            "read_noise_e": 0.5,
            "quantum_efficiency_pct": 91,
            "optical_length": 12.5,
            "mass": 95,
            "tside_thread": "CS",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Io_M": {
            "brand": "Player One",
            "name": "Io-M",
            "type": "type_camera",
            "sensor_width_mm": 5.6,
            "sensor_height_mm": 3.2,
            "width": 1920,
            "height": 1080,
            "pixel_size_um": 2.9,
            "full_well_e": 12000,
            "read_noise_e": 0.5,
            "quantum_efficiency_pct": 91,
            "optical_length": 12.5,
            "mass": 95,
            "tside_thread": "CS",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Ganymede_C": {
            "brand": "Player One",
            "name": "Ganymede-C",
            "type": "type_camera",
            "sensor_width_mm": 5.6,
            "sensor_height_mm": 3.2,
            "width": 1920,
            "height": 1080,
            "pixel_size_um": 2.9,
            "full_well_e": 12000,
            "read_noise_e": 0.5,
            "quantum_efficiency_pct": 91,
            "optical_length": 12.5,
            "mass": 110,
            "tside_thread": "CS",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Ganymede_M": {
            "brand": "Player One",
            "name": "Ganymede-M",
            "type": "type_camera",
            "sensor_width_mm": 5.6,
            "sensor_height_mm": 3.2,
            "width": 1920,
            "height": 1080,
            "pixel_size_um": 2.9,
            "full_well_e": 12000,
            "read_noise_e": 0.5,
            "quantum_efficiency_pct": 91,
            "optical_length": 12.5,
            "mass": 110,
            "tside_thread": "CS",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Titan_C": {
            "brand": "Player One",
            "name": "Titan-C",
            "type": "type_camera",
            "sensor_width_mm": 5.6,
            "sensor_height_mm": 3.2,
            "width": 1920,
            "height": 1080,
            "pixel_size_um": 2.9,
            "full_well_e": 12000,
            "read_noise_e": 0.5,
            "quantum_efficiency_pct": 91,
            "optical_length": 12.5,
            "mass": 140,
            "tside_thread": "CS",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Titan_M": {
            "brand": "Player One",
            "name": "Titan-M",
            "type": "type_camera",
            "sensor_width_mm": 5.6,
            "sensor_height_mm": 3.2,
            "width": 1920,
            "height": 1080,
            "pixel_size_um": 2.9,
            "full_well_e": 12000,
            "read_noise_e": 0.5,
            "quantum_efficiency_pct": 91,
            "optical_length": 12.5,
            "mass": 140,
            "tside_thread": "CS",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Triton_C": {
            "brand": "Player One",
            "name": "Triton-C",
            "type": "type_camera",
            "sensor_width_mm": 5.6,
            "sensor_height_mm": 3.2,
            "width": 1920,
            "height": 1080,
            "pixel_size_um": 2.9,
            "full_well_e": 12000,
            "read_noise_e": 0.5,
            "quantum_efficiency_pct": 91,
            "optical_length": 12.5,
            "mass": 125,
            "tside_thread": "CS",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Triton_M": {
            "brand": "Player One",
            "name": "Triton-M",
            "type": "type_camera",
            "sensor_width_mm": 5.6,
            "sensor_height_mm": 3.2,
            "width": 1920,
            "height": 1080,
            "pixel_size_um": 2.9,
            "full_well_e": 12000,
            "read_noise_e": 0.5,
            "quantum_efficiency_pct": 91,
            "optical_length": 12.5,
            "mass": 125,
            "tside_thread": "CS",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Charon_C": {
            "brand": "Player One",
            "name": "Charon-C",
            "type": "type_camera",
            "sensor_width_mm": 5.6,
            "sensor_height_mm": 3.2,
            "width": 1920,
            "height": 1080,
            "pixel_size_um": 2.9,
            "full_well_e": 12000,
            "read_noise_e": 0.5,
            "quantum_efficiency_pct": 91,
            "optical_length": 12.5,
            "mass": 85,
            "tside_thread": "CS",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Charon_M": {
            "brand": "Player One",
            "name": "Charon-M",
            "type": "type_camera",
            "sensor_width_mm": 5.6,
            "sensor_height_mm": 3.2,
            "width": 1920,
            "height": 1080,
            "pixel_size_um": 2.9,
            "full_well_e": 12000,
            "read_noise_e": 0.5,
            "quantum_efficiency_pct": 91,
            "optical_length": 12.5,
            "mass": 85,
            "tside_thread": "CS",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Oberon_C": {
            "brand": "Player One",
            "name": "Oberon-C",
            "type": "type_camera",
            "sensor_width_mm": 5.6,
            "sensor_height_mm": 3.2,
            "width": 1920,
            "height": 1080,
            "pixel_size_um": 2.9,
            "full_well_e": 12000,
            "read_noise_e": 0.5,
            "quantum_efficiency_pct": 91,
            "optical_length": 12.5,
            "mass": 115,
            "tside_thread": "CS",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Oberon_M": {
            "brand": "Player One",
            "name": "Oberon-M",
            "type": "type_camera",
            "sensor_width_mm": 5.6,
            "sensor_height_mm": 3.2,
            "width": 1920,
            "height": 1080,
            "pixel_size_um": 2.9,
            "full_well_e": 12000,
            "read_noise_e": 0.5,
            "quantum_efficiency_pct": 91,
            "optical_length": 12.5,
            "mass": 115,
            "tside_thread": "CS",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Poseidon_C_Pro_v2": {
            "brand": "Player One",
            "name": "Poseidon-C Pro v2",
            "type": "type_camera",
            "sensor_width_mm": 23.5,
            "sensor_height_mm": 15.7,
            "width": 6252,
            "height": 4176,
            "pixel_size_um": 3.76,
            "full_well_e": 71700,
            "read_noise_e": 1.0,
            "quantum_efficiency_pct": 81,
            "optical_length": 17.5,
            "mass": 470,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Artemis_C_Pro_v2": {
            "brand": "Player One",
            "name": "Artemis-C Pro v2",
            "type": "type_camera",
            "sensor_width_mm": 19.1,
            "sensor_height_mm": 13.0,
            "width": 4144,
            "height": 2822,
            "pixel_size_um": 4.63,
            "full_well_e": 63700,
            "read_noise_e": 1.2,
            "quantum_efficiency_pct": 75,
            "optical_length": 17.5,
            "mass": 760,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Ares_C_Pro_v2": {
            "brand": "Player One",
            "name": "Ares-C Pro v2",
            "type": "type_camera",
            "sensor_width_mm": 11.31,
            "sensor_height_mm": 11.31,
            "width": 3008,
            "height": 3008,
            "pixel_size_um": 3.76,
            "full_well_e": 50000,
            "read_noise_e": 1.0,
            "quantum_efficiency_pct": 80,
            "optical_length": 17.5,
            "mass": 810,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Zeus_C_Pro_v2": {
            "brand": "Player One",
            "name": "Zeus-C Pro v2",
            "type": "type_camera",
            "sensor_width_mm": 36.0,
            "sensor_height_mm": 24.0,
            "width": 9576,
            "height": 6388,
            "pixel_size_um": 3.76,
            "full_well_e": 51000,
            "read_noise_e": 1.2,
            "quantum_efficiency_pct": 80,
            "optical_length": 17.5,
            "mass": 510,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Hades_C_Pro_v2": {
            "brand": "Player One",
            "name": "Hades-C Pro v2",
            "type": "type_camera",
            "sensor_width_mm": 14.7,
            "sensor_height_mm": 10.2,
            "width": 1944,
            "height": 1472,
            "pixel_size_um": 7.12,
            "full_well_e": 100000,
            "read_noise_e": 3.5,
            "quantum_efficiency_pct": 77,
            "optical_length": 17.5,
            "mass": 480,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Athena_C_Pro_v2": {
            "brand": "Player One",
            "name": "Athena-C Pro v2",
            "type": "type_camera",
            "sensor_width_mm": 5.6,
            "sensor_height_mm": 3.2,
            "width": 1920,
            "height": 1080,
            "pixel_size_um": 2.9,
            "full_well_e": 12000,
            "read_noise_e": 0.5,
            "quantum_efficiency_pct": 91,
            "optical_length": 17.5,
            "mass": 440,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Poseidon_M_Pro_v2": {
            "brand": "Player One",
            "name": "Poseidon-M Pro v2",
            "type": "type_camera",
            "sensor_width_mm": 23.5,
            "sensor_height_mm": 15.7,
            "width": 6252,
            "height": 4176,
            "pixel_size_um": 3.76,
            "full_well_e": 71700,
            "read_noise_e": 1.0,
            "quantum_efficiency_pct": 91,
            "optical_length": 17.5,
            "mass": 470,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Artemis_M_Pro_v2": {
            "brand": "Player One",
            "name": "Artemis-M Pro v2",
            "type": "type_camera",
            "sensor_width_mm": 19.1,
            "sensor_height_mm": 13.0,
            "width": 4144,
            "height": 2822,
            "pixel_size_um": 4.63,
            "full_well_e": 66000,
            "read_noise_e": 1.2,
            "quantum_efficiency_pct": 90,
            "optical_length": 17.5,
            "mass": 760,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Ares_M_Pro_v2": {
            "brand": "Player One",
            "name": "Ares-M Pro v2",
            "type": "type_camera",
            "sensor_width_mm": 11.31,
            "sensor_height_mm": 11.31,
            "width": 3008,
            "height": 3008,
            "pixel_size_um": 3.76,
            "full_well_e": 50000,
            "read_noise_e": 1.0,
            "quantum_efficiency_pct": 91,
            "optical_length": 17.5,
            "mass": 810,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Zeus_M_Pro_v2": {
            "brand": "Player One",
            "name": "Zeus-M Pro v2",
            "type": "type_camera",
            "sensor_width_mm": 36.0,
            "sensor_height_mm": 24.0,
            "width": 9576,
            "height": 6388,
            "pixel_size_um": 3.76,
            "full_well_e": 51000,
            "read_noise_e": 1.2,
            "quantum_efficiency_pct": 91,
            "optical_length": 17.5,
            "mass": 510,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Hades_M_Pro_v2": {
            "brand": "Player One",
            "name": "Hades-M Pro v2",
            "type": "type_camera",
            "sensor_width_mm": 14.7,
            "sensor_height_mm": 10.2,
            "width": 1944,
            "height": 1472,
            "pixel_size_um": 7.12,
            "full_well_e": 100000,
            "read_noise_e": 3.5,
            "quantum_efficiency_pct": 77,
            "optical_length": 17.5,
            "mass": 480,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
        "Player_One_Athena_M_Pro_v2": {
            "brand": "Player One",
            "name": "Athena-M Pro v2",
            "type": "type_camera",
            "sensor_width_mm": 5.6,
            "sensor_height_mm": 3.2,
            "width": 1920,
            "height": 1080,
            "pixel_size_um": 2.9,
            "full_well_e": 12000,
            "read_noise_e": 0.5,
            "quantum_efficiency_pct": 91,
            "optical_length": 17.5,
            "mass": 440,
            "tside_thread": "M42",
            "tside_gender": "Female",
            "cside_thread": "",
            "cside_gender": "",
            "reversible": False,
            "bf_role": "end",
        },
    }

    @classmethod
    def Player_One_Poseidon_C_Pro(cls):
        return cls.from_database(cls._DATABASE["Player_One_Poseidon_C_Pro"])

    @classmethod
    def Player_One_Artemis_C_Pro(cls):
        return cls.from_database(cls._DATABASE["Player_One_Artemis_C_Pro"])

    @classmethod
    def Player_One_Ares_C_Pro(cls):
        return cls.from_database(cls._DATABASE["Player_One_Ares_C_Pro"])

    @classmethod
    def Player_One_Apollo_MAX_C_Pro(cls):
        return cls.from_database(cls._DATABASE["Player_One_Apollo_MAX_C_Pro"])

    @classmethod
    def Player_One_Zeus_C_Pro(cls):
        return cls.from_database(cls._DATABASE["Player_One_Zeus_C_Pro"])

    @classmethod
    def Player_One_Hades_C_Pro(cls):
        return cls.from_database(cls._DATABASE["Player_One_Hades_C_Pro"])

    @classmethod
    def Player_One_Athena_C_Pro(cls):
        return cls.from_database(cls._DATABASE["Player_One_Athena_C_Pro"])

    @classmethod
    def Player_One_Ceres_C_Pro(cls):
        return cls.from_database(cls._DATABASE["Player_One_Ceres_C_Pro"])

    @classmethod
    def Player_One_Poseidon_M_Pro(cls):
        return cls.from_database(cls._DATABASE["Player_One_Poseidon_M_Pro"])

    @classmethod
    def Player_One_Artemis_M_Pro(cls):
        return cls.from_database(cls._DATABASE["Player_One_Artemis_M_Pro"])

    @classmethod
    def Player_One_Ares_M_Pro(cls):
        return cls.from_database(cls._DATABASE["Player_One_Ares_M_Pro"])

    @classmethod
    def Player_One_Apollo_MAX_M_Pro(cls):
        return cls.from_database(cls._DATABASE["Player_One_Apollo_MAX_M_Pro"])

    @classmethod
    def Player_One_Zeus_M_Pro(cls):
        return cls.from_database(cls._DATABASE["Player_One_Zeus_M_Pro"])

    @classmethod
    def Player_One_Hades_M_Pro(cls):
        return cls.from_database(cls._DATABASE["Player_One_Hades_M_Pro"])

    @classmethod
    def Player_One_Athena_M_Pro(cls):
        return cls.from_database(cls._DATABASE["Player_One_Athena_M_Pro"])

    @classmethod
    def Player_One_Ceres_M_Pro(cls):
        return cls.from_database(cls._DATABASE["Player_One_Ceres_M_Pro"])

    @classmethod
    def Player_One_Ceres_C(cls):
        return cls.from_database(cls._DATABASE["Player_One_Ceres_C"])

    @classmethod
    def Player_One_Neptune_II_C(cls):
        return cls.from_database(cls._DATABASE["Player_One_Neptune_II_C"])

    @classmethod
    def Player_One_Saturn_C(cls):
        return cls.from_database(cls._DATABASE["Player_One_Saturn_C"])

    @classmethod
    def Player_One_Uranus_C(cls):
        return cls.from_database(cls._DATABASE["Player_One_Uranus_C"])

    @classmethod
    def Player_One_Mars_II_C(cls):
        return cls.from_database(cls._DATABASE["Player_One_Mars_II_C"])

    @classmethod
    def Player_One_Mercury_C(cls):
        return cls.from_database(cls._DATABASE["Player_One_Mercury_C"])

    @classmethod
    def Player_One_Ceres_M(cls):
        return cls.from_database(cls._DATABASE["Player_One_Ceres_M"])

    @classmethod
    def Player_One_Neptune_II_M(cls):
        return cls.from_database(cls._DATABASE["Player_One_Neptune_II_M"])

    @classmethod
    def Player_One_Saturn_M(cls):
        return cls.from_database(cls._DATABASE["Player_One_Saturn_M"])

    @classmethod
    def Player_One_Uranus_M(cls):
        return cls.from_database(cls._DATABASE["Player_One_Uranus_M"])

    @classmethod
    def Player_One_Mars_II_M(cls):
        return cls.from_database(cls._DATABASE["Player_One_Mars_II_M"])

    @classmethod
    def Player_One_Mercury_M(cls):
        return cls.from_database(cls._DATABASE["Player_One_Mercury_M"])

    @classmethod
    def Player_One_Jupiter_C(cls):
        return cls.from_database(cls._DATABASE["Player_One_Jupiter_C"])

    @classmethod
    def Player_One_Luna_C(cls):
        return cls.from_database(cls._DATABASE["Player_One_Luna_C"])

    @classmethod
    def Player_One_Pluto_C(cls):
        return cls.from_database(cls._DATABASE["Player_One_Pluto_C"])

    @classmethod
    def Player_One_Callisto_C(cls):
        return cls.from_database(cls._DATABASE["Player_One_Callisto_C"])

    @classmethod
    def Player_One_Io_C(cls):
        return cls.from_database(cls._DATABASE["Player_One_Io_C"])

    @classmethod
    def Player_One_Ganymede_C(cls):
        return cls.from_database(cls._DATABASE["Player_One_Ganymede_C"])

    @classmethod
    def Player_One_Titan_C(cls):
        return cls.from_database(cls._DATABASE["Player_One_Titan_C"])

    @classmethod
    def Player_One_Triton_C(cls):
        return cls.from_database(cls._DATABASE["Player_One_Triton_C"])

    @classmethod
    def Player_One_Charon_C(cls):
        return cls.from_database(cls._DATABASE["Player_One_Charon_C"])

    @classmethod
    def Player_One_Oberon_C(cls):
        return cls.from_database(cls._DATABASE["Player_One_Oberon_C"])

    @classmethod
    def Player_One_Jupiter_M(cls):
        return cls.from_database(cls._DATABASE["Player_One_Jupiter_M"])

    @classmethod
    def Player_One_Luna_M(cls):
        return cls.from_database(cls._DATABASE["Player_One_Luna_M"])

    @classmethod
    def Player_One_Pluto_M(cls):
        return cls.from_database(cls._DATABASE["Player_One_Pluto_M"])

    @classmethod
    def Player_One_Callisto_M(cls):
        return cls.from_database(cls._DATABASE["Player_One_Callisto_M"])

    @classmethod
    def Player_One_Io_M(cls):
        return cls.from_database(cls._DATABASE["Player_One_Io_M"])

    @classmethod
    def Player_One_Ganymede_M(cls):
        return cls.from_database(cls._DATABASE["Player_One_Ganymede_M"])

    @classmethod
    def Player_One_Titan_M(cls):
        return cls.from_database(cls._DATABASE["Player_One_Titan_M"])

    @classmethod
    def Player_One_Triton_M(cls):
        return cls.from_database(cls._DATABASE["Player_One_Triton_M"])

    @classmethod
    def Player_One_Charon_M(cls):
        return cls.from_database(cls._DATABASE["Player_One_Charon_M"])

    @classmethod
    def Player_One_Oberon_M(cls):
        return cls.from_database(cls._DATABASE["Player_One_Oberon_M"])

    @classmethod
    def Player_One_Poseidon_C_Pro_v2(cls):
        return cls.from_database(cls._DATABASE["Player_One_Poseidon_C_Pro_v2"])

    @classmethod
    def Player_One_Artemis_C_Pro_v2(cls):
        return cls.from_database(cls._DATABASE["Player_One_Artemis_C_Pro_v2"])

    @classmethod
    def Player_One_Ares_C_Pro_v2(cls):
        return cls.from_database(cls._DATABASE["Player_One_Ares_C_Pro_v2"])

    @classmethod
    def Player_One_Zeus_C_Pro_v2(cls):
        return cls.from_database(cls._DATABASE["Player_One_Zeus_C_Pro_v2"])

    @classmethod
    def Player_One_Hades_C_Pro_v2(cls):
        return cls.from_database(cls._DATABASE["Player_One_Hades_C_Pro_v2"])

    @classmethod
    def Player_One_Athena_C_Pro_v2(cls):
        return cls.from_database(cls._DATABASE["Player_One_Athena_C_Pro_v2"])

    @classmethod
    def Player_One_Poseidon_M_Pro_v2(cls):
        return cls.from_database(cls._DATABASE["Player_One_Poseidon_M_Pro_v2"])

    @classmethod
    def Player_One_Artemis_M_Pro_v2(cls):
        return cls.from_database(cls._DATABASE["Player_One_Artemis_M_Pro_v2"])

    @classmethod
    def Player_One_Ares_M_Pro_v2(cls):
        return cls.from_database(cls._DATABASE["Player_One_Ares_M_Pro_v2"])

    @classmethod
    def Player_One_Zeus_M_Pro_v2(cls):
        return cls.from_database(cls._DATABASE["Player_One_Zeus_M_Pro_v2"])

    @classmethod
    def Player_One_Hades_M_Pro_v2(cls):
        return cls.from_database(cls._DATABASE["Player_One_Hades_M_Pro_v2"])

    @classmethod
    def Player_One_Athena_M_Pro_v2(cls):
        return cls.from_database(cls._DATABASE["Player_One_Athena_M_Pro_v2"])
