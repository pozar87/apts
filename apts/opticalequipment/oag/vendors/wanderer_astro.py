from ..base import OAG


class Wanderer_astroOAG(OAG):
    _DATABASE = {'Wanderer_Astro_OAG_M42': {'brand': 'Wanderer Astro',
        'name': 'OAG (M42)', 'type': 'type_oag', 'optical_length': 16,
        'mass': 170, 'tside_thread': 'M42', 'tside_gender': 'Female',
        'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False,
        'bf_role': ''}, 'Wanderer_Astro_OAG_M54': {'brand':
        'Wanderer Astro', 'name': 'OAG (M54)', 'type': 'type_oag',
        'optical_length': 19, 'mass': 280, 'tside_thread': 'M54',
        'tside_gender': 'Female', 'cside_thread': 'M54', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Wanderer_Astro_OAG_M42(cls):
        return cls.from_database(cls._DATABASE['Wanderer_Astro_OAG_M42'])

    @classmethod
    def Wanderer_Astro_OAG_M54(cls):
        return cls.from_database(cls._DATABASE['Wanderer_Astro_OAG_M54'])
