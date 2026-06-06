from ..base import GuideScope


class QHYGuideScope(GuideScope):
    _DATABASE = {'QHY_Mini_Guide_Scope_30mm': {'brand': 'QHY', 'name':
        'Mini Guide Scope 30mm', 'type': 'type_guide_scope',
        'optical_length': 0, 'mass': 130, 'tside_thread': '',
        'tside_gender': 'Male', 'cside_thread': 'CS', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''},
        'QHY_Mini_Guide_Scope_60mm': {'brand': 'QHY', 'name':
        'Mini Guide Scope 60mm', 'type': 'type_guide_scope',
        'optical_length': 0, 'mass': 320, 'tside_thread': '',
        'tside_gender': 'Male', 'cside_thread': 'M42', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def QHY_Mini_Guide_Scope_30mm(cls):
        return cls.from_database(cls._DATABASE['QHY_Mini_Guide_Scope_30mm'])

    @classmethod
    def QHY_Mini_Guide_Scope_60mm(cls):
        return cls.from_database(cls._DATABASE['QHY_Mini_Guide_Scope_60mm'])
