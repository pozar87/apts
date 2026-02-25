from ..base import Camera

class QsiCamera(Camera):
    _DATABASE = {'QSI_690ws': {'brand': 'QSI', 'name': '690ws', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 800, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QSI_690wsg': {'brand': 'QSI', 'name': '690wsg', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 850, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QSI_660ws': {'brand': 'QSI', 'name': '660ws', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 700, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QSI_660wsg': {'brand': 'QSI', 'name': '660wsg', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 750, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QSI_583ws': {'brand': 'QSI', 'name': '583ws', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 600, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QSI_583wsg': {'brand': 'QSI', 'name': '583wsg', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 650, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}, 'QSI_616ws': {'brand': 'QSI', 'name': '616ws', 'type': 'type_camera', 'optical_length': 6.5, 'mass': 700, 'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': 'end'}}

    @classmethod
    def QSI_690ws(cls):
        return cls.from_database(cls._DATABASE['QSI_690ws'])

    @classmethod
    def QSI_690wsg(cls):
        return cls.from_database(cls._DATABASE['QSI_690wsg'])

    @classmethod
    def QSI_660ws(cls):
        return cls.from_database(cls._DATABASE['QSI_660ws'])

    @classmethod
    def QSI_660wsg(cls):
        return cls.from_database(cls._DATABASE['QSI_660wsg'])

    @classmethod
    def QSI_583ws(cls):
        return cls.from_database(cls._DATABASE['QSI_583ws'])

    @classmethod
    def QSI_583wsg(cls):
        return cls.from_database(cls._DATABASE['QSI_583wsg'])

    @classmethod
    def QSI_616ws(cls):
        return cls.from_database(cls._DATABASE['QSI_616ws'])