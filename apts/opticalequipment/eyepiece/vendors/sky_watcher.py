from ...abstract import OutputOpticalEqipment
from ....constants import GraphConstants, OpticalType
from ....units import get_unit_registry
from ....utils import ConnectionType, Gender
from ..base import Eyepiece

class Sky_watcherEyepiece(Eyepiece):
    _DATABASE = {'Sky_Watcher_Aero_ED_2mm': {'brand': 'Sky-Watcher', 'name': 'Aero ED 2mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 180, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Aero_ED_3_5mm': {'brand': 'Sky-Watcher', 'name': 'Aero ED 3.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 190, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Aero_ED_5mm': {'brand': 'Sky-Watcher', 'name': 'Aero ED 5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 200, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Aero_ED_7mm': {'brand': 'Sky-Watcher', 'name': 'Aero ED 7mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 210, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Aero_ED_9mm': {'brand': 'Sky-Watcher', 'name': 'Aero ED 9mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 220, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Aero_ED_11mm': {'brand': 'Sky-Watcher', 'name': 'Aero ED 11mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 230, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Aero_ED_15mm': {'brand': 'Sky-Watcher', 'name': 'Aero ED 15mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 250, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Aero_ED_20mm': {'brand': 'Sky-Watcher', 'name': 'Aero ED 20mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 280, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Nirvana_UWA_15mm': {'brand': 'Sky-Watcher', 'name': 'Nirvana UWA 15mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 350, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Nirvana_UWA_20mm': {'brand': 'Sky-Watcher', 'name': 'Nirvana UWA 20mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 400, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Nirvana_UWA_23mm': {'brand': 'Sky-Watcher', 'name': 'Nirvana UWA 23mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 450, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Nirvana_UWA_31mm': {'brand': 'Sky-Watcher', 'name': 'Nirvana UWA 31mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 550, 'tside_thread': '2"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Super_Plossl_6mm': {'brand': 'Sky-Watcher', 'name': 'Super Plossl 6mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 90, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Super_Plossl_10mm': {'brand': 'Sky-Watcher', 'name': 'Super Plossl 10mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 95, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Super_Plossl_15mm': {'brand': 'Sky-Watcher', 'name': 'Super Plossl 15mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 100, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Super_Plossl_20mm': {'brand': 'Sky-Watcher', 'name': 'Super Plossl 20mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 110, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Super_Plossl_25mm': {'brand': 'Sky-Watcher', 'name': 'Super Plossl 25mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 120, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Super_Plossl_32mm': {'brand': 'Sky-Watcher', 'name': 'Super Plossl 32mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 150, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Plossl_6mm': {'brand': 'Sky-Watcher', 'name': 'Plossl 6mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 90, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Plossl_9mm': {'brand': 'Sky-Watcher', 'name': 'Plossl 9mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 95, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Plossl_12mm': {'brand': 'Sky-Watcher', 'name': 'Plossl 12mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 100, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Plossl_15mm': {'brand': 'Sky-Watcher', 'name': 'Plossl 15mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 105, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Plossl_20mm': {'brand': 'Sky-Watcher', 'name': 'Plossl 20mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 115, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Plossl_25mm': {'brand': 'Sky-Watcher', 'name': 'Plossl 25mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 125, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_7_2_21_5mm_Zoom': {'brand': 'Sky-Watcher', 'name': '7.2-21.5mm Zoom', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 300, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Starguider_Dual_ED_2_5mm': {'brand': 'Sky-Watcher', 'name': 'Starguider Dual ED 2.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 170, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Starguider_Dual_ED_3_2mm': {'brand': 'Sky-Watcher', 'name': 'Starguider Dual ED 3.2mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 175, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Starguider_Dual_ED_4mm': {'brand': 'Sky-Watcher', 'name': 'Starguider Dual ED 4mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 180, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Starguider_Dual_ED_5mm': {'brand': 'Sky-Watcher', 'name': 'Starguider Dual ED 5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 185, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Starguider_Dual_ED_6mm': {'brand': 'Sky-Watcher', 'name': 'Starguider Dual ED 6mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 192, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Starguider_Dual_ED_8mm': {'brand': 'Sky-Watcher', 'name': 'Starguider Dual ED 8mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 200, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Starguider_Dual_ED_10mm': {'brand': 'Sky-Watcher', 'name': 'Starguider Dual ED 10mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 210, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Starguider_Dual_ED_15mm': {'brand': 'Sky-Watcher', 'name': 'Starguider Dual ED 15mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 235, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Starguider_Dual_ED_20mm': {'brand': 'Sky-Watcher', 'name': 'Starguider Dual ED 20mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 265, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Starguider_Dual_ED_25mm': {'brand': 'Sky-Watcher', 'name': 'Starguider Dual ED 25mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 290, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Long_Eye_Relief_4_5mm': {'brand': 'Sky-Watcher', 'name': 'Long Eye Relief 4.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 130, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Long_Eye_Relief_6mm': {'brand': 'Sky-Watcher', 'name': 'Long Eye Relief 6mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 135, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Long_Eye_Relief_8mm': {'brand': 'Sky-Watcher', 'name': 'Long Eye Relief 8mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 145, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Long_Eye_Relief_10mm': {'brand': 'Sky-Watcher', 'name': 'Long Eye Relief 10mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 155, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Long_Eye_Relief_12_5mm': {'brand': 'Sky-Watcher', 'name': 'Long Eye Relief 12.5mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 165, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Long_Eye_Relief_15mm': {'brand': 'Sky-Watcher', 'name': 'Long Eye Relief 15mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 175, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Long_Eye_Relief_18mm': {'brand': 'Sky-Watcher', 'name': 'Long Eye Relief 18mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 190, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Long_Eye_Relief_21mm': {'brand': 'Sky-Watcher', 'name': 'Long Eye Relief 21mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 210, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Long_Eye_Relief_25mm': {'brand': 'Sky-Watcher', 'name': 'Long Eye Relief 25mm', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 240, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_12mm_Reticle_Eyepiece_1_25': {'brand': 'Sky-Watcher', 'name': '12mm Reticle Eyepiece (1.25")', 'type': 'type_eyepiece', 'optical_length': 0, 'mass': 130, 'tside_thread': '1.25"', 'tside_gender': 'Male', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Sky_Watcher_Aero_ED_2mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Aero_ED_2mm'])

    @classmethod
    def Sky_Watcher_Aero_ED_3_5mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Aero_ED_3_5mm'])

    @classmethod
    def Sky_Watcher_Aero_ED_5mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Aero_ED_5mm'])

    @classmethod
    def Sky_Watcher_Aero_ED_7mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Aero_ED_7mm'])

    @classmethod
    def Sky_Watcher_Aero_ED_9mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Aero_ED_9mm'])

    @classmethod
    def Sky_Watcher_Aero_ED_11mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Aero_ED_11mm'])

    @classmethod
    def Sky_Watcher_Aero_ED_15mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Aero_ED_15mm'])

    @classmethod
    def Sky_Watcher_Aero_ED_20mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Aero_ED_20mm'])

    @classmethod
    def Sky_Watcher_Nirvana_UWA_15mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Nirvana_UWA_15mm'])

    @classmethod
    def Sky_Watcher_Nirvana_UWA_20mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Nirvana_UWA_20mm'])

    @classmethod
    def Sky_Watcher_Nirvana_UWA_23mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Nirvana_UWA_23mm'])

    @classmethod
    def Sky_Watcher_Nirvana_UWA_31mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Nirvana_UWA_31mm'])

    @classmethod
    def Sky_Watcher_Super_Plossl_6mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Super_Plossl_6mm'])

    @classmethod
    def Sky_Watcher_Super_Plossl_10mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Super_Plossl_10mm'])

    @classmethod
    def Sky_Watcher_Super_Plossl_15mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Super_Plossl_15mm'])

    @classmethod
    def Sky_Watcher_Super_Plossl_20mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Super_Plossl_20mm'])

    @classmethod
    def Sky_Watcher_Super_Plossl_25mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Super_Plossl_25mm'])

    @classmethod
    def Sky_Watcher_Super_Plossl_32mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Super_Plossl_32mm'])

    @classmethod
    def Sky_Watcher_Plossl_6mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Plossl_6mm'])

    @classmethod
    def Sky_Watcher_Plossl_9mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Plossl_9mm'])

    @classmethod
    def Sky_Watcher_Plossl_12mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Plossl_12mm'])

    @classmethod
    def Sky_Watcher_Plossl_15mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Plossl_15mm'])

    @classmethod
    def Sky_Watcher_Plossl_20mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Plossl_20mm'])

    @classmethod
    def Sky_Watcher_Plossl_25mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Plossl_25mm'])

    @classmethod
    def Sky_Watcher_7_2_21_5mm_Zoom(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_7_2_21_5mm_Zoom'])

    @classmethod
    def Sky_Watcher_Starguider_Dual_ED_2_5mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Starguider_Dual_ED_2_5mm'])

    @classmethod
    def Sky_Watcher_Starguider_Dual_ED_3_2mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Starguider_Dual_ED_3_2mm'])

    @classmethod
    def Sky_Watcher_Starguider_Dual_ED_4mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Starguider_Dual_ED_4mm'])

    @classmethod
    def Sky_Watcher_Starguider_Dual_ED_5mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Starguider_Dual_ED_5mm'])

    @classmethod
    def Sky_Watcher_Starguider_Dual_ED_6mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Starguider_Dual_ED_6mm'])

    @classmethod
    def Sky_Watcher_Starguider_Dual_ED_8mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Starguider_Dual_ED_8mm'])

    @classmethod
    def Sky_Watcher_Starguider_Dual_ED_10mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Starguider_Dual_ED_10mm'])

    @classmethod
    def Sky_Watcher_Starguider_Dual_ED_15mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Starguider_Dual_ED_15mm'])

    @classmethod
    def Sky_Watcher_Starguider_Dual_ED_20mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Starguider_Dual_ED_20mm'])

    @classmethod
    def Sky_Watcher_Starguider_Dual_ED_25mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Starguider_Dual_ED_25mm'])

    @classmethod
    def Sky_Watcher_Long_Eye_Relief_4_5mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Long_Eye_Relief_4_5mm'])

    @classmethod
    def Sky_Watcher_Long_Eye_Relief_6mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Long_Eye_Relief_6mm'])

    @classmethod
    def Sky_Watcher_Long_Eye_Relief_8mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Long_Eye_Relief_8mm'])

    @classmethod
    def Sky_Watcher_Long_Eye_Relief_10mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Long_Eye_Relief_10mm'])

    @classmethod
    def Sky_Watcher_Long_Eye_Relief_12_5mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Long_Eye_Relief_12_5mm'])

    @classmethod
    def Sky_Watcher_Long_Eye_Relief_15mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Long_Eye_Relief_15mm'])

    @classmethod
    def Sky_Watcher_Long_Eye_Relief_18mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Long_Eye_Relief_18mm'])

    @classmethod
    def Sky_Watcher_Long_Eye_Relief_21mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Long_Eye_Relief_21mm'])

    @classmethod
    def Sky_Watcher_Long_Eye_Relief_25mm(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Long_Eye_Relief_25mm'])

    @classmethod
    def Sky_Watcher_12mm_Reticle_Eyepiece_1_25(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_12mm_Reticle_Eyepiece_1_25'])