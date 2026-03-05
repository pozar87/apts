from ..base import Camera

class QhyCamera(Camera):
    _DATABASE = {
        'QHY_MiniGuideScope_5III': {
            'brand': 'QHY',
            'name': 'MiniGuideScope + 5III',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 210,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 4.8,
            'sensor_height_mm': 3.6,
            'width': 1280,
            'height': 960,
            'pixel_size_um': 3.75
        },
        'QHY_PoleMaster': {
            'brand': 'QHY',
            'name': 'PoleMaster',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 100,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 4.8,
            'sensor_height_mm': 3.6,
            'width': 1280,
            'height': 960,
            'pixel_size_um': 3.75
        },
        'QHY_QHY_128C_Pro': {
            'brand': 'QHY',
            'name': 'QHY 128C Pro',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 1300,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 36.03,
            'sensor_height_mm': 24.05,
            'width': 6036,
            'height': 4028,
            'pixel_size_um': 5.97,
            'quantum_efficiency_pct': 53,
            'read_noise_e': 2.5,
            'full_well_e': 76000
        },
        'QHY_QHY_128M_Pro': {
            'brand': 'QHY',
            'name': 'QHY 128M Pro',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 1300,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 36.03,
            'sensor_height_mm': 24.05,
            'width': 6036,
            'height': 4028,
            'pixel_size_um': 5.97,
            'quantum_efficiency_pct': 91,
            'read_noise_e': 2.5,
            'full_well_e': 76000
        },
        'QHY_QHY_163C': {
            'brand': 'QHY',
            'name': 'QHY 163C',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 550,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 17.7,
            'sensor_height_mm': 13.4,
            'width': 4656,
            'height': 3522,
            'pixel_size_um': 3.8,
            'quantum_efficiency_pct': 60,
            'read_noise_e': 1.2,
            'full_well_e': 20000
        },
        'QHY_QHY_163M': {
            'brand': 'QHY',
            'name': 'QHY 163M',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 550,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 17.7,
            'sensor_height_mm': 13.4,
            'width': 4656,
            'height': 3522,
            'pixel_size_um': 3.8,
            'quantum_efficiency_pct': 60,
            'read_noise_e': 1.2,
            'full_well_e': 20000
        },
        'QHY_QHY_168C': {
            'brand': 'QHY',
            'name': 'QHY 168C',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 600,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 23.77,
            'sensor_height_mm': 15.78,
            'width': 4952,
            'height': 3288,
            'pixel_size_um': 4.8,
            'quantum_efficiency_pct': 50,
            'read_noise_e': 2.3,
            'full_well_e': 46000
        },
        'QHY_QHY_168M': {
            'brand': 'QHY',
            'name': 'QHY 168M',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 600,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 23.77,
            'sensor_height_mm': 15.78,
            'width': 4952,
            'height': 3288,
            'pixel_size_um': 4.8,
            'quantum_efficiency_pct': 91,
            'read_noise_e': 2.3,
            'full_well_e': 46000
        },
        'QHY_QHY_174C': {
            'brand': 'QHY',
            'name': 'QHY 174C',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 180,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 11.3,
            'sensor_height_mm': 7.1,
            'width': 1936,
            'height': 1216,
            'pixel_size_um': 5.86,
            'quantum_efficiency_pct': 77,
            'read_noise_e': 6.0,
            'full_well_e': 32000
        },
        'QHY_QHY_174M': {
            'brand': 'QHY',
            'name': 'QHY 174M',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 180,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 11.3,
            'sensor_height_mm': 7.1,
            'width': 1936,
            'height': 1216,
            'pixel_size_um': 5.86,
            'quantum_efficiency_pct': 77,
            'read_noise_e': 6.0,
            'full_well_e': 32000
        },
        'QHY_QHY_183C': {
            'brand': 'QHY',
            'name': 'QHY 183C',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 500,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 13.2,
            'sensor_height_mm': 8.8,
            'width': 5496,
            'height': 3672,
            'pixel_size_um': 2.4,
            'quantum_efficiency_pct': 84,
            'read_noise_e': 1.6,
            'full_well_e': 15000
        },
        'QHY_QHY_183C_M42_Adapter': {
            'brand': 'QHY',
            'name': 'QHY 183C + M42 Adapter',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 530,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 13.2,
            'sensor_height_mm': 8.8,
            'width': 5496,
            'height': 3672,
            'pixel_size_um': 2.4,
            'quantum_efficiency_pct': 84,
            'read_noise_e': 1.6,
            'full_well_e': 15000
        },
        'QHY_QHY_183C_Pro': {
            'brand': 'QHY',
            'name': 'QHY 183C Pro',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 520,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 13.2,
            'sensor_height_mm': 8.8,
            'width': 5496,
            'height': 3672,
            'pixel_size_um': 2.4,
            'quantum_efficiency_pct': 84,
            'read_noise_e': 1.6,
            'full_well_e': 15000
        },
        'QHY_QHY_183M': {
            'brand': 'QHY',
            'name': 'QHY 183M',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 500,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 13.2,
            'sensor_height_mm': 8.8,
            'width': 5496,
            'height': 3672,
            'pixel_size_um': 2.4,
            'quantum_efficiency_pct': 84,
            'read_noise_e': 1.6,
            'full_well_e': 15000
        },
        'QHY_QHY_183M_M42_Adapter': {
            'brand': 'QHY',
            'name': 'QHY 183M + M42 Adapter',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 530,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 13.2,
            'sensor_height_mm': 8.8,
            'width': 5496,
            'height': 3672,
            'pixel_size_um': 2.4,
            'quantum_efficiency_pct': 84,
            'read_noise_e': 1.6,
            'full_well_e': 15000
        },
        'QHY_QHY_183M_Pro': {
            'brand': 'QHY',
            'name': 'QHY 183M Pro',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 520,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 13.2,
            'sensor_height_mm': 8.8,
            'width': 5496,
            'height': 3672,
            'pixel_size_um': 2.4,
            'quantum_efficiency_pct': 84,
            'read_noise_e': 1.6,
            'full_well_e': 15000
        },
        'QHY_QHY_2020C': {
            'brand': 'QHY',
            'name': 'QHY 2020C',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 1000,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 13.3,
            'sensor_height_mm': 13.3,
            'width': 2048,
            'height': 2048,
            'pixel_size_um': 6.5,
            'quantum_efficiency_pct': 74,
            'read_noise_e': 3.7,
            'full_well_e': 70000
        },
        'QHY_QHY_2020M': {
            'brand': 'QHY',
            'name': 'QHY 2020M',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 1000,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 13.3,
            'sensor_height_mm': 13.3,
            'width': 2048,
            'height': 2048,
            'pixel_size_um': 6.5,
            'quantum_efficiency_pct': 74,
            'read_noise_e': 3.7,
            'full_well_e': 70000
        },
        'QHY_QHY_247C': {
            'brand': 'QHY',
            'name': 'QHY 247C',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 700,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 23.5,
            'sensor_height_mm': 15.7,
            'width': 6048,
            'height': 4032,
            'pixel_size_um': 3.91,
            'quantum_efficiency_pct': 50,
            'read_noise_e': 2.3,
            'full_well_e': 46000
        },
        'QHY_QHY_247M': {
            'brand': 'QHY',
            'name': 'QHY 247M',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 700,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 23.5,
            'sensor_height_mm': 15.7,
            'width': 6048,
            'height': 4032,
            'pixel_size_um': 3.91,
            'quantum_efficiency_pct': 91,
            'read_noise_e': 2.3,
            'full_well_e': 46000
        },
        'QHY_QHY_268C': {
            'brand': 'QHY',
            'name': 'QHY 268C',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 800,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 23.5,
            'sensor_height_mm': 15.7,
            'width': 6248,
            'height': 4176,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 81,
            'read_noise_e': 1.1,
            'full_well_e': 51000
        },
        'QHY_QHY_268C_M42_Adapter': {
            'brand': 'QHY',
            'name': 'QHY 268C + M42 Adapter',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 890,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 23.5,
            'sensor_height_mm': 15.7,
            'width': 6248,
            'height': 4176,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 81,
            'read_noise_e': 1.1,
            'full_well_e': 51000
        },
        'QHY_QHY_268C_Pro': {
            'brand': 'QHY',
            'name': 'QHY 268C Pro',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 860,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 23.5,
            'sensor_height_mm': 15.7,
            'width': 6248,
            'height': 4176,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 81,
            'read_noise_e': 1.1,
            'full_well_e': 51000
        },
        'QHY_QHY_268M': {
            'brand': 'QHY',
            'name': 'QHY 268M',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 800,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 23.5,
            'sensor_height_mm': 15.7,
            'width': 6248,
            'height': 4176,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 91,
            'read_noise_e': 1.1,
            'full_well_e': 51000
        },
        'QHY_QHY_268M_M42_Adapter': {
            'brand': 'QHY',
            'name': 'QHY 268M + M42 Adapter',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 890,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 23.5,
            'sensor_height_mm': 15.7,
            'width': 6248,
            'height': 4176,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 91,
            'read_noise_e': 1.1,
            'full_well_e': 51000
        },
        'QHY_QHY_268M_Pro': {
            'brand': 'QHY',
            'name': 'QHY 268M Pro',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 860,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 23.5,
            'sensor_height_mm': 15.7,
            'width': 6248,
            'height': 4176,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 91,
            'read_noise_e': 1.1,
            'full_well_e': 51000
        },
        'QHY_QHY_294C': {
            'brand': 'QHY',
            'name': 'QHY 294C',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 620,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 19.1,
            'sensor_height_mm': 13.0,
            'width': 4144,
            'height': 2822,
            'pixel_size_um': 4.63,
            'quantum_efficiency_pct': 75,
            'read_noise_e': 1.2,
            'full_well_e': 64000
        },
        'QHY_QHY_294C_M42_Adapter': {
            'brand': 'QHY',
            'name': 'QHY 294C + M42 Adapter',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 710,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 19.1,
            'sensor_height_mm': 13.0,
            'width': 4144,
            'height': 2822,
            'pixel_size_um': 4.63,
            'quantum_efficiency_pct': 75,
            'read_noise_e': 1.2,
            'full_well_e': 64000
        },
        'QHY_QHY_294C_Pro': {
            'brand': 'QHY',
            'name': 'QHY 294C Pro',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 680,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 19.1,
            'sensor_height_mm': 13.0,
            'width': 4144,
            'height': 2822,
            'pixel_size_um': 4.63,
            'quantum_efficiency_pct': 75,
            'read_noise_e': 1.2,
            'full_well_e': 64000
        },
        'QHY_QHY_294M': {
            'brand': 'QHY',
            'name': 'QHY 294M',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 620,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 19.1,
            'sensor_height_mm': 13.0,
            'width': 4144,
            'height': 2822,
            'pixel_size_um': 4.63,
            'quantum_efficiency_pct': 90,
            'read_noise_e': 1.2,
            'full_well_e': 66000
        },
        'QHY_QHY_294M_M42_Adapter': {
            'brand': 'QHY',
            'name': 'QHY 294M + M42 Adapter',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 710,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 19.1,
            'sensor_height_mm': 13.0,
            'width': 4144,
            'height': 2822,
            'pixel_size_um': 4.63,
            'quantum_efficiency_pct': 90,
            'read_noise_e': 1.2,
            'full_well_e': 66000
        },
        'QHY_QHY_294M_Pro': {
            'brand': 'QHY',
            'name': 'QHY 294M Pro',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 680,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 19.1,
            'sensor_height_mm': 13.0,
            'width': 4144,
            'height': 2822,
            'pixel_size_um': 4.63,
            'quantum_efficiency_pct': 90,
            'read_noise_e': 1.2,
            'full_well_e': 66000
        },
        'QHY_QHY_367C_Pro': {
            'brand': 'QHY',
            'name': 'QHY 367C Pro',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 900,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 36.0,
            'sensor_height_mm': 24.0,
            'width': 7376,
            'height': 4928,
            'pixel_size_um': 4.88,
            'quantum_efficiency_pct': 50,
            'read_noise_e': 2.4,
            'full_well_e': 80000
        },
        'QHY_QHY_367M_Pro': {
            'brand': 'QHY',
            'name': 'QHY 367M Pro',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 900,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 36.0,
            'sensor_height_mm': 24.0,
            'width': 7376,
            'height': 4928,
            'pixel_size_um': 4.88,
            'quantum_efficiency_pct': 91,
            'read_noise_e': 2.4,
            'full_well_e': 80000
        },
        'QHY_QHY_410C': {
            'brand': 'QHY',
            'name': 'QHY 410C',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 950,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 36.0,
            'sensor_height_mm': 24.0,
            'width': 6072,
            'height': 4044,
            'pixel_size_um': 5.94,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 1.1,
            'full_well_e': 100000
        },
        'QHY_QHY_410C_M42_Adapter': {
            'brand': 'QHY',
            'name': 'QHY 410C + M42 Adapter',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 980,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 36.0,
            'sensor_height_mm': 24.0,
            'width': 6072,
            'height': 4044,
            'pixel_size_um': 5.94,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 1.1,
            'full_well_e': 100000
        },
        'QHY_QHY_410M': {
            'brand': 'QHY',
            'name': 'QHY 410M',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 950,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 36.0,
            'sensor_height_mm': 24.0,
            'width': 6072,
            'height': 4044,
            'pixel_size_um': 5.94,
            'quantum_efficiency_pct': 91,
            'read_noise_e': 1.1,
            'full_well_e': 100000
        },
        'QHY_QHY_410M_M42_Adapter': {
            'brand': 'QHY',
            'name': 'QHY 410M + M42 Adapter',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 980,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 36.0,
            'sensor_height_mm': 24.0,
            'width': 6072,
            'height': 4044,
            'pixel_size_um': 5.94,
            'quantum_efficiency_pct': 91,
            'read_noise_e': 1.1,
            'full_well_e': 100000
        },
        'QHY_QHY_411C': {
            'brand': 'QHY',
            'name': 'QHY 411C',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 1000,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 54.0,
            'sensor_height_mm': 40.0,
            'width': 14192,
            'height': 10640,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 1.5,
            'full_well_e': 50000
        },
        'QHY_QHY_411M': {
            'brand': 'QHY',
            'name': 'QHY 411M',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 1000,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 54.0,
            'sensor_height_mm': 40.0,
            'width': 14192,
            'height': 10640,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 91,
            'read_noise_e': 1.5,
            'full_well_e': 50000
        },
        'QHY_QHY_461C': {
            'brand': 'QHY',
            'name': 'QHY 461C',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 1200,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 44.0,
            'sensor_height_mm': 33.0,
            'width': 11656,
            'height': 8750,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 1.5,
            'full_well_e': 50000
        },
        'QHY_QHY_461C_M42_Adapter': {
            'brand': 'QHY',
            'name': 'QHY 461C + M42 Adapter',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 1230,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 44.0,
            'sensor_height_mm': 33.0,
            'width': 11656,
            'height': 8750,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 1.5,
            'full_well_e': 50000
        },
        'QHY_QHY_461M': {
            'brand': 'QHY',
            'name': 'QHY 461M',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 1200,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 44.0,
            'sensor_height_mm': 33.0,
            'width': 11656,
            'height': 8750,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 91,
            'read_noise_e': 1.5,
            'full_well_e': 50000
        },
        'QHY_QHY_461M_M42_Adapter': {
            'brand': 'QHY',
            'name': 'QHY 461M + M42 Adapter',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 1230,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 44.0,
            'sensor_height_mm': 33.0,
            'width': 11656,
            'height': 8750,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 91,
            'read_noise_e': 1.5,
            'full_well_e': 50000
        },
        'QHY_QHY_492C': {
            'brand': 'QHY',
            'name': 'QHY 492C',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 750,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 19.1,
            'sensor_height_mm': 13.0,
            'width': 4144,
            'height': 2822,
            'pixel_size_um': 4.63,
            'quantum_efficiency_pct': 75,
            'read_noise_e': 1.2,
            'full_well_e': 64000
        },
        'QHY_QHY_492M': {
            'brand': 'QHY',
            'name': 'QHY 492M',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 750,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 19.1,
            'sensor_height_mm': 13.0,
            'width': 4144,
            'height': 2822,
            'pixel_size_um': 4.63,
            'quantum_efficiency_pct': 90,
            'read_noise_e': 1.2,
            'full_well_e': 66000
        },
        'QHY_QHY_5200C': {
            'brand': 'QHY',
            'name': 'QHY 5200C',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 900,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 23.5,
            'sensor_height_mm': 15.7,
            'width': 6248,
            'height': 4176,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 81,
            'read_noise_e': 1.1,
            'full_well_e': 51000
        },
        'QHY_QHY_5200M': {
            'brand': 'QHY',
            'name': 'QHY 5200M',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 900,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 23.5,
            'sensor_height_mm': 15.7,
            'width': 6248,
            'height': 4176,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 91,
            'read_noise_e': 1.1,
            'full_well_e': 51000
        },
        'QHY_QHY_533C': {
            'brand': 'QHY',
            'name': 'QHY 533C',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 700,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 11.31,
            'sensor_height_mm': 11.31,
            'width': 3008,
            'height': 3008,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 1.0,
            'full_well_e': 50000
        },
        'QHY_QHY_533C_M42_Adapter': {
            'brand': 'QHY',
            'name': 'QHY 533C + M42 Adapter',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 770,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 11.31,
            'sensor_height_mm': 11.31,
            'width': 3008,
            'height': 3008,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 1.0,
            'full_well_e': 50000
        },
        'QHY_QHY_533C_Pro': {
            'brand': 'QHY',
            'name': 'QHY 533C Pro',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 740,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 11.31,
            'sensor_height_mm': 11.31,
            'width': 3008,
            'height': 3008,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 1.0,
            'full_well_e': 50000
        },
        'QHY_QHY_533M': {
            'brand': 'QHY',
            'name': 'QHY 533M',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 700,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 11.31,
            'sensor_height_mm': 11.31,
            'width': 3008,
            'height': 3008,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 91,
            'read_noise_e': 1.0,
            'full_well_e': 50000
        },
        'QHY_QHY_533M_M42_Adapter': {
            'brand': 'QHY',
            'name': 'QHY 533M + M42 Adapter',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 770,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 11.31,
            'sensor_height_mm': 11.31,
            'width': 3008,
            'height': 3008,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 91,
            'read_noise_e': 1.0,
            'full_well_e': 50000
        },
        'QHY_QHY_533M_Pro': {
            'brand': 'QHY',
            'name': 'QHY 533M Pro',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 740,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 11.31,
            'sensor_height_mm': 11.31,
            'width': 3008,
            'height': 3008,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 91,
            'read_noise_e': 1.0,
            'full_well_e': 50000
        },
        'QHY_QHY_550C': {
            'brand': 'QHY',
            'name': 'QHY 550C',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 650,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 8.5,
            'sensor_height_mm': 7.1,
            'width': 2460,
            'height': 2070,
            'pixel_size_um': 3.45,
            'quantum_efficiency_pct': 70,
            'read_noise_e': 2.2,
            'full_well_e': 10500
        },
        'QHY_QHY_550M': {
            'brand': 'QHY',
            'name': 'QHY 550M',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 650,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 8.5,
            'sensor_height_mm': 7.1,
            'width': 2460,
            'height': 2070,
            'pixel_size_um': 3.45,
            'quantum_efficiency_pct': 70,
            'read_noise_e': 2.2,
            'full_well_e': 10500
        },
        'QHY_QHY_5III_120C': {
            'brand': 'QHY',
            'name': 'QHY 5III 120C',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 60,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 4.8,
            'sensor_height_mm': 3.6,
            'width': 1280,
            'height': 960,
            'pixel_size_um': 3.75,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 4.0,
            'full_well_e': 13000
        },
        'QHY_QHY_5III_120M': {
            'brand': 'QHY',
            'name': 'QHY 5III 120M',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 60,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 4.8,
            'sensor_height_mm': 3.6,
            'width': 1280,
            'height': 960,
            'pixel_size_um': 3.75,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 4.0,
            'full_well_e': 13000
        },
        'QHY_QHY_5III_174M': {
            'brand': 'QHY',
            'name': 'QHY 5III 174M',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 80,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 11.3,
            'sensor_height_mm': 7.1,
            'width': 1936,
            'height': 1216,
            'pixel_size_um': 5.86,
            'quantum_efficiency_pct': 77,
            'read_noise_e': 6.0,
            'full_well_e': 32000
        },
        'QHY_QHY_5III_178C': {
            'brand': 'QHY',
            'name': 'QHY 5III 178C',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 80,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 7.4,
            'sensor_height_mm': 5.0,
            'width': 3072,
            'height': 2048,
            'pixel_size_um': 2.4,
            'quantum_efficiency_pct': 78,
            'read_noise_e': 1.4,
            'full_well_e': 15000
        },
        'QHY_QHY_5III_178M': {
            'brand': 'QHY',
            'name': 'QHY 5III 178M',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 80,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 7.4,
            'sensor_height_mm': 5.0,
            'width': 3072,
            'height': 2048,
            'pixel_size_um': 2.4,
            'quantum_efficiency_pct': 78,
            'read_noise_e': 1.4,
            'full_well_e': 15000
        },
        'QHY_QHY_5III_200C': {
            'brand': 'QHY',
            'name': 'QHY 5III 200C',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 70,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 7.68,
            'sensor_height_mm': 4.32,
            'width': 1920,
            'height': 1080,
            'pixel_size_um': 4.0,
            'quantum_efficiency_pct': 92,
            'read_noise_e': 0.6,
            'full_well_e': 8800
        },
        'QHY_QHY_5III_200M': {
            'brand': 'QHY',
            'name': 'QHY 5III 200M',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 70,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 7.68,
            'sensor_height_mm': 4.32,
            'width': 1920,
            'height': 1080,
            'pixel_size_um': 4.0,
            'quantum_efficiency_pct': 92,
            'read_noise_e': 0.6,
            'full_well_e': 8800
        },
        'QHY_QHY_5III_224C': {
            'brand': 'QHY',
            'name': 'QHY 5III 224C',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 80,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 4.8,
            'sensor_height_mm': 3.6,
            'width': 1304,
            'height': 976,
            'pixel_size_um': 3.75,
            'quantum_efficiency_pct': 75,
            'read_noise_e': 0.75,
            'full_well_e': 19000
        },
        'QHY_QHY_5III_290C': {
            'brand': 'QHY',
            'name': 'QHY 5III 290C',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 80,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 5.6,
            'sensor_height_mm': 3.2,
            'width': 1936,
            'height': 1096,
            'pixel_size_um': 2.9,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 1.0,
            'full_well_e': 14600
        },
        'QHY_QHY_5III_290M': {
            'brand': 'QHY',
            'name': 'QHY 5III 290M',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 80,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 5.6,
            'sensor_height_mm': 3.2,
            'width': 1936,
            'height': 1096,
            'pixel_size_um': 2.9,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 1.0,
            'full_well_e': 14600
        },
        'QHY_QHY_5III_385C': {
            'brand': 'QHY',
            'name': 'QHY 5III 385C',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 80,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 7.3,
            'sensor_height_mm': 4.1,
            'width': 1936,
            'height': 1096,
            'pixel_size_um': 3.75,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 0.7,
            'full_well_e': 18700
        },
        'QHY_QHY_5III_385M': {
            'brand': 'QHY',
            'name': 'QHY 5III 385M',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 80,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 7.3,
            'sensor_height_mm': 4.1,
            'width': 1936,
            'height': 1096,
            'pixel_size_um': 3.75,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 0.7,
            'full_well_e': 18700
        },
        'QHY_QHY_5III_462C': {
            'brand': 'QHY',
            'name': 'QHY 5III 462C',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 80,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 5.6,
            'sensor_height_mm': 3.2,
            'width': 1920,
            'height': 1080,
            'pixel_size_um': 2.9,
            'quantum_efficiency_pct': 91,
            'read_noise_e': 0.5,
            'full_well_e': 12000
        },
        'QHY_QHY_5III_462M': {
            'brand': 'QHY',
            'name': 'QHY 5III 462M',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 90,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 5.6,
            'sensor_height_mm': 3.2,
            'width': 1920,
            'height': 1080,
            'pixel_size_um': 2.9,
            'quantum_efficiency_pct': 91,
            'read_noise_e': 0.5,
            'full_well_e': 12000
        },
        'QHY_QHY_5III_482C': {
            'brand': 'QHY',
            'name': 'QHY 5III 482C',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 90,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 11.13,
            'sensor_height_mm': 6.26,
            'width': 1920,
            'height': 1080,
            'pixel_size_um': 5.8,
            'quantum_efficiency_pct': 85,
            'read_noise_e': 1.5,
            'full_well_e': 50000
        },
        'QHY_QHY_5III_482M': {
            'brand': 'QHY',
            'name': 'QHY 5III 482M',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 90,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 11.13,
            'sensor_height_mm': 6.26,
            'width': 1920,
            'height': 1080,
            'pixel_size_um': 5.8,
            'quantum_efficiency_pct': 85,
            'read_noise_e': 1.5,
            'full_well_e': 50000
        },
        'QHY_QHY_5III_485C': {
            'brand': 'QHY',
            'name': 'QHY 5III 485C',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 80,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 11.1,
            'sensor_height_mm': 6.2,
            'width': 3840,
            'height': 2160,
            'pixel_size_um': 2.9,
            'quantum_efficiency_pct': 85,
            'read_noise_e': 1.0,
            'full_well_e': 13000
        },
        'QHY_QHY_5III_533C': {
            'brand': 'QHY',
            'name': 'QHY 5III 533C',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 80,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 11.31,
            'sensor_height_mm': 11.31,
            'width': 3008,
            'height': 3008,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 1.0,
            'full_well_e': 50000
        },
        'QHY_QHY_5III_533M': {
            'brand': 'QHY',
            'name': 'QHY 5III 533M',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 80,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 11.31,
            'sensor_height_mm': 11.31,
            'width': 3008,
            'height': 3008,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 91,
            'read_noise_e': 1.0,
            'full_well_e': 50000
        },
        'QHY_QHY_5III_568C': {
            'brand': 'QHY',
            'name': 'QHY 5III 568C',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 110,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 14.5,
            'sensor_height_mm': 10.8,
            'width': 2472,
            'height': 2064,
            'pixel_size_um': 5.86,
            'quantum_efficiency_pct': 78,
            'read_noise_e': 2.0,
            'full_well_e': 30000
        },
        'QHY_QHY_5III_568M': {
            'brand': 'QHY',
            'name': 'QHY 5III 568M',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 110,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 14.5,
            'sensor_height_mm': 10.8,
            'width': 2472,
            'height': 2064,
            'pixel_size_um': 5.86,
            'quantum_efficiency_pct': 78,
            'read_noise_e': 2.0,
            'full_well_e': 30000
        },
        'QHY_QHY_5III_585C': {
            'brand': 'QHY',
            'name': 'QHY 5III 585C',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 80,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 11.1,
            'sensor_height_mm': 6.3,
            'width': 3856,
            'height': 2180,
            'pixel_size_um': 2.9,
            'quantum_efficiency_pct': 91,
            'read_noise_e': 0.8,
            'full_well_e': 32000
        },
        'QHY_QHY_5III_600C': {
            'brand': 'QHY',
            'name': 'QHY 5III 600C',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 120,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 36.0,
            'sensor_height_mm': 24.0,
            'width': 9576,
            'height': 6388,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 1.2,
            'full_well_e': 51000
        },
        'QHY_QHY_5III_600M': {
            'brand': 'QHY',
            'name': 'QHY 5III 600M',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 120,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 36.0,
            'sensor_height_mm': 24.0,
            'width': 9576,
            'height': 6388,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 91,
            'read_noise_e': 1.2,
            'full_well_e': 51000
        },
        'QHY_QHY_5III_662C': {
            'brand': 'QHY',
            'name': 'QHY 5III 662C',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 80,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 5.57,
            'sensor_height_mm': 3.13,
            'width': 1920,
            'height': 1080,
            'pixel_size_um': 2.9,
            'quantum_efficiency_pct': 91,
            'read_noise_e': 0.8,
            'full_well_e': 38200
        },
        'QHY_QHY_5III_678C': {
            'brand': 'QHY',
            'name': 'QHY 5III 678C',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 100,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 7.7,
            'sensor_height_mm': 4.3,
            'width': 3840,
            'height': 2160,
            'pixel_size_um': 2.0,
            'quantum_efficiency_pct': 83,
            'read_noise_e': 0.6,
            'full_well_e': 10000
        },
        'QHY_QHY_5III_678M': {
            'brand': 'QHY',
            'name': 'QHY 5III 678M',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 100,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 7.7,
            'sensor_height_mm': 4.3,
            'width': 3840,
            'height': 2160,
            'pixel_size_um': 2.0,
            'quantum_efficiency_pct': 83,
            'read_noise_e': 0.6,
            'full_well_e': 10000
        },
        'QHY_QHY_5III_715C': {
            'brand': 'QHY',
            'name': 'QHY 5III 715C',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 80,
            'tside_thread': 'CS',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 5.6,
            'sensor_height_mm': 3.2,
            'width': 3864,
            'height': 2192,
            'pixel_size_um': 1.45,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 0.72,
            'full_well_e': 6000
        },
        'QHY_QHY_600C': {
            'brand': 'QHY',
            'name': 'QHY 600C',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 1050,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 36.0,
            'sensor_height_mm': 24.0,
            'width': 9576,
            'height': 6388,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 1.2,
            'full_well_e': 51000
        },
        'QHY_QHY_600C_M42_Adapter': {
            'brand': 'QHY',
            'name': 'QHY 600C + M42 Adapter',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 1130,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 36.0,
            'sensor_height_mm': 24.0,
            'width': 9576,
            'height': 6388,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 1.2,
            'full_well_e': 51000
        },
        'QHY_QHY_600C_Pro': {
            'brand': 'QHY',
            'name': 'QHY 600C Pro',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 1100,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 36.0,
            'sensor_height_mm': 24.0,
            'width': 9576,
            'height': 6388,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 1.2,
            'full_well_e': 51000
        },
        'QHY_QHY_600LC': {
            'brand': 'QHY',
            'name': 'QHY 600LC',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 1150,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 36.0,
            'sensor_height_mm': 24.0,
            'width': 9576,
            'height': 6388,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 80,
            'read_noise_e': 1.2,
            'full_well_e': 51000
        },
        'QHY_QHY_600LM': {
            'brand': 'QHY',
            'name': 'QHY 600LM',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 1150,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 36.0,
            'sensor_height_mm': 24.0,
            'width': 9576,
            'height': 6388,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 91,
            'read_noise_e': 1.2,
            'full_well_e': 51000
        },
        'QHY_QHY_600M': {
            'brand': 'QHY',
            'name': 'QHY 600M',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 1050,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 36.0,
            'sensor_height_mm': 24.0,
            'width': 9576,
            'height': 6388,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 91,
            'read_noise_e': 1.2,
            'full_well_e': 51000
        },
        'QHY_QHY_600M_M42_Adapter': {
            'brand': 'QHY',
            'name': 'QHY 600M + M42 Adapter',
            'type': 'type_camera',
            'optical_length': 12.5,
            'mass': 1130,
            'tside_thread': 'M42',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 36.0,
            'sensor_height_mm': 24.0,
            'width': 9576,
            'height': 6388,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 91,
            'read_noise_e': 1.2,
            'full_well_e': 51000
        },
        'QHY_QHY_600M_Pro': {
            'brand': 'QHY',
            'name': 'QHY 600M Pro',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 1100,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 36.0,
            'sensor_height_mm': 24.0,
            'width': 9576,
            'height': 6388,
            'pixel_size_um': 3.76,
            'quantum_efficiency_pct': 91,
            'read_noise_e': 1.2,
            'full_well_e': 51000
        },
        'QHY_QHY_990C': {
            'brand': 'QHY',
            'name': 'QHY 990C',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 600,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 6.96,
            'sensor_height_mm': 5.26,
            'width': 1296,
            'height': 1032,
            'pixel_size_um': 5.0
        },
        'QHY_QHY_990M': {
            'brand': 'QHY',
            'name': 'QHY 990M',
            'type': 'type_camera',
            'optical_length': 17.5,
            'mass': 600,
            'tside_thread': 'M54',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 6.96,
            'sensor_height_mm': 5.26,
            'width': 1296,
            'height': 1032,
            'pixel_size_um': 5.0
        }
    }

    @classmethod
    def QHY_QHY_600M(cls):
        """
        Factory method for QHY 600M camera.
        Sensor: Sony IMX455 (Full-Frame Mono)
        """
        return cls(36.0, 24.0, 9576, 6388, 'QHY QHY 600M', pixel_size=3.76, read_noise=1.2, full_well=51000, quantum_efficiency=91, mass=1050, backfocus=17.5, optical_length=17.5)

    @classmethod
    def QHY_QHY_600C(cls):
        """
        Factory method for QHY 600C camera.
        Sensor: Sony IMX455 (Full-Frame Color)
        """
        return cls(36.0, 24.0, 9576, 6388, 'QHY QHY 600C', pixel_size=3.76, read_noise=1.2, full_well=51000, quantum_efficiency=80, mass=1050, backfocus=17.5, optical_length=17.5)

    @classmethod
    def QHY_QHY_268M(cls):
        """
        Factory method for QHY 268M camera.
        Sensor: Sony IMX571 (APS-C Mono)
        """
        return cls(23.5, 15.7, 6248, 4176, 'QHY QHY 268M', pixel_size=3.76, read_noise=1.1, full_well=51000, quantum_efficiency=91, mass=800, backfocus=17.5, optical_length=17.5)

    @classmethod
    def QHY_QHY_268C(cls):
        """
        Factory method for QHY 268C camera.
        Sensor: Sony IMX571 (APS-C Color)
        """
        return cls(23.5, 15.7, 6248, 4176, 'QHY QHY 268C', pixel_size=3.76, read_noise=1.1, full_well=51000, quantum_efficiency=81, mass=800, backfocus=17.5, optical_length=17.5)

    @classmethod
    def QHY_QHY_600M_Pro(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_600M_Pro'])

    @classmethod
    def QHY_QHY_268M_Pro(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_268M_Pro'])

    @classmethod
    def QHY_QHY_533M_Pro(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_533M_Pro'])

    @classmethod
    def QHY_QHY_533M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_533M'])

    @classmethod
    def QHY_QHY_294M_Pro(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_294M_Pro'])

    @classmethod
    def QHY_QHY_294M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_294M'])

    @classmethod
    def QHY_QHY_183M_Pro(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_183M_Pro'])

    @classmethod
    def QHY_QHY_183M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_183M'])

    @classmethod
    def QHY_QHY_163M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_163M'])

    @classmethod
    def QHY_QHY_168M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_168M'])

    @classmethod
    def QHY_QHY_367M_Pro(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_367M_Pro'])

    @classmethod
    def QHY_QHY_410M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_410M'])

    @classmethod
    def QHY_QHY_411M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_411M'])

    @classmethod
    def QHY_QHY_461M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_461M'])

    @classmethod
    def QHY_QHY_492M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_492M'])

    @classmethod
    def QHY_QHY_128M_Pro(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_128M_Pro'])

    @classmethod
    def QHY_QHY_247M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_247M'])

    @classmethod
    def QHY_QHY_600C_Pro(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_600C_Pro'])

    @classmethod
    def QHY_QHY_268C_Pro(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_268C_Pro'])

    @classmethod
    def QHY_QHY_533C_Pro(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_533C_Pro'])

    @classmethod
    def QHY_QHY_533C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_533C'])

    @classmethod
    def QHY_QHY_294C_Pro(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_294C_Pro'])

    @classmethod
    def QHY_QHY_294C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_294C'])

    @classmethod
    def QHY_QHY_183C_Pro(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_183C_Pro'])

    @classmethod
    def QHY_QHY_183C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_183C'])

    @classmethod
    def QHY_QHY_163C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_163C'])

    @classmethod
    def QHY_QHY_168C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_168C'])

    @classmethod
    def QHY_QHY_367C_Pro(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_367C_Pro'])

    @classmethod
    def QHY_QHY_410C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_410C'])

    @classmethod
    def QHY_QHY_411C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_411C'])

    @classmethod
    def QHY_QHY_461C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_461C'])

    @classmethod
    def QHY_QHY_492C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_492C'])

    @classmethod
    def QHY_QHY_128C_Pro(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_128C_Pro'])

    @classmethod
    def QHY_QHY_247C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_247C'])

    @classmethod
    def QHY_QHY_5III_178M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_178M'])

    @classmethod
    def QHY_QHY_5III_178C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_178C'])

    @classmethod
    def QHY_QHY_5III_290M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_290M'])

    @classmethod
    def QHY_QHY_5III_290C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_290C'])

    @classmethod
    def QHY_QHY_5III_462C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_462C'])

    @classmethod
    def QHY_QHY_5III_485C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_485C'])

    @classmethod
    def QHY_QHY_5III_715C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_715C'])

    @classmethod
    def QHY_QHY_5III_533M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_533M'])

    @classmethod
    def QHY_QHY_5III_533C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_533C'])

    @classmethod
    def QHY_QHY_5III_224C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_224C'])

    @classmethod
    def QHY_QHY_5III_174M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_174M'])

    @classmethod
    def QHY_QHY_5III_585C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_585C'])

    @classmethod
    def QHY_QHY_5III_662C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_662C'])

    @classmethod
    def QHY_QHY_600M_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_600M_M42_Adapter'])

    @classmethod
    def QHY_QHY_268M_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_268M_M42_Adapter'])

    @classmethod
    def QHY_QHY_533M_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_533M_M42_Adapter'])

    @classmethod
    def QHY_QHY_294M_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_294M_M42_Adapter'])

    @classmethod
    def QHY_QHY_183M_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_183M_M42_Adapter'])

    @classmethod
    def QHY_QHY_410M_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_410M_M42_Adapter'])

    @classmethod
    def QHY_QHY_461M_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_461M_M42_Adapter'])

    @classmethod
    def QHY_QHY_600C_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_600C_M42_Adapter'])

    @classmethod
    def QHY_QHY_268C_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_268C_M42_Adapter'])

    @classmethod
    def QHY_QHY_533C_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_533C_M42_Adapter'])

    @classmethod
    def QHY_QHY_294C_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_294C_M42_Adapter'])

    @classmethod
    def QHY_QHY_183C_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_183C_M42_Adapter'])

    @classmethod
    def QHY_QHY_410C_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_410C_M42_Adapter'])

    @classmethod
    def QHY_QHY_461C_M42_Adapter(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_461C_M42_Adapter'])

    @classmethod
    def QHY_PoleMaster(cls):
        return cls.from_database(cls._DATABASE['QHY_PoleMaster'])

    @classmethod
    def QHY_MiniGuideScope_5III(cls):
        return cls.from_database(cls._DATABASE['QHY_MiniGuideScope_5III'])

    @classmethod
    def QHY_QHY_5III_120M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_120M'])

    @classmethod
    def QHY_QHY_5III_200M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_200M'])

    @classmethod
    def QHY_QHY_5III_385M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_385M'])

    @classmethod
    def QHY_QHY_5III_678M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_678M'])

    @classmethod
    def QHY_QHY_5III_482M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_482M'])

    @classmethod
    def QHY_QHY_5III_120C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_120C'])

    @classmethod
    def QHY_QHY_5III_200C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_200C'])

    @classmethod
    def QHY_QHY_5III_385C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_385C'])

    @classmethod
    def QHY_QHY_5III_678C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_678C'])

    @classmethod
    def QHY_QHY_5III_482C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_482C'])

    @classmethod
    def QHY_QHY_5III_462M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_462M'])

    @classmethod
    def QHY_QHY_5III_568M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_568M'])

    @classmethod
    def QHY_QHY_5III_600M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_600M'])

    @classmethod
    def QHY_QHY_5III_568C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_568C'])

    @classmethod
    def QHY_QHY_5III_600C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5III_600C'])

    @classmethod
    def QHY_QHY_990M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_990M'])

    @classmethod
    def QHY_QHY_600LM(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_600LM'])

    @classmethod
    def QHY_QHY_5200M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5200M'])

    @classmethod
    def QHY_QHY_2020M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_2020M'])

    @classmethod
    def QHY_QHY_550M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_550M'])

    @classmethod
    def QHY_QHY_174M(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_174M'])

    @classmethod
    def QHY_QHY_990C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_990C'])

    @classmethod
    def QHY_QHY_600LC(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_600LC'])

    @classmethod
    def QHY_QHY_5200C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_5200C'])

    @classmethod
    def QHY_QHY_2020C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_2020C'])

    @classmethod
    def QHY_QHY_550C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_550C'])

    @classmethod
    def QHY_QHY_174C(cls):
        return cls.from_database(cls._DATABASE['QHY_QHY_174C'])
