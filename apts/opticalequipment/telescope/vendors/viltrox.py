from ..base import Telescope

class ViltroxTelescope(Telescope):
    _DATABASE = {'Viltrox_85mm_f_1_8_II_Sony_E': {'brand': 'Viltrox', 'name': '85mm f/1.8 II (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 312, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Viltrox_85mm_f_1_8_II_Nikon_Z': {'brand': 'Viltrox', 'name': '85mm f/1.8 II (Nikon Z)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 312, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon Z', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Viltrox_85mm_f_1_8_II_Canon_RF': {'brand': 'Viltrox', 'name': '85mm f/1.8 II (Canon RF)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 312, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Canon RF', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Viltrox_85mm_f_1_8_II_Fuji_X': {'brand': 'Viltrox', 'name': '85mm f/1.8 II (Fuji X)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 312, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Fuji X', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Viltrox_56mm_f_1_4_Sony_E': {'brand': 'Viltrox', 'name': '56mm f/1.4 (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 260, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Viltrox_56mm_f_1_4_Fuji_X': {'brand': 'Viltrox', 'name': '56mm f/1.4 (Fuji X)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 260, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Fuji X', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Viltrox_56mm_f_1_4_Nikon_Z': {'brand': 'Viltrox', 'name': '56mm f/1.4 (Nikon Z)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 260, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Nikon Z', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Viltrox_23mm_f_1_4_Sony_E': {'brand': 'Viltrox', 'name': '23mm f/1.4 (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 245, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Viltrox_23mm_f_1_4_Fuji_X': {'brand': 'Viltrox', 'name': '23mm f/1.4 (Fuji X)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 245, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Fuji X', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Viltrox_33mm_f_1_4_Sony_E': {'brand': 'Viltrox', 'name': '33mm f/1.4 (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 255, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Viltrox_33mm_f_1_4_Fuji_X': {'brand': 'Viltrox', 'name': '33mm f/1.4 (Fuji X)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 255, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Fuji X', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Viltrox_13mm_f_1_4_Sony_E': {'brand': 'Viltrox', 'name': '13mm f/1.4 (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 420, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Viltrox_13mm_f_1_4_Fuji_X': {'brand': 'Viltrox', 'name': '13mm f/1.4 (Fuji X)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 420, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Fuji X', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Viltrox_75mm_f_1_2_Sony_E': {'brand': 'Viltrox', 'name': '75mm f/1.2 (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 510, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Viltrox_75mm_f_1_2_Fuji_X': {'brand': 'Viltrox', 'name': '75mm f/1.2 (Fuji X)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 510, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Fuji X', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Viltrox_AF_85mm_f_1_8_EOS': {'brand': 'Viltrox', 'name': 'AF 85mm f/1.8 (EOS)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 350, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Viltrox_AF_56mm_f_1_4_EOS_M': {'brand': 'Viltrox', 'name': 'AF 56mm f/1.4 (EOS-M)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 260, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'EOS', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Viltrox_24mm_f_1_8_Sony_E': {'brand': 'Viltrox', 'name': '24mm f/1.8 (Sony E)', 'type': 'type_camera_lens', 'optical_length': 0, 'mass': 255, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'Sony E', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Viltrox_85mm_f_1_8_II_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Viltrox_85mm_f_1_8_II_Sony_E'])

    @classmethod
    def Viltrox_85mm_f_1_8_II_Nikon_Z(cls):
        return cls.from_database(cls._DATABASE['Viltrox_85mm_f_1_8_II_Nikon_Z'])

    @classmethod
    def Viltrox_85mm_f_1_8_II_Canon_RF(cls):
        return cls.from_database(cls._DATABASE['Viltrox_85mm_f_1_8_II_Canon_RF'])

    @classmethod
    def Viltrox_85mm_f_1_8_II_Fuji_X(cls):
        return cls.from_database(cls._DATABASE['Viltrox_85mm_f_1_8_II_Fuji_X'])

    @classmethod
    def Viltrox_56mm_f_1_4_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Viltrox_56mm_f_1_4_Sony_E'])

    @classmethod
    def Viltrox_56mm_f_1_4_Fuji_X(cls):
        return cls.from_database(cls._DATABASE['Viltrox_56mm_f_1_4_Fuji_X'])

    @classmethod
    def Viltrox_56mm_f_1_4_Nikon_Z(cls):
        return cls.from_database(cls._DATABASE['Viltrox_56mm_f_1_4_Nikon_Z'])

    @classmethod
    def Viltrox_23mm_f_1_4_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Viltrox_23mm_f_1_4_Sony_E'])

    @classmethod
    def Viltrox_23mm_f_1_4_Fuji_X(cls):
        return cls.from_database(cls._DATABASE['Viltrox_23mm_f_1_4_Fuji_X'])

    @classmethod
    def Viltrox_33mm_f_1_4_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Viltrox_33mm_f_1_4_Sony_E'])

    @classmethod
    def Viltrox_33mm_f_1_4_Fuji_X(cls):
        return cls.from_database(cls._DATABASE['Viltrox_33mm_f_1_4_Fuji_X'])

    @classmethod
    def Viltrox_13mm_f_1_4_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Viltrox_13mm_f_1_4_Sony_E'])

    @classmethod
    def Viltrox_13mm_f_1_4_Fuji_X(cls):
        return cls.from_database(cls._DATABASE['Viltrox_13mm_f_1_4_Fuji_X'])

    @classmethod
    def Viltrox_75mm_f_1_2_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Viltrox_75mm_f_1_2_Sony_E'])

    @classmethod
    def Viltrox_75mm_f_1_2_Fuji_X(cls):
        return cls.from_database(cls._DATABASE['Viltrox_75mm_f_1_2_Fuji_X'])

    @classmethod
    def Viltrox_AF_85mm_f_1_8_EOS(cls):
        return cls.from_database(cls._DATABASE['Viltrox_AF_85mm_f_1_8_EOS'])

    @classmethod
    def Viltrox_AF_56mm_f_1_4_EOS_M(cls):
        return cls.from_database(cls._DATABASE['Viltrox_AF_56mm_f_1_4_EOS_M'])

    @classmethod
    def Viltrox_24mm_f_1_8_Sony_E(cls):
        return cls.from_database(cls._DATABASE['Viltrox_24mm_f_1_8_Sony_E'])