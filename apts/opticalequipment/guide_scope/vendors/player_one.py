from ..base import GuideScope


class PlayerOneGuideScope(GuideScope):
    _DATABASE = {'Player_One_Guide_Scope_30mm': {'brand': 'Player One',
        'name': 'Guide Scope 30mm', 'type': 'type_guide_scope',
        'optical_length': 0, 'mass': 120, 'tside_thread': '',
        'tside_gender': 'Male', 'cside_thread': 'CS', 'cside_gender':
        'Male', 'reversible': False, 'bf_role': ''},
        'Player_One_Guide_Scope_60mm': {'brand': 'Player One', 'name':
        'Guide Scope 60mm', 'type': 'type_guide_scope', 'optical_length': 0,
        'mass': 300, 'tside_thread': '', 'tside_gender': 'Male',
        'cside_thread': 'M42', 'cside_gender': 'Male', 'reversible': False,
        'bf_role': ''}}

    @classmethod
    def Player_One_Guide_Scope_30mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_Guide_Scope_30mm'])

    @classmethod
    def Player_One_Guide_Scope_60mm(cls):
        return cls.from_database(cls._DATABASE['Player_One_Guide_Scope_60mm'])
