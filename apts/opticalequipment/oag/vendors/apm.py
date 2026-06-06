from ..base import OAG


class ApmOAG(OAG):
    _DATABASE = {'APM_OAG_M48': {'brand': 'APM', 'name': 'OAG (M48)',
        'type': 'type_oag', 'optical_length': 17, 'mass': 200,
        'tside_thread': 'M48', 'tside_gender': 'Female', 'cside_thread':
        'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def APM_OAG_M48(cls):
        return cls.from_database(cls._DATABASE['APM_OAG_M48'])
