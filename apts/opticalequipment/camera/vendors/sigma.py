from ..base import Camera

class SigmaCamera(Camera):
    _DATABASE = {'Sigma_fp': {'brand': 'Sigma', 'name': 'fp', 'type': 'type_dslr', 'optical_length': 20, 'mass': 427, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Sigma_fp_L': {'brand': 'Sigma', 'name': 'fp L', 'type': 'type_dslr', 'optical_length': 20, 'mass': 427, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Sigma_sd_Quattro': {'brand': 'Sigma', 'name': 'sd Quattro', 'type': 'type_dslr', 'optical_length': 20, 'mass': 625, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Sigma_sd_Quattro_H': {'brand': 'Sigma', 'name': 'sd Quattro H', 'type': 'type_dslr', 'optical_length': 20, 'mass': 625, 'tside_thread': 'Sony E', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}}

    @classmethod
    def Sigma_fp(cls):
        return cls.from_database(cls._DATABASE['Sigma_fp'])

    @classmethod
    def Sigma_fp_L(cls):
        return cls.from_database(cls._DATABASE['Sigma_fp_L'])

    @classmethod
    def Sigma_sd_Quattro(cls):
        return cls.from_database(cls._DATABASE['Sigma_sd_Quattro'])

    @classmethod
    def Sigma_sd_Quattro_H(cls):
        return cls.from_database(cls._DATABASE['Sigma_sd_Quattro_H'])