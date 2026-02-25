from ..base import Camera

class OmegonCamera(Camera):
    _DATABASE = {'Omegon_veTEC_571C': {'brand': 'Omegon', 'name': 'veTEC 571C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 600, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Omegon_veTEC_533C': {'brand': 'Omegon', 'name': 'veTEC 533C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 450, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Omegon_veTEC_294C': {'brand': 'Omegon', 'name': 'veTEC 294C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Omegon_veTEC_183C': {'brand': 'Omegon', 'name': 'veTEC 183C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 400, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Omegon_veTEC_26000C_Pro': {'brand': 'Omegon', 'name': 'veTEC 26000C Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 750, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Omegon_veTEC_2600MC': {'brand': 'Omegon', 'name': 'veTEC 2600MC', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 650, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Omegon_veTEC_571M': {'brand': 'Omegon', 'name': 'veTEC 571M', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 620, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Omegon_veTEC_16000C': {'brand': 'Omegon', 'name': 'veTEC 16000C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 550, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Omegon_veTEC_585C': {'brand': 'Omegon', 'name': 'veTEC 585C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 180, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Omegon_veTEC_462C': {'brand': 'Omegon', 'name': 'veTEC 462C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 150, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Omegon_veTEC_178M': {'brand': 'Omegon', 'name': 'veTEC 178M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 140, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Omegon_veTEC_290M': {'brand': 'Omegon', 'name': 'veTEC 290M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 160, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Omegon_vePROBE_462C': {'brand': 'Omegon', 'name': 'vePROBE 462C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 120, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Omegon_vePROBE_290MC': {'brand': 'Omegon', 'name': 'vePROBE 290MC', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 130, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}}

    @classmethod
    def Omegon_veTEC_571C(cls):
        return cls.from_database(cls._DATABASE['Omegon_veTEC_571C'])

    @classmethod
    def Omegon_veTEC_533C(cls):
        return cls.from_database(cls._DATABASE['Omegon_veTEC_533C'])

    @classmethod
    def Omegon_veTEC_294C(cls):
        return cls.from_database(cls._DATABASE['Omegon_veTEC_294C'])

    @classmethod
    def Omegon_veTEC_183C(cls):
        return cls.from_database(cls._DATABASE['Omegon_veTEC_183C'])

    @classmethod
    def Omegon_veTEC_26000C_Pro(cls):
        return cls.from_database(cls._DATABASE['Omegon_veTEC_26000C_Pro'])

    @classmethod
    def Omegon_veTEC_2600MC(cls):
        return cls.from_database(cls._DATABASE['Omegon_veTEC_2600MC'])

    @classmethod
    def Omegon_veTEC_571M(cls):
        return cls.from_database(cls._DATABASE['Omegon_veTEC_571M'])

    @classmethod
    def Omegon_veTEC_16000C(cls):
        return cls.from_database(cls._DATABASE['Omegon_veTEC_16000C'])

    @classmethod
    def Omegon_veTEC_585C(cls):
        return cls.from_database(cls._DATABASE['Omegon_veTEC_585C'])

    @classmethod
    def Omegon_veTEC_462C(cls):
        return cls.from_database(cls._DATABASE['Omegon_veTEC_462C'])

    @classmethod
    def Omegon_veTEC_178M(cls):
        return cls.from_database(cls._DATABASE['Omegon_veTEC_178M'])

    @classmethod
    def Omegon_veTEC_290M(cls):
        return cls.from_database(cls._DATABASE['Omegon_veTEC_290M'])

    @classmethod
    def Omegon_vePROBE_462C(cls):
        return cls.from_database(cls._DATABASE['Omegon_vePROBE_462C'])

    @classmethod
    def Omegon_vePROBE_290MC(cls):
        return cls.from_database(cls._DATABASE['Omegon_vePROBE_290MC'])