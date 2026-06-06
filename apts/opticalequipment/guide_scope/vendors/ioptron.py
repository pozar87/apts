from ..base import GuideScope


class iOptronGuideScope(GuideScope):
    _DATABASE = {'iOptron_iGuide_60mm': {'brand': 'iOptron', 'name':
        'iGuide 60mm', 'type': 'type_guide_scope', 'optical_length': 0,
        'mass': 320, 'tside_thread': '', 'tside_gender': 'Male',
        'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False,
        'bf_role': ''}, 'iOptron_Guide_Scope_30mm': {'brand': 'iOptron',
        'name': 'Guide Scope 30mm', 'type': 'type_guide_scope',
        'optical_length': 0, 'mass': 120, 'tside_thread': '',
        'tside_gender': 'Male', 'cside_thread': 'CS', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''},
        'iOptron_Guide_Scope_60mm': {'brand': 'iOptron', 'name':
        'Guide Scope 60mm', 'type': 'type_guide_scope', 'optical_length': 0,
        'mass': 310, 'tside_thread': '', 'tside_gender': 'Male',
        'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False,
        'bf_role': ''}}

    @classmethod
    def iOptron_iGuide_60mm(cls):
        return cls.from_database(cls._DATABASE['iOptron_iGuide_60mm'])

    @classmethod
    def iOptron_Guide_Scope_30mm(cls):
        return cls.from_database(cls._DATABASE['iOptron_Guide_Scope_30mm'])

    @classmethod
    def iOptron_Guide_Scope_60mm(cls):
        return cls.from_database(cls._DATABASE['iOptron_Guide_Scope_60mm'])
