from ..base import Camera

class Explore_scientificCamera(Camera):
    _DATABASE = {'Explore_Scientific_5MP_Guide_Camera': {'brand': 'Explore Scientific', 'name': '5MP Guide Camera', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 80, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Explore_Scientific_3MP_USB3_Planetary': {'brand': 'Explore Scientific', 'name': '3MP USB3 Planetary', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 100, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Explore_Scientific_Starlight_571C': {'brand': 'Explore Scientific', 'name': 'Starlight 571C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 600, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Explore_Scientific_Starlight_533C': {'brand': 'Explore Scientific', 'name': 'Starlight 533C', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 450, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'Explore_Scientific_Starlight_585C': {'brand': 'Explore Scientific', 'name': 'Starlight 585C', 'type': 'type_camera', 'optical_length': 12.5, 'mass': 160, 'tside_thread': 'CS', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}}

    @classmethod
    def Explore_Scientific_5MP_Guide_Camera(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_5MP_Guide_Camera'])

    @classmethod
    def Explore_Scientific_3MP_USB3_Planetary(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_3MP_USB3_Planetary'])

    @classmethod
    def Explore_Scientific_Starlight_571C(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_Starlight_571C'])

    @classmethod
    def Explore_Scientific_Starlight_533C(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_Starlight_533C'])

    @classmethod
    def Explore_Scientific_Starlight_585C(cls):
        return cls.from_database(cls._DATABASE['Explore_Scientific_Starlight_585C'])