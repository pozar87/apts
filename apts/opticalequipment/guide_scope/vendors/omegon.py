from ..base import GuideScope


class OmegonGuideScope(GuideScope):
    _DATABASE = {'Omegon_50mm_Guide_Scope': {'brand': 'Omegon', 'name':
        '50mm Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0,
        'mass': 260, 'tside_thread': '', 'tside_gender': 'Male',
        'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False,
        'bf_role': ''}, 'Omegon_60mm_Guide_Scope': {'brand': 'Omegon',
        'name': '60mm Guide Scope', 'type': 'type_guide_scope',
        'optical_length': 0, 'mass': 310, 'tside_thread': '',
        'tside_gender': 'Male', 'cside_thread': 'M42', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Omegon_50mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Omegon_50mm_Guide_Scope'])

    @classmethod
    def Omegon_60mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Omegon_60mm_Guide_Scope'])
