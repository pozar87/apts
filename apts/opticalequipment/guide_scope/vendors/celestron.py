from ..base import GuideScope


class CelestronGuideScope(GuideScope):
    _DATABASE = {'Celestron_80mm_Guide_Scope': {'brand': 'Celestron',
        'name': '80mm Guide Scope', 'type': 'type_guide_scope',
        'optical_length': 0, 'mass': 650, 'tside_thread': '',
        'tside_gender': 'Male', 'cside_thread': 'M42', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''},
        'Celestron_50mm_Guide_Scope': {'brand': 'Celestron', 'name':
        '50mm Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0,
        'mass': 280, 'tside_thread': '', 'tside_gender': 'Male',
        'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False,
        'bf_role': ''}, 'Celestron_60mm_Guide_Scope': {'brand': 'Celestron',
        'name': '60mm Guide Scope', 'type': 'type_guide_scope',
        'optical_length': 0, 'mass': 340, 'tside_thread': '',
        'tside_gender': 'Male', 'cside_thread': 'M42', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Celestron_80mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Celestron_80mm_Guide_Scope'])

    @classmethod
    def Celestron_50mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Celestron_50mm_Guide_Scope'])

    @classmethod
    def Celestron_60mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['Celestron_60mm_Guide_Scope'])
