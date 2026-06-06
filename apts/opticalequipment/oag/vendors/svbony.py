from ..base import OAG


class SvbonyOAG(OAG):
    _DATABASE = {'SVBony_OAG_M42': {'brand': 'SVBony', 'name': 'OAG (M42)',
        'type': 'type_oag', 'optical_length': 15, 'mass': 150,
        'tside_thread': 'M42', 'tside_gender': 'Female', 'cside_thread':
        'M42', 'cside_gender': 'Male', 'reversible': False, 'bf_role': ''}}

    @classmethod
    def SVBony_OAG_M42(cls):
        return cls.from_database(cls._DATABASE['SVBony_OAG_M42'])
