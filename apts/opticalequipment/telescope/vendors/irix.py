from ..base import Telescope

class IrixTelescope(Telescope):
    _DATABASE = {'Irix_150mm_f_2_8_Macro_Canon': {'brand': 'Irix', 'name': '150mm f/2.8 Macro (Canon)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 831, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Irix_150mm_f_2_8_Macro_Nikon': {'brand': 'Irix', 'name': '150mm f/2.8 Macro (Nikon)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 831, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Irix_45mm_f_1_4_Canon': {'brand': 'Irix', 'name': '45mm f/1.4 (Canon)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 710, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Irix_11mm_f_4_Canon': {'brand': 'Irix', 'name': '11mm f/4 (Canon)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 620, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Irix_150mm_f_2_8_Macro_EOS': {'brand': 'Irix', 'name': '150mm f/2.8 Macro (EOS)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 831, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Irix_150mm_f_2_8_Macro_Nikon_F': {'brand': 'Irix', 'name': '150mm f/2.8 Macro (Nikon F)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 831, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Irix_11mm_f_4_Firefly_EOS': {'brand': 'Irix', 'name': '11mm f/4 Firefly (EOS)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 535, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Irix_11mm_f_4_Firefly_Nikon_F': {'brand': 'Irix', 'name': '11mm f/4 Firefly (Nikon F)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 535, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Irix_15mm_f_2_4_Blackstone_EOS': {'brand': 'Irix', 'name': '15mm f/2.4 Blackstone (EOS)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 562, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Irix_15mm_f_2_4_Blackstone_Nikon_F': {'brand': 'Irix', 'name': '15mm f/2.4 Blackstone (Nikon F)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 562, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Irix_45mm_f_1_4_EOS': {'brand': 'Irix', 'name': '45mm f/1.4 (EOS)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 720, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Irix_45mm_f_1_4_Nikon_F': {'brand': 'Irix', 'name': '45mm f/1.4 (Nikon F)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 720, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon F', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Irix_45mm_f_1_4_Sony_E': {'brand': 'Irix', 'name': '45mm f/1.4 (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 720, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Irix_150mm_f_2_8_Macro_Canon(cls):
        return cls.from_database(cls._DATABASE['Irix_150mm_f_2_8_Macro_Canon'])

    @classmethod
    def Irix_150mm_f_2_8_Macro_Nikon(cls):
        return cls.from_database(cls._DATABASE['Irix_150mm_f_2_8_Macro_Nikon'])

    @classmethod
    def Irix_45mm_f_1_4_Canon(cls):
        return cls.from_database(cls._DATABASE['Irix_45mm_f_1_4_Canon'])

    @classmethod
    def Irix_11mm_f_4_Canon(cls):
        return cls.from_database(cls._DATABASE['Irix_11mm_f_4_Canon'])

    @classmethod
    def Irix_150mm_f_2_8_Macro_EOS(cls):
        return cls.from_database(cls._DATABASE['Irix_150mm_f_2_8_Macro_EOS'])

    @classmethod
    def Irix_150mm_f_2_8_Macro_Nikon_F(cls):
        return cls.from_database(cls._DATABASE['Irix_150mm_f_2_8_Macro_Nikon_F'])

    @classmethod
    def Irix_11mm_f_4_Firefly_EOS(cls):
        return cls.from_database(cls._DATABASE['Irix_11mm_f_4_Firefly_EOS'])

    @classmethod
    def Irix_11mm_f_4_Firefly_Nikon_F(cls):
        return cls.from_database(cls._DATABASE['Irix_11mm_f_4_Firefly_Nikon_F'])

    @classmethod
    def Irix_15mm_f_2_4_Blackstone_EOS(cls):
        return cls.from_database(cls._DATABASE['Irix_15mm_f_2_4_Blackstone_EOS'])

    @classmethod
    def Irix_15mm_f_2_4_Blackstone_Nikon_F(cls):
        return cls.from_database(cls._DATABASE['Irix_15mm_f_2_4_Blackstone_Nikon_F'])

    @classmethod
    def Irix_45mm_f_1_4_EOS(cls):
        return cls.from_database(cls._DATABASE['Irix_45mm_f_1_4_EOS'])

    @classmethod
    def Irix_45mm_f_1_4_Nikon_F(cls):
        return cls.from_database(cls._DATABASE['Irix_45mm_f_1_4_Nikon_F'])

    @classmethod
    def Irix_45mm_f_1_4_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Irix_45mm_f_1_4_Sony_E'])