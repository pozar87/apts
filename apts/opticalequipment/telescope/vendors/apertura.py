from ..base import Telescope

class AperturaTelescope(Telescope):
    _DATABASE = {
        'Apertura_AD6_Dobsonian': {'brand': 'Apertura', 'name': 'AD6 Dobsonian', 'type': 'newtonian_reflector', 'optical_length': 0, 'mass': 8255, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 152, 'focal_length_mm': 1200, 'central_obstruction_mm': 42}, # Verified via specs (18.2 lbs OTA)
        'Apertura_AD8_Dobsonian': {'brand': 'Apertura', 'name': 'AD8 Dobsonian', 'type': 'newtonian_reflector', 'optical_length': 0, 'mass': 11113, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 203, 'focal_length_mm': 1200, 'central_obstruction_mm': 47}, # Verified via specs (24.5 lbs OTA)
        'Apertura_AD10_Dobsonian': {'brand': 'Apertura', 'name': 'AD10 Dobsonian', 'type': 'newtonian_reflector', 'optical_length': 0, 'mass': 15785, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 254, 'focal_length_mm': 1250, 'central_obstruction_mm': 63}, # Verified via specs (34.8 lbs OTA)
        'Apertura_AD12_Dobsonian': {'brand': 'Apertura', 'name': 'AD12 Dobsonian', 'type': 'newtonian_reflector', 'optical_length': 0, 'mass': 21682, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 305, 'focal_length_mm': 1520, 'central_obstruction_mm': 70}, # Verified via specs (47.8 lbs OTA)
        'Apertura_AD16_Dobsonian': {'brand': 'Apertura', 'name': 'AD16 Dobsonian', 'type': 'newtonian_reflector', 'optical_length': 0, 'mass': 34246, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 406, 'focal_length_mm': 1800, 'central_obstruction_mm': 88}, # Verified via specs (75.5 lbs OTA)
    }

    @classmethod
    def Apertura_AD6_Dobsonian(cls):
        return cls.from_database(cls._DATABASE['Apertura_AD6_Dobsonian'])

    @classmethod
    def Apertura_AD8_Dobsonian(cls):
        return cls.from_database(cls._DATABASE['Apertura_AD8_Dobsonian'])

    @classmethod
    def Apertura_AD10_Dobsonian(cls):
        return cls.from_database(cls._DATABASE['Apertura_AD10_Dobsonian'])

    @classmethod
    def Apertura_AD12_Dobsonian(cls):
        return cls.from_database(cls._DATABASE['Apertura_AD12_Dobsonian'])

    @classmethod
    def Apertura_AD14_Dobsonian(cls):
        return cls.from_database(cls._DATABASE['Apertura_AD14_Dobsonian'])

    @classmethod
    def Apertura_AD16_Dobsonian(cls):
        return cls.from_database(cls._DATABASE['Apertura_AD16_Dobsonian'])