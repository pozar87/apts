from ..base import GuideScope


class TSOpticsGuideScope(GuideScope):
    _DATABASE = {'TS_Optics_50mm_Guide_Scope': {'brand': 'TS-Optics',
        'name': '50mm Guide Scope', 'type': 'type_guide_scope',
        'optical_length': 0, 'mass': 260, 'tside_thread': '',
        'tside_gender': 'Male', 'cside_thread': 'M42', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''},
        'TS_Optics_60mm_Guide_Scope': {'brand': 'TS-Optics', 'name':
        '60mm Guide Scope', 'type': 'type_guide_scope', 'optical_length': 0,
        'mass': 310, 'tside_thread': '', 'tside_gender': 'Male',
        'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False,
        'bf_role': ''}}

    @classmethod
    def TS_Optics_50mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_50mm_Guide_Scope'])

    @classmethod
    def TS_Optics_60mm_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE['TS_Optics_60mm_Guide_Scope'])
