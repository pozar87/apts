from ..base import GuideScope


class ExploreScientificGuideScope(GuideScope):
    _DATABASE = {'Explore_Scientific_50mm_Guide_Scope': {'brand':
        'Explore Scientific', 'name': '50mm Guide Scope', 'type':
        'type_guide_scope', 'optical_length': 0, 'mass': 270,
        'tside_thread': '', 'tside_gender': 'Male', 'cside_thread': 'M42',
        'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Explore_Scientific_50mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE[
            'Explore_Scientific_50mm_Guide_Scope'])
