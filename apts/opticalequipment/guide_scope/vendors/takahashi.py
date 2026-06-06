from ..base import GuideScope


class TakahashiGuideScope(GuideScope):
    _DATABASE = {'Takahashi_GT_40_Guide_Scope': {'brand': 'Takahashi',
        'name': 'GT-40 Guide Scope', 'type': 'type_guide_scope',
        'optical_length': 0, 'mass': 250, 'tside_thread': '',
        'tside_gender': 'Male', 'cside_thread': 'M42', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Takahashi_GT_40_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Takahashi_GT_40_Guide_Scope'])
