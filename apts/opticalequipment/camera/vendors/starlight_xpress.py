from ..base import Camera

class Starlight_xpressCamera(Camera):
    _DATABASE = {'Starlight_Xpress_Trius_SX_694': {'brand': 'Starlight Xpress', 'name': 'Trius SX-694', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 400, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Starlight_Xpress_Trius_SX_814': {'brand': 'Starlight Xpress', 'name': 'Trius SX-814', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 450, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Starlight_Xpress_Trius_SX_825': {'brand': 'Starlight Xpress', 'name': 'Trius SX-825', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Starlight_Xpress_Trius_SX_46': {'brand': 'Starlight Xpress', 'name': 'Trius SX-46', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 700, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Starlight_Xpress_Ultrastar': {'brand': 'Starlight Xpress', 'name': 'Ultrastar', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 200, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Starlight_Xpress_Lodestar_X2': {'brand': 'Starlight Xpress', 'name': 'Lodestar X2', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 150, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Starlight_Xpress_CoStar': {'brand': 'Starlight Xpress', 'name': 'CoStar', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 120, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Starlight_Xpress_Lodestar_PRO': {'brand': 'Starlight Xpress', 'name': 'Lodestar PRO', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 180, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Starlight_Xpress_SXVR_H694': {'brand': 'Starlight Xpress', 'name': 'SXVR-H694', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 450, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Starlight_Xpress_SXVR_H814': {'brand': 'Starlight Xpress', 'name': 'SXVR-H814', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Starlight_Xpress_SXVR_H9': {'brand': 'Starlight Xpress', 'name': 'SXVR-H9', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 350, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Starlight_Xpress_SXVR_H18': {'brand': 'Starlight Xpress', 'name': 'SXVR-H18', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 550, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Starlight_Xpress_SXVR_H35': {'brand': 'Starlight Xpress', 'name': 'SXVR-H35', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 700, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Starlight_Xpress_SXVR_H36': {'brand': 'Starlight Xpress', 'name': 'SXVR-H36', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 750, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Starlight_Xpress_Trius_SX_56': {'brand': 'Starlight Xpress', 'name': 'Trius SX-56', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 800, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Starlight_Xpress_Trius_SX_36': {'brand': 'Starlight Xpress', 'name': 'Trius SX-36', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 600, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Starlight_Xpress_Trius_SX_26': {'brand': 'Starlight Xpress', 'name': 'Trius SX-26', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Starlight_Xpress_Trius_SX_16': {'brand': 'Starlight Xpress', 'name': 'Trius SX-16', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 350, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Starlight_Xpress_MiniStar': {'brand': 'Starlight Xpress', 'name': 'MiniStar', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 180, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Starlight_Xpress_SuperStar': {'brand': 'Starlight Xpress', 'name': 'SuperStar', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 250, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}}

    @classmethod
    def Starlight_Xpress_Trius_SX_694(cls):
        return cls.from_database(cls._DATABASE['Starlight_Xpress_Trius_SX_694'])

    @classmethod
    def Starlight_Xpress_Trius_SX_814(cls):
        return cls.from_database(cls._DATABASE['Starlight_Xpress_Trius_SX_814'])

    @classmethod
    def Starlight_Xpress_Trius_SX_825(cls):
        return cls.from_database(cls._DATABASE['Starlight_Xpress_Trius_SX_825'])

    @classmethod
    def Starlight_Xpress_Trius_SX_46(cls):
        return cls.from_database(cls._DATABASE['Starlight_Xpress_Trius_SX_46'])

    @classmethod
    def Starlight_Xpress_Ultrastar(cls):
        return cls.from_database(cls._DATABASE['Starlight_Xpress_Ultrastar'])

    @classmethod
    def Starlight_Xpress_Lodestar_X2(cls):
        return cls.from_database(cls._DATABASE['Starlight_Xpress_Lodestar_X2'])

    @classmethod
    def Starlight_Xpress_CoStar(cls):
        return cls.from_database(cls._DATABASE['Starlight_Xpress_CoStar'])

    @classmethod
    def Starlight_Xpress_Lodestar_PRO(cls):
        return cls.from_database(cls._DATABASE['Starlight_Xpress_Lodestar_PRO'])

    @classmethod
    def Starlight_Xpress_SXVR_H694(cls):
        return cls.from_database(cls._DATABASE['Starlight_Xpress_SXVR_H694'])

    @classmethod
    def Starlight_Xpress_SXVR_H814(cls):
        return cls.from_database(cls._DATABASE['Starlight_Xpress_SXVR_H814'])

    @classmethod
    def Starlight_Xpress_SXVR_H9(cls):
        return cls.from_database(cls._DATABASE['Starlight_Xpress_SXVR_H9'])

    @classmethod
    def Starlight_Xpress_SXVR_H18(cls):
        return cls.from_database(cls._DATABASE['Starlight_Xpress_SXVR_H18'])

    @classmethod
    def Starlight_Xpress_SXVR_H35(cls):
        return cls.from_database(cls._DATABASE['Starlight_Xpress_SXVR_H35'])

    @classmethod
    def Starlight_Xpress_SXVR_H36(cls):
        return cls.from_database(cls._DATABASE['Starlight_Xpress_SXVR_H36'])

    @classmethod
    def Starlight_Xpress_Trius_SX_56(cls):
        return cls.from_database(cls._DATABASE['Starlight_Xpress_Trius_SX_56'])

    @classmethod
    def Starlight_Xpress_Trius_SX_36(cls):
        return cls.from_database(cls._DATABASE['Starlight_Xpress_Trius_SX_36'])

    @classmethod
    def Starlight_Xpress_Trius_SX_26(cls):
        return cls.from_database(cls._DATABASE['Starlight_Xpress_Trius_SX_26'])

    @classmethod
    def Starlight_Xpress_Trius_SX_16(cls):
        return cls.from_database(cls._DATABASE['Starlight_Xpress_Trius_SX_16'])

    @classmethod
    def Starlight_Xpress_MiniStar(cls):
        return cls.from_database(cls._DATABASE['Starlight_Xpress_MiniStar'])

    @classmethod
    def Starlight_Xpress_SuperStar(cls):
        return cls.from_database(cls._DATABASE['Starlight_Xpress_SuperStar'])