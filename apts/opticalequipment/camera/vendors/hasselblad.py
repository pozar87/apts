from ..base import Camera

class HasselbladCamera(Camera):
    _DATABASE = {'Hasselblad_X2D_100C': {'brand': 'Hasselblad', 'name': 'X2D 100C', 'type': 'type_dslr', 'optical_length': 26.7, 'mass': 895, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Hasselblad_X1D_II_50C': {'brand': 'Hasselblad', 'name': 'X1D II 50C', 'type': 'type_dslr', 'optical_length': 26.7, 'mass': 650, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Hasselblad_907X_50C': {'brand': 'Hasselblad', 'name': '907X 50C', 'type': 'type_dslr', 'optical_length': 26.7, 'mass': 740, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}}

    @classmethod
    def Hasselblad_X2D_100C(cls):
        return cls.from_database(cls._DATABASE['Hasselblad_X2D_100C'])

    @classmethod
    def Hasselblad_X1D_II_50C(cls):
        return cls.from_database(cls._DATABASE['Hasselblad_X1D_II_50C'])

    @classmethod
    def Hasselblad_907X_50C(cls):
        return cls.from_database(cls._DATABASE['Hasselblad_907X_50C'])