from ..base import GuideScope


class MeadeGuideScope(GuideScope):
    _DATABASE = {'Meade_50mm_Guide_Scope': {'brand': 'Meade', 'name':
        '50mm Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0,
        'mass': 270, 'tside_thread': '', 'tside_gender': 'Male',
        'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False,
        'bf_role': ''}, 'Meade_LX85_60mm_Guide_Scope': {'brand': 'Meade',
        'name': 'LX85 60mm Guide Scope', 'type': 'type_guide_scope',
        'optical_length': 0, 'mass': 320, 'tside_thread': '',
        'tside_gender': 'Male', 'cside_thread': 'M42', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Meade_50mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Meade_50mm_Guide_Scope'])

    @classmethod
    def Meade_LX85_60mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Meade_LX85_60mm_Guide_Scope'])
