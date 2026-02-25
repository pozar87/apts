from ..base import Camera

class GenericCamera(Camera):

    @classmethod
    def OM_System_Olympus_OM_1(cls):
        return cls.from_database(cls._DATABASE['OM_System_Olympus_OM_1'])

    @classmethod
    def OM_System_Olympus_OM_1_II(cls):
        return cls.from_database(cls._DATABASE['OM_System_Olympus_OM_1_II'])

    @classmethod
    def OM_System_Olympus_E_M1_III(cls):
        return cls.from_database(cls._DATABASE['OM_System_Olympus_E_M1_III'])

    @classmethod
    def OM_System_Olympus_E_M1_II(cls):
        return cls.from_database(cls._DATABASE['OM_System_Olympus_E_M1_II'])

    @classmethod
    def OM_System_Olympus_E_M5_III(cls):
        return cls.from_database(cls._DATABASE['OM_System_Olympus_E_M5_III'])

    @classmethod
    def OM_System_Olympus_E_M10_IV(cls):
        return cls.from_database(cls._DATABASE['OM_System_Olympus_E_M10_IV'])

    @classmethod
    def OM_System_Olympus_E_PL10(cls):
        return cls.from_database(cls._DATABASE['OM_System_Olympus_E_PL10'])