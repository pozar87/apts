from ..base import Telescope

class Sky_watcherTelescope(Telescope):
    _DATABASE = {'Sky_Watcher_Esprit_80ED': {'brand': 'Sky-Watcher', 'name': 'Esprit 80ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Esprit_100ED': {'brand': 'Sky-Watcher', 'name': 'Esprit 100ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 5400, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Esprit_120ED': {'brand': 'Sky-Watcher', 'name': 'Esprit 120ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 7800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Esprit_150ED': {'brand': 'Sky-Watcher', 'name': 'Esprit 150ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 12000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Evostar_72ED': {'brand': 'Sky-Watcher', 'name': 'Evostar 72ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 1900, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Evostar_80ED': {'brand': 'Sky-Watcher', 'name': 'Evostar 80ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Evostar_100ED': {'brand': 'Sky-Watcher', 'name': 'Evostar 100ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Evostar_120ED': {'brand': 'Sky-Watcher', 'name': 'Evostar 120ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 5400, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Evostar_72ED_DS_Pro': {'brand': 'Sky-Watcher', 'name': 'Evostar 72ED DS-Pro', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Evostar_80ED_DS_Pro': {'brand': 'Sky-Watcher', 'name': 'Evostar 80ED DS-Pro', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Evostar_100ED_DS_Pro': {'brand': 'Sky-Watcher', 'name': 'Evostar 100ED DS-Pro', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Evostar_150ED': {'brand': 'Sky-Watcher', 'name': 'Evostar 150ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 8000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Quattro_150P': {'brand': 'Sky-Watcher', 'name': 'Quattro 150P', 'type': 'newtonian_reflector', 'optical_length': 0, 'mass': 5700, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 150, 'focal_length_mm': 600, 'central_obstruction_mm': 52}, 'Sky_Watcher_Quattro_200P': {'brand': 'Sky-Watcher', 'name': 'Quattro 200P', 'type': 'newtonian_reflector', 'optical_length': 0, 'mass': 9500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 200, 'focal_length_mm': 800, 'central_obstruction_mm': 70}, 'Sky_Watcher_Quattro_250P': {'brand': 'Sky-Watcher', 'name': 'Quattro 250P', 'type': 'newtonian_reflector', 'optical_length': 0, 'mass': 15000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 250, 'focal_length_mm': 1000, 'central_obstruction_mm': 82}, 'Sky_Watcher_Quattro_300P': {'brand': 'Sky-Watcher', 'name': 'Quattro 300P', 'type': 'newtonian_reflector', 'optical_length': 0, 'mass': 23000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 300, 'focal_length_mm': 1200, 'central_obstruction_mm': 100}, 'Sky_Watcher_150PDS_Newtonian': {'brand': 'Sky-Watcher', 'name': '150PDS Newtonian', 'type': 'type_telescope', 'optical_length': 0, 'mass': 4800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_200PDS_Newtonian': {'brand': 'Sky-Watcher', 'name': '200PDS Newtonian', 'type': 'type_telescope', 'optical_length': 0, 'mass': 8800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_250PDS_Newtonian': {'brand': 'Sky-Watcher', 'name': '250PDS Newtonian', 'type': 'type_telescope', 'optical_length': 0, 'mass': 11500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Explorer_130P': {'brand': 'Sky-Watcher', 'name': 'Explorer 130P', 'type': 'type_telescope', 'optical_length': 0, 'mass': 3200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Explorer_150P': {'brand': 'Sky-Watcher', 'name': 'Explorer 150P', 'type': 'type_telescope', 'optical_length': 0, 'mass': 5200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Explorer_200P': {'brand': 'Sky-Watcher', 'name': 'Explorer 200P', 'type': 'type_telescope', 'optical_length': 0, 'mass': 8500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Explorer_250P': {'brand': 'Sky-Watcher', 'name': 'Explorer 250P', 'type': 'type_telescope', 'optical_length': 0, 'mass': 11000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Explorer_300P': {'brand': 'Sky-Watcher', 'name': 'Explorer 300P', 'type': 'type_telescope', 'optical_length': 0, 'mass': 16000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Skyliner_150P': {'brand': 'Sky-Watcher', 'name': 'Skyliner 150P', 'type': 'type_telescope', 'optical_length': 0, 'mass': 5000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Skyliner_200P': {'brand': 'Sky-Watcher', 'name': 'Skyliner 200P', 'type': 'type_telescope', 'optical_length': 0, 'mass': 8500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Skyliner_250P': {'brand': 'Sky-Watcher', 'name': 'Skyliner 250P', 'type': 'type_telescope', 'optical_length': 0, 'mass': 11600, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Skyliner_300P': {'brand': 'Sky-Watcher', 'name': 'Skyliner 300P', 'type': 'type_telescope', 'optical_length': 0, 'mass': 16000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Skyliner_400P': {'brand': 'Sky-Watcher', 'name': 'Skyliner 400P', 'type': 'type_telescope', 'optical_length': 0, 'mass': 25000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Heritage_130P': {'brand': 'Sky-Watcher', 'name': 'Heritage 130P', 'type': 'type_telescope', 'optical_length': 0, 'mass': 3000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Heritage_150P': {'brand': 'Sky-Watcher', 'name': 'Heritage 150P', 'type': 'type_telescope', 'optical_length': 0, 'mass': 4500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Mak_90': {'brand': 'Sky-Watcher', 'name': 'Mak-90', 'type': 'type_telescope', 'optical_length': 0, 'mass': 1600, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Mak_102': {'brand': 'Sky-Watcher', 'name': 'Mak-102', 'type': 'type_telescope', 'optical_length': 0, 'mass': 2000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Mak_127': {'brand': 'Sky-Watcher', 'name': 'Mak-127', 'type': 'type_telescope', 'optical_length': 0, 'mass': 3500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Mak_150': {'brand': 'Sky-Watcher', 'name': 'Mak-150', 'type': 'type_telescope', 'optical_length': 0, 'mass': 5000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Mak_180': {'brand': 'Sky-Watcher', 'name': 'Mak-180', 'type': 'type_telescope', 'optical_length': 0, 'mass': 6300, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Heritage_76_Mini': {'brand': 'Sky-Watcher', 'name': 'Heritage 76 Mini', 'type': 'type_telescope', 'optical_length': 0, 'mass': 1600, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Heritage_100P': {'brand': 'Sky-Watcher', 'name': 'Heritage 100P', 'type': 'type_telescope', 'optical_length': 0, 'mass': 2200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Heritage_130P_FlexTube': {'brand': 'Sky-Watcher', 'name': 'Heritage 130P FlexTube', 'type': 'type_telescope', 'optical_length': 0, 'mass': 3200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Heritage_150P_FlexTube': {'brand': 'Sky-Watcher', 'name': 'Heritage 150P FlexTube', 'type': 'type_telescope', 'optical_length': 0, 'mass': 4800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Star_Discovery_130i': {'brand': 'Sky-Watcher', 'name': 'Star Discovery 130i', 'type': 'type_telescope', 'optical_length': 0, 'mass': 3300, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Star_Discovery_150i': {'brand': 'Sky-Watcher', 'name': 'Star Discovery 150i', 'type': 'type_telescope', 'optical_length': 0, 'mass': 5000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Starquest_130P': {'brand': 'Sky-Watcher', 'name': 'Starquest 130P', 'type': 'type_telescope', 'optical_length': 0, 'mass': 3200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Virtuoso_GTi_130P': {'brand': 'Sky-Watcher', 'name': 'Virtuoso GTi 130P', 'type': 'type_telescope', 'optical_length': 0, 'mass': 3300, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Virtuoso_GTi_150P': {'brand': 'Sky-Watcher', 'name': 'Virtuoso GTi 150P', 'type': 'type_telescope', 'optical_length': 0, 'mass': 4800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Star_Discovery_150P': {'brand': 'Sky-Watcher', 'name': 'Star Discovery 150P', 'type': 'type_telescope', 'optical_length': 0, 'mass': 5000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Star_Discovery_200P': {'brand': 'Sky-Watcher', 'name': 'Star Discovery 200P', 'type': 'type_telescope', 'optical_length': 0, 'mass': 8200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_AZ_EQ5_GT_8_Newton': {'brand': 'Sky-Watcher', 'name': 'AZ-EQ5 GT 8" Newton', 'type': 'type_telescope', 'optical_length': 0, 'mass': 8500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_AZ_EQ6_Pro_8_Newton': {'brand': 'Sky-Watcher', 'name': 'AZ-EQ6 Pro 8" Newton', 'type': 'type_telescope', 'optical_length': 0, 'mass': 8600, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Black_Diamond_ED80': {'brand': 'Sky-Watcher', 'name': 'Black Diamond ED80', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2600, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Black_Diamond_ED100': {'brand': 'Sky-Watcher', 'name': 'Black Diamond ED100', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4300, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Black_Diamond_ED120': {'brand': 'Sky-Watcher', 'name': 'Black Diamond ED120', 'type': 'type_refractor', 'optical_length': 0, 'mass': 6500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Sky_Watcher_Esprit_80ED(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Esprit_80ED'])

    @classmethod
    def Sky_Watcher_Esprit_100ED(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Esprit_100ED'])

    @classmethod
    def Sky_Watcher_Esprit_120ED(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Esprit_120ED'])

    @classmethod
    def Sky_Watcher_Esprit_150ED(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Esprit_150ED'])

    @classmethod
    def Sky_Watcher_Evostar_72ED(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Evostar_72ED'])

    @classmethod
    def Sky_Watcher_Evostar_80ED(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Evostar_80ED'])

    @classmethod
    def Sky_Watcher_Evostar_100ED(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Evostar_100ED'])

    @classmethod
    def Sky_Watcher_Evostar_120ED(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Evostar_120ED'])

    @classmethod
    def Sky_Watcher_Evostar_72ED_DS_Pro(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Evostar_72ED_DS_Pro'])

    @classmethod
    def Sky_Watcher_Evostar_80ED_DS_Pro(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Evostar_80ED_DS_Pro'])

    @classmethod
    def Sky_Watcher_Evostar_100ED_DS_Pro(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Evostar_100ED_DS_Pro'])

    @classmethod
    def Sky_Watcher_Evostar_150ED(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Evostar_150ED'])

    @classmethod
    def Sky_Watcher_Quattro_150P(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Quattro_150P'])

    @classmethod
    def Sky_Watcher_Quattro_200P(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Quattro_200P'])

    @classmethod
    def Sky_Watcher_Quattro_250P(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Quattro_250P'])

    @classmethod
    def Sky_Watcher_Quattro_300P(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Quattro_300P'])

    @classmethod
    def Sky_Watcher_150PDS_Newtonian(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_150PDS_Newtonian'])

    @classmethod
    def Sky_Watcher_200PDS_Newtonian(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_200PDS_Newtonian'])

    @classmethod
    def Sky_Watcher_250PDS_Newtonian(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_250PDS_Newtonian'])

    @classmethod
    def Sky_Watcher_Explorer_130P(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Explorer_130P'])

    @classmethod
    def Sky_Watcher_Explorer_150P(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Explorer_150P'])

    @classmethod
    def Sky_Watcher_Explorer_200P(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Explorer_200P'])

    @classmethod
    def Sky_Watcher_Explorer_250P(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Explorer_250P'])

    @classmethod
    def Sky_Watcher_Explorer_300P(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Explorer_300P'])

    @classmethod
    def Sky_Watcher_Skyliner_150P(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Skyliner_150P'])

    @classmethod
    def Sky_Watcher_Skyliner_200P(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Skyliner_200P'])

    @classmethod
    def Sky_Watcher_Skyliner_250P(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Skyliner_250P'])

    @classmethod
    def Sky_Watcher_Skyliner_300P(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Skyliner_300P'])

    @classmethod
    def Sky_Watcher_Skyliner_400P(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Skyliner_400P'])

    @classmethod
    def Sky_Watcher_Heritage_130P(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Heritage_130P'])

    @classmethod
    def Sky_Watcher_Heritage_150P(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Heritage_150P'])

    @classmethod
    def Sky_Watcher_Mak_90(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Mak_90'])

    @classmethod
    def Sky_Watcher_Mak_102(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Mak_102'])

    @classmethod
    def Sky_Watcher_Mak_127(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Mak_127'])

    @classmethod
    def Sky_Watcher_Mak_150(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Mak_150'])

    @classmethod
    def Sky_Watcher_Mak_180(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Mak_180'])

    @classmethod
    def Sky_Watcher_Heritage_76_Mini(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Heritage_76_Mini'])

    @classmethod
    def Sky_Watcher_Heritage_100P(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Heritage_100P'])

    @classmethod
    def Sky_Watcher_Heritage_130P_FlexTube(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Heritage_130P_FlexTube'])

    @classmethod
    def Sky_Watcher_Heritage_150P_FlexTube(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Heritage_150P_FlexTube'])

    @classmethod
    def Sky_Watcher_Star_Discovery_130i(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Star_Discovery_130i'])

    @classmethod
    def Sky_Watcher_Star_Discovery_150i(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Star_Discovery_150i'])

    @classmethod
    def Sky_Watcher_Starquest_130P(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Starquest_130P'])

    @classmethod
    def Sky_Watcher_Virtuoso_GTi_130P(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Virtuoso_GTi_130P'])

    @classmethod
    def Sky_Watcher_Virtuoso_GTi_150P(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Virtuoso_GTi_150P'])

    @classmethod
    def Sky_Watcher_Star_Discovery_150P(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Star_Discovery_150P'])

    @classmethod
    def Sky_Watcher_Star_Discovery_200P(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Star_Discovery_200P'])

    @classmethod
    def Sky_Watcher_AZ_EQ5_GT_8_Newton(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_AZ_EQ5_GT_8_Newton'])

    @classmethod
    def Sky_Watcher_AZ_EQ6_Pro_8_Newton(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_AZ_EQ6_Pro_8_Newton'])

    @classmethod
    def Sky_Watcher_Black_Diamond_ED80(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Black_Diamond_ED80'])

    @classmethod
    def Sky_Watcher_Black_Diamond_ED100(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Black_Diamond_ED100'])

    @classmethod
    def Sky_Watcher_Black_Diamond_ED120(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Black_Diamond_ED120'])
