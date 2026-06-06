from ..base import GuideScope


class StarlightXpressGuideScope(GuideScope):
    _DATABASE = {'Starlight_Xpress_Lodestar_Guide_Scope': {'brand':
        'Starlight Xpress', 'name': 'Lodestar Guide Scope', 'type':
        'type_guide_scope', 'optical_length': 0, 'mass': 300,
        'tside_thread': '', 'tside_gender': 'Male', 'cside_thread': 'M42',
        'cside_gender': 'Male', 'reversible': False, 'bf_role': ''},
        'Starlight_Xpress_SX_Guide_Scope_50mm': {'brand':
        'Starlight Xpress', 'name': 'SX Guide Scope 50mm', 'type':
        'type_guide_scope', 'optical_length': 0, 'mass': 280,
        'tside_thread': '', 'tside_gender': 'Male', 'cside_thread': 'M42',
        'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def Starlight_Xpress_Lodestar_Guide_Scope(cls):
        return cls.from_database(cls._DATABASE[
            'Starlight_Xpress_Lodestar_Guide_Scope'])

    @classmethod
    def Starlight_Xpress_SX_Guide_Scope_50mm(cls):
        return cls.from_database(cls._DATABASE[
            'Starlight_Xpress_SX_Guide_Scope_50mm'])
