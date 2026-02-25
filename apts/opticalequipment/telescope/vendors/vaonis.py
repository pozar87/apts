from ..base import Telescope

class VaonisTelescope(Telescope):
    _DATABASE = {'Vaonis_Stellina': {'brand': 'Vaonis', 'name': 'Stellina', 'type': 'type_telescope', 'optical_length': 0, 'mass': 4500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vaonis_Vespera': {'brand': 'Vaonis', 'name': 'Vespera', 'type': 'type_telescope', 'optical_length': 0, 'mass': 2500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vaonis_Vespera_Pro': {'brand': 'Vaonis', 'name': 'Vespera Pro', 'type': 'type_telescope', 'optical_length': 0, 'mass': 3500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Vaonis_Hyperia': {'brand': 'Vaonis', 'name': 'Hyperia', 'type': 'type_telescope', 'optical_length': 0, 'mass': 6000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Vaonis_Stellina(cls):
        return cls.from_database(cls._DATABASE['Vaonis_Stellina'])

    @classmethod
    def Vaonis_Vespera(cls):
        return cls.from_database(cls._DATABASE['Vaonis_Vespera'])

    @classmethod
    def Vaonis_Vespera_Pro(cls):
        return cls.from_database(cls._DATABASE['Vaonis_Vespera_Pro'])

    @classmethod
    def Vaonis_Hyperia(cls):
        return cls.from_database(cls._DATABASE['Vaonis_Hyperia'])