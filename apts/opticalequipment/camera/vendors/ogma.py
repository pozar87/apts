from ..base import Camera

class OgmaCamera(Camera):
    _DATABASE = {'OGMA_OGC_533C_Pro': {'brand': 'OGMA', 'name': 'OGC-533C Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 450, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'OGMA_OGC_294C_Pro': {'brand': 'OGMA', 'name': 'OGC-294C Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'OGMA_OGC_571C_Pro': {'brand': 'OGMA', 'name': 'OGC-571C Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 650, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'OGMA_OGC_183C_Pro': {'brand': 'OGMA', 'name': 'OGC-183C Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 420, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'OGMA_OGC_585C': {'brand': 'OGMA', 'name': 'OGC-585C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 180, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'OGMA_OGC_462C': {'brand': 'OGMA', 'name': 'OGC-462C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'OGMA_OGC_678C': {'brand': 'OGMA', 'name': 'OGC-678C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 170, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'OGMA_OGC_178C': {'brand': 'OGMA', 'name': 'OGC-178C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'OGMA_OGC_533M_Pro': {'brand': 'OGMA', 'name': 'OGC-533M Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 460, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'OGMA_OGC_2600C_Pro': {'brand': 'OGMA', 'name': 'OGC-2600C Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 700, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'OGMA_OGC_2600M_Pro': {'brand': 'OGMA', 'name': 'OGC-2600M Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 710, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'OGMA_OGC_290MC': {'brand': 'OGMA', 'name': 'OGC-290MC', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 140, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'OGMA_OGC_178MM': {'brand': 'OGMA', 'name': 'OGC-178MM', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 120, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'OGMA_OGC_571M_Pro': {'brand': 'OGMA', 'name': 'OGC-571M Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 610, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'OGMA_OGC_2600C': {'brand': 'OGMA', 'name': 'OGC-2600C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 690, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'OGMA_OGC_2600M': {'brand': 'OGMA', 'name': 'OGC-2600M', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 700, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'OGMA_OGC_571C': {'brand': 'OGMA', 'name': 'OGC-571C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 590, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'OGMA_OGC_183M_Pro': {'brand': 'OGMA', 'name': 'OGC-183M Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 440, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}}

    @classmethod
    def OGMA_OGC_533C_Pro(cls):
        return cls.from_database(cls._DATABASE['OGMA_OGC_533C_Pro'])

    @classmethod
    def OGMA_OGC_294C_Pro(cls):
        return cls.from_database(cls._DATABASE['OGMA_OGC_294C_Pro'])

    @classmethod
    def OGMA_OGC_571C_Pro(cls):
        return cls.from_database(cls._DATABASE['OGMA_OGC_571C_Pro'])

    @classmethod
    def OGMA_OGC_183C_Pro(cls):
        return cls.from_database(cls._DATABASE['OGMA_OGC_183C_Pro'])

    @classmethod
    def OGMA_OGC_585C(cls):
        return cls.from_database(cls._DATABASE['OGMA_OGC_585C'])

    @classmethod
    def OGMA_OGC_462C(cls):
        return cls.from_database(cls._DATABASE['OGMA_OGC_462C'])

    @classmethod
    def OGMA_OGC_678C(cls):
        return cls.from_database(cls._DATABASE['OGMA_OGC_678C'])

    @classmethod
    def OGMA_OGC_178C(cls):
        return cls.from_database(cls._DATABASE['OGMA_OGC_178C'])

    @classmethod
    def OGMA_OGC_533M_Pro(cls):
        return cls.from_database(cls._DATABASE['OGMA_OGC_533M_Pro'])

    @classmethod
    def OGMA_OGC_2600C_Pro(cls):
        return cls.from_database(cls._DATABASE['OGMA_OGC_2600C_Pro'])

    @classmethod
    def OGMA_OGC_2600M_Pro(cls):
        return cls.from_database(cls._DATABASE['OGMA_OGC_2600M_Pro'])

    @classmethod
    def OGMA_OGC_290MC(cls):
        return cls.from_database(cls._DATABASE['OGMA_OGC_290MC'])

    @classmethod
    def OGMA_OGC_178MM(cls):
        return cls.from_database(cls._DATABASE['OGMA_OGC_178MM'])

    @classmethod
    def OGMA_OGC_571M_Pro(cls):
        return cls.from_database(cls._DATABASE['OGMA_OGC_571M_Pro'])

    @classmethod
    def OGMA_OGC_2600C(cls):
        return cls.from_database(cls._DATABASE['OGMA_OGC_2600C'])

    @classmethod
    def OGMA_OGC_2600M(cls):
        return cls.from_database(cls._DATABASE['OGMA_OGC_2600M'])

    @classmethod
    def OGMA_OGC_571C(cls):
        return cls.from_database(cls._DATABASE['OGMA_OGC_571C'])

    @classmethod
    def OGMA_OGC_183M_Pro(cls):
        return cls.from_database(cls._DATABASE['OGMA_OGC_183M_Pro'])