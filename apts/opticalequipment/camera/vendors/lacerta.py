from ..base import Camera

class LacertaCamera(Camera):
    _DATABASE = {'Lacerta_DeepSkyPro_2600C': {'brand': 'Lacerta', 'name': 'DeepSkyPro 2600C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 700, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Lacerta_DeepSkyPro_533C': {'brand': 'Lacerta', 'name': 'DeepSkyPro 533C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 450, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Lacerta_DeepSkyPro_294C': {'brand': 'Lacerta', 'name': 'DeepSkyPro 294C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Lacerta_DeepSkyPro_571C': {'brand': 'Lacerta', 'name': 'DeepSkyPro 571C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 580, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Lacerta_DeepSkyPro_2600M': {'brand': 'Lacerta', 'name': 'DeepSkyPro 2600M', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 720, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Lacerta_DeepSkyPro_183C': {'brand': 'Lacerta', 'name': 'DeepSkyPro 183C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 420, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Lacerta_DeepSkyPro_183M': {'brand': 'Lacerta', 'name': 'DeepSkyPro 183M', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 430, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Lacerta_DeepSkyPro_585C': {'brand': 'Lacerta', 'name': 'DeepSkyPro 585C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 180, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Lacerta_DeepSkyPro_462C': {'brand': 'Lacerta', 'name': 'DeepSkyPro 462C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 120, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Lacerta_DeepSkyPro_290MC': {'brand': 'Lacerta', 'name': 'DeepSkyPro 290MC', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 150, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Lacerta_DeepSkyPro_178MM': {'brand': 'Lacerta', 'name': 'DeepSkyPro 178MM', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 130, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}}

    @classmethod
    def Lacerta_DeepSkyPro_2600C(cls):
        return cls.from_database(cls._DATABASE['Lacerta_DeepSkyPro_2600C'])

    @classmethod
    def Lacerta_DeepSkyPro_533C(cls):
        return cls.from_database(cls._DATABASE['Lacerta_DeepSkyPro_533C'])

    @classmethod
    def Lacerta_DeepSkyPro_294C(cls):
        return cls.from_database(cls._DATABASE['Lacerta_DeepSkyPro_294C'])

    @classmethod
    def Lacerta_DeepSkyPro_571C(cls):
        return cls.from_database(cls._DATABASE['Lacerta_DeepSkyPro_571C'])

    @classmethod
    def Lacerta_DeepSkyPro_2600M(cls):
        return cls.from_database(cls._DATABASE['Lacerta_DeepSkyPro_2600M'])

    @classmethod
    def Lacerta_DeepSkyPro_183C(cls):
        return cls.from_database(cls._DATABASE['Lacerta_DeepSkyPro_183C'])

    @classmethod
    def Lacerta_DeepSkyPro_183M(cls):
        return cls.from_database(cls._DATABASE['Lacerta_DeepSkyPro_183M'])

    @classmethod
    def Lacerta_DeepSkyPro_585C(cls):
        return cls.from_database(cls._DATABASE['Lacerta_DeepSkyPro_585C'])

    @classmethod
    def Lacerta_DeepSkyPro_462C(cls):
        return cls.from_database(cls._DATABASE['Lacerta_DeepSkyPro_462C'])

    @classmethod
    def Lacerta_DeepSkyPro_290MC(cls):
        return cls.from_database(cls._DATABASE['Lacerta_DeepSkyPro_290MC'])

    @classmethod
    def Lacerta_DeepSkyPro_178MM(cls):
        return cls.from_database(cls._DATABASE['Lacerta_DeepSkyPro_178MM'])