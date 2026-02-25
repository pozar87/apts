from ..base import Camera

class Flir_point_greyCamera(Camera):
    _DATABASE = {'FLIR_Point_Grey_Chameleon3_USB3': {'brand': 'FLIR/Point Grey', 'name': 'Chameleon3 USB3', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 200, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'FLIR_Point_Grey_Grasshopper3_USB3': {'brand': 'FLIR/Point Grey', 'name': 'Grasshopper3 USB3', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 350, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'FLIR_Point_Grey_Blackfly_S_IMX290': {'brand': 'FLIR/Point Grey', 'name': 'Blackfly S (IMX290)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 250, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'FLIR_Point_Grey_Blackfly_S_IMX178': {'brand': 'FLIR/Point Grey', 'name': 'Blackfly S (IMX178)', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 220, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'FLIR_Point_Grey_Firefly_S': {'brand': 'FLIR/Point Grey', 'name': 'Firefly S', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 180, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}}

    @classmethod
    def FLIR_Point_Grey_Chameleon3_USB3(cls):
        return cls.from_database(cls._DATABASE['FLIR_Point_Grey_Chameleon3_USB3'])

    @classmethod
    def FLIR_Point_Grey_Grasshopper3_USB3(cls):
        return cls.from_database(cls._DATABASE['FLIR_Point_Grey_Grasshopper3_USB3'])

    @classmethod
    def FLIR_Point_Grey_Blackfly_S_IMX290(cls):
        return cls.from_database(cls._DATABASE['FLIR_Point_Grey_Blackfly_S_IMX290'])

    @classmethod
    def FLIR_Point_Grey_Blackfly_S_IMX178(cls):
        return cls.from_database(cls._DATABASE['FLIR_Point_Grey_Blackfly_S_IMX178'])

    @classmethod
    def FLIR_Point_Grey_Firefly_S(cls):
        return cls.from_database(cls._DATABASE['FLIR_Point_Grey_Firefly_S'])