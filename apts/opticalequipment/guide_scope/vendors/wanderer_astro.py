from ..base import GuideScope


class WandererAstroGuideScope(GuideScope):
    _DATABASE = {'Wanderer_Astro_Guide_Scope_30mm': {'brand':
        'Wanderer Astro', 'name': 'Guide Scope 30mm', 'type':
        'type_guide_scope', 'optical_length': 0, 'mass': 110,
        'tside_thread': '', 'tside_gender': 'Male', 'cside_thread': 'CS',
        'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Wanderer_Astro_Guide_Scope_50mm': {'brand': 'Wanderer Astro',
        'name': 'Guide Scope 50mm', 'type': 'type_guide_scope',
        'optical_length': 0, 'mass': 250, 'tside_thread': '',
        'tside_gender': 'Male', 'cside_thread': 'M42', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Wanderer_Astro_Guide_Scope_30mm(cls):
        return cls.from_database(cls._DATABASE[
            'Wanderer_Astro_Guide_Scope_30mm'])

    @classmethod
    def Wanderer_Astro_Guide_Scope_50mm(cls):
        return cls.from_database(cls._DATABASE[
            'Wanderer_Astro_Guide_Scope_50mm'])
