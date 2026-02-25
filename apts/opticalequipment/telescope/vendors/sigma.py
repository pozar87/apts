from ..base import Telescope

class SigmaTelescope(Telescope):
    _DATABASE = {'Sigma_135mm_f_2_Art': {'brand': 'Sigma', 'name': '135mm f/2 Art', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 1130, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sigma_105mm_f_1_4_Art': {'brand': 'Sigma', 'name': '105mm f/1.4 Art', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 1645, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sigma_150_600mm_f_5_6_3_DG': {'brand': 'Sigma', 'name': '150-600mm f/5-6.3 DG', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 2860, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sigma_14mm_f_1_8_Art': {'brand': 'Sigma', 'name': '14mm f/1.8 Art', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 1120, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sigma_180mm_f_2_8_APO_Macro_Canon': {'brand': 'Sigma', 'name': '180mm f/2.8 APO Macro (Canon)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 975, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sigma_180mm_f_2_8_APO_Macro_Nikon': {'brand': 'Sigma', 'name': '180mm f/2.8 APO Macro (Nikon)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 975, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sigma_500mm_f_4_DG_OS_HSM': {'brand': 'Sigma', 'name': '500mm f/4 DG OS HSM', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 3310, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sigma_60_600mm_f_4_5_6_3_DG_Canon': {'brand': 'Sigma', 'name': '60-600mm f/4.5-6.3 DG (Canon)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 2700, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sigma_100_400mm_f_5_6_3_DG_Canon': {'brand': 'Sigma', 'name': '100-400mm f/5-6.3 DG (Canon)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 1160, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sigma_150_600mm_f_5_6_3_DG_Nikon': {'brand': 'Sigma', 'name': '150-600mm f/5-6.3 DG (Nikon)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 2860, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sigma_150_600mm_f_5_6_3_Sony_E': {'brand': 'Sigma', 'name': '150-600mm f/5-6.3 (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 2100, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sigma_135mm_f_1_8_Art_Sony_E': {'brand': 'Sigma', 'name': '135mm f/1.8 Art (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 1130, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sigma_105mm_f_1_4_Art_Sony_E': {'brand': 'Sigma', 'name': '105mm f/1.4 Art (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 1645, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sigma_135mm_f_1_8_Art_Nikon_F': {'brand': 'Sigma', 'name': '135mm f/1.8 Art (Nikon F)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 1130, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sigma_105mm_f_1_4_Art_Nikon_F': {'brand': 'Sigma', 'name': '105mm f/1.4 Art (Nikon F)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 1645, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sigma_85mm_f_1_4_Art_EOS': {'brand': 'Sigma', 'name': '85mm f/1.4 Art (EOS)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 1130, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sigma_85mm_f_1_4_Art_Sony_E': {'brand': 'Sigma', 'name': '85mm f/1.4 Art (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 1130, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sigma_85mm_f_1_4_Art_Nikon_F': {'brand': 'Sigma', 'name': '85mm f/1.4 Art (Nikon F)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 1130, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sigma_40mm_f_1_4_Art_EOS': {'brand': 'Sigma', 'name': '40mm f/1.4 Art (EOS)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 1200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sigma_40mm_f_1_4_Art_Sony_E': {'brand': 'Sigma', 'name': '40mm f/1.4 Art (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 1200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sigma_24mm_f_1_4_Art_EOS': {'brand': 'Sigma', 'name': '24mm f/1.4 Art (EOS)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 665, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sigma_24mm_f_1_4_Art_Sony_E': {'brand': 'Sigma', 'name': '24mm f/1.4 Art (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 665, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sigma_20mm_f_1_4_Art_EOS': {'brand': 'Sigma', 'name': '20mm f/1.4 Art (EOS)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 950, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sigma_20mm_f_1_4_Art_Sony_E': {'brand': 'Sigma', 'name': '20mm f/1.4 Art (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 950, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sigma_50mm_f_1_4_Art_EOS': {'brand': 'Sigma', 'name': '50mm f/1.4 Art (EOS)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 815, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sigma_50mm_f_1_4_Art_Sony_E': {'brand': 'Sigma', 'name': '50mm f/1.4 Art (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 815, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sigma_50mm_f_1_4_Art_Nikon_F': {'brand': 'Sigma', 'name': '50mm f/1.4 Art (Nikon F)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 815, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sigma_60_600mm_f_4_5_6_3_DG_EOS': {'brand': 'Sigma', 'name': '60-600mm f/4.5-6.3 DG (EOS)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 2700, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sigma_60_600mm_f_4_5_6_3_DG_Sony_E': {'brand': 'Sigma', 'name': '60-600mm f/4.5-6.3 DG (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 2700, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sigma_150_600mm_f_5_6_3_DG_Sony_E': {'brand': 'Sigma', 'name': '150-600mm f/5-6.3 DG (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 2860, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sigma_150_600mm_f_5_6_3_DG_Nikon_F': {'brand': 'Sigma', 'name': '150-600mm f/5-6.3 DG (Nikon F)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 2860, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sigma_100_400mm_f_5_6_3_DG_EOS': {'brand': 'Sigma', 'name': '100-400mm f/5-6.3 DG (EOS)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 1160, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sigma_100_400mm_f_5_6_3_DG_Sony_E': {'brand': 'Sigma', 'name': '100-400mm f/5-6.3 DG (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 1160, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Sigma_135mm_f_2_Art(cls):
        return cls.from_database(cls._DATABASE['Sigma_135mm_f_2_Art'])

    @classmethod
    def Sigma_105mm_f_1_4_Art(cls):
        return cls.from_database(cls._DATABASE['Sigma_105mm_f_1_4_Art'])

    @classmethod
    def Sigma_150_600mm_f_5_6_3_DG(cls):
        return cls.from_database(cls._DATABASE['Sigma_150_600mm_f_5_6_3_DG'])

    @classmethod
    def Sigma_14mm_f_1_8_Art(cls):
        return cls.from_database(cls._DATABASE['Sigma_14mm_f_1_8_Art'])

    @classmethod
    def Sigma_180mm_f_2_8_APO_Macro_Canon(cls):
        return cls.from_database(cls._DATABASE['Sigma_180mm_f_2_8_APO_Macro_Canon'])

    @classmethod
    def Sigma_180mm_f_2_8_APO_Macro_Nikon(cls):
        return cls.from_database(cls._DATABASE['Sigma_180mm_f_2_8_APO_Macro_Nikon'])

    @classmethod
    def Sigma_500mm_f_4_DG_OS_HSM(cls):
        return cls.from_database(cls._DATABASE['Sigma_500mm_f_4_DG_OS_HSM'])

    @classmethod
    def Sigma_60_600mm_f_4_5_6_3_DG_Canon(cls):
        return cls.from_database(cls._DATABASE['Sigma_60_600mm_f_4_5_6_3_DG_Canon'])

    @classmethod
    def Sigma_100_400mm_f_5_6_3_DG_Canon(cls):
        return cls.from_database(cls._DATABASE['Sigma_100_400mm_f_5_6_3_DG_Canon'])

    @classmethod
    def Sigma_150_600mm_f_5_6_3_DG_Nikon(cls):
        return cls.from_database(cls._DATABASE['Sigma_150_600mm_f_5_6_3_DG_Nikon'])

    @classmethod
    def Sigma_150_600mm_f_5_6_3_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Sigma_150_600mm_f_5_6_3_Sony_E'])

    @classmethod
    def Sigma_135mm_f_1_8_Art_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Sigma_135mm_f_1_8_Art_Sony_E'])

    @classmethod
    def Sigma_105mm_f_1_4_Art_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Sigma_105mm_f_1_4_Art_Sony_E'])

    @classmethod
    def Sigma_135mm_f_1_8_Art_Nikon_F(cls):
        return cls.from_database(cls._DATABASE['Sigma_135mm_f_1_8_Art_Nikon_F'])

    @classmethod
    def Sigma_105mm_f_1_4_Art_Nikon_F(cls):
        return cls.from_database(cls._DATABASE['Sigma_105mm_f_1_4_Art_Nikon_F'])

    @classmethod
    def Sigma_85mm_f_1_4_Art_EOS(cls):
        return cls.from_database(cls._DATABASE['Sigma_85mm_f_1_4_Art_EOS'])

    @classmethod
    def Sigma_85mm_f_1_4_Art_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Sigma_85mm_f_1_4_Art_Sony_E'])

    @classmethod
    def Sigma_85mm_f_1_4_Art_Nikon_F(cls):
        return cls.from_database(cls._DATABASE['Sigma_85mm_f_1_4_Art_Nikon_F'])

    @classmethod
    def Sigma_40mm_f_1_4_Art_EOS(cls):
        return cls.from_database(cls._DATABASE['Sigma_40mm_f_1_4_Art_EOS'])

    @classmethod
    def Sigma_40mm_f_1_4_Art_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Sigma_40mm_f_1_4_Art_Sony_E'])

    @classmethod
    def Sigma_24mm_f_1_4_Art_EOS(cls):
        return cls.from_database(cls._DATABASE['Sigma_24mm_f_1_4_Art_EOS'])

    @classmethod
    def Sigma_24mm_f_1_4_Art_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Sigma_24mm_f_1_4_Art_Sony_E'])

    @classmethod
    def Sigma_20mm_f_1_4_Art_EOS(cls):
        return cls.from_database(cls._DATABASE['Sigma_20mm_f_1_4_Art_EOS'])

    @classmethod
    def Sigma_20mm_f_1_4_Art_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Sigma_20mm_f_1_4_Art_Sony_E'])

    @classmethod
    def Sigma_50mm_f_1_4_Art_EOS(cls):
        return cls.from_database(cls._DATABASE['Sigma_50mm_f_1_4_Art_EOS'])

    @classmethod
    def Sigma_50mm_f_1_4_Art_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Sigma_50mm_f_1_4_Art_Sony_E'])

    @classmethod
    def Sigma_50mm_f_1_4_Art_Nikon_F(cls):
        return cls.from_database(cls._DATABASE['Sigma_50mm_f_1_4_Art_Nikon_F'])

    @classmethod
    def Sigma_60_600mm_f_4_5_6_3_DG_EOS(cls):
        return cls.from_database(cls._DATABASE['Sigma_60_600mm_f_4_5_6_3_DG_EOS'])

    @classmethod
    def Sigma_60_600mm_f_4_5_6_3_DG_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Sigma_60_600mm_f_4_5_6_3_DG_Sony_E'])

    @classmethod
    def Sigma_150_600mm_f_5_6_3_DG_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Sigma_150_600mm_f_5_6_3_DG_Sony_E'])

    @classmethod
    def Sigma_150_600mm_f_5_6_3_DG_Nikon_F(cls):
        return cls.from_database(cls._DATABASE['Sigma_150_600mm_f_5_6_3_DG_Nikon_F'])

    @classmethod
    def Sigma_100_400mm_f_5_6_3_DG_EOS(cls):
        return cls.from_database(cls._DATABASE['Sigma_100_400mm_f_5_6_3_DG_EOS'])

    @classmethod
    def Sigma_100_400mm_f_5_6_3_DG_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Sigma_100_400mm_f_5_6_3_DG_Sony_E'])