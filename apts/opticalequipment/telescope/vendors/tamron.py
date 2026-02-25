from ..base import Telescope

class TamronTelescope(Telescope):
    _DATABASE = {'Tamron_SP_150_600mm_f_5_6_3_G2_Canon': {'brand': 'Tamron', 'name': 'SP 150-600mm f/5-6.3 G2 (Canon)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 2010, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Tamron_SP_150_600mm_f_5_6_3_G2_Nikon': {'brand': 'Tamron', 'name': 'SP 150-600mm f/5-6.3 G2 (Nikon)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 2010, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Tamron_100_400mm_f_4_5_6_3_Sony_E': {'brand': 'Tamron', 'name': '100-400mm f/4.5-6.3 (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 1115, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Tamron_150_500mm_f_5_6_7_Sony_E': {'brand': 'Tamron', 'name': '150-500mm f/5-6.7 (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 1725, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Tamron_SP_150_600mm_f_5_6_3_EOS': {'brand': 'Tamron', 'name': 'SP 150-600mm f/5-6.3 (EOS)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 2010, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Tamron_SP_150_600mm_f_5_6_3_Nikon_F': {'brand': 'Tamron', 'name': 'SP 150-600mm f/5-6.3 (Nikon F)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 2010, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Tamron_SP_150_600mm_f_5_6_3_Sony_E': {'brand': 'Tamron', 'name': 'SP 150-600mm f/5-6.3 (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 2010, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Tamron_150_500mm_f_5_6_7_Fuji_X': {'brand': 'Tamron', 'name': '150-500mm f/5-6.7 (Fuji X)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 1725, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Fuji X', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Tamron_100_400mm_f_4_5_6_3_EOS': {'brand': 'Tamron', 'name': '100-400mm f/4.5-6.3 (EOS)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 1135, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Tamron_70_180mm_f_2_8_Sony_E': {'brand': 'Tamron', 'name': '70-180mm f/2.8 (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 815, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Tamron_70_300mm_f_4_5_6_3_Sony_E': {'brand': 'Tamron', 'name': '70-300mm f/4.5-6.3 (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 545, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Tamron_28_200mm_f_2_8_5_6_Sony_E': {'brand': 'Tamron', 'name': '28-200mm f/2.8-5.6 (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 575, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Tamron_35_150mm_f_2_2_8_Sony_E': {'brand': 'Tamron', 'name': '35-150mm f/2-2.8 (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 1165, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Tamron_50_400mm_f_4_5_6_3_Sony_E': {'brand': 'Tamron', 'name': '50-400mm f/4.5-6.3 (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 1155, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Tamron_SP_150_600mm_f_5_6_3_G2_Canon(cls):
        return cls.from_database(cls._DATABASE['Tamron_SP_150_600mm_f_5_6_3_G2_Canon'])

    @classmethod
    def Tamron_SP_150_600mm_f_5_6_3_G2_Nikon(cls):
        return cls.from_database(cls._DATABASE['Tamron_SP_150_600mm_f_5_6_3_G2_Nikon'])

    @classmethod
    def Tamron_100_400mm_f_4_5_6_3_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Tamron_100_400mm_f_4_5_6_3_Sony_E'])

    @classmethod
    def Tamron_150_500mm_f_5_6_7_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Tamron_150_500mm_f_5_6_7_Sony_E'])

    @classmethod
    def Tamron_SP_150_600mm_f_5_6_3_EOS(cls):
        return cls.from_database(cls._DATABASE['Tamron_SP_150_600mm_f_5_6_3_EOS'])

    @classmethod
    def Tamron_SP_150_600mm_f_5_6_3_Nikon_F(cls):
        return cls.from_database(cls._DATABASE['Tamron_SP_150_600mm_f_5_6_3_Nikon_F'])

    @classmethod
    def Tamron_SP_150_600mm_f_5_6_3_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Tamron_SP_150_600mm_f_5_6_3_Sony_E'])

    @classmethod
    def Tamron_150_500mm_f_5_6_7_Fuji_X(cls):
        return cls.from_database(cls._DATABASE['Tamron_150_500mm_f_5_6_7_Fuji_X'])

    @classmethod
    def Tamron_100_400mm_f_4_5_6_3_EOS(cls):
        return cls.from_database(cls._DATABASE['Tamron_100_400mm_f_4_5_6_3_EOS'])

    @classmethod
    def Tamron_70_180mm_f_2_8_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Tamron_70_180mm_f_2_8_Sony_E'])

    @classmethod
    def Tamron_70_300mm_f_4_5_6_3_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Tamron_70_300mm_f_4_5_6_3_Sony_E'])

    @classmethod
    def Tamron_28_200mm_f_2_8_5_6_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Tamron_28_200mm_f_2_8_5_6_Sony_E'])

    @classmethod
    def Tamron_35_150mm_f_2_2_8_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Tamron_35_150mm_f_2_2_8_Sony_E'])

    @classmethod
    def Tamron_50_400mm_f_4_5_6_3_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Tamron_50_400mm_f_4_5_6_3_Sony_E'])