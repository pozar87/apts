from ..base import Camera

class AtikCamera(Camera):
    _DATABASE = {'Atik_Horizon': {'brand': 'Atik', 'name': 'Horizon', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 600, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Atik_383L': {'brand': 'Atik', 'name': '383L+', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 550, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Atik_460EX': {'brand': 'Atik', 'name': '460EX', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 450, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Atik_ONE_6_0': {'brand': 'Atik', 'name': 'ONE 6.0', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 800, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Atik_Infinity': {'brand': 'Atik', 'name': 'Infinity', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 300, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Atik_414EX': {'brand': 'Atik', 'name': '414EX', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 400, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Atik_490EX': {'brand': 'Atik', 'name': '490EX', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Atik_ONE_9_0': {'brand': 'Atik', 'name': 'ONE 9.0', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1000, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Atik_16200': {'brand': 'Atik', 'name': '16200', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 700, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Atik_Horizon_II': {'brand': 'Atik', 'name': 'Horizon II', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 650, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Atik_414EX_Mono': {'brand': 'Atik', 'name': '414EX Mono', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 420, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Atik_428EX': {'brand': 'Atik', 'name': '428EX', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 480, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Atik_450EX': {'brand': 'Atik', 'name': '450EX', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 460, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Atik_ONE_2_0': {'brand': 'Atik', 'name': 'ONE 2.0', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 700, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Atik_ACIS_7_1': {'brand': 'Atik', 'name': 'ACIS 7.1', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 900, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Atik_ACIS_12_1': {'brand': 'Atik', 'name': 'ACIS 12.1', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 1100, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Atik_11000': {'brand': 'Atik', 'name': '11000', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 550, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Atik_16HR': {'brand': 'Atik', 'name': '16HR', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 600, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Atik_320E': {'brand': 'Atik', 'name': '320E', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 300, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Atik_4000': {'brand': 'Atik', 'name': '4000', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 400, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Atik_Titan_Mono': {'brand': 'Atik', 'name': 'Titan Mono', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 150, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Atik_GP_CAM3_290M': {'brand': 'Atik', 'name': 'GP-CAM3 290M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 120, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Atik_GP_CAM2_290M': {'brand': 'Atik', 'name': 'GP-CAM2 290M', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 100, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Atik_VS14': {'brand': 'Atik', 'name': 'VS14', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 200, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Atik_Apx60': {'brand': 'Atik', 'name': 'Apx60', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 800, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}}

    @classmethod
    def Atik_Horizon(cls):
        return cls.from_database(cls._DATABASE['Atik_Horizon'])

    @classmethod
    def Atik_383L(cls):
        return cls.from_database(cls._DATABASE['Atik_383L'])

    @classmethod
    def Atik_460EX(cls):
        return cls.from_database(cls._DATABASE['Atik_460EX'])

    @classmethod
    def Atik_ONE_6_0(cls):
        return cls.from_database(cls._DATABASE['Atik_ONE_6_0'])

    @classmethod
    def Atik_Infinity(cls):
        return cls.from_database(cls._DATABASE['Atik_Infinity'])

    @classmethod
    def Atik_414EX(cls):
        return cls.from_database(cls._DATABASE['Atik_414EX'])

    @classmethod
    def Atik_490EX(cls):
        return cls.from_database(cls._DATABASE['Atik_490EX'])

    @classmethod
    def Atik_ONE_9_0(cls):
        return cls.from_database(cls._DATABASE['Atik_ONE_9_0'])

    @classmethod
    def Atik_16200(cls):
        return cls.from_database(cls._DATABASE['Atik_16200'])

    @classmethod
    def Atik_Horizon_II(cls):
        return cls.from_database(cls._DATABASE['Atik_Horizon_II'])

    @classmethod
    def Atik_414EX_Mono(cls):
        return cls.from_database(cls._DATABASE['Atik_414EX_Mono'])

    @classmethod
    def Atik_428EX(cls):
        return cls.from_database(cls._DATABASE['Atik_428EX'])

    @classmethod
    def Atik_450EX(cls):
        return cls.from_database(cls._DATABASE['Atik_450EX'])

    @classmethod
    def Atik_ONE_2_0(cls):
        return cls.from_database(cls._DATABASE['Atik_ONE_2_0'])

    @classmethod
    def Atik_ACIS_7_1(cls):
        return cls.from_database(cls._DATABASE['Atik_ACIS_7_1'])

    @classmethod
    def Atik_ACIS_12_1(cls):
        return cls.from_database(cls._DATABASE['Atik_ACIS_12_1'])

    @classmethod
    def Atik_11000(cls):
        return cls.from_database(cls._DATABASE['Atik_11000'])

    @classmethod
    def Atik_16HR(cls):
        return cls.from_database(cls._DATABASE['Atik_16HR'])

    @classmethod
    def Atik_320E(cls):
        return cls.from_database(cls._DATABASE['Atik_320E'])

    @classmethod
    def Atik_4000(cls):
        return cls.from_database(cls._DATABASE['Atik_4000'])

    @classmethod
    def Atik_Titan_Mono(cls):
        return cls.from_database(cls._DATABASE['Atik_Titan_Mono'])

    @classmethod
    def Atik_GP_CAM3_290M(cls):
        return cls.from_database(cls._DATABASE['Atik_GP_CAM3_290M'])

    @classmethod
    def Atik_GP_CAM2_290M(cls):
        return cls.from_database(cls._DATABASE['Atik_GP_CAM2_290M'])

    @classmethod
    def Atik_VS14(cls):
        return cls.from_database(cls._DATABASE['Atik_VS14'])

    @classmethod
    def Atik_Apx60(cls):
        return cls.from_database(cls._DATABASE['Atik_Apx60'])