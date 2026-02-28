from ..base import Telescope

class Sky_watcherTelescope(Telescope):
    _DATABASE = {
        'Sky_Watcher_Esprit_80ED': {'brand': 'Sky-Watcher', 'name': 'Esprit 80ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3970, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 80, 'focal_length_mm': 400, 'central_obstruction_mm': 0}, # Verified via Sky-Watcher official specs (3.97 kg tube) https://www.skywatcher.com/product/esprit-80ed-apo-triplet/
        'Sky_Watcher_Esprit_100ED': {'brand': 'Sky-Watcher', 'name': 'Esprit 100ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 6300, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 100, 'focal_length_mm': 550, 'central_obstruction_mm': 0}, # Verified via Sky-Watcher official specs (6.3 kg tube) https://www.skywatcher.com/product/esprit-100-ed-apo-triplet/
        'Sky_Watcher_Esprit_120ED': {'brand': 'Sky-Watcher', 'name': 'Esprit 120ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 9610, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 120, 'focal_length_mm': 840, 'central_obstruction_mm': 0}, # Verified via Sky-Watcher official specs (9.61 kg tube) http://skywatcher.com/product/esprit-120ed-apo-triplet/
        'Sky_Watcher_Esprit_150ED': {'brand': 'Sky-Watcher', 'name': 'Esprit 150ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 14520, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 150, 'focal_length_mm': 1050, 'central_obstruction_mm': 0}, # Verified via Sky-Watcher official specs (14.52 kg tube) http://skywatcher.com/product/esprit-150ed-apo-triplet/
        'Sky_Watcher_Evostar_72ED': {'brand': 'Sky-Watcher', 'name': 'Evostar 72ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 1900, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Evostar_80ED': {'brand': 'Sky-Watcher', 'name': 'Evostar 80ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Evostar_100ED': {'brand': 'Sky-Watcher', 'name': 'Evostar 100ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Evostar_120ED': {'brand': 'Sky-Watcher', 'name': 'Evostar 120ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 5400, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Evostar_72ED_DS_Pro': {'brand': 'Sky-Watcher', 'name': 'Evostar 72ED DS-Pro', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Evostar_80ED_DS_Pro': {'brand': 'Sky-Watcher', 'name': 'Evostar 80ED DS-Pro', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Evostar_100ED_DS_Pro': {'brand': 'Sky-Watcher', 'name': 'Evostar 100ED DS-Pro', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Evostar_150ED': {'brand': 'Sky-Watcher', 'name': 'Evostar 150ED', 'type': 'type_refractor', 'optical_length': 0, 'mass': 8000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M54', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Quattro_150P': {'brand': 'Sky-Watcher', 'name': 'Quattro 150P', 'type': 'type_telescope', 'optical_length': 0, 'mass': 5000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Quattro_200P': {'brand': 'Sky-Watcher', 'name': 'Quattro 200P', 'type': 'type_telescope', 'optical_length': 0, 'mass': 8000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Quattro_250P': {'brand': 'Sky-Watcher', 'name': 'Quattro 250P', 'type': 'type_telescope', 'optical_length': 0, 'mass': 12000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Quattro_300P': {'brand': 'Sky-Watcher', 'name': 'Quattro 300P', 'type': 'type_telescope', 'optical_length': 0, 'mass': 16000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_150PDS_Newtonian': {'brand': 'Sky-Watcher', 'name': '150PDS Newtonian', 'type': 'type_telescope', 'optical_length': 0, 'mass': 4800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_200PDS_Newtonian': {'brand': 'Sky-Watcher', 'name': '200PDS Newtonian', 'type': 'type_telescope', 'optical_length': 0, 'mass': 8800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_250PDS_Newtonian': {'brand': 'Sky-Watcher', 'name': '250PDS Newtonian', 'type': 'type_telescope', 'optical_length': 0, 'mass': 11500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Explorer_130P': {'brand': 'Sky-Watcher', 'name': 'Explorer 130P', 'type': 'type_telescope', 'optical_length': 0, 'mass': 3200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Explorer_150P': {'brand': 'Sky-Watcher', 'name': 'Explorer 150P', 'type': 'type_telescope', 'optical_length': 0, 'mass': 5200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Explorer_200P': {'brand': 'Sky-Watcher', 'name': 'Explorer 200P', 'type': 'type_telescope', 'optical_length': 0, 'mass': 8500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Explorer_250P': {'brand': 'Sky-Watcher', 'name': 'Explorer 250P', 'type': 'type_telescope', 'optical_length': 0, 'mass': 11000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Explorer_300P': {'brand': 'Sky-Watcher', 'name': 'Explorer 300P', 'type': 'type_telescope', 'optical_length': 0, 'mass': 16000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Skyliner_150P': {'brand': 'Sky-Watcher', 'name': 'Skyliner 150P', 'type': 'type_telescope', 'optical_length': 0, 'mass': 5000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Skyliner_200P': {'brand': 'Sky-Watcher', 'name': 'Skyliner 200P', 'type': 'type_telescope', 'optical_length': 0, 'mass': 8500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Skyliner_250P': {'brand': 'Sky-Watcher', 'name': 'Skyliner 250P', 'type': 'type_telescope', 'optical_length': 0, 'mass': 11600, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Skyliner_300P': {'brand': 'Sky-Watcher', 'name': 'Skyliner 300P', 'type': 'type_telescope', 'optical_length': 0, 'mass': 16000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Skyliner_400P': {'brand': 'Sky-Watcher', 'name': 'Skyliner 400P', 'type': 'type_telescope', 'optical_length': 0, 'mass': 25000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Heritage_130P': {'brand': 'Sky-Watcher', 'name': 'Heritage 130P', 'type': 'type_telescope', 'optical_length': 0, 'mass': 3000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Heritage_150P': {'brand': 'Sky-Watcher', 'name': 'Heritage 150P', 'type': 'type_telescope', 'optical_length': 0, 'mass': 4500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Mak_90': {'brand': 'Sky-Watcher', 'name': 'Mak-90', 'type': 'type_telescope', 'optical_length': 0, 'mass': 1600, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Mak_102': {'brand': 'Sky-Watcher', 'name': 'Mak-102', 'type': 'type_telescope', 'optical_length': 0, 'mass': 2000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Mak_127': {'brand': 'Sky-Watcher', 'name': 'Mak-127', 'type': 'type_telescope', 'optical_length': 0, 'mass': 3500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Mak_150': {'brand': 'Sky-Watcher', 'name': 'Mak-150', 'type': 'type_telescope', 'optical_length': 0, 'mass': 5000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Mak_180': {'brand': 'Sky-Watcher', 'name': 'Mak-180', 'type': 'type_telescope', 'optical_length': 0, 'mass': 6300, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Heritage_76_Mini': {'brand': 'Sky-Watcher', 'name': 'Heritage 76 Mini', 'type': 'type_telescope', 'optical_length': 0, 'mass': 1600, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Heritage_100P': {'brand': 'Sky-Watcher', 'name': 'Heritage 100P', 'type': 'type_telescope', 'optical_length': 0, 'mass': 2200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Heritage_130P_FlexTube': {'brand': 'Sky-Watcher', 'name': 'Heritage 130P FlexTube', 'type': 'type_telescope', 'optical_length': 0, 'mass': 3200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Heritage_150P_FlexTube': {'brand': 'Sky-Watcher', 'name': 'Heritage 150P FlexTube', 'type': 'type_telescope', 'optical_length': 0, 'mass': 4800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Star_Discovery_130i': {'brand': 'Sky-Watcher', 'name': 'Star Discovery 130i', 'type': 'type_telescope', 'optical_length': 0, 'mass': 3300, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Star_Discovery_150i': {'brand': 'Sky-Watcher', 'name': 'Star Discovery 150i', 'type': 'type_telescope', 'optical_length': 0, 'mass': 5000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Starquest_130P': {'brand': 'Sky-Watcher', 'name': 'Starquest 130P', 'type': 'type_telescope', 'optical_length': 0, 'mass': 3200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Virtuoso_GTi_130P': {'brand': 'Sky-Watcher', 'name': 'Virtuoso GTi 130P', 'type': 'type_telescope', 'optical_length': 0, 'mass': 3300, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Virtuoso_GTi_150P': {'brand': 'Sky-Watcher', 'name': 'Virtuoso GTi 150P', 'type': 'type_telescope', 'optical_length': 0, 'mass': 4800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Star_Adventurer_GTi_80ED': {'brand': 'Sky-Watcher', 'name': 'Star Adventurer GTi 80ED', 'type': 'type_telescope', 'optical_length': 0, 'mass': 2600, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Starquest_80MC': {'brand': 'Sky-Watcher', 'name': 'Starquest 80MC', 'type': 'type_telescope', 'optical_length': 0, 'mass': 1800, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Heritage_P130_FlexTube': {'brand': 'Sky-Watcher', 'name': 'Heritage P130 FlexTube', 'type': 'type_telescope', 'optical_length': 0, 'mass': 3100, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Skyliner_200P_FlexTube': {'brand': 'Sky-Watcher', 'name': 'Skyliner 200P FlexTube', 'type': 'type_telescope', 'optical_length': 0, 'mass': 8600, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Skyliner_250P_FlexTube': {'brand': 'Sky-Watcher', 'name': 'Skyliner 250P FlexTube', 'type': 'type_telescope', 'optical_length': 0, 'mass': 11700, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Skyliner_300P_FlexTube': {'brand': 'Sky-Watcher', 'name': 'Skyliner 300P FlexTube', 'type': 'type_telescope', 'optical_length': 0, 'mass': 16200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Skyliner_350P_FlexTube': {'brand': 'Sky-Watcher', 'name': 'Skyliner 350P FlexTube', 'type': 'type_telescope', 'optical_length': 0, 'mass': 19000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Stargate_500P_Truss_Dob': {'brand': 'Sky-Watcher', 'name': 'Stargate 500P Truss Dob', 'type': 'type_telescope', 'optical_length': 0, 'mass': 35000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Stargate_450P_Truss_Dob': {'brand': 'Sky-Watcher', 'name': 'Stargate 450P Truss Dob', 'type': 'type_telescope', 'optical_length': 0, 'mass': 28000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Evostar_150DX': {'brand': 'Sky-Watcher', 'name': 'Evostar 150DX', 'type': 'type_refractor', 'optical_length': 0, 'mass': 8000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Equinox_80': {'brand': 'Sky-Watcher', 'name': 'Equinox 80', 'type': 'type_refractor', 'optical_length': 0, 'mass': 3000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Equinox_100': {'brand': 'Sky-Watcher', 'name': 'Equinox 100', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Equinox_120': {'brand': 'Sky-Watcher', 'name': 'Equinox 120', 'type': 'type_refractor', 'optical_length': 0, 'mass': 6500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_SkyMax_102': {'brand': 'Sky-Watcher', 'name': 'SkyMax 102', 'type': 'type_telescope', 'optical_length': 0, 'mass': 2200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_SkyMax_127': {'brand': 'Sky-Watcher', 'name': 'SkyMax 127', 'type': 'type_telescope', 'optical_length': 0, 'mass': 3400, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_SkyMax_150_Pro': {'brand': 'Sky-Watcher', 'name': 'SkyMax 150 Pro', 'type': 'type_telescope', 'optical_length': 0, 'mass': 5200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_SkyMax_180_Pro': {'brand': 'Sky-Watcher', 'name': 'SkyMax 180 Pro', 'type': 'type_telescope', 'optical_length': 0, 'mass': 6500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'SC (Schmidt-Cassegrain)', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Traditional_Dob_6': {'brand': 'Sky-Watcher', 'name': 'Traditional Dob 6"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 5000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Traditional_Dob_8': {'brand': 'Sky-Watcher', 'name': 'Traditional Dob 8"', 'type': 'newtonian_reflector', 'optical_length': 0, 'mass': 9070, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': '', 'aperture_mm': 203.2, 'focal_length_mm': 1200, 'central_obstruction_mm': 47}, # Verified via Sky-Watcher official specs (9.07 kg OTA),
        'Sky_Watcher_Traditional_Dob_10': {'brand': 'Sky-Watcher', 'name': 'Traditional Dob 10"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 10000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Traditional_Dob_12': {'brand': 'Sky-Watcher', 'name': 'Traditional Dob 12"', 'type': 'type_telescope', 'optical_length': 0, 'mass': 13500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_SkyMax_90': {'brand': 'Sky-Watcher', 'name': 'SkyMax 90', 'type': 'type_telescope', 'optical_length': 0, 'mass': 1500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '1.25"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_SkyMax_102_AZ_GTi': {'brand': 'Sky-Watcher', 'name': 'SkyMax 102 AZ-GTi', 'type': 'type_telescope', 'optical_length': 0, 'mass': 2200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_SkyMax_127_AZ_GTi': {'brand': 'Sky-Watcher', 'name': 'SkyMax 127 AZ-GTi', 'type': 'type_telescope', 'optical_length': 0, 'mass': 3400, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Star_Discovery_150P': {'brand': 'Sky-Watcher', 'name': 'Star Discovery 150P', 'type': 'type_telescope', 'optical_length': 0, 'mass': 5000, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Star_Discovery_200P': {'brand': 'Sky-Watcher', 'name': 'Star Discovery 200P', 'type': 'type_telescope', 'optical_length': 0, 'mass': 8200, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_AZ_EQ5_GT_8_Newton': {'brand': 'Sky-Watcher', 'name': 'AZ-EQ5 GT 8" Newton', 'type': 'type_telescope', 'optical_length': 0, 'mass': 8500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_AZ_EQ6_Pro_8_Newton': {'brand': 'Sky-Watcher', 'name': 'AZ-EQ6 Pro 8" Newton', 'type': 'type_telescope', 'optical_length': 0, 'mass': 8600, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '2"', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Black_Diamond_ED80': {'brand': 'Sky-Watcher', 'name': 'Black Diamond ED80', 'type': 'type_refractor', 'optical_length': 0, 'mass': 2600, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Black_Diamond_ED100': {'brand': 'Sky-Watcher', 'name': 'Black Diamond ED100', 'type': 'type_refractor', 'optical_length': 0, 'mass': 4300, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}, 'Sky_Watcher_Black_Diamond_ED120': {'brand': 'Sky-Watcher', 'name': 'Black Diamond ED120', 'type': 'type_refractor', 'optical_length': 0, 'mass': 6500, 'tside_thread': '', 'tside_gender': '', 'cside_thread': 'M48', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}
        'Sky_Watcher_150PDS_Newtonian': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 4800,
         'name': '150PDS Newtonian',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_200PDS_Newtonian': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 8800,
         'name': '200PDS Newtonian',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_250PDS_Newtonian': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 11500,
         'name': '250PDS Newtonian',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_AZ_EQ5_GT_8_Newton': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 8500,
         'name': 'AZ-EQ5 GT 8" Newton',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_AZ_EQ6_Pro_8_Newton': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 8600,
         'name': 'AZ-EQ6 Pro 8" Newton',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Black_Diamond_ED100': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': 'M48',
         'mass': 4300,
         'name': 'Black Diamond ED100',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_refractor'},
        'Sky_Watcher_Black_Diamond_ED120': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': 'M48',
         'mass': 6500,
         'name': 'Black Diamond ED120',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_refractor'},
        'Sky_Watcher_Black_Diamond_ED80': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': 'M48',
         'mass': 2600,
         'name': 'Black Diamond ED80',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_refractor'},
        'Sky_Watcher_Equinox_100': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': 'M48',
         'mass': 4500,
         'name': 'Equinox 100',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_refractor'},
        'Sky_Watcher_Equinox_120': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': 'M48',
         'mass': 6500,
         'name': 'Equinox 120',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_refractor'},
        'Sky_Watcher_Equinox_80': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': 'M48',
         'mass': 3000,
         'name': 'Equinox 80',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_refractor'},
        'Sky_Watcher_Esprit_100ED': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': 'M48',
         'mass': 5400,
         'name': 'Esprit 100ED',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_refractor'},
        'Sky_Watcher_Esprit_120ED': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': 'M48',
         'mass': 7800,
         'name': 'Esprit 120ED',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_refractor'},
        'Sky_Watcher_Esprit_150ED': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': 'M54',
         'mass': 12000,
         'name': 'Esprit 150ED',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_refractor'},
        'Sky_Watcher_Esprit_80ED': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': 'M48',
         'mass': 4000,
         'name': 'Esprit 80ED',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_refractor'},
        'Sky_Watcher_Evostar_100ED': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': 'M48',
         'mass': 4200,
         'name': 'Evostar 100ED',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_refractor'},
        'Sky_Watcher_Evostar_100ED_DS_Pro': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': 'M48',
         'mass': 4500,
         'name': 'Evostar 100ED DS-Pro',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_refractor'},
        'Sky_Watcher_Evostar_120ED': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': 'M48',
         'mass': 5400,
         'name': 'Evostar 120ED',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_refractor'},
        'Sky_Watcher_Evostar_150DX': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': 'M48',
         'mass': 8000,
         'name': 'Evostar 150DX',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_refractor'},
        'Sky_Watcher_Evostar_150ED': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': 'M54',
         'mass': 8000,
         'name': 'Evostar 150ED',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_refractor'},
        'Sky_Watcher_Evostar_72ED': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': 'M48',
         'mass': 1900,
         'name': 'Evostar 72ED',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_refractor'},
        'Sky_Watcher_Evostar_72ED_DS_Pro': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': 'M48',
         'mass': 2200,
         'name': 'Evostar 72ED DS-Pro',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_refractor'},
        'Sky_Watcher_Evostar_80ED': {'aperture_mm': 80,
         'bf_role': '',
         'brand': 'Sky-Watcher',
         'central_obstruction_mm': 0,
         'cside_gender': 'Male',
         'cside_thread': 'M48',
         'focal_length_mm': 600,
         'mass': 2470,
         'name': 'Evostar 80ED',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_refractor'},  # Verified via Sky-Watcher official specs (2.47 kg OTA) http://skywatcher.com/product/bk-80ed-otaw/
        'Sky_Watcher_Evostar_80ED_DS_Pro': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': 'M48',
         'mass': 2800,
         'name': 'Evostar 80ED DS-Pro',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_refractor'},
        'Sky_Watcher_Explorer_130P': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 3200,
         'name': 'Explorer 130P',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Explorer_150P': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 5200,
         'name': 'Explorer 150P',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Explorer_200P': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 8500,
         'name': 'Explorer 200P',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Explorer_250P': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 11000,
         'name': 'Explorer 250P',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Explorer_300P': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 16000,
         'name': 'Explorer 300P',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Heritage_100P': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '1.25"',
         'mass': 2200,
         'name': 'Heritage 100P',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Heritage_130P': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 3000,
         'name': 'Heritage 130P',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Heritage_130P_FlexTube': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 3200,
         'name': 'Heritage 130P FlexTube',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Heritage_150P': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 4500,
         'name': 'Heritage 150P',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Heritage_150P_FlexTube': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 4800,
         'name': 'Heritage 150P FlexTube',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Heritage_76_Mini': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '1.25"',
         'mass': 1600,
         'name': 'Heritage 76 Mini',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Heritage_P130_FlexTube': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 3100,
         'name': 'Heritage P130 FlexTube',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Mak_102': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '1.25"',
         'mass': 2000,
         'name': 'Mak-102',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Mak_127': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '1.25"',
         'mass': 3500,
         'name': 'Mak-127',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Mak_150': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 5000,
         'name': 'Mak-150',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Mak_180': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 6300,
         'name': 'Mak-180',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Mak_90': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '1.25"',
         'mass': 1600,
         'name': 'Mak-90',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Quattro_150P': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': 'M48',
         'mass': 5000,
         'name': 'Quattro 150P',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Quattro_200P': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': 'M48',
         'mass': 8000,
         'name': 'Quattro 200P',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Quattro_250P': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': 'M48',
         'mass': 12000,
         'name': 'Quattro 250P',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Quattro_300P': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': 'M48',
         'mass': 16000,
         'name': 'Quattro 300P',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_SkyMax_102': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '1.25"',
         'mass': 2200,
         'name': 'SkyMax 102',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_SkyMax_102_AZ_GTi': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 2200,
         'name': 'SkyMax 102 AZ-GTi',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_SkyMax_127': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '1.25"',
         'mass': 3400,
         'name': 'SkyMax 127',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_SkyMax_127_AZ_GTi': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 3400,
         'name': 'SkyMax 127 AZ-GTi',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_SkyMax_150_Pro': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': 'SC (Schmidt-Cassegrain)',
         'mass': 5200,
         'name': 'SkyMax 150 Pro',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_SkyMax_180_Pro': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': 'SC (Schmidt-Cassegrain)',
         'mass': 6500,
         'name': 'SkyMax 180 Pro',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_SkyMax_90': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '1.25"',
         'mass': 1500,
         'name': 'SkyMax 90',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Skyliner_150P': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 5000,
         'name': 'Skyliner 150P',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Skyliner_200P': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 8500,
         'name': 'Skyliner 200P',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Skyliner_200P_FlexTube': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 8600,
         'name': 'Skyliner 200P FlexTube',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Skyliner_250P': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 11600,
         'name': 'Skyliner 250P',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Skyliner_250P_FlexTube': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 11700,
         'name': 'Skyliner 250P FlexTube',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Skyliner_300P': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 16000,
         'name': 'Skyliner 300P',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Skyliner_300P_FlexTube': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 16200,
         'name': 'Skyliner 300P FlexTube',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Skyliner_350P_FlexTube': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 19000,
         'name': 'Skyliner 350P FlexTube',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Skyliner_400P': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 25000,
         'name': 'Skyliner 400P',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Star_Adventurer_GTi_80ED': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 2600,
         'name': 'Star Adventurer GTi 80ED',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Star_Discovery_130i': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 3300,
         'name': 'Star Discovery 130i',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Star_Discovery_150P': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 5000,
         'name': 'Star Discovery 150P',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Star_Discovery_150i': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 5000,
         'name': 'Star Discovery 150i',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Star_Discovery_200P': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 8200,
         'name': 'Star Discovery 200P',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Stargate_450P_Truss_Dob': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 28000,
         'name': 'Stargate 450P Truss Dob',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Stargate_500P_Truss_Dob': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 35000,
         'name': 'Stargate 500P Truss Dob',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Starquest_130P': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 3200,
         'name': 'Starquest 130P',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Starquest_80MC': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 1800,
         'name': 'Starquest 80MC',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Traditional_Dob_10': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 10000,
         'name': 'Traditional Dob 10"',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Traditional_Dob_12': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 13500,
         'name': 'Traditional Dob 12"',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Traditional_Dob_6': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 5000,
         'name': 'Traditional Dob 6"',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Traditional_Dob_8': {'aperture_mm': 203.2,
         'bf_role': '',
         'brand': 'Sky-Watcher',
         'central_obstruction_mm': 47,
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'focal_length_mm': 1200,
         'mass': 9070,
         'name': 'Traditional Dob 8"',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'newtonian_reflector'},  # Verified via Sky-Watcher official specs (9.07 kg OTA)
        'Sky_Watcher_Virtuoso_GTi_130P': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 3300,
         'name': 'Virtuoso GTi 130P',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
        'Sky_Watcher_Virtuoso_GTi_150P': {'bf_role': '',
         'brand': 'Sky-Watcher',
         'cside_gender': 'Male',
         'cside_thread': '2"',
         'mass': 4800,
         'name': 'Virtuoso GTi 150P',
         'optical_length': 0,
         'reversible': False,
         'tside_gender': '',
         'tside_thread': '',
         'type': 'type_telescope'},
    }

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
    def Sky_Watcher_Star_Adventurer_GTi_80ED(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Star_Adventurer_GTi_80ED'])

    @classmethod
    def Sky_Watcher_Starquest_80MC(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Starquest_80MC'])

    @classmethod
    def Sky_Watcher_Heritage_P130_FlexTube(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Heritage_P130_FlexTube'])

    @classmethod
    def Sky_Watcher_Skyliner_200P_FlexTube(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Skyliner_200P_FlexTube'])

    @classmethod
    def Sky_Watcher_Skyliner_250P_FlexTube(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Skyliner_250P_FlexTube'])

    @classmethod
    def Sky_Watcher_Skyliner_300P_FlexTube(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Skyliner_300P_FlexTube'])

    @classmethod
    def Sky_Watcher_Skyliner_350P_FlexTube(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Skyliner_350P_FlexTube'])

    @classmethod
    def Sky_Watcher_Stargate_500P_Truss_Dob(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Stargate_500P_Truss_Dob'])

    @classmethod
    def Sky_Watcher_Stargate_450P_Truss_Dob(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Stargate_450P_Truss_Dob'])

    @classmethod
    def Sky_Watcher_Evostar_150DX(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Evostar_150DX'])

    @classmethod
    def Sky_Watcher_Equinox_80(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Equinox_80'])

    @classmethod
    def Sky_Watcher_Equinox_100(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Equinox_100'])

    @classmethod
    def Sky_Watcher_Equinox_120(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Equinox_120'])

    @classmethod
    def Sky_Watcher_SkyMax_102(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_SkyMax_102'])

    @classmethod
    def Sky_Watcher_SkyMax_127(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_SkyMax_127'])

    @classmethod
    def Sky_Watcher_SkyMax_150_Pro(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_SkyMax_150_Pro'])

    @classmethod
    def Sky_Watcher_SkyMax_180_Pro(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_SkyMax_180_Pro'])

    @classmethod
    def Sky_Watcher_Traditional_Dob_6(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Traditional_Dob_6'])

    @classmethod
    def Sky_Watcher_Traditional_Dob_8(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Traditional_Dob_8'])

    @classmethod
    def Sky_Watcher_Traditional_Dob_10(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Traditional_Dob_10'])

    @classmethod
    def Sky_Watcher_Traditional_Dob_12(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_Traditional_Dob_12'])

    @classmethod
    def Sky_Watcher_SkyMax_90(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_SkyMax_90'])

    @classmethod
    def Sky_Watcher_SkyMax_102_AZ_GTi(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_SkyMax_102_AZ_GTi'])

    @classmethod
    def Sky_Watcher_SkyMax_127_AZ_GTi(cls):
        return cls.from_database(cls._DATABASE['Sky_Watcher_SkyMax_127_AZ_GTi'])

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
