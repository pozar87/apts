from ..base import GuideScope


class SVBonyGuideScope(GuideScope):
    _DATABASE = {'SVBony_SV106_50mm_Guide_Scope': {'brand': 'SVBony',
        'name': 'SV106 50mm Guide Scope', 'type': 'type_guide_scope',
        'optical_length': 0, 'mass': 250, 'tside_thread': '',
        'tside_gender': 'Male', 'cside_thread': 'M42', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''},
        'SVBony_SV165_30mm_Guide_Scope': {'brand': 'SVBony', 'name':
        'SV165 30mm Guide Scope', 'type': 'type_guide_scope',
        'optical_length': 0, 'mass': 120, 'tside_thread': '',
        'tside_gender': 'Male', 'cside_thread': 'CS', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''},
        'SVBony_SV106_60mm_Guide_Scope': {'brand': 'SVBony', 'name':
        'SV106 60mm Guide Scope', 'type': 'type_guide_scope',
        'optical_length': 0, 'mass': 300, 'tside_thread': '',
        'tside_gender': 'Male', 'cside_thread': 'M42', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''},
        'SVBony_SV210_30mm_Guide_Scope': {'brand': 'SVBony', 'name':
        'SV210 30mm Guide Scope', 'type': 'type_guide_scope',
        'optical_length': 0, 'mass': 100, 'tside_thread': '',
        'tside_gender': 'Male', 'cside_thread': 'CS', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''},
        'SVBony_SV48P_Guide_Scope': {'brand': 'SVBony', 'name':
        'SV48P Guide Scope', 'type': 'type_guide_scope', 'optical_length': 
        0, 'mass': 250, 'tside_thread': '', 'tside_gender': 'Male',
        'cside_thread': 'CS', 'cside_gender': 'Male', 'reversible': False,
        'bf_role': ''}, 'SVBony_SV106_Guide_60mm': {'brand': 'SVBony',
        'name': 'SV106 Guide 60mm', 'type': 'type_guide_scope',
        'optical_length': 0, 'mass': 300, 'tside_thread': '',
        'tside_gender': 'Male', 'cside_thread': 'M42', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def SVBony_SV106_50mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV106_50mm_Guide_Scope']
            )

    @classmethod
    def SVBony_SV165_30mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV165_30mm_Guide_Scope']
            )

    @classmethod
    def SVBony_SV106_60mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV106_60mm_Guide_Scope']
            )

    @classmethod
    def SVBony_SV210_30mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV210_30mm_Guide_Scope']
            )

    @classmethod
    def SVBony_SV48P_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV48P_Guide_Scope'])

    @classmethod
    def SVBony_SV106_Guide_60mm(cls):
        return cls.from_database(cls._DATABASE['SVBony_SV106_Guide_60mm'])
