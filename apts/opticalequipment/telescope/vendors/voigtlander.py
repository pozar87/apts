from ..base import Telescope

class VoigtlanderTelescope(Telescope):
    _DATABASE = {'Voigtlander_Nokton_50mm_f_1_2_Sony_E': {'brand': 'Voigtlander', 'name': 'Nokton 50mm f/1.2 (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 480, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Voigtlander_APO_Lanthar_110mm_f_2_5_Sony_E': {'brand': 'Voigtlander', 'name': 'APO-Lanthar 110mm f/2.5 (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 756, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Voigtlander_Nokton_25mm_f_0_95_II_MFT': {'brand': 'Voigtlander', 'name': 'Nokton 25mm f/0.95 II (MFT)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 410, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'MFT', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Voigtlander_Nokton_42_5mm_f_0_95_MFT': {'brand': 'Voigtlander', 'name': 'Nokton 42.5mm f/0.95 (MFT)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 571, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'MFT', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Voigtlander_Macro_APO_Lanthar_65mm_f_2_Sony_E': {'brand': 'Voigtlander', 'name': 'Macro APO-Lanthar 65mm f/2 (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 625, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Voigtlander_Nokton_35mm_f_1_2_Sony_E': {'brand': 'Voigtlander', 'name': 'Nokton 35mm f/1.2 (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 420, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Voigtlander_Nokton_40mm_f_1_2_Sony_E': {'brand': 'Voigtlander', 'name': 'Nokton 40mm f/1.2 (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 420, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Voigtlander_Nokton_50mm_f_1_0_Nikon_Z': {'brand': 'Voigtlander', 'name': 'Nokton 50mm f/1.0 (Nikon Z)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 780, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon Z', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Voigtlander_HELIAR_40mm_f_2_8_Sony_E': {'brand': 'Voigtlander', 'name': 'HELIAR 40mm f/2.8 (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 124, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Voigtlander_APO_SKOPAR_90mm_f_2_8_Sony_E': {'brand': 'Voigtlander', 'name': 'APO-SKOPAR 90mm f/2.8 (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 260, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Voigtlander_COLOR_SKOPAR_21mm_f_3_5_Sony_E': {'brand': 'Voigtlander', 'name': 'COLOR-SKOPAR 21mm f/3.5 (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 230, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Voigtlander_Nokton_50mm_f_1_2_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Voigtlander_Nokton_50mm_f_1_2_Sony_E'])

    @classmethod
    def Voigtlander_APO_Lanthar_110mm_f_2_5_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Voigtlander_APO_Lanthar_110mm_f_2_5_Sony_E'])

    @classmethod
    def Voigtlander_Nokton_25mm_f_0_95_II_MFT(cls):
        return cls.from_database(cls._DATABASE['Voigtlander_Nokton_25mm_f_0_95_II_MFT'])

    @classmethod
    def Voigtlander_Nokton_42_5mm_f_0_95_MFT(cls):
        return cls.from_database(cls._DATABASE['Voigtlander_Nokton_42_5mm_f_0_95_MFT'])

    @classmethod
    def Voigtlander_Macro_APO_Lanthar_65mm_f_2_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Voigtlander_Macro_APO_Lanthar_65mm_f_2_Sony_E'])

    @classmethod
    def Voigtlander_Nokton_35mm_f_1_2_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Voigtlander_Nokton_35mm_f_1_2_Sony_E'])

    @classmethod
    def Voigtlander_Nokton_40mm_f_1_2_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Voigtlander_Nokton_40mm_f_1_2_Sony_E'])

    @classmethod
    def Voigtlander_Nokton_50mm_f_1_0_Nikon_Z(cls):
        return cls.from_database(cls._DATABASE['Voigtlander_Nokton_50mm_f_1_0_Nikon_Z'])

    @classmethod
    def Voigtlander_HELIAR_40mm_f_2_8_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Voigtlander_HELIAR_40mm_f_2_8_Sony_E'])

    @classmethod
    def Voigtlander_APO_SKOPAR_90mm_f_2_8_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Voigtlander_APO_SKOPAR_90mm_f_2_8_Sony_E'])

    @classmethod
    def Voigtlander_COLOR_SKOPAR_21mm_f_3_5_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Voigtlander_COLOR_SKOPAR_21mm_f_3_5_Sony_E'])