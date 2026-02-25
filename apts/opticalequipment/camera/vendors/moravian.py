from ..base import Camera

class MoravianCamera(Camera):
    _DATABASE = {'Moravian_C3_61000_Pro': {'brand': 'Moravian', 'name': 'C3-61000 Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1200, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Moravian_C1_12000': {'brand': 'Moravian', 'name': 'C1-12000', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 600, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Moravian_C4_16000': {'brand': 'Moravian', 'name': 'C4-16000', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 900, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Moravian_C3_26000_Pro': {'brand': 'Moravian', 'name': 'C3-26000 Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1000, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Moravian_C1_5000': {'brand': 'Moravian', 'name': 'C1-5000', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Moravian_C5_100000': {'brand': 'Moravian', 'name': 'C5-100000', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1500, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Moravian_C3_12000_Pro': {'brand': 'Moravian', 'name': 'C3-12000 Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 800, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Moravian_C2_3000': {'brand': 'Moravian', 'name': 'C2-3000', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 400, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Moravian_C3_16000_Pro': {'brand': 'Moravian', 'name': 'C3-16000 Pro', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1000, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Moravian_C4_9000': {'brand': 'Moravian', 'name': 'C4-9000', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 700, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Moravian_C1_3000': {'brand': 'Moravian', 'name': 'C1-3000', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 350, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Moravian_C1x_61000': {'brand': 'Moravian', 'name': 'C1x-61000', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1300, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Moravian_C1x_26000': {'brand': 'Moravian', 'name': 'C1x-26000', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 900, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Moravian_C1_5500': {'brand': 'Moravian', 'name': 'C1-5500', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Moravian_C2_7000': {'brand': 'Moravian', 'name': 'C2-7000', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 600, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Moravian_C3_61000_Pro_v2': {'brand': 'Moravian', 'name': 'C3-61000 Pro v2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1250, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Moravian_C4_20000': {'brand': 'Moravian', 'name': 'C4-20000', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1100, 'tside_thread': 'M54', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Moravian_C5_100000_v2': {'brand': 'Moravian', 'name': 'C5-100000 v2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1600, 'tside_thread': 'M68', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}}

    @classmethod
    def Moravian_C3_61000_Pro(cls):
        return cls.from_database(cls._DATABASE['Moravian_C3_61000_Pro'])

    @classmethod
    def Moravian_C1_12000(cls):
        return cls.from_database(cls._DATABASE['Moravian_C1_12000'])

    @classmethod
    def Moravian_C4_16000(cls):
        return cls.from_database(cls._DATABASE['Moravian_C4_16000'])

    @classmethod
    def Moravian_C3_26000_Pro(cls):
        return cls.from_database(cls._DATABASE['Moravian_C3_26000_Pro'])

    @classmethod
    def Moravian_C1_5000(cls):
        return cls.from_database(cls._DATABASE['Moravian_C1_5000'])

    @classmethod
    def Moravian_C5_100000(cls):
        return cls.from_database(cls._DATABASE['Moravian_C5_100000'])

    @classmethod
    def Moravian_C3_12000_Pro(cls):
        return cls.from_database(cls._DATABASE['Moravian_C3_12000_Pro'])

    @classmethod
    def Moravian_C2_3000(cls):
        return cls.from_database(cls._DATABASE['Moravian_C2_3000'])

    @classmethod
    def Moravian_C3_16000_Pro(cls):
        return cls.from_database(cls._DATABASE['Moravian_C3_16000_Pro'])

    @classmethod
    def Moravian_C4_9000(cls):
        return cls.from_database(cls._DATABASE['Moravian_C4_9000'])

    @classmethod
    def Moravian_C1_3000(cls):
        return cls.from_database(cls._DATABASE['Moravian_C1_3000'])

    @classmethod
    def Moravian_C1x_61000(cls):
        return cls.from_database(cls._DATABASE['Moravian_C1x_61000'])

    @classmethod
    def Moravian_C1x_26000(cls):
        return cls.from_database(cls._DATABASE['Moravian_C1x_26000'])

    @classmethod
    def Moravian_C1_5500(cls):
        return cls.from_database(cls._DATABASE['Moravian_C1_5500'])

    @classmethod
    def Moravian_C2_7000(cls):
        return cls.from_database(cls._DATABASE['Moravian_C2_7000'])

    @classmethod
    def Moravian_C3_61000_Pro_v2(cls):
        return cls.from_database(cls._DATABASE['Moravian_C3_61000_Pro_v2'])

    @classmethod
    def Moravian_C4_20000(cls):
        return cls.from_database(cls._DATABASE['Moravian_C4_20000'])

    @classmethod
    def Moravian_C5_100000_v2(cls):
        return cls.from_database(cls._DATABASE['Moravian_C5_100000_v2'])