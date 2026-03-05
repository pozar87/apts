from ..base import Camera

class Om_system_olympusCamera(Camera):
    _DATABASE = {
        'OM_System_Olympus_OM_1': {
            'brand': 'OM System/Olympus',
            'name': 'OM-1',
            'type': 'type_dslr',
            'optical_length': 19.25,
            'mass': 599,
            'tside_thread': 'MFT',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 17.4,
            'sensor_height_mm': 13.0,
            'width': 5184,
            'height': 3888,
            'pixel_size_um': 3.3
        },
        'OM_System_Olympus_OM_1_II': {
            'brand': 'OM System/Olympus',
            'name': 'OM-1 II',
            'type': 'type_dslr',
            'optical_length': 19.25,
            'mass': 599,
            'tside_thread': 'MFT',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 17.4,
            'sensor_height_mm': 13.0,
            'width': 5184,
            'height': 3888,
            'pixel_size_um': 3.3
        },
        'OM_System_Olympus_E_M1_III': {
            'brand': 'OM System/Olympus',
            'name': 'E-M1 III',
            'type': 'type_dslr',
            'optical_length': 19.25,
            'mass': 580,
            'tside_thread': 'MFT',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 17.4,
            'sensor_height_mm': 13.0,
            'width': 5184,
            'height': 3888,
            'pixel_size_um': 3.3
        },
        'OM_System_Olympus_E_M1_II': {
            'brand': 'OM System/Olympus',
            'name': 'E-M1 II',
            'type': 'type_dslr',
            'optical_length': 19.25,
            'mass': 574,
            'tside_thread': 'MFT',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 17.4,
            'sensor_height_mm': 13.0,
            'width': 5184,
            'height': 3888,
            'pixel_size_um': 3.3
        },
        'OM_System_Olympus_E_M5_III': {
            'brand': 'OM System/Olympus',
            'name': 'E-M5 III',
            'type': 'type_dslr',
            'optical_length': 19.25,
            'mass': 414,
            'tside_thread': 'MFT',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 17.4,
            'sensor_height_mm': 13.0,
            'width': 5184,
            'height': 3888,
            'pixel_size_um': 3.3
        },
        'OM_System_Olympus_E_M10_IV': {
            'brand': 'OM System/Olympus',
            'name': 'E-M10 IV',
            'type': 'type_dslr',
            'optical_length': 19.25,
            'mass': 383,
            'tside_thread': 'MFT',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 17.4,
            'sensor_height_mm': 13.0,
            'width': 5184,
            'height': 3888,
            'pixel_size_um': 3.3
        },
        'OM_System_Olympus_E_PL10': {
            'brand': 'OM System/Olympus',
            'name': 'E-PL10',
            'type': 'type_dslr',
            'optical_length': 19.25,
            'mass': 332,
            'tside_thread': 'MFT',
            'tside_gender': 'Female',
            'cside_thread': '',
            'cside_gender': '',
            'reversible': False,
            'bf_role': 'end',
            'sensor_width_mm': 17.3,
            'sensor_height_mm': 13.0,
            'width': 4608,
            'height': 3456,
            'pixel_size_um': 3.8
        }
    }

    @classmethod
    def OM_System_Olympus_OM_1(cls):
        return cls.from_database(cls._DATABASE['OM_System_Olympus_OM_1'])

    @classmethod
    def OM_System_Olympus_OM_1_II(cls):
        return cls.from_database(cls._DATABASE['OM_System_Olympus_OM_1_II'])

    @classmethod
    def OM_System_Olympus_E_M1_III(cls):
        return cls.from_database(cls._DATABASE['OM_System_Olympus_E_M1_III'])

    @classmethod
    def OM_System_Olympus_E_M1_II(cls):
        return cls.from_database(cls._DATABASE['OM_System_Olympus_E_M1_II'])

    @classmethod
    def OM_System_Olympus_E_M5_III(cls):
        return cls.from_database(cls._DATABASE['OM_System_Olympus_E_M5_III'])

    @classmethod
    def OM_System_Olympus_E_M10_IV(cls):
        return cls.from_database(cls._DATABASE['OM_System_Olympus_E_M10_IV'])

    @classmethod
    def OM_System_Olympus_E_PL10(cls):
        return cls.from_database(cls._DATABASE['OM_System_Olympus_E_PL10'])
