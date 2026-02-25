from ..base import Telescope

class MitakonTelescope(Telescope):
    _DATABASE = {'Mitakon_85mm_f_1_2_Sony_E': {'brand': 'Mitakon', 'name': '85mm f/1.2 (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 690, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Mitakon_85mm_f_1_2_EOS': {'brand': 'Mitakon', 'name': '85mm f/1.2 (EOS)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 690, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Mitakon_85mm_f_1_2_Nikon_F': {'brand': 'Mitakon', 'name': '85mm f/1.2 (Nikon F)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 690, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Mitakon_50mm_f_0_95_Sony_E': {'brand': 'Mitakon', 'name': '50mm f/0.95 (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 720, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Mitakon_50mm_f_0_95_Nikon_Z': {'brand': 'Mitakon', 'name': '50mm f/0.95 (Nikon Z)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 720, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon Z', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Mitakon_35mm_f_0_95_Sony_E': {'brand': 'Mitakon', 'name': '35mm f/0.95 (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 560, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Mitakon_35mm_f_0_95_MFT': {'brand': 'Mitakon', 'name': '35mm f/0.95 (MFT)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 560, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'MFT', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Mitakon_35mm_f_0_95_Fuji_X': {'brand': 'Mitakon', 'name': '35mm f/0.95 (Fuji X)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 560, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Fuji X', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Mitakon_20mm_f_2_4_5x_Macro_Sony_E': {'brand': 'Mitakon', 'name': '20mm f/2 4.5x Macro (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 345, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Mitakon_85mm_f_1_2_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Mitakon_85mm_f_1_2_Sony_E'])

    @classmethod
    def Mitakon_85mm_f_1_2_EOS(cls):
        return cls.from_database(cls._DATABASE['Mitakon_85mm_f_1_2_EOS'])

    @classmethod
    def Mitakon_85mm_f_1_2_Nikon_F(cls):
        return cls.from_database(cls._DATABASE['Mitakon_85mm_f_1_2_Nikon_F'])

    @classmethod
    def Mitakon_50mm_f_0_95_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Mitakon_50mm_f_0_95_Sony_E'])

    @classmethod
    def Mitakon_50mm_f_0_95_Nikon_Z(cls):
        return cls.from_database(cls._DATABASE['Mitakon_50mm_f_0_95_Nikon_Z'])

    @classmethod
    def Mitakon_35mm_f_0_95_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Mitakon_35mm_f_0_95_Sony_E'])

    @classmethod
    def Mitakon_35mm_f_0_95_MFT(cls):
        return cls.from_database(cls._DATABASE['Mitakon_35mm_f_0_95_MFT'])

    @classmethod
    def Mitakon_35mm_f_0_95_Fuji_X(cls):
        return cls.from_database(cls._DATABASE['Mitakon_35mm_f_0_95_Fuji_X'])

    @classmethod
    def Mitakon_20mm_f_2_4_5x_Macro_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Mitakon_20mm_f_2_4_5x_Macro_Sony_E'])