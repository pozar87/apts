from ..base import Focuser


class WandererAstroFocuser(Focuser):
    _DATABASE = {
        "Wanderer_Astro_WandererFocuser": {'brand': 'Wanderer Astro', 'name': 'WandererFocuser', 'type': 'type_focuser', 'optical_length': 0, 'mass': 130, 'tside_thread': '', 'tside_gender': '', 'cside_thread': '', 'cside_gender': '', 'reversible': False, 'bf_role': ''},
    }

    @classmethod
    def Wanderer_Astro_WandererFocuser(cls):
        return cls.from_database(cls._DATABASE["Wanderer_Astro_WandererFocuser"])
