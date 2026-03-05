from ..base import Telescope

class CoronadoTelescope(Telescope):
    _DATABASE = {
        'Coronado_PST_40mm': {'brand': 'Coronado', 'name': 'PST 40mm', 'type': 'type_refractor', 'optical_length': 0, 'mass': 1450, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 40, 'focal_length_mm': 400}, # Verified via Coronado specs
        'Coronado_SolarMax_II_60': {'brand': 'Coronado', 'name': 'SolarMax II 60', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2700, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 60, 'focal_length_mm': 400}, # Verified via Coronado specs
        'Coronado_SolarMax_II_90': {'brand': 'Coronado', 'name': 'SolarMax II 90', 'type': 'type_refractor', 'optical_length': 0, 'mass': 5500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 90, 'focal_length_mm': 800},
        'Coronado_SolarMax_III_70': {'brand': 'Coronado', 'name': 'SolarMax III 70', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 70, 'focal_length_mm': 400},
        'Coronado_SolarMax_III_90': {'brand': 'Coronado', 'name': 'SolarMax III 90', 'type': 'type_refractor', 'optical_length': 0, 'mass': 6000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 90, 'focal_length_mm': 800},
    }

    @classmethod
    def Coronado_PST_40mm(cls):
        return cls.from_database(cls._DATABASE['Coronado_PST_40mm'])

    @classmethod
    def Coronado_SolarMax_II_60(cls):
        return cls.from_database(cls._DATABASE['Coronado_SolarMax_II_60'])

    @classmethod
    def Coronado_SolarMax_II_90(cls):
        return cls.from_database(cls._DATABASE['Coronado_SolarMax_II_90'])

    @classmethod
    def Coronado_SolarMax_III_70(cls):
        return cls.from_database(cls._DATABASE['Coronado_SolarMax_III_70'])

    @classmethod
    def Coronado_SolarMax_III_90(cls):
        return cls.from_database(cls._DATABASE['Coronado_SolarMax_III_90'])
