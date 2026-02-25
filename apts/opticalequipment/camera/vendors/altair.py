from ..base import Camera

class AltairCamera(Camera):
    _DATABASE = {'Altair_Hypercam_269C_Pro': {'brand': 'Altair', 'name': 'Hypercam 269C Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 700, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Altair_Hypercam_183M_Pro': {'brand': 'Altair', 'name': 'Hypercam 183M Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Altair_Hypercam_533C_Pro': {'brand': 'Altair', 'name': 'Hypercam 533C Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 450, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Altair_Hypercam_294C_Pro': {'brand': 'Altair', 'name': 'Hypercam 294C Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 680, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Altair_Hypercam_571C_Pro': {'brand': 'Altair', 'name': 'Hypercam 571C Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 650, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Altair_Hypercam_26000C_Pro': {'brand': 'Altair', 'name': 'Hypercam 26000C Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 750, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Altair_Hypercam_585C': {'brand': 'Altair', 'name': 'Hypercam 585C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Altair_Hypercam_462C': {'brand': 'Altair', 'name': 'Hypercam 462C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Altair_Hypercam_678C': {'brand': 'Altair', 'name': 'Hypercam 678C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 160, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Altair_Hypercam_174M': {'brand': 'Altair', 'name': 'Hypercam 174M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Altair_Hypercam_290M': {'brand': 'Altair', 'name': 'Hypercam 290M', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 200, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Altair_Hypercam_290C': {'brand': 'Altair', 'name': 'Hypercam 290C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 200, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Altair_Hypercam_178M': {'brand': 'Altair', 'name': 'Hypercam 178M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 180, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Altair_Hypercam_178C': {'brand': 'Altair', 'name': 'Hypercam 178C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 180, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Altair_Hypercam_224C': {'brand': 'Altair', 'name': 'Hypercam 224C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 120, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Altair_Hypercam_120M': {'brand': 'Altair', 'name': 'Hypercam 120M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Altair_Hypercam_385C': {'brand': 'Altair', 'name': 'Hypercam 385C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 150, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Altair_Hypercam_174C': {'brand': 'Altair', 'name': 'Hypercam 174C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 60, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Altair_Hypercam_2600C_Pro': {'brand': 'Altair', 'name': 'Hypercam 2600C Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 750, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Altair_Hypercam_16000M_Pro': {'brand': 'Altair', 'name': 'Hypercam 16000M Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 550, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Altair_GPCAM3_290M': {'brand': 'Altair', 'name': 'GPCAM3 290M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 150, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Altair_GPCAM3_178M': {'brand': 'Altair', 'name': 'GPCAM3 178M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 130, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Altair_GPCAM3_462C': {'brand': 'Altair', 'name': 'GPCAM3 462C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 100, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Altair_GPCAM3_385C': {'brand': 'Altair', 'name': 'GPCAM3 385C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 100, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Altair_Hypercam_26000M_Pro': {'brand': 'Altair', 'name': 'Hypercam 26000M Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 770, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Altair_Hypercam_571M_Pro': {'brand': 'Altair', 'name': 'Hypercam 571M Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 660, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Altair_Hypercam_533M_Pro': {'brand': 'Altair', 'name': 'Hypercam 533M Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 460, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Altair_Hypercam_294M_Pro': {'brand': 'Altair', 'name': 'Hypercam 294M Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 690, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Altair_Hypercam_183M_Pro_v2': {'brand': 'Altair', 'name': 'Hypercam 183M Pro v2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 510, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Altair_Hypercam_2600M_Pro': {'brand': 'Altair', 'name': 'Hypercam 2600M Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 760, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}}

    @classmethod
    def Altair_Hypercam_269C_Pro(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_269C_Pro'])

    @classmethod
    def Altair_Hypercam_183M_Pro(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_183M_Pro'])

    @classmethod
    def Altair_Hypercam_533C_Pro(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_533C_Pro'])

    @classmethod
    def Altair_Hypercam_294C_Pro(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_294C_Pro'])

    @classmethod
    def Altair_Hypercam_571C_Pro(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_571C_Pro'])

    @classmethod
    def Altair_Hypercam_26000C_Pro(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_26000C_Pro'])

    @classmethod
    def Altair_Hypercam_585C(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_585C'])

    @classmethod
    def Altair_Hypercam_462C(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_462C'])

    @classmethod
    def Altair_Hypercam_678C(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_678C'])

    @classmethod
    def Altair_Hypercam_174M(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_174M'])

    @classmethod
    def Altair_Hypercam_290M(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_290M'])

    @classmethod
    def Altair_Hypercam_290C(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_290C'])

    @classmethod
    def Altair_Hypercam_178M(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_178M'])

    @classmethod
    def Altair_Hypercam_178C(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_178C'])

    @classmethod
    def Altair_Hypercam_224C(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_224C'])

    @classmethod
    def Altair_Hypercam_120M(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_120M'])

    @classmethod
    def Altair_Hypercam_385C(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_385C'])

    @classmethod
    def Altair_Hypercam_174C(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_174C'])

    @classmethod
    def Altair_Hypercam_2600C_Pro(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_2600C_Pro'])

    @classmethod
    def Altair_Hypercam_16000M_Pro(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_16000M_Pro'])

    @classmethod
    def Altair_GPCAM3_290M(cls):
        return cls.from_database(cls._DATABASE['Altair_GPCAM3_290M'])

    @classmethod
    def Altair_GPCAM3_178M(cls):
        return cls.from_database(cls._DATABASE['Altair_GPCAM3_178M'])

    @classmethod
    def Altair_GPCAM3_462C(cls):
        return cls.from_database(cls._DATABASE['Altair_GPCAM3_462C'])

    @classmethod
    def Altair_GPCAM3_385C(cls):
        return cls.from_database(cls._DATABASE['Altair_GPCAM3_385C'])

    @classmethod
    def Altair_Hypercam_26000M_Pro(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_26000M_Pro'])

    @classmethod
    def Altair_Hypercam_571M_Pro(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_571M_Pro'])

    @classmethod
    def Altair_Hypercam_533M_Pro(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_533M_Pro'])

    @classmethod
    def Altair_Hypercam_294M_Pro(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_294M_Pro'])

    @classmethod
    def Altair_Hypercam_183M_Pro_v2(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_183M_Pro_v2'])

    @classmethod
    def Altair_Hypercam_2600M_Pro(cls):
        return cls.from_database(cls._DATABASE['Altair_Hypercam_2600M_Pro'])