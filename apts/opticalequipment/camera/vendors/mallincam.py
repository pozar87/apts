from ..base import Camera

class MallincamCamera(Camera):
    _DATABASE = {'Mallincam_SkyRaider_DS26000C': {'brand': 'Mallincam', 'name': 'SkyRaider DS26000C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 700, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Mallincam_SkyRaider_DS16000C': {'brand': 'Mallincam', 'name': 'SkyRaider DS16000C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Mallincam_SkyRaider_DS2100C': {'brand': 'Mallincam', 'name': 'SkyRaider DS2100C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 350, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Mallincam_SkyRaider_DS287C': {'brand': 'Mallincam', 'name': 'SkyRaider DS287C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 250, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Mallincam_Xtreme_Solar_System_Imager': {'brand': 'Mallincam', 'name': 'Xtreme Solar System Imager', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 120, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Mallincam_SkyRaider_DS26C': {'brand': 'Mallincam', 'name': 'SkyRaider DS26C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 500, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Mallincam_SkyRaider_DS10C': {'brand': 'Mallincam', 'name': 'SkyRaider DS10C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 300, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Mallincam_Xtreme': {'brand': 'Mallincam', 'name': 'Xtreme', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 350, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Mallincam_Universe': {'brand': 'Mallincam', 'name': 'Universe', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 600, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Mallincam_Micro': {'brand': 'Mallincam', 'name': 'Micro', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 120, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}}

    @classmethod
    def Mallincam_SkyRaider_DS26000C(cls):
        return cls.from_database(cls._DATABASE['Mallincam_SkyRaider_DS26000C'])

    @classmethod
    def Mallincam_SkyRaider_DS16000C(cls):
        return cls.from_database(cls._DATABASE['Mallincam_SkyRaider_DS16000C'])

    @classmethod
    def Mallincam_SkyRaider_DS2100C(cls):
        return cls.from_database(cls._DATABASE['Mallincam_SkyRaider_DS2100C'])

    @classmethod
    def Mallincam_SkyRaider_DS287C(cls):
        return cls.from_database(cls._DATABASE['Mallincam_SkyRaider_DS287C'])

    @classmethod
    def Mallincam_Xtreme_Solar_System_Imager(cls):
        return cls.from_database(cls._DATABASE['Mallincam_Xtreme_Solar_System_Imager'])

    @classmethod
    def Mallincam_SkyRaider_DS26C(cls):
        return cls.from_database(cls._DATABASE['Mallincam_SkyRaider_DS26C'])

    @classmethod
    def Mallincam_SkyRaider_DS10C(cls):
        return cls.from_database(cls._DATABASE['Mallincam_SkyRaider_DS10C'])

    @classmethod
    def Mallincam_Xtreme(cls):
        return cls.from_database(cls._DATABASE['Mallincam_Xtreme'])

    @classmethod
    def Mallincam_Universe(cls):
        return cls.from_database(cls._DATABASE['Mallincam_Universe'])

    @classmethod
    def Mallincam_Micro(cls):
        return cls.from_database(cls._DATABASE['Mallincam_Micro'])