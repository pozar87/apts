from ..base import Camera

class BresserCamera(Camera):
    _DATABASE = {'Bresser_MikroCamII_5MP': {'brand': 'Bresser', 'name': 'MikroCamII 5MP', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 100, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Bresser_MikroCamII_10MP': {'brand': 'Bresser', 'name': 'MikroCamII 10MP', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 120, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Bresser_Full_HD_Deep_Sky': {'brand': 'Bresser', 'name': 'Full HD Deep Sky', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 300, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Bresser_Astro_2MP_Guide': {'brand': 'Bresser', 'name': 'Astro 2MP Guide', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}}

    @classmethod
    def Bresser_MikroCamII_5MP(cls):
        return cls.from_database(cls._DATABASE['Bresser_MikroCamII_5MP'])

    @classmethod
    def Bresser_MikroCamII_10MP(cls):
        return cls.from_database(cls._DATABASE['Bresser_MikroCamII_10MP'])

    @classmethod
    def Bresser_Full_HD_Deep_Sky(cls):
        return cls.from_database(cls._DATABASE['Bresser_Full_HD_Deep_Sky'])

    @classmethod
    def Bresser_Astro_2MP_Guide(cls):
        return cls.from_database(cls._DATABASE['Bresser_Astro_2MP_Guide'])