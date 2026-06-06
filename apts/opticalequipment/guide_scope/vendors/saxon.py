from ..base import GuideScope


class SaxonGuideScope(GuideScope):
    _DATABASE = {'Saxon_Guide_Scope_50mm': {'brand': 'Saxon', 'name':
        'Guide Scope 50mm', 'type': 'type_guide_scope', 'optical_length': 0,
        'mass': 250, 'tside_thread': '', 'tside_gender': 'Male',
        'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False,
        'bf_role': ''}}

    @classmethod
    def Saxon_Guide_Scope_50mm(cls):
        return cls.from_database(cls._DATABASE['Saxon_Guide_Scope_50mm'])
